import time
import google.generativeai as genai

genai.configure(api_key="GEMINI API ACCESS KEY")
model = genai.GenerativeModel('gemini-1.5-flash')  

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

def judge_opening(case):
    return call_gemini(f"""
    Act as a distinguished High Court Judge presiding over case number {case['Serial No']}: {case['Case Details']}. 
    
    Provide a formal, authoritative opening address that:
    
    1. Begins with "THE COURT:" followed by a formal salutation such as "This Hon'ble Court is now in session."
    
    2. States the full case citation with proper legal nomenclature (e.g., "Criminal Appeal No. {case['Serial No']} of [Petitioner/Appellant] versus [Respondent]" or "Writ Petition (Civil) No. {case['Serial No']}")
    
    3. Acknowledges the presence of legal representatives with appropriate honorifics 
    
    4. References relevant sections of applicable laws mentioned in the case details (e.g., "This matter pertains to alleged violations under Section X of the Y Act")
    
    5. Briefly summarizes the core legal question or relief sought (e.g., "seeking relief against the impugned order dated...")
    
    6. Uses authentic Indian judicial language including appropriate terminology such as "wherein," "hereinafter," "aforementioned," "prayed for," etc.
    
    7. Concludes with a formal initiation such as "The Court will now hear submissions from the learned counsel for the petitioner/appellant" or "Let the proceedings commence with the submissions of the learned counsel"
    
    Ensure the tone conveys gravitas, judicial temperament, and absolute impartiality. Incorporate Indian legal formalities and procedural elements specific to the type of proceeding (trial court, appellate jurisdiction, constitutional bench, etc.).
    
    Draw necessary inferences from the case details to create a contextually appropriate opening that would be delivered in an Indian court of appropriate jurisdiction.
    """)

def defendant_statement(case):
    return call_gemini(f"""
    You are the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Provide a formal statement to the court that:
    
    1. Begins with formal address: "DEFENDANT/PETITIONER: May it please Your Lordship/Honor,"
    
    2. Introduces yourself appropriately with name and status (e.g., "I, [Name], the petitioner/accused in the aforementioned matter...")
    
    3. Explains your position with proper legal terminology used in Indian courts (e.g., "I most respectfully submit that the allegations levied against me are devoid of merit and unsustainable in the eyes of law")
    
    4. Clearly articulates your requested relief using precise legal language (e.g., "I seek the quashing of the impugned FIR registered against me," "I pray that this Hon'ble Court may be pleased to set aside the judgment of the lower court")
    
    5. References specific sections of applicable law that support your position (e.g., "The charges under Section 420 IPC are wholly unsubstantiated as the essential ingredients of the offense are absent")
    
    6. Concludes with a formal submission (e.g., "I most humbly pray that this Hon'ble Court may be pleased to grant the relief as prayed for in the interests of justice")
    
    Maintain a deferential, respectful tone throughout while being assertive about your legal position. Include appropriate honorifics and courtroom formalities specific to Indian judicial proceedings. Adapt your language for the specific context (criminal trial, civil dispute, writ petition, appeal, etc.) as indicated by the case details.
    """)

def plaintiff_statement(case):
    return call_gemini(f"""
    You are the plaintiff/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Provide a formal statement to the court that:
    
    1. Begins with formal address: "COMPLAINANT/PLAINTIFF: With utmost respect to Your Lordship/Honor,"
    
    2. Introduces yourself appropriately with name and status (e.g., "I, [Name], the complainant/respondent in the aforementioned matter...")
    
    3. Details your allegations using specific legal terminology prevalent in Indian courts (e.g., "I have been gravely aggrieved by the acts and omissions of the accused/defendant")
    
    4. Articulates factual background with temporal specificity (e.g., "On [date], the accused/defendant willfully and deliberately...")
    
    5. References applicable legal provisions supporting your case (e.g., "The accused has committed offenses punishable under Sections 406 and 420 of the Indian Penal Code")
    
    6. Clarifies your position on case proceedings (e.g., "I vehemently oppose the accused's petition for discharge" or "I seek stringent punishment as prescribed by law")
    
    7. Concludes with a formal submission (e.g., "I humbly pray that this Hon'ble Court may be pleased to uphold justice by dismissing the relief sought by the petitioner")
    
    Maintain a respectful yet assertive tone with appropriate deference to the court. Include proper legal terminology, honorifics, and courtroom formalities specific to Indian judicial proceedings. Adapt your language to the specific context (criminal complaint, civil dispute, opposition to writ petition, etc.) as indicated by the case details.
    """)

