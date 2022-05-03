import Laser_Gun_Rewritten

weapon = Laser_Gun_Rewritten.Laser_Weapon()
print(weapon)

# this prints out a pretty list of all the things
# purely optional but useful for debugging
weight_list = ["Rifle", "Light Machine Gun", "Submachinegun", "Carbine", "Pistol", "Sniper"]
weights = []
for i in range(len(weight_list)):
    weights.append((weight_list[i], weapon.weights[i]))
print(weights)