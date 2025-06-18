from classifier import classify_comment
from utils.io import read_input_file, write_output_file
from config.settings import INPUT_FILE, OUTPUT_FILE

def main():
    comments = read_input_file(INPUT_FILE)
    results = [classify_comment(comment) for comment in comments]
    write_output_file(OUTPUT_FILE, results)

if __name__ == "__main__":
    main()
