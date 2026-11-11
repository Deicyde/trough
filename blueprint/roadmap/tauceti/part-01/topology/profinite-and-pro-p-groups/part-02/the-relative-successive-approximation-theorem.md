---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq
statement: formalized
proof: formalized
---

# The relative successive-approximation theorem

Let `r, w ∈ λ_1(F)` be relators of the
free pro-`p` group `F` on a finite linearly ordered type with the same class `ρ ∈ gr_1(F)` and the
same exponent vector `v = exponentSum r`, and suppose that for every `m ≥ 1` each element of
`λ_{m+1}(F)` lying in the closed commutator subgroup `K` has class `δ_ρ(⟦ω⟧)` for a family
`ω : X → λ_m(F)` with `ω_i ∈ K` at every generator `i` with `v_i ≠ 0`. Then a continuous
automorphism of `F` carries `r` to `w`.

This is the form of the argument for a relator whose `p`-power part lies in `λ_2(F)`: there `Im δ_ρ`
misses the classes `π^{m+1} ξ_i`, so `δ_ρ` is not onto. It is the constrained theorem
`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq` with `Z = K` and with `C i = K` at the
generators carrying a nonzero exponent: such corrections preserve the exponent vector of the
relator, which keeps the deviations in `K` along the approximation. The hypothesis on the
corrections is the constrained form of the span statement that `Im δ_ρ` contains the class of
every element of `λ_{m+1}(F) ∩ K`; it is assumed here, not established.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq.{u} {p : ℕ}
  [Fact (Nat.Prime p)] {X : Type u} [Finite X] [LinearOrder X]
  (r w : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1))
  (h :
    TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r = TauCeti.gradedMk p (TauCeti.freeProP p X) 1 w)
  (hrw : (TauCeti.freeProP.exponentSum p X) ↑r = (TauCeti.freeProP.exponentSum p X) ↑w)
  (hspan :
    ∀ (m : ℕ) (hm : 1 ≤ m) (z : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) (m + 1))),
      ↑z ∈ (commutator (TauCeti.freeProP p X)).topologicalClosure →
        ∃ ω,
          (∀ (i : X),
              Multiplicative.toAdd ((TauCeti.freeProP.exponentSum p X) ↑r) i ≠ 0 →
                ↑(ω i) ∈ (commutator (TauCeti.freeProP p X)).topologicalClosure) ∧
            (((TauCeti.freeProP.basisModificationDelta p X hm)
                  (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r))
                fun i => TauCeti.gradedMk p (TauCeti.freeProP p X) m (ω i)) =
              TauCeti.gradedMk p (TauCeti.freeProP p X) (m + 1) z) :
  ∃ e, e ↑r = ↑w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The constrained successive-approximation theorem](../part-01/the-constrained-successive-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_exponentSum_eq` in TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean#L268)
