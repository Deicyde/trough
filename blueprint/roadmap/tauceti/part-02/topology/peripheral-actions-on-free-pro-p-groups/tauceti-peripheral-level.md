---
declaration: def
origin: cited
lean: TauCeti.Peripheral.level
statement: formalized
---

# TauCeti.Peripheral.level

The `n`-th peripheral level is the set of conjugators whose defect lies in the `n`-th term
of the closed lower central series.

```lean
TauCeti.Peripheral.level.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (x : Fin r → F) (u : ℤ_[p]) (n : ℕ) : Set ((Fin r → F) × F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.level`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.level).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.level`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.level)
- [Source of `TauCeti.Peripheral.level` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean#L89)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PeripheralActions/STATUS.md)
