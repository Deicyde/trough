---
declaration: theorem
origin: cited
lean: Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff
statement: formalized
proof: formalized
---

# Pointed Millington criterion

Two coset representations on `β` are conjugate by a
permutation carrying the base point `e₁ ⟦1⟧` to `e₂ ⟦1⟧` if and only if the subgroups are equal.

```lean
Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff.{u_1, u_3} {G : Type u_1}
  {β : Type u_3} [Group G] {H₁ H₂ : Subgroup G} (e₁ : G ⧸ H₁ ≃ β) (e₂ : G ⧸ H₂ ≃ β) :
  (∃ τ,
      τ (e₁ ↑1) = e₂ ↑1 ∧
        (MulEquiv.toMonoidHom (MulAut.conj τ)).comp e₁.permutationRepresentation =
          e₂.permutationRepresentation) ↔
    H₁ = H₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/CosetRepresentation.html#Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff).

## Sources

- [Tau Ceti documentation: `Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/CosetRepresentation.html#Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff)
- [Source of `Equiv.exists_conj_permutationRepresentation_quotient_apply_eq_iff` in TauCeti/Algebra/GroupAction/CosetRepresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/GroupAction/CosetRepresentation.lean#L337)
