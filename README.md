# HOI4 magyarosítás

[Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3281592737)

Mint tudjuk, a Paradox Magyarország készített egy fordítást a játékhoz, amely már évek óta nem került frissítésre. Ennek a hiánynak a betöltésére szerettük volna folytatni a játék magyar nyelvre történő fordítását. A fordítás tartalmazza a játék összes szövegét, beleértve a DLC-két is.

## Segítenél a fordításban?

Ha észrevételeid vannak, vagy hibát találtál a fordításban, jelezd nekünk vagy forkold a repót és küldj egy pull requestet!

### Hogyan kezdj neki?

#### Hiányzó szövegek

A hiányzó szövegeket a [tobetranslated.csv](tobetranslated.csv) fájlban találod az alábbi formátumban:

| Fájlnév               | Kulcs                         |
| --------------------- | ----------------------------- |
| aat_bop_l_english.yml | SWE_riksdag_political_balance |

Ebben az esetben a `aat_bop_l_english.yml` a fájl neve, a `SWE_riksdag_political_balance` pedig a kulcs, amelynek a fordítása hiányzik.

### Fordítási fájlok

A fordítási fájlokat a [content/localisation/replace](content/localisation/replace) mappában találod.
A fájlok a `yml` kiterjesztésűek, amelyek YAML formátumban vannak írva.

Például:

```yaml
autonomy_occupation_zone:0 "Occupation Zone"
```

Ebben az esetben a `autonomy_occupation_zone` a kulcs, amelynek a fordítása a `Megszállási zóna`. Ezért a fájl tartalma a következő lesz:

```yaml
autonomy_occupation_zone:0 "Megszállási zóna"
```

## Közreműködők

- [Bencúr](https://steamcommunity.com/profiles/76561198344557146)

## Kapcsolat

<p align="center">
  <a href="https://discord.gg/NcptrNxQAp"><img
    src=".github/assets/discord.svg"
    alt="Discord"
    height="80"
  /></a>
  <a href="https://steamcommunity.com/id/krm88/"><img
    src=".github/assets/steam.svg"
    alt="Steam"
    height="80"
  /></a>
</p>