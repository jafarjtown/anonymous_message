const div = document.querySelector('#links')
div.style.display = 'none'
async function createLink(){
    const req = await fetch('cr/')
    const res = await req.json()

    const sLink = document.querySelector('#sLink')
    const vLink = document.querySelector('#vLink')

    let slink = res.link1
    let vlink = res.link2
    sLink.href = slink
    sLink.innerText = slink
    vLink.href = vlink
    vLink.innerText = vlink
    document.querySelector('.start_div').style.display = 'none'
    div.style.display = 'block'

}
async function clearLink() {
    const req = await fetch('clear/')
    const res = await req.json()
    location.reload()
}

const btn = document.querySelector('#btn')
btn?.addEventListener('click', createLink)
const clear = document.querySelector('#clear')
clear?.addEventListener('click', clearLink)
console.log(clear)


const copy1btn = document.querySelector('#copy1')
const copy2btn = document.querySelector('#copy2')
function copy1() {
    let str = document.querySelector('#sLink').href
    navigator.clipboard.writeText(`${str}`)
    alert('copied')
    
}
copy1btn.addEventListener('click', copy1)
function copy2() {
    let str = document.querySelector('#vLink').href
    navigator.clipboard.writeText(`${str}`)
    alert('copied')
}
copy2btn.addEventListener('click', copy2)
 
