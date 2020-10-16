# Summary-scores

The files in here are as follows:

Bed005.tsv is the general file for the meeting Bed005

Bed005_cleaned_.tsv is the cleaned version of the Bed005 meeting.

Bed005_scores.txt is the scoring metric that was used. Here utterance::frequency is the measurement. Each score is scored using Jin's excel file.

summary-score-out.py is the file that is used for generating the summary score. Runs from the terminal line with the following command:

<python3 summary-score-out.py windows.xlsx Bed005.tsv>

utterance_scores.py is used for developing an intuition, to run use the command:

<python3 utterance_scores.py windows.xlsx Bed005.tsv>
