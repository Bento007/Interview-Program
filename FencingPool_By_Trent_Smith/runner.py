from tournament import Tournament

if __name__ == "__main__":

    fileList = ["MEconflicts.csv", "MEentries.csv", "MEshort.csv"]

    print("starting...")
    for file in fileList:
        tour = "Result_" + file.split('.')[0] + ".txt"
        with open(tour, "w") as result:
            t = Tournament(file)
            t.create()
            result.write("%s" % (t))