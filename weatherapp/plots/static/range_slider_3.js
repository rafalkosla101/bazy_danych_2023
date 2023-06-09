const range3 = document.getElementById("wind_direction");
const minval3 = document.querySelector(".wind_direction_min");
const maxval3 = document.querySelector(".wind_direction_max");
const rangeInput3 = document.querySelectorAll(".wind_direction");

let minRange3, maxRange3, minPercentage3, maxPercentage3;
    const minRangeFill3 = () => {
  range.style.left = (0 / rangeInput3[0].max) * 100 + "%";
}
const maxRangeFill3 = () => {
  range.style.right = 100-(0 / rangeInput3[1].max) * 100 + "%";
}
const MinVlaueBubbleStyle3 = () => {
  minPercentage3 = (0 / rangeInput3[0].max) * 100
  minval3.style.left = minPercentage3 + "%"
  minval3.style.transform = `translate(-${minPercentage3 /2}%, -100%)`
}
const MaxVlaueBubbleStyle3 = () => {
  maxPercentage3 = 0
  maxval3.style.right = maxPercentage3 + "%"
  maxval3.style.transform = `translate(${maxPercentage3 / 2}%, 100%)`
}

const setMinValueOutput3 = () => {
  minRange3 = parseInt(rangeInput3[0].value);
  minval3.innerHTML = rangeInput3[0].value
}
const setMaxValueOutput3 = () => {
  maxRange3 = parseInt(rangeInput3[1].value);
  maxval3.innerHTML = rangeInput3[1].value
}
  setMinValueOutput3()
setMaxValueOutput3()
minRangeFill3()
maxRangeFill3()
MinVlaueBubbleStyle3()
MaxVlaueBubbleStyle3()

rangeInput3.forEach((input) => {
input.addEventListener("input", (e) => {
setMinValueOutput3();
setMaxValueOutput3();

minRangeFill3();
maxRangeFill3();

MinVlaueBubbleStyle3();
MaxVlaueBubbleStyle3();

if (maxRange3 - minRange3 < minRangeValueGap3) {
  if (e.target.className === "min") {
    rangeInput3[0].value = maxRange3 - minRangeValueGap3;
    setMinValueOutput3();
    minRangeFill3();
    MinVlaueBubbleStyle3();
    e.target.style.zIndex = "2"
  }
  else {
    rangeInput3[1].value = minRange3 + minRangeValueGap3;
    e.target.style.zIndex = "2"
    setMaxValueOutput3();
    maxRangeFill3();
    MaxVlaueBubbleStyle3();
  }
}

});
});