const greetBtn = document.getElementById('greet_btn');
const saveBtn = document.getElementById('save_btn');
const loadBtn = document.getElementById('load_btn');

const textArea = document.querySelector('textarea');

const start_x = document.getElementById('start_x');
const start_y = document.getElementById('start_y');
const width = document.getElementById('width');
const height = document.getElementById('height');
imgPath = document.getElementById('img');

const allSlides = document.querySelectorAll('.slide')
let pressed = false

for (let node of document.querySelectorAll('.slide')) {
  node.addEventListener('mousedown', mouseDown)
//  node.addEventListener('mousemove', mouseMove)
}

//const div = document.createElement('div')
//div.classList.add('blue_div')
//div.style.background = '#87CEFA'
//div.style.opacity = '0.5'

function mouseDown(event) {
    if (event.target.classList.contains('active')){
        if (pressed) {
            pressed = false
            width.value =  event.pageX - getCoords(event)['left']
            height.value =  event.pageY - getCoords(event)['top']
            imgPath.value = event.target.getAttribute('datasrc')
            console.log(imgPath.value)

//            console.log(width.value)
//            console.log(height.value)
//            div.style.right = `${event.pageX}px`
//            div.style.bottom = `${event.pageY}px`
//            event.target.append(div)
//            console.log(`right ${div.style.right}, bottom ${div.style.bottom}`)
        }else{
            pressed = true
            start_x.value =  event.pageX - getCoords(event)['left']
            start_y.value =  event.pageY - getCoords(event)['top']
//            console.log(start_x.value)
//            console.log(start_y.value)
        }
    }
}

function mouseMove(event) {
//    if (event.target.classList.contains('active')){
//        if (pressed) {
////        console.log(getCoords(event))
//        console.log(`event.clientX ${event.clientX}, event.clientY ${event.clientY}`)
////        console.log(`width ${event.target.clientWidth}, event.target.clientHeight ${event.target.clientHeight}`)
//            div.style.right = `${event.pageX}px`
//            div.style.bottom = `${event.pageY }px`
//            event.target.append(div)
//        }
//    }
}


function getCoords(elem) {
  let box = elem.target.getBoundingClientRect();

  return {
    top: box.top + window.pageYOffset,
    right: box.right + window.pageXOffset,
    bottom: box.bottom + window.pageYOffset,
    left: box.left + window.pageXOffset
//        elem: elem.target,
//    top: box.top,
//    right: box.right,
//    bottom: box.bottom,
//    left: box.left
  };
}

//function mouseUp(event) {
//    if (event.target.classList.contains('active')){
//        finish_x.value = event.pageX
//        finish_y.value = event.pageY
//        console.log(`pageX:${event.pageX}, pageY:${event.pageY}`)
//    }
//}

greetBtn.addEventListener('click', () => {
//    let centerX = document.documentElement.clientWidth / 2;
//    let centerY = document.documentElement.clientHeight / 2;
//
//    let elem = document.elementFromPoint(centerX, centerY);
//
//    elem.style.background = "red";
//    alert(elem.tagName);
})

saveBtn.addEventListener('click', () => {

})

loadBtn.addEventListener('click', () => {

})

