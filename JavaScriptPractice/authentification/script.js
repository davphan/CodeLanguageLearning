document.onload = console.log("...js working...")

function takeInfo() {
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value
    let x = localStorage.getItem(username)
    if (x !== null) {
        if (x == password) {
            alert("successful login!")
        }
        else {
            alert("incorrect password")
        }
    } else {
        alert("no matching username")
    }
}

function link() {
    window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

function newAccount() {
    // TESTING
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value
    localStorage.setItem(username, password)
    alert(`new user! Username: ${username}, Password: ${password}`)
}

$("input").on('keyup', function(event) {
    if (event.keyCode ===13) {
        document.getElementById("loginEnter").click()
    }
})