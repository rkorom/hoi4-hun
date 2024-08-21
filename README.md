# HOI4 magyarosítás

[Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3281592737)

Mint tudjuk, a Paradox Magyarország készített egy fordítást a játékhoz, amely már évek óta nem került frissítésre. Ennek a hiánynak a betöltésére szerettük volna folytatni a játék magyar nyelvre történő fordítását. A fordítás tartalmazza a játék összes szövegét, beleértve a DLC-két is.

## Közreműködők

- [Bencúr](https://steamcommunity.com/profiles/76561198344557146)

## Segítenél a fordításban?

Ha észrevételeid vannak, vagy hibát találtál a fordításban, jelezd nekünk vagy forkold a repót és küldj egy pull requestet!

### Hogyan kezdj neki?

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
