---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.not_exists_peripheral_identity_two
statement: formalized
proof: formalized
---

# TauCeti.Peripheral.not\_exists\_peripheral\_identity\_two

At exponent `2`, no normalized peripheral product in a rank-two free pro-`2` group is
trivial even modulo the second closed lower-central-series term.

```lean
TauCeti.Peripheral.not_exists_peripheral_identity_two.{u_1} {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP 2 F) (e : F ≃ₜ* TauCeti.freeProP 2 (Fin 2)) :
  ¬∃ c d,
      hF.padicPow (TauCeti.Peripheral.basis e 0) 2 *
            (c⁻¹ * hF.padicPow (TauCeti.Peripheral.basis e 1) 2 * c) *
          (d⁻¹ * hF.padicPow (TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e)) 2 * d) ∈
        TauCeti.closedLowerCentralSeries F 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Peripheral.level](tauceti-peripheral-level.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.not_exists_peripheral_identity_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Nonunit.html#TauCeti.Peripheral.not_exists_peripheral_identity_two).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.not_exists_peripheral_identity_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Nonunit.html#TauCeti.Peripheral.not_exists_peripheral_identity_two)
- [Source of `TauCeti.Peripheral.not_exists_peripheral_identity_two` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Nonunit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Nonunit.lean#L79)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
