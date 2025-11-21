def wp_para(text):
    return f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
def wp_heading_two(heading):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{heading}</h2><!-- /wp:heading -->'

intro = 'history of Bangladesh, a survey of the notable events and people in the history of Bangladesh, from the 3rd century bce to the present day. Bangladesh, located in the northeastern region of the Indian subcontinent, has been independently ruled since 1971, but the land and peoples of the modern country have centuries-long histories that centre on the thriving delta of the Ganges River. Dhaka is the capital of Bangladesh, having previously served as the capital city of Bengal province during the Mughal dynasty (1608–39 and 1660–1704), East Bengal province (1947), and East Pakistan (1956).'
h2 = 'Buddhist, Hindu, and Muslim dynasties until about 1700'
outro = 'From the 3rd century bce Buddhism flourished as the Mauryan emperors extended their influence in Bengal. Under the Gupta kings, who reigned from the early 4th to the late 6th century ce, Hinduism reestablished its hold, but Buddhism did not fully disappear. The two religions coexisted under the Pala dynasty (8th–12th century), as well as under the Chandra dynasty (10th–11th century) in the southeast. By the end of the 11th century, the Senas, who were strongly Hindu, had gained control over a large part of Bengal.'

content = (
    wp_para(intro) + 
    wp_heading_two(h2) + 
    wp_para(outro)
)

print(content)