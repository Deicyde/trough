---
declaration: theorem
origin: cited
lean: TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv
statement: formalized
proof: formalized
---

# The inverse Tate uniformisation is Galois-equivariant

For an algebraic extension `L/K`
and a `K`-automorphism `σ` of `L`, the parameter of `σ P` is `σ` applied to the parameter of
`P`.

```lean
TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv.{u_1, u_2} {K : Type u_1}
  [NormedField K] [CompleteSpace K] [IsUltrametricDist K] {L : Type u_2} [NormedField L]
  [NormedAlgebra K L] [CompleteSpace L] [IsUltrametricDist L] [DecidableEq L]
  [Algebra.IsAlgebraic K L] (q : Kˣ) (hq : ‖↑q‖ < 1) (σ : Gal(L/K))
  (P :
    (WeierstrassCurve.toAffine
        (WeierstrassCurve.Affine.baseChange (TauCeti.tateCurveAt q hq) L)).Point) :
  (TauCeti.tateUniformizationBaseChangeEquiv L q hq).symm
      ((WeierstrassCurve.Affine.Point.map ↑σ) P) =
    Additive.ofMul
      ((TauCeti.tateParameterMap q ↑σ)
        (Additive.toMul ((TauCeti.tateUniformizationBaseChangeEquiv L q hq).symm P)))
```

## Depends on

- [The Tate uniformisation over an extension as a group isomorphism `Lˣ / q^ℤ ≃ E_q(L)`, written additively on the source](the-tate-uniformisation-over-an-extension-as-a-g.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv)
- [Source of `TauCeti.tateUniformizationBaseChangeEquiv_symm_map_algEquiv` in TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean#L156)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
