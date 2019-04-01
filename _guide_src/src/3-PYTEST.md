# Section 3 - L'outil Pytest

Pour ceux qui connaissent déja le module `unittest` fourni de base avec Python, vous vous demandez sûrement pourquoi `pytest` et pas `unittest` ?

C'est ce qu'on va voir tout de suite, et on peut commencer par l'article de Sam & Max: [http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-3/](http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-3/).

On va travailler dans le dossier `examples/simple`.

## 1. Ecrire un test

Pour écrire un test, il suffit de créer un fichier qui commence par "`test_`" dans le dossier "`tests`": par exemple, "`test_me.py`".

Dans ce fichier, les fonctions commençant par "`test_`" seront exécutées en tant que cas de test.

Dans `unittest`, il y a plusieurs façons de faire des assertions:

- `self.assertTrue`
- `self.assertFalse`
- `self.assertEqual`
- `self.assertNotEqual`
- `self.assertIs`
- `self.assertIsNot`
- ...

C'est un style populaire pour réaliser des assertions, car il permet à première vue de tester énormément de choses (et permet d'avoir plus d'infos quand le test échoue).
Pytest lui n'a qu'une fonction d'assertion:

- `assert`

Là comme ça, ça a l'air un peu limité, mais avec `assert` on peut tester n'importe quoi, il suffit de lui passer une expression booléenne.

*Exemple de fonction de test:*

```python
def test_reverse():
  assert "azerty"[::-1] == "ytreza"
```

*Un autre test:*

```python
def ma_fonction(a):
  return a * a
  
def test_ma_fonction():
  assert ma_fonction(1) == 1
  assert ma_fonction(5) == 25
```

*Exemple d'exécution de pytest:*

```text
(venv) PS C:\Users\...\simple> pytest
=============================================== test session starts ====================================================
platform win32 -- Python 3.7.1, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- c:\users\...\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\...\simple, inifile: pytest.ini
plugins: pythonpath-0.7.3, django-3.4.8, cov-2.6.1
collected 1 item

tests/test_simple.py::test_simple PASSED                                                                          [100%]

=============================================== 1 passed in 0.03 seconds ===============================================
(venv) PS C:\Users\...\simple>
```

## 2. La gestion des erreurs

Là où `unittest` utilise des fonctions précises pour avoir de bons retours d'erreurs, on pourrait croire que pytest est moins bon avec son `assert` unique.
Mais non:

```
(venv) PS C:\Users\...\simple> pytest tests/test_simple.py::test_error
========================================================== test session starts ==========================================================
platform win32 -- Python 3.7.1, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- c:\users\...\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\...\simple, inifile: pytest.ini
plugins: pythonpath-0.7.3, django-3.4.8, cov-2.6.1
collected 2 items
run-last-failure: rerun previous 1 failure first

tests/test_simple.py::test_error FAILED                                                                                            [ 50%]

=============================================================== FAILURES ================================================================
______________________________________________________________ test_error _______________________________________________________________

    def test_error():
>       assert {"a": 1, "b": 5} == {"a": 2}
E       AssertionError: assert {'a': 1, 'b': 5} == {'a': 2}
E         Differing items:
E         {'a': 1} != {'a': 2}
E         Left contains more items:
E         {'b': 5}
E         Full diff:
E         - {'a': 1, 'b': 5}
E         + {'a': 2}


tests\test_simple.py:9: AssertionError
======================================================= 1 failed in 0.09 seconds ========================================================
(venv) PS C:\Users\...\simple>
```

Pytest nous explique directement ce qui ne va pas.
Il permet même de nous montrer l'état des variables de la fonction:

```
(venv) PS C:\Users\...\simple> pytest tests/test_simple.py::test_variables_error
========================================================== test session starts ==========================================================
platform win32 -- Python 3.7.1, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- c:\users\...\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\...\simple, inifile: pytest.ini
plugins: pythonpath-0.7.3, django-3.4.8, cov-2.6.1
collected 1 item

tests/test_simple.py::test_variables_error FAILED                                                                                  [100%]

=============================================================== FAILURES ================================================================
_________________________________________________________ test_variables_error __________________________________________________________

    def test_variables_error():
        a = 1
        b = 1
        result = 3

>       assert a + b == result
E       assert 2 == 3
E         -2
E         +3

a          = 1
b          = 1
result     = 3

tests\test_simple.py:17: AssertionError
======================================================= 1 failed in 0.09 seconds ========================================================
```

C'est quand même super pratique !

## 3. Les fixtures

### a. C'est quoi ?