def defense_opening(case):
    return call_gemini(f"""
    You are a learned Senior Advocate/Defense Counsel representing the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your opening statement that:
    
    1. Begins with formal address: "DEFENSE COUNSEL: May it please Your Lordship," followed by introducing yourself (e.g., "I, [Name], learned counsel appearing on behalf of the accused/petitioner in the matter at hand")
    
    2. Introduces your client formally (e.g., "My client, the petitioner herein, approaches this Hon'ble Court seeking relief against the impugned order/FIR/judgment dated...")
    
    3. Outlines the legal grounds for your client's position with reference to specific provisions (e.g., "The petition is founded on the grounds enumerated under Section 482 CrPC read with Article 226 of the Constitution of India")
    
    4. Cites relevant Supreme Court and High Court precedents by name and citation (e.g., "I draw this Hon'ble Court's attention to the ratio laid down in Arnesh Kumar v. State of Bihar (2014) 8 SCC 273")
    
    5. Clarifies the legal questions at issue (e.g., "The primary question for Your Lordship's consideration is whether the ingredients of Section 420 IPC are made out from the bare allegations")
    
    6. Previews your legal strategy (e.g., "I shall demonstrate that the prosecution case suffers from fatal infirmities and cannot sustain judicial scrutiny")
    
    7. Concludes with formal expression (e.g., "With these preliminary submissions, I shall now elaborate upon the factual matrix and legal propositions in support of my client")
    
    Use eloquent, formal legal language with appropriate honorifics and courtroom formalities. Incorporate relevant sections of Indian statutes (IPC, CrPC, Evidence Act, Constitution) and landmark judgments with proper citations. Frame arguments specifically for the Indian legal context while adapting to the appropriate jurisdiction level and procedure (trial court, appellate court, writ jurisdiction) indicated by the case details.
    """)

def prosecution_opening(case):
    return call_gemini(f"""
    You are a learned Public Prosecutor/State Counsel/Plaintiff's Advocate representing the State/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your opening statement that:
    
    1. Begins with formal address: "PROSECUTION/PLAINTIFF COUNSEL: May it please Your Lordship," followed by introducing yourself (e.g., "I, [Name], learned counsel appearing on behalf of the State/complainant/respondent in the matter at hand")
    
    2. Introduces the case formally (e.g., "The present matter pertains to serious allegations of offenses committed by the accused/violations of the complainant's legal rights")
    
    3. Outlines the factual background with specificity (e.g., "I would respectfully draw Your Lordship's attention to the events that transpired on [date] wherein the accused, with mala fide intent...")
    
    4. References applicable legal provisions with precision (e.g., "The accused stands charged under Section 302 read with Section 120B of the Indian Penal Code")
    
    5. Cites relevant Supreme Court and High Court precedents by name and citation (e.g., "I would rely upon the settled position of law as enunciated in State of Maharashtra v. Kamal Dupey (2008) 16 SCC 491")
    
    6. Previews your legal strategy and burden of proof (e.g., "The prosecution shall establish beyond reasonable doubt each ingredient of the offense through documentary and testimonial evidence")
    
    7. Concludes with formal expression (e.g., "With these preliminary submissions, I shall now elaborate upon the factual matrix and legal propositions that establish the culpability of the accused")
    
    Use precise, formal legal language with appropriate honorifics and courtroom formalities. Incorporate relevant sections of Indian statutes (IPC, CrPC, Evidence Act, specific laws) and landmark judgments with proper citations. Frame arguments specifically for the Indian legal context while adapting to the appropriate jurisdiction level and procedure (trial court, appellate court, writ jurisdiction) indicated by the case details.
    """)

