"""
 FizzBuzz 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "FizzBuzz"
__author = "chris@chrislaffra.com"

def __algorithm():
    def fizzbuzz(x):
        return ("fizzbuzz" if (x % 15==0) else 
                "fizz" if x % 3 == 0 else  
                "buzz" if x % 5 == 0 else 
                x)
            
    for x in range(1,101):
        print(x, fizzbuzz(x))

def __visualization():
    def draw(SIZE):
        for n in range(x):
            px = 30 + round(n/SIZE) * 40
            py = 35 + (n%SIZE) *25
            value = fizzbuzz(n+1)
            color, fb = (("red", "FB") if value == 'fizzbuzz' else
                         ("blue", "F") if value == 'fizz' else
                         ("orange", "B") if value == 'buzz' else
                         ("#DDD", value))
            text(px, py, fb, 20, "Arial", color)
        
    draw(15)  # try also with 9