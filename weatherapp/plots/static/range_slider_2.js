const range2 = document.getElementById("wind_speed");
const minval2 = document.querySelector(".wind_speed_min");
const maxval2 = document.querySelector(".wind_speed_max");
const rangeInput2 = document.querySelectorAll(".wind_speed");

let minRange2, maxRange2, minPercentage2, maxPercentage2;
    const minRangeFill2 = () => {
  range.style.left = (0 / rangeInput2[0].max) * 100 + "%";
}
const maxRangeFill2 = () => {
  range.style.right = 100-(0 / rangeInput2[1].max) * 100 + "%";
}
const MinVlaueBubbleStyle2 = () => {
  minPercentage2 = (0 / rangeInput2[0].max) * 100
  minval2.style.left = minPercentage2 + "%"
  minval2.style.transform = `translate(-${minPercentage2 /2}%, -100%)`
}
const MaxVlaueBubbleStyle2 = () => {
  maxPercentage2 = 0
  maxval2.style.right = maxPercentage2 + "%"
  maxval2.style.transform = `translate(${maxPercentage2 / 2}%, 100%)`
}

const setMinValueOutput2 = () => {
  minRange2 = parseInt(rangeInput2[0].value);
  minval2.innerHTML = rangeInput2[0].value
}
const setMaxValueOutput2 = () => {
  maxRange2 = parseInt(rangeInput2[1].value);
  maxval2.innerHTML = rangeInput2[1].value
}
  setMinValueOutput2()
setMaxValueOutput2()
minRangeFill2()
maxRangeFill2()
MinVlaueBubbleStyle2()
MaxVlaueBubbleStyle2()

rangeInput2.forEach((input) => {
input.addEventListener("input", (e) => {
setMinValueOutput2();
setMaxValueOutput2();

minRangeFill2();
maxRangeFill2();

MinVlaueBubbleStyle2();
MaxVlaueBubbleStyle2();

if (maxRange2 - minRange2 < minRangeValueGap2) {
  if (e.target.className === "min") {
    rangeInput2[0].value = maxRange2 - minRangeValueGap2;
    setMinValueOutput2();
    minRangeFill2();
    MinVlaueBubbleStyle2();
    e.target.style.zIndex = "2"
  }
  else {
    rangeInput2[1].value = minRange2 + minRangeValueGap2;
    e.target.style.zIndex = "2"
    setMaxValueOutput2();
    maxRangeFill2();
    MaxVlaueBubbleStyle2();
  }
}

});
});