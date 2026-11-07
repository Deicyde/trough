---
declaration: def
origin: cited
lean: TopCat.singularUniversalCoefficientEquiv
statement: formalized
---

# The splitting of the universal coefficient sequence

of singular cohomology over a
hereditary commutative ring: a `k`-linear equivalence
`Hⁿ⁺¹(X; R, M) ≃ₗ[k] Ext¹(Hₙ(X; R), M) × Hom(Hₙ₊₁(X; R), M)` whose second component is the
Kronecker map (`TopCat.singularUniversalCoefficientEquiv_apply_snd`) and whose inverse restricts
to `TopCat.singularExtToCohomology` on the first factor
(`TopCat.singularUniversalCoefficientEquiv_symm_inl`).  It is built from the section
`TopCat.singularKroneckerSection` and is not natural in `X`.

```lean
TopCat.singularUniversalCoefficientEquiv.{w} {k : Type w} [CommRing k]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1] (X : TopCat)
  (R M : ModuleCat k) [Module.Projective k ↑R] (n : ℕ) :
  ↑(TopCat.singularCohomology R k M X (n + 1)) ≃ₗ[k]
    CategoryTheory.Abelian.Ext
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj R).obj X) M 1 ×
      (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) (n + 1)).obj R).obj X ⟶ M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.singularUniversalCoefficientEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularUniversalCoefficientEquiv).

## Sources

- [Tau Ceti documentation: `TopCat.singularUniversalCoefficientEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularUniversalCoefficientEquiv)
- [Source of `TopCat.singularUniversalCoefficientEquiv` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean#L214)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
