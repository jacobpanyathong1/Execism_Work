export function needsLicense(kind) {

  const withLicense = ['truck', 'car'];

  if (withLicense.includes(kind)) {

    return true;
  }
  else {

    return false;

  }
}


export function chooseVehicle(option1, option2) {

  const year1 = (option1.match(/\d{4}/) || [Infinity])[0];

  const year2 = (option2.match(/\d{4}/) || [Infinity])[0];

  if (year1 < year2) return option1 + ' is clearly the better choice.';

  if (year2 < year1) return option2 + ' is clearly the better choice.';

  const alphanumeric1 = (option1.match(/[a-zA-Z0-9]+/g) || []).join('');

  const alphanumeric2 = (option2.match(/[a-zA-Z0-9]+/g) || []).join('');

  return alphanumeric1 <= alphanumeric2 ? option1 + ' is clearly the better choice.' : option2 + ' is clearly the better choice.';
}



export function calculateResellPrice(originalPrice, age) {
  if (age < 3) {
    return originalPrice * 0.80;
  }
  if (age > 10) {
    return originalPrice * 0.50;
  }
  return originalPrice * 0.70;
}


