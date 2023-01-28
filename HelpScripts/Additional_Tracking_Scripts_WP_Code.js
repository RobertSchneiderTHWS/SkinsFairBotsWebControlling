
// original_sale_product_price
document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('.single_add_to_cart_button').addEventListener('click', function() {
    var price = document.querySelector('del .woocommerce-Price-amount bdi').innerHTML.substring(0, 6);
	var item_name = document.querySelector('.product_title').innerHTML;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({'event': 'sale_product_details', 'item_name': item_name, 'origin_sale_product_price': price});
  });
});

// product_kollektion, payment methods & stattrak
var kollektions = ["Jagd", "Breakout", "Print-Stream", "Horror", "Fire"];
var payment_methods = ["Rechnung", "Klarna", "Paypal", "Steam", "Crypto"];
var stat_trak = null;
function randomChance(chance) {
  return Math.random() < chance;
}
if (randomChance(0.8)) {
  stat_trak = "False";
} else {
  stat_trak = "True"
}

var randomKollektion = Math.floor(Math.random() * kollektions.length);
var randomPaymentMethods = Math.floor(Math.random() * payment_methods.length);

var randomKollektion = kollektions[randomKollektion];
var randomPaymentMethods = payment_methods[randomPaymentMethods];
var randomStatTrak = stat_trak;

dataLayer.push({
    'event': 'purchased_product_details',
    'kollektion': randomKollektion,
	'payment_method': randomPaymentMethods,
	'stat_trak': randomStatTrak
});

// currency_change
const queryString = location.search;
if (queryString.includes("currency=")) {
 	const currency = queryString.substring(queryString.length - 3);
	dataLayer.push({
 	'event': 'currency_change',
 	'currency': currency
});
}
