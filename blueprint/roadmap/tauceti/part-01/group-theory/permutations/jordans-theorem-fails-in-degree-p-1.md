---
declaration: theorem
origin: cited
lean: TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq
statement: formalized
proof: formalized
---

# Jordan's theorem fails in degree `p + 1`

A primitive permutation group of degree `n`
containing a cycle of prime length `p` need not contain the alternating group when `p + 1 = n`:
the affine group `AGL(1, 8)` of the field with eight elements is primitive on eight points and
contains a `7`-cycle. This shows that the bound `p + 3 ≤ n` of
`TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem` cannot be weakened to
`p + 1 ≤ n`.

```lean
TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq :
  ¬∀ (α : Type) [inst : Fintype α] [inst_1 : DecidableEq α] (G : Subgroup (Equiv.Perm α)),
      MulAction.IsPreprimitive (↥G) α →
        ∀ g ∈ G,
          g.IsCycle →
            Nat.Prime g.support.card → g.support.card + 1 = Nat.card α → alternatingGroup α ≤ G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/Jordan/Counterexamples.html#TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/Jordan/Counterexamples.html#TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq)
- [Source of `TauCeti.not_forall_alternatingGroup_le_of_isPreprimitive_of_isCycle_mem_of_card_support_add_one_eq` in TauCeti/GroupTheory/Perm/Jordan/Counterexamples.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Perm/Jordan/Counterexamples.lean#L68)