Sur des tests simples, il n'y a pas grand chose à écrire, du coup c'est concis et rapide.
Sur des cas plus complexes, on peut avoir besoin de créer énormément de choses au préalable (surtout côté tests d'intégration).

Pour limiter le code nécessaire à la création des scénarios, pytest propose une fonctionnalité super utile: les `fixtures`.

Ceux qui connaissent déja un peu le monde du testing savent déjà ce qu'est une fixture côté base de données: ce sont des données à charger en DB avant l'exécution des tests.
Dans le cas de pytest, les fixtures sont différentes. Ce ne sont pas nécessairement des "données", et ce n'est pas nécessairement placé en base de données.  

Via les fixtures, on peut par exemple:

- automatiser la désactivation du SMTP pour empêcher l'envoi de mail dans chaque fonction,
- monkeypatcher certaines fonctions avant de démarrer un test,
- automatiser la création d'un cloud avant chaque test,
- créer un navigateur via selenium avant de commencer un test e2e,
- préparer un environnement où l'on crée une resource et un utilisateur pour pouvoir faire des réservations,
- on peut faire n'importe quoi finalement.

Voici comment on déclare et appelle une fixture:

```python
import pytest

@pytest.fixture
def ma_fixture():
  return {
    "a": 5,
    "b": 6
  }
  
def test_ma_fixture(ma_fixture):
  assert ma_fixture == {"a": 5, "b": 6}
```

### b. Ça va où ?

Ces fixtures sont stockées à plusieurs endroits possibles:

- dans un ou plusieurs fichiers `conftest.py` (un fichier possible par path)
- directement dans un module de test `test_*.py`

En fonction de la position d'un module de test, les fixtures seront chargés au fil du parcours de l'arborescence pour aller jusqu'a ce test.

Exemple:

- tests/
  - a/
    - conftest.py
    - b/
      - conftest.py
      - test_toto.py
  - b/
    - test_tutu.py
  - conftest.py
  
Sur cet exemple:

- le module `test_toto.py` va charger les fixtures des fichiers `conftest.py` de
  - `tests/`,
  - `tests/a/`,
  - `tests/a/b/`,
- alors que le module `test_tutu.py` va charger les fixtures des fichiers `conftest.py` de:
  - `tests/`, c'est tout.

### c. Les scopes

Les fixtures peuvent avoir plusieurs "scopes".

- Le scope `session`: la fixture va s'exécuter une seule fois avant toute la session de test
  - C'est utile pour les tâches qui prennent du temps, comme créer la DB avec mise en place des migrations
  - Ou encore démarrage d'un serveur en arrière plan pour les tests e2e
- Le scope `module`: pour un module (un fichier python), la fixture ne va s'exécuter qu'une seule fois par module.
  - C'est utile lorsque plusieurs tests nécessitent le même environnement au préalable: comme la création d'un cloud et d'une ressource pour faire plusieurs tests.
- Le scope `class`: moins utilisé sur `pytest`, mais si vous voulez utiliser des classes comme avec `unittest`, ça revient à déclarer une fonction `tearDown` et `setUp` dans la classe.
  - En pratique on n'aura pas besoin de s'en servir, les 3 autres scopes sont plus flexibles.
- Le scope `function`: c'est le scope par défaut, la fixture s'exécute avant le démarrage d'une fonction en particulier

Voici des exemples:

```python
# Exemples

@pytest.fixture(scope="session")
def session_fixture():
  return {
    "session_key": 1234
  }
 
@pytest.fixture(scope="module")
def module_fixture():
  return {
    "module_key": 7890
  }
  
@pytest.fixture
def function_fixture():
  return {
    "function_key": 1902
  }
  
def test_fix1(session_fixture, module_fixture, function_fixture):
  # session_fixture va se créer
  # module_fixture va se créer
  # function_fixture va se créer
  pass
  
def test_fix2():
  # session_fixture existe déja
  # module_fixture existe déja
  # function_fixture va se créer
  pass
```

### d. Setup & Teardown

Maintenant que vous savez comment construire une fixture (à la `setUp` côté `unittest`), vous vous demandez sûrement comment gérer sa destruction (`tearDown`) ?

Avec une fixture classique, on ne peut que gérer la vie de la donnée avant qu'elle ne soit passée dans le test, mais pas après. Pour cela, il faut utiliser une fixture appelée `yield`, du nom du mot-clé Python qui permet de créer des générateurs (et des coroutines).

Je vais pas trop rentrer dans le détail, mais c'est le même principe que pour un `context manager` (bloc `with`):

```python
from contextlib import contextmanager

@contextmanager
def mon_bloc():
  # On déclare une variable
  ma_var = 5
  print("avant bloc")
  
  # On "envoie" la variable à l'extérieur du générateur
  yield ma_var
  
  print("après bloc")
  
def ma_fonction():
  # On appelle le context manager
  with mon_bloc() as var:
    # affiche "avant bloc"
    print(var)
    # affiche 5
  # affiche "après bloc"
```

On va utiliser le même système pour la fixture:

```python
import pytest

@pytest.yield_fixture
def ma_fixture():
  # On déclare une variable
  ma_var = "toto"
  
  # On "envoie" la variable à l'extérieur du générateur
  yield ma_var
  
  # On peut faire une action post-fixture, comme supprimer des entrées DB
  db.clear()
  
def test_fixture(ma_fixture):
  assert ma_fixture == "toto"
  # à la fin du test, va supprimer les entrées DB
```

**Attention:** La notation `@pytest.yield_fixture` est dépréciée: le décorateur `fixture` comprend désormais l'instruction `yield`. Il est donc préférable de directement utiliser `@pytest.fixture`. J'ai ici utilisé `@pytest.yield_fixture` pour montrer le rapport.

### e. L'héritage

Il est possible de mettre en place des dépendances entre les fixtures.
Par contre, attention aux scopes:

- Il n'est pas possible pour une fixture de dépendre d'un scope plus petit
  - C'est à dire qu'un scope "session" ne peut pas dépendre d'un scope "function".
  - Mais le contraire oui.

Voici un exemple:

```python
@pytest.fixture(scope="session")
def mon_cloud():
  return Cloud()
  
@pytest.fixture
def mon_user(mon_cloud):
  return User(cloud=mon_cloud)
  
def test_fix(mon_user):
  # mon_user va automatiquement utiliser mon_cloud
  pass
  
def test_fix2(mon_user, mon_cloud):
  # mon_cloud existe déja dans mon_user, ici on récupère juste une référence
  assert mon_user.cloud == mon_cloud
```

Voici un exemple qui ne marche pas:

```python
@pytest.fixture
def mon_cloud():
  return Cloud()
  
@pytest.fixture(scope="session")
def mon_user(mon_cloud):
  # ça va casser, mon_cloud étant d'un scope plus petit
  pass
```

### f. Bonus

Petite commande bonus: on peut afficher les étapes de "setup" et de "teardown" des fixtures lors de l'exécution des tests.

Attention c'est un peu verbeux:

```
(venv) PS C:\Users\...\simple> pytest --setup-show
=============================================== test session starts ================================================
platform win32 -- Python 3.7.1, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- c:\users\...\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\...\simple, inifile: pytest.ini
plugins: pythonpath-0.7.3, django-3.4.8, cov-2.6.1
collected 2 items

tests/test_scopes.py::test_fix1
SETUP    S _fail_for_invalid_template_variable
SETUP    S django_test_environment
SETUP    S session_fixture
SETUP    S django_db_blocker
    SETUP    M module_fixture
      SETUP    C _django_setup_unittest (fixtures used: django_db_blocker)
        SETUP    F _dj_autoclear_mailbox
        SETUP    F _django_clear_site_cache
        SETUP    F _django_db_marker
        SETUP    F _django_set_urlconf
        SETUP    F _live_server_helper
        SETUP    F _template_string_if_invalid_marker
        SETUP    F function_fixture
        tests/test_scopes.py::test_fix1 (fixtures used: _dj_autoclear_mailbox, _django_clear_site_cache, _django_db_marker, _django_set_urlconf, _django_setup_unittest, _fail_for_invalid_template_variable, _live_server_helper, _template_string_if_invalid_marker, django_db_blocker, django_test_environment, function_fixture, module_fixture, session_fixture)PASSED
        TEARDOWN F function_fixture
        TEARDOWN F _template_string_if_invalid_marker
        TEARDOWN F _live_server_helper
        TEARDOWN F _django_set_urlconf
        TEARDOWN F _django_db_marker
        TEARDOWN F _django_clear_site_cache
        TEARDOWN F _dj_autoclear_mailbox
      TEARDOWN C _django_setup_unittest
tests/test_scopes.py::test_fix2
      SETUP    C _django_setup_unittest (fixtures used: django_db_blocker)
        SETUP    F _dj_autoclear_mailbox
        SETUP    F _django_clear_site_cache
        SETUP    F _django_db_marker
        SETUP    F _django_set_urlconf
        SETUP    F _live_server_helper
        SETUP    F _template_string_if_invalid_marker
        tests/test_scopes.py::test_fix2 (fixtures used: _dj_autoclear_mailbox, _django_clear_site_cache, _django_db_marker, _django_set_urlconf, _django_setup_unittest, _fail_for_invalid_template_variable, _live_server_helper, _template_string_if_invalid_marker, django_db_blocker, django_test_environment)PASSED
        TEARDOWN F _template_string_if_invalid_marker
        TEARDOWN F _live_server_helper
        TEARDOWN F _django_set_urlconf
        TEARDOWN F _django_db_marker
        TEARDOWN F _django_clear_site_cache
        TEARDOWN F _dj_autoclear_mailbox
      TEARDOWN C _django_setup_unittest
    TEARDOWN M module_fixture
TEARDOWN S django_db_blocker
TEARDOWN S django_test_environment
TEARDOWN S _fail_for_invalid_template_variable
TEARDOWN S session_fixture

============================================= 2 passed in 0.12 seconds =============================================
(venv) PS C:\Users\...\simple>
```

On discerne bien toutes les fixtures utilisées, avec les scopes (S pour `session`, M pour `module`, C pour `class` et F pour `function`).
