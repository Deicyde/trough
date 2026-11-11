---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq
statement: formalized
proof: formalized
---

# The genus of a smooth projective plane curve (Fulton, *Algebraic Curves*, Section 8.3)

for
an irreducible nonsingular homogeneous plane equation of degree `d`, the genus
`dim_k H¹(C, 𝒪_C)` of the curve `C` is `(d - 1)(d - 2) / 2`.

```lean
TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq.{u, u_1} {k : Type u} [Field k]
  {K : Type u_1} [Field K] [Algebra k K] [IsAlgClosed K] {G : MvPolynomial (Fin 3) k} {d : ℕ}
  (hG : G.IsHomogeneous d)
  (hsm :
    ∀ (b : Fin 3 → K),
      b ≠ 0 →
        (MvPolynomial.aeval b) G = 0 → ∃ j, (MvPolynomial.aeval b) ((MvPolynomial.pderiv j) G) ≠ 0)
  [Fact (Irreducible G)] :
  AlgebraicGeometry.Scheme.genus k (TauCeti.AlgebraicGeometry.projectivePlaneCurve hG) =
    (d - 1) * (d - 2) / 2
```

## Depends on

- [The projective plane curve `G = 0` of a homogeneous polynomial `G ∈ R[X₀, X₁, X₂]`](the-projective-plane-curve-g-0-of-a-homogeneous.md)

## Proof depends on

- [The dimension theorem at the origin](../../ring-theory/part-01/multivariate-polynomials/the-dimension-theorem-at-the-origin.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The Jacobian criterion for a hypersurface](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-a-hypersurface.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Genus.html#TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Genus.html#TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq)
- [Source of `TauCeti.AlgebraicGeometry.projectivePlaneCurve.genus_eq` in TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Genus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Genus.lean#L132)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
