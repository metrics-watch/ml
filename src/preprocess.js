const moment = require("moment");
const requesttime = /[\w\W]*?\/(\d+) [\w\W]*/;
const cleanpath = /\/TOKEN\/[0-9a-z]*?\/(.*)/;
const matchbarcode = /[0-9]/g;
const matchweirdchar = /\%C/g;

const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: fs.createReadStream("data/sample.json"),
  crlfDelay: Infinity
});

const entries = [];
const fd = {};

rl.on("line", line => entries.push(JSON.parse(line)));

const preprocess = entries =>
  entries
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
      url: cleanpath
        .exec(event.url)[1]
        .replace(matchbarcode, "")
        .replace(matchweirdchar, ""),
      responsetime: Number.parseInt(requesttime.exec(event._raw)[1], 10)
    }))
    .filter(event => event.url !== "LOCATION");

rl.once("close", () => {
  const events = preprocess(entries);
  events.filter((_, i) => i % 2 === 0).forEach(event => {
    const name = filenamesmall(event);
    fs.appendFileSync(name, JSON.stringify(event) + "\n");
  });

  events.forEach(event => {
    const name = filenamebig(event);
    fs.appendFileSync(name, JSON.stringify(event) + "\n");
  });
});

const filenamesmall = event =>
  `data/small/${event.datetime.format("YYYY-MM-DD")}.json`;
const filenamebig = event =>
  `data/big/${event.datetime.format("YYYY-MM-DD")}.json`;
