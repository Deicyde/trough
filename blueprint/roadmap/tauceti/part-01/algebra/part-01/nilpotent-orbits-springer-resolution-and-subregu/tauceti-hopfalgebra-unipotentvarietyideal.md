---
declaration: def
origin: cited
lean: TauCeti.HopfAlgebra.unipotentVarietyIdeal
statement: formalized
---

# TauCeti.HopfAlgebra.unipotentVarietyIdeal

The **ideal of the unipotent variety** of the affine group `Spec H` over a field `k`: the
functions vanishing at every unipotent point with values in the algebraic closure of `k`. Over a
finite-type `H` it is the radical of the unipotence ideal of any faithful representation
(`radical_unipotenceIdeal_eq_unipotentVarietyIdeal`), and the algebraic closure may be replaced by
any algebraically closed extension (`mem_unipotentVarietyIdeal_iff_of_isAlgClosed`).

```lean
TauCeti.HopfAlgebra.unipotentVarietyIdeal.{u, v} (k : Type u) (H : Type v) [Field k] [CommRing H]
  [HopfAlgebra k H] : Ideal H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfAlgebra.unipotentVarietyIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/UnipotentPoint/Variety.html#TauCeti.HopfAlgebra.unipotentVarietyIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfAlgebra.unipotentVarietyIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/UnipotentPoint/Variety.html#TauCeti.HopfAlgebra.unipotentVarietyIdeal)
- [Source of `TauCeti.HopfAlgebra.unipotentVarietyIdeal` in TauCeti/Algebra/AlgebraicGroup/Representation/UnipotentPoint/Variety.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Representation/UnipotentPoint/Variety.lean#L71)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
