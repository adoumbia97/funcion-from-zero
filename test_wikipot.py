from mylib.bot import scrape
from click.testing import CliRunner
from wikipot import cli



def test_scrape():
   # runner=CliRunner()
   # result=runner.invoke(scrape)
    
    assert "Microsoft" in scrape()


def test_cli():
    runnner=CliRunner()
    result=runnner.invoke(cli)
    assert "Microsoft" in result.output