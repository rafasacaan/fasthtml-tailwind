import os
import sys
import argparse
from fasthtml.components import html2ft

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Process an HTML file and output a Python file.')
    parser.add_argument('filename', help='The name of the HTML file (without extension) located in the src folder.')
    parser.add_argument('--output-dir', default='.', help='Optional output directory for the .py file (default is root).')

    # Parse the arguments
    args = parser.parse_args()
    filename = args.filename
    output_dir = args.output_dir
    html_file = os.path.join('src', f"{filename}.html")

    # Check if the HTML file exists
    if not os.path.exists(html_file):
        print(f"Error: {html_file} does not exist.")
        sys.exit(1)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the HTML file content
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Process the content through html2ft
    processed_content = html2ft(html_content)

    # Write the result to a .py file in the specified output directory
    py_file = os.path.join(output_dir, f"{filename}.py")
    with open(py_file, 'w') as f:
        f.write("from fasthtml.components import *\n\ncontent = ")
        f.write(processed_content)

    print(f"Processed content saved to {py_file}")

if __name__ == "__main__":
    main()