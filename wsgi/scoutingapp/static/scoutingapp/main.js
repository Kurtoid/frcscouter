$(document)
.ready(
       function () { // page loaded
           var $fuel_initial = $("#id_fuel");
           if ($fuel_initial.length > 0) { // if scouting page
               // detected
               console.log("Detected");
               var $gear_initial = $("#id_gears_scout");
               // add hopper volley list
               $("<ul class=\"collection\" id =\"hopper_load_list\"><br>")
               .insertBefore($fuel_initial.parent());
               $("<ul class=\"collection\" id =\"gear_list\"><br>")
               .insertBefore($gear_initial.parent());
               $fuel_initial.parent().attr('class', 'col s4') // change width of select
               $gear_initial.parent().attr('class', 'col s4') // change width of select

               // convert text field to select...
               var attrs = {};
               $.each($fuel_initial[0].attributes, function (idx, attr) {
                   attrs[attr.nodeName] = attr.nodeValue;
               });

               $fuel_initial.replaceWith(function () {
                   return $("<select />", attrs).append($(this).contents());
               });
               attrs = {};
               $.each($gear_initial[0].attributes, function (idx, attr) {
                   attrs[attr.nodeName] = attr.nodeValue;
               });
               $gear_initial.replaceWith(function () {
                   return $("<select />", attrs).append($(this).contents());
               });
               $("<div class =\"col s4\"><select id=\"volleyType\" /></div> ")
               .insertAfter($(".customListMaker").parent())
               $("<div class =\"col s4\"><select id=\"volleyEff\" /></div> ")
               .insertAfter($("#volleyType").parent())
               $(
                 '<div class="row"><a class="waves-effect waves-light red accent-4 btn" id="volleyAdd">Add</a></div>')
               .insertAfter($("#volleyEff").parent().parent())

               $("<div class =\"col s4\"><select id=\"gear_dropped\" /></div> ")
               .insertAfter($(".customListMaker2").parent())
               $(
                 '<div class="row"><a class="waves-effect waves-light red accent-4 btn" id="gearAdd">Add</a></div>')
               .insertAfter($("#gear_dropped").parent().parent())
               // now a select object
               console.log("starting request")
               var list = ""
               // get new items for hopper types
               $.get("http://" + location.host + '/scoutingapp/gethoppertypes',
                     function (contents) {
                         console.log(contents);
                         console.log("request complete");
                         list = contents;
                         list = list.split('\n');
                         for (var i = 0; i < list.length; i++) {
                             // code here using lines[i] which will give you each line
                             $("#id_fuel").append(
                                                  $("<option value=\"" + i
                                                    + "\">" + list[i]
                                                    + "</option>"));
                             console.log(i);
                         }
                         $('select').material_select();

                     }, 'text');
               $.get("http://" + location.host + '/scoutingapp/getshottypes',
                     function (contents) {
                         console.log(contents);
                         console.log("request complete");
                         list = contents;
                         list = list.split('\n');
                         for (var i = 0; i < list.length; i++) {
                             // code here using lines[i] which will give you each line
                             $("#volleyType").append(
                                                     $("<option value=\"" + i
                                                       + "\">" + list[i]
                                                       + "</option>"));
                             console.log(i);
                         }
                         $('select').material_select();

                     }, 'text');
               $.get("http://" + location.host + '/scoutingapp/getveff',
                     function (contents) {
                         console.log(contents);
                         console.log("request complete");
                         list = contents;
                         list = list.split('\n');
                         for (var i = 0; i < list.length; i++) {
                             // code here using lines[i] which will give you each line
                             $("#volleyEff").append(
                                                    $("<option value=\"" + i
                                                      + "\">" + list[i]
                                                      + "</option>"));
                             console.log(i);
                         }
                         $('select').material_select();

                     }, 'text');
               $.get("http://" + location.host + '/scoutingapp/getgearsource',
                     function (contents) {
                         console.log(contents);
                         console.log("request complete");
                         list = contents;
                         list = list.split('\n');
                         for (var i = 0; i < list.length; i++) {
                             // code here using lines[i] which will give you each line
                             $("#id_gears_scout").append(
                                                         $("<option value=\""
                                                           + i + "\">"
                                                           + list[i]
                                                           + "</option>"));
                             console.log(i);
                         }
                         $('select').material_select();

                     }, 'text');
               $.get("http://" + location.host + '/scoutingapp/getgeardropped',
                     function (contents) {
                         console.log(contents);
                         console.log("request complete");
                         list = contents;
                         list = list.split('\n');
                         for (var i = 0; i < list.length; i++) {
                             // code here using lines[i] which will give you each line
                             $("#gear_dropped").append(
                                                       $("<option value=\"" + i
                                                         + "\">" + list[i]
                                                         + "</option>"));
                             console.log(i);
                         }
                         $('select').material_select();

                     }, 'text');
               console.log("Elemement found");
           }
           $('#volleyAdd')
           .click(
                  function () {
                      console.log("select selected")
                      var str = ""
                      $("#id_fuel option:selected").each(function () {
                          str += $(this).text() + " ";
                      });
                      $("#volleyType option:selected").each(function () {
                          str += $(this).text() + " ";
                      });
                      $("#volleyEff option:selected").each(function () {
                          str += $(this).text() + " ";
                      });
                      // add item to list
                      $("#hopper_load_list")
                      .append(
                              $("<li class=\"collection-item hitem dismissable\"><div ><div class=\"kListItemF\">" + str
                                + "</div><a class = \"secondary-content\" href=\"#!\" onClick=\"$(this).parent().parent().remove()\"><i class=\"material-icons\">cancel</i></a></div></li>"));
                      console.log("done!")
                  });
           $('#gearAdd')
           .click(
                  function () {
                      console.log("select selected")
                      var str = ""
                      $("#id_gears_scout option:selected").each(function () {
                          str += $(this).text() + " ";
                      });
                      $("#gear_dropped option:selected").each(function () {
                          str += $(this).text() + " ";
                      });
                      // add item to list
                      $("#gear_list")
                      .append(
                              $("<li class=\"collection-item hitem dismissable\"><div ><div class=\"kListItemG\">" + str
                                + "</div><a class = \"secondary-content\" href=\"#!\" onClick=\"$(this).parent().parent().remove()\"><i class=\"material-icons\">cancel</i></a></div></li>"));
                      console.log("done!")
                  });
           $('select').material_select();

       });
$(function () {
    $('#main').smoothState();
});

$('#mainForm')
.submit(
        function () {
            // document.myform.myinput.value = '1';
            var attrs = {};

            $.each($('#mainForm select[name="fuel"]')[0].attributes,
                   function (idx, attr) {
                       attrs[attr.nodeName] = attr.nodeValue;
                   });

            $('#mainForm select[name="fuel"]').replaceWith(function () {
                return $("<input />", attrs).append($(this).contents());
            });
            var t = ""
            $(".kListItemF").each(function (index) {

                // alert($(this).text());
                t += $(this).text() + ";";
            })

            $('#mainForm input[name="fuel"]').val(t);

            attrs = {};

            $.each($('#mainForm select[name="gears_scout"]')[0].attributes,
                   function (idx, attr) {
                       attrs[attr.nodeName] = attr.nodeValue;
                   });

            $('#mainForm select[name="gears_scout"]').replaceWith(function () {
                return $("<input />", attrs).append($(this).contents());
            });
            var t = ""
            $(".kListItemG").each(function (index) {

                // alert($(this).text());
                t += $(this).text() + ";";
            })

            $('#mainForm input[name="gears_scout"]').val(t);
            console.log("Submit!")
            return true;
        });
