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
- [Source of `TauCeti.centralizerHopfIdeal` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean#L81)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
