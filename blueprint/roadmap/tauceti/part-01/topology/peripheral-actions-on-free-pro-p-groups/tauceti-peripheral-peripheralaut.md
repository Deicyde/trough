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
- [Source of `TauCeti.Peripheral.peripheralAut` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean#L70)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
