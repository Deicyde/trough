---
declaration: def
origin: cited
lean: TauCeti.centralizerHopfIdeal
statement: formalized
---

# TauCeti.centralizerHopfIdeal

The Hopf ideal of the centralizer of an element `x` of the Lie algebra, the stabilizer of `x`
under the adjoint representation. Contravariantly, it cuts out the closed subgroup of `Spec H`
fixing `x` under `Ad`.

```lean
TauCeti.centralizerHopfIdeal.{u} {k : Type u} [Field k] (H : Type u) [CommRing H] [HopfAlgebra k H]
  [Module.Finite k (TauCeti.Bialgebra.CotangentSpace k H)]
  (x : Module.Dual k (TauCeti.Bialgebra.CotangentSpace k H)) : TauCeti.HopfIdeal k H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.centralizerHopfIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.centralizerHopfIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.centralizerHopfIdeal`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.centralizerHopfIdeal)
- [Source of `TauCeti.centralizerHopfIdeal` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean#L81)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
