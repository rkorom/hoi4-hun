# HOI4 magyarosítás

Mint tudjuk, a Paradox Magyarország készített egy fordítást a játékhoz, amely 2020 óta nem került frissítésre.
Azóta számos próbálkozás történt a magyarosítás megvalósítására, de egyik sem érte el a kívánt minőséget, ezért úgy döntöttem, hogy elkezdem a magyarosítást open-source formában. Ennek köszönhetően bárki hozzájárulhat a fejlesztéshez, szemben az összes eddigi próbálkozással.

## Telepítés

Iratkozz fel a modra [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3281592737)-on keresztül, majd állítsd be a játék nyelvének az angolt. A magyarosítás automatikusan kicseréli az angol szövegeket magyarra.

Amennyiben a játékot nem a Steamen keresztül vásároltad meg, úgy a(z) [src/content](src/content) mappában található fájlokat kell a játék mappájába másolnod kézileg. Fontos, hogy ebben az esetben a mod nem fog automatikusan frissülni, így neked kell gondoskodnod a fordítások rendszeres frissítéséről.

## Közreműködők

[![Contributors](.github/assets/contributors.svg)](https://github.com/rkorom/hoi4-hun/graphs/contributors)

 
## Segítenél a fordításban?

Ha észrevételeid vannak, vagy hibát találtál a fordításban, jelezd nekünk vagy forkold a repót és küldj egy pull requestet!
Amennyiben elakadtál, vagy kérdésed van, vedd fel velem a kapcsolatot [Discordon](https://discord.gg/NcptrNxQAp) vagy [Steamen](https://steamcommunity.com/id/krm88/) keresztül.

### Hogyan kezdj neki?

A hiányzó szövegeket a [todo.csv](todo.csv) fájlban találod az alábbi formátumban:

| Fájlnév               | Kulcs                         |
| --------------------- | ----------------------------- |
| aat_bop_l_english.yml | SWE_riksdag_political_balance |

A fenit példában a(z) `aat_bop_l_english.yml` a fájl neve, a(z) `SWE_riksdag_political_balance` pedig a kulcs, amelynek a fordítása hiányzik.

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

__Hivatalos dokumentáció a fordításról: [Paradox Interactive - Localisation](https://hoi4.paradoxwikis.com/Localisation)__

### Projekt struktúra

1. __`.github/` mappa__: A GitHub-specifikus beállítások, mint például a workflow-k (GitHub Actions), a hozzájárulási útmutatók, és egyéb GitHub-specifikus fájlok tárolása.
2. __`.vscode/` mappa__:  A Visual Studio Code-specifikus beállítások tárolása.
3. __`scripts/`__ mappa: Különböző segédszkriptek, például formázási és fordítási szkriptek tárolása. Ez a mappa lehetővé teszi a fejlesztéshez szükséges segédeszközök elkülönítését.
4. __`src/` mappa__: A projekt forrásfájljainak tárolása, ebben az esetben a mod tartalmai, mint a `content`, valamint a modhoz szükséges egyéb fájlok, mint a `descriptor.mod`, `metadata.vdf`, és a `preview.jpg`.
5. __Projekt gyökérmappája__:  Itt találhatók a globális konfigurációs fájlok, licenc, README, és más dokumentációs fájlok.