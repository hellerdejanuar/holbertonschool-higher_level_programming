$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (req) {
  $.each(req.results, function (index, element) { 
    $('UL#list_movies').append("<li>" + element.title + "</li>");
  });
});