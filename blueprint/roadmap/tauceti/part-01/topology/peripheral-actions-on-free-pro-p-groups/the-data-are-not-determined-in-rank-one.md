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

## Proof depends on

- [Burnside's basis theorem, cardinal form](../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one)
- [Source of `TauCeti.Peripheral.exists_isPeripheralPermAut_swap_rank_one` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean#L280)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
