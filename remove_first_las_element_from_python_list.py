'''
remove_first_and_last(list_to_clean)

html = ['<h1>', 'some content', '</h1>' ]

remove_first_and_last(html) --> ['some content']

html_2= ['<h1>', 'some content', 'more, '</h1>' ]
remove_first_and_last(html_2) --> ['some content', 'more]

one, *two, three = [1, 2, 3, 4, 5] --> one = [1] , two = [2, 3, 4], three = [5]

'''

def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'some content', '</h1>']
html_2= ['<h1>', 'some content', 'more' , '</h1>']

print(remove_first_and_last(html))
print(remove_first_and_last(html_2))

