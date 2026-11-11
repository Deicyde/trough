---
declaration: theorem
origin: cited
lean: WeierstrassCurve.hasse_bound, WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card
statement: formalized
proof: formalized
---

# The Hasse bound (Silverman V.1.1)

an elliptic curve `E` over a field with `q` elements
satisfies `(#E(𝔽_q) - (q + 1))² ≤ 4q`, that is `|#E(𝔽_q) - (q + 1)| ≤ 2√q`, where the count
includes the point at infinity. `frobeniusTrace_sq_le_four_mul_card` is the same bound for the
trace `a_q`.

```lean
WeierstrassCurve.hasse_bound.{u_1} {F : Type u_1} [Field F] [Finite F] (W : WeierstrassCurve F)
  [W.IsElliptic] : (↑(Nat.card W.toAffine.Point) - (↑(Nat.card F) + 1)) ^ 2 ≤ 4 * ↑(Nat.card F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound).

## Other forms

**The Hasse bound, in trace form.** Formalized in Tau Ceti as [`WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card).

```lean
WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card.{u_1} {F : Type u_1} [Field F] [Finite F]
  (W : WeierstrassCurve F) : W.frobeniusTrace ^ 2 ≤ 4 * ↑(Nat.card F)
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound)
- [Source of `WeierstrassCurve.hasse_bound` in TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean#L67)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
