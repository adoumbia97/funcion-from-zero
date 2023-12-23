from wikipot import scrape

def test_scrape():
    assert "Microsoft" in scrape()