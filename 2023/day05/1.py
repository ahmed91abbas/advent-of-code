with open("data.in") as f:
    lines = f.read()

(
    seeds_txt,
    seed_to_soil_txt,
    soil_to_ferti_text,
    ferti_to_water_txt,
    water_to_light_txt,
    light_to_temp_txt,
    temp_to_humid_txt,
    humid_to_loc_txt,
) = lines.split("\n\n")


def parse_map(txt):
    return [[int(x) for x in line.split(" ")] for line in txt.split("\n")[1:]]


def get_dest(src, ranges):
    for dest_range, src_range, range_diff in ranges:
        if src in range(src_range, src_range + range_diff):
            return dest_range + (src - src_range)
    return src


seeds = [int(x) for x in seeds_txt.split(" ") if x.isdigit()]
seed_to_soil = parse_map(seed_to_soil_txt)
soil_to_ferti = parse_map(soil_to_ferti_text)
ferti_to_water = parse_map(ferti_to_water_txt)
water_to_light = parse_map(water_to_light_txt)
light_to_temp = parse_map(light_to_temp_txt)
temp_to_humid = parse_map(temp_to_humid_txt)
humid_to_loc = parse_map(humid_to_loc_txt.strip())

locations = []
for seed in seeds:
    soil = get_dest(seed, seed_to_soil)
    ferti = get_dest(soil, soil_to_ferti)
    water = get_dest(ferti, ferti_to_water)
    light = get_dest(water, water_to_light)
    temp = get_dest(light, light_to_temp)
    humid = get_dest(temp, temp_to_humid)
    loc = get_dest(humid, humid_to_loc)
    locations.append(loc)

print(min(locations))
