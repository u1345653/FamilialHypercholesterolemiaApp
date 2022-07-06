class Person(object):
  def __init__( self, pedigree_position):
    self.pedigree_position = pedigree_position
    self.age = 0
    self.gender = "f"
    self.ldl_cholesterol = 0
    self.total_cholesterol = 0
    self.tendon_xanthoma_status = 9
    self.coronary_artery_status = 9
    self.coronary_artery_age = 0
    self.dna_dx_status = 9
    self.fh_probability = 0.00

    if pedigree_position == 1:
      self.pedigree_role = 'Grandparent 1'
    elif pedigree_position == 2:
      self.pedigree_role = 'Grandparent 2'
    elif pedigree_position == 3:
      self.pedigree_role = 'Parent 2'
    elif pedigree_position == 4:
      self.pedigree_role = 'Sibling 1'
    elif pedigree_position == 5:
      self.pedigree_role = 'Sibling 2'
    elif pedigree_position == 6:
      self.pedigree_role = 'Parent 1'
    elif pedigree_position == 7:
      self.pedigree_role = 'Child 1'
    elif pedigree_position == 8:
      self.pedigree_role = 'Child 2'
    elif pedigree_position == 9:
      self.pedigree_role = 'Child 3'

  def add_age(self, age):
    self.age = age
    return age

  def add_gender(self, gender):
    self.gender = gender
    return gender

  def add_ldl_cholesterol(self, ldl_cholesterol):
    self.ldl_cholesterol = ldl_cholesterol
    return ldl_cholesterol

  def add_total_cholesterol(self, total_cholesterol):
    self.total_cholesterol = total_cholesterol
    return total_cholesterol

  def add_cad_status(self, coronary_artery_status):
    self.coronary_artery_status = coronary_artery_status
    return coronary_artery_status

  def add_cad_age(self, coronary_artery_age):
    self.coronary_artery_age = coronary_artery_age
    return coronary_artery_age

  def add_dna_dx_status(self, dna_dx_status):
    self.dna_dx_status = dna_dx_status
    return dna_dx_status