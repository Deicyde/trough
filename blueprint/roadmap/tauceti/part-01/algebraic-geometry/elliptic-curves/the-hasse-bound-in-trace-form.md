---
declaration: theorem
origin: cited
lean: WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card, WeierstrassCurve.hasse_bound
statement: formalized
proof: formalized
---

# The Hasse bound, in trace form

over a finite field with `q` elements, the Frobenius trace
`a_q` of a Weierstrass curve satisfies `a_q² ≤ 4q`. For an elliptic curve this is the Hasse bound;
for a singular curve the trace is `0` or `±1`. `hasse_bound` states the same inequality in terms
of the number of points of an elliptic curve.

```lean
WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card.{u_1} {F : Type u_1} [Field F] [Finite F]
  (W : WeierstrassCurve F) : W.frobeniusTrace ^ 2 ≤ 4 * ↑(Nat.card F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card).

## Other forms

**The Hasse bound (Silverman V.1.1).** Formalized in Tau Ceti as [`WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound).

```lean
WeierstrassCurve.hasse_bound.{u_1} {F : Type u_1} [Field F] [Finite F] (W : WeierstrassCurve F)
  [W.IsElliptic] : (↑(Nat.card W.toAffine.Point) - (↑(Nat.card F) + 1)) ^ 2 ≤ 4 * ↑(Nat.card F)
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card)
- [Source of `WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card` in TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean#L43)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)
