'''
Author: Trent Smith
Date:   07/25/2017
'''

from math import ceil
from fencer import Fencer

class Pool():
    """Tracks the participant in a pool"""

    def __init__(self, number=0):
        self.schools = {}
        self.participants = []
        self.poolSize = 0
        self.poolNumber = number

    def addParticipant(self,participant):
        self.participants.append(participant)
        self.poolSize+=1
        self.schools[participant.school] = self.schools.setdefault(participant.school, 0) + 1

    def removeParticipant(self,participant):
        #check if participant is in pool
        try:
            self.participants.remove(participant)
            self.poolSize-=1
            self.schools[participant.school] = self.schools[participant.school] - 1

        except ValueError:
            print("Participant Not In Pool")

    def __lt__(self, pool2):
        return self.poolSize < pool2.poolSize

    def __len__(self):
        return self.poolSize

    def __str__(self):
        response = '--)------- Pool # %2i -------(-- (%i)\n' % (self.poolNumber, self.poolSize)
        for participant in self.participants:
            response += '%s\n' % (participant)
        return response

    def __repr__(self):
        return 'poolNumber: %2i, poolSize: %i, participants: %s' % (self.poolNumber, self.poolSize,
                                                                    self.participants)

class Tournament():
    def __init__(self, CSVFile):
        self.participants = []
        self.totalEntries = 0
        self.schoolPoolMax = {}
        self.CSVFile = CSVFile
        self.poolMax = 0
        self.poolCount = 0
        self.pools = []

    def create(self):
        '''creates the tournament pools based on rank and school.'''
        self._readRoster()
        self._sortParticipantsByRank()
        self._calculatePoolSize()
        self._calculateSchoolMaxPerPool()
        self._populatePools()

    def _readRoster(self):
        """Read a CSV file of participants"""
        with open(self.CSVFile, "r") as data:
            for line in data:
                try:
                    self.participants.append(Fencer( *[i.strip() for i in line.split(',')] ) )
                except ValueError as error:
                    print ('File:%s caused %s. Invalid data: "%s"' % (self.CSVFile, error,line))
        self.totalEntries = len(self.participants)

    def _calculateSchoolMaxPerPool(self):
        """Determine the maximum number of participants allowed from the same school in each pool
        Pre: self.participants has been populated with Fencers
        Post: self.schoolPoolMax is updated"""
        for i in self.participants:
            school = i.school
            self.schoolPoolMax[school] = self.schoolPoolMax.setdefault(school,0.0) + 1
        for i in self.schoolPoolMax:
            if i != 'unafilliated':
                self.schoolPoolMax[i] = ceil (self.schoolPoolMax[i] / self.poolCount)

    def _sortParticipantsByRank(self):
        """Sorts the self.participants by rank. Example  A15 > A14 > A13 > B15
        Pre: self.participants has been populated with Fencers.
        Post: self.participants list is sorted from highest to lowest rank"""
        self.participants.sort(key=lambda participants: participants.rank, reverse=True)

    def _calculatePoolSize(self):
        """Calculates pools size based on the number of participants.
        Pre: self.participants has been populated with Fencers.
        Post: self.poolMax and self.poolCount are updated"""

        # total = len(self.participants)
        total = self.totalEntries
        if total%6 == 0:
            self.poolCount = total // 6
            self.poolMax=6
        elif total%6 == 1:
            self.poolCount = total // 6
            self.poolMax=7
        elif total%7 == 0:
            self.poolCount = total // 7
            self.poolMax = 7
        elif total%7 == 1:
            self.poolCount = total // 7
            self.poolMax = 8
        elif total%8 == 0:
            self.poolCount = total // 8
            self.poolMax = 8
        else:
            self.poolCount = total // 6 + 1
            self.poolMax = 6

    def _populatePools(self):
        """Fills the pools with participants based on rank and school.
        Pre: self.poolMax and self.poolCount assigned
        Post: self.pools are assign participants"""

        pools = self.pools
        poolCount = self.poolCount
        participants = self.participants

        for i in range(1,poolCount+1):
            pools.append(Pool(i))

        #snake version
        modifier = 1 #used to snake through pools
        j=0
        # for i in range(len(self.participants)):
        for i in range(self.totalEntries):
            if i % poolCount == 0:
                modifier = -modifier
            j_last = j
            while(self._atPoolLimit(pools[j], participants[i])):
                j = (j + modifier) % poolCount
                if j == j_last: #prevent infinte loop
                    break

            pools[j].addParticipant(participants[i])
            j = (j + modifier) % poolCount

    def _atPoolLimit(self, pool, participant):
        """Returns True if the pools is full or there are too many participants from the same school in the same pool"""
        return ( pool.poolSize >= self.poolMax
            or pool.schools.setdefault(participant.school,0.0) == self.schoolPoolMax[participant.school] )

    def __str__(self):
        response = "Competitor List\n"
        for i in self.participants:
            response += "%s\n" % (i)
        response += "\n"
        for i in self.pools:
            # response += '--)-------- Pool # %2i -------(--(%i)\n' % (i.poolNumber, i.poolSize)
            response += "%s\n" % (i)
        return response

    def __repr__(self):
        return 'CSVFile = %s, schoolPoolMax = %s, poolMax = %i, poolCount = %i, participants = %s, pools = %s' %\
               (self.CSVFile, self.schoolPoolMax, self.poolMax, self.poolCount, self.participants, self.pools)
