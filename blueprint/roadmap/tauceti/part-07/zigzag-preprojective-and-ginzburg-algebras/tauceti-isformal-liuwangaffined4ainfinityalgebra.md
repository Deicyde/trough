---
declaration: theorem
origin: cited
lean: TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra
statement: formalized
proof: formalized
---

# TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra

**Liu--Wang's `A∞` algebra is formal**, for every scalar `c`: the displayed quartic operation
`m₄` is a Hochschild coboundary of the strict zigzag algebra, so it defines the trivial
`A∞` deformation.

```lean
TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra.{w} {k : Type w} [CommRing k] (c : k) :
  (TauCeti.liuWangAffineD4AInfinityAlgebra k c).IsFormal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/Affine/D/Four.html#TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/Affine/D/Four.html#TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra)
- [Source of `TauCeti.isFormal_liuWangAffineD4AInfinityAlgebra` in TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/Affine/D/Four.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/Affine/D/Four.lean#L343)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
