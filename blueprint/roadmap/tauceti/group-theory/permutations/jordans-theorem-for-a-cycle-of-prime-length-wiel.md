---
declaration: theorem
origin: cited
lean: TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem
statement: formalized
proof: formalized
---

# Jordan's theorem for a cycle of prime length (Wielandt, Theorem 13.9)

A primitive
permutation group of degree at least `p + 3` that contains a cycle of prime length `p` contains
the alternating group.

```lean
TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem.{u_1} {α : Type u_1} [Fintype α]
  [DecidableEq α] {G : Subgroup (Equiv.Perm α)} (hG : MulAction.IsPreprimitive (↥G) α) {p : ℕ}
  (hp : Nat.Prime p) (hp' : p + 3 ≤ Nat.card α) {g : Equiv.Perm α} (hgc : g.IsCycle)
  (hgp : g.support.card = p) (hg : g ∈ G) : alternatingGroup α ≤ G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/Jordan.html#TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/Jordan.html#TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem)
- [Source of `TauCeti.alternatingGroup_le_of_isPreprimitive_of_isCycle_mem` in TauCeti/GroupTheory/Perm/Jordan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Perm/Jordan.lean#L153)
