---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.zetaFunction_eq
statement: formalized
proof: formalized
---

# Isogenous curves over a finite field have the same zeta function

`Z(W/F, T) = exp (∑_{n ≥ 1} #W(𝔽_{qⁿ}) Tⁿ / n)`.

```lean
TauCeti.Isogeny.zetaFunction_eq.{u_1} {F : Type u_1} [Field F] [Finite F]
  {W₁ W₂ : WeierstrassCurve.Affine F} [WeierstrassCurve.IsElliptic W₁]
  [WeierstrassCurve.IsElliptic W₂] (φ : TauCeti.Isogeny W₁ W₂) :
  WeierstrassCurve.zetaFunction W₁ = WeierstrassCurve.zetaFunction W₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hurwitz genus formula](../../part-01/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula.md)
- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq)
- [Source of `TauCeti.Isogeny.zetaFunction_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean#L112)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
