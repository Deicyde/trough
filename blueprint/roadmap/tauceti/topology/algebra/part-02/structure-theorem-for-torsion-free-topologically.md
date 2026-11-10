---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt
statement: formalized
proof: formalized
---

# Structure theorem for torsion-free topologically finitely generated abelian pro-`p` groups

Such a group is topologically isomorphic to `ℤ_p ^ r`.

```lean
TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {A : Type u_1} [CommGroup A] [TopologicalSpace A] [IsTopologicalGroup A] [CompactSpace A]
  [TotallyDisconnectedSpace A] [IsMulTorsionFree A] (hA : TauCeti.IsProP p A)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated A) :
  ∃ r, Nonempty (A ≃ₜ* Multiplicative (Fin r → ℤ_[p]))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Structure theorem for topologically finitely generated abelian pro-`p` groups](../part-01/structure-theorem-for-topologically-finitely-gen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Torsion.html#TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Torsion.html#TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt)
- [Source of `TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt` in TauCeti/Topology/Algebra/Group/Profinite/ProP/Torsion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/Torsion.lean#L136)
