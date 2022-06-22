var dark = true;

function changeTheme(){
    let body = document.body;
    dark = !dark;
    body.setAttribute("data-theme", dark ? "t-dark" : "t-light");
}