def defense_interrogation_questions(case, plaintiff_statement):
    return call_gemini(f"""
    You are a learned Senior Advocate/Defense Counsel representing the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Based on the case details and the plaintiff's statement: {plaintiff_statement}, conduct a formal examination-in-chief or cross-examination that:
    
    1. Begins with formal address to the court and witness (e.g., "DEFENSE COUNSEL: With Your Lordship's permission, I shall now proceed to examine/cross-examine the witness.")
    
    2. Clearly identifies the witness being examined (e.g., "Questions to [Name/Designation], [Complainant/Investigating Officer/Expert Witness]")
    
    3. Formulates 5-8 strategically crafted questions using proper Indian legal interrogation techniques:
       - For prosecution witnesses: Questions that challenge credibility, expose contradictions, or establish favorable facts
       - For defense witnesses: Questions that bolster your client's position and pre-emptively address potential challenges
    
    4. Incorporates proper examination protocol for Indian courts:
       - Prefaces questions with "I put it to you that..." when suggesting contradictions
       - Uses "Is it not a fact that..." when establishing favorable points
       - Employs "Would you agree with me that..." when seeking beneficial admissions
    
    5. References specific documents, dates, and legal provisions relevant to the case (e.g., "Drawing your attention to the FIR registered on [date], is it not correct that...")
    
    6. Concludes with a formal notation (e.g., "No further questions, My Lord/Your Honor")
    
    Questions should be precisely tailored to the specific legal context (criminal trial, civil dispute, etc.), following proper Indian Evidence Act protocols. Focus on establishing facts that directly support your client's requested relief or undermine the opposing party's case. Maintain formal courtroom decorum throughout.
    
    Format your questions clearly, numbering each one, and ensuring they are direct and challenging but maintaining courtroom decorum.
    """)

def plaintiff_responses_to_defense(case, plaintiff_statement, defense_questions):
    return call_gemini(f"""
    You are the plaintiff/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}.
    
    You previously provided this statement to the court: {plaintiff_statement}
    
    Now, you must respond to each question from the defense counsel during cross-examination. The defense counsel has asked:
    
    {defense_questions}
    
    Provide your responses to each question:
    
    1. Begin each response with "PLAINTIFF/COMPLAINANT/RESPONDENT:"
    
    2. Maintain consistency with your initial statement while being realistic about potential vulnerabilities in your testimony
    
    3. Show appropriate emotion when questioned about sensitive matters (hesitation, firmness, indignation, etc.)
    
    4. Occasionally display defensiveness when challenged on key points, but avoid appearing rehearsed
    
    5. Sometimes ask for clarification on complex questions
    
    6. Use phrases like "To the best of my recollection...", "I am certain that...", or "I cannot recall precisely..." when appropriate
    
    7. Respond with appropriate legal terminology but avoid sounding like a legal expert if you're not portrayed as one
    
    8. For questions suggesting contradictions:
       - Sometimes concede minor points while maintaining the core of your testimony
       - Occasionally respectfully disagree with the premise of the question 
       - Provide context or clarification if a statement appears contradictory when isolated
    
    Format your responses to correspond with each numbered question, maintaining the character of a real witness under cross-examination in an Indian courtroom.
    """)

def prosecution_interrogation_questions(case, defendant_statement):
    return call_gemini(f"""
    You are a learned Public Prosecutor/State Counsel/Plaintiff's Advocate representing the State/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Based on the case details and the defendant's statement: {defendant_statement}, conduct a formal examination-in-chief or cross-examination that:
    
    1. Begins with formal address to the court and witness (e.g., "PROSECUTION/PLAINTIFF COUNSEL: With Your Lordship's kind permission, I shall now proceed to examine/cross-examine the witness.")
    
    2. Clearly identifies the witness being examined (e.g., "Questions to [Name/Designation], [Accused/Defense Witness/Expert Witness]")
    
    3. Formulates 5-8 strategically crafted questions using proper Indian legal interrogation techniques:
       - For prosecution witnesses: Questions that establish elements of the offense/claim and strengthen your case
       - For defense witnesses: Questions that expose inconsistencies, challenge credibility, or establish unfavorable facts
    
    4. Incorporates proper examination protocol for Indian courts:
       - Prefaces questions with "I put it to you that..." when suggesting contradictions
       - Uses "Is it not a fact that..." when establishing incriminating points
       - Employs "Would you agree with me that..." when seeking damaging admissions
    
    5. References specific documents, dates, and legal provisions relevant to the case (e.g., "Drawing your attention to the statement recorded under Section 164 CrPC, is it not correct that...")
    
    6. Concludes with a formal notation (e.g., "No further questions, My Lord/Your Honor")
    
    Questions should be precisely tailored to the specific legal context (criminal trial, civil dispute, etc.), following proper Indian Evidence Act protocols. Focus on establishing facts that directly prove the elements of your case or undermine the opposing party's defenses. Maintain formal courtroom decorum throughout.
    
    Format your questions clearly, numbering each one, and ensuring they are direct and challenging but maintaining courtroom decorum.
    """)

