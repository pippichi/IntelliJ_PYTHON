KEY_WORDS = ['交通','停车','态度','上菜','性价比']
GOOD_LEVELS = ['好','便','容易','行','可以','满意','快']
BAD_LEVELS = []
for i in GOOD_LEVELS:
    BAD_LEVELS.append('不\w{0,10}'+i)