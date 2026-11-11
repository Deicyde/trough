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

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.zetaFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.html#TauCeti.Isogeny.zetaFunction_eq)
- [Source of `TauCeti.Isogeny.zetaFunction_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Frobenius/Isogenous.lean#L112)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
