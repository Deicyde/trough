---
declaration: theorem
origin: cited
lean: TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup
statement: formalized
proof: formalized
---

# The key step of Tits's theorem on normal subgroups

If `H` is normal, a simple reflection
whose Bruhat cell lies in `H ⊔ B` commutes with every simple reflection whose cell does not.

```lean
TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) {H : Subgroup G} [H.Normal] {s t : T.WeylGroup} (hs : s ∈ T.simple)
  (ht : t ∈ T.simple) (hsH : T.bruhatCell s ⊆ ↑(H ⊔ T.subgroupB))
  (htH : ¬T.bruhatCell t ⊆ ↑(H ⊔ T.subgroupB)) : s * t = t * s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup).

## Sources

- [Tau Ceti documentation: `TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup)
- [Source of `TauCeti.TitsSystem.simple_mul_comm_of_bruhatCell_subset_sup` in TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean#L71)
