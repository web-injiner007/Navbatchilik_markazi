let baza = "{% static 'images/baza.png' %}";
let grandstream = "{% static 'images/grandstre.png' %}";
let panasonic = "{% static 'images/panasonic.png' %}";
let vlan = "{% static 'images/panasonic.png' %}";

// ====== DATA ======
const linesData1 = [
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: false },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: false },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: false },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: false },
];

const tree = document.getElementById("treeList");

tree.innerHTML = linesData1
  .map(
    (item) => `
    <li>
       ${item.toWork ? "" : '<span class="li-date">03.10.2025 11:54</span>'}
       
      <div class="box ${
        item.toWork ? "active" : "inactive"
      }" onclick="openWindow()">
        ${item.text}
        <p>${item.angle}</p>
      </div>
      <div class="img-box">
        <img src="{% static 'images/baza.png' %}" alt="baza"/>
      </div>
    </li>
  `
  )
  .join("");

const linesData2 = [
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: false },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: false },
];

const tree2 = document.getElementById("treeList2");

tree2.innerHTML = linesData2
  .map(
    (item) => `
    <li>
     ${item.toWork ? "" : '<span class="li-date">03.10.2025 11:54</span>'}
      <div class="box ${
        item.toWork ? "active" : "inactive"
      }" onclick="openWindow2()">
        ${item.text}
        <p>${item.angle}</p>
      </div>
      <div class="img-box">
        <img src="{% static 'images/grandstre.png' %}" alt="baza"/>
      </div>
    </li>
  `
  )
  .join("");

const linesData3 = [
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: false },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: false },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: false },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
];

const tree3 = document.getElementById("treeList3");

tree3.innerHTML = linesData3
  .map(
    (item) => `
    <li>
     ${item.toWork ? "" : '<span class="li-date">03.10.2025 11:54</span>'}
      <div class="box ${
        item.toWork ? "active" : "inactive"
      }" onclick="openWindow3()">
        ${item.text}
        <p>${item.angle}</p>
      </div>
      <div class="img-box">
        <img src="{% static 'images/panasonic.png' %}" alt="baza"/>
      </div>
    </li>
  `
  )
  .join("");

const linesData4 = [
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: false },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Toshkent", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: false },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
  { angle: "20.0.0.101", text: "Samarqand", toWork: true },
  { angle: "20.0.0.101", text: "Navoiy", toWork: true },
  { angle: "20.0.0.101", text: "Buxoro", toWork: true },
];

const tree4 = document.getElementById("treeList4");

tree4.innerHTML = linesData4
  .map(
    (item) => `
    <li>
     ${item.toWork ? "" : '<span class="li-date">03.10.2025 11:54</span>'}
      <div class="box ${
        item.toWork ? "active" : "inactive"
      }" onclick="openWindow4()">
        ${item.text}
        <p>${item.angle}</p>
      </div>
      <div class="img-box">
        <img src="{% static 'images/switch.png' %}" alt="baza"/>
      </div>
    </li>
  `
  )
  .join("");

let visibleBox = document.getElementById("visible-id");
let visibleBox2 = document.getElementById("visible-id2");
let visibleBox3 = document.getElementById("visible-id3");
let visibleBox4 = document.getElementById("visible-id4");

function openWindow() {
  visibleBox.classList.add("visible-active");
  visibleBox2.classList.remove("visible-active");
  visibleBox3.classList.remove("visible-active");
  visibleBox4.classList.remove("visible-active");
}

function openWindow2() {
  visibleBox2.classList.add("visible-active");
   visibleBox.classList.remove("visible-active");
  visibleBox3.classList.remove("visible-active");
  visibleBox4.classList.remove("visible-active");
}

function openWindow3() {
  visibleBox3.classList.add("visible-active");
   visibleBox2.classList.remove("visible-active");
  visibleBox.classList.remove("visible-active");
  visibleBox4.classList.remove("visible-active");
}

function openWindow4() {
  visibleBox4.classList.add("visible-active");
   visibleBox2.classList.remove("visible-active");
  visibleBox3.classList.remove("visible-active");
  visibleBox1.classList.remove("visible-active");
}

function visibleClose() {
  visibleBox.classList.remove("visible-active");
}

function visibleClose2() {
  visibleBox2.classList.remove("visible-active");
}

function visibleClose3() {
  visibleBox3.classList.remove("visible-active");
}

function visibleClose4() {
  visibleBox4.classList.remove("visible-active");
}
