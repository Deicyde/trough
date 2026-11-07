---
declaration: def
origin: cited
lean: TauCeti.Peripheral.exponent
statement: formalized
---

# TauCeti.Peripheral.exponent

The unique common unit exponent of a peripheral automorphism of a marked free
pro-`p` group of positive rank.

```lean
TauCeti.Peripheral.exponent.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r)) (hr : 0 < r) :
  ↥(TauCeti.Peripheral.peripheralAut hF (TauCeti.Peripheral.basis e)) →* ℤ_[p]ˣ
```

## Depends on

- [TauCeti.Peripheral.peripheralAut](tauceti-peripheral-peripheralaut.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exponent`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.html#TauCeti.Peripheral.exponent).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exponent`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.html#TauCeti.Peripheral.exponent)
- [Source of `TauCeti.Peripheral.exponent` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Group.lean#L113)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
