//Pose Estimation HRI Assignment 1 by Aigerim Keutayeva
let video;
let poseNet;
let pose;
let skeleton;
let happy_time = 0;
let angry_time = 0;
let sad_time = 0;
let scary_time = 0;
let happy_c = 0;
let angry_c = 0;
let sad_c = 0;
let scary_c = 0;


function setup() {
    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    poseNet = ml5.poseNet(video, modelLoaded);
    poseNet.on('pose', gotPoses);
}

function gotPoses(poses) {
    console.log(poses);
    if (poses.length > 0) {
        pose = poses[0].pose;
        skeleton = poses[0].skeleton;
    }
}

function modelLoaded() {
    console.log('PoseNet Ready');
}
  
// Functions for showing current emotions
function happy() {
    return "Happy!";
}
function angry() {
    return "Angry!";
}
function sad() {
    return "Sad!";
}
function scary() {
    return "Scary!";
}

// After long time of experience the coefficient 720 was selected for seconds count
function happy_seconds() {
    return Math.floor(happy_time++ / 720) + " sec";
}
function angry_seconds() {
    return Math.floor(angry_time++ / 720) + " sec";
}
function sad_seconds() {
    return Math.floor(sad_time++ / 720) + " sec";
}
function scary_seconds() {
    return Math.floor(scary_time++ / 720) + " sec";
}

// After long time of experience the coefficient 2680 was selected for seconds count
function happy_count() {
    return Math.floor(happy_c++ / 2680) + " times";
}
function angry_count() {
    return Math.floor(angry_c++ / 2680) + " times";
}
function sad_count() {
    return Math.floor(sad_c++ / 2680) + " times";
}
function scary_count() {
    return Math.floor(scary_c++ / 2680) + " times";
}


function draw() {
    image(video, 0, 0);
    if (pose) {
        for (let i = 0; i < pose.keypoints.length; i++) {
            let x = pose.keypoints[i].position.x;
            let y = pose.keypoints[i].position.y;
            fill(255, 0, 253);
            ellipse(x, y, 16, 16);

            // Logic of emotions
            
            if ((pose.keypoints[9].position.y || pose.keypoints[10].position.y) < (pose.keypoints[0].position.y)){
                document.getElementById("emotion").innerHTML = happy();
                document.getElementById("seconds1").innerHTML = happy_seconds();
                document.getElementById("count1").innerHTML = happy_count();
            } else if (pose.keypoints[9].position.x > pose.keypoints[5].position.x &&
                       pose.keypoints[10].position.x < pose.keypoints[6].position.x &&
                       pose.keypoints[9].position.y > pose.keypoints[7].position.y &&
                       pose.keypoints[10].position.y > pose.keypoints[8].position.y) {
                document.getElementById("emotion").innerHTML = angry();
                document.getElementById("seconds2").innerHTML = angry_seconds();
                document.getElementById("count2").innerHTML = angry_count();
            } else if (pose.keypoints[9].position.x > pose.keypoints[7].position.x &&
                       pose.keypoints[10].position.x < pose.keypoints[8].position.x &&
                       pose.keypoints[9].position.y < pose.keypoints[7].position.y &&
                       pose.keypoints[10].position.y < pose.keypoints[8].position.y) {
                document.getElementById("emotion").innerHTML = sad();
                document.getElementById("seconds3").innerHTML = sad_seconds();
                document.getElementById("count3").innerHTML = sad_count();
            } else if (pose.keypoints[9].position.x < pose.keypoints[5].position.x &&
                       pose.keypoints[10].position.x > pose.keypoints[6].position.x &&
                       pose.keypoints[9].position.y < pose.keypoints[7].position.y &&
                       pose.keypoints[10].position.y < pose.keypoints[8].position.y) {
                document.getElementById("emotion").innerHTML = scary();
                document.getElementById("seconds4").innerHTML = scary_seconds();
                document.getElementById("count4").innerHTML = scary_count();
            } else {
                document.getElementById("emotion").innerHTML = "No Emotions";
            }               
         }

        for (let i = 0; i < skeleton.length; i++) {
            let a = skeleton[i][0];
            let b = skeleton[i][1];
            strokeWeight(2);
            stroke(255);
            line(a.position.x, a.position.y, b.position.x, b.position.y);
        }
     }
}