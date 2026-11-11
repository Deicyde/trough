---
declaration: theorem
origin: cited
lean: TopCat.singularKronecker_bijective_of_projective_homology_lt
statement: formalized
proof: formalized
---

# The universal coefficient theorem below the first non-projective homology, over any commutative ring `k`

for a projective coefficient module `R`, if the singular homology modules
`Hⱼ(X; R)` are projective for `j < n`, the Kronecker map `Hⁿ(X; R, M) →ₗ[k] (Hₙ(X; R) ⟶ M)` is
bijective, for every module `M`. For `n = 1` the hypothesis is that `H₀(X; R)` is projective, which
holds for free `R` (`ModuleCat.free_singularHomology_zero`).

```lean
TopCat.singularKronecker_bijective_of_projective_homology_lt.{w} {k : Type w} [CommRing k]
  (X : TopCat) {R : ModuleCat k} [Module.Projective k ↑R] (M : ModuleCat k) (n : ℕ)
  (h :
    ∀ j < n,
      CategoryTheory.Projective
        (((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) j).obj R).obj X)) :
  Function.Bijective ⇑(X.singularKronecker k n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem below the first non-projective homology](../../algebra/part-02/homology/the-universal-coefficient-theorem-below-the-firs.md)

## Lean

Formalized in Tau Ceti as [`TopCat.singularKronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_of_projective_homology_lt).

## Sources

- [Tau Ceti documentation: `TopCat.singularKronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopCat.singularKronecker_bijective_of_projective_homology_lt)
- [Source of `TopCat.singularKronecker_bijective_of_projective_homology_lt` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean#L114)
