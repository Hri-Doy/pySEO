
def wp_list(list):
    new_list = ['<ul>']
    for i in list:
        lists = f'<li>{i}</li>'
        new_list.append(lists)
    new_list.append('</ul>')
    list_from_string = ''.join(new_list)
    final_list = f'<!-- wp:list -->{list_from_string}<!-- /wp:list -->'
    return final_list
list = ['apple', 'banana', 'jackfruit', 'berry', 'mango']
fruits_list = wp_list(list)
print(fruits_list)