const menulist = document.getElementById('menulist')
menulist.style.maxHeight = '0px'

function menutoggle() {
    if (menulist.style.maxHeight == '0px'){
        menulist.style.maxHeight = '100vh'
    }
    else{
        menulist.style.maxHeight ='0px'
    }
}

const toTop = document.querySelector(".top")

toTop.onclick = r =>{
    window.scrollTo(0,0)
} 

window.addEventListener('scroll', function(){
    if (window.pageYOffset > 280){
        toTop.classList.add('active')
    }
    else{
        toTop.classList.remove('active')
    }
})


const loader = document.querySelector('.perloader')

window.addEventListener('load', () => {
    loader.classList.add('hidden')

    loader.addEventListener('transitionend', () => {
        document.body.removeChild(loader)
    })
})

const popup = document.querySelector('.popup')

function togglePopup() {
    popup.classList.toggle('active')

}
const popup1 = document.querySelector('.popup1')

function togglePopup1() {
    popup1.classList.toggle('active')

}
const popup2 = document.querySelector('.popup2')

function togglePopup2() {
    popup2.classList.toggle('active')

}