---
declaration: theorem
origin: cited
lean: TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator
statement: formalized
proof: formalized
---

# The torsion-free case of the structure theorem

The coordinate `q` of the exponent vector
`exponentSum r = q • w`, `w x₀ = 1`, of the relator vanishes exactly when `r` lies in the closed
commutator subgroup of the free pro-`p` group; then the factor `ℤ_p ⧸ q ℤ_p` of
`oneRelatorAbelianizationEquiv` is `ℤ_p` and `G^{ab} ≅ ℤ_p^X` is torsion-free.

```lean
TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator.{u} {p : ℕ}
  [Fact (Nat.Prime p)] {X : Type u} (r : TauCeti.freeProP p X) (x₀ : X) (w : X → ℤ_[p])
  (hw : w x₀ = 1) (q : ℤ_[p])
  (hr : Multiplicative.toAdd ((TauCeti.freeProP.exponentSum p X) r) = q • w) [Finite X] :
  q = 0 ↔ r ∈ (commutator (TauCeti.freeProP p X)).topologicalClosure
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.html#TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator).

## Sources

- [Tau Ceti documentation: `TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.html#TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator)
- [Source of `TauCeti.presentedProP.oneRelator_q_eq_zero_iff_mem_topologicalClosure_commutator` in TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Presentation/Abelianization.lean#L401)
