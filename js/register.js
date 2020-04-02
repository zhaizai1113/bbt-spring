var username = document.getElementById('username').value;
var gender = document.querySelector('input[name="gender"]:checked');
var grade = document.getElementById("grade");
var campus = document.getElementById("campus");
var college = document.getElementById("college");
var phone = document.getElementById('phone');
var department1 = document.getElementById("department1");
var department2 = document.getElementById("department2");
var adjust = document.querySelector('input[name="adjust"]:checked');
var time = document.getElementById("time");
var self_introduce = document.getElementById('self_introduce');
var phoneReg = /^1[0-9]{10}$/;




function Confirm() {
 /* if (!disable) {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("tips").style.visibility = "hidden";
    let nickname = document.getElementById("nickname").value;
    let gradeIndex = document.getElementById("grade").selectedIndex;
    let grade = document.getElementById("grade").options[gradeIndex].value;
    let checkedGender = document.querySelector('input[name="gender"]:checked');
    let tel = document.getElementById("tel").value;
    let wechat = document.getElementById("wechat").value;
    let checkedExp = document.querySelector(
      'input[name="expectation"]:checked'
    );*/
    let err = document.getElementById("error");
    let phoneReg = /^1[0-9]{10}$/;

    if (username === "") {
      err.innerText = "请输入你的姓名";
    } else if (gender === "") {
      err.innerText = "请选择你的性别";
    } else if (grade === "") {
      err.innerText = "请选择你的年级";
    } else if (campus === "") {
      err.innerText = "请输入你的校区";
    } else if (college === "") {
      err.innerText = "请输入你的学院";
    } else if (!phoneReg.test(phone)) {
      err.innerhtml="请输入你的手机号码";
    } else if (department1 === "") {
      err.innerText = "请选择你的第一志愿";
    } else if (adjust === null) {
      err.innerText = "请选择你是否接受调剂";
    } else {
      let gender = checkedGender.value;
      let expectation = checkedExp.value;
      disable = true;
      fetch(prefix + "/info", {
        method: "post",
        credentials: "include",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          nickname, // 昵称
          grade, // 年级 （大12345，研123）
          tel, // 手机号
          wechat, // 微信号
          gender, // 性别（男/女）
          expectation // 期望匹配的性别（男/女/随机）
        })
      })
        .then(checkStatus)
        .then(res => res.json())
        .then(res => {
          window.location.href = "complete.html";
        })
        .catch(error => {
          if(error.res.status == 400){
            document.getElementById('error').innerText = error.res.statusText;
          }
          disable = false;
        });
          window.location='final.html';
    }
 // }
}