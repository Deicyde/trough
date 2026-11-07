---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1
statement: formalized
proof: formalized
---

# The `φ`-descent sequence is exact at `H¹(G_K, E₁[φ])`

the kernel of
`H¹(G_K, E₁[φ]) → H¹(G_K, E₁)[φ]` is the image of `E₂(K) ⧸ φ(E₁(K))` under the Kummer map.
Together with `TauCeti.Isogeny.kummerClassMap_injective` and
`TauCeti.Isogeny.kerCoeffInclH1_surjective` this is the short exact sequence
`0 → E₂(K) ⧸ φ(E₁(K)) → H¹(G_K, E₁[φ]) → H¹(G_K, E₁)[φ] → 0`.

```lean
TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1.{u_1} {K : Type u_1} [Field K]
  {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic] [W₂.IsElliptic]
  (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine)
  [Algebra.IsSeparable (↥φ.fieldPullback.fieldRange) W₁.toAffine.FunctionField] [DecidableEq K] :
  Function.Exact ⇑φ.kummerClassMap ⇑φ.kerCoeffInclH1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.hurwitz\_genus\_formula](../../part-01/algebraic-curves-function-fields-divisors-and-ri/tauceti-hurwitz-genus-formula.md)
- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.html#TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.html#TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1)
- [Source of `TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.lean#L449)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
