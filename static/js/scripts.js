function changePage(increment) {
    let pageNumberElement = document.getElementById("page-number");
    let currentPage = parseInt(pageNumberElement.innerHTML, 10);

    if (isNaN(currentPage)) {
        currentPage = 1;
    }

    let newPage = currentPage + increment;

    if (newPage < 1) {
        newPage = 1;
    }

    let activeLink = document.querySelector('.nav-bar-movies .active');
    let movieList = activeLink ? activeLink.getAttribute('data-movie-list') : 'now_playing';

    $.ajax({
        url: '/movies/' + movieList,
        type: 'GET',
        data: { 'page': newPage },
        success: function(response) {
            document.querySelector('.content').innerHTML = response;
            pageNumberElement.innerHTML = newPage;
        },
        error: function(error) {
            console.log(error);
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    let currentUrl = window.location.pathname;
    let navLinks = document.querySelectorAll('.nav-bar-movies a');
    
    navLinks.forEach(function(link) {
        if (link.href.includes(currentUrl)) {
            link.classList.add('active');
        }
    });
});
