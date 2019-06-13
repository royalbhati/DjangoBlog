const heartIcon=document.getElementById("heart-icon")
const heartCount=document.getElementById("heart-count")
const noh=heartCount.textContent
console.log(heartIcon)
heartCount.addEventListener('click',function(){
    console.log("clicked")
    heartCount.textContent=(Number(noh)+1)
})