$('document').ready(main);

// Search-bar listener
function setListeners() {
    $("#search-input").on("input", setSearchInput);
}

const setSearchInput = () => {
    const search_btn = $("#search-btn");
    if ($("#search-input").val().length > 0) {
        search_btn.addClass('active-search');
    } else {
        search_btn.removeClass('active-search');
    }
}

function main() {
    setListeners();
    setSearchInput();
}