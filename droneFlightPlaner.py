def calc_drone_min_energy(route):
  """ Calculate the minimum amount of energy required to keep
  a drone afloat when increasing altitude costs kilowatt hours
  of electricity and dropping altitude gains kilowatt hours.

  --route A 3D array of location changes of x, y, and z directions.

  Only the z location matters, as x and y movement does not
  cost electricity.

  Keeps track of the lowest point below zero that the drone
  costs in kilowatt hours.  At minimum, the drone needs at
  least that many KWh to say afloat and not crash when
  raising altitude.
  """

  total_energy = 0
  prev_height = route[0][2]
  min_req = 0
  
  for coord in route[1:]:
    curr_height = coord[2]
    total_energy -= curr_height - prev_height
    prev_height = coord[2]
    
    if total_energy < 0 and total_energy < min_req:
      min_req = total_energy
    
  return -min_req
    
  
# Simple Test
route = [ [0,   2, 10],
          [3,   5,  0],
          [9,  20,  6],
          [10, 12, 15],
          [10, 10,  8] ]

output = 5

print(calc_drone_min_energy(route))
