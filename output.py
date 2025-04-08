'''These are the modules we are going to need for making the design better'''
from rich import print as rprint
from rich.rule import Rule
from rich.panel import Panel
from rich.table import Table
from rich.console import Console , Group
from rich.prompt import Prompt
#dont worry about these imports :)
def space():
    '''#prints a line to seprate the section'''
    rule = Rule(style="bold cyan", align="center")
    rprint(rule)

def user_input():
    '''#use this to get input from the users it makes it more cute'''
    user_command = Prompt.ask("[bold blue]>>> [/bold blue]" )
    return user_command

def t_header(text):
    '''#use this for headers'''
    header = Rule(f"{text}", style="bold yellow")
    rprint(header)

def t_description(text=" ", maintitle=None):
    '''#this is for the description but i advise to run the program once
    to see how it looks and dont just use it everywhere'''
    description = Panel(
        text,
        title=maintitle,
        subtitle=None,
        style="dim white",
        border_style="cyan",
    )
    rprint(description)

def t_select(*rows , s=0):
    '''#use the main code as example and give the options to the user like this'''
    table = Table(title="Choose an Option Or If You Want to Quit Enter 'exit'")
    table.add_column("Option", justify="center", style="bold yellow", no_wrap=True)
    table.add_column("Description", justify="left", style="cyan")

    for index, row in enumerate(rows, start=s):
        table.add_row(str(index), row)
    rprint(table)

def m_error(message):
    '''# prints an error message'''
    rprint(f"[bold red]✗ Error:[/bold red] {message} ,Please try again.")

def m_success(message):
    '''#prints a success message'''
    rprint(f"[bold green]✓ Success:[/bold green] {message}")

def m_info(message):
    '''#This is pretty much useless we use it for showing whic page is the user on'''
    rprint(f"[bold blue]ℹ Info:[/bold blue] {message}")

def m_post(mydict):
    '''#we use this to show a post to the user'''

    console = Console()

    table = Table(title="Post Details")

    table.add_column("Field", style="bold cyan", justify="left")
    table.add_column("Value", style="bold yellow", justify="left")

    table.add_row("👤 Author", mydict["author"])
    table.add_row("📅 Date", f"{mydict['year']}/{mydict['month']:02}/{mydict['day']:02}")
    table.add_row("📝 Caption", mydict["caption"])
    table.add_row("👍 Likes", str(mydict["like"]))
    table.add_row("💬 Comments Count", str(mydict["comment"]))
    table.add_row("📌 Saves", str(mydict["save"]))
    table.add_row("🔗 Shares", str(mydict["share"]))

    comments_table = Table(title="💬 Comments")
    comments_table.add_column("👥 User", style="cyan", justify="left")
    comments_table.add_column("🗨️ Comment", style="yellow", justify="left")

    for user, comment in mydict["comments"]:
        comments_table.add_row(user, comment)

    group = Group(table, comments_table)

    panel = Panel(
        group,
        title="📸 Instagram Post",
        title_align="center",
        border_style="bright_magenta",
    )

    console.print(panel)
