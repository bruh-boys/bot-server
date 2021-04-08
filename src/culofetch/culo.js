const si = require("systeminformation");
const chalk = require("chalk");
const figlet = require("figlet");

si.cpu()
  .then((data) => {
    console.log("CPU Information:");
    console.log(`- manufacturer: ${data.manufacturer}`);
    console.log(`- brand: ${data.brand}`);
    console.log(`- speed: ${data.speed}`);
    console.log(`- threads: ${data.cores}`);
    console.log(`- cores: ${data.physicalCores}`);
  })
  .catch((error) => console.error(error));

si.cpuTemperature()
  .then((data) => {
    console.log("CPU temperature");
    console.log(`- temperature: ${data.main}`);
  })
  .catch((error) => console.error(error));

si.mem()
  .then((data) => {
    console.log("RAM information: ");
    console.log(`- total memory: ${data.total}`);
    console.log(`- memory used: ${data.used}`);
  })
  .catch((error) => console.error(error));

si.osInfo()
  .then((data) => {
    console.log("OS information: ");
    console.log(`- platform: ${data.platform}`);
    console.log(`- distro: ${data.distro}`);
    console.log(`- kernel: ${data.kernel}`);
  })
  .catch((error) => console.error(error));
// emoji chill
console.log(
  chalk.greenBright(
    figlet.textSync("culo fetch", {
      font: "ANSI Shadow",
      horizontalLayout: "default",
      verticalLayout: "default",
      width: 50,
      whitespaceBreak: true,
    })
  )
);
