# Section 1 - Installation

## Prérequis

- Python 3 et pip (au moins 3.6)
- Google Chrome
- Un terminal

## 1. Préparation

Pour commencer, on va installer tout ce qu'il faut.

Pour utiliser des paquets Python sans écraser l'environnement système, on va utiliser un **virtualenv**.
Un *virtualenv* est une sorte d'installation Python *indépendante*, avec ses propres paquets.

Voici ce qu'il faut taper:

```bash
> pip install virtualenv
```

Ensuite, la création de ce virtualenv:

```bash
> virtualenv -p python3 ./venv
```

Une fois le virtualenv crée, il faut l'activer:

```bash
# Pour Windows, sous Powershell
> ./venv/Scripts/activate.ps1
# Pour Windows, sous cmd
> ./venv/Scripts/activate.bat
# Pour Linux
> source ./venv/bin/activate
```

Une fois dans le virtualenv, le *prompt* de la console va changer avec le texte `(venv)` devant.

```bash
# Exemple avec Powershell
(venv) PS C:\.....> _
```

D'ici, on peut installer les paquets nécessaires:

```bash
> pip install -r requirements.txt
```

## 2. Chromedriver

On va aborder les tests end-to-end lors de ce dojo, et pour ce faire on va utiliser l'outil `selenium` (rapatrié dans les `requirements`).

Selenium va piloter une instance de navigateur via son *webdriver*. Dans le cadre de ce dojo, on va se concentrer sur Google Chrome et sur le `chromedriver`.

Voici un lien vers [chromedriver 2.46](https://chromedriver.storage.googleapis.com/2.46/chromedriver_win32.zip).

Il faut ensuite le décompresser dans un emplacement accessible depuis un terminal (dans le PATH). Pour faire simple, j'ai juste mis le driver dans `C:\Windows\system32`, un peu sale mais fonctionnel.

Pour tester, tapez `chromedriver` depuis cmd ou Powershell, ça devrait fonctionner.

## 3. Documentation

Pour la documentation autour de `pytest`, je recommande:

- le [site officiel](https://docs.pytest.org/en/latest/getting-started.html)
- la doc du module [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
- le livre **TDD with Python**, pour un guide complet autour du testing en Python
- et le livre **Python Testing with pytest**, pour un guide autour de Pytest
