# Section 2 - Les types de tests

Avant de commencer à tester, on va voir différents types de tests (plus d'infos sur [le wiki](https://sharingcloud.atlassian.net/wiki/spaces/SKB/pages/859439125/1.3.+Tests+et+couverture)).

## 1. Tests unitaires

Les tests unitaires se chargent de vérifier le comportement d'une fonctionnalité à la fois, en essayant de tester chaque branche du code. Ils sont censés être concis et exhaustifs, en restant limités en scope.

Ce sont les tests les plus simples à écrire: puisque le scope est par définition limité, il n'y a pas de dépendance forte avec le reste du code.

```python
def test_simple():
  assert "a" * 5 == "aaaaa"
```

## 2. Tests d'intégration

Les tests d'intégration se chargent de vérifier les communications entre plusieurs modules du code et voir si tout tourne bien ensemble. Ils sont plus longs mais plus pertinents car on peut décrire des cas d'utilisation.

Ils sont plus complexes à rédiger: en fonction des cas, il peut être nécessaire de préparer une "situation" de test en amont, en utilisant plus de code que nécessaire pour le test en lui même. Par exemple, sur un test portant sur la *création d'une réservation*, il faut au préalable: **un cloud, un utilisateur, une ressource, et une adresse**. Heureusement, avec pytest il est assez simple d'écrire très peu de code pour ne se concentrer que sur le test à l'aide d'un outil très utile: *les fixtures*.

```python
def test_integration(dependency1, dependency2):
  result = dependency1.execute(dependency2.value)
  assert result == "some_value"
```

## 3. Tests end-to-end

Les tests end-to-end vérifient le comportement d'une application dans sa globalité, en mode boîte noire. Le plus souvent, on passe par des outils comme `selenium` qui nous apporte une API autour d'un navigateur, pour exécuter des actions comme appuyer sur un bouton, récupérer un élément du DOM et vérifier des comportements. Ce sont les plus longs et les plus compliqués à écrire, mais ça permet de faire des tests qui se rapprochent du comportement d'un utilisateur en face de son appareil.

Ces tests ne remplacent pas tous les tests fonctionnels réalisés "à la main", mais ils peuvent être très utiles pour automatiser certaines tâches répétitives.

```python
def test_e2e(browser):
  browser.navigate_to("/toto")  
  assert browser.check_url("/toto")

  element = browser.find_element_by_css_selector("#my-elem")
  assert element.value == "my-value"
``` 
