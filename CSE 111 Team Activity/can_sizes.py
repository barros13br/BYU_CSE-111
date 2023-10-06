""""Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. """

#Import math here
import math
# here is the main function.
def main():
    storage_1_picnic = compute_storage_efficiency(6.83, 10.16)
    storage_1_tall = compute_storage_efficiency(7.78, 11.91)
    storage_2 = compute_storage_efficiency(8.73, 11.59)
    storage_2_5 = compute_storage_efficiency(10.32, 11.91)
    storage_3_cylinder = compute_storage_efficiency(10.79, 17.78)
    storage_5 = compute_storage_efficiency(13.02, 14.29)
    storage_6z = compute_storage_efficiency(5.40, 8.89)
    storage_8z_short = compute_storage_efficiency(6.83, 7.62)
    storage_10 = compute_storage_efficiency(15.72, 17.78)
    storage_211 = compute_storage_efficiency(6.83, 12.38)
    storage_300 = compute_storage_efficiency(7.62, 11.27)
    storage_303 = compute_storage_efficiency(8.10, 11.11)

    #here is the print space
    print()
    print(f"#1 Picnic {storage_1_picnic:.2f}")
    print(f"#1 Tall {storage_1_tall:.2f}")
    print(f"#2 {storage_2:.2f}")
    print(f"#2.5 {storage_2_5:.2f}")
    print(f"#3 Cylinder {storage_3_cylinder:.2f}")
    print(f"#5 {storage_5:.2f}")
    print(f"#6Z {storage_6z:.2f}")
    print(f"#8Z short {storage_8z_short:.2f}")
    print(f"#10 {storage_10:.2f}")
    print(f"#211 {storage_211:.2f}")
    print(f"#300 {storage_300:.2f}")
    print(f"#303 {storage_303:.2f}")
    print()

#this is the function that calculates the surface area
def compute_surface_area(radius, height):
    surface_math = 2 * math.pi * radius * (radius + height)
    return surface_math

#this is the function that calculates the volume
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

#this is the function that calculates the vstorage efficiency
def compute_storage_efficiency(radius, height):
    valor_volume = compute_volume(radius, height)
    valor_surface = compute_surface_area(radius, height)

    storage = valor_volume / valor_surface
    return storage

#here is the main function that display all the program.
main()