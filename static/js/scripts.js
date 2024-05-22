function changePage(increment) {
    let pageNumberElement = document.getElementById("page-number");
    let currentPage = parseInt(pageNumberElement.innerHTML, 10);

    if (isNaN(currentPage)) {
        currentPage = 1
    }

    let newPage = currentPage + increment;

    if (newPage < 1) {
        newPage = 1;
    }

    $.ajax({
        url: '/movies',
        type: 'GET',
        data: {'page': newPage},
        success: function(response) {
            document.querySelector('.content').innerHTML = response;
            pageNumberElement.innerHTML = newPage;
        },
        error: function(error) {
            console.log(error);
        }
    });
}
