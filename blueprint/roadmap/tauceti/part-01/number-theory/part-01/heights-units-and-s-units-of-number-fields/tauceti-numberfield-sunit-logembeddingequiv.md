---
declaration: def
origin: cited
lean: TauCeti.NumberField.SUnit.logEmbeddingEquiv
statement: formalized
---

# TauCeti.NumberField.SUnit.logEmbeddingEquiv

The `S`-logarithmic embedding induces a `ℤ`-linear equivalence from the `S`-units modulo
torsion onto the `S`-unit lattice. This is the `S`-analogue of Mathlib's
`NumberField.Units.logEmbeddingEquiv`.

```lean
TauCeti.NumberField.SUnit.logEmbeddingEquiv.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))) :
  (Additive ↥((↑S).unit K) ⧸ Submodule.torsion ℤ (Additive ↥((↑S).unit K))) ≃ₗ[ℤ]
    ↥(TauCeti.NumberField.SUnit.unitLattice S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's inequality at a finite place](../../part-03/number-field/liouvilles-inequality-at-a-finite-place.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.SUnit.logEmbeddingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Lattice.html#TauCeti.NumberField.SUnit.logEmbeddingEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.SUnit.logEmbeddingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Lattice.html#TauCeti.NumberField.SUnit.logEmbeddingEquiv)
- [Source of `TauCeti.NumberField.SUnit.logEmbeddingEquiv` in TauCeti/NumberTheory/NumberField/SUnits/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/SUnits/Lattice.lean#L229)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HeightsAndUnits/STATUS.md)
