"use strict";

class FacePoints {
    constructor() {
        this.eye_left = [];
        this.eye_right = [];

        this.eyebrow_left = [];
        this.eyebrow_right = [];

        this.nose_median = [];
        this.nose_bottom = [];

        this.lips_inner = [];
        this.lips_outer = [];

        this.face_contour = [];
    }
}

function readURL(input) {
    return new Promise(function (resolve, reject) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                resolve(reader.result);
            };
            reader.onerror = function () {
                reject();
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            reject();
        }
    });
}

/**
 *
 * @param {HTMLCanvasElement} canvas
 * @param {String} imageSource
 * @returns {Promise<>}
 */
function loadImage(canvas, imageSource) {
    return new Promise(function (resolve, reject) {
        let img = new Image();
        img.onload = function () {
            let rw = img.width / canvas.width,
                rh = img.height / canvas.height;
            let ration = rw > rh ? rw : rh;
            let w = img.width / ration, h = img.height / ration;
            let left = (canvas.width - w) / 2,
                top = (canvas.height - h) / 2;

            let context = canvas.getContext("2d");
            context.clearRect(0, 0, canvas.width, canvas.height);
            context.drawImage(img, left, top, w, h);

            resolve();
        };
        img.onerror = function () {
            reject();
        };
        img.src = imageSource;
    })
}

/**
 * Load face points from server
 * @param {String} base64Img
 * @returns {Promise<FacePoints[]>}
 */
function getPoints(base64Img) {
    return new Promise(function (resolve, reject) {
        let xhr = new XMLHttpRequest();

        const body = 'image=' + encodeURIComponent(base64Img);
        
        xhr.open("POST", 'http://localhost:8001/', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onreadystatechange = function () {
            if (4 === xhr.readyState) {
                if (200 !== xhr.status) {
                    reject();
                } else {
                    resolve(JSON.parse(xhr.response));
                }
            }
        };

        xhr.send(body);
    });
}

/**
 *
 * @param {HTMLCanvasElement} canvas
 * @param {FacePoints} facePoints
 */
function drawPoints(canvas, facePoints) {
    let context = canvas.getContext("2d");
    let radius = 2;

    for (let key in facePoints) {
        if (!facePoints.hasOwnProperty(key)) {
            continue;
        }
        let partPoints = facePoints[key];
        for (let pi = 0; pi < partPoints.length; pi++) {
            let p = partPoints[pi],
                x = p[0],
                y = p[1];
            context.beginPath();
            context.arc(x, y, radius, 0, 2 * Math.PI, false);
            context.fillStyle = 'green';
            context.fill();
            context.lineWidth = 0;
            context.strokeStyle = '#003300';
            context.stroke();
        }
    }
}

/**
 * Draw polygon and fill it
 * @param {HTMLCanvasElement} canvas
 * @param {Number[][]} points
 * @param {String} color
 */
function fillShape(canvas, points, color) {
    let ctx = canvas.getContext('2d');
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(points[0][0], points[0][1]);
    for (let i = 1; i < points.length; i++) {
        ctx.lineTo(points[i][0], points[i][1]);
    }
    ctx.closePath();
    ctx.fill();
}

/**
 * Extract to one array all point which is contour of top lip
 * @param {Array} pointSet
 * @returns {Number[] | string}
 */
function extractTopLipPoints(pointSet) {
    let inLine = pointSet['lips_inner'];
    let outLine = pointSet['lips_outer'];
    const top = outLine.slice(0, 7);
    const bottom = inLine.slice(0, 5);
    return top.concat(bottom.reverse());
}

/**
 * Extract to one array all point which is contour of bottom lip
 * @param {Array} pointSet
 * @returns {Number[] | string}
 */
function extractBottomLipPoints(pointSet) {
    let inLine = pointSet['lips_inner'];
    let outLine = pointSet['lips_outer'];
    const blTop = inLine.slice(4, 8).concat([inLine[0]]);
    const blBottom = outLine.slice(6, 12).concat([outLine[0]]);
    return blTop.concat(blBottom.reverse());
}