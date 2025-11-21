list = ['item one', 'item two', 'item three', 'item four', 'item five', 'item six', 'item seven']

def wp_list(list):
    list_item = ['<ul>']
    for item in list:
        single_list = f'<li>{item}</li>'
        list_item.append(single_list)
    list_item.append('</ul>')

    list_from_string = ''.join(list_item)
    final_list = f'<!-- wp:list -->{list_from_string}<!-- /wp:list -->'
    return final_list

fruits = ['apple', 'banana', 'jackfruit', 'chery']
new_list = wp_list(fruits)
print(new_list)