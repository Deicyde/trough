---
declaration: def
origin: cited
lean: TopPair.singularCohomologyDualEquiv, TopPair.singularKronecker_bijective_succ_of_projective_homology, TopPair.singularKronecker_bijective_of_projective_homology_lt, TopPair.singularKronecker_bijective_of_projective_homology
statement: formalized
---

# The relative universal coefficient theorem over a field

the relative singular cohomology
of a pair with coefficients in a field `k` is the dual of its relative singular homology,
`Hⁿ(X, A; k) ≃ₗ[k] Module.Dual k (Hₙ(X, A; k))`.  It sends a class to the linear form underlying
its relative Kronecker pairing (`TopPair.singularCohomologyDualEquiv_apply`).

```lean
TopPair.singularCohomologyDualEquiv.{w} {k : Type w} [Field k] (P : TopPair) (n : ℕ) :
  ↑(P.singularCohomology (↧k) k (↧k) n) ≃ₗ[k] Module.Dual k ↑(P.singularHomology (↧k) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem with projective homology](../../algebra/homology/the-universal-coefficient-theorem-with-projectiv.md)

## Lean

Formalized in Tau Ceti as [`TopPair.singularCohomologyDualEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.html#TopPair.singularCohomologyDualEquiv).

## Other forms

**The relative universal coefficient theorem above a projective homology module, over a hereditary commutative ring.** Formalized in Tau Ceti as [`TopPair.singularKronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_succ_of_projective_homology).

```lean
TopPair.singularKronecker_bijective_succ_of_projective_homology.{w, u_1} {k : Type u_1} [CommRing k]
  (P : TopPair) (R M : ModuleCat k) [Module.Projective k ↑R]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1]
  [CategoryTheory.Linear k (ModuleCat k)] (n : ℕ)
  [CategoryTheory.Projective (P.singularHomology R n)] :
  Function.Bijective ⇑(P.singularKronecker k (n + 1))
```

**The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`.** Formalized in Tau Ceti as [`TopPair.singularKronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_of_projective_homology_lt).

```lean
TopPair.singularKronecker_bijective_of_projective_homology_lt.{w, u_1} {k : Type u_1} [CommRing k]
  (P : TopPair) (R M : ModuleCat k) [Module.Projective k ↑R] [CategoryTheory.Linear k (ModuleCat k)]
  (n : ℕ) (h : ∀ j < n, CategoryTheory.Projective (P.singularHomology R j)) :
  Function.Bijective ⇑(P.singularKronecker k n)
```

**The relative universal coefficient theorem with projective homology, over any commutative ring `k`.** Formalized in Tau Ceti as [`TopPair.singularKronecker_bijective_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient.html#TopPair.singularKronecker_bijective_of_projective_homology).

```lean
TopPair.singularKronecker_bijective_of_projective_homology.{w, u_1} {k : Type u_1} [CommRing k]
  (P : TopPair) (R M : ModuleCat k) [Module.Projective k ↑R]
  [hP : ∀ (n : ℕ), CategoryTheory.Projective (P.singularHomology R n)]
  [CategoryTheory.Linear k (ModuleCat k)] (n : ℕ) : Function.Bijective ⇑(P.singularKronecker k n)
```

## Sources

- [Tau Ceti documentation: `TopPair.singularCohomologyDualEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.html#TopPair.singularCohomologyDualEquiv)
- [Source of `TopPair.singularCohomologyDualEquiv` in TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cohomology/UniversalCoefficient/Field.lean#L125)
