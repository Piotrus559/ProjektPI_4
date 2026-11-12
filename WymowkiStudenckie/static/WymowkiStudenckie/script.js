
const przyciskLosowania = document.getElementById("losuj-wymowke");

przyciskLosowania.addEventListener("click", function() {
    const oceny = document.querySelectorAll('input[name="ocena"]');

    oceny.forEach(function(ocena) {
        ocena.checked = false;
    });
});
