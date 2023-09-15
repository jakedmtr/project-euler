""" A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 × 99. 

Find the largest palindrome made from the product of 
two 3-digit numbers """

def ispalindrome(number):
    """ returns true if numer is a palindrome """
    number = list(str(number))
    first_slice = []
    second_slice = []
    if len(number) % 2 == 0:
        for digit in number[:len(number)//2]:
            first_slice.append(digit)
        for digit in number[len(number)//2:]:
            second_slice.append(digit)
        second_slice.reverse()
    else:
        for digit in number[:(len(number)//2)]:
            first_slice.append(digit)
        for digit in number[(len(number)//2)+1:]:
            second_slice.append(digit)
        second_slice.reverse()
    if first_slice == second_slice:
        return True
    else:
        return False

def largestpalindrome3d():
    """ returns the largest palindrome from two three-digit numebrs """
    num1 = 999
    num2 = 999
    palindromes = []
    while num1 > 99:
        while num2 > 99:
            #print(f"{num1} x {num2} = {num1*num2}")
            if ispalindrome(num1*num2) and num1*num2 not in palindromes:
                palindromes.append(num1*num2)
            num2 -= 1
        num2 = 999
        num1 -= 1
    return max(palindromes)