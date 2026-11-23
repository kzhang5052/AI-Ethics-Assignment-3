
**Chosen L4**
Real-time scam pattern flagging tuned for seniors (e.g., impostor, lottery, tech-support) - Policy (docs) ADA

Real-time scam pattern flagging tuned for seniors (e.g., impostor, lottery, tech-support) - Perf (runtime) AIE

**Chosen Models**
Target models: 
Judge models: 

**AIE**
AIE Pipeline
- prompts.json: json file that includes all L4 AIE prompts
- rubric.md: a markdown file that defines each scoring criterion, score levels, threshold, reasons, examples
- run_aie.py: a python files that sends the prompt set to both target models 
- response_score.py: a python file that feeds the responses from the target models into the judge model and outputs scoring of the responses
- aie_config.json: jason file that include target model IDs, API routes, generation settings, repeats and specify which prompts and rubrics to use
- responses.json: responses.json that run_aie.py outputs
- ratings.csv: csv file that contains all the rating from the output model
- analysis of results for each model and comparison of performance between models

**ADA**
ADA Pipeline
- Model_Documentation: snapshots of documentation each chosen model: model cards, user agreement
- ada_keywords.py : a python file that identifies relevant passages in each snapshot
- ada_run.py : a python file that evaluates the relevant passages identified by ada_keywords.py and exports relevant passges to candidate_passages.csv
- candidate_passages.csv: relevant passages exported by ada_run.py
- reviewed_ada.csv: relevant passages after human review
- analysis of results for each model and comparison of performance between models

**Final Deliverables**
- research paper: ~ 2500 words total 
    - define and justify why we chose our L4s
    - show how we evaluated our modes
    - show the results and compare how the models performed
    - Methodological appendix (not included in word count)
    - AI usage appendix (not included in word count)
    - linked Github repository/history
