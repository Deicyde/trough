---
declaration: theorem
origin: cited
lean: TopPair.singularKronecker_bijective_of_projective_homology_lt
statement: formalized
proof: formalized
---

# The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`

for a projective coefficient module `R`, if the relative singular
homology modules `Hⱼ(X, A; R)` of a pair are projective for `j < n`, for instance zero, the
relative Kronecker map `Hⁿ(X, A; R, M) →ₗ[k] (Hₙ(X, A; R) ⟶ M)` is bijective, for every module
`M`.

```lean
TopPair.singularKronecker_bijective_of_projective_homology_lt.{w, u_1} {k : Type u_1} [CommRing k]
  (P : TopPair) (R M : ModuleCat k) [Module.Projective k ↑R] [CategoryTheory.Linear k (ModuleCat k)]
  (n : ℕ) (h : ∀ j < n, CategoryTheory.Projective (P.singularHomology R j)) :
  Function.Bijective ⇑(P.singularKronecker k n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem below the first non-projective homology](../../algebra/part-02/homology/the-universal-coefficient-theorem-below-the-firs.md)

## Lean

Formalized in Tau Ceti as [`TopPair.singularKronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_of_projective_homology_lt).

## Sources

- [Tau Ceti documentation: `TopPair.singularKronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_of_projective_homology_lt)
- [Source of `TopPair.singularKronecker_bijective_of_projective_homology_lt` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean#L348)
