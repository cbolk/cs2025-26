SYMBOL = '*'

def process_unary_file(filename):
    """
    Reads a file containing unary-encoded integers (as '*' repeated),
    separated by spaces and newlines. Returns a list of integers and their mean,
    and prints the mean rounded down in unary code.
    """
    values = []

    try:
        # Open the file and read all content in one long string ("\n" included)
        with open(filename, 'r') as f:
            content = f.read()

        # Split by whitespace (spaces, tabs, newlines)
        tokens = content.split()

        # Convert each token to its length (unary decoding)
        totvalues = 0
        for token in tokens:
            value = len(token)
            totvalues += value
            values.append(value)

        numvalues = len(values)
        # Compute mean
        if numvalues > 0:
            mean_value = totvalues / numvalues
        else
            mean_value = 0

        # Floor the mean and display in unary
        mean_floor = int(mean_value)
        print(SYMBOL * mean_floor)

        return values, mean_value

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")

    except Exception as e:
        print("Error:", e)

