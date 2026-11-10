---
declaration: theorem
origin: cited
lean: TauCeti.Place.map_residue_eq_of_valuation_lt_one
statement: formalized
proof: formalized
---

# Kummer's theorem sees one factor per place

a place `P'` over `P` at which two monic
polynomials with irreducible reductions both vanish reduces them to the same irreducible
polynomial, namely the minimal polynomial of the residue of `y`.  This is what makes the places
attached to distinct irreducible factors of the reduction of `φ` distinct (Stichtenoth,
Theorem 3.3.7).

```lean
TauCeti.Place.map_residue_eq_of_valuation_lt_one.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] {P : TauCeti.Place k F} {P' : TauCeti.Place k' F'}
  (hres : TauCeti.Place.restrict k F P' = P) {y : F'} (hy : y ∈ P'.integers)
  {g₁ g₂ : Polynomial ↥P.integers} (hg₁ : g₁.Monic)
  (hirr₁ : Irreducible (Polynomial.map (IsLocalRing.residue ↥P.integers) g₁))
  (hv₁ : P'.valuation ((P.integersEval y) g₁) < 1) (hg₂ : g₂.Monic)
  (hirr₂ : Irreducible (Polynomial.map (IsLocalRing.residue ↥P.integers) g₂))
  (hv₂ : P'.valuation ((P.integersEval y) g₂) < 1) :
  Polynomial.map (IsLocalRing.residue ↥P.integers) g₁ =
    Polynomial.map (IsLocalRing.residue ↥P.integers) g₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.map_residue_eq_of_valuation_lt_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.map_residue_eq_of_valuation_lt_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.map_residue_eq_of_valuation_lt_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.map_residue_eq_of_valuation_lt_one)
- [Source of `TauCeti.Place.map_residue_eq_of_valuation_lt_one` in TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean#L278)
