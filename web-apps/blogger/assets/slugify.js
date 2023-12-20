const title_input = document.querySelector('input[name=title]');
const slug_input = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g,'-and-')      // replace & with '-and-' 
        .replace(/[\s\W-]+/g, '-'); // replace spaces, non word chars and dashes with single dash
};

title_input.addEventListener('keyup', (e)=> {
    slug_input.setAttribute('value', slugify(title_input.value));
} );