from wikipot import scrape
from click.testing import CliRunner



def test_scrape():
    runner=CliRunner()
    result=runner.invoke(scrape)
    assert result.exit_code == 0