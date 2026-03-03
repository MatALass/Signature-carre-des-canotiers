# Compatibilité (HTML email)

## Principes utilisés
- Layout en **tables**
- CSS **inline uniquement**
- Pas de flexbox / grid / position:fixed
- Images avec `display:block`

## Clients
### Gmail (web)
✅ Très bon rendu.  
⚠️ Gmail peut supprimer certains attributs inutiles mais garde bien les tables.

### Gmail (mobile)
✅ Généralement OK.  
⚠️ Attention aux tailles : privilégier logo 56–96px.

### Apple Mail (macOS / iOS)
✅ Excellent.

### Outlook Desktop (Windows)
⚠️ Le moteur Word est limité :
- certains styles CSS sont ignorés
- les marges/paddings peuvent varier
✅ Les tables + inline CSS restent la base la plus stable.

## Recommandations
- Toujours tester sur 2 signatures : full et compact.
- Eviter les images trop lourdes (>50KB par icône).
- Héberger les images sur HTTPS stable (GitHub Pages recommandé).