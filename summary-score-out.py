#Python file for mapping student utternaces
import sys
import os
import pandas as pd
import numpy as np
from rouge_score import rouge_scorer
import re

def main():
    model_output = sys.argv[1]
    utterances_in   = sys.argv[2]

    #model_output = r'/Users/alexro/PycharmProjects/BART-Review/windows.xlsx'
    #utterances = r'/Users/alexro/PycharmProjects/BART-Review/Bed005.tsv'
    df = pd.read_excel(model_output)

    summary = df['summary'].tolist()
    #print(summary)

    gs_labels = []

    with open(utterances_in, "r") as utter:
        text = utter.read()

    for lines in text.split('\n'):
        #print(lines.split("::")[1])
        if len(lines.split('::')[1].strip().split()) > 3:
            gs_labels.append(lines.split('::')[1].strip())


    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    summary_score = []

    x = [0,1000]
    #out = r'/home/aroustai/Summary_Scores/output/Bed005_75' + str(i) + '.txt'
    out = r'/home/aroustai/Summary_Scores/output/Bed005_scores.txt'

    for items in gs_labels:
        summary_score.append([items,0])

    for window in summary:
        for i, utterances in enumerate(gs_labels):
                scores = scorer.score(utterances,window)

                #convert rougeL recall string to a float
                score_split = str(scores["rougeL"])
                recall = score_split.split(" recall=")[1].split(",")[0]
                recall = float(recall.replace(")", "").strip())

                #print(summary_score[i])

                if recall >0.7:
                    #print(range(len(summary_score)))
                    summary_score[i][1] +=1

                    #print(range(len(summary_score)))
                    #print(summary_score[i])


            #for utt, scores in summary_score:

    with open(out, 'w+') as f:
        for utterance, frequency in summary_score:
            f.write(str(utterance) + '::' + str(frequency))
            f.write(("\n"))


            #summary_score = []
            #x[0] = x[0] + 200
            #x[1] = x[1] + 200

    #print(summary_score)

main()

