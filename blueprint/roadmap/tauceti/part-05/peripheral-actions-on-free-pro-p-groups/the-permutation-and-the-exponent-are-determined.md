---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.IsPeripheralPermAut.unique
statement: formalized
proof: formalized
---

# The permutation and the exponent are determined in rank at least two

For the basis of a
free pro-`p` group of rank `r ≥ 2`, an automorphism peripheral for `(σ, u)` and for `(σ', u')`
has `σ = σ'` and `u = u'`.

```lean
TauCeti.Peripheral.IsPeripheralPermAut.unique.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] {hF : TauCeti.IsProP p F} {e : F ≃ₜ* TauCeti.freeProP p (Fin r)}
  (hr : 2 ≤ r) {σ σ' : Equiv.Perm (Fin (r + 1))} {u u' : ℤ_[p]ˣ} {φ : TauCeti.ContinuousAut F}
  (h : TauCeti.Peripheral.IsPeripheralPermAut hF (TauCeti.Peripheral.basis e) σ u φ)
  (h' : TauCeti.Peripheral.IsPeripheralPermAut hF (TauCeti.Peripheral.basis e) σ' u' φ) :
  σ = σ' ∧ u = u'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.IsPeripheralPermAut.unique`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.IsPeripheralPermAut.unique).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.IsPeripheralPermAut.unique`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.html#TauCeti.Peripheral.IsPeripheralPermAut.unique)
- [Source of `TauCeti.Peripheral.IsPeripheralPermAut.unique` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean#L215)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
