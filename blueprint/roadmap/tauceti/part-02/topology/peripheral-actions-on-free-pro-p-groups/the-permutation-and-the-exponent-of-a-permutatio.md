---
declaration: def
origin: cited
lean: TauCeti.Peripheral.permData
statement: formalized
---

# The permutation and the exponent of a permutation-peripheral automorphism

**The permutation and the exponent of a permutation-peripheral automorphism**, for the basis
of a free pro-`p` group of rank at least two, as a homomorphism.

```lean
TauCeti.Peripheral.permData.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r)) (hr : 2 ≤ r) :
  ↥(TauCeti.Peripheral.peripheralPermAut hF (TauCeti.Peripheral.basis e)) →*
    Equiv.Perm (Fin (r + 1)) × ℤ_[p]ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The permutation and the exponent are determined in rank at least two](the-permutation-and-the-exponent-are-determined.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.permData`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.permData).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.permData`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.permData)
- [Source of `TauCeti.Peripheral.permData` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean#L242)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PeripheralActions/STATUS.md)
