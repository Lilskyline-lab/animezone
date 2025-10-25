#!/usr/bin/env python3
"""
Script pour mettre à jour les imports dans les fichiers Python après réorganisation
Ce script modifie les imports pour pointer vers la nouvelle structure de dossiers
"""

import os
import re
import sys
from pathlib import Path

def update_imports_in_file(file_path):
    """
    Met à jour les imports dans un fichier Python
    
    Args:
        file_path: Chemin du fichier à mettre à jour
    """
    print(f"Traitement de {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mettre à jour les imports
    # Exemple: from app import xyz -> from src.core.app import xyz
    content = re.sub(r'from\s+app\s+import', 'from src.core.app import', content)
    content = re.sub(r'import\s+app\s+', 'import src.core.app as app ', content)
    
    # Mettre à jour d'autres imports si nécessaire
    content = re.sub(r'from\s+web_scraper\s+import', 'from src.core.web_scraper import', content)
    content = re.sub(r'import\s+web_scraper\s+', 'import src.core.web_scraper as web_scraper ', content)
    
    # Mise à jour des imports API
    content = re.sub(r'from\s+API\.', 'from src.api.', content)
    content = re.sub(r'import\s+API\.', 'import src.api.', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Imports mis à jour dans {file_path}")

def update_all_imports(directory):
    """
    Met à jour les imports dans tous les fichiers Python d'un répertoire
    
    Args:
        directory: Répertoire à traiter
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                update_imports_in_file(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "src"
    
    update_all_imports(directory)
    print(f"Tous les imports dans {directory} ont été mis à jour")