import PyPDF2
import json
import os
import re

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

def parse_questions(text):
    """Parse questions from extracted text"""
    questions = []
    
    # Pattern to find questions (adjust based on actual format)
    # Looking for numbered questions like "1.", "2.", etc.
    lines = text.split('\n')
    
    current_question = None
    current_text = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if it's a question number
        if re.match(r'^\d+[\.\)]\s+', line):
            # Save previous question
            if current_question:
                questions.append({
                    'number': current_question,
                    'text': current_text.strip()
                })
            
            # Start new question
            match = re.match(r'^(\d+)[\.\)]\s+(.*)', line)
            if match:
                current_question = match.group(1)
                current_text = match.group(2)
        else:
            # Continue current question/answer
            current_text += " " + line
    
    # Add last question
    if current_question:
        questions.append({
            'number': current_question,
            'text': current_text.strip()
        })
    
    return questions

def extract_all_tests():
    """Extract all test PDFs"""
    test_folder = "test"
    output_folder = "preguntas_extraidas"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_files = [f for f in os.listdir(test_folder) if f.endswith('.pdf')]
    
    all_questions = []
    
    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(test_folder, pdf_file)
        print(f"\nExtracting: {pdf_file}")
        
        text = extract_pdf_text(pdf_path)
        if text:
            # Save raw text
            txt_filename = pdf_file.replace('.pdf', '.txt')
            with open(os.path.join(output_folder, txt_filename), 'w', encoding='utf-8') as f:
                f.write(text)
            
            print(f"  ✓ Extracted {len(text)} characters")
    
    print(f"\n✓ All PDFs extracted to {output_folder}/")

if __name__ == "__main__":
    extract_all_tests()
