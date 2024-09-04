import glob
fname_wildcards = []
    fname_wildcards.append(fname_prefix + '_MODIFIED_*.' + fname_extension)

for wildcard in fname_wildcards:
    print(wildcard)
    keepers = []
    fnames_from_most_recent = sorted([f for f in glob.glob(wildcard[1:])], reverse=True)
    print(fnames_from_most_recent)
    for idx in range(1, len(fnames_from_most_recent)):
        os.system('cmp --silent -- {} {} > mod.txt'.format(
            fnames_from_most_recent[0], 
            fnames_from_most_recent[idx],
        ))
        with open('mod.txt', 'r') as f:
            bytes_diff = ''
            for line in f.readlines():
                bytes_diff.append(line)
            print(len(bytes_diff))
        if len(bytes_diff) == 0:
            os.system('rm {}'.format(fnames_from_most_recent[idx]))