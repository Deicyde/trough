---
declaration: def
origin: cited
lean: TauCeti.etaleMass
statement: formalized
---

# TauCeti.etaleMass

The **étale mass** `M_n(K) = (1 / n!) ∑_ρ q ^ (-d(ρ))` of a nonarchimedean local field `K`,
summed over the labelled Galois sets of size `n`, where `q` is the residue cardinality of `K`.

```lean
TauCeti.etaleMass.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] (n : ℕ) : ENNReal
```

## Depends on

- [TauCeti.GaloisSet](tauceti-galoisset.md)
- [TauCeti.orbitDiscriminantExponent](tauceti-orbitdiscriminantexponent.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.etaleMass`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.html#TauCeti.etaleMass).

## Sources

- [Tau Ceti documentation: `TauCeti.etaleMass`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.html#TauCeti.etaleMass)
- [Source of `TauCeti.etaleMass` in TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/EtaleMassFormula/Mass.lean#L113)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
