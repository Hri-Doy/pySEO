import httpx
urls_list = [
    'https://mewmewshopbd.com/blog/best-dog-food',
    'https://www.dogfoodadvisor.com/',
    'https://www.petmd.com/dog/vet-verified/best-dog-food',
    'https://www.purepetsfood.com/best-dog-food-in-bangladesh/',
    'https://www.chewy.com/b/dry-food-294',
    'https://www.allaboutdogfood.co.uk/',
    'https://www.petsathome.com/product/listing/dog/dog-food',
    'https://headsupfortails.com/collections/dog-food?srsltid=AfmBOoq0pbXGPlM-yLKvsvCg4BkoYuMbAVup7tDHOG85KAjj_qTde36U'
]

for url in urls_list:
    r = httpx.get(url)
    print(url, r.status_code, sep = "......")