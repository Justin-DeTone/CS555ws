import test_age
import tag_parse as tag
import age
from family_structure_test import *


#KV User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(test_age.test_mar_b4_death('xp', people))
print(test_age.test_div_b4_death('xp', people))


#JT User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(uniqueIndividualIDsTest(people))
print(uniqueFamilyIDsTest(families))
print(listDeceasedTest(people))

#JD User Stories


#RT User Stories
