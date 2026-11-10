---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.forall_mem_level_iff
statement: formalized
proof: formalized
---

# TauCeti.Peripheral.forall_mem_level_iff

A pair of conjugators lies in every peripheral level exactly when its defect is trivial: in
a pro-`p` group the terms of the closed lower central series have trivial intersection.

```lean
TauCeti.Peripheral.forall_mem_level_iff.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (x : Fin r → F) (u : ℤ_[p])
  (cd : (Fin r → F) × F) :
  (∀ (n : ℕ), cd ∈ TauCeti.Peripheral.level hF x u n) ↔
    TauCeti.Peripheral.defect hF x u cd.1 cd.2 = 1
```

## Depends on

- [TauCeti.Peripheral.level](tauceti-peripheral-level.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.forall_mem_level_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.forall_mem_level_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.forall_mem_level_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.forall_mem_level_iff)
- [Source of `TauCeti.Peripheral.forall_mem_level_iff` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean#L114)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
