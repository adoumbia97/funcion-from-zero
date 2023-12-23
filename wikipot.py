import  click
from mylib.bot import  scrape


#We can use the click framwork to handle argument:
## option, means positionnal, is_flag means boolean

@click.command()
@click.option('--name', prompt="Wikipedia to scrape",help='Web pase we want to scrabe', default='Microsoft')
def cli(name="Microsoft", length=1):
    result= scrape(name, length)
    click.echo(click.style(f"{result}", fg="white", bg="blue")) 

if __name__=='__main__':
    cli()