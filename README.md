# AGENTS-OF-JUSTICE
Courtroom Simulation README
This Python script simulates a courtroom trial based on a given case from a CSV file (transformed_data.csv). It leverages the Google Gemini API to generate realistic legal dialogue and proceedings, tailored to the Indian judicial system. The simulation includes various stages of a trial, from opening statements to the final verdict, with detailed legal arguments, interrogations, and judicial reasoning.
Features

Simulates a complete trial with roles for the judge, defense, prosecution, plaintiff, and defendant.
Generates formal legal dialogue using Indian judicial terminology and protocols.
Incorporates relevant Indian statutes (e.g., IPC, CrPC, Evidence Act) and landmark case law.
Supports structured trial stages: opening statements, witness statements, interrogations, arguments, closing statements, and verdict.
Reads case details from a CSV file and processes a specific case based on its serial number.
Uses the Google Gemini API (gemini-1.5-flash) for natural language generation.

Prerequisites

Python 3.x installed.
Google Gemini API Key:
Obtain an API key from Google for the Gemini model.
Replace "GEMINI API ACCESS KEY" in the script with your actual API key.


Required Python Libraries:
Install the Google Generative AI library:pip install google-generativeai




CSV File:
Ensure a file named transformed_data.csv exists in the same directory as the script.
The CSV must contain at least two columns: Serial No and Case Details.



File Structure

transformed_data.csv: Input CSV file containing case details.
Expected columns:
Serial No: Unique identifier for each case (e.g., "1", "2").
Case Details: Description of the case (e.g., "Criminal case involving theft under Section 378 IPC").




courtroom_simulation.py: Main script containing the trial simulation logic.

Usage

Prepare the CSV File:

Create or modify transformed_data.csv with case data. Example format:Serial No,Case Details
1,Criminal case involving theft under Section 378 IPC by Mr. John Doe against the State
2,Civil dispute over property ownership between Ms. Jane Smith and Mr. Robert Brown




Set Up the API Key:

Replace "GEMINI API ACCESS KEY" in the script with your Google Gemini API key:genai.configure(api_key="YOUR_ACTUAL_API_KEY")




Run the Script:

Execute the script and specify a case by its serial number. For example:from courtroom_simulation import run_trial, load_case

# Load case with Serial No 1
case = load_case(1)
if case:
    run_trial(case)
else:
    print("Case not found.")


Alternatively, run the script directly and modify the load_case call to select a different serial number.


Output:

The script will print a detailed trial simulation, including:
Case details
Judge's opening address
Defense and prosecution opening statements
Defendant and plaintiff statements
Defense and prosecution interrogations
Main arguments and closing statements
Judge's final verdict


Each section is clearly labeled and separated by dividers for readability.



Script Components
The script is modular, with functions for each trial stage. Key components include:

Utility Functions:

load_case(serial_no): Loads a case from the CSV file based on the serial number.
print_divider(): Prints a visual separator for output clarity.
print_section_header(title): Prints a formatted section header.


API Interaction:

call_gemini(prompt, retries=3): Sends prompts to the Gemini API with retry logic for robust error handling.


Trial Stages:

judge_opening(case): Generates the judge's formal opening address.
defense_opening(case): Defense counsel's opening statement.
prosecution_opening(case): Prosecution counsel's opening statement.
defendant_statement(case): Defendant's formal statement.
plaintiff_statement(case): Plaintiff's formal statement.
defense_interrogation(case, plaintiff_statement): Defense's cross-examination of the plaintiff.
prosecution_interrogation(case, defendant_statement): Prosecution's cross-examination of the defendant.
defense_argument(case, defense_interrogation_full, prosecution_interrogation_full): Defense's main legal arguments.
prosecution_argument(case, defense_interrogation_full, prosecution_interrogation_full): Prosecution's main legal arguments.
defense_closing(case, defense_argument, prosecution_argument): Defense's closing statement.
prosecution_closing(case, defense_argument, prosecution_argument): Prosecution's closing statement.
judge_verdict(case, defense, prosecution): Judge's final verdict based on all proceedings.


Main Function:

run_trial(case): Orchestrates the entire trial simulation, calling each stage in sequence.



Customization

Change Case: Modify the serial_no in load_case(serial_no) to simulate a different case.
Adjust Prompts: Edit the prompts in each function to change the tone, detail level, or specific legal references.
Extend Functionality: Add new trial stages (e.g., witness testimonies, expert reports) by creating new functions and integrating them into run_trial.

Notes

API Dependency: The script relies on the Google Gemini API, which may have rate limits or costs depending on your plan. Ensure your API key is active and has sufficient quota.
Error Handling: The call_gemini function includes retry logic for API errors. Adjust retries or add custom error handling as needed.
CSV Format: Ensure the CSV file is properly formatted and encoded in UTF-8 to avoid parsing errors.
Legal Accuracy: The generated dialogue is simulated and may not be legally binding or perfectly accurate. Use this tool for educational or illustrative purposes only.

