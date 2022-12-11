# Main Function
# TODO 1 -> Add Ideas
# TODO 2 -> View Idea By Title
# TODO 3 -> Search Idea By Title
# TODO 4 -> Show All Ideas
# TODO 5 -> Delete/Edit

# Structure
# idealist add-idea
# idealist add-idea --title / details/ status
#
# idealist view-idea
# idealist search
# idealist show-all


import click
from database import connectDB
import terminaltables
from click_help_colors import HelpColorsGroup, HelpColorsCommand


@click.group(cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="green")
@click.version_option(prog_name="idealist", version="0.01")
def main():
    """Idealist Cli"""
    pass


@main.command()
@click.option("--title", "-t", help="Provide the Title", type=str, prompt=True)
@click.option("--detail", "-d", help="Provide the detail", type=str, prompt=True)
@click.option("--status", "-s", help="Provide the status", prompt=True, type=click.Choice(["ToDo", "Doing", "Done"]))
def add_idea(title, detail, status):
    """Add Idea To Database"""
    click.echo("Adding a new Idea to Database")
    click.secho(f"\n\nSuccessfully Added {title} to Database", fg="green")
    click.echo("\n\n\n============Summary=============")
    # table
    connectDB.create_table()
    connectDB.add_data(title, detail, status)
    user_idea = [["Idea Info", "Details"], ["Title", title], ["Detail", detail], ["Status", status]]
    table_1 = terminaltables.AsciiTable(user_idea)
    click.echo(table_1.table)


@main.command()
@click.option("--title", "-t", prompt=True)
def view_idea(title):
    """Get idea by Title """
    click.secho(f"\n\nSearched for Title::{title}\n\n", fg="green")
    result = connectDB.get_single_idea_by_title(title)
    table = terminaltables.AsciiTable(result)
    click.echo(table.table)


@main.command()
@click.argument("text", type=str)
@click.option("--by", "-b", default="Title", help="Option To Search By", type=click.Choice(["Title", "Detail", "Status"]))
def search(by, text):
    """Search By Option -> Title | Detail |  Status"""
    click.secho(f"\n\nSearching for {by}::{text}\n\n", fg="green")
    result = None
    if by == "Title":
        result = connectDB.get_single_idea_by_title(text)
    elif by == "Detail":
        result = connectDB.get_single_idea_by_detail(text)
    elif by == "Status":
        result = connectDB.get_single_idea_by_status(text)

    if not result:
        click.secho(f"No Match Found for {by} = {text}", fg="red")
        return

    table = terminaltables.AsciiTable(result)
    click.echo(table.table)


@main.command()
def show_all():
    """Show all idea"""
    click.echo("Showing all ideas")
    click.echo("\n\n====================")
    result = connectDB.view_data()
    result_table_header = ["Title", "Detail", "Status"]
    click.secho(f"{result_table_header}")
    result_table = terminaltables.AsciiTable(result)
    click.echo(result_table.table)


if __name__ == "__main__":
    main()
