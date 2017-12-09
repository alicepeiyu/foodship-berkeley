

function changePic1(x){
	var num = Math.floor(Math.random()*5)+1;
	var location = "/static/pics/"+x+"/"+num+".jpg";
	var pic = document.getElementById("pic1");
	pic1.src = location;
}

function changePic2(x){
	var num = Math.floor(Math.random()*5)+1;
	var location = "/static/pics/"+x+"/"+num+".jpg";
	var pic2 = document.getElementById("pic2");
	pic2.src = location;
}

function changePic3(x){
	var num = Math.floor(Math.random()*5)+1;
	var location = "/static/pics/"+x+"/"+num+".jpg";
	var pic3 = document.getElementById("pic3");
	pic3.src = location;
}

function changePics(x){
	var location1 = "/static/pics/"+x+"/"+"1.jpg";
	var location2 = "/static/pics/"+x+"/"+"2.jpg";
	var location3 = "/static/pics/"+x+"/"+"3.jpg";
	var pic1 = document.getElementById("foto1");
	var pic2 = document.getElementById("foto2");	
	var pic3 = document.getElementById("foto3");
	pic1.src = location1;
	pic2.src = location2;
	pic3.src = location3;
}

function passusername(){
	var form = document.getElementById("ownpage");
	form.submit();
}

function checkUserName() {
      $.ajax({
      url : "https://berkeley-foodship-api.herokuapp.com/checkemail",// your username checker url
      type : "POST",
      dataType :"json",
      data : {"email": $("#email").val()},
      success : function (data) {
        if(data == "success")
          {$(".success").show();$(".success").text("Email is OK to use."); $("#submit").prop("disabled",false);}
        else
          {$(".success").show();$(".success").text("Email already exists."); $("#submit").prop("disabled",true);}
      }
    });
}








