#!/usr/bin/env python3
"""
Simple script to translate Vietnamese product names to English
Uses a manual translation dictionary for common grocery items
"""

import pandas as pd
import re

def create_translation_dictionary():
    """
    Create a manual translation dictionary for common Vietnamese grocery items
    """
    translation_dict = {
        # Fruits
        "Dưa Hấu": "Watermelon",
        "Dưa Hấu Đỏ": "Red Watermelon", 
        "Chuối": "Banana",
        "Táo": "Apple",
        "Cam": "Orange",
        "Nho": "Grape",
        "Xoài": "Mango",
        "Dứa": "Pineapple",
        "Dâu": "Strawberry",
        
        # Vegetables
        "Cà chua": "Tomato",
        "Hành tây": "Onion",
        "Hành lá": "Green Onion",
        "Tỏi": "Garlic",
        "Gừng": "Ginger",
        "Khoai tây": "Potato",
        "Cà rốt": "Carrot",
        "Bắp cải": "Cabbage",
        "Rau muống": "Water Spinach",
        "Rau cải": "Chinese Cabbage",
        "Rau xà lách": "Lettuce",
        "Cà tím": "Eggplant",
        "Ớt": "Chili Pepper",
        "Dưa chuột": "Cucumber",
        "Bí đỏ": "Pumpkin",
        
        # Meat & Protein
        "Thịt heo": "Pork",
        "Thịt bò": "Beef", 
        "Thịt gà": "Chicken",
        "Cá": "Fish",
        "Tôm": "Shrimp",
        "Cua": "Crab",
        "Trứng": "Egg",
        "Mỡ heo": "Pork Fat",
        "Chả": "Vietnamese Sausage",
        "Nem": "Spring Roll",
        "Chả cốm": "Fried Rice Cake",
        
        # Dairy & Eggs
        "Sữa": "Milk",
        "Sữa tươi": "Fresh Milk",
        "Sữa chua": "Yogurt",
        "Phô mai": "Cheese",
        "Bơ": "Butter",
        "Kem": "Ice Cream",
        
        # Grains & Cereals
        "Gạo": "Rice",
        "Bún": "Rice Noodles",
        "Mì": "Noodles",
        "Bánh mì": "Bread",
        "Bánh": "Cake",
        "Cháo": "Porridge",
        "Ngũ cốc": "Cereal",
        
        # Beverages
        "Nước": "Water",
        "Nước ngọt": "Soft Drink",
        "Cà phê": "Coffee",
        "Trà": "Tea",
        "Nước cam": "Orange Juice",
        "Bia": "Beer",
        "Rượu": "Wine",
        
        # Spices & Seasoning
        "Muối": "Salt",
        "Đường": "Sugar",
        "Tiêu": "Pepper",
        "Bột ngọt": "MSG",
        "Nước mắm": "Fish Sauce",
        "Dầu ăn": "Cooking Oil",
        "Tương ớt": "Chili Sauce",
        "Tương cà": "Ketchup",
        
        # Snacks & Sweets
        "Kẹo": "Candy",
        "Bánh kẹo": "Confectionery",
        "Bánh quy": "Cookie",
        "Bánh ngọt": "Sweet Cake",
        "Khoai chiên": "French Fries",
        
        # Household Items
        "Khăn giấy": "Tissue Paper",
        "Xà phòng": "Soap",
        "Dầu gội": "Shampoo",
        "Kem đánh răng": "Toothpaste",
        "Bàn chải": "Toothbrush",
        
        # Common descriptors
        "Đông lạnh": "Frozen",
        "Tươi": "Fresh",
        "Khô": "Dried",
        "Đóng hộp": "Canned",
        "Gói": "Package",
        "Khay": "Tray",
        "Chai": "Bottle",
        "Lon": "Can",
        "Túi": "Bag",
        "Hộp": "Box",
        "Size": "Size",
        "kg": "kg",
        "g": "g",
        "ml": "ml",
        "l": "l",
        
        # Brands (keep as is)
        "CP": "CP",
        "Vĩnh Tân": "Vinh Tan",
        "Muwono": "Muwono",
        "Gấu Đỏ": "Red Bear",
        "Ngon Ngon": "Ngon Ngon",
        
        # Special terms
        "XẢ TỒN": "CLEARANCE",
        "Miền Tây": "Mekong Delta",
        "Baby": "Baby",
        "TQ": "Chinese",
        "Đỏ": "Red",
        "Trắng": "White",
        "Xanh": "Green",
        "Vàng": "Yellow",
        "Nâu": "Brown",
        "Đen": "Black"
    }
    return translation_dict

def translate_product_name(product_name, translation_dict):
    """
    Translate a product name using the dictionary
    """
    translated = product_name
    
    # Try to find matches in the dictionary
    for vietnamese, english in translation_dict.items():
        if vietnamese in product_name:
            translated = translated.replace(vietnamese, english)
    
    return translated

def main():
    print("Starting product name translation...")
    print("=" * 50)
    
    # Read the original CSV file
    print("Loading orderdetail.csv...")
    df = pd.read_csv('data/orderdetail.csv')
    
    print(f"Total records: {len(df):,}")
    print(f"Unique products: {df['productname'].nunique():,}")
    
    # Create translation dictionary
    print("Creating translation dictionary...")
    translation_dict = create_translation_dictionary()
    
    # Apply translations
    print("Translating product names...")
    df['productname_en'] = df['productname'].apply(
        lambda x: translate_product_name(x, translation_dict)
    )
    
    # Save the translated dataset
    output_file = 'data/orderdetail_en.csv'
    print(f"Saving translated dataset to {output_file}...")
    df.to_csv(output_file, index=False)
    
    print(f"✅ Translation completed successfully!")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total records: {len(df):,}")
    
    # Show some examples of translations
    print("\n" + "=" * 50)
    print("Sample translations:")
    print("=" * 50)
    
    sample_products = df[['productname', 'productname_en']].drop_duplicates().head(10)
    for _, row in sample_products.iterrows():
        print(f"Vietnamese: {row['productname']}")
        print(f"English:    {row['productname_en']}")
        print("-" * 30)

if __name__ == "__main__":
    main()
