const express = require("express");
const bodyParser = require("body-parser");
const mysql = require("mysql2");
const cors = require("cors");

const app = express();
app.use(bodyParser.json());
app.use(cors());

// Kết nối MySQL
const db = mysql.createConnection({
    host: "localhost",
    user: "Longvu", // Thay bằng username của bạn
    password: "12042004@", // Thay bằng mật khẩu của bạn
    database: "QLuser" // Tên cơ sở dữ liệu
});

db.connect(err => {
    if (err) throw err;
    console.log("Đã kết nối MySQL!");
});

// API đăng ký người dùng
app.post("/register", (req, res) => {
    const { username, password, email } = req.body;

    if (!username || !password || !email) {
        return res.json({ success: false, message: "Thông tin không đầy đủ." });
    }

    const query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)";
    db.query(query, [username, password, email], (err, result) => {
        if (err) {
            console.error("Lỗi khi thêm người dùng:", err);
            return res.json({ success: false, message: "Đăng ký thất bại." });
        }
        res.json({ success: true, message: "Đăng ký thành công!" });
    });
});

// API đăng nhập người dùng
app.post("/login", (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.json({ success: false, message: "Vui lòng nhập đầy đủ thông tin." });
    }

    const query = "SELECT * FROM users WHERE username = ? AND password = ?";
    db.query(query, [username, password], (err, results) => {
        if (err) {
            console.error("Lỗi khi đăng nhập:", err);
            return res.json({ success: false, message: "Đăng nhập thất bại." });
        }
        if (results.length > 0) {
            res.json({ success: true, message: "Đăng nhập thành công!" });
        } else {
            res.json({ success: false, message: "Sai tên đăng nhập hoặc mật khẩu." });
        }
    });
});

// Khởi động server
app.listen(3000, () => {
    console.log("Server đang chạy trên cổng 3000.");
});
