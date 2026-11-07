---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.continuous_exponent
statement: formalized
proof: formalized
---

# The exponent character is continuous

Its graph is closed, being the peripheral graph of
the basis, and its target `ℤ_[p]ˣ` is compact.

```lean
TauCeti.Peripheral.continuous_exponent.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r)) (hr : 0 < r) :
  Continuous ⇑(TauCeti.Peripheral.exponent hF e hr)
```

## Depends on

- [TauCeti.Peripheral.exponent](tauceti-peripheral-exponent.md)
- [TauCeti.Peripheral.peripheralAut](tauceti-peripheral-peripheralaut.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.continuous_exponent`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.html#TauCeti.Peripheral.continuous_exponent).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.continuous_exponent`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.html#TauCeti.Peripheral.continuous_exponent)
- [Source of `TauCeti.Peripheral.continuous_exponent` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Topology.lean#L139)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
