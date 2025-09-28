from bs4 import BeautifulSoup

with open('web scrapping/index.html','r') as html_file:
    content=html_file.read()
    #print(content)
    #creating an instance of beautifulsoup lib
    soup=BeautifulSoup(content,'lxml')
    #print( soup.prettify() ) prettify method is used to print the html content in a structured way
    #articles_html_tags=soup.find_all('h2')
    #for article in articles_html_tags:
    #    print(article.text)
    
    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')