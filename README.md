# Signature email — Carré des Canotiers

Signature email standardisée (HTML email-safe + version texte) pour les membres du **Carré des Canotiers**.

Variantes : **Full** / **Compact** / **Texte**  
Compatible : Gmail, Apple Mail, Outlook (avec limites connues)  
Assets versionnés + page de preview + générateur (config → dist)

---

## Contenu

- `templates/` : sources avec placeholders `{{...}}`
- `dist/` : signatures prêtes à copier-coller (générées)
- `assets/` : logo + icônes (remplacer les placeholders)
- `docs/` : preview + compatibilité
- `tools/` : config + script de build

---

## Quick start

### 1) Personnaliser la config
Copie/édite :

- `tools/config.example.json` → `tools/config.json`

### 2) Générer `dist/`
```bash
python tools/build.py --config tools/config.json