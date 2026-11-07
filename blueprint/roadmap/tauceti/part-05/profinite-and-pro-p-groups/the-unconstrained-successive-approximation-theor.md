---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top
statement: formalized
proof: formalized
---

# The unconstrained successive-approximation theorem

Let `r, w ∈ λ_1(F)` be relators of
the free pro-`p` group `F` on a finite linearly ordered type with the same class `ρ ∈ gr_1(F)`, and
suppose the basis-modification map `δ_ρ` is onto `gr_{m+1}(F)` for every `m ≥ 1`. Then a continuous
automorphism of `F` carries `r` to `w`.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top.{u}
  {p : ℕ} [Fact (Nat.Prime p)] {X : Type u} [Finite X] [LinearOrder X]
  (r w : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1))
  (h :
    TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r = TauCeti.gradedMk p (TauCeti.freeProP p X) 1 w)
  (hspan :
    ∀ (m : ℕ) (hm : 1 ≤ m),
      ((TauCeti.freeProP.basisModificationDelta p X hm)
            (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r)).range =
        ⊤) :
  ∃ e, e ↑r = ↑w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top` in TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean#L250)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
