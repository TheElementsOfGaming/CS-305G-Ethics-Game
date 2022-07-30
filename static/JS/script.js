$(document).ready(function() {
    let shareholderScore = $('#shareholderScore').text().split("/"); shareholderScore = shareholderScore[0] / shareholderScore[1];
    let publicScore = $('#publicScore').text().split("/"); publicScore = publicScore[0] / publicScore[1];
    let moneyScore = $('#moneyScore').text().split("/"); moneyScore = moneyScore[0] / moneyScore[1];
    let moraleScore = $('#moraleScore').text().split("/"); moraleScore = moraleScore[0] / moraleScore[1];

    $('#shareholderScore').css({"background-color":`hsl(${120 * shareholderScore}, 100%, 50%)`,"border-color":`hsl(${120 * shareholderScore}, 100%, 50%)`})
    $('#publicScore').css({"background-color":`hsl(${120 * publicScore}, 100%, 50%)`,"border-color":`hsl(${120 * publicScore}, 100%, 50%)`})
    $('#moneyScore').css({"background-color":`hsl(${120 * moneyScore}, 100%, 50%)`,"border-color":`hsl(${120 * moneyScore}, 100%, 50%)`})
    $('#moraleScore').css({"background-color":`hsl(${120 * moraleScore}, 100%, 50%)`,"border-color":`hsl(${120 * moraleScore}, 100%, 50%)`})
    $('.score').on('DOMSubtreeModified', function(){
    let shareholderScore = $('#shareholderScore').text().split("/"); shareholderScore = shareholderScore[0] / shareholderScore[1];
    let publicScore = $('#publicScore').text().split("/"); publicScore = publicScore[0] / publicScore[1];
    let moneyScore = $('#moneyScore').text().split("/"); moneyScore = moneyScore[0] / moneyScore[1];
    let moraleScore = $('#moraleScore').text().split("/"); moraleScore = moraleScore[0] / moraleScore[1];

    $('#shareholderScore').css({"background-color":`hsl(${120 * shareholderScore}, 100%, 50%)`,"border-color":`hsl(${120 * shareholderScore}, 100%, 50%)`})
    $('#publicScore').css({"background-color":`hsl(${120 * publicScore}, 100%, 50%)`,"border-color":`hsl(${120 * publicScore}, 100%, 50%)`})
    $('#moneyScore').css({"background-color":`hsl(${120 * moneyScore}, 100%, 50%)`,"border-color":`hsl(${120 * moneyScore}, 100%, 50%)`})
    $('#moraleScore').css({"background-color":`hsl(${120 * moraleScore}, 100%, 50%)`,"border-color":`hsl(${120 * moraleScore}, 100%, 50%)`})
    });
});

function changeValue() {
    $('#shareholderScore').text("20/25")
}