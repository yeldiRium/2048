from app import App
from console.input import ConsoleInput
from console.output import ConsoleOutput

input_stream = ConsoleInput()
output = ConsoleOutput()
app = App(input_stream, output)
app.run()
