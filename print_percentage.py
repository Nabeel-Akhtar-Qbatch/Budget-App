def printProgressBar(value, label, amnt):
    n_bar = 40 #size of progress bar
    max = 100
    j = value/max
    bar = '█' * int(n_bar * j)
    bar = bar + '-' * int(n_bar * (1 - j))
    print(f"\n{label.ljust(1)} (PKR. {amnt})| [{bar:{n_bar}s}] {int(100 * j)}% ")

