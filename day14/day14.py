from collections import defaultdict

def process_data():
  file = open("2021/day14/input.txt", "r")
  polymer_string = file.readline().strip()
  pair_count = defaultdict(int)
  for i in range(len(polymer_string)-1):
    pair_count[polymer_string[i:i+2]] += 1
  string_ends =polymer_string[0]+polymer_string[-1]
  file.readline() 
  rules = {}
  for line in file.read().splitlines():
    [pair, insert] = line.split(' -> ')
    rules[pair]= insert
  return pair_count, string_ends, rules

def one_step(old_pairs, rules):
  new_pairs = defaultdict(int)
  for pair in old_pairs:
    first,second = pair
    if not(pair in rules):
      print(pair,'not found in rules')
    new_pairs[first+rules[pair]]+= old_pairs[pair]
    new_pairs[rules[pair]+second]+= old_pairs[pair]
  return new_pairs

def count_letters(pairs, ends): 
  lettercount = defaultdict(int)
  for a,b in pairs:
    lettercount[a]+= pairs[a+b]
    lettercount[b]+= pairs[a+b]
  for c in ends: 
    lettercount[c] += 1 
    #because letters occur with multiplicity 2, except the ends ones
  for c in lettercount:
    lettercount[c] = lettercount[c] //2   
  return lettercount

def polymerize(steps):
  pairs, ends, rules = process_data()
  for _ in range(steps):
    pairs = one_step(pairs, rules)
  lettercount = count_letters(pairs, ends)

  return max(lettercount.values()) - min(lettercount.values())

def Main():
  print(f'Part 1: {polymerize(10)}\nPart 2: {polymerize(40)}')
  
if __name__ == '__main__':
    Main()
