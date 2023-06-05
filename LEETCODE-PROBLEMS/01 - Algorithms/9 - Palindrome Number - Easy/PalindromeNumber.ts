/* Given an integer x, return true if x is a 
 *  palindrome, and false otherwise.
 */
class PalindromeNumber {

    /**
     * Returns true if x is palindrome
     * and returns false if not
     * @param x input integer
     * @returns boolean representation of palindrome status of x
     */
    public isPalindrome(x: number): boolean {
        let rev: string = x.toString().split("").reverse().join(""); // supposedly the ts equivalent of python slicing
        return rev===x.toString();
    }
}