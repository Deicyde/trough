---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isIntegralModularForm_iff_rightUnit
statement: formalized
proof: formalized
---

# Integral modular forms are the invariants of the Weierstrass Hopf algebroid

`f` is an
integral modular form of weight `k` exactly when `η_R f = u⁻ᵏ η_L f` in `Γ`.

```lean
WeierstrassCurve.isIntegralModularForm_iff_rightUnit {k : ℕ}
  {f : MvPolynomial WeierstrassCurve.Coeff ℤ} :
  WeierstrassCurve.IsIntegralModularForm k f ↔
    TauCeti.WeierstrassHopfAlgebroid.rightUnit f =
      ↑(TauCeti.WeierstrassChange.ChangeRing.universalChange
                  (MvPolynomial WeierstrassCurve.Coeff ℤ)).u⁻¹ ^
          k *
        (algebraMap (MvPolynomial WeierstrassCurve.Coeff ℤ)
            TauCeti.WeierstrassHopfAlgebroid.ArrowRing)
          f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.isIntegralModularForm_iff_rightUnit`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.html#WeierstrassCurve.isIntegralModularForm_iff_rightUnit).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.isIntegralModularForm_iff_rightUnit`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.html#WeierstrassCurve.isIntegralModularForm_iff_rightUnit)
- [Source of `WeierstrassCurve.isIntegralModularForm_iff_rightUnit` in TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean#L459)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
