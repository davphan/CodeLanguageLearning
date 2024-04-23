"use strict";

(function() {
  window.addEventListener("load", init);

  function init() {
    document.querySelector("form").addEventListener("submit", (e) => {
      e.preventDefault();

    });
  }

  async function submitForm() {
    let params = new FormData(document.querySelector("form"));
    let response = await fetch("/")
  }
}) ();