// @ts-check
//
// ☝🏽 The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion on the web
// and supported IDEs when implementing this exercise. You don't need to
// understand types, JSDoc, or TypeScript in order to complete this JavaScript
// exercise, and can completely ignore this comment block and directive.

import { Console } from "console";

// 👋🏽 Hi again!
//
// A quick reminder about exercise stubs:
//
// 💡 You're allowed to completely clear any stub before you get started. Often
// we recommend using the stub, because they are already set-up correctly to
// work with the tests, which you can find in ./freelancer-rates.spec.js.
//
// 💡 You don't need to write JSDoc comment blocks yourself; it is not expected
// in idiomatic JavaScript, but some companies and style-guides do enforce them.
//
// Get those rates calculated!

/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
const DAY_RATE = 8
export function dayRate(ratePerHour) {
  let payRate = ratePerHour * DAY_RATE;
  return payRate;
}

/**
 * Calculates the number of days in a budget, rounded down
 *
 * @param {number} budget: the total budget
 * @param {number} ratePerHour: the rate per hour
 * @returns {number} the number of days
 */


export function daysInBudget(budget, ratePerHour) {
  const TOTAL_RATE_PER_DAY = ratePerHour * DAY_RATE;
  let totalDays = budget / TOTAL_RATE_PER_DAY;
  return Math.floor(totalDays);
}

/**
 * Calculates the discounted rate for large projects, rounded up
 *
 * @param {number} ratePerHour
 * @param {number} numDays: number of days the project spans
 * @param {number} discount: for example 20% written as 0.2
 * @returns {number} the rounded up discounted rate
 */

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  /**
   * This function inputs the Hourly rate, number of days, and discount to return 
   * the overall cost for clients.
   */
  //------------------------------------------------------------------------------------
  
  //Billing Days
  const BILLING_DAYS = 22;
  //Discount Percentage
  const DISCOUNT_RATE = (1 - discount);
  // Total Daily Rate
  const TOTAL_RATE_PER_DAY = ratePerHour * DAY_RATE;
  // Applying Discount
  const DAILY_RATE_DISCOUNT = (
    ratePerHour * 
    DAY_RATE * 
    DISCOUNT_RATE
    );
  //Calculating Billing Periods
  const BILLING_PERIODS = Math.floor( 
    numDays / 
    BILLING_DAYS
    );
  // Calculating Total Days with Discount
  const TOTAL_DISCOUNT_DAYS = ( 
    BILLING_DAYS * 
    BILLING_PERIODS
    );
  // Calculating Remaining Days for Daily Rate
  const REMAINING_DAYS = (
    numDays - TOTAL_DISCOUNT_DAYS
  );
  // Total Cost with Monthly Rate
  let totalDiscountCost = ( 
    DAILY_RATE_DISCOUNT * 
    TOTAL_DISCOUNT_DAYS
    );
  // Total Cost for Daily Rate
  let totalDailyCost = (REMAINING_DAYS * TOTAL_RATE_PER_DAY);
  // Total Cost for Client
  let overallCost = Math.ceil ( 
    totalDailyCost + 
    totalDiscountCost
    );
  //Returning Overall Cost for Client
  return overallCost;
} 
