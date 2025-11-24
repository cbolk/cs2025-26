def check_file(fname):
    try:
        # Try to open the file in read mode
        with open(fname, "r"):
            content = f.read(1)  # Read just one character
            return len(content) > 0
    except:
        # If any error occurs (file not found, no permission, etc.)
        return False
