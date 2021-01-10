from data_scraper.scraper import Scraper

my_scraper = Scraper(0)
my_scraper.get_all_property_data(500,
                                 "https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=6&search%5Bcity_id%5D=38&search%5Bdistrict_id%5D=54&nrAdsPerPage=72")
