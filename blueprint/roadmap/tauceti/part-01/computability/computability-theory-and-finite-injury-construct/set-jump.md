---
declaration: def
origin: cited
lean: Set.jump
statement: formalized
---

# Set.jump

The **jump** `Z'` of a set `Z`: the indices `e` for which the program numbered `e` halts on
input `e` relative to the oracle of `Z`.

```lean
Set.jump (Z : Set ℕ) : Set ℕ
```

## Depends on

- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Lean

Formalized in Tau Ceti as [`Set.jump`](https://taucetiproject.org/docs/TauCeti/Computability/Jump/Basic.html#Set.jump).

## Sources

- [Tau Ceti documentation: `Set.jump`](https://taucetiproject.org/docs/TauCeti/Computability/Jump/Basic.html#Set.jump)
- [Source of `Set.jump` in TauCeti/Computability/Jump/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Jump/Basic.lean#L64)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
