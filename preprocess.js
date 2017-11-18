const fs = require("fs");
const readline = require("readline");
const moment = require("moment");
const inputpath = "./data/sample.json";
const preoutputpath = "./data/sample_pre_grid.json";
const postoutputpath = "./data/sample_post_grid.json";
const requesttime = /[\w\W]*?\/(\d+) [\w\W]*/;
const cleanpath = /\/TOKEN\/[0-9a-z]*?\/(.*)/;

const rl = readline.createInterface({ input: fs.createReadStream(inputpath) });
const preoutput = fs.createWriteStream(preoutputpath);
const postoutput = fs.createWriteStream(postoutputpath);

const entries = [];

rl.on("line", data => {
  const entry = JSON.parse(data);
  entries.push(entry);
});

rl.on("close", () => {
  const events = entries
    .map(entry => entry.result)
    .filter(entry => entry.url)
    .filter(entry => entry.url.indexOf("/TOKEN/") === 0)
    .map(event => ({
      method: event.method,
      status: Number.parseInt(event.status_code, 10),
      minuteofday:
        moment(event._time).hour() * 60 + moment(event._time).minute(),
      dayofweek: moment(event._time).day(),
      datetime: moment(event._time),
      url: cleanpath.exec(event.url)[1],
      responsetime: Number.parseInt(requesttime.exec(event._raw)[1], 10)
    }))
    .filter(event => event.url === "GRID");

  events
    .filter(event => event.datetime.isBefore("2017-11-01"))
    .forEach(event => preoutput.write(JSON.stringify(event) + "\n"));

  events
    .filter(event => event.datetime.isBetween("2017-11-01", "2017-11-09"))
    .forEach(event => postoutput.write(JSON.stringify(event) + "\n"));

  preoutput.end();
  postoutput.end();
});
