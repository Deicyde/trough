---
declaration: theorem
origin: cited
lean: TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt
statement: formalized
proof: formalized
---

# The universal coefficient theorem below the first non-projective homology

for a chain
complex `X` indexed by `ℕ` with projective terms whose homology objects are projective below
degree `n`, the Kronecker map `Hⁿ(Hom(X, Y)) →ₗ[k] (Hₙ(X) ⟶ Y)` is bijective, for every object
`Y`. In particular this holds when `X` is exact below degree `n`.

```lean
TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt.{v_1, u_1, u_3} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {k : Type u_3} [CommRing k]
  [CategoryTheory.Linear k C] {X : ChainComplex C ℕ} {Y : C}
  [∀ (n : ℕ), CategoryTheory.Projective (X.X n)] (n : ℕ)
  (h : ∀ j < n, CategoryTheory.Projective (HomologicalComplex.homology X j)) :
  Function.Bijective ⇑(TauCeti.ChainComplex.kronecker k X Y n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem with projective homology](the-universal-coefficient-theorem-with-projectiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt)
- [Source of `TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_lt` in TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean#L240)
