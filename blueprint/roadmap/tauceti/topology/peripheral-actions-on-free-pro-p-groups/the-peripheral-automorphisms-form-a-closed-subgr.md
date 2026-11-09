---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.isClosed_peripheralAut
statement: formalized
proof: formalized
---

# The peripheral automorphisms form a closed subgroup

**The peripheral automorphisms form a closed subgroup** of `ContinuousAut F` for the
congruence topology, when `F` is topologically finitely generated.

```lean
TauCeti.Peripheral.isClosed_peripheralAut.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (x : Fin r → F)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated F) :
  IsClosed ↑(TauCeti.Peripheral.peripheralAut hF x)
```

## Depends on

- [TauCeti.Peripheral.peripheralAut](tauceti-peripheral-peripheralaut.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.isClosed_peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.html#TauCeti.Peripheral.isClosed_peripheralAut).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.isClosed_peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.html#TauCeti.Peripheral.isClosed_peripheralAut)
- [Source of `TauCeti.Peripheral.isClosed_peripheralAut` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.lean#L79)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
