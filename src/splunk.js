const splunkjs = require("splunk-sdk");

const service = new splunkjs.Service();

service.login((err, success) => {
  if (err) {
    throw err;
  }
  // TODO 
  Splunk.get(
    source,
    "sourcetype= earliest=-200m latest=-140m",
    function(rows) {
      //console.log("rows", rows);
      if (rows && rows.length) {
        commitDataToApi(rows);
      }
      res.send(rows);
    }
  );
});
