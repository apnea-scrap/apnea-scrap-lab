window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]]
  },
  options: {
    processHtmlClass: "arithmatex"
  }
};

function typesetMath() {
  if (window.MathJax) {
    window.MathJax.typesetPromise();
  }
}

document.addEventListener("DOMContentLoaded", typesetMath);

if (window.document$) {
  window.document$.subscribe(typesetMath);
}
