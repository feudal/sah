function toggle(link) {
	card = link.parentElement.parentElement;
	card.classList.toggle('big-card');
	details = card.getElementsByClassName('details')[0]
	details.classList.toggle('big-details');
	frame = card.getElementsByClassName('frame')[0]
	frame.classList.toggle('big-frame');
}

tog_menu = document.getElementById("toggle_menu")
tog_menu.addEventListener("click", toggle_menu)


function toggle_menu() {
	document.getElementById("id_menu").classList.toggle('active');
}

// ------------------active links---------------------------
var pathname = window.location.pathname; 
console.log(pathname)

var btnContainer = document.getElementById("id_menu");
var btns = btnContainer.getElementsByClassName("link");

// if (pathname == '/') {
// 	btns[0].classList.add('active')
// }
if (pathname == '/players') {
	btns[1].classList.add('active')
}
if (pathname == '/other_players') {
	btns[2].classList.add('active')
}
