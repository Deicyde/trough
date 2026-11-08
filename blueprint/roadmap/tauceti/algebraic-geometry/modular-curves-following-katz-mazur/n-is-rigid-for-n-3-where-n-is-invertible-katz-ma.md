---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma
statement: formalized
proof: formalized
---

# `[Γ(N)]` is rigid for `N ≥ 3` where `N` is invertible (Katz–Mazur, 2.7.2)

Over a base `B`
on which `N` is invertible, `[Γ(N)]` is isomorphic to the rigid naive problem `[Γ(N)]_naive`
(`ModuliProblem.isRigid_gammaNaive`).

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma.{u} (B : AlgebraicGeometry.Scheme) (N : ℕ)
  [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) (hN3 : 3 ≤ N) :
  (TauCeti.AlgebraicGeometry.ModuliProblem.gamma B N).IsRigid
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mathlib's Jacobian addition formula at `(φₘ : ωₘ : ψₘ)` and `(φₙ : ωₙ : ψₙ)` returns `(φₙ₊ₘ : ωₙ₊ₘ : ψₙ₊ₘ)`, scaled by `ψₙ₋ₘ`](../elliptic-curve/mathlibs-jacobian-addition-formula-at-m-m-m-and.md)
- [Mathlib's Jacobian doubling formula sends `(φₙ : ωₙ : ψₙ)` to `(φ₂ₙ : ω₂ₙ : ψ₂ₙ)`, as an equality of triples and not merely of the points they represent](../elliptic-curve/mathlibs-jacobian-doubling-formula-sends-n-n-n-t.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.isRigid_gamma` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L348)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
