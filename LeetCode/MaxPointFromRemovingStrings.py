#this one fails
def maximumGain( s, x, y):
    points = 0
    partial_string = ""
    s += " "
    for index, c in enumerate(s):

        if y > x:
            if "ba" in partial_string:
                partial_string = partial_string[0:len(partial_string) - 2]
                print(partial_string)
                points += y
            elif "ab" in partial_string and c != 'a':
                partial_string = partial_string[0:len(partial_string) - 2]
                print(partial_string)
                points += x
            partial_string += c
        else:
            if "ab" in partial_string:
                partial_string = partial_string[0:len(partial_string) - 2]
                print(partial_string)
                points += x
            elif "ba" in partial_string and c != 'a':
                partial_string = partial_string[0:len(partial_string) - 2]
                print(partial_string)
                points += y
            partial_string += c
    return points


#This one passes but is really inefficient
def maximumGain2(s, x, y):
        points = 0
        partial_string = ""
        s += " "
        ab_count = s.count('ab')
        ba_count = s.count('ba')
        while ab_count > 0 or ba_count > 0:
            if y > x:
                if ba_count > 0:
                    s = s.replace('ba', "")
                    points += y * ba_count
                    ba_count = s.count('ba')
                    ab_count = s.count('ab')
                elif ab_count > 0:
                    s = s.replace('ab', "")
                    points += x * ab_count
                    ba_count = s.count('ba')
                    ab_count = s.count('ab')
            else:
                if ab_count > 0:
                    s = s.replace('ab', "")
                    points += x * ab_count
                    ba_count = s.count('ba')
                    ab_count = s.count('ab')
                elif ba_count > 0:
                    s = s.replace('ba', "")
                    points += y * ba_count
                    ba_count = s.count('ba')
                    ab_count = s.count('ab')
        return points