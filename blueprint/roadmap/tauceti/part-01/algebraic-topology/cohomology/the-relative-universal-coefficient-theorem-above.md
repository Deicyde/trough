---
declaration: theorem
origin: cited
lean: TopPair.singularKronecker_bijective_succ_of_projective_homology
statement: formalized
proof: formalized
---

# The relative universal coefficient theorem above a projective homology module, over a hereditary commutative ring

for a projective coefficient module `R`, if `Hₙ(X, A; R)` is
projective, the relative Kronecker map `Hⁿ⁺¹(X, A; R, M) →ₗ[k] (Hₙ₊₁(X, A; R) ⟶ M)` is bijective,
for every module `M`. Nothing is assumed about the relative homology in the other degrees.

```lean
TopPair.singularKronecker_bijective_succ_of_projective_homology.{w, u_1} {k : Type u_1} [CommRing k]
  (P : TopPair) (R M : ModuleCat k) [Module.Projective k ↑R]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1]
  [CategoryTheory.Linear k (ModuleCat k)] (n : ℕ)
  [CategoryTheory.Projective (P.singularHomology R n)] :
  Function.Bijective ⇑(P.singularKronecker k (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem above a projective homology object](../../algebra/part-02/homology/the-universal-coefficient-theorem-above-a-projec.md)

## Lean

Formalized in Tau Ceti as [`TopPair.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_succ_of_projective_homology).

## Sources

- [Tau Ceti documentation: `TopPair.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_succ_of_projective_homology)
- [Source of `TopPair.singularKronecker_bijective_succ_of_projective_homology` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.lean#L375)
