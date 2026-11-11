---
declaration: theorem
origin: cited
lean: WeierstrassCurve.height_formalGroup_eq_one_iff
statement: formalized
proof: formalized
---

# The height-one criterion for `Ê`

over a field of characteristic `p`, the formal group of
a Weierstrass curve has height one exactly when the coefficient of `Tᵖ⁻¹` in its invariant
differential is nonzero.

```lean
WeierstrassCurve.height_formalGroup_eq_one_iff.{u_1} {K : Type u_1} [Field K]
  (W : WeierstrassCurve K) {p : ℕ} [hp : Fact (Nat.Prime p)] [CharP K p] :
  W.formalGroup.height p = 1 ↔ (PowerSeries.coeff (p - 1)) W.formalGroup.invariantDifferential ≠ 0
```

## Depends on

- [FormalGroup.height](../../ring-theory/part-01/bordism-formal-groups-and-chromatic-operations/formalgroup-height.md)

## Proof depends on

- [The `p`-series has order a power of `p` in characteristic `p`](../../ring-theory/part-01/bordism-formal-groups-and-chromatic-operations/the-p-series-has-order-a-power-of-p-in-character.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.height_formalGroup_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.html#WeierstrassCurve.height_formalGroup_eq_one_iff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.height_formalGroup_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.html#WeierstrassCurve.height_formalGroup_eq_one_iff)
- [Source of `WeierstrassCurve.height_formalGroup_eq_one_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.lean#L98)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCohomology/STATUS.md)
