import PyPDF2
import sys

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            print(f"Total pages: {len(pdf_reader.pages)}\n")
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text += f"\n--- PAGE {page_num} ---\n"
                text += page.extract_text()
            
            return text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "Base.pdf"
    text = extract_pdf_text(pdf_path)
    
    if text:
        # Save to text file
        with open("Base_content.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\nText extracted successfully to Base_content.txt")
        
        # Print first 2000 characters
        print("\n--- PREVIEW ---")
        print(text[:2000])
