---
declaration: theorem
origin: cited
lean: WeierstrassCurve.hasse_bound
statement: formalized
proof: formalized
---

# WeierstrassCurve.hasse_bound

**The Hasse bound** (Silverman V.1.1): an elliptic curve `E` over a field with `q` elements
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

- [TauCeti.hurwitz_genus_formula](../../part-01/algebraic-curves-function-fields-divisors-and-ri/tauceti-hurwitz-genus-formula.md)
- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.hasse_bound`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.html#WeierstrassCurve.hasse_bound)
- [Source of `WeierstrassCurve.hasse_bound` in TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/HasseBound.lean#L53)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
