try:
    from HowMonoPy._wrapper import how_mono
except FileNotFoundError:  # If a library cannot be found the OS is unsupported
    raise ImportError("OS not supported")
