'''
Author: Trent Smith
Date:   07/25/2017
'''

class Rank():
    'Represent the rank Example: A15, U, C5'
    def __init__(self,rank):
        rank = rank.upper()
        if rank == 'U':
            self.rankLetter = rank
            self.rankNumber = 0
        else:
            self.rankLetter = rank[0]
            self.rankNumber = int(rank[1:])

    def __eq__(self, rank2):
        return (self.rankLetter == rank2.rankLetter and
                self.rankNumber == rank2.rankNumber )

    def __ne__(self, rank2):
        return (self.rankLetter != rank2.rankLetter or
                self.rankNumber != rank2.rankNumber )

    def __lt__(self, rank2):
        return self.rankLetter > rank2.rankLetter or (self.rankLetter == rank2.rankLetter and
                                                  self.rankNumber < rank2.rankNumber)

    def __le__(self, rank2):
        return self.rankLetter > rank2.rankLetter or (self.rankLetter == rank2.rankLetter and
                                                  self.rankNumber <= rank2.rankNumber)

    def __gt__(self,rank2):
        return self.rankLetter < rank2.rankLetter or (self.rankLetter == rank2.rankLetter and
                                                  self.rankNumber > rank2.rankNumber)

    def __ge__(self, rank2):
        return self.rankLetter < rank2.rankLetter or (self.rankLetter == rank2.rankLetter and
                                                  self.rankNumber >= rank2.rankNumber)

    def __str__(self):
        if self.rankNumber:
            return '%s\t%i\t' % (self.rankLetter, self.rankNumber)
        else:
            return '%s' % (self.rankLetter)

    def __repr__(self):
        return (self.rankLetter,self.rankNumber)


class Fencer():
    'Representing a person who will be in the tournament.'
    def __init__( self, lastName, firstName,
                  school, rank ):

        self.lastName = lastName
        self.firstName= firstName
        self.rank = Rank(rank)

        # if len(school) == 0:
        if school == '':
            self.school='unafilliated'
        else:
            self.school=school

    def __str__(self):
        return '%-16s\t%-16s\t%-32s\t%s' % (self.firstName, self.lastName,
                                       self.school, self.rank)
    def __repr__(self):
        return [ self.firstName, self.lastName,self.school, self.rank]