let cells = document.getElementsByTagName('td');

for (let cell of cells) {
    console.log(cell);
    if (cell.textContent.includes("True")) {
        cell.style.color = "green";
    } else {
        cell.style.color = "red";
    }
}