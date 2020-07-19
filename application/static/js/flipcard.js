var flipcardBtns = document.getElementsByClassName("flipcard-btn");

var flipcard = function() {
    var cardNumber = this.getAttribute("data-card");
    var card = document.getElementById(cardNumber);
    card.classList.toggle("flipcard-flip");
};

for (var i = 0; i < flipcardBtns.length; i++) {
    flipcardBtns[i].addEventListener('click', flipcard, false);
}
