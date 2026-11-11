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
- [Source of `TauCeti.Peripheral.IsPeripheralPermAut.unique` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Permutation.lean#L215)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
