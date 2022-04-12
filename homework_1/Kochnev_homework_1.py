import pandas as pd
import numpy as np

"""""""""""""""""
DATA PREPARATION
"""""""""""""""""

#It is needed for macOS
def correct_txt_delimeter(path):
    filename = path
    with open(filename) as infile, open('outfile.csv','w') as outfile:
        for line in infile:
            outfile.write(line.replace("\t",';'))
    df = pd.read_fwf(filename)
    df.to_csv('data/mtesrl_20150626_MD0000600012_stats.csv')

def form_working_dataset(path):
    #correct_txt_delimeter()
    df = pd.read_csv(path, sep="\t", skiprows=2)
    dataset_formed = df[['EVENT', 'AVGTSMR']]

    return dataset_formed

"""""""""""""""
    PART 1
"""""""""""""""
def solve_part_1(path):
    first_dataset_formed = form_working_dataset(path)
    min = first_dataset_formed.groupby('EVENT').min()
    min.rename(columns={'AVGTSMR': 'min'}, inplace=True)
    median = first_dataset_formed.groupby('EVENT').median()
    median.rename(columns={'AVGTSMR': 'median'}, inplace=True)
    res_90 = first_dataset_formed.groupby('EVENT').quantile(0.9)
    res_90.rename(columns={'AVGTSMR': '90%'}, inplace=True)
    res_99 = first_dataset_formed.groupby('EVENT').quantile(0.99)
    res_99.rename(columns={'AVGTSMR': '99%'}, inplace=True)
    res_99_9 = first_dataset_formed.groupby('EVENT').quantile(0.999)
    res_99_9.rename(columns={'AVGTSMR': '99.9%'}, inplace=True)

    table_part_1 = pd.concat([min, median, res_90, res_99, res_99_9], axis=1).to_csv('table_part_1.csv')
    #print("    T A S K 1")
    #print(pd.concat([min, median, res_90, res_99, res_99_9], axis=1))

"""""""""""""""
    PART 2
"""""""""""""""
def solve_part_2(path):
    #print("    T A S K 2")
    second_dataset_formed = form_working_dataset(path)
    transaction_types = second_dataset_formed['EVENT'].value_counts()

    for i in transaction_types.index:
        table_part_2 = pd.DataFrame(columns=['ExecTime', 'TransNo', 'Weight, %', 'Percent, %'])
        min = second_dataset_formed.AVGTSMR[second_dataset_formed["EVENT"] == i].min()
        res_99_9 = np.percentile(second_dataset_formed.AVGTSMR[second_dataset_formed["EVENT"] == i], 99.9)
        length = len(second_dataset_formed[(second_dataset_formed["EVENT"] == i)])
        percent = 0

        for j in range(int(min - min % 5), int(res_99_9), 5):
            quantity = len(second_dataset_formed[(second_dataset_formed["EVENT"] == i) & (second_dataset_formed['AVGTSMR'] <= j + 5) & (second_dataset_formed['AVGTSMR'] > j)])
            weight = quantity / length * 100
            percent += weight
            table_part_2.loc[len(table_part_2)] = [j + 5, int(quantity), weight, percent]

        table_part_2.to_csv('table_'+i+'.csv')


if __name__ == '__main__':
    # You may input file path below:
    path = 'mtesrl_20150626_MD0000600012_stats.txt'
    solve_part_1(path)
    solve_part_2(path)