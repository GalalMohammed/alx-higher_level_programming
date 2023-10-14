$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (movies) {
    $.each(movies, function (i, movie) {
	    $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
