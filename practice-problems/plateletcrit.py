#Normal range for platelets is typically between 150,000 to 450,000 per microlite
#Plateletcrit (PCT): This is a measure of the volume occupied by platelets in the blood as a percentage.
#It is calculated using the formula:
#The normal range for PCT is 0.22% to 0.24%.
#PCT=platelet count×mean platelet volume (MPV)/10,000
while True:
    try:
        platelet_count = float(input("Platelet count(pL): "))
        mpv = float(input("MPV(fL): "))
        k = 10000
        pct = ((platelet_count*mpv)/k)/1000
        remarks = f"PCT value {pct:.2f}% is normal" if 0.22 <= pct <= 0.36 else f"PCT value {pct:.2f}% is not normal"
        print(remarks)
        print()
        
    except ValueError:
        print("Invalid input!")
        continue
 


