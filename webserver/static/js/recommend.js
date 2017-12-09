function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
}

function recImages(){
	var list = [1,2,3,4,5];
	shuffle(list);
	var source1 = document.getElementById("rec-food1").innerHTML;
	document.getElementById("rec-image1").src = "/static/pics/"+source1+"/"+list[0]+".jpg";
	var source2 = document.getElementById("rec-food2").innerHTML;
	document.getElementById("rec-image2").src = "/static/pics/"+source2+"/"+list[1]+".jpg";
	var source3 = document.getElementById("rec-food3").innerHTML;
	document.getElementById("rec-image3").src = "/static/pics/"+source3+"/"+list[2]+".jpg";
}
recImages();