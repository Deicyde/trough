---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq
statement: formalized
proof: formalized
---

# The constrained successive-approximation theorem

Let `r, w ∈ λ_1(F)` be relators of the
free pro-`p` group `F` on a finite linearly ordered type with the same class `ρ ∈ gr_1(F)`, let
`Z ⊆ F` and let `C : X → Subgroup F` be closed admissible corrections, with every admissible basis
modification `θ_ω`, `ω : X → λ_1(F)` with `ω_i ∈ C i` for every `i`, preserving each `C i`, and
every admissible endomorphism `φ` of `F`, one with `x_i⁻¹ * φ(x_i) ∈ C i` for every `i`, congruent
to the identity modulo `λ_1(F)` having its deviation `(φ r)⁻¹ * w` in `Z`. Suppose that for every
`m ≥ 1` each element of `λ_{m+1}(F)` lying in `Z` has class `δ_ρ(⟦ω⟧)` for a family
`ω : X → λ_m(F)` with `ω_i ∈ C i` for every `i`. Then an admissible continuous automorphism of `F`
carries `r` to `w`.

The admissibility of the automorphism is the limit of the admissibility of the finite
approximations, which needs the `C i` closed. The constrained span statement is the hypothesis a
normal-form argument has to establish; it is assumed here. Taking `Z = F` and `C i = F` recovers
the unconstrained theorem
`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_basisModificationDelta_eq_top`.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq.{u} {p : ℕ} [Fact (Nat.Prime p)] {X : Type u}
  [Finite X] [LinearOrder X] (Z : Set (TauCeti.freeProP p X))
  (C : X → Subgroup (TauCeti.freeProP p X)) (hclosed : ∀ (i : X), IsClosed ↑(C i))
  (hC :
    ∀ (ω : X → ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1)),
      (∀ (i : X), ↑(ω i) ∈ C i) →
        ∀ (i : X), ∀ c ∈ C i, (TauCeti.freeProP.basisModification ω) c ∈ C i)
  (r w : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1))
  (h :
    TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r = TauCeti.gradedMk p (TauCeti.freeProP p X) 1 w)
  (hZ :
    ∀ (φ : TauCeti.freeProP p X →ₜ* TauCeti.freeProP p X),
      (∀ (g : TauCeti.freeProP p X),
          g⁻¹ * φ g ∈ TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) 1) →
        (∀ (i : X), (TauCeti.freeProP.of i)⁻¹ * φ (TauCeti.freeProP.of i) ∈ C i) →
          (φ ↑r)⁻¹ * ↑w ∈ Z)
  (hspan :
    ∀ (m : ℕ) (hm : 1 ≤ m) (z : ↥(TauCeti.pLowerCentralSeries p (TauCeti.freeProP p X) (m + 1))),
      ↑z ∈ Z →
        ∃ ω,
          (∀ (i : X), ↑(ω i) ∈ C i) ∧
            (((TauCeti.freeProP.basisModificationDelta p X hm)
                  (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 r))
                fun i => TauCeti.gradedMk p (TauCeti.freeProP p X) m (ω i)) =
              TauCeti.gradedMk p (TauCeti.freeProP p X) (m + 1) z) :
  ∃ e, (∀ (i : X), (TauCeti.freeProP.of i)⁻¹ * e (TauCeti.freeProP.of i) ∈ C i) ∧ e ↑r = ↑w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's criterion modulo `λ_1`](../algebra/part-01/burnsides-criterion-modulo-1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq` in TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/SuccessiveApproximation/Basic.lean#L211)
