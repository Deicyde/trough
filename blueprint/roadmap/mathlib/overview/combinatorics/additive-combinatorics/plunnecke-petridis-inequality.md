# Plünnecke-Petridis inequality

Mathlib states this as `Finset.pluennecke_petridis_inequality_add`.

```lean
Finset.pluennecke_petridis_inequality_add.{u_1} {G : Type u_1} [DecidableEq G] [AddGroup G]
  {A B : Finset G} (C : Finset G) (hA : ∀ A' ⊆ A, (A + B).card * A'.card ≤ (A' + B).card * A.card) :
  (C + A + B).card * A.card ≤ (A + B).card * (C + A).card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Finset.pluennecke_petridis_inequality_add`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.html#Finset.pluennecke_petridis_inequality_add)
- [Source of `Finset.pluennecke_petridis_inequality_add` in Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/PluenneckeRuzsa.lean#L121)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L547)