def defendant_responses_to_prosecution(case, defendant_statement, prosecution_questions):
    return call_gemini(f"""
    You are the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}.
    
    You previously provided this statement to the court: {defendant_statement}
    
    Now, you must respond to each question from the prosecution counsel during cross-examination. The prosecution counsel has asked:
    
    {prosecution_questions}
    
    Provide your responses to each question:
    
    1. Begin each response with "DEFENDANT/ACCUSED/PETITIONER:"
    
    2. Maintain consistency with your initial statement while being realistic about potential vulnerabilities in your testimony
    
    3. Show appropriate emotion when questioned about sensitive matters (hesitation, firmness, concern, etc.)
    
    4. Occasionally display defensiveness when challenged on key points, but avoid appearing evasive
    
    5. Sometimes ask for clarification on complex questions
    
    6. Use phrases like "To the best of my knowledge...", "I maintain that...", or "I do not recall the exact..." when appropriate
    
    7. Respond with appropriate legal terminology but avoid sounding overly rehearsed
    
    8. For questions suggesting contradictions:
       - Sometimes concede minor points while maintaining your core defense
       - Occasionally respectfully disagree with the premise of the question 
       - Provide context or clarification if a statement appears contradictory when isolated
    
    Format your responses to correspond with each numbered question, maintaining the character of a real defendant under cross-examination in an Indian courtroom.
    """)

def defense_argument(case, defense_interrogation_full, prosecution_interrogation_full):
    return call_gemini(f"""
    You are a learned Senior Advocate/Defense Counsel representing the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your main arguments that:
    
    1. Begin with formal address: "DEFENSE COUNSEL: May it please Your Lordship," followed by a concise introduction of your submission
    
    2. Structure arguments under clear, numbered legal grounds (e.g., "GROUND I: The impugned FIR fails to disclose essential ingredients of the alleged offense")
    
    3. Incorporate testimony from your cross-examination: {defense_interrogation_full} using specific quotes and insights
    
    4. Counter the prosecution's examination: {prosecution_interrogation_full} by highlighting weaknesses or inconsistencies
    
    5. Cite relevant landmark judgments with full citations and ratio decidendi:
       - Supreme Court precedents (e.g., "In Lalita Kumari v. Government of Uttar Pradesh (2014) 2 SCC 1, the Hon'ble Supreme Court held that...")
       - High Court decisions relevant to the jurisdiction
       - Constitutional bench decisions when applicable
    
    6. Apply specific provisions of Indian law with precise statutory interpretation:
       - Criminal matters: IPC sections, CrPC provisions (especially Sections 227, 239, 482), Evidence Act
       - Civil matters: CPC provisions, specific acts, limitation periods
       - Constitutional matters: Fundamental rights, judicial review principles
    
    7. Analyze the burden of proof and its application to the present facts (e.g., "The prosecution has failed to establish beyond reasonable doubt that...")
    
    8. Conclude with specific prayer (e.g., "In light of the above submissions, it is most respectfully prayed that this Hon'ble Court may be pleased to quash the impugned FIR/allow the appeal/grant the relief as sought in the petition.")
    
    Maintain sophisticated legal reasoning with proper jurisprudential concepts relevant to Indian law (e.g., mens rea, actus reus, res ipsa loquitur, falsus in uno falsus in omnibus). Use formal, persuasive language throughout with appropriate legal maxims and principles. Adapt arguments to the specific procedural stage and court level (trial, revision, appeal, etc.) as indicated by the case details.
    """)

