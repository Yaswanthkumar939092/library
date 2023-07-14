// // refresh:function(frm) {
//     var pageHeadContent = document.getElementsByClassName('page-head-content')

//     var searchInput = document.createElement('input');
//     searchInput.type = 'search';
//     searchInput.placeholder = 'Search...';
//     searchInput.value = 'Google Access'; // Pre-populate with "Google Access"

//     pageHeadContent.appendChild(searchInput);
// //   }


function hey() {
    let elements = document.getElementsByClassName('navbar');
    // for (let i = 0; i < elements.length; i++) {
        elements.style.setProperty('background-color', 'blue', '!important');
    // }
}

setTimeout(hey, 1000);
