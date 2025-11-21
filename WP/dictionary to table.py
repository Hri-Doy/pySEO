'''
<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody>

<tr><td>Key</td><td>value</td></tr><tr><td>key</td><td>value</td></tr>

</tbody></table></figure><!-- /wp:table -->
'''

def dictionary_table(dictionary):
    codes = f'<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes

my_data = {
    'name' : 'Hriday',
    'age':25,
    'look':'Brown'
}

test = dictionary_table(my_data)
print(test)