var shown = false;
var sidebar = document.getElementsByClassName('sidebar')[0];
var options = document.getElementById('options');
console.log(sidebar);

function options_click(){
    shown = !shown;
    if (shown) show();
    else hide();
}

function show(){
    console.log(sidebar.classList);
    sidebar.classList.add('show');
    options.classList.add('opt-cross');
    options.classList.remove('.opt-bar');
}

function hide(){
    sidebar.classList.remove('show');
    options.classList.remove('opt-cross');
    options.classList.add('.opt-bar');
}