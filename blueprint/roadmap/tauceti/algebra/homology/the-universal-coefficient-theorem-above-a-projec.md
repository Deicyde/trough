---
declaration: theorem
origin: cited
lean: TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology
statement: formalized
proof: formalized
---

# The universal coefficient theorem above a projective homology object

**The universal coefficient theorem above a projective homology object**, when every object
has projective dimension at most one, as for modules over a principal ideal domain: for a chain
complex `X` indexed by `ℕ` with projective terms whose homology `Hₙ(X)` is projective, the
Kronecker map `Hⁿ⁺¹(Hom(X, Y)) →ₗ[k] (Hₙ₊₁(X) ⟶ Y)` is bijective, for every object `Y`. Nothing
is assumed about the homology in the other degrees.

```lean
TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology.{v_1, u_1, u_3} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Abelian C] {k : Type u_3} [CommRing k]
  [CategoryTheory.Linear k C] [∀ (V : C), CategoryTheory.HasProjectiveDimensionLE V 1]
  {X : ChainComplex C ℕ} {Y : C} [∀ (n : ℕ), CategoryTheory.Projective (X.X n)] (n : ℕ)
  [CategoryTheory.Projective (HomologicalComplex.homology X n)] :
  Function.Bijective ⇑(TauCeti.ChainComplex.kronecker k X Y (n + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The universal coefficient theorem with projective homology](the-universal-coefficient-theorem-with-projectiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology).

## Sources

- [Tau Ceti documentation: `TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.html#TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology)
- [Source of `TauCeti.ChainComplex.kronecker_bijective_succ_of_projective_homology` in TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/UniversalCoefficient/Basic.lean#L272)
