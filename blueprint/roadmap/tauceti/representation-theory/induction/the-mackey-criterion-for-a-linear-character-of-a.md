---
declaration: theorem
origin: cited
lean: TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv
statement: formalized
proof: formalized
---

# The Mackey criterion for a linear character of an inverted subgroup of index two

the
induced representation is irreducible exactly when some value of `χ` is not a square root of `1`.
Conjugation by any element outside `N` inverts it, by
`TauCeti.conj_eq_inv_of_notMem_of_index_two`, so `{}^s χ = χ⁻¹` for every such `s` and the
criterion becomes the single condition `χ ≠ χ⁻¹`.  The inversion hypothesis is asked of the one
outside element `s` only.

```lean
TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv.{u} {k G : Type u} [Field k] [Group G]
  {N : Subgroup G} [Finite G] [IsAlgClosed k] [CharZero k] (hindex : N.index = 2) {s : G}
  (hs : s ∉ N) (hinv : ∀ x ∈ N, s * x * s⁻¹ = x⁻¹) (χ : ↥N →* kˣ) :
  CategoryTheory.Simple (TauCeti.indFDRep (FDRep.ofLinearCharacter χ)) ↔ ∃ x, χ x ^ 2 ≠ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mackey irreducibility criterion](the-mackey-irreducibility-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/LinearCharacter.html#TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Mackey/LinearCharacter.html#TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv)
- [Source of `TauCeti.simple_indFDRep_ofLinearCharacter_iff_of_conj_eq_inv` in TauCeti/RepresentationTheory/Induction/Mackey/LinearCharacter.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Mackey/LinearCharacter.lean#L127)
