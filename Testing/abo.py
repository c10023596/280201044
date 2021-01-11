def anagrams(s):
  if s == "":
    return [s]
  else:
    answer = []
    for w in anagrams(s[1:]):
      for pos in range(len(w) + 1):
        answer.append(w[:pos]+s[0]+w[pos:])
    return answer

print(anagrams("cokps"))