---
declaration: abbrev
origin: cited
lean: TauCeti.ContinuousOuterDerivation
statement: formalized
---

# The continuous outer derivations `OutDer_cont(A)`

the quotient Lie algebra of the
continuous derivations by the Lie ideal of inner derivations, with the quotient topology. The
ideal is the image of `ad` itself rather than its closure, so this quotient need not be
Hausdorff.

```lean
TauCeti.ContinuousOuterDerivation.{u, v} (R : Type u) (A : Type v) [CommRing R] [Ring A]
  [Algebra R A] [TopologicalSpace A] [IsTopologicalAddGroup A] [SeparatelyContinuousMul A]
  [ContinuousConstSMul R A] : Type v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousOuterDerivation`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Derivation/Continuous.html#TauCeti.ContinuousOuterDerivation).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousOuterDerivation`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Derivation/Continuous.html#TauCeti.ContinuousOuterDerivation)
- [Source of `TauCeti.ContinuousOuterDerivation` in TauCeti/Algebra/Lie/Derivation/Continuous.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Derivation/Continuous.lean#L232)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
