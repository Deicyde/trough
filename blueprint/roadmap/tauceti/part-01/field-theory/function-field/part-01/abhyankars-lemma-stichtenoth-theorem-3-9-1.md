---
declaration: theorem
origin: cited
lean: TauCeti.Place.ramificationIdx_restrict_sup, TauCeti.Place.ramificationIdx_restrict_sup_of_isGalois
statement: formalized
proof: formalized
---

# Abhyankar's lemma (Stichtenoth, Theorem 3.9.1)

Let `E₁` and `E₂` be intermediate fields
of a finite separable extension `F' / F` of function fields, and `P'` a place of `F'` such that
the residue field of the place `P` below it in `F` is perfect, for instance because `k` is perfect
(`TauCeti.Place.perfectField_residueField`). If the ramification index of `P' ∩ E₁` over `P` is
nonzero in `k`, then the ramification index of `P' ∩ E₁ E₂` over `P` is the least common multiple
of those of `P' ∩ E₁` and `P' ∩ E₂`.

In particular, if `P' ∩ E₁` and `P' ∩ E₂` have ramification index `1` over `P`, then so does
`P' ∩ E₁ E₂`.

```lean
TauCeti.Place.ramificationIdx_restrict_sup.{u, v, w} {k : Type u} {F : Type v} {F' : Type w}
  [Field k] [Field F] [Field F'] [Algebra k F] [Algebra k F'] [Algebra F F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] (hF : TauCeti.IsFunctionField k F)
  (P' : TauCeti.Place k F') [PerfectField (TauCeti.Place.restrict k F P').ResidueField]
  (E₁ E₂ : IntermediateField F F')
  (h₁ : ↑(TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₁) P')) ≠ 0) :
  TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥(E₁ ⊔ E₂)) P') =
    (TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₁) P')).lcm
      (TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₂) P'))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental identity](the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Galois correspondence for the inertia field](the-galois-correspondence-for-the-inertia-field.md)
- [The residue action, on residues (Stichtenoth, Theorem 3.8.2)](the-residue-action-on-residues-stichtenoth-theor.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.ramificationIdx_restrict_sup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Abhyankar.html#TauCeti.Place.ramificationIdx_restrict_sup).

## Other forms

**Abhyankar's lemma in a Galois extension (Stichtenoth, Theorem 3.9.1).** Formalized in Tau Ceti as [`TauCeti.Place.ramificationIdx_restrict_sup_of_isGalois`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Abhyankar.html#TauCeti.Place.ramificationIdx_restrict_sup_of_isGalois).

```lean
TauCeti.Place.ramificationIdx_restrict_sup_of_isGalois.{u, v, w} {k : Type u} {F : Type v}
  {F' : Type w} [Field k] [Field F] [Field F'] [Algebra k F] [Algebra k F'] [Algebra F F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [IsGalois F F'] (Q : TauCeti.Place k F')
  [Algebra.IsSeparable (TauCeti.Place.restrict k F Q).ResidueField Q.ResidueField]
  (E₁ E₂ : IntermediateField F F')
  (h₁ : ↑(TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₁) Q)) ≠ 0) :
  TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥(E₁ ⊔ E₂)) Q) =
    (TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₁) Q)).lcm
      (TauCeti.Place.ramificationIdx F (TauCeti.Place.restrict k (↥E₂) Q))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.ramificationIdx_restrict_sup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Abhyankar.html#TauCeti.Place.ramificationIdx_restrict_sup)
- [Source of `TauCeti.Place.ramificationIdx_restrict_sup` in TauCeti/FieldTheory/FunctionField/Place/Extension/Abhyankar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Place/Extension/Abhyankar.lean#L133)
