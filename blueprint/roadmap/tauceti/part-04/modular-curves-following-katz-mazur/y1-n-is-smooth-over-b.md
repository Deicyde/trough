---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap
statement: formalized
proof: formalized
---

# `Y₁(N)` is smooth over `B`

For `N ≥ 4` invertible on `B`, the structure morphism of the
fine moduli scheme `Y₁(N)` to `B` is smooth; for example `Y₁(N)` is smooth over `ℤ[1/N]`.

```lean
TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap.{u} (B : AlgebraicGeometry.Scheme) (N : ℕ)
  [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) (h4 : 4 ≤ N) :
  AlgebraicGeometry.Smooth (TauCeti.AlgebraicGeometry.EllObj.yOne B N).structureMap
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `n`-torsion of an elliptic curve is étale where `n` is invertible](the-n-torsion-of-an-elliptic-curve-is-etale-wher.md)
- [`Y₁(N)` is a fine moduli scheme for `N ≥ 4`](y1-n-is-a-fine-moduli-scheme-for-n-4.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap)
- [Source of `TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap` in TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean#L761)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
