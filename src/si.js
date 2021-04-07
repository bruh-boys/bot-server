const si = require('systeminformation');
const chalk=require("chalk")
const figlet=require("figlet")

valueObject = {
  cpu: 'brand, cores,speedMin,speedMax',
  osInfo: 'platform, release, distro,kernel',
  system: 'model, manufacturer',
  mem: 'total,used,active',
  diskLayout: 'type, size'

}

si.get(valueObject).then(data => console.log(data));

console.log(chalk.greenBright(figlet.textSync('culo fetch', {
    font: 'ANSI Shadow',
    horizontalLayout: 'default',
    verticalLayout: 'default',
    width: 50,
    whitespaceBreak: true
})));



