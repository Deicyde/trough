---
declaration: def
origin: cited
lean: TopCat.singularCohomologyDualEquiv, TopCat.singularKronecker_bijective_succ_of_projective_homology, TopCat.singularKroneckerEquiv, TopCat.singularKronecker_bijective_zero, TopCat.singularKronecker_bijective_of_projective_homology
statement: formalized
---

# The universal coefficient theorem over a field

singular cohomology with coefficients in
a field `k` is the dual of singular homology, `Hⁿ(X; k) ≃ₗ[k] Module.Dual k (Hₙ(X; k))`.  It sends
a class to the linear form underlying its Kronecker pairing
(`TopCat.singularCohomologyDualEquiv_apply`).

```lean
TopCat.singularCohomologyDualEquiv.{w} {k : Type w} [Field k] (X : TopCat) (n : ℕ) :
  ↑(TopCat.singularCohomology (↧k) k (↧k) X n) ≃ₗ[k]
    Module.Dual k ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj ↧k).obj X)
```

## Depends on

- [The universal coefficient theorem with projective homology](../../algebra/homology/the-universal-coefficient-theorem-with-projectiv.md)

## Lean

Formalized in Tau Ceti as [`TopCat.singularCohomologyDualEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.html#TopCat.singularCohomologyDualEquiv).

## Other forms

**The universal coefficient theorem above a projective homology module, over a hereditary commutative ring.** Formalized in Tau Ceti as [`TopCat.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_succ_of_projective_homology).

```lean
TopCat.singularKronecker_bijective_succ_of_projective_homology.{w} {k : Type w} [CommRing k]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1] (X : TopCat)
  (R M : ModuleCat k) [Module.Projective k ↑R] (n : ℕ)
  [CategoryTheory.Projective
      (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj R).obj X)] :
  Function.Bijective ⇑(X.singularKronecker k (n + 1))
```

**The universal coefficient theorem for injective coefficients.** Formalized in Tau Ceti as [`TopCat.singularKroneckerEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Kronecker.html#TopCat.singularKroneckerEquiv).

```lean
TopCat.singularKroneckerEquiv.{w, v, u, u_1} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [CategoryTheory.Limits.HasCoproducts C] {R M : C} (X : TopCat)
  (k : Type u_1) [Ring k] [CategoryTheory.Linear k C] [CategoryTheory.Injective M] (n : ℕ) :
  ↑(TopCat.singularCohomology R k M X n) ≃ₗ[k]
    ((AlgebraicTopology.singularHomologyFunctor C n).obj R).obj X ⟶ M
```

**The universal coefficient theorem in degree zero.** Formalized in Tau Ceti as [`TopCat.singularKronecker_bijective_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Kronecker.html#TopCat.singularKronecker_bijective_zero).

```lean
TopCat.singularKronecker_bijective_zero.{w, v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.Limits.HasCoproducts C] {R M : C} (X : TopCat) (k : Type u_1) [Ring k]
  [CategoryTheory.Linear k C] : Function.Bijective ⇑(X.singularKronecker k 0)
```

**The universal coefficient theorem with projective homology, over any commutative ring `k`.** Formalized in Tau Ceti as [`TopCat.singularKronecker_bijective_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_of_projective_homology).

```lean
TopCat.singularKronecker_bijective_of_projective_homology.{w} {k : Type w} [CommRing k] (X : TopCat)
  (R M : ModuleCat k) [Module.Projective k ↑R]
  [hX :
    ∀ (n : ℕ),
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj R).obj X)]
  (n : ℕ) : Function.Bijective ⇑(X.singularKronecker k n)
```

## Sources

- [Tau Ceti documentation: `TopCat.singularCohomologyDualEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.html#TopCat.singularCohomologyDualEquiv)
- [Source of `TopCat.singularCohomologyDualEquiv` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.lean#L64)