def prosecution_argument(case, defense_interrogation_full, prosecution_interrogation_full):
    return call_gemini(f"""
    You are a learned Public Prosecutor/State Counsel/Plaintiff's Advocate representing the State/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your main arguments that:
    
    1. Begin with formal address: "PROSECUTION/PLAINTIFF COUNSEL: May it please Your Lordship," followed by a concise introduction of your submission
    
    2. Structure arguments under clear, numbered legal grounds (e.g., "GROUND I: The evidence on record establishes prima facie case against the accused")
    
    3. Incorporate testimony from your examination: {prosecution_interrogation_full} using specific quotes and insights
    
    4. Counter the defense's cross-examination: {defense_interrogation_full} by reinforcing strengths and explaining apparent inconsistencies
    
    5. Cite relevant landmark judgments with full citations and ratio decidendi:
       - Supreme Court precedents (e.g., "In State of Rajasthan v. Balchand (1977) 4 SCC 308, the Hon'ble Supreme Court held that...")
       - High Court decisions relevant to the jurisdiction
       - Constitutional bench decisions when applicable
    
    6. Apply specific provisions of Indian law with precise statutory interpretation:
       - Criminal matters: IPC sections, CrPC provisions, Evidence Act
       - Civil matters: CPC provisions, specific acts, limitation periods
       - Constitutional matters: State powers, restrictions on fundamental rights
    
    7. Analyze the threshold requirements for the specific proceeding and how they are met (e.g., "The material on record satisfies the test laid down for framing of charges under Section 228 CrPC...")
    
    8. Conclude with specific opposition to relief (e.g., "In light of the above submissions, it is most respectfully prayed that this Hon'ble Court may be pleased to dismiss the petition/uphold the charges/confirm the conviction.")
    
    Maintain sophisticated legal reasoning with proper jurisprudential concepts relevant to Indian law. Use formal, persuasive language throughout with appropriate legal maxims and principles. Adapt arguments to the specific procedural stage and court level (trial, revision, appeal, etc.) as indicated by the case details.
    """)

def defense_closing(case, defense_argument, prosecution_argument):
    return call_gemini(f"""
    You are a learned Senior Advocate/Defense Counsel representing the defendant/accused/petitioner in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your closing statement that:
    
    1. Begins with formal address: "DEFENSE COUNSEL: In conclusion, may it please Your Lordship,"
    
    2. Summarizes your strongest arguments from your main submission: {defense_argument} with concise recapitulation (without verbatim repetition)
    
    3. Provides point-by-point rebuttal to the prosecution's specific contentions: {prosecution_argument}, using the structure:
       - "The learned counsel for the [prosecution/respondent] has contended that... However, this submission deserves to be rejected for the following reasons..."
    
    4. Reinforces key legal principles with additional authorities or constitutional values:
       - "The settled position of law as enunciated by the Hon'ble Supreme Court in [case citation] squarely applies to the facts of the present case..."
       - "The cardinal principle of criminal jurisprudence that the accused is presumed innocent until proven guilty beyond reasonable doubt must guide this Hon'ble Court's determination..."
    
    5. Addresses any remaining ambiguities or weaknesses in your case preemptively:
       - "Although the prosecution has attempted to establish [point], this allegation falls flat when scrutinized under the established legal standards because..."
    
    6. Appeals to broader principles of justice, equity, and good conscience where applicable:
       - "The continued prosecution/denial of relief would lead to manifest injustice and abuse of the process of law..."
    
    7. Concludes with formal prayer emphasizing the specific relief sought:
       - "In light of the totality of circumstances and legal position highlighted above, it is most humbly prayed that this Hon'ble Court may be pleased to allow the [petition/appeal/application] and grant relief as sought for."
    
    Use eloquent legal language with appropriate honorifics and concluding formalities. Demonstrate deep understanding of Indian jurisprudence while adapting to the specific procedural context and court hierarchy as indicated by the case details. Maintain respectful but assertive tone throughout.
    """)

def prosecution_closing(case, defense_argument, prosecution_argument):
    return call_gemini(f"""
    You are a learned Public Prosecutor/State Counsel/Plaintiff's Advocate representing the State/complainant/respondent in Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Present your closing statement that:
    
    1. Begins with formal address: "PROSECUTION/PLAINTIFF COUNSEL: In conclusion, may it please Your Lordship,"
    
    2. Summarizes your strongest arguments from your main submission: {prosecution_argument} with concise recapitulation (without verbatim repetition)
    
    3. Provides point-by-point rebuttal to the defense's specific contentions: {defense_argument}, using the structure:
       - "The learned counsel for the [defense/petitioner] has contended that... However, this submission is untenable for the following reasons..."
    
    4. Reinforces key legal principles with additional authorities or policy considerations:
       - "The consistent view taken by the Hon'ble Courts in [case citations] establishes beyond doubt that..."
       - "The legislative intent behind Section [x] of [statute] clearly indicates that the present case falls squarely within its ambit..."
    
    5. Addresses any apparent weaknesses in your case with persuasive explanations:
       - "While the defense has attempted to create doubt regarding [issue], when viewed in proper context and in light of the preponderance of evidence..."
    
    6. Appeals to broader principles of public interest, deterrence, or victim justice where applicable:
       - "Granting relief to the accused/petitioner would not only be against the established legal position but would also undermine public faith in the justice system..."
    
    7. Concludes with formal prayer emphasizing opposition to the relief sought:
       - "In light of the submissions made above and the evidence on record, it is most respectfully prayed that this Hon'ble Court may be pleased to dismiss the [petition/appeal/application] and uphold justice."
    
    Use eloquent legal language with appropriate honorifics and concluding formalities. Demonstrate deep understanding of Indian jurisprudence while adapting to the specific procedural context and court hierarchy as indicated by the case details. Maintain respectful but firm tone throughout.
    """)

