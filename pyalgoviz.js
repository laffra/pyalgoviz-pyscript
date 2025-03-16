
let context = null;
let canvas = null;

function init() {
    /* Initializes the drawing canvas */
    let div = $(".drawing").empty();
    canvas = $("<canvas>")
        .attr("width", parseInt(div.width()))
        .attr("height", parseInt(div.height()))
        .appendTo(div);
    context = canvas[0].getContext("2d");
}

function clear() {
    /* Clears the drawing canvas */
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width(), canvas.height());
}

function number(x, y, label, value, scale=4, color='black') {
    /* Draw a number */
    text(x, y+10, label);
    rect(x+20, y, value*scale, 10, color);
    text(x+22+value*scale, y+10, value);
}

function barchart(x, y, w, h, items, highlight=-1, scale=1, fill='black', border='black') {
    /* Draw a barchart */
    rect(x, y, w, h, '#FDFDF0', border);
    if (items) {
        let d = Math.min(15, Math.floor(w/items.length));
        let offset = (w - items.length*d)/2;
        items.forEach((item, n) => {
            let hitem = item*scale;
            rect(offset+x+n*d, y+h-hitem, d-2, hitem, n===highlight ? 'red' : fill);
        });
    }
}

function text(x, y, txt, size=13, font='Arial', color='black') {
    /* Draw a text */
    context.fillStyle = color
    context.font = `${size}px ${font}`
    context.fillText(txt, x, y)
}

function error(msg) {
    /* Draw an error message */
    text(20, 20, msg, 20, 'Arial', 'red')
}

function line(x1, y1, x2, y2, color='black', width=1) {
    /* Draw a line */
    context.strokeStyle = color
    context.lineWidth = width
    context.beginPath()
    context.moveTo(x1, y1)
    context.lineTo(x2, y2)
    context.stroke()
}

function rect(x, y, w, h, fill='white', border='black') {
    /* Draw a rectangle */
    context.strokeStyle = border
    context.strokeRect(x, y, w, h)
    context.fillStyle = fill
    context.fillRect(x, y, w, h)
}

function circle(x, y, radius, fill='white', border='black') {
    /* Draw a circle */
    context.strokeStyle = border
    context.beginPath()
    context.arc(x, y, radius, 0, 2 * Math.PI)
    context.stroke()
    context.fillStyle = border
    context.fill()
}

function arc(cx, cy, innerRadius, outerRadius, startAngle, endAngle, color='black') {
    /* Draw an arc */
}

function render(items) {
    for (let item of items) {
        eval(item)
    }
}