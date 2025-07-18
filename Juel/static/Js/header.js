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

function togglePopup(name, price, bed, capacity, roomsize, view, recommend, pic1, pic2, pic3) {
    pic1 = "/media/" + pic1
    pic2 = "/media/" + pic2
    pic3 = "/media/" + pic3

    document.getElementById('rname').innerHTML = name
    document.getElementById('bed').innerHTML = bed
    document.getElementById('capacity').innerHTML = capacity
    document.getElementById('rsize').innerHTML = roomsize
    document.getElementById('rview').innerHTML = view
    document.getElementById('recommend').innerHTML = recommend
    document.getElementById('price').innerHTML = price
    document.getElementById('pic1').setAttribute('src', pic1)
    document.getElementById('pic2').setAttribute('src', pic2)
    document.getElementById('pic3').setAttribute('src', pic3)

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