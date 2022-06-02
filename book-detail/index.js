var dark = true;

function changeTheme(){
    let body = document.body;
    body.setAttribute("data-theme", dark ? "t-dark" : "t-light");
    dark = !dark;
}