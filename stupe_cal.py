from cx_Freeze import setup, Executable
base = None
setup(name="Mohd Askery",
      version="0.1",
      description="the python calculator",
      executables=[Executable("main.py")]
      )
