
"""
Point d'entrée principal 
Configuration pour le développement local et Replit
"""

import os
from app import app as application

# Exposer app
app = application

if __name__ == "__main__":
    # Configuration de développement
    debug_mode = True if os.environ.get('ENV') == 'development' else False
    port = int(os.environ.get('PORT', 8080))
    
    # Forcer l'utilisation de 0.0.0.0 pour la compatibilité
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
