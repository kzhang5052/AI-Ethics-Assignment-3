# AI Ethics Assignment 3

This project compares what providers document about real-time scam warnings for older adults (ADA) with how two chat models respond to potential scams (AIE).

| Location | Purpose |
| --- | --- |
| [ADA evidence log](ada/evidence.md) | Record quotations, document locations, and which parts of the indicator each quotation supports. |
| [Source register](research/l4-ada-source-register-2026-11-20.json) and [keyword rules](ada_keywords.py) | Find documents and candidate passages for manual review. |
| [AIE prompts](aie/prompts.json) | Draft scam scenarios and benign controls to send to both models. |
| [Runs](runs/) | Save model responses and judgments by run. |
| [Paper](report/paper.md) and [methodological appendix](report/appendix.md) | Explain the measures, comparison, and limitations. |

## Getting started

1. Open the source register, select a provider document, and add one verified quotation to the ADA evidence log.
2. Review the draft prompts and define scoring criteria in the appendix before collecting responses.
3. For each run, record the date, model identifiers, settings, prompt IDs, verbatim responses, and judgments so the comparison can be checked.
