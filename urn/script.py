from database import *

cli = CliContext()

with db_session as session:
    cli.add_game(name="Legend of the Five Rings")
    cli.add_fact(text="I am a test", game=Game.get(name="Legend of the Five Rings"))
    cli.delete_fact(1)