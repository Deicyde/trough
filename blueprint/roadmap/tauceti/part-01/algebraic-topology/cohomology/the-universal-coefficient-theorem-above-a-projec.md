---
declaration: theorem
origin: cited
lean: TopCat.singularKronecker_bijective_succ_of_projective_homology
statement: formalized
proof: formalized
---

# The universal coefficient theorem above a projective homology module, over a hereditary commutative ring

for a projective coefficient module `R`, if `Hₙ(X; R)` is projective, the
Kronecker map `Hⁿ⁺¹(X; R, M) →ₗ[k] (Hₙ₊₁(X; R) ⟶ M)` is bijective, for every module `M`. The
`Ext¹(Hₙ(X; R), M)` term of the universal coefficient sequence vanishes.

```lean
TopCat.singularKronecker_bijective_succ_of_projective_homology.{w} {k : Type w} [CommRing k]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1] (X : TopCat)
  (R M : ModuleCat k) [Module.Projective k ↑R] (n : ℕ)
  [CategoryTheory.Projective
      (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj R).obj X)] :
  Function.Bijective ⇑(X.singularKronecker k (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem above a projective homology object](../../algebra/part-02/homology/the-universal-coefficient-theorem-above-a-projec.md)

## Lean

Formalized in Tau Ceti as [`TopCat.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_succ_of_projective_homology).

## Sources

- [Tau Ceti documentation: `TopCat.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_succ_of_projective_homology)
- [Source of `TopCat.singularKronecker_bijective_succ_of_projective_homology` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean#L313)
