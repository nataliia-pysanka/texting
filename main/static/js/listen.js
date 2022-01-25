const start_x = document.getElementById('start_x');
const start_y = document.getElementById('start_y');
const finish_x = document.getElementById('finish_x');
const finish_y = document.getElementById('finish_y');
const imgPath = document.getElementById('img');

const img_width = document.getElementById('img_width');
const img_height = document.getElementById('img_height');

const allSlides = document.querySelectorAll('.slide')
let pressed = false

for (let node of document.querySelectorAll('.slide')) {
  node.addEventListener('mousedown', mouseDown)
}

//const div = document.createElement('div')
//div.classList.add('blue_div')
//div.style.background = '#87CEFA'
//div.style.opacity = '0.5'

function mouseDown(event) {
    if (event.target.classList.contains('active')){
        if (pressed) {
            pressed = false
            finish_x.value =  event.pageX - getCoords(event)['left']
            finish_y.value =  event.pageY - getCoords(event)['top']
            imgPath.value = event.target.getAttribute('datasrc')
            img_width.value = getCoords(event)['right'] - getCoords(event)['left']
            img_height.value = getCoords(event)['bottom'] - getCoords(event)['top']
            console.log(`${start_x.value}, ${start_y.value}, ${finish_x.value}, ${finish_y.value}`)
            console.log(`${img_width.value}, ${img_height.value}`)
        }else{
            pressed = true
            start_x.value =  event.pageX - getCoords(event)['left']
            start_y.value =  event.pageY - getCoords(event)['top']
        }
    }
}


function getCoords(elem) {
  let box = elem.target.getBoundingClientRect();

  return {
    top: box.top + window.pageYOffset,
    right: box.right + window.pageXOffset,
    bottom: box.bottom + window.pageYOffset,
    left: box.left + window.pageXOffset
  };
}
