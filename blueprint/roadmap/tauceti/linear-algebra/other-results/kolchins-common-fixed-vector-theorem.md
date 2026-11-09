---
declaration: theorem
origin: cited
lean: Representation.exists_common_fixed_vector_of_isUnipotent
statement: formalized
proof: formalized
---

# Kolchin's common fixed vector theorem

If every element of a monoid acts unipotently on a
nonzero finite-dimensional vector space over a field, then the monoid fixes a nonzero vector.

```lean
Representation.exists_common_fixed_vector_of_isUnipotent.{u, v, w} {K : Type u} {G : Type w}
  {V : Type v} [Field K] [Monoid G] [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V]
  [Nontrivial V] (ρ : Representation K G V) (hunipotent : ∀ (g : G), IsNilpotent (ρ g - 1)) :
  ∃ v, v ≠ 0 ∧ ∀ (g : G), (ρ g) v = v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside density theorem](../../representation-theory/other-results/burnside-density-theorem.md)

## Lean

Formalized in Tau Ceti as [`Representation.exists_common_fixed_vector_of_isUnipotent`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Eigenspace/JointEigenvector/Kolchin.html#Representation.exists_common_fixed_vector_of_isUnipotent).

## Sources

- [Tau Ceti documentation: `Representation.exists_common_fixed_vector_of_isUnipotent`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Eigenspace/JointEigenvector/Kolchin.html#Representation.exists_common_fixed_vector_of_isUnipotent)
- [Source of `Representation.exists_common_fixed_vector_of_isUnipotent` in TauCeti/LinearAlgebra/Eigenspace/JointEigenvector/Kolchin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Eigenspace/JointEigenvector/Kolchin.lean#L108)
