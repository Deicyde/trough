---
declaration: theorem
origin: cited
lean: TauCeti.ChainComplex.kronecker_bijective_of_projective_homology, TauCeti.ChainComplex.kronecker_bijective, TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_of_add_one_eq
statement: formalized
proof: formalized
---

# The universal coefficient theorem with projective homology

for a chain complex `X`
indexed by `ℕ` whose terms and homology objects are all projective, the Kronecker map
`Hⁿ(Hom(X, Y)) →ₗ[k] (Hₙ(X) ⟶ Y)` is bijective in every degree, for every object `Y`.

```lean
TauCeti.ChainComplex.kronecker_bijective_of_projective_homology.{v_1, u_1, u_3} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {k : Type u_3} [CommRing k]
  [CategoryTheory.Linear k C] {X : ChainComplex C ℕ} {Y : C}
  [∀ (n : ℕ), CategoryTheory.Projective (X.X n)]
  [∀ (n : ℕ), CategoryTheory.Projective (HomologicalComplex.homology X n)] (n : ℕ) :
  Function.Bijective ⇑(TauCeti.ChainComplex.kronecker k X Y n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [The universal coefficient theorem below the first non-projective homology](the-universal-coefficient-theorem-below-the-firs.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ChainComplex.kronecker_bijective_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_of_projective_homology).

## Other forms

**The universal coefficient theorem for injective coefficients.** Formalized in Tau Ceti as [`TauCeti.ChainComplex.kronecker_bijective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Kronecker.html#TauCeti.ChainComplex.kronecker_bijective).

```lean
TauCeti.ChainComplex.kronecker_bijective.{v_1, u_1, u_2, u_3} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {α : Type u_2}
  [AddRightCancelSemigroup α] [One α] {k : Type u_3} [Ring k] [CategoryTheory.Linear k C]
  {X : ChainComplex C α} {Y : C} [CategoryTheory.Injective Y] (i : α) :
  Function.Bijective ⇑(TauCeti.ChainComplex.kronecker k X Y i)
```

**The universal coefficient theorem in one degree with projective homology below it.** Formalized in Tau Ceti as [`TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_of_add_one_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_of_add_one_eq).

```lean
TauCeti.ChainComplex.kronecker_bijective_of_projective_homology_of_add_one_eq.{v_1, u_1, u_2, u_3}
  {C : Type u_1} [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {α : Type u_2}
  [AddRightCancelSemigroup α] [One α] {k : Type u_3} [CommRing k] [CategoryTheory.Linear k C]
  {X : ChainComplex C α} {Y : C} {i j : α} (hij : j + 1 = i)
  [CategoryTheory.Projective (HomologicalComplex.cycles X j)]
  [CategoryTheory.IsSplitMono (HomologicalComplex.iCycles X j)]
  [CategoryTheory.IsSplitMono (HomologicalComplex.iCycles X i)]
  [CategoryTheory.Projective (HomologicalComplex.homology X j)] :
  Function.Bijective ⇑(TauCeti.ChainComplex.kronecker k X Y i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ChainComplex.kronecker_bijective_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_of_projective_homology)
- [Source of `TauCeti.ChainComplex.kronecker_bijective_of_projective_homology` in TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean#L258)
