---
declaration: def
origin: cited
lean: TauCeti.Toric.Fan.projectiveSpace
statement: formalized
---

# TauCeti.Toric.Fan.projectiveSpace

The fan of projective space attached to an integral basis `b` of an integral lattice: its
cones are spanned by the families of ray generators `projectiveSpaceGenerator b` omitting at least
one of them. For a basis indexed by a type with `n` elements it is the fan of `n`-dimensional
complex projective space.

```lean
TauCeti.Toric.Fan.projectiveSpace.{u_1, u_2, u_3} {N : Type u_1} {V : Type u_2} {ι : Type u_3}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} [Fintype ι]
  (b : Module.Basis ι ℤ N) (hi : TauCeti.Toric.IsIntegralLattice i) : TauCeti.Toric.Fan i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.projectiveSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Fan/ProjectiveSpace/Basic.html#TauCeti.Toric.Fan.projectiveSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.projectiveSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Fan/ProjectiveSpace/Basic.html#TauCeti.Toric.Fan.projectiveSpace)
- [Source of `TauCeti.Toric.Fan.projectiveSpace` in TauCeti/Geometry/Toric/Algebraic/Fan/ProjectiveSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Toric/Algebraic/Fan/ProjectiveSpace/Basic.lean#L275)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AnalyticToricGeometry/STATUS.md)
