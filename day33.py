import fitz

def read_pdf(file_path):
    document = fitz.open(file_path)

    text = ""

    for page in range(len(document)):
        p_data = document[page]
        text += p_data.get_text()


    document.close()
    return text

def main():
    file_path = "resume.pdf"

    try:
        content = read_pdf(file_path)
        print("\n\n")

    except Exception as e:
        print(f"failed to read pdf {e}")

if __name__ == "__main__":
    main()