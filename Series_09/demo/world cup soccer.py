def processMatches(filename):
    
    """
    >>> stats = processMatches('worldcup2010.txt')
    >>> stats
    {'A': {'Uruguay': [1, 1, 1, 3, 2], 'Mexico': [0, 2, 1, 1, 5], 'France': [2, 0, 1, 6, 2], 'South Africa': [1, 1, 1, 3, 4]}, 'C': {'Slovenia': [1, 1, 1, 6, 6], 'England': [0, 0, 3, 4, 4], 'Algeria': [0, 2, 1, 3, 7], 'USA': [2, 0, 1, 5, 1]}, 'B': {'Argentina': [2, 1, 0, 3, 2], 'Greece': [3, 0, 0, 3, 0], 'Nigeria': [1, 2, 0, 2, 3], 'South Korea': [0, 3, 0, 0, 3]}, 'E': {'Denmark': [1, 2, 0, 3, 4], 'Netherlands': [2, 0, 1, 3, 1], 'Cameroon': [1, 0, 2, 4, 2], 'Japan': [0, 2, 1, 0, 3]}, 'D': {'Ghana': [1, 1, 1, 3, 3], 'Serbia': [1, 1, 1, 3, 4], 'Australia': [1, 2, 0, 3, 6], 'Germany': [2, 1, 0, 5, 1]}, 'G': {'Brazil': [3, 0, 0, 3, 0], 'North Korea': [1, 1, 1, 2, 2], 'Portugal': [0, 2, 1, 1, 3], 'Ivory Coast': [1, 2, 0, 3, 4]}, 'F': {'Paraguay': [2, 0, 1, 5, 2], 'Slovakia': [0, 0, 3, 3, 3], 'New Zealand': [0, 2, 1, 2, 6], 'Italy': [1, 1, 1, 4, 3]}, 'H': {'Switzerland': [1, 0, 2, 3, 2], 'Honduras': [0, 1, 2, 1, 2], 'Spain': [0, 0, 3, 1, 1], 'Chile': [1, 1, 1, 3, 3]}}
    >>> stats['A']
    {'Uruguay': [1, 1, 1, 3, 2], 'Mexico': [0, 2, 1, 1, 5], 'France': [2, 0, 1, 6, 2], 'South Africa': [1, 1, 1, 3, 4]}
    >>> stats['B']
    {'Argentina': [2, 1, 0, 3, 2], 'Greece': [3, 0, 0, 3, 0], 'Nigeria': [1, 2, 0, 2, 3], 'South Korea': [0, 3, 0, 0, 3]}
    >>> stats['F']
    {'Paraguay': [2, 0, 1, 5, 2], 'Slovakia': [0, 0, 3, 3, 3], 'New Zealand': [0, 2, 1, 2, 6], 'Italy': [1, 1, 1, 4, 3]}
    """
    
    fl = open(filename, 'r')
    stats = {}
    for line in fl:
        if not line.startswith('#'):
            line = line.strip().split(',')
            if len(line) == 4:
                
                # gegevens over wedstrijd inlezen
                hometeam, awayteam, score, group = line
                homegoals, awaygoals = [int(x) for x in score.split('-')]
                
                # datastructuur bijgewerken
                if group not in stats:
                    stats[group] = {}
                if hometeam not in stats[group]:
                    stats[group][hometeam] = [0, 0, 0, 0, 0]
                if awayteam not in stats[group]:
                    stats[group][awayteam] = [0, 0, 0, 0, 0]
                    
                # bijwerken aantal doelpunten
                stats[group][hometeam][3] += homegoals
                stats[group][hometeam][4] += awaygoals
                stats[group][awayteam][3] += awaygoals
                stats[group][awayteam][4] += homegoals
    
                # bijwerken gevonnen, verloren, en gelijke spelen
                if homegoals > awaygoals:
                    homegoals, awaygoals = 0, 1
                elif homegoals < awaygoals:
                    homegoals, awaygoals = 1, 0
                else:
                    homegoals, awaygoals = 2, 2
                stats[group][hometeam][homegoals] += 1
                stats[group][awayteam][awaygoals] += 1
                
    return stats

