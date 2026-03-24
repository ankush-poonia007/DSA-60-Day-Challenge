import os

# Exact mapping based on your provided image list
image_map = {
    1: "Day01_19Feb(1).png", 2: "Day02_20Feb (2).png", 3: "Day03_21Feb(2).png",
    4: "Day04_22Feb(2).png", 5: "Day05_23Feb (2).png", 6: "Day06_24Feb (2).png",
    7: "Day07_25Feb (3).png", 8: "Day08_26Feb (2).png", 9: "Day09_27Feb (2).png",
    10: "Day10_28Feb (2).png", 11: "Day11_01March (2).png", 12: "Day12_02March (2).png",
    13: "Day13_03March (2).png", 14: "Day14_04March (2).png", 15: "Day15_05March (2).png",
    16: "Day16_06March (2).png", 17: "Day17_07March (2).png", 18: "Day18_08March (2).png",
    19: "Day19_09March (2).png", 20: "Day20_10March (2).png", 21: "Day21_11March.png",
    22: "Day22_12March.png", 23: "Day23_13March.png", 24: "Day24_14March.png",
    25: "Day25_15March.png", 26: "Day26_16March.png", 27: "Day27_17March.png",
    28: "Day28_18March.png", 29: "Day29_19March.png", 30: "Day30_20March.png",
    31: "Day31_21March.png", 32: "Day32_22March.png", 33: "Day33_23March.png",
    34: "Day34_24March.png"
}

for day, img_name in image_map.items():
    folder_name = f"Day-{day:02d}"
    md_path = os.path.join(folder_name, "README.md")
    
    if os.path.exists(md_path):
        # Using a relative path to the assets folder
        verification_text = (
            f"\n\n---\n"
            f"## ✅ Verification\n"
            f"![Test Case Result](../assets/{img_name})\n"
            f"*Passed all test cases on GeeksforGeeks.*"
        )
        
        # Open in append mode to add to the existing README content
        with open(md_path, "a", encoding="utf-8") as f:
            f.write(verification_text)
        print(f"Success: Linked {img_name} to {folder_name}")
    else:
        print(f"Skipped: {folder_name} not found.")

print("\nAll 34 daily READMEs are now verified with screenshots!")