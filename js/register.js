var username = $("input[id='username").val();
var gender = $("input[name='gender']").val();
var grade = $("input[name='grade']").val();
var campus = $("select[id='campus']").val();
var college = $("select[id='college']").val();
var phone = $("input[id='phone']").val();
var department1 = $("select[id='department1']").val();
var department2 = $("select[id='department2']").val();
var adjust = $("input[name='adjust']").val();
var time = $("select[id='time']").val();
var self_introduce = $("textarea[id='selfintro']").val();
var phoneche=0;

function phonecheck() {
  if (phone.toString().length!=11) {
    phoneche=1
  }
}




function submit() {
    if (username === "") {
      $("#errusername").html("请输入你的姓名");
      $("#errusername").css("color",'red');
    } else if (gender === null) {
      $("#errsex").html("请选择你的性别");
      $("#errsex").css("color",'red');
    } else if (grade === "") {
      err.innerText = "请选择你的年级";
    } else if (campus === "") {
      err.innerText = "请输入你的校区";
    } else if (college === "") {
      err.innerText = "请输入你的学院";
    } else if (phonecheck(phone)===1) {
      err.innerhtml="电请输入正确的电话号码";
    } else if (department1 === "") {
      err.innerText = "请选择你的第一志愿";
    } else if (adjust === null) {
      err.innerText = "请选择你是否接受调剂";
    } else if (department1 === "") {
      err.innerText = "请选择你的面试时间";
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
          username, // 姓名
          sex,//性别
          grade, // 年级 （大12）
          campus,//校区
          college,//学院
          phone, // 手机号
          department1,//第一志愿
          department2,//第二志愿
          adjust,//调剂（是否）
          time,//面试时间
          selfintro,//自我介绍
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
}