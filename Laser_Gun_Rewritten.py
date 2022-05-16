import random

# data structure: each component has a dictionary based on tag, which each contains a list of components: those are a dictionary of a name (string) and a tuple containing weights
# each tuple is (rifle, LMG, SMG, carbine, pistol, sniper)
# Tag rewrite has been done! see below, however
# also, while we're on the topic, each assignment should *really* be a function because I repeat the same thing with almost zero variation for *each attribute HOLY FUCK*
tag_dict = {
    "Stock Type" : {    
        "straight-grip stock" : (2, 3, -2, 0, -2, 3),
        "pistol grip and shoulder stock" : (3, 2, 1, 1, -3, 1),
        "semi-grip stock" : (3, 1, -3, 3, -2, 2),
        "near-vertical grip and shoulder stock" : (3, 1, -2, 1, -1, 3),
        "thumb-hole stock" : (2, 3, -2, 2, -1, 1),
        "pistol grip and compact stock" : (-1, -1, 2, 0, 1, -1),
        "pistol grip without a shoulder stock" : (-4, -4, 3, 2, 3, -4),
    },
    "Stock Material" : {
        "alloy" : (0, 0, 0, 0, 0, 0,),
        "wood" : (0, 0, 0, 0, 0, 0,),
        "plastic" : (0, 0, 0, 0, 0, 0,),
        "composite" : (0, 0, 0, 0, 0, 0,)
    },
    "Stock Construction" : {
        "fixed" : (2, 2, -2, -1, -3, 2),
        "folding" : (2, -2, 3, 2, 2, -3),
        "skeletonized" : (2, -2, 3, 2, -2, -3),
    },
    "Barrel Length" : {
        "6 inches" : (-4, -3, 2, 1, 2, -5),
        "12 inches" : (-1, -2, 2, 1, -1, -3),
        "16 inches" : (0, -1, 1, 1, -1, -2),
        "18 inches" : (1, -1, 1, 0, -2, -1),
        "20 inches" : (0, 0, -1, -1, -3, 0),
        "24 inches" : (-1, 1, -2, -2, -3, 2),
    },
    "Barrel Focus": {
        "short-focus" : (-3, -2, 2, 1, 1, -5),
        "medium-focus" : (0, -1, 2, 1, 1, -2),
        "long-focus" : (1, 1, -1, 0, -1, 3),
    },
    "Barrel Accessory" : {
        "collimator" : (2, 2, -2, -2, -3, 5),
        "beam splitter" : (0, -1, 2, -1, -2, -5),
        "compensator" : (1, 2, -2, -2, -3, 3),
        "bloom suppressor" : (1, -2, -1, 0, 2, 4),
        "set of heatsink fins" : (2, 4, 4, 2, 1, -4),
    },
    "Beam Spectrum" : {
        "infrared" : (0, 0, 0, 0, 0, 0), 
        "visible-light" : (0, 0, 0, 0, 0, 0),
        "ultraviolet" : (0, 0, 0, 0, 0, 0),
        "x-ray" : (0, 0, 0, 0, 0, 0), 
    },
    "Beam Mode" : {
        "continuous" : (0, 2, 2, 1, 0, -2),
        "pulsed" : (0, -2, -2, -1, 0, 2)
    },
    "Magazine Loading" : {
        "side" : (0, 0, 0, 0, -2, -2),
        "bottom" : (2, 2, 2, 1, -1, 2),
        "top" : (-1, -1, 1, 0, -2, -5),
        "inside of the stock" : (1, 2, -2, 3, 3, 0),
        "inside of a hinge break" : (1, -1, -2, 0, 2, 3),
    },
    "Magazine Shape" : {
        "light cylinder" : (-3, -2, 2, 0, 4, -5),
        "light box" : (-3, -2, 2, 0, 4, -5),
        "medium cylinder" : (1, 2, -2, 0, -1, -1),
        "medium box" : (1, 2, -2, 0, -1, -1),
        "heavy cylinder" : (0, 2, -3, -2, -5, 5),
        "heavy box" : (0, 2, -3, -2, -5, 5),
    },
    "Top Accessory" : {
        "reflex sight" : (3, 1, 2, 2, 1, -2),
        "iron sight" : (0, 0, 3, 1, 3, -5),
        "low-magnification optical sight" : (-1, 2, -2, -1, -2, 2),
        "high-magnification optical sight" : (-1, 2, -4, -3, -5, 5),
    },
    "Bottom Accessory" : {
        "bipod" : (1, 3, -2, -3, -5, 3),
        "foregrip" : (3, -2, 3, 1, 1, -3),
        "empty rail" : (1, -2, 2, 1, 3, -5),
        "tac-light" : (0, 0, 0, 0, 0, 0)
    },
    "Weapon Shape" : {
        "boxy" : (0, 0, 0, 0, 0, 0),
        "curvy" : (0, 0, 0, 0, 0, 0),
        "slim" : (0, 0, 0, 0, 0, 0),
    }
}

stock_type_dict = {
    "Rifle" : [
        "straight-grip stock", 
        "pistol grip and shoulder stock",
        "semi-grip stock",
        "near-vertical grip and shoulder stock",
        "thumb-hole stock",
    ],
    "Light Machine Gun" : [
        "straight-grip stock",
        "pistol grip and shoulder stock",
        "semi-grip stock",
        "thumb-hole stock",
    ],
    "Submachinegun" : [
        "pistol grip and compact stock",
        "pistol grip without a shoulder stock"
    ],
    "Carbine" : [
        "semi-grip stock",
        "pistol grip and shoulder stock",
        "pistol grip without a shoulder stock",
        "thumb-hole stock",
        "pistol grip and compact stock",
    ],
    "Pistol" : [
        "pistol grip without a shoulder stock",
        "pistol grip and shoulder stock",
    ],
    "Sniper" : [
        "thumb-hole stock",
        "straight-grip stock",
        "near-vertical grip and shoulder stock",
        "semi-grip stock",
    ]
}
stock_material_dict = {
    "Rifle" : [
        "alloy",
        "wood",
        "plastic",
        "composite",
    ],
    "Light Machine Gun" : [
        "alloy",
        "wood",
        "plastic",
        "composite",
    ],
    "Submachinegun" : [
        "alloy",
        "wood",
        "plastic",
        "composite",
    ],
    "Carbine" : [
        "alloy",
        "wood",
        "plastic",
        "composite",
    ],
    "Pistol" : [
        "alloy",
        "plastic",
        "composite",
    ],
    "Sniper" : [
        "alloy",
        "wood",
        "plastic",
        "composite",
    ]
}
stock_construction_dict = {
    "Rifle": [
        "fixed",
        "folding",
        "skeletonized"
    ],
    "Light Machine Gun": [
        "fixed",
    ],
    "Submachinegun": [
        "fixed",
        "folding",
        "skeletonized",
    ],
    "Carbine": [
        "fixed",
        "folding",
        "skeletonized",
    ],
    "Pistol": [
        "fixed",
        "folding",
        "skeletonized",
    ],
    "Sniper": [
        "fixed"
    ]
}
barrel_length_dict = {
    "Rifle" : [
        "12 inches",
        "16 inches",
        "18 inches",
        "20 inches",
        "24 inches",
    ],
    "Light Machine Gun" : [
        "18 inches",
        "20 inches",
        "24 inches",
    ],
    "Submachinegun" : [
        "6 inches",
        "12 inches",
        "16 inches",
        "18 inches",
    ],
    "Carbine" : [
        "12 inches",
        "16 inches",
        "18 inches",
    ],
    "Pistol" : [
        "6 inches",
        "12 inches",
    ],
    "Sniper" : [
        "18 inches",
        "20 inches",
        "24 inches",
    ]
}
barrel_focus_dict = {
    "Rifle" : [
        "medium-focus",
        "long-focus",
    ],
    "Light Machine Gun" : [
        "medium-focus",
        "long-focus",
    ],
    "Submachinegun" : [
        "short-focus",
        "medium-focus",
    ],
    "Carbine" : [
        "short-focus",
        "medium-focus",
        "long-focus"
    ],
    "Pistol" : [
        "short-focus",
        "medium-focus",
    ],
    "Sniper" : [
        "long-focus"
    ]
}
barrel_accessory_dict = {
    "Rifle" : [
        "collimator",
        "compensator",
        "bloom suppressor",
        "set of heatsink fins",
    ],
    "Light Machine Gun" : [
        "collimator",
        "beam splitter",
        "compensator",
        "bloom suppressor",
        "set of heatsink fins",
    ],
    "Submachinegun" : [
        "beam splitter",
        "compensator",
        "set of heatsink fins",
    ],
    "Carbine" : [
        "collimator",
        "beam splitter",
        "compensator",
        "bloom suppressor",
        "set of heatsink fins",
    ],
    "Pistol" : [
        "beam splitter",
        "compensator",
        "bloom suppressor",
        "set of heatsink fins",
    ],
    "Sniper" : [
        "collimator",
        "compensator",
        "bloom suppressor",
    ]
}
beam_spectrum_dict = {
    "Rifle" : [
        "visible-light",
        "ultraviolet",
        "x-ray"
    ],
    "Light Machine Gun" : [
        "ultraviolet",
        "x-ray",
    ],
    "Submachinegun" : [
        "infrared",
        "visible-light",
    ],
    "Carbine" : [
        "infrared",
        "visible-light",
        "ultraviolet",
    ],
    "Pistol" : [
        "infrared",
        "visible-light",
    ],
    "Sniper" : [
        "ultraviolet",
        "x-ray"
    ]
}
beam_mode_dict = {
    "Rifle" : [
        "continuous",
        "pulsed",
    ],
    "Light Machine Gun" : [
       "continuous",
    ],
    "Submachinegun" : [
       "continuous",
    ],
    "Carbine" : [
        "continuous",
        "pulsed",
    ],
    "Pistol" : [
        "continuous",
        "pulsed",
    ],
    "Sniper" : [
        "pulsed",
    ]
}
magazine_loading_dict = {
    "Rifle" : [
        "side",
        "bottom",
        "inside of the stock",
        "inside of a hinge break",
    ],
    "Light Machine Gun" : [
        "bottom",
        "inside of the stock",
    ],
    "Submachinegun" : [
        "side",
        "top",
        "bottom",
        "inside of the stock",
    ],
    "Carbine" : [
        "side",
        "bottom",
        "inside of the stock",
        "inside of a hinge break",
        "top",
    ],
    "Pistol" : [
        "bottom",
        "inside of the stock",
    ],
    "Sniper" : [
        "bottom",
        "inside of the stock",
        "inside of a hinge break"
        ]
}
magazine_shape_dict = {
    "Rifle" : [
        "medium cylinder",
        "medium box",
    ],
    "Light Machine Gun" : [
        "medium cylinder",
        "medium box",
        "heavy cylinder",
        "heavy box",
    ],
    "Submachinegun" : [
        "light cylinder",
        "light box",
        "medium cylinder",
        "medium box",
    ],
    "Carbine" : [
        "light cylinder",
        "light box",
        "medium cylinder",
        "medium box",
        "heavy cylinder",
        "heavy box",
    ],
    "Pistol" : [
        "light cylinder",
        "light box",
        "medium cylinder",
        "medium box",
    ],
    "Sniper" : [
        "medium cylinder",
        "medium box",
        "heavy cylinder",
        "heavy box",
    ]
}
weapon_shape_dict = {
    "Rifle" : [
        "boxy",
        "curvy",
        "slim",
    ],
    "Light Machine Gun" : [
        "boxy",
        "curvy",
        "slim",
    ],
    "Submachinegun" : [
        "boxy",
        "curvy",
        "slim",
    ],
    "Carbine" : [
        "boxy",
        "curvy",
        "slim",
    ],
    "Pistol" : [
        "boxy",
        "curvy",
        "slim",
    ],
    "Sniper" : [
        "boxy",
        "curvy",
        "slim",
    ]
}
top_accessory_dict = {
    "Rifle" : [ 
        "reflex sight",
        "low-magnification optical sight",
        "high-magnification optical sight",
    ],
    "Light Machine Gun" : [
        "low-magnification optical sight",
        "high-magnification optical sight",
    ],
    "Submachinegun" : [
        "iron sight",
        "reflex sight",
        "low-magnification optical sight",
    ],
    "Carbine" : [
        "iron sight",
        "reflex sight",
        "low-magnification optical sight",
        "high-magnification optical sight",
    ],
    "Pistol" : [
        "iron sight",
        "reflex sight",
    ],
    "Sniper" : [
        "high-magnification optical sight",
    ]
}
bottom_accessory_dict = {
    "Rifle" : [ 
        "foregrip",
        "empty rail",
        "tac-light",
    ],
    "Light Machine Gun" : [
        "bipod",
    ],
    "Submachinegun" : [
        "foregrip",
        "empty rail",
        "tac-light",
    ],
    "Carbine" : [
        "foregrip",
        "empty rail",
        "tac-light",
    ],
    "Pistol" : [
        "foregrip",
        "empty rail",
        "tac-light",
    ],
    "Sniper" : [
        "bipod",
    ]
}


def weighted_draw_tag(self, old_weights) -> str:
    # initialize the weights
    # there is probably a better way of doing it (re: spitting tags into catagories) but it's 3AM and brain no work
    # I *really* want to store these in a dictionary but that would mean I wouldn't be able to look the tag back up
    weight_list = ["Rifle", "Light Machine Gun", "Submachinegun", "Carbine", "Pistol", "Sniper"]
    weights = []
    for value in weight_list:
        weights.append([value, 20])
    total_weights = 0

    for i in range(len(old_weights)):
        weights[i][1] += old_weights[i]

    # fuck knows adding up the weights twice is inefficient but how the hell else am I going to know what the total is?!
    for i in range(len(weights)):
        total_weights += weights[i][1]
    target = random.randrange(total_weights)
    randomlot = 0
    for i in range(len(weights)):
        randomlot += weights[i][1]
        if randomlot > target:
            return weights[i][0]


class Laser_Weapon:
    def __init__(self) -> None:
        #initialize
        self.stock = {}
        self.barrel = {}
        self.beam = {}
        self.magazine = {}
        self.attachments = {}
        self.shape = ""

        self.weights = [0, 0, 0, 0, 0, 0] # by varrying this, you can control what gets generated
        # generate magazine 
        value = magazine_loading_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Magazine Loading"][value[index]][i]
        self.magazine["Loading"] = value[index]
        
        value = magazine_shape_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Magazine Shape"][value[index]][i]
        self.magazine["Shape"] = value[index]
        
         # generate beam
        value = beam_spectrum_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Beam Spectrum"][value[index]][i]
        self.beam["Spectrum"] = value[index]
        
        value = beam_mode_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Beam Mode"][value[index]][i]
        self.beam["Mode"] = value[index]

        # generate barrel
        value = barrel_length_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Barrel Length"][value[index]][i]
        self.barrel["Length"] = value[index]

        value = barrel_focus_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Barrel Focus"][value[index]][i]
        self.barrel["Focus"] = value[index]

        value = barrel_accessory_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Barrel Accessory"][value[index]][i]
        self.barrel["Accessory"] = value[index]

        # generate stock
        value = stock_type_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Stock Type"][value[index]][i]
        self.stock["Type"] = value[index]
        
        value = stock_material_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Stock Material"][value[index]][i]
        self.stock["Material"] = value[index]

        value = stock_construction_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Stock Construction"][value[index]][i]
        self.stock["Construction"] = value[index]

        # generate the top and bottom features
        value = top_accessory_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Top Accessory"][value[index]][i]
        self.attachments["Top Accessory"] = value[index]

        value = bottom_accessory_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Bottom Accessory"][value[index]][i]
        self.attachments["Bottom Accessory"] = value[index]

        # the shape of the weapon
        value = weapon_shape_dict[weighted_draw_tag(self, self.weights)]
        index = random.randrange(len(value))
        for i in range(len(self.weights)):
            self.weights[i] += tag_dict["Weapon Shape"][value[index]][i]
        self.shape = value[index]


    def __str__(self) -> str:
        output = "The weapon has a " + self.stock["Type"] + ". "
        output += "The furniture is made of " + self.stock["Material"]
        output += " and is of " + self.stock["Construction"] + " construction."
        output += "\nThe barrel is " + self.barrel["Length"] + " long, is " + self.barrel["Focus"] + " and holds a " + self.barrel["Accessory"] + "."
        output += "\nThe beam is in the " + self.beam["Spectrum"] + " spectrum and is " + self.beam["Mode"] + "-fire."
        output += "\nThe battery loads from the " + self.magazine["Loading"] + " and is a " + self.magazine["Shape"] + " shape and size."
        output += "\nThe top rail holds a " + self.attachments["Top Accessory"]
        output += " and the bottom rail holds a " + self.attachments["Bottom Accessory"] + "."
       
        output += "\nThe weapon's overall shape is " + self.shape + "."

        #determine the most likely category of a weapon
        # *pure* cludge but it works

        weight_list = ["service rifle", "light machine gun", "sub-machinegun", "carbine", "pistol", "sniper rifle"]
        weight_list_removed = weight_list[:]
        weight_list_removed.pop(self.weights.index(max(self.weights)))

        most_likely = max(self.weights)
        weights_removed = self.weights[:]
        weights_removed.pop((self.weights.index(max(self.weights))))
        second_most_likely = max(weights_removed)

        output += "\nThis weapon scores highest as a " + weight_list[self.weights.index(most_likely)] + ", and second-highest as a " + weight_list_removed[weights_removed.index(second_most_likely)] + "."
        
        return output
