---
declaration: def
origin: cited
lean: WeierstrassCurve.pointedTwistEquivNonabelianH1
statement: formalized
---

# Pointed twists are classified by nonabelian Galois cohomology

For a Galois extension
`L/K`, the pointed twists of `W` split by `L` are in bijection with
`H¹(Gal(L/K), Aut(W_L))`. The equivalence sends a trivialisation `C` to the class of the cocycle
`σ ↦ C (σ C)⁻¹`.

```lean
WeierstrassCurve.pointedTwistEquivNonabelianH1.{u_1, u_3} {K : Type u_1} [Field K]
  (W : WeierstrassCurve K) (L : Type u_3) [Field L] [Algebra K L] [IsGalois K L] :
  W.PointedTwist L ≃ TauCeti.NonabelianH1 Gal(L/K) (W.AutCoeff L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.pointedTwistEquivNonabelianH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Twist/Classification.html#WeierstrassCurve.pointedTwistEquivNonabelianH1).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.pointedTwistEquivNonabelianH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Twist/Classification.html#WeierstrassCurve.pointedTwistEquivNonabelianH1)
- [Source of `WeierstrassCurve.pointedTwistEquivNonabelianH1` in TauCeti/AlgebraicGeometry/EllipticCurve/Twist/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Twist/Classification.lean#L205)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
