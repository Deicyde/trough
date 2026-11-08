---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.zetaFunction_eq
statement: formalized
proof: formalized
---

# Isogenous curves over a finite field have the same zeta function `Z(W/F, T) = exp (∑_{n ≥ 1} #W(𝔽_{qⁿ}) Tⁿ / n)`

```lean
TauCeti.Isogeny.zetaFunction_eq.{u_1} {F : Type u_1} [Field F] [Finite F]
  {W₁ W₂ : WeierstrassCurve.Affine F} [WeierstrassCurve.IsElliptic W₁]
  [WeierstrassCurve.IsElliptic W₂] (φ : TauCeti.Isogeny W₁ W₂) :
  WeierstrassCurve.zetaFunction W₁ = WeierstrassCurve.zetaFunction W₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Mathlib's Jacobian addition formula at `(φₘ : ωₘ : ψₘ)` and `(φₙ : ωₙ : ψₙ)` returns `(φₙ₊ₘ : ωₙ₊ₘ : ψₙ₊ₘ)`, scaled by `ψₙ₋ₘ`](../elliptic-curve/mathlibs-jacobian-addition-formula-at-m-m-m-and.md)
- [Mathlib's Jacobian doubling formula sends `(φₙ : ωₙ : ψₙ)` to `(φ₂ₙ : ω₂ₙ : ψ₂ₙ)`, as an equality of triples and not merely of the points they represent](../elliptic-curve/mathlibs-jacobian-doubling-formula-sends-n-n-n-t.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/tauceti-place-sum-ramificationidx-mul-relativede.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq)
- [Source of `TauCeti.Isogeny.zetaFunction_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean#L112)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
