---
declaration: theorem
origin: cited
lean: TauCeti.simple_indFDRep_iff_doubleCoset, TauCeti.simple_indFDRep_iff_of_normal, TauCeti.simple_indFDRep_ofLinearCharacter_iff, TauCeti.simple_indFDRep_iff
statement: formalized
proof: formalized
---

# The Mackey irreducibility criterion

The representation induced from `A` is irreducible
exactly when `A` is irreducible and every double coset `HsH` other than `H` itself, read at its
chosen representative, is Mackey disjoint. Algebraic closure supplies scalar Schur.

```lean
TauCeti.simple_indFDRep_iff_doubleCoset.{u} {k G : Type u} [Field k] [Group G] [Finite G]
  [IsAlgClosed k] [NeZero ↑(Nat.card G)] {H : Subgroup G} (A : FDRep k ↥H) :
  CategoryTheory.Simple (TauCeti.indFDRep A) ↔
    CategoryTheory.Simple A ∧
      ∀ (D : DoubleCoset.Quotient ↑H ↑H),
        D ≠ DoubleCoset.mk H H 1 → TauCeti.MackeyDisjoint A (Quotient.out D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.simple_indFDRep_iff_doubleCoset`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Split.html#TauCeti.simple_indFDRep_iff_doubleCoset).

## Other forms

**The Mackey irreducibility criterion for a normal subgroup.** Formalized in Tau Ceti as [`TauCeti.simple_indFDRep_iff_of_normal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Split.html#TauCeti.simple_indFDRep_iff_of_normal).

```lean
TauCeti.simple_indFDRep_iff_of_normal.{u} {k G : Type u} [Field k] [Group G] [Finite G]
  [IsAlgClosed k] [NeZero ↑(Nat.card G)] {H : Subgroup G} [H.Normal] (A : FDRep k ↥H) :
  CategoryTheory.Simple (TauCeti.indFDRep A) ↔
    CategoryTheory.Simple A ∧ ∀ s ∉ H, IsEmpty (TauCeti.conjNormalFDRep s A ≅ A)
```

**The Mackey irreducibility criterion for an induced linear character.** Formalized in Tau Ceti as [`TauCeti.simple_indFDRep_ofLinearCharacter_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/LinearCharacter.html#TauCeti.simple_indFDRep_ofLinearCharacter_iff).

```lean
TauCeti.simple_indFDRep_ofLinearCharacter_iff.{u} {k G : Type u} [Field k] [Group G]
  {N : Subgroup G} [N.Normal] [Finite G] [IsAlgClosed k] [NeZero ↑(Nat.card G)] (χ : ↥N →* kˣ) :
  CategoryTheory.Simple (TauCeti.indFDRep (FDRep.ofLinearCharacter χ)) ↔
    ∀ s ∉ N, ∃ x, χ ((MulAut.conjNormal s) x) ≠ χ x
```

**The Mackey irreducibility criterion, elementwise.** Formalized in Tau Ceti as [`TauCeti.simple_indFDRep_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Split.html#TauCeti.simple_indFDRep_iff).

```lean
TauCeti.simple_indFDRep_iff.{u} {k G : Type u} [Field k] [Group G] [Finite G] [IsAlgClosed k]
  [NeZero ↑(Nat.card G)] {H : Subgroup G} (A : FDRep k ↥H) :
  CategoryTheory.Simple (TauCeti.indFDRep A) ↔
    CategoryTheory.Simple A ∧ ∀ s ∉ H, TauCeti.MackeyDisjoint A s
```

## Sources

- [Tau Ceti documentation: `TauCeti.simple_indFDRep_iff_doubleCoset`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/Split.html#TauCeti.simple_indFDRep_iff_doubleCoset)
- [Source of `TauCeti.simple_indFDRep_iff_doubleCoset` in TauCeti/RepresentationTheory/Induction/Mackey/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Mackey/Split.lean#L94)
