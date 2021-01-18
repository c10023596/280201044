class DNA:

  def __init__(self, A, T, G, C):
    self.A = A
    self.T = T
    self.G = G
    self.C = C
  
  def count_nucleotides(self):
    return {"A": self.A, "T": self.T, "G": self.G, "C": self.C}
  
  def calculate_complement(self):
    return {"A": self.T, "T": self.A, "G": self.C, "C": self.G}
  
  def count_point_mutations(self, dna):
    