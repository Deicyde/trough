---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one
statement: formalized
proof: formalized
---

# The data are not determined in rank one

In rank one the peripheral tuple is `(x, x⁻¹)`,
and an automorphism with `x ↦ x ^ u` is peripheral both for the trivial permutation with
exponent `u` and for the transposition with exponent `-u`.

```lean
TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {F : Type u_1} [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin 1))
  (u : ℤ_[p]ˣ) :
  ∃ φ,
    TauCeti.Peripheral.IsPeripheralPermAut hF (TauCeti.Peripheral.basis e) 1 u φ ∧
      TauCeti.Peripheral.IsPeripheralPermAut hF (TauCeti.Peripheral.basis e) (Equiv.swap 0 1) (-u) φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one)
- [Source of `TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean#L280)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
