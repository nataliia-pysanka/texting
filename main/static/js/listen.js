const greetBtn = document.getElementById('greet_btn');
const saveBtn = document.getElementById('save_btn');
const loadBtn = document.getElementById('load_btn');
const textArea = document.querySelector('textarea');

const url = "http://127.0.0.1:8000/";

slide.addEventListener('mousedown', () => {
//    let slide = document.querySelector('.slide.active');
    console.log(event.clientX)
//    console.log(slide)
})

greetBtn.addEventListener('click', () => {
    let centerX = document.documentElement.clientWidth / 2;
    let centerY = document.documentElement.clientHeight / 2;

    let elem = document.elementFromPoint(centerX, centerY);

    elem.style.background = "red";
    alert(elem.tagName);
})

saveBtn.addEventListener('click', () => {

})

loadBtn.addEventListener('click', () => {

})

