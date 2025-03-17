"""
 Bloom Filters - Membership Check 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Bloom Filters - Membership Check"
__author = "kalyan359"

def __algorithm():
    bloom_filter_list = [True, False, True, True, True, False, True, False, False, False]
    word_list = ['Kalyan','Chris Laffra','Chris','Chandra','Python']

    def hash_func1(word):
        # for simplicity sake, picked default hash function
        # speed of bloom filter depends on speed of hash function
        # performance of bloom filter on uniform distribution nature of hash func
        # famous hash functions are fnv,murmur etc.
        return abs(hash(word))%10

    def hash_func2(word):
        return (sum([ord(i) for i in list(word)])%23)%10

    for word in word_list:
        if bloom_filter_list[hash_func1(word)] and bloom_filter_list[hash_func2(word)]:
            print(word + ' may exist in data set')
        else:
            print(word + ' does not exist in data set')

def __visualization():
    X, Y, D = 100, 150, 40
    y=0

    rect(X, 72,450, 40, '#333')
    text(X+15, 102, 'Membership Check using Bloom Filter', 25, color='lightblue')

    def draw_grid(word):
        text(200, 250,'Word Test:', 15)
        rect(305, 225, 150,40, '#333')
        text(315, 250,word,20,color='lightblue')
        color1 = 'black' if bloom_filter_list[hash_func1(word)] else 'red'
        color2 = 'black' if bloom_filter_list[hash_func2(word)] else 'red'
        text(200, 300,'Hash 1 value:', 15)
        rect(305, 275, 30,30, color1)
        text(315, 300,hash_func1(word),20,color='lightblue')
        text(200, 335,'Hash 2 value:', 15)
        rect(305, 320, 30,30, color2)
        text(315, 340,hash_func2(word),20,color='lightblue')
        if color1 == 'black' and color2 == 'black':
            rect(175, 370, 300,40, 'black')
            text(215, 390, word + ' may exist in dataset', 15,color='lightblue')
        else:
            rect(175, 370, 300,40, 'red')
            text(215, 390, word + ' does not exist in dataset', 15,color='lightblue')
        
        
    
    def final_data_grid(bloom_filter_list):
        for x in range(10):
            color = 'teal' if bloom_filter_list[x] else 'orange'
            rect(X+x*D, Y+y*D, D-5, D-5, color)
            text(X+x*D+2, Y+y*D+D/2, x, 15)


    draw_grid(word)
    final_data_grid(bloom_filter_list)