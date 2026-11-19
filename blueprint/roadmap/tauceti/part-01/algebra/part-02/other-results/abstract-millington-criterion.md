---
declaration: theorem
origin: cited
lean: Equiv.exists_conj_permutationRepresentation_quotient_iff
statement: formalized
proof: formalized
---

# Abstract Millington criterion

For any two subgroups `H₁, H₂` of `G` and bijections
`e₁ : G ⧸ H₁ ≃ β` and `e₂ : G ⧸ H₂ ≃ β`, the coset permutation representations read through `e₁`
and `e₂` are conjugate in `Equiv.Perm β` if and only if `H₁` and `H₂` are conjugate in `G`.

```lean
Equiv.exists_conj_permutationRepresentation_quotient_iff.{u_1, u_3} {G : Type u_1} {β : Type u_3}
  [Group G] {H₁ H₂ : Subgroup G} (e₁ : G ⧸ H₁ ≃ β) (e₂ : G ⧸ H₂ ≃ β) :
  (∃ τ,
      (MulEquiv.toMonoidHom (MulAut.conj τ)).comp e₁.permutationRepresentation =
        e₂.permutationRepresentation) ↔
    ∃ g, g • H₁ = H₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Equiv.exists_conj_permutationRepresentation_quotient_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/CosetRepresentation.html#Equiv.exists_conj_permutationRepresentation_quotient_iff).

## Sources

- [Tau Ceti documentation: `Equiv.exists_conj_permutationRepresentation_quotient_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/CosetRepresentation.html#Equiv.exists_conj_permutationRepresentation_quotient_iff)
- [Source of `Equiv.exists_conj_permutationRepresentation_quotient_iff` in TauCeti/Algebra/GroupAction/CosetRepresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/GroupAction/CosetRepresentation.lean#L304)
