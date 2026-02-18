import PyPDF2
import os

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text += page.extract_text() + "\n"
            
            return text
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return None

def extract_all_solutions():
    """Extract all solution PDFs"""
    sol_folder = "soluciones"
    output_folder = "preguntas_extraidas"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_files = [f for f in os.listdir(sol_folder) if f.endswith('.pdf')]
    
    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(sol_folder, pdf_file)
        print(f"\nExtracting: {pdf_file}")
        
        text = extract_pdf_text(pdf_path)
        if text:
            # Save raw text
            txt_filename = pdf_file.replace('.pdf', '.txt')
            with open(os.path.join(output_folder, txt_filename), 'w', encoding='utf-8') as f:
                f.write(text)
            
            print(f"  ✓ Extracted {len(text)} characters")
    
    print(f"\n✓ All solution PDFs extracted to {output_folder}/")

if __name__ == "__main__":
    extract_all_solutions()
