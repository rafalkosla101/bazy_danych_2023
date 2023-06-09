let minRangeValueGap = 1;
const range = document.getElementById("temperature");
const minval = document.querySelector(".temp_min");
const maxval = document.querySelector(".temp_max");
const rangeInput = document.querySelectorAll(".temp");

let minRange, maxRange, minPercentage, maxPercentage;
    const minRangeFill = () => {
  range.style.left = (0 / rangeInput[0].max) * 100 + "%";
}
const maxRangeFill = () => {
  range.style.right = 100-(0 / rangeInput[1].max) * 100 + "%";
}
const MinVlaueBubbleStyle = () => {
  minPercentage = (0 / rangeInput[0].max) * 100
  minval.style.left = minPercentage + "%"
  minval.style.transform = `translate(-${minPercentage /2}%, -100%)`
}
const MaxVlaueBubbleStyle = () => {
  maxPercentage = 0
  maxval.style.right = maxPercentage + "%"
  maxval.style.transform = `translate(${maxPercentage / 2}%, 100%)`
}

const setMinValueOutput = () => {
  minRange = parseInt(rangeInput[0].value);
  minval.innerHTML = rangeInput[0].value
}
const setMaxValueOutput = () => {
  maxRange = parseInt(rangeInput[1].value);
  maxval.innerHTML = rangeInput[1].value
}
  setMinValueOutput()
setMaxValueOutput()
minRangeFill()
maxRangeFill()
MinVlaueBubbleStyle()
MaxVlaueBubbleStyle()

rangeInput.forEach((input) => {
input.addEventListener("input", (e) => {
setMinValueOutput();
setMaxValueOutput();

minRangeFill();
maxRangeFill();

MinVlaueBubbleStyle();
MaxVlaueBubbleStyle();

if (maxRange - minRange < minRangeValueGap) {
  if (e.target.className === "min") {
    rangeInput[0].value = maxRange - minRangeValueGap;
    setMinValueOutput();
    minRangeFill();
    MinVlaueBubbleStyle();
    e.target.style.zIndex = "2"
  }
  else {
    rangeInput[1].value = minRange + minRangeValueGap;
    e.target.style.zIndex = "2"
    setMaxValueOutput();
    maxRangeFill();
    MaxVlaueBubbleStyle();
  }
}

});
});