---
declaration: module
origin: cited
lean: pinching_sq_eq_self, pinching_kraus_ortho, pinching_bound, pinching_pythagoras, pinching_kraus, pinching_kraus_commutes, pinching_kraus_mul_self, finite_spectrum_inst
statement: formalized
proof: formalized
---

# Pinching channels

The module `QuantumInfo.Channels.Pinching`, [QuantumInfo/Channels/Pinching.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean): 24 declarations, 4 with a docstring, 4 listed as significant.

> A pinching channel decoheres in the eigenspaces of a given state.
> More precisely, given a state ρ, the pinching channel with respect to ρ is defined as
>   E(σ) = ∑ Pᵢ σ Pᵢ
> where the P\_i are the projectors onto the i-th eigenspaces of ρ = ∑ᵢ pᵢ Pᵢ, with i ≠ j → pᵢ ≠ pⱼ.
>
> …

**`pinching_kraus`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L26).

```lean
def pinching_kraus (ρ : MState d) : spectrum ℝ ρ.m → HermitianMat d ℂ
```

**`pinching_kraus_commutes`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L29).

```lean
lemma pinching_kraus_commutes (ρ : MState d) (i : spectrum ℝ ρ.m) :
    Commute (pinching_kraus ρ i).mat ρ.m
```

**`pinching_kraus_mul_self`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L35).

```lean
lemma pinching_kraus_mul_self (ρ : MState d) (i : spectrum ℝ ρ.m) :
    (pinching_kraus ρ i).mat * ρ.m = i.val • pinching_kraus ρ i
```

**`finite_spectrum_inst`**, an instance, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L45).

```lean
instance finite_spectrum_inst (ρ : MState d) : Fintype (spectrum ℝ ρ.m)
```

**`pinching_kraus_orthogonal`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L48).

```lean
lemma pinching_kraus_orthogonal (ρ : MState d) {i j : spectrum ℝ ρ.m} (h : i ≠ j) :
    (pinching_kraus ρ i).mat * (pinching_kraus ρ j).mat = 0
```

**`pinching_sq_eq_self`**, a theorem, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L57). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kraus operators of the pinching channelare projectors: they square to themselves.

```lean
theorem pinching_sq_eq_self (ρ : MState d) (k) : (pinching_kraus ρ k) ^ 2  = pinching_kraus ρ k
```

**`pinching_kraus_ortho`**, a theorem, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L65). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kraus operators of the pinching channel are orthogonal projectors.

```lean
theorem pinching_kraus_ortho (ρ : MState d) (i j : spectrum ℝ ρ.m) :
    (pinching_kraus ρ i).mat * (pinching_kraus ρ j).mat = if i = j then (pinching_kraus ρ i).mat else 0
```

**`pinching_sum`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L72).

```lean
lemma pinching_sum (ρ : MState d) : ∑ k, pinching_kraus ρ k = 1
```

**`pinching_map`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L84).

```lean
def pinching_map (ρ : MState d) : CPTPMap d d ℂ
```

**`pinchingMap_apply_M`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L95).

```lean
lemma pinchingMap_apply_M (σ ρ : MState d) : (pinching_map σ ρ).M =
  ⟨_, (MatrixMap.of_kraus_isCompletelyPositive
    (HermitianMat.mat ∘ pinching_kraus σ)).IsPositive.IsHermitianPreserving ρ.M.H⟩
```

**`pinching_eq_sum_conj`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L100).

```lean
lemma pinching_eq_sum_conj (σ ρ : MState d) : (pinching_map σ ρ).M =
    ∑ k, (pinching_kraus σ k).mat * ρ.M * (pinching_kraus σ k).mat
```

**`pinching_commutes_kraus`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L105).

```lean
lemma pinching_commutes_kraus (σ ρ : MState d) (i : spectrum ℝ σ.m) :
    Commute (pinching_map σ ρ).m (pinching_kraus σ i).mat
```

**`pinching_commutes`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L116).

```lean
lemma pinching_commutes (ρ σ : MState d) :
    Commute (pinching_map σ ρ).m σ.m
```

**`pinching_self`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L134).

```lean
lemma pinching_self (ρ : MState d) : pinching_map ρ ρ = ρ
```

**`pinching_bound`**, a theorem, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L153). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Lemma 3.10 of Hayashi's book "Quantum Information Theory - Mathematical Foundations".
> Also, Lemma 5 in https://arxiv.org/pdf/quant-ph/0107004.
> -- Used in (S60)

```lean
theorem pinching_bound (ρ σ : MState d) : ρ.M ≤ (↑(Fintype.card (spectrum ℝ σ.m)) : ℝ) • (pinching_map σ ρ).M
```

**`ker_le_ker_pinching_of_PosDef`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L228).

```lean
lemma ker_le_ker_pinching_of_PosDef (ρ σ : MState d) (hpos : σ.m.PosDef) : σ.M.ker ≤ (pinching_map σ ρ).M.ker
```

**`pinching_idempotent`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L237).

```lean
lemma pinching_idempotent (ρ σ : MState d) :
    (pinching_map σ) (pinching_map σ ρ) = (pinching_map σ ρ)
```

**`inner_cfc_pinching`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L247).

```lean
lemma inner_cfc_pinching (ρ σ : MState d) (f : ℝ → ℝ) :
    ⟪ρ.M, (pinching_map σ ρ).M.cfc f⟫ = ⟪(pinching_map σ ρ).M, (pinching_map σ ρ).M.cfc f⟫
```

**`inner_cfc_pinching_right`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L273).

```lean
lemma inner_cfc_pinching_right (ρ σ : MState d) (f : ℝ → ℝ) :
    ⟪(pinching_map σ ρ).M, σ.M.cfc f⟫ = ⟪ρ.M, σ.M.cfc f⟫
```

**`pinching_map_eq_sum_conj_hermitian`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L302).

```lean
lemma pinching_map_eq_sum_conj_hermitian (σ ρ : MState d) :
    (pinching_map σ ρ).M = ∑ k, ρ.M.conj (pinching_kraus σ k).mat
```

**`pinching_map_ker_le`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L307).

```lean
lemma pinching_map_ker_le (ρ σ : MState d) : (pinching_map σ ρ).M.ker ≤ ρ.M.ker
```

**`pinching_kraus_ker_of_ne_zero`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L331).

```lean
lemma pinching_kraus_ker_of_ne_zero {d : Type*} [Fintype d] [DecidableEq d]
    (σ : MState d) (v : d → ℂ) (hv : σ.m.mulVec v = 0)
    (k : spectrum ℝ σ.m) (hk : k.val ≠ 0) :
    (pinching_kraus σ k).mat *ᵥ v = 0
```

**`ker_le_ker_pinching_map_ker`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L349).

```lean
lemma ker_le_ker_pinching_map_ker (ρ σ : MState d) (h : σ.M.ker ≤ ρ.M.ker) :
    σ.M.ker ≤ (pinching_map σ ρ).M.ker
```

**`pinching_pythagoras`**, a theorem, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean#L395). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Exercise 2.8 of Hayashi's book "A group theoretic approach to Quantum Information".

```lean
theorem pinching_pythagoras (ρ σ : MState d) :
    𝐃(ρ‖σ) = 𝐃(ρ‖pinching_map σ ρ) + 𝐃(pinching_map σ ρ‖σ)
```

## Depends on

- [QuantumInfo.Entropy.Relative](../entropy/relative.md)

## Sources

- [QuantumInfo/Channels/Pinching.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Pinching.lean)
