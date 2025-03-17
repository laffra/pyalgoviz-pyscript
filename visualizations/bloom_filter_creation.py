"""
 Bloom Filter - Creation 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Bloom Filter - Creation"
__author = "kalyan359"

def __algorithm():
    #One of the algorithms which has blown my mind is a Bloom filter! 
    #I liked the concept very much, and it comes to my mind once every day because of its sheer awesomeness.
    #It operates in a humble humble small array and produces super quick results!
    #sad :( hashlib is not supported here, so came up with some dummy hash functions.

    #import hashlib

    def bloom_filter():
        #size of bloom filter is very important
        #bigger the bloom filter is, the better is its performance(fewer false positives)
        #also, bloom filters are bitvectors and not lists
        #here for simplicity purpose, consider bloomfilter as a list of size 10.
        return [False]*10

    def hash_func1(word):
        # for simplicity sake, picked default hash function
        # speed of bloom filter depends on speed of hash function
        # performance of bloom filter on uniform distribution nature of hash func
        # famous hash functions are fnv,murmur etc.
        return abs(hash(word))%10

    def hash_func2(word):
        return (sum([ord(i) for i in list(word)])%23)%10

    def insert_bloom_filter(word):
        bloom_filter_list[hash_func1(word)] = True
        bloom_filter_list[hash_func2(word)] = True


    bloom_filter_list = bloom_filter()
    word_list = ['Kalyan','Chandra','Chris','Laffra']
    #removed the map usage to make the visualization code easy
    #map(insert_bloom_filter,word_list)
    for word in word_list:
        insert_bloom_filter(word)

    print(bloom_filter_list)

def __visualization():
    X, Y, D = 100, 150, 40
    y=0

    rect(X, 72, 495, 40, '#333')
    text(X+75, 102, 'Bloom Filter Creation', 30, color='lightblue')

    def draw_grid(word):
        text(200, 250,'Word inserted:', 15)
        rect(305, 225, 100,30, '#333')
        text(315, 250,word,20,color='lightblue')
        text(200, 300,'Hash 1 value:', 15)
        rect(305, 275, 30,30, '#333')
        text(315, 300,hash_func1(word),20,color='lightblue')
        text(200, 335,'Hash 2 value:', 15)
        rect(305, 320, 30,30, '#333')
        text(315, 340,hash_func2(word),20,color='lightblue')
        for x in range(10):
            color = 'teal' if x==hash_func1(word) or x==hash_func2(word) else 'orange'
            rect(X+x*D, Y+y*D, D-5, D-5, color)
            text(X+x*D+2, Y+y*D+D/2, x, 15)

    def final_data_grid(bloom_filter_list):
        for x in range(10):
            color = 'teal' if bloom_filter_list[x] else 'orange'
            rect(X+x*D, Y+y*D, D-5, D-5, color)
            text(X+x*D+2, Y+y*D+D/2, x, 15)


    draw_grid(word)
    final_data_grid(bloom_filter_list)