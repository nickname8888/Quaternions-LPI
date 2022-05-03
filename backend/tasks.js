// const Task = require("../models/task");
const express = require("express");
const router = express.Router();
const {spawn} = require('child_process');
var kill  = require('tree-kill');

var subprocess;
router.post("/start", async (req, res) => {
    try {
        console.log(req.body);
        function runScript(){
            return spawn('python3', [
            "-u",'../yolov5/detect.py',
            // "--source", 'http://192.168.36.22:8080/video',
            "--source",'../yolov5/source/test.mp4'
            ]);
        } 
        subprocess = runScript()
        subprocess.stdout.on('data', (data) => {
            // sarr.push(`${data}`)
            console.log(`Running: ${data}`);
        });
        subprocess.stderr.on('data', (data) => {
            console.log(`error:${data}`);
        });
        subprocess.stderr.on('close', () => {
            console.log("Closed");
        });  
        
        console.log("After runScript")
        res.send(task);
    } catch (error) {
        res.send(error);
    }
});

router.post("/stop", async (req, res) => {
    try {
        console.log(req.body);
        kill(subprocess.pid);  
        res.send("Stopped the process");
    } catch (error) {
        res.send(error);
    }
});

router.get("/", async (req, res) => {
    try {
        // const tasks = await Task.find();
        res.send(JSON.stringify(sarr));
    } catch (error) {
        res.send(error);
    }
});

module.exports = router;