def judge_verdict(case, defense, prosecution):
    return call_gemini(f"""
    You are a distinguished Judge of appropriate jurisdiction presiding over Case No. {case['Serial No']}: {case['Case Details']}. 
    
    Based on the comprehensive proceedings, deliver a formal judgment that:
    
    1. Begins with proper case citation and court identification:
       - "IN THE [APPROPRIATE COURT - Supreme Court/High Court/Sessions Court] AT [LOCATION]"
       - "Case/Appeal/Petition No. {case['Serial No']} of [YEAR]"
       - "[PARTIES WITH PROPER DESIGNATION]...Petitioner(s)/Appellant(s) VERSUS [OPPOSING PARTIES]...Respondent(s)"
    
    2. Identifies yourself as the presiding judicial officer:
       - "JUDGMENT DELIVERED BY THE HON'BLE [MR./MS.] JUSTICE [NAME]:"
    
    3. Provides a comprehensive summary of case background:
       - "This [petition/appeal/application] under [relevant legal provision] comes before this Court challenging [impugned order/seeking relief]..."
    
    4. Summarizes the contentions of both parties with proper attribution:
       - "The learned counsel for the [petitioner/appellant] has contended that... {defense}"
       - "Per contra, the learned counsel for the [respondent] has argued that... {prosecution}"
    
    5. Frames specific questions of law or issues for determination:
       - "The following issues arise for consideration before this Court:"
       - "ISSUE I: Whether..."
       - "ISSUE II: Whether..."
    
    6. Conducts detailed legal analysis of each issue:
       - Cites relevant statutory provisions with full text
       - Applies controlling precedents with full citations and extended quotations
       - Evaluates evidence and arguments systematically
       - Shows independent judicial reasoning beyond the parties' submissions
    
    7. Delivers a clear, unambiguous verdict on each issue and overall:
       - "In view of the foregoing discussion, this Court is of the considered opinion that..."
       - Provides specific orders (e.g., "The FIR is hereby quashed," "The appeal is allowed," "The conviction is set aside")
    
    8. Addresses consequential matters:
       - Costs, interim orders, implementation directions
       - Time limitations, if applicable
    
    9. Concludes with formal closing:
       - "The [petition/appeal/application] is accordingly [allowed/dismissed]."
       - "Order accordingly."
       - "[DATE]"
    
    Use authoritative, formal judicial language that demonstrates deep understanding of Indian legal principles, jurisprudence, and constitutional values. Balance competing interests while strictly adhering to established legal principles. Write in a measured, thoughtful tone with proper paragraph structure and logical progression of ideas. Adapt the judgment format and reasoning to the appropriate court level and jurisdiction as indicated by the case details.
    """)

def defense_interrogation(case, plaintiff_statement):
    # First, generate the defense lawyer's questions
    questions = defense_interrogation_questions(case, plaintiff_statement)
    
    # Then, generate the plaintiff's responses to those questions
    responses = plaintiff_responses_to_defense(case, plaintiff_statement, questions)
    
    # Return the full interrogation exchange
    return f"===== DEFENSE INTERROGATION =====\n\n{questions}\n\n===== PLAINTIFF RESPONSES =====\n\n{responses}"

def prosecution_interrogation(case, defendant_statement):
    # First, generate the prosecution lawyer's questions
    questions = prosecution_interrogation_questions(case, defendant_statement)
    
    # Then, generate the defendant's responses to those questions
    responses = defendant_responses_to_prosecution(case, defendant_statement, questions)
    
    # Return the full interrogation exchange
    return f"===== PROSECUTION INTERROGATION =====\n\n{questions}\n\n===== DEFENDANT RESPONSES =====\n\n{responses}"
