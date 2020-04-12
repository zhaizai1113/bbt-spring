var username = $("#username").val();
var gender = $("input[name='gender']").val();
var grade = $("input[name='grade']").val();
var campus = $("#campus").val();
var college = $("select[id='college']").val();
var phone = $("#phone").val();
var department1 = $("#department1").val();
var department2 = $("#department2").val();
var adjust = $("input[name='adjust']").val();
var time = $("#time").val();
var self_introduce = $("#selfintro").val();
var phoneche = 0;
let bumen = new Array("编辑部","综合管理部","综合新闻部","外联部","策划推广部","产品运营部","节目部","人力资源部","技术部","视频部","视觉设计部");
let xueyuan = new Array("机械与汽车工程学院","建筑学院","土木与交通学院","电子与信息学院","材料科学与工程学院","化学与化工学院","轻工科学与工程学院","食品科学与工程学院","数学学院","物理与光电学院","经济与贸易学院","自动化科学与工程学院","计算机科学与工程学院","电力学院","生物科学与工程学院","环境与能源学院","软件学院","工商管理学院","公共管理学院","马克思主义学院","外国语学院","法学院","新闻与传播学院","艺术学院","体育学院","设计学院","医学院","国际教育学院");
function phonecheck() {
  if (phone.toString().length!=11) {
    phoneche = 1;
  }
}
for (var i = xueyuan.length - 1; i >= 0; i--) {
  $("#college").append("<option value =" + xueyuan[i] + ">"  + xueyuan[i] + "</option>");
}
for (var i = bumen.length - 1; i >= 0; i--) {
  $("#department1").append("<option value =" + bumen[i] + ">"  + bumen[i] + "</option>");
}
for (var i = bumen.length - 1; i >= 0; i--) {
  $("#department2").append("<option value =" + bumen[i] + ">"  + bumen[i] + "</option>");
}


function submit() {
  console.log("username");
    if (username == "") {
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
      err.innerhtml="请输入正确的电话号码";
    } else if (department1 === "") {
      err.innerText = "请选择你的第一志愿";
    } else if (adjust === null) {
      err.innerText = "请选择你是否接受调剂";
    } else if (department1 === "") {
      err.innerText = "请选择你的面试时间";
    } else {
      fetch(url,init).then(function(res) {
        return res.json();
      })
      .then(function(myJson) {
        console.log(myJson);
      })

function getData() {
  let name = $("#username").val();
  let gender = $("#gender").val();
  console.log({name,gender});
  let request = new XMLHttpRequest();
  requese.open("POST", baseUrl + "/post");
  let data = {
    'username': name,
    'gender': gender
  }
  request.send(JSON.stringfy(data));
  request.onload = function(e){
    console.log("请求成功");
    console.log({e});
  }
  request.onerror = function(e){
    console.log("请求失败");
    console.log({e});
  }
}

























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