def heading_one(text):
    return f'<h1>{text}</h1>'

def heading_two(text):
    return f'<h2>{text}</h2>'

def para(text):
    return f'<p>{text}</p>'


def heading(type, text):
    return f'<{type}>{text}</{type}>'
h1 = heading('h1', 'This is a heading')
print(h1)

def paragraph(type, text):
    return f'<{type}>{text}</{type}>'
p = paragraph('p', 'This is a paragraph')
print(p)