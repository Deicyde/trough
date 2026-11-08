---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed, TauCeti.freeProP.nonempty_continuousMulEquiv_freeProP_openSubgroup_index
statement: formalized
proof: formalized
---

# The pro-`p` Nielsen–Schreier theorem

A closed subgroup `U` of the free pro-`p` group on
any type `X` is free pro-`p` on a pointed profinite space: some subset `s` of `U` converging to
`1` has a topological isomorphism `F_p(insert 1 s, 1) ≃ₜ* U` sending the generator attached to each
point of `insert 1 s` to that point, so that `s` is a basis of `U` converging to `1`.

```lean
TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed.{u} {p : ℕ} {X : Type u}
  [Fact (Nat.Prime p)] {U : Subgroup (TauCeti.freeProP p X)} (hU : IsClosed ↑U) :
  ∃ s,
    TauCeti.ConvergesToOne s ∧
      ∃ e,
        ∀ (x : ↑(insert 1 s)),
          e (TauCeti.freeProCPointed.of (TauCeti.finiteGroupClassP p) ⟨1, ⋯⟩ x) = ↑x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dimension shifting in every positive degree, `Hⁱ⁺¹(G, M) ≅ Hⁱ(G, Coind_1^G M ⧸ M)` for `i ≥ 1` and a compact group `G`, as an isomorphism of Mathlib's canonical continuous cohomology](../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree-hi-1.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Schreier index formula for open subgroups](the-schreier-index-formula-for-open-subgroups.md)
- [Serre's theorem at arbitrary rank, as an equivalence](../profinite-and-pro-p-groups/part-01/serres-theorem-at-arbitrary-rank-as-an-equivalen.md)
- [Shapiro's lemma in every degree](../../representation-theory/homological/shapiros-lemma-in-every-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/ClosedSubgroup.html#TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed).

## Other forms

**The pro-`p` Nielsen–Schreier theorem for open subgroups.** Formalized in Tau Ceti as [`TauCeti.freeProP.nonempty_continuousMulEquiv_freeProP_openSubgroup_index`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.html#TauCeti.freeProP.nonempty_continuousMulEquiv_freeProP_openSubgroup_index).

```lean
TauCeti.freeProP.nonempty_continuousMulEquiv_freeProP_openSubgroup_index.{u} {p : ℕ} {X : Type u}
  [hp : Fact (Nat.Prime p)] [Finite X] [Nonempty X] (U : OpenSubgroup (TauCeti.freeProP p X))
  (Y : Type u) [Finite Y] (hY : Nat.card Y = 1 + (↑U).index * (Nat.card X - 1)) :
  Nonempty (↥↑U ≃ₜ* TauCeti.freeProP p Y)
```

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/ClosedSubgroup.html#TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed)
- [Source of `TauCeti.freeProP.exists_convergesToOne_continuousMulEquiv_of_isClosed` in TauCeti/Topology/Algebra/Group/Profinite/Free/ClosedSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/ClosedSubgroup.lean#L105)
