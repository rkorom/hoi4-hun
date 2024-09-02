# Közreműködés

A közreműködés során kérjük, hogy tartsd be az alábbi [irányelveket](CODE_OF_CONDUCT.md), hogy a fordítás minősége megfelelő legyen.

## Teendők listája

A hiányzó szövegeket a [todo.csv](todo.csv) fájlban találod az alábbi formátumban:

| Fájlnév               | Kulcs                         |
| --------------------- | ----------------------------- |
| aat_bop_l_english.yml | SWE_riksdag_political_balance |

A fenti példában a(z) `aat_bop_l_english.yml` a fájl neve, a(z) `SWE_riksdag_political_balance` pedig a kulcs, amelynek a fordítása hiányzik.

## Forrásfájlok

A fordítási fájlokat a [src/content/localisation/replace](src/content/localisation/replace) mappában találod.
A fájlok a `yml` kiterjesztésűek, amelyek YAML formátumban vannak írva.

Például:

```yaml
autonomy_occupation_zone:0 "Occupation Zone"
```

Ebben az esetben a `autonomy_occupation_zone` a kulcs, amelynek a fordítása a `Megszállási zóna`. Ezért a fájl tartalma a következő lesz:

```yaml
autonomy_occupation_zone:0 "Megszállási zóna"
```

## Projekt struktúra

1. __`.github/` mappa__: A GitHub-specifikus beállítások, mint például a workflow-k (GitHub Actions), a hozzájárulási útmutatók, és egyéb GitHub-specifikus fájlok tárolása.
2. __`.vscode/` mappa__:  A Visual Studio Code-specifikus beállítások tárolása.
3. __`scripts/`__ mappa: Különböző segédszkriptek, például formázási és fordítási szkriptek tárolása. Ez a mappa lehetővé teszi a fejlesztéshez szükséges segédeszközök elkülönítését.
4. __`src/` mappa__: A projekt forrásfájljainak tárolása, ebben az esetben a mod tartalmai, mint a `content`, valamint a modhoz szükséges egyéb fájlok, mint a `descriptor.mod`, `metadata.vdf`, és a `preview.jpg`.
5. __Projekt gyökérmappája__:  Itt találhatók a globális konfigurációs fájlok, licenc, README, és más dokumentációs fájlok.

## Hasznos linkek

- __Hivatalos dokumentáció a fordításról: [Paradox Interactive - Localisation](https://hoi4.paradoxwikis.com/Localisation)__