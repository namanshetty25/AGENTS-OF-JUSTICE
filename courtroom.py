from agents import (
    judge_opening,
    prosecution_opening,
    defendant_statement,
    defense_opening,
    plaintiff_statement,
    defense_interrogation,
    prosecution_interrogation,
    defense_argument,
    prosecution_argument,
    defense_closing,
    prosecution_closing,
    judge_verdict
)

def print_divider():
    print("\n" + "="*50 + "\n")

def print_section_header(title):
    print_divider()
    print(f"===== {title} =====")
    print()

def run_trial(case):
    # Print case details
    print_section_header("CASE DETAILS")
    print(f"Case Number: {case['Serial No']}")
    print(f"Case: {case['Case Details']}")
    
    # Judge's Opening Address
    print_section_header("JUDGE'S OPENING ADDRESS")
    j_open = judge_opening(case)
    print(j_open)

    # Opening Statements
    print_section_header("DEFENSE OPENING STATEMENT")
    d_open = defense_opening(case)
    print(d_open)
    
    print_section_header("PROSECUTION OPENING STATEMENT")
    p_open = prosecution_opening(case)
    print(p_open)

    # Witness Statements
    print_section_header("DEFENDANT STATEMENT")
    d_statement = defendant_statement(case)
    print(d_statement)
    
    print_section_header("PLAINTIFF STATEMENT")
    p_statement = plaintiff_statement(case)
    print(p_statement)
    
    # Interrogations
    print_section_header("DEFENSE INTERROGATION OF PLAINTIFF")
    d_interrogate = defense_interrogation(case, p_statement)
    print(d_interrogate)
    
    print_section_header("PROSECUTION INTERROGATION OF DEFENDANT")
    p_interrogate = prosecution_interrogation(case, d_statement)
    print(p_interrogate)
    
    # Main Arguments
    print_section_header("DEFENSE ARGUMENTS")
    d_arg = defense_argument(case, d_interrogate, p_interrogate)
    print(d_arg)
    
    print_section_header("PROSECUTION ARGUMENTS")
    p_arg = prosecution_argument(case, d_interrogate, p_interrogate)
    print(p_arg)

# Closing Statements
    print_section_header("DEFENSE CLOSING STATEMENT")
    d_close = defense_closing(case, d_arg, p_arg)
    print(d_close)
    
    print_section_header("PROSECUTION CLOSING STATEMENT")
    p_close = prosecution_closing(case, d_arg, p_arg)
    print(p_close)

    # Judge's Verdict
    print_section_header("JUDGE'S VERDICT")
    # Compile all defense and prosecution content for the judge to consider
    defense_compilation = f"{d_open}\n\n{d_statement}\n\n{d_interrogate}\n\n{d_arg}\n\n{d_close}"
    prosecution_compilation = f"{p_open}\n\n{p_statement}\n\n{p_interrogate}\n\n{p_arg}\n\n{p_close}"
    
    verdict = judge_verdict(case, defense_compilation, prosecution_compilation)
    print(verdict)
    
    print_divider()
    print("===== TRIAL CONCLUDED =====")
    print_divider()