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



    #print(gs_labels)

    best_score = 0
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    summary_score = []

    #print(summary[0])

    i = 0
    x = [0,1000]
    #out = r'/home/aroustai/Summary_Scores/output/Bed005_75' + str(i) + '.txt'
    out = r'/home/aroustai/Summary_Scores/output/Bed005_70.txt'

    with open(out, 'w+') as f:
        for window in summary:
            #print("Running Rouge_L score on summary: " + str(i))
            f.write("For window: " + str(x[0]) + "<---->" + str(x[1]) + "\n")
            for utterances in gs_labels:
                scores = scorer.score(utterances,window)

                #if scores > best_score:
                #    best_score = scores
                #    best_label = words
                #print(scores)
                score_split = str(scores["rougeL"])
                #print(scores)
                recall = score_split.split(" recall=")[1].split(",")[0]
                recall = float(recall.replace(")", "").strip())
                #print(prec)
                #prec = prec[0].split('=')[1]
                #print(prec)
                if recall >0.7:
                    summary_score.append([utterances, scores["rougeL"]])
                    #print(utterances, scores["rougeL"])



            for utt, scores in summary_score:
                f.write(str(utt) + ' :: ' + str(scores))
                f.write("\n\n")

            summary_score = []
            x[0] = x[0] + 200
            x[1] = x[1] + 200


main()

