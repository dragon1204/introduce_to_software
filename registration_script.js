function registration(e){
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var user = {
        username : username,
        email : email,
        password : password,
    };
    var json = JSON.stringify(user);
    localStorage.setItem(username, json);
    alert("đăng ký thành công");
}

function login(e){
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var user = localStorage.getItem(user);
    var data = json.parse(user);
    if(user == null){
        alert("Vui lòng nhập thông tin")
    }
    else if(username == data.username && password == data.password){
        alert("Đăng nhập thành công")
        window.location.href="index.html"
    }

    else{
        alert("Đăng nhập thất bại")
    } 
}