---
declaration: module
origin: cited
lean: OptimalHypothesisRate.iInf_IsCompact, OptimalHypothesisRate.iInf_IsConvex, OptimalHypothesisRate.of_empty, OptimalHypothesisRate.exists_min', OptimalHypothesisRate.exists_min, OptimalHypothesisRate.pos_of_lt_one, OptimalHypothesisRate.optimalHypothesisRate_antitone, OptimalHypothesisRate.Ref81Lem5
statement: formalized
proof: formalized
---

# QuantumInfo.ResourceTheory.HypothesisTesting

The module `QuantumInfo.ResourceTheory.HypothesisTesting`, [QuantumInfo/ResourceTheory/HypothesisTesting.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean): 21 declarations (1 instance with no name), 11 with a docstring, 9 listed as significant.

> Defines `OptimalHypothesisRate`, the optimal rate of distinguishing an `MState` ρ from a set of other
> mixed states `S`, with at most Type I error ε.
>
> That is to say: take a projective measurement (a `POVM`) with elements `{T, 1-T}`, where measuring `T`
> will mean we conclude our unknown state was ρ, and measuring `1-T` will mean we think the state was
> something in `S`. We only accept T's such that `Tr[(1-T)ρ] ≤ ε`, that is, we have at most an ε
> probability of incorrectly concluding it was ρ. The Type II error associated to this T is then
> `max_{σ ∈ S} Tr[T σ]`, that is, the (worst possible, over possible states) chance of incorrectly
> concluding our state was in `S`. Optimize over `T` to get the lowest possible Type II error rate,
> and the resulting error rate is `OptimalHypothesisRate ρ ε S`.
>
> We make this accessible through the notation `β_ ε(ρ‖S)`.
>
> See [The tangled state of quantum hypothesis testing](https://doi.org/10.1038/s41567-023-02289-9) by
> Mario Berta et al. for a broader overview.

**`OptimalHypothesisRate`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L45).

> The optimal hypothesis testing rate, for a tolerance ε: given a state ρ and a set of states S,
> the optimum distinguishing rate that allows a probability ε of errors.

```lean
noncomputable def OptimalHypothesisRate (ρ : MState d) (ε : Prob) (S : Set (MState d)) : Prob
```

**`OptimalHypothesisRate.iInf_Inhabited`**, an instance, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L54).

> The space of strategies `T` in `OptimalHypothesisRate` is inhabited, we always have some valid strategy.

```lean
instance iInf_Inhabited (ρ : MState d) (ε : Prob) :
    Inhabited { m // ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1 }
```

**An instance with no name**, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L58).

```lean
instance (ρ : MState d) (ε : Prob) : Inhabited {m | ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1}
```

**`OptimalHypothesisRate.iInf_IsCompact`**, a theorem, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L62). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The space of strategies `T` in `OptimalHypothesisRate` is compact.

```lean
theorem iInf_IsCompact (ρ : MState d) (ε : Prob) : IsCompact { m | ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1 }
```

**`OptimalHypothesisRate.iInf_IsConvex`**, a theorem, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L73). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The space of strategies `T` in `OptimalHypothesisRate` is convex.

```lean
theorem iInf_IsConvex (ρ : MState d) (ε : Prob) : Convex ℝ { m | ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1 }
```

**`OptimalHypothesisRate.of_empty`**, a theorem, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L92). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> When `S` is empty, the optimal hypothesis testing rate is zero.

```lean
theorem of_empty {ρ : MState d} (ε : Prob) : β_ ε(ρ‖∅) = 0
```

**`OptimalHypothesisRate.le_sup_exp_val`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L97).

```lean
lemma le_sup_exp_val {ρ : MState d} (ε : Prob) {S : Set (MState d)}
    (m : HermitianMat d ℂ) (hExp : ρ.exp_val (1 - m) ≤ ε) (hm : 0 ≤ m ∧ m ≤ 1) :
    β_ ε(ρ‖S) ≤ ⨆ σ ∈ S, ⟨_, σ.exp_val_prob hm⟩
```

**`OptimalHypothesisRate.le_of_subset`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L104).

```lean
lemma le_of_subset (ρ : MState d) (ε : Prob) {S1 S2 : Set (MState d)} (h : S1 ⊆ S2) :
    β_ ε(ρ‖S1) ≤ β_ ε(ρ‖S2)
```

**`OptimalHypothesisRate.of_singleton`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L108).

```lean
lemma of_singleton {ρ σ : MState d} {ε : Prob} :
    β_ ε(ρ‖{σ}) =
      ⨅ T : { m : HermitianMat d ℂ // ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1},
        ⟨_, σ.exp_val_prob T.2.right⟩
```

**`OptimalHypothesisRate.negLog_le_singleton`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L115).

```lean
lemma negLog_le_singleton (ρ : MState d) (ε : Prob) (S : Set (MState d))
    (σ : MState d) (h : σ ∈ S) : —log β_ ε(ρ‖S) ≤ —log β_ ε(ρ‖{σ})
```

**`OptimalHypothesisRate.singleton_le_exp_val`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L122).

```lean
lemma singleton_le_exp_val {ρ σ : MState d} {ε : Prob} (m : HermitianMat d ℂ)
    (hExp : ρ.exp_val (1 - m) ≤ ε) (hm : 0 ≤ m ∧ m ≤ 1) :
  β_ ε(ρ‖{σ}) ≤ ⟨_, σ.exp_val_prob hm⟩
```

**`OptimalHypothesisRate.exists_min'`**, a theorem, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L133). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> There exists an optimal T for the hypothesis testing, that is, it's a minimum
> and not just an infimum. This states we have `1 - ε ≤ ρ.exp_val T`, but we can always
> "worsen" T to make that bound tight, which is `exists_min`.

```lean
theorem exists_min' (ρ : MState d) (ε : Prob) (S : Set (MState d)):
    ∃ (T : { m : HermitianMat d ℂ // ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1}),
      (⨆ σ ∈ S, ⟨_, σ.exp_val_prob T.prop.right⟩ = β_ ε(ρ‖S))
      ∧ 1 - ε ≤ ρ.exp_val T
```

**`OptimalHypothesisRate.exists_min`**, a theorem, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L176). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> There exists an optimal T for the hypothesis testing, that is, it's a minimum and
> not just an infimum. This tightens the `T` from `exists_min'` to a `⟪ρ,T⟫ = 1 - ε` bound.

```lean
theorem exists_min (ρ : MState d) (ε : Prob) (S : Set (MState d)):
    ∃ (T : { m : HermitianMat d ℂ // ρ.exp_val (1 - m) ≤ ε ∧ 0 ≤ m ∧ m ≤ 1}),
      (⨆ σ ∈ S, ⟨_, σ.exp_val_prob T.prop.right⟩ = β_ ε(ρ‖S))
      ∧ ρ.exp_val T = 1 - ε
```

**`OptimalHypothesisRate.pos_of_lt_one`**, a theorem, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L231). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> When the allowed Type I error `ε` is less than 1 (so, we have some limit on our errors),
> and the kernel of the state `ρ` contains the kernel of some element in `S`, then the optimal
> hypothesis rate is positive - there is some lower bound on the type II errors we'll see. In
> other words, under these conditions, we cannot completely avoid type II errors.

```lean
theorem pos_of_lt_one {ρ : MState d} (S : Set (MState d))
  (hρ : ∃ σ ∈ S, σ.M.ker ≤ ρ.M.ker)
  {ε : Prob} (hε : ε < 1) : 0 < β_ ε(ρ‖S)
```

**`OptimalHypothesisRate.Lemma3`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L261).

```lean
lemma Lemma3 {ρ : MState d} (ε : Prob) {S : Set (MState d)} (hS₁ : IsCompact S)
    (hS₂ : Convex ℝ (MState.M '' S)) : ⨆ σ ∈ S, β_ ε(ρ‖{σ}) = β_ ε(ρ‖S)
```

**`OptimalHypothesisRate.ker_diagonal_prob_eq_bot`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L304).

```lean
lemma ker_diagonal_prob_eq_bot {q : Prob} (hq₁ : 0 < q) (hq₂ : q < 1) :
    HermitianMat.ker (.diagonal ℂ (ProbDistribution.coin q ·)) = ⊥
```

**`OptimalHypothesisRate.optimalHypothesisRate_antitone`**, a theorem, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L326). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Lemma S1

```lean
theorem optimalHypothesisRate_antitone (ρ σ : MState d) (ℰ : CPTPMap d d₂) (ε : Prob) :
    β_ ε(ρ‖{σ}) ≤ β_ ε(ℰ ρ‖{ℰ σ})
```

**`OptimalHypothesisRate.Ref81Lem5`**, a theorem, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L357). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> This is from [Strong converse exponents for a quantum channel discrimination problem
> and quantum-feedback-assisted communication](https://doi.org/10.1007/s00220-016-2645-4), Lemma 5.
>
> It seems like this is actually true for all 0 < α (with appropriate modifications at α = 1), but we only need
> it for the case of 1 < α.

```lean
theorem Ref81Lem5 (ρ σ : MState d) (ε : Prob) (hε : ε < 1) (α : ℝ) (hα : 1 < α) :
    —log β_ ε(ρ‖{σ}) ≤ D̃_ α(ρ‖σ) + —log (1 - ε) *
      (.ofNNReal ⟨α, zero_le_one.trans hα.le⟩) / (.ofNNReal ⟨α - 1, sub_nonneg_of_le hα.le⟩)
```

**`OptimalHypothesisRate.rate_pos_of_smul_pos`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L524).

```lean
lemma rate_pos_of_smul_pos {ε : Prob} {d : Type*} [Fintype d] [DecidableEq d] {ρ σ₁ σ₂ : MState d}
    (hσ₂ : 0 < β_ ε(ρ‖{σ₂})) {c : ℝ} (hc : 0 < c) (hσ : c • σ₂ ≤ σ₁.M) : 0 < β_ ε(ρ‖{σ₁})
```

**`OptimalHypothesisRate.rate_Continuous_singleton`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L542).

```lean
lemma rate_Continuous_singleton {ε : Prob} {d : Type*} [Fintype d] [DecidableEq d] (ρ : MState d) :
    Continuous fun σ ↦ β_ ε(ρ‖{σ})
```

**`OptimalHypothesisRate.optimalHypothesisRate_unique`**, a theorem, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean#L554). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> On the 1D Hilbert space, the optimal hypothesis testing rate is simply 1 - ε,
> since there's nothing to learn. (More generally this would hold whenever ρ=σ.) -

```lean
theorem optimalHypothesisRate_unique {d : Type*} [Fintype d] [DecidableEq d]
    (ε : Prob) (ρ σ : MState d) [Unique d] : β_ ε(ρ‖{σ}) = 1 - ε
```

## Depends on

- [QuantumInfo.Entropy.Relative](../entropy/relative.md)

## Proof depends on

- [Duals of matrix map](../channels/dual.md)
- [DPI (Data Processing Inequality)](../entropy/dpi.md)
- [QuantumInfo.ForMathlib.ContinuousSup](../formathlib/continuoussup.md)
- [QuantumInfo.ForMathlib.Minimax](../formathlib/minimax.md)
- [Positive Operator-Valued Measures](../measurements/povm.md)

## Sources

- [QuantumInfo/ResourceTheory/HypothesisTesting.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/HypothesisTesting.lean)
