from cx_Freeze import setup, Executable
 
setup(
    name="BallAndBeam EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("Main.py")])
