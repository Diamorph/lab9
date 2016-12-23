var name = false;
var rate = false;
var check = false;
var city = false;
var date = false;
var image;



function checkButton(){
    btn = document.getElementById("submit-btn");
    if (name && rate && check && city && date)
    {
        document.getElementById("submit-btn").removeAttribute("disabled"); 
        document.getElementById("submit-btn").setAttribute("style", "background: #84b732;");
    }
    else {
        document.getElementById("submit-btn").setAttribute("disabled", true); 
        document.getElementById("submit-btn").setAttribute("style", "background:#9D9F9A;");        
}
}


function nameValidator(form){
    inp = document.getElementById("name");
    val = inp.value;
    if (val.length == 0){
        name = false;
        inp.setAttribute("placeholder","Введіть назву ресторану");
        inp.setAttribute("style","border-color: #f55");
    }
    else {
        name = true;
        inp.setAttribute("style","border-color: #af8");
    }
    checkButton();
}

function rateValidator(form) {
    inp = document.getElementById("rate");
    val = inp.value;
    if(/^[0-9]+$/.test(val) &&  val >= 1 && val <= 10){
        rate = true;
        inp.setAttribute("style" , "border-color: #af8");
    }
       
    else{
        rate  = false;
        inp.setAttribute("placeholder" , "Введіть рейтинг");
        inp.setAttribute("style" , "border-color: #f55");
    }
checkButton();
 }



function checkValidator(form) {
    inp = document.getElementById("check");
    val = inp.value;
    if(/^[0-9]+$/.test(val) &&  val >= 1){
        check = true;
        inp.setAttribute("style" , "border-color: #af8");
    }
       
    else{
        check  = false;
        inp.setAttribute("placeholder" , "Введіть рейтинг");
        inp.setAttribute("style" , "border-color: #f55");
    }
checkButton();
 }

function cityValidator(){
    inp = document.getElementById("city");
    val = inp.value;
    if (val.length == 0){
        city = false;
        inp.setAttribute("placeholder", "Введіть місто");
        inp.setAttribute("style", "border-color: #f55");
    }
    else{
        city = true;
        inp.setAttribute("style", "border-color: #af8");
    }
    checkButton();
}

function dateValidator(){
    inp = document.getElementById("date");
    val = inp.value;
    if (val.length == 0){
        date = false;
        inp.setAttribute("placeholder", "Введіть дату відкриття");
        inp.setAttribute("style", "border-color: #f55");
    }
    else{
        date = true;
        inp.setAttribute("style", "border-color: #af8");
    }
    checkButton();
}

function imageValidator(){
    inp = document.getElementById("image");
    val = inp.value;
    if (val.length == 0){
        date = false;
        inp.setAttribute("placeholder", "Додайте фото");
        inp.setAttribute("style", "border-color: #f55");
    }
    else{
        date = true;
        inp.setAttribute("style", "border-color: #af8");
    }
    checkButton();
}

document.getElementById("name").onchange = nameValidator;
document.getElementById("rate").onchange = rateValidator;
document.getElementById("check").onchange = checkValidator;
document.getElementById("city").onchange = cityValidator;
document.getElementById("date").onchange = dateValidator;
document.getElementById("image").onchange = imageValidator;
document.getElementById("submit-btn").onchange = checkButton;