def showGroup(stats, group, filename=None):

    """
    >>> stats = processMatches('worldcup2010.txt')
    >>> showGroup(stats, 'A')
                                GROUP A                            
    +-----------------------+-----+-------------------------+-----+
    |                       |   P |   W   L   D   F   A   S | Pts |
    +-----------------------+-----+-------------------------+-----+
    |                France |   3 |   2   0   1   6   2   4 |   7 |
    |               Uruguay |   3 |   1   1   1   3   2   1 |   4 |
    |          South Africa |   3 |   1   1   1   3   4  -1 |   4 |
    |                Mexico |   3 |   0   2   1   1   5  -4 |   1 |
    +-----------------------+-----+-------------------------+-----+
    >>> showGroup(stats, 'D')
                                GROUP D                            
    +-----------------------+-----+-------------------------+-----+
    |                       |   P |   W   L   D   F   A   S | Pts |
    +-----------------------+-----+-------------------------+-----+
    |               Germany |   3 |   2   1   0   5   1   4 |   6 |
    |                 Ghana |   3 |   1   1   1   3   3   0 |   4 |
    |                Serbia |   3 |   1   1   1   3   4  -1 |   4 |
    |             Australia |   3 |   1   2   0   3   6  -3 |   3 |
    +-----------------------+-----+-------------------------+-----+
    >>> showGroup(stats, 'F')
                                GROUP F                            
    +-----------------------+-----+-------------------------+-----+
    |                       |   P |   W   L   D   F   A   S | Pts |
    +-----------------------+-----+-------------------------+-----+
    |              Paraguay |   3 |   2   0   1   5   2   3 |   7 |
    |                 Italy |   3 |   1   1   1   4   3   1 |   4 |
    |              Slovakia |   3 |   0   0   3   3   3   0 |   3 |
    |           New Zealand |   3 |   0   2   1   2   6  -4 |   1 |
    +-----------------------+-----+-------------------------+-----+
    >>> showGroup(stats, 'F', 'groupF.txt')

    >>> stats = processMatches('worldcup2006.txt')
    >>> showGroup(stats, 'G')
                                GROUP G                            
    +-----------------------+-----+-------------------------+-----+
    |                       |   P |   W   L   D   F   A   S | Pts |
    +-----------------------+-----+-------------------------+-----+
    |           Switzerland |   3 |   2   0   1   4   0   4 |   7 |
    |                France |   3 |   1   0   2   3   1   2 |   5 |
    |           South Korea |   3 |   1   1   1   3   4  -1 |   4 |
    |                  Togo |   3 |   0   3   0   1   6  -5 |   0 |
    +-----------------------+-----+-------------------------+-----+

    >>> stats = processMatches('worldcup2002.txt')
    >>> showGroup(stats, 'H')
                                GROUP H                            
    +-----------------------+-----+-------------------------+-----+
    |                       |   P |   W   L   D   F   A   S | Pts |
    +-----------------------+-----+-------------------------+-----+
    |                 Japan |   3 |   2   0   1   5   2   3 |   7 |
    |               Belgium |   3 |   1   0   2   6   5   1 |   5 |
    |                Russia |   3 |   1   2   0   4   4   0 |   3 |
    |               Tunisia |   3 |   0   2   1   1   5  -4 |   1 |
    +-----------------------+-----+-------------------------+-----+
    """
    
    if filename:
        fl = open(filename, 'w')
    else:
        import sys
        fl = sys.stdout
        
    sep1 = '+-----------------------+-----+-------------------------+-----+'
    sep2 = '|                       |   P |   W   L   D   F   A   S | Pts |'
    
    fl.write('GROUP {}'.format(group).center(len(sep1)) + '\n')
    fl.write('{}\n'.format(sep1))
    fl.write('{}\n'.format(sep2))
    fl.write('{}\n'.format(sep1))
    for team, score in sorted(
        stats[group].items(), 
        key=lambda x: (-3 * x[1][0] - x[1][2], x[1][4] - x[1][3], x[0])
    ):
        template = '| {:>21s} | {:3d} | {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} | {:3d} |\n'
        fl.write(
            template.format(
                team,
                sum(score[:3]),
                score[0],
                score[1],
                score[2],
                score[3],
                score[4],
                score[3] - score[4],
                3* score[0] + score[2]
            )
        )
    fl.write('{}\n'.format(sep1))
        
    if filename:
        fl.close()
       
if __name__ == '__main__':
    import doctest
    doctest.testmod()