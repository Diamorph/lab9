$(document).ready(function(){
        $(".delete-btn").click(function(){
            btn = $(this);
            inp = $("#delete-post");
            inp.attr("value", btn.attr("value"));
        });
});


$(document).ready(function(){
        $("#delete-post").click(function(){
            btn = $(this);
            //alert(btn.attr("value"));
            $.ajax({type: "delete", url: $(location).attr('pathname') + '?rest=' + btn.attr("value"), success: function(result){
//                alert(result);
               
                if (result.status === 'error'){
                    alert('error');}
                else
                    {$("#rest_" + btn.attr("value")).remove();}
            }});
        });
    });

$(document).ready(function(){
    $(".search").click(function(){
        btn = $(this);
        inp = $("#search");
        $.ajax({
            type: "GET",
            url : "/rest/search/",
            data: {search: inp.val(), xhr: true},
            success: function(result){
var elems ;
               elems = jQuery.parseJSON(result);
             alert(elems);
            $(".main_content").remove();

            $('#new_content').append(Mustache.to_html("{{#elems}}\
            <div class = 'cont'>\
             <p><img src = '{{image}}'></p>\
             <a href = '/rest/{{id}}' >\
             <p>Назва :'{{name}}'</p></a>\
             <p>Рейтинг :'{{rate}}'</p>\
             <p>Середній чек: '{{check}}'</p>\
             <p>Місто:'{{city}}'</p>\
             <p>Дата:'{{date}}'</p></form>\
<div>\
{{/elems}}", { elems: elems }));

            /*for(i in result)
            { $("#new_content").append('<p><img src = "'+result[i].image+'"></p><a href = "/rest/' +result[i].id +' " ><p>Назва :'+result[i].name+'</p></a><p>Рейтинг :'+result[i].rate+'</p><p>Середній чек: '+result[i].check +'</p><p>Місто:'+result[i].city+'</p><p>Дата:'+result[i].date+'</p></form>');
            };*/
           
        }});
    });
});

