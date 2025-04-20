import time
import pandas as pd
import google.generativeai as genai
from tqdm import tqdm
# Configure Gemini API
genai.configure(api_key="AIzaSyDR3YoWaQ_bTLJelv8uRBVIZrGHvTle0U4")
model = genai.GenerativeModel('gemini-1.5-flash')

# Utility function to call Gemini API with retries
def call_gemini(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if attempt == retries - 1:
                return f"Error generating response after {retries} attempts: {e}"
            time.sleep(1)
    return "Error: Unable to generate response."

# Load all cases from CSV
def load_all_cases():
    try:
        df = pd.read_csv('cases.csv')
        if 'id' not in df.columns or 'text' not in df.columns:
            raise ValueError("CSV must contain 'id' and 'text' columns")
        return df.to_dict('records')
    except FileNotFoundError:
        print("Error: 'cases.csv' file not found.")
        return []
    except Exception as e:
        print(f"Error loading cases: {e}")
        return []

# Judge's opening address
def judge_opening(case):
    prompt = f"""
    Act as a distinguished High Court Judge presiding over case number {case['id']}: {case['text']}. 
    
    Provide a formal, authoritative opening address that:
    
    1. Begins with "THE COURT:" followed by a formal salutation
    2. States the full case citation
    3. Acknowledges legal representatives
    4. References applicable laws
    5. Summarizes the core legal question
    6. Uses Indian judicial language
    7. Concludes with a formal initiation
    """
    return call_gemini(prompt)

# Defendant's statement
def defendant_statement(case):
    prompt = f"""
    You are the defendant/accused/petitioner in Case No. {case['id']}: {case['text']}. 
    
    Provide a formal statement:
    
    1. Begins with "DEFENDANT/PETITIONER: May it please Your Lordship/Honor,"
    2. Introduces yourself
    3. Explains your position
    4. Articulates requested relief
    5. References applicable law
    6. Concludes formally
    """
    return call_gemini(prompt)

# Plaintiff's statement
def plaintiff_statement(case):
    prompt = f"""
    You are the plaintiff/complainant/respondent in Case No. {case['id']}: {case['text']}. 
    
    Provide a formal statement:
    
    1. Begins with "COMPLAINANT/PLAINTIFF: With utmost respect to Your Lordship/Honor,"
    2. Introduces yourself
    3. Details allegations
    4. Provides factual background
    5. References legal provisions
    6. Clarifies position
    7. Concludes formally
    """
    return call_gemini(prompt)

# Defense opening statement
def defense_opening(case):
    prompt = f"""
    You are a Senior Advocate/Defense Counsel in Case No. {case['id']}: {case['text']}. 
    
    Present your opening statement:
    
    1. Begins with "DEFENSE COUNSEL: May it please Your Lordship,"
    2. Introduces client
    3. Outlines legal grounds
    4. Cites precedents
    5. Clarifies legal questions
    6. Previews strategy
    7. Concludes formally
    """
    return call_gemini(prompt)

# Prosecution opening statement
def prosecution_opening(case):
    prompt = f"""
    You are a Public Prosecutor/Plaintiff's Advocate in Case No. {case['id']}: {case['text']}. 
    
    Present your opening statement:
    
    1. Begins with "PROSECUTION/PLAINTIFF COUNSEL: May it please Your Lordship,"
    2. Introduces case
    3. Outlines factual background
    4. References legal provisions
    5. Cites precedents
    6. Previews strategy
    7. Concludes formally
    """
    return call_gemini(prompt)

# Defense interrogation questions
def defense_interrogation_questions(case, plaintiff_statement):
    prompt = f"""
    You are a Senior Advocate/Defense Counsel in Case No. {case['id']}: {case['text']}. 
    
    Based on plaintiff's statement: {plaintiff_statement}, conduct a cross-examination:
    
    1. Begins with formal address
    2. Identifies witness
    3. Formulates 5-8 questions
    4. Uses proper protocol
    5. References documents/laws
    6. Concludes formally
    """
    return call_gemini(prompt)

# Plaintiff responses to defense
def plaintiff_responses_to_defense(case, plaintiff_statement, defense_questions):
    prompt = f"""
    You are the plaintiff in Case No. {case['id']}: {case['text']}.
    
    Statement: {plaintiff_statement}
    
    Respond to defense questions: {defense_questions}
    
    Responses:
    1. Begin with "PLAINTIFF/COMPLAINANT/RESPONDENT:"
    2. Maintain consistency
    3. Show emotion
    4. Display defensiveness
    5. Ask for clarification
    6. Use recollection phrases
    7. Use legal terminology
    8. Handle contradictions
    """
    return call_gemini(prompt)

# Prosecution interrogation questions
def prosecution_interrogation_questions(case, defendant_statement):
    prompt = f"""
    You are a Public Prosecutor in Case No. {case['id']}: {case['text']}. 
    
    Based on defendant's statement: {defendant_statement}, conduct a cross-examination:
    
    1. Begins with formal address
    2. Identifies witness
    3. Formulates 5-8 questions
    4. Uses proper protocol
    5. References documents/laws
    6. Concludes formally
    """
    return call_gemini(prompt)

# Defendant responses to prosecution
def defendant_responses_to_prosecution(case, defendant_statement, prosecution_questions):
    prompt = f"""
    You are the defendant in Case No. {case['id']}: {case['text']}.
    
    Statement: {defendant_statement}
    
    Respond to prosecution questions: {prosecution_questions}
    
    Responses:
    1. Begin with "DEFENDANT/ACCUSED/PETITIONER:"
    2. Maintain consistency
    3. Show emotion
    4. Display defensiveness
    5. Ask for clarification
    6. Use recollection phrases
    7. Use legal terminology
    8. Handle contradictions
    """
    return call_gemini(prompt)

# Defense interrogation
def defense_interrogation(case, plaintiff_statement):
    questions = defense_interrogation_questions(case, plaintiff_statement)
    responses = plaintiff_responses_to_defense(case, plaintiff_statement, questions)
    return f"===== DEFENSE INTERROGATION =====\n\n{questions}\n\n===== PLAINTIFF RESPONSES =====\n\n{responses}"

# Prosecution interrogation
def prosecution_interrogation(case, defendant_statement):
    questions = prosecution_interrogation_questions(case, defendant_statement)
    responses = defendant_responses_to_prosecution(case, defendant_statement, questions)
    return f"===== PROSECUTION INTERROGATION =====\n\n{questions}\n\n===== DEFENDANT RESPONSES =====\n\n{responses}"

# Defense arguments
def defense_argument(case, defense_interrogation_full, prosecution_interrogation_full):
    prompt = f"""
    You are a Senior Advocate in Case No. {case['id']}: {case['text']}. 
    
    Present arguments:
    
    1. Begin with "DEFENSE COUNSEL: May it please Your Lordship,"
    2. Numbered legal grounds
    3. Use cross-examination: {defense_interrogation_full}
    4. Counter examination: {prosecution_interrogation_full}
    5. Cite judgments
    6. Apply Indian law
    7. Analyze burden of proof
    8. Conclude with prayer
    """
    return call_gemini(prompt)

# Prosecution arguments
def prosecution_argument(case, defense_interrogation_full, prosecution_interrogation_full):
    prompt = f"""
    You are a Public Prosecutor in Case No. {case['id']}: {case['text']}. 
    
    Present arguments:
    
    1. Begin with "PROSECUTION/PLAINTIFF COUNSEL: May it please Your Lordship,"
    2. Numbered legal grounds
    3. Use examination: {prosecution_interrogation_full}
    4. Counter cross-examination: {defense_interrogation_full}
    5. Cite judgments
    6. Apply Indian law
    7. Analyze requirements
    8. Conclude with opposition
    """
    return call_gemini(prompt)

# Defense closing
def defense_closing(case, defense_argument, prosecution_argument):
    prompt = f"""
    You are a Senior Advocate in Case No. {case['id']}: {case['text']}. 
    
    Present closing:
    
    1. Begin with "DEFENSE COUNSEL: In conclusion, may it please Your Lordship,"
    2. Summarize arguments: {defense_argument}
    3. Rebut prosecution: {prosecution_argument}
    4. Reinforce principles
    5. Address ambiguities
    6. Appeal to justice
    7. Conclude with prayer
    """
    return call_gemini(prompt)

# Prosecution closing
def prosecution_closing(case, defense_argument, prosecution_argument):
    prompt = f"""
    You are a Public Prosecutor in Case No. {case['id']}: {case['text']}. 
    
    Present closing:
    
    1. Begin with "PROSECUTION/PLAINTIFF COUNSEL: In conclusion, may it please Your Lordship,"
    2. Summarize arguments: {prosecution_argument}
    3. Rebut defense: {defense_argument}
    4. Reinforce principles
    5. Address weaknesses
    6. Appeal to public interest
    7. Conclude with prayer
    """
    return call_gemini(prompt)

def judge_verdict(case, defense, prosecution):
    prompt = f"""
    You are a Judge in Case No. {case['id']}: {case['text']}.
    
    Deliver a judgment:
    
    1. Begin with case citation
    2. Identify as presiding officer
    3. Summarize background
    4. Summarize contentions: {defense} and {prosecution}
    5. Frame legal questions
    6. Analyze issues
    7. Deliver verdict - IMPORTANT: In your verdict section, clearly state one of the following phrases to indicate your decision:
       - If ruling for plaintiff: "plaintiff's claim is allowed" OR "complaint is allowed" OR "petition is allowed" OR "suit is decreed" OR "appeal is allowed" OR "granted" OR "allowed" OR "plaintiff succeeds"
       - If ruling against plaintiff: "plaintiff's claim is dismissed" OR "complaint is dismissed" OR "petition is dismissed" OR "suit is dismissed" OR "appeal is dismissed" OR "denied" OR "rejected" OR "plaintiff fails"
    8. Address consequential matters
    9. Conclude formally
    
    Your verdict must include one of the specific phrases above to clearly indicate whether you're finding in favor of or against the plaintiff.
    """
    
    return call_gemini(prompt)

def extract_verdict(verdict_text):
    """
    Returns 1 if verdict is in favor of the plaintiff/respondent/complainant,
    else returns 0 (against the plaintiff).
    """
    verdict_text = verdict_text.lower()

    # Keywords indicating the plaintiff's request was accepted
    favor_plaintiff_keywords = [
        "plaintiff's claim is allowed",
        "complaint is allowed",
        "petition is allowed",
        "suit is decreed",
        "appeal is allowed",
        "granted",
        "allowed",
        "plaintiff succeeds"
    ]

    # Keywords indicating the plaintiff's request was rejected
    against_plaintiff_keywords = [
        "plaintiff's claim is dismissed",
        "complaint is dismissed",
        "petition is dismissed",
        "suit is dismissed",
        "appeal is dismissed",
        "denied",
        "rejected",
        "plaintiff fails"
    ]

    for keyword in favor_plaintiff_keywords:
        if keyword in verdict_text:
            return 1

    for keyword in against_plaintiff_keywords:
        if keyword in verdict_text:
            return 0

    # Default to against plaintiff if uncertain
    return 0


# Run trial
def run_trial(case):
    j_open = judge_opening(case)
    d_open = defense_opening(case)
    p_open = prosecution_opening(case)
    d_statement = defendant_statement(case)
    p_statement = plaintiff_statement(case)
    d_interrogate = defense_interrogation(case, p_statement)
    p_interrogate = prosecution_interrogation(case, d_statement)
    d_arg = defense_argument(case, d_interrogate, p_interrogate)
    p_arg = prosecution_argument(case, d_interrogate, p_interrogate)
    d_close = defense_closing(case, d_arg, p_arg)
    p_close = prosecution_closing(case, d_arg, p_arg)
    defense_compilation = f"{d_open}\n\n{d_statement}\n\n{d_interrogate}\n\n{d_arg}\n\n{d_close}"
    prosecution_compilation = f"{p_open}\n\n{p_statement}\n\n{p_interrogate}\n\n{p_arg}\n\n{p_close}"
    verdict = judge_verdict(case, defense_compilation, prosecution_compilation)
    return verdict

# Save predictions
def save_predictions(predictions):
    try:
        df = pd.DataFrame(predictions, columns=['ID', 'Verdict'])
        df['Verdict'] = df['Verdict'].map({1: 'GRANTED', 0: 'DENIED'})
        df.to_csv('submission.csv', index=False)
    except Exception as e:
        print(f"Error saving submission.csv: {e}")

def main():
    print("� Fellows‍⚖ Starting Courtroom Simulation for All Cases")
    
    cases = load_all_cases()
    if not cases:
        print("No cases found. Exiting.")
        return
    
    print(f"Found {len(cases)} cases to process.")
    
    predictions = []
    
    # Initialize progress bar with total number of cases
    with tqdm(total=len(cases), desc="Processing Cases", unit="case") as pbar:
        for i, case in enumerate(cases, 1):
            print(f"\n🔍 Processing Case {i}/{len(cases)}: id {case['id']}")
            try:
                verdict_text = run_trial(case)
                verdict = extract_verdict(verdict_text)
                predictions.append((case['id'], verdict))
                print(f"Case {case['id']} verdict: {'GRANTED' if verdict == 1 else 'DENIED'}")
            except Exception as e:
                print(f"Error processing case {case['id']}: {e}")
                predictions.append((case['id'], 0))
            # Update progress bar
            pbar.update(1)
    
    save_predictions(predictions)
    print("\nAll cases processed. Simulation complete.")

if __name__ == "__main__":
    main()
