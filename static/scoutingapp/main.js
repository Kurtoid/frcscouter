$(document)
.ready(
       function () { // page loaded
           if ($("#id_hopper_load").length > 0) { // if scouting page
               // detected

               // add hopper volley list
               $("<ul class=\"collection\" id =\"hopper_load_list\"><br>")
               .insertBefore($("#id_hopper_load").parent());
               $("#id_hopper_load").parent().attr('class', 'col s4') // change width of select

               // convert text field to select...
               var attrs = {};
               $.each($("#id_hopper_load")[0].attributes, function (idx, attr) {
                   attrs[attr.nodeName] = attr.nodeValue;
               });

               $("#id_hopper_load").replaceWith(function () {
                   return $("<select />", attrs).append($(this).contents());
               });
               $("<div class =\"col s4\"><select id=\"volleyType\" /></div> ")
               .insertAfter($(".customListMaker").parent())
               $("<div class =\"col s4\"><select id=\"volleyEff\" /></div> ")
               .insertAfter($("#volleyType").parent())
               $(
                 '<div class="row s4"><a class="waves-effect waves-light btn" id="volleyAdd">Add</a></div>')
               .insertAfter($("#volleyEff").parent())
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
                             $("#id_hopper_load").append(
                                                         $("<option value=\""
                                                           + i + "\">"
                                                           + list[i]
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
               console.log("Elemement found");
           }
           $('#volleyAdd')
           .click(
                  function () {
                      console.log("select selected")
                      var str = ""
                      $("#id_hopper_load option:selected").each(function () {
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
                              $("<li class=\"collection-item hitem\">" + str
                                + "</li>"));
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

            $.each($('#mainForm select[name="hopper_load"]')[0].attributes,
                   function (idx, attr) {
                       attrs[attr.nodeName] = attr.nodeValue;
                   });

            $('#mainForm select[name="hopper_load"]').replaceWith(function () {
                return $("<input />", attrs).append($(this).contents());
            });
            var t = ""
            $(".hitem").each(function (index) {

//                alert($(this).text());
                t += $(this).text() + ";";
            })

            $('#mainForm input[name="hopper_load"]').val(t);

            console.log("Submit!")
            return true;
        });
