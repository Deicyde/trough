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

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem (Silverman, *The Arithmetic of Elliptic Curves*, III.4.11 in its separable form)](../elliptic-curve/the-factorisation-theorem-silverman-the-arithmet.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Mathlib's Jacobian addition formula at `(φₘ : ωₘ : ψₘ)` and `(φₙ : ωₙ : ψₙ)` returns `(φₙ₊ₘ : ωₙ₊ₘ : ψₙ₊ₘ)`, scaled by `ψₙ₋ₘ`](../elliptic-curve/mathlibs-jacobian-addition-formula-at-m-m-m-and.md)
- [Mathlib's Jacobian doubling formula sends `(φₙ : ωₙ : ψₙ)` to `(φ₂ₙ : ω₂ₙ : ψ₂ₙ)`, as an equality of triples and not merely of the points they represent](../elliptic-curve/mathlibs-jacobian-doubling-formula-sends-n-n-n-t.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/tauceti-place-sum-ramificationidx-mul-relativede.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound).

## Other forms

**The Hasse bound, in trace form.** Formalized in Tau Ceti as [`WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card).

```lean
WeierstrassCurve.frobeniusTrace_sq_le_four_mul_card.{u_1} {F : Type u_1} [Field F] [Finite F]
  (W : WeierstrassCurve F) [W.IsElliptic] : W.frobeniusTrace ^ 2 ≤ 4 * ↑(Nat.card F)
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound)
- [Source of `WeierstrassCurve.hasse_bound` in TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean#L53)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
