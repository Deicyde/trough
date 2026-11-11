---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod, TauCeti.IsProP.exists_continuousLinearEquiv_pi_padicInt_prod_torsion
statement: formalized
proof: formalized
---

# Structure theorem for topologically finitely generated abelian pro-`p` groups

Such a
group is topologically isomorphic to `ℤ_p ^ r × ∏ i : Fin m, ℤ/p^(e i)` with every `e i`
positive, where the finite factor carries the discrete topology.

```lean
TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {A : Type u_1} [CommGroup A] [TopologicalSpace A] [IsTopologicalGroup A] [CompactSpace A]
  [TotallyDisconnectedSpace A] (hA : TauCeti.IsProP p A)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated A) :
  ∃ r m e,
    (∀ (i : Fin m), 0 < e i) ∧
      Nonempty (A ≃ₜ* Multiplicative ((Fin r → ℤ_[p]) × ((i : Fin m) → ZMod (p ^ e i))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Structure theorem for finitely generated modules over a discrete valuation ring](../../../algebra/part-02/module/structure-theorem-for-finitely-generated-modules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/StructureTheorem.html#TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod).

## Other forms

**Structure theorem for topologically finitely generated abelian pro-`p` groups, as topological `ℤ_[p]`-modules.** Formalized in Tau Ceti as [`TauCeti.IsProP.exists_continuousLinearEquiv_pi_padicInt_prod_torsion`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Torsion.html#TauCeti.IsProP.exists_continuousLinearEquiv_pi_padicInt_prod_torsion).

```lean
TauCeti.IsProP.exists_continuousLinearEquiv_pi_padicInt_prod_torsion.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {A : Type u_1} [CommGroup A] [TopologicalSpace A] [IsTopologicalGroup A]
  [CompactSpace A] [TotallyDisconnectedSpace A] (hA : TauCeti.IsProP p A)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated A) :
  ∃ r, Nonempty (Additive A ≃L[ℤ_[p]] (Fin r → ℤ_[p]) × ↥(Submodule.torsion ℤ_[p] (Additive A)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/StructureTheorem.html#TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod)
- [Source of `TauCeti.IsProP.exists_continuousMulEquiv_pi_padicInt_prod_pi_zmod` in TauCeti/Topology/Algebra/Group/Profinite/ProP/StructureTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ProP/StructureTheorem.lean#L56)
