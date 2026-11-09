---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.peripheralAut_eq_top_rank_one
statement: formalized
proof: formalized
---

# TauCeti.Peripheral.peripheralAut_eq_top_rank_one

In rank one the peripheral automorphism group is the whole group of continuous
automorphisms.

```lean
TauCeti.Peripheral.peripheralAut_eq_top_rank_one.{u_1} {p : ℕ} {F : Type u_1} [Group F]
  [TopologicalSpace F] [Fact (Nat.Prime p)] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin 1)) :
  TauCeti.Peripheral.peripheralAut hF (TauCeti.Peripheral.basis e) = ⊤
```

## Depends on

- [TauCeti.Peripheral.peripheralAut](tauceti-peripheral-peripheralaut.md)

## Proof depends on

- [TauCeti.profiniteFrattini](../profinite-and-pro-p-groups/part-01/tauceti-profinitefrattini.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.peripheralAut_eq_top_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/RankOne.html#TauCeti.Peripheral.peripheralAut_eq_top_rank_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.peripheralAut_eq_top_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/RankOne.html#TauCeti.Peripheral.peripheralAut_eq_top_rank_one)
- [Source of `TauCeti.Peripheral.peripheralAut_eq_top_rank_one` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/RankOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/RankOne.lean#L105)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
