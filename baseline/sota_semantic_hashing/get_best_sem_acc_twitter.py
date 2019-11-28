
dir_path = './results/results_semhash_twitter_sentiment140_10runs/'

runs = 10

for data_type in ["corr", "inc", "inc_with_corr"]:
    str_write = ''
    for dataset_name in ['sentiment140']:
        str_write += dataset_name + '\n'

        acc_avg = 0
        acc_max = 0
        for run in range(1, runs + 1):
            acc = 0
            subdir_path = dir_path + '{}_run{}/'.format(data_type, run)
            filename = subdir_path + '{}_f1.txt.txt'.format(dataset_name)
            f = open(filename, 'r')
            lines = f.read().split('\n')
            # Get max acc from 1 run
            for l in lines:
                if l is not "":
                    l_split = l.split(': ')
                    l_acc = float(l_split[1])
                    print(l_acc)
                    if l_acc >= acc:
                        acc = l_acc
            # Get average acc
            acc_avg += acc
            # Get max acc
            if acc >= acc_max:
                acc_max = acc
        acc_avg /= runs
        str_write += '  Avg-{}: {:.2f}\n'.format(runs, acc_avg * 100)
        str_write += '  Best-{}: {:.2f}\n\n'.format(runs, acc_max * 100)
    f_out = open(dir_path + data_type, 'w')
    f_out.write(str_write)