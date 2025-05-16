## Prepare the environment

from upsonic import UpsonicClient, Direct, Task
from upsonic.tools import ComputerUse

def cu_prompts(thing):
    return f"Hi, just click on the {thing} not more click then say OK"



client = UpsonicClient("http://0.0.0.0:7541")


direct = Direct(model="claude/claude-3-7-sonnet", client=client)
## 






## Application Logic

task3 = Task(cu_prompts("Web Browser icon"), tools=[ComputerUse])
task4 = Task(cu_prompts("Click to the close icon in the top right corner of the web browser"), tools=[ComputerUse])




direct.print_do(task3)
direct.print_do(task4)
print(task3.get_total_cost())