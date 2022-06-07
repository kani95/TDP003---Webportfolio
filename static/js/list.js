$('document').ready(main);

// Search-bar listener
function setListeners() {
    $("#search-input").on("input", () => {
        const search_btn = $("#search-btn");
        if ($("#search-input").val().length > 0) {
            search_btn.addClass('active-search');
        } else {
            search_btn.removeClass('active-search');
        }
        console.log("hello")
    });
}


function main() {
    setListeners();
}