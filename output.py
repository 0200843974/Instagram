from rich import print
from rich.rule import Rule
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.console import Group
from rich.prompt import Prompt
#dont worry about these imports :)

def space(): #prints a line to seprate the section
    rule = Rule(style="bold cyan", align="center")
    print(rule)

def COMMAND(): #use this to get input from the users it makes it more cute
    user_command = Prompt.ask("[bold blue]>>> [/bold blue]" )
    return user_command

def t_header(text): #use this for headers
    header = Rule(f"{text}", style="bold yellow")
    print(header)

def t_description(text=" ", maintitle=None): #this is for the description but i advise to run the program once to see how it looks and dont just use it everywhere
    description = Panel(
        text,
        title=maintitle,
        subtitle=None,
        style="dim white",
        border_style="cyan",
    )
    print(description)

def t_select(*rows): #use the main code as example and give the options to the user like this
    table = Table(title="Choose an Option Or If You Want to Quit Enter 'exit'")
    table.add_column("Option", justify="center", style="bold yellow", no_wrap=True)
    table.add_column("Description", justify="left", style="cyan")

    for index, row in enumerate(rows, start=0):
        table.add_row(str(index), row)
    
    print(table)

def m_error(message): # prints an error message
    print(f"[bold red]✗ Error:[/bold red] {message} ,Please try again.")

def m_success(message): #prints a success message
    print(f"[bold green]✓ Success:[/bold green] {message}")

def m_info(message):#This is pretty much useless we use it for showing whic page is the user on
    print(f"[bold blue]ℹ Info:[/bold blue] {message}")

def m_post(a_dictionary): #we use this to show a post to the user

    console = Console()

    table = Table(title="Post Details")

    table.add_column("Field", style="bold cyan", justify="left")
    table.add_column("Value", style="bold yellow", justify="left")

    table.add_row("👤 Author", a_dictionary["author"])
    table.add_row("📅 Date", f"{a_dictionary['year']}/{a_dictionary['month']:02}/{a_dictionary['day']:02}")
    table.add_row("📝 Caption", a_dictionary["caption"])
    table.add_row("👍 Likes", str(a_dictionary["like"]))
    table.add_row("💬 Comments Count", str(a_dictionary["comment"]))
    table.add_row("📌 Saves", str(a_dictionary["save"]))
    table.add_row("🔗 Shares", str(a_dictionary["share"]))

    comments_table = Table(title="💬 Comments")
    comments_table.add_column("👥 User", style="cyan", justify="left")
    comments_table.add_column("🗨️ Comment", style="yellow", justify="left")

    for user, comment in a_dictionary["comments"]:
        comments_table.add_row(user, comment)

    group = Group(table, comments_table)

    panel = Panel(
        group,
        title="📸 Instagram Post",
        title_align="center",
        border_style="bright_magenta",
    )

    console.print(panel)
    



