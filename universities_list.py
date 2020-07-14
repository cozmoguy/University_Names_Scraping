from selenium import webdriver

browser = webdriver.Chrome()


for index in range(2,28):
    browser.get(f'https://www.4icu.org/reviews/index{index}.htm')

    names = browser.find_elements_by_xpath('/html/body/div[1]/div[4]/div/table/tbody/tr')

    for i in range(len(names)):
        word = names[i].text

        word_list = word.split(' ')
        name = word.replace(' ' + word_list[-1],'')
        country = word_list[-1]

        print({
            'Name':name,
            'Country_code':country
        })

browser.close()