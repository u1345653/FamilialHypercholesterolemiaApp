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

  def get_age(self):
    return self.age

  def get_gender(self):
    return self.gender

  def get_ldl_cholesterol(self):
    return self.ldl_cholesterol

  def get_total_cholesterol(self):
    return self.total_cholesterol

  def get_cad_status(self):
    return self.coronary_artery_status

  def get_cad_age(self):
    return self.coronary_artery_age

  def get_dna_dx_status(self):
    return self.dna_dx_status