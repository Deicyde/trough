---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.flucOf_eq_zero_of_eigen, CondensedMatter.TightBindingChain.fluc_ne_zero_of_defectOf_pos, CondensedMatter.TightBindingChain.not_eigen_of_defectOf_pos, CondensedMatter.TightBindingChain.norm_localizedState, CondensedMatter.TightBindingChain.flucOf_position_localizedState, CondensedMatter.TightBindingChain.exists_neighbour, CondensedMatter.TightBindingChain.flucOf_openHamiltonian_localizedState_ne_zero, CondensedMatter.TightBindingChain.inner_bracket_localizedState
statement: formalized
proof: formalized
---

# The uncertainty of a localized electron

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Open.LocalizedUncertainty`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean): 9 declarations, 8 with a docstring.

## i. Overview

> An eigenvector of `H` or of `X` has no fluctuation in that observable, so its centered Gram
> defect vanishes. For a localized electron `|n⟩` this means `Var X = 0`: both sides of the
> energy–position uncertainty relation are `0`, and the relation says nothing about the pair.
>
> The pair does not vanish there. As soon as the chain hops, `t ≠ 0`, and has two sites, a
> localized electron fluctuates in energy, `Var H > 0`: fixing the position sends the whole
> uncertainty to the energy, and only the bracket `⟨n|⁅H, X⁆|n⟩` is zero.
>
> Conversely, a vector with positive defect is an eigenvector of neither `H` nor `X`: it
> fluctuates in both.

## ii. Key results

> - `flucOf_eq_zero_of_eigen` : an eigenvector has no fluctuation in its observable.
> - `fluc_ne_zero_of_defectOf_pos` : a positive defect forces fluctuations in `H` and `X`.
> - `flucOf_openHamiltonian_localizedState_ne_zero` : a localized electron fluctuates in energy.
> - `inner_bracket_localizedState` : the bracket vanishes in a localized electron.
> - `robertson_schrodinger_localizedState` : in `|n⟩`, `Var X = 0` and the defect is `0`, while
>   `Var H > 0`.

## iv. References

> * H. P. Robertson, *The uncertainty principle*, Phys. Rev. 34 (1929) 163.
> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Eigenvectors

**`CondensedMatter.TightBindingChain.flucOf_eq_zero_of_eigen`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L62).

> A unit eigenvector of `A` with real eigenvalue has no fluctuation in `A`.

```lean
lemma flucOf_eq_zero_of_eigen {A : T.HilbertSpace →ₗ[ℂ] T.HilbertSpace} {ψ : T.HilbertSpace}
    (hψ : ‖ψ‖ = 1) {c : ℝ} (h : A ψ = (c : ℂ) • ψ) : T.flucOf A ψ = 0
```

**`CondensedMatter.TightBindingChain.fluc_ne_zero_of_defectOf_pos`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L70).

> A positive defect forces fluctuations in both `H` and `X`.

```lean
lemma fluc_ne_zero_of_defectOf_pos {ψ : T.HilbertSpace} (h : 0 < T.defectOf ψ) :
    T.flucOf T.openHamiltonian ψ ≠ 0 ∧ T.flucOf T.position ψ ≠ 0
```

**`CondensedMatter.TightBindingChain.not_eigen_of_defectOf_pos`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L75).

> A vector with positive defect is an eigenvector of neither `H` nor `X`.

```lean
lemma not_eigen_of_defectOf_pos {ψ : T.HilbertSpace} (hψ : ‖ψ‖ = 1)
    (h : 0 < T.defectOf ψ) (c : ℝ) :
    T.openHamiltonian ψ ≠ (c : ℂ) • ψ ∧ T.position ψ ≠ (c : ℂ) • ψ
```

## B. The localized electron

**`CondensedMatter.TightBindingChain.norm_localizedState`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L87).

```lean
lemma norm_localizedState (n : Fin T.N) : ‖(|n⟩ : T.HilbertSpace)‖ = 1 :=
  (localizedState (T := T)).orthonormal.1 n
```

**`CondensedMatter.TightBindingChain.flucOf_position_localizedState`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L91).

> A localized electron has no fluctuation in position.

```lean
lemma flucOf_position_localizedState (n : Fin T.N) : T.flucOf T.position |n⟩ = 0 :=
  T.flucOf_eq_zero_of_eigen (T.norm_localizedState n) (T.position_apply_localizedState n)
```

**`CondensedMatter.TightBindingChain.exists_neighbour`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L95).

> Every site of a chain with two sites has a neighbour.

```lean
lemma exists_neighbour (hN : 2 ≤ T.N) (n : Fin T.N) :
    ∃ m : Fin T.N, (m : ℕ) + 1 = n ∨ (n : ℕ) + 1 = m
```

**`CondensedMatter.TightBindingChain.flucOf_openHamiltonian_localizedState_ne_zero`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L103).

> **A localized electron fluctuates in energy.** If the chain hops and has two sites,
> `H |n⟩ - ⟨H⟩ |n⟩ ≠ 0`: its overlap with a neighbour is `-t`.

```lean
lemma flucOf_openHamiltonian_localizedState_ne_zero (ht : T.t ≠ 0) (hN : 2 ≤ T.N)
    (n : Fin T.N) : T.flucOf T.openHamiltonian |n⟩ ≠ 0 := by
  obtain ⟨m, hm⟩ := T.exists_neighbour hN n
  have hmn : m ≠ n := by rintro rfl; omega
  intro h
  have h' := congrArg (fun φ => ⟪(|m⟩ : T.HilbertSpace), φ⟫_ℂ) h
  simp only [flucOf, ← Complex.coe_smul, inner_sub_right, inner_smul_right,
    T.localizedState_orthonormal_eq_ite, hmn, ↓reduceIte, mul_zero, sub_zero,
    T.inner_openHamiltonian, hm, inner_zero_right, neg_eq_zero, Complex.ofReal_eq_zero] at h'
  exact ht h'
```

**`CondensedMatter.TightBindingChain.inner_bracket_localizedState`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L115).

> The bracket `⁅H, X⁆` vanishes in a localized electron.

```lean
lemma inner_bracket_localizedState (n : Fin T.N) :
    ⟪|n⟩, ((⁅T.openHamiltonianObservable, T.positionObservable⁆ : Observable _) :
      _ →L[ℂ] _) |n⟩⟫_ℂ = 0 := by
  rw [inner_bracket_openHamiltonian_position_eq]
  simp
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_localizedState`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean#L124).

> **Robertson–Schrödinger is empty in a localized electron.** In `|n⟩`, `Var X = 0` and the
> centered Gram defect is `0`: both sides of the relation vanish. The energy does not:
> `Var H > 0` as soon as the chain hops and has two sites.

```lean
lemma robertson_schrodinger_localizedState (ht : T.t ≠ 0) (hN : 2 ≤ T.N) (n : Fin T.N) :
    variance (ofVec (T.norm_localizedState n)) T.positionObservable = 0 ∧
      centeredGramDefect (ofVec (T.norm_localizedState n)) T.openHamiltonianObservable
        T.positionObservable = 0 ∧
      0 < variance (ofVec (T.norm_localizedState n)) T.openHamiltonianObservable
```

## Depends on

- [The velocity band of forced uncertainty](../part-02/velocityband-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Open/LocalizedUncertainty.lean)
