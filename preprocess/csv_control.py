import pandas as pd
import re
import csv


def convert_csv(raw_csv_path):
    test_df = pd.read_csv(
        raw_csv_path, header=None)
    test_df = test_df.drop(test_df.columns[1], axis=1)
    test_df.to_csv('test_dice.csv')

# replaceがなぜかできないので、exlで置き換え
# bash による操作でも可能。コードは以下
# cat test_datacp.csv | tr -d ] >  test_data_rev.csv

# csvによる読み込みは以下
# with open('/mnt/cloudy_z/src/yhamajima/Ureter_EDA/preprocess/testtest.csv', 'r') as rfile:
#     inf_result_re = rfile.read()
#     print(inf_result_re)
# test_csv = re.sub('[', '', inf_result_re)
# print(test_csv)
#  with open(new_path, 'w') as f:
#         f.write(test_csv)


def separate_along_dice(file_path,):
    # save_pathの策定
    new_path = './inf_clear.csv'

    test_df = pd.read_csv(
        file_path, header=None)
    test_df = test_df.drop(test_df.columns[0], axis=1)

    # make csv with dice more than or equal to 0.8 listed
    dice_max_08 = test_df[2] >= 0.8
    sum08 = dice_max_08.sum()
    list08 = test_df[dice_max_08]
    list08.to_csv('dice_max_08.csv')
    print(sum08)

    # make csv with dice greater than or equal to 0.6 but less than 0.8 listed
    dice_max_0608 = ((test_df[2] >= 0.6) & (test_df[2] < 0.8))
    sum0608 = dice_max_0608.sum()
    list0608 = test_df[dice_max_0608]
    list0608.to_csv('dice_max_0608.csv')
    print(sum0608)

    # make csv with dice greater than or equal to 0.5 but less than 0.6 listed
    dice_max_0506 = ((test_df[2] > 0.5) & (test_df[2] < 0.6))
    sum0506 = dice_max_0506.sum()
    list0506 = test_df[dice_max_0506]
    list0506.to_csv('dice_max_0506.csv')
    print(sum0506)

    # make csv with dice less than 0.5 listed
    dice_max_05 = (test_df[2] < 0.5)
    sum05 = dice_max_05.sum()
    list05 = test_df[dice_max_05]
    list05.to_csv('dice_max_05.csv')
    print(sum05)

    dice_max_0 = (test_df[2] == 0)
    sum00 = dice_max_0.sum()
    list00 = test_df[dice_max_0]
    list00.to_csv('dice_0.csv')

    # make csv with dice less than 0.5 listed (dice 0 ommited)
    dice_max_0500 = (test_df[2] < 0.5) & (test_df[2] != 0.0)
    sum0500 = dice_max_0500.sum()
    list0500 = test_df[dice_max_0500]
    list0500.to_csv('dice_max_05_0omit.csv')
    print(sum0500)

    print((sum08 + sum0608 + sum0506 + sum05))
    print(sum00)


if __name__ == '__main__':
    # convert_csv('/mnt/cloudy_z/src/yhamajima/eda_data/inf_result.csv')
    separate_along_dice(
        '/mnt/cloudy_z/src/yhamajima/Ureter_EDA/preprocess/test_dice_re.csv'
    )
