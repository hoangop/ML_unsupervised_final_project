#!/usr/bin/env python3
"""
Advanced script to translate Vietnamese product names to English
Uses deep-translator with multiple translation engines for better accuracy
"""

import pandas as pd
import time
from tqdm import tqdm
from deep_translator import GoogleTranslator, MyMemoryTranslator
import re

def translate_with_fallback(text, max_retries=3):
    """
    Translate text using multiple engines with fallback
    """
    if not text or pd.isna(text):
        return text
    
    # Clean the text
    text = str(text).strip()
    if len(text) < 2:
        return text
    
    # Try Google Translate first
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source='vi', target='en')
            result = translator.translate(text)
            if result and result != text:
                return result
        except Exception as e:
            print(f"Google Translate attempt {attempt + 1} failed: {e}")
            time.sleep(1)
    
    # Fallback to MyMemory
    try:
        translator = MyMemoryTranslator(source='vi', target='en')
        result = translator.translate(text)
        if result and result != text:
            return result
    except Exception as e:
        print(f"MyMemory fallback failed: {e}")
    
    # If all fails, return original text
    return text

def clean_product_name(name):
    """
    Clean and preprocess product name for better translation
    """
    if not name or pd.isna(name):
        return name
    
    # Remove extra whitespace
    name = re.sub(r'\s+', ' ', str(name).strip())
    
    # Remove special characters that might confuse translator
    name = re.sub(r'[\[\]()]', '', name)
    
    return name

def main():
    print("Starting advanced product name translation...")
    print("=" * 60)
    
    # Read the original CSV file
    print("Loading orderdetail.csv...")
    df = pd.read_csv('data/orderdetail.csv')
    
    print(f"Total records: {len(df):,}")
    print(f"Unique products: {df['productname'].nunique():,}")
    
    # Get unique product names
    unique_products = df['productname'].unique()
    print(f"Translating {len(unique_products):,} unique product names...")
    
    # Create translation dictionary
    translation_dict = {}
    
    # Translate unique product names
    for i, product_name in enumerate(tqdm(unique_products, desc="Translating products")):
        try:
            # Clean the product name
            clean_name = clean_product_name(product_name)
            
            # Translate to English
            translated_name = translate_with_fallback(clean_name)
            
            # Store in dictionary
            translation_dict[product_name] = translated_name
            
            # Add delay to avoid rate limiting
            time.sleep(0.2)
            
            # Show progress every 100 products
            if (i + 1) % 100 == 0:
                print(f"Translated {i + 1}/{len(unique_products)} products...")
                
        except Exception as e:
            print(f"Error translating '{product_name}': {e}")
            # Keep original name if translation fails
            translation_dict[product_name] = product_name
    
    print(f"\nTranslation completed for {len(translation_dict):,} products")
    
    # Apply translations to the dataframe
    print("Applying translations to dataset...")
    df['productname_en'] = df['productname'].map(translation_dict)
    
    # Save the translated dataset
    output_file = 'data/orderdetail_en_advanced.csv'
    print(f"Saving translated dataset to {output_file}...")
    df.to_csv(output_file, index=False)
    
    print(f"✅ Advanced translation completed successfully!")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total records: {len(df):,}")
    
    # Show some examples of translations
    print("\n" + "=" * 60)
    print("Sample translations:")
    print("=" * 60)
    
    sample_products = df[['productname', 'productname_en']].drop_duplicates().head(15)
    for _, row in sample_products.iterrows():
        print(f"Vietnamese: {row['productname']}")
        print(f"English:    {row['productname_en']}")
        print("-" * 40)
    
    # Show translation statistics
    print("\n" + "=" * 60)
    print("Translation Statistics:")
    print("=" * 60)
    
    # Count how many products were actually translated
    translated_count = 0
    for original, translated in translation_dict.items():
        if original != translated and translated != original:
            translated_count += 1
    
    print(f"Products successfully translated: {translated_count:,}")
    print(f"Translation success rate: {(translated_count/len(translation_dict)*100):.1f}%")

if __name__ == "__main__":
    main()
