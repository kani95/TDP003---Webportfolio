$('document').ready(main);

// Search-bar listener
function setListeners() {
    $("#search-input").on("input", setSearchInput);
}

function setProjectDir() {
    // get all folders in our .directory-list
    const allFolders = $(".directory-list li > ul");
    const clickArray = [];
    index = 0;
    allFolders.each(function () {
        // add the folder class to the parent <li>
        const folderAndName = $(this).parent();
        folderAndName.addClass("folder");

        // backup this inner <ul>
        const backupOfThisFolder = $(this);

        // then delete it
        $(this).remove();

        // add an <a> tag to whats left ie. the folder name
        if (index === 0) {
            folderAndName.wrapInner("<a id='root-dir' class='pulse' href='javascript:void(0)'/>");
        }
        else {
            folderAndName.wrapInner("<a href='javascript:void(0)' />");
        }

        // then put the inner <ul> back
        folderAndName.append(backupOfThisFolder);

        // now add a slideToggle to the <a> we just added
        folderAndName.find("a").click(function (e) {
            $(this).siblings("ul").slideToggle("slow", function() {
                doneRootDir();
            });
        });

        clickArray.push(folderAndName.find('a'));
        index++;
    })

    clickArray.reverse().forEach((e) => e.click());
}

function doneRootDir () {
    $('.directory-container').removeClass('invisible')
}


const setupRootDir = function () {
    $('#root-dir').click(e => {
        e.target.classList.remove('pulse')
    });
}

const setSearchInput = () => {
    const search_btn = $("#search-btn");
    if ($("#search-input").val() !== undefined) {
        if ($("#search-input").val().length > 0) {
            search_btn.addClass('active-search');
        } else {
            search_btn.removeClass('active-search');
        }
    }
}

function setupMagicBorder() {
    $('.magic-border').mousemove(function(e) {

        const x = e.pageX - e.target.offsetLeft
        const y = e.pageY - e.target.offsetTop
    
        e.target.style.setProperty('--x', `${ x }px`)
        e.target.style.setProperty('--y', `${ y }px`)
    })
}

function main() {
    setListeners();
    setSearchInput();
    setProjectDir();
    setupRootDir();
    setupMagicBorder();
}