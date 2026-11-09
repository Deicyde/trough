---
declaration: def
origin: cited
lean: TauCeti.Peripheral.peripheralAut
statement: formalized
---

# TauCeti.Peripheral.peripheralAut

The continuous automorphisms peripheral for `x` with some common unit exponent.

```lean
TauCeti.Peripheral.peripheralAut.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (x : Fin r → F) : Subgroup (TauCeti.ContinuousAut F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.html#TauCeti.Peripheral.peripheralAut).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.html#TauCeti.Peripheral.peripheralAut)
- [Source of `TauCeti.Peripheral.peripheralAut` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean#L70)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
