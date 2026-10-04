# Literally just a module file for basic functions.

def line_break(comment):
    def brk(repeat):
        while repeat > 0:
            repeat-=1
            print("")
    brk(2) # Starting with "repeat" line breaks, or blank prints.
    print(f"# {comment} #") # Organize logger output with a comment.
    brk(0) # Ending with "repeat" line breaks, or blank prints.
    
    '''
    import random
from rule34Py import rule34Py
client = rule34Py()
client.api_key = "93be47b937a43f8b8590cbc14dcbfd94a0b3ad867d5cfce119b6cf3c60927e6a4ac92699c176a42cc3899b61036c72e1c4e22715359a767559cb0031ddd7dcae"
client.user_id = "3803821"
    @commands.hybrid_command(
        name="sam34",
        description="This is a testing command that does nothing.",
    )   
    @discord.app_commands.allowed_installs(guilds=True, users=True)
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def sam34get(self, context: Context, *, message: str) -> None:
        r34tags = message.split(", ")
        p_id=random.randint(2,99)
        r34limit = 1
        loopwait = 0
        result = client.search(r34tags, page_id = p_id, limit = r34limit)
        r34_id = ['']
        for result in result:
            r34_id.append(f'https://rule34.xxx/index.php?page=post&s=view&id={result.id}')
            loopwait+=1
            if loopwait == r34limit: # making it break
                await context.send(f"{('\n'.join(r34_id))}") # Limit doesn't exist to anything else.
        '''