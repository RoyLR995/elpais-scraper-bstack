from pages.home_page import HomePage
from pages.opinion_page import OpinionPage

def test_scrape_opinion_articles(driver):
    home = HomePage(driver)
    opinion = OpinionPage(driver)

    home.go_to_opinion_section()

    articles = opinion.get_first_5_articles()
    for idx, article in enumerate(articles, start=1):
        opinion.extract_article_data(article, idx)

