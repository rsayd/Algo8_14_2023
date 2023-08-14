"""
Balance Index

Here, a balance point is ON an index, not between indices.

Return the balance index where sums are equal on either side
exclude its own value).

Return -1 if none exist.

"""

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
  // Pseudocode your game plan
  // your code here
}

console.log(balanceIndex(nums1), 'should equal', expected1);
console.log(balanceIndex(nums2), 'should equal', expected2);


Answer:

function balanceIndex(nums) {
    // Variables
    let lsum = 0;
    let rsum = 0;

    // If array length is less than 3, return -1.
    if (nums.length < 3) {
        return -1;
    }
    // Outer for loop continually sums the left of i.
    for (let i = 1; i < nums.length - 1; i++) {
        lsum += nums[i-1];
        // Inner for loop iterates through and sums right of i.
        for (let j = i + 1; j < nums.length; j++) {
            rsum += nums[j];
        }
        // If left sum equals right sum, return the index.
        if (lsum == rsum) {
            return i;
        }
        // Reset the right sum for the next iteration of i.
        rsum = 0;
    }
    // If left sum never equals right sum, return -1.
    return -1
}