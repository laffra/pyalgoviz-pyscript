
let context = null;
let canvas = null;
let None = null;

function init() {
    /* Initializes the drawing canvas */
    let div = $(".drawing").empty();
    let parent = div.parent();
    canvas = $("<canvas>")
        .attr("width", parseInt(parent.width()))
        .attr("height", parseInt(parent.height()))
        .appendTo(div);
    context = canvas[0].getContext("2d");
}

function clear() {
    /* Clears the drawing canvas */
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width(), canvas.height());
}

function n(x, y, label, value, scale=4, color='black') {
    /* Draw a number */
    text(x, y+10, label);
    rect(x+20, y, value*scale, 10, color);
    text(x+22+value*scale, y+10, value);
}

function b(x, y, w, h, items, highlight=-1, fill="black", scale=1) {
    /* Draw a barchart */
    rect(x, y, w, h, '#FDFDF0', "gray");
    if (items) {
        let d = Math.min(15, Math.floor(w/items.length));
        let offset = (w - items.length*d)/2;
        items.forEach((item, n) => {
            let hitem = item*scale;
            rect(offset+x+n*d, y+h-hitem, d-2, hitem, n===highlight ? 'red' : fill, "lightgray");
        });
    }
}

function t(x, y, txt, size=13, font='Arial', color='black') {
    /* Draw a text */
    context.fillStyle = color
    context.font = `${size}px ${font}`
    context.fillText(txt, x, y)
}

function e(msg) {
    /* Draw an error message */
    $(".log-viz").append(
        $("<div>")
            .text(msg)
            .addClass("error")
    );
}

function l(x1, y1, x2, y2, color='black', width=1) {
    /* Draw a line */
    context.strokeStyle = color
    context.lineWidth = width
    context.beginPath()
    context.moveTo(x1, y1)
    context.lineTo(x2, y2)
    context.stroke()
    context.lineWidth = 1
}

function r(x, y, w, h, fill='white', border='black') {
    /* Draw a rectangle */
    context.strokeStyle = border
    context.strokeRect(x, y, w, h)
    context.fillStyle = fill
    context.fillRect(x, y, w, h)
}

function c(x, y, radius, fill='white', border='black') {
    /* Draw a circle */
    context.beginPath()
    context.arc(x, y, radius, 0, 2 * Math.PI)
    context.fillStyle = fill
    context.fill()
    context.strokeStyle = border
    context.stroke()
}

function a(x, y, radius, startAngle, endAngle, border='black', width=1) {
    context.beginPath()
    context.arc(x, y, radius, startAngle, endAngle)
    context.strokeStyle = border
    context.lineWidth = width
    context.stroke()
}

function p(string) {
    $(".log-viz").append(
        $("<div>")
            .text(string)
            .addClass("log-line")
    );
}

const audioContext = new (window.AudioContext || window.webkitAudioContext)()

function s(frequency, duration) {
    const oscillator = audioContext.createOscillator()
    const gainNode = audioContext.createGain()
    
    oscillator.connect(gainNode)
    gainNode.connect(audioContext.destination)
    
    oscillator.frequency.value = frequency
    oscillator.type = 'sine'
    
    gainNode.gain.setValueAtTime(0.005, audioContext.currentTime)
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + duration/1000)
    
    oscillator.start()
    oscillator.stop(audioContext.currentTime + duration/1000)
}

barchart = b;
text = t;
circle = c;
arc = a;
beep = s;
error = e;
rect = r;
line = l;
number = n;

function render(operations) {
    $(".log-viz").empty();
    eval(operations)
}