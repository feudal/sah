function toggle(link) {
	card = link.parentElement.parentElement;
	card.classList.toggle('big-card');
	details = card.getElementsByClassName('details')[0]
	details.classList.toggle('big-details');
	frame = card.getElementsByClassName('frame')[0]
	frame.classList.toggle('big-frame');
}
