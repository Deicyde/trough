---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom, TauCeti.Isogeny.wronskian_xRatFunc_sq_mul_Ψ₂Sq
statement: formalized
proof: formalized
---

# The Wronskian identity of an isogeny

if `φ^*ω₂ = c ω₁`, then

  `w(x) u₁ = c D(x)² φ^*u₂`,

where `w` is the Wronskian of `φ.xRatFunc = N / D` and `u = 2y + a₁x + a₃` is the denominator of
the invariant differential.

```lean
TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom.{u_1} {F : Type u_1}
  [Field F] {W₁ W₂ : WeierstrassCurve.Affine F} [WeierstrassCurve.IsElliptic W₁]
  [WeierstrassCurve.IsElliptic W₂] {φ : TauCeti.Isogeny W₁ W₂} {c : F}
  (hc : φ.pullbackDifferential W₂.invariantDifferential = c • W₁.invariantDifferential) :
  (Polynomial.aeval W₁.genericX) (φ.xRatFunc.denom.wronskian φ.xRatFunc.num) *
      W₁.invariantDifferentialDenom =
    (algebraMap F W₁.FunctionField) c * (Polynomial.aeval W₁.genericX) φ.xRatFunc.denom ^ 2 *
      φ.fieldPullback W₂.invariantDifferentialDenom
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Wronskian.html#TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom).

## Other forms

**The Wronskian identity with `y` eliminated.** Formalized in Tau Ceti as [`TauCeti.Isogeny.wronskian_xRatFunc_sq_mul_Ψ₂Sq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Wronskian.html#TauCeti.Isogeny.wronskian_xRatFunc_sq_mul_%CE%A8%E2%82%82Sq).

```lean
TauCeti.Isogeny.wronskian_xRatFunc_sq_mul_Ψ₂Sq.{u_1} {F : Type u_1} [Field F]
  {W₁ W₂ : WeierstrassCurve.Affine F} [WeierstrassCurve.IsElliptic W₁]
  [WeierstrassCurve.IsElliptic W₂] {φ : TauCeti.Isogeny W₁ W₂} {c : F}
  (hc : φ.pullbackDifferential W₂.invariantDifferential = c • W₁.invariantDifferential) :
  φ.xRatFunc.denom.wronskian φ.xRatFunc.num ^ 2 * WeierstrassCurve.Ψ₂Sq W₁ =
    Polynomial.C (c ^ 2) * φ.xRatFunc.denom *
      (Polynomial.C 4 * φ.xRatFunc.num ^ 3 +
            Polynomial.C (WeierstrassCurve.b₂ W₂) * φ.xRatFunc.num ^ 2 * φ.xRatFunc.denom +
          Polynomial.C (2 * WeierstrassCurve.b₄ W₂) * φ.xRatFunc.num * φ.xRatFunc.denom ^ 2 +
        Polynomial.C (WeierstrassCurve.b₆ W₂) * φ.xRatFunc.denom ^ 3)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Wronskian.html#TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom)
- [Source of `TauCeti.Isogeny.aeval_wronskian_xRatFunc_mul_invariantDifferentialDenom` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Wronskian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/Wronskian.lean#L76)
