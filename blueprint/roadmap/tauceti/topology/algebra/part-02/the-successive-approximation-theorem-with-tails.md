---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top
statement: formalized
proof: formalized
---

# The successive-approximation theorem with tails

Let `r, w ∈ λ_1(F)` be relators of the
free pro-`p` group `F` on a finite linearly ordered type with the same class `ρ ∈ gr_1(F)`, let
`S` be a set of generators and `l₁, l₂` disjoint duplicate-free lists of generators containing
`S`, and suppose `gr_{m+1}(F) = Im δ_ρ + ⟨π^{m+1} ξ_i : i ∈ S⟩` for every `m ≥ 1`. Then a
continuous automorphism `e` of `F` carries `r` to `(∏_{i ∈ l₁} t_i) * w * (∏_{i ∈ l₂} t_i)` for
tail elements `t_i` of the closed procyclic subgroups `⟨x_i⟩`, all lying in `λ_2(F)`.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top.{u}
  {p : ℕ} [Fact (Nat.Prime p)] {X : Type u} [Finite X] [LinearOrder X]
  (r w : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1))
  (h :
    TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r = TauCeti.gradedMk p (TauCeti.freeProP p X) 1 w)
  (S : Set X) (l₁ l₂ : List X) (hnd : (l₁ ++ l₂).Nodup) (hl : ∀ i ∈ S, i ∈ l₁ ++ l₂)
  (hspan :
    ∀ (m : ℕ) (hm : 1 ≤ m),
      ((TauCeti.freeProP.basisModificationDelta p X hm)
              (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r)).range ⊔
          TauCeti.freeProP.gradedPowIterSpan p X S (m + 1) =
        ⊤) :
  ∃ e t,
    (∀ (i : X), t i ∈ (Subgroup.closure {TauCeti.freeProP.of i}).topologicalClosure) ∧
      (∀ (i : X), t i ∈ TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 2) ∧
        e ↑r = (List.map t l₁).prod * ↑w * (List.map t l₂).prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Tail.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Tail.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_sup_gradedPowIterSpan_eq_top` in TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Tail.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Tail.lean#L275)
