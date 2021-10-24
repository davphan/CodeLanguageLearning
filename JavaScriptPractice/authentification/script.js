//login functions
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
    window.location.href = "sign-up.html"
}

// sign-up functions

function sign_up() {
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value
    let repass = document.getElementById('re-enter').value
    if (username === '' || password === '' || repass === '') {
        alert("empty field")
    } else if (password != repass) {
        alert("passwords do not match")
        alert(`Username: ${username}, Password: ${password}, Re-enter: ${repass}`)
    } else {
        if (localStorage.getItem(username) === null) {
            localStorage.setItem(username, password)
            alert(`new user! Username: ${username}, Password: ${password}`)
            window.location.href = "login.html"
        } else {
            alert("user already exists")
        }
    }
}

function returnHome() {
    window.location.href = "login.html"
}

// allows text input submit by hitting enter key
$("input").on('keyup', function(event) {
    if (event.keyCode ===13) {
        document.getElementById("loginEnter").click()
    }
})