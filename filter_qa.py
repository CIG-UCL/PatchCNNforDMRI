import argparse

def load_eddy(path, thresholda=2, thresholdb=1, thresholdc=3, thresholdd=1, thresholde=0.1, lineno=96):
	"""
	"""
	filename = '/QAfrom-eddylog.txt'

	pfile = open(path + filename, 'r')

	lines = pfile.readlines()
	
	if lineno is None:
		lineno = len(lines) - 1
        
	move = []

	#for line in lines-1:
	for i in range(lineno):
		line = lines[i]
		m = 0
		t0, _, t1, _, r0, _, r1, _, out, _, _ = line.split(' ')
		t0, t1, r0, r1, out = float(t0), float(t1), float(r0), float(r1), float(out)
		if t0 < thresholda and t1 < thresholdb and r0 < thresholdc and r1 < thresholdd and out < thresholde:
			m = 1

		move.append(m)
	
               # print line.split(' ')
	pfile.close()

	pfile = open(path + '/scheme.txt', 'w')
	pfile.writelines("%s " % str(item) for item in move)
	pfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--t0", type=float)
    parser.add_argument("--t1", type=float)
    parser.add_argument("--r0", type=float)
    parser.add_argument("--r1", type=float)
    parser.add_argument("--out", type=float)
    parser.add_argument("--num", type=int)
    args = parser.parse_args()

    load_eddy(args.path, args.t0, args.t1, args.r0, args.r1, args.out, args.num)
