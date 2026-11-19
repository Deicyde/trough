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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.height_formalGroup_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.html#WeierstrassCurve.height_formalGroup_eq_one_iff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.height_formalGroup_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.html#WeierstrassCurve.height_formalGroup_eq_one_iff)
- [Source of `WeierstrassCurve.height_formalGroup_eq_one_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Height/Basic.lean#L98)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
