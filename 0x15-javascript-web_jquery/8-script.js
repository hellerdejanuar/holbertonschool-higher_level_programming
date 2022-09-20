$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function (req) {
  $.each(req.results, function (element => { 
    $('UL#list_movies').append("<li>" + element.name + "</li>");
    console.log(element.name);
  });
});
