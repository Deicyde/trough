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

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/tauceti-place-sum-ramificationidx-mul-relativede.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.html#TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.html#TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1)
- [Source of `TauCeti.Isogeny.exact_kummerClassMap_kerCoeffInclH1` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Descent.lean#L449)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
