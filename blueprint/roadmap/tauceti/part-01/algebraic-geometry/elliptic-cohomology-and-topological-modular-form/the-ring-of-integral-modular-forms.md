---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isIntegralModularForm_iff
statement: formalized
proof: formalized
---

# The ring of integral modular forms

A polynomial in the coefficients of the universal
Weierstrass curve is an integral modular form of weight `k` exactly when it lies in
`ℤ[c₄, c₆, Δ]` and is weighted homogeneous of weight `k`.

```lean
WeierstrassCurve.isIntegralModularForm_iff {k : ℕ} {f : MvPolynomial WeierstrassCurve.Coeff ℤ} :
  WeierstrassCurve.IsIntegralModularForm k f ↔
    f ∈
        ℤ[WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
          WeierstrassCurve.c₆ WeierstrassCurve.Universal.curve,
          WeierstrassCurve.Δ WeierstrassCurve.Universal.curve] ∧
      MvPolynomial.IsWeightedHomogeneous WeierstrassCurve.coefficientWeight f k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deligne's theorem (`WeierstrassCurve.IsIntegralModularForm.mem_adjoin`)](delignes-theorem-weierstrasscurve-isintegralmodu.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.isIntegralModularForm_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.html#WeierstrassCurve.isIntegralModularForm_iff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.isIntegralModularForm_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.html#WeierstrassCurve.isIntegralModularForm_iff)
- [Source of `WeierstrassCurve.isIntegralModularForm_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.lean#L552)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
