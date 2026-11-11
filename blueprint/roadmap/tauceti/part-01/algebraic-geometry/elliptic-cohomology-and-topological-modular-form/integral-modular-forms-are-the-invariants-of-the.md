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
- [Source of `WeierstrassCurve.isIntegralModularForm_iff_rightUnit` in TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean#L459)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCohomology/STATUS.md)
