---
declaration: def
origin: cited
lean: Setoid.HasCantorAntichainOn
statement: formalized
---

# Setoid.HasCantorAntichainOn

`A` carries a **Cantor antichain** for `E`: a continuous map of Cantor space into `A` whose
distinct points have `E`-inequivalent images.

```lean
Setoid.HasCantorAntichainOn.{u} {X : Type u} [TopologicalSpace X] (E : Setoid X) (A : Set X) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Setoid.HasCantorAntichainOn`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Antichain.html#Setoid.HasCantorAntichainOn).

## Sources

- [Tau Ceti documentation: `Setoid.HasCantorAntichainOn`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Antichain.html#Setoid.HasCantorAntichainOn)
- [Source of `Setoid.HasCantorAntichainOn` in TauCeti/SetTheory/Descriptive/Antichain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/Antichain.lean#L105)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
