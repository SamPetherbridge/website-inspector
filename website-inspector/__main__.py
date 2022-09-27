import click
import pandas
from rich.console import Console
from seleniumwire import webdriver

console = Console()


def get_page_requests(url):
    console.log("Loading browser")
    driver = webdriver.Chrome()

    console.log("Loading " + url)
    driver.get(url)

    console.log("Waiting to conform the page has loaded.")
    driver.implicitly_wait(10)

    driver.quit()

    requested_urls = []
    for request in driver.requests:
        if request.response:
            requested_urls.append(request.url)

    return requested_urls


def save_data(data, heading, filename="export"):
    console.log("Exporting Data")
    df = pandas.DataFrame(data={heading : data})
    df.to_csv("./" + filename + ".csv", sep=',', index=False)


@click.command()
@click.option("--url", prompt="What URL would you like to analyse")
def analyse(url):
    # Get the data
    data = get_page_requests(url)

    # Export Data
    save_data(data, "Requested URLS")


if __name__ == '__main__':
    analyse()
