const electron = require('electron');
const app = electron.app;
const browserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow(){
mainWindow = new browserWindow();

mainWindow.loadURL('file://'+__dirname+'index.html');
}
