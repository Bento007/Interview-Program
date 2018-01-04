from tournament import Tournament

import cProfile
def perf_test(data):
    for _ in range(1000):
        t = Tournament(file)
        t.create()

if __name__ == "__main__":

    fileList = ["MEconflicts.csv", "MEentries.csv", "MEshort.csv"]

    print("starting...")
    for file in fileList:
        # cProfile.run("perf_test(file)")

        tour = "Result_" + file.split('.')[0] + ".txt"
        with open(tour, "w") as result:
            t = Tournament(file)
            t.create()
            result.write("%s" % (t))