function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
}

function loadImages(){
    var image1 = document.getElementById("image1");
    var image2 = document.getElementById("image2");
    var image3 = document.getElementById("image3");
    var image4 = document.getElementById("image4");
    var image5 = document.getElementById("image5");
    var list = [1,2,3,4,5];
    shuffle(list);
    var source1 = document.getElementById("food1").innerHTML;
    image1.src = "/static/pics/"+source1+"/"+list[0]+".jpg";
    var source2 = document.getElementById("food2").innerHTML;
    image2.src = "/static/pics/"+source2+"/"+list[1]+".jpg";
    var source3 = document.getElementById("food3").innerHTML;
    image3.src = "/static/pics/"+source3+"/"+list[2]+".jpg";
    var source4 = document.getElementById("food4").innerHTML;
    image4.src = "/static/pics/"+source4+"/"+list[3]+".jpg";
    var source5 = document.getElementById("food5").innerHTML;
    image5.src = "/static/pics/"+source5+"/"+list[4]+".jpg";
}

loadImages();