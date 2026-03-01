#!/usr/bin/env python3
"""
Fast script to copy files to EFI_EnglishTraining folder with translated names
"""

import os
import shutil
from pathlib import Path

# Translation mapping for folder and file names
TRANSLATIONS = {
    'Borradores': 'Drafts',
    'Handbook Diario': 'Daily Handbook',
    'Labs': 'Labs',
    'PowerPoint Presentation': 'PowerPoint Presentation',
    'Quizzes': 'Quizzes',
    'Curso 1 borrador remix.docx': 'Course 1 Draft Remix.docx',
    'Curso 1 borrador.docx': 'Course 1 Draft.docx',
    'Dia 1 - EFI basics.docx': 'Day 1 - EFI Basics.docx',
    'Dia 2 -Power_Ground.docx': 'Day 2 - Power_Ground.docx',
    'Dia 3 - Laptops y conexiones.docx': 'Day 3 - Laptops and Connections.docx',
    'Dia 4 - Tiempos de Inyeccion y Dwell.docx': 'Day 4 - Injection Times and Dwell.docx',
    'Dia 5 - Basic Tuning VE_Spark.docx': 'Day 5 - Basic Tuning VE_Spark.docx',
    'Dia 6 - Cranking and AFR Corrections.docx': 'Day 6 - Cranking and AFR Corrections.docx',
    'Dia 7 - Troubleshooting.docx': 'Day 7 - Troubleshooting.docx',
    'Dia 8 - Final Review.docx': 'Day 8 - Final Review.docx',
    'Handbook Dia 1.docx': 'Handbook Day 1.docx',
    'Handbook Dia 2.docx': 'Handbook Day 2.docx',
    'Handbook Dia 3.docx': 'Handbook Day 3.docx',
    'Handbook Dia 4.docx': 'Handbook Day 4.docx',
    'Handbook Dia 5.docx': 'Handbook Day 5.docx',
    'Handbook Dia 6.docx': 'Handbook Day 6.docx',
    'Prompt for Hnadbooks.docx': 'Prompt for Handbooks.docx',
    'Reporte de Laboratorio 1.xlsx': 'Laboratory Report 1.xlsx',
    'Reporte lab 2.xlsx': 'Laboratory Report 2.xlsx',
    'Dia 1.pptx': 'Day 1.pptx',
    'Dia 3 - LA INTERFAZ DIGITAL Y EL DESPERTAR DE LA ECU.pptx': 'Day 3 - The Digital Interface and the Awakening of the ECU.pptx',
    'DÍA 2 — ALIMENTACIÓN, CONTROL DIGITAL Y RUIDO.pptx': 'Day 2 - Power Supply, Digital Control and Noise.pptx',
    'Lectura 1.xlsx': 'Reading 1.xlsx',
    'Quiz Dia 1.docx': 'Quiz Day 1.docx',
    'Quiz Dia 2.docx': 'Quiz Day 2.docx',
    'Prontuario Clase Piloto.docx': 'Pilot Class Handbook.docx',
}

def get_translated_name(name):
    """Get translated name or return original if not in mapping"""
    return TRANSLATIONS.get(name, name)

def copy_with_translation(source_dir, target_dir):
    """Recursively copy files and folders with translated names"""
    
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Create target directory
    target_path.mkdir(parents=True, exist_ok=True)
    
    for item in source_path.iterdir():
        # Skip git and pycache
        if item.name.startswith('.'):
            continue
        
        # Get translated name
        translated_name = get_translated_name(item.name)
        target_item = target_path / translated_name
        
        if item.is_dir():
            # Recursively copy directory
            copy_with_translation(item, target_item)
        else:
            # Copy file
            target_item.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target_item)
            print(f"✓ {item.name} → {translated_name}")

def main():
    source = '/workspaces/EFI_Traning'
    target = '/workspaces/EFI_EnglishTraining'
    
    print("Copying and translating files...")
    print(f"Source: {source}")
    print(f"Target: {target}\n")
    
    # Remove existing target directory if it exists
    if Path(target).exists():
        shutil.rmtree(target)
    
    copy_with_translation(source, target)
    
    print(f"\n✓ All files copied to {target}")
    print("Note: File names have been translated. File contents remain in original language.")

if __name__ == '__main__':
    main()
