import cx_Freeze

executables = [cx_Freeze.Executable("GreenLife.py", base = "Win32GUI", icon = "arbol.ico")]
cx_Freeze.setup(
    name="Green Life",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["assets","juego.py","tutorial.py","worlds.py","world1.py","world2.py"]}},
    executables = executables

    )
