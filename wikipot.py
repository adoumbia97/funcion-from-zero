import wikipedia
import  click


#We can use the click framwork to handle argument:
## option, means positionnal, is_flag means boolean

@click.command()
@click.option('--name', prompt="Wikipedia to scrape",help='Web pase we want to scrabe', default='Microsoft')
def scrape(name="Microsoft", length=1):
    result= wikipedia.summary(name, sentences=length)
    click.echo(click.style(f"{result}", fg="white", bg="blue")) 

if __name__=='__main__':
    scrape()