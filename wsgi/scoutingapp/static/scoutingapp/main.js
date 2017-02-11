$(document).ready(function() { // page loaded
// var list = ""
// $("<select id=\"ghfkuo\">").insertAfter($("#id_hopper_load"))
// $.get("http://" + location.host + '/scoutingapp/gethoppertypes',
// function(contents) {
// console.log(contents);
// console.log("request complete");
// list = contents;
// list = list.split('\n');
// for (var i = 0; i < list.length; i++) {
// // code here using lines[i] which will give you each
// // line
// $("#ghfkuo").append($("<option value=\"" + i + "\">" + list[i] +
// "</option>"));
// console.log(i);
// }
// $('select').material_select();
//
// }, 'text');
// if ($("#id_hopper_load").length > 0) {
// console.log("Elemement found");
// $("<ul class=\"collection\" id =\"hopper_load_list\"><br>").insertBefore(
// $("#id_hopper_load"));
// }
// $('#ghfkuo').change('select', function() {
// // do something
// console.log("select selected")
// var str=""
// $( "#ghfkuo option:selected" ).each(function() {
// str += $( this ).text() + " ";
// });
// $("#hopper_load_list").append($("<li
// class=\"collection-item\">"+str+"</li>"));
// });
// console.log("starting request")
	$('select').material_select();

	$('#main').smoothState();
});
