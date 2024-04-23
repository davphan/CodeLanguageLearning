"use strict";

(function() {
  window.addEventListener("load", init);

  async function init() {
    document.querySelector("form").addEventListener("submit", (e) => {
      e.preventDefault();
      sumbitForm();
    })
    document.querySelector("button").addEventListener("click", () => {
      alert("i ben clickd")
    })
  }

  async function sumbitForm() {
    let data = new FormData(document.querySelector("form"));
    let response = await fetch("/input", {method: "POST", body: data})
  }
}) ();