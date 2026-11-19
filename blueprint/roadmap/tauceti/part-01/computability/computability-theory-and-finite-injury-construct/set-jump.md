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
- [Source of `Set.jump` in TauCeti/Computability/Jump/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/Jump/Basic.lean#L66)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
