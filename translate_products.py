#!/usr/bin/env python3
"""
Script to translate Vietnamese product names to English
Reads orderdetail.csv and creates orderdetail_en.csv with translated product names
"""

import pandas as pd
import re
from googletrans import Translator
import time
from tqdm import tqdm

def translate_vietnamese_to_english(text):
    """
    Translate Vietnamese text to English using Google Translate
    """
    try:
        translator = Translator()
        result = translator.translate(text, src='vi', dest='en')
        return result.text
    except Exception as e:
        print(f"Translation error for '{text}': {e}")
        return text  # Return original text if translation fails

def clean_product_name(name):
    """
    Clean product name by removing special characters and extra spaces
    """
    # Remove extra whitespace
    name = re.sub(r'\s+', ' ', name.strip())
    return name

def main():
    print("Starting product name translation...")
    print("=" * 50)
    
    # Read the original CSV file
    print("Loading orderdetail.csv...")
    df = pd.read_csv('data/orderdetail.csv')
    
    print(f"Total records: {len(df):,}")
    print(f"Unique products: {df['productname'].nunique():,}")
    
    # Get unique product names for translation
    unique_products = df['productname'].unique()
    print(f"Translating {len(unique_products):,} unique product names...")
    
    # Create translation dictionary
    translation_dict = {}
    
    # Translate unique product names
    translator = Translator()
    
    for i, product_name in enumerate(tqdm(unique_products, desc="Translating products")):
        try:
            # Clean the product name
            clean_name = clean_product_name(product_name)
            
            # Translate to English
            result = translator.translate(clean_name, src='vi', dest='en')
            translated_name = result.text
            
            # Store in dictionary
            translation_dict[product_name] = translated_name
            
            # Add small delay to avoid rate limiting
            time.sleep(0.1)
            
        except Exception as e:
            print(f"Error translating '{product_name}': {e}")
            # Keep original name if translation fails
            translation_dict[product_name] = product_name
    
    print(f"\nTranslation completed for {len(translation_dict):,} products")
    
    # Apply translations to the dataframe
    print("Applying translations to dataset...")
    df['productname_en'] = df['productname'].map(translation_dict)
    
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
