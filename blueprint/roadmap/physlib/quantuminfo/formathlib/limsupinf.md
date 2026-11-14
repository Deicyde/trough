---
declaration: module
origin: cited
lean: Filter.tendsto_sub_atTop_iff_nat, ENNReal.tendsto_sub_const_nhds_zero_iff, exists_strictMono_seq_le, exists_seq_bound, exists_liminf_zero_of_forall_liminf_le, exists_liminf_zero_of_forall_liminf_le_with_UB, exists_limsup_zero_of_forall_limsup_le, tendsto_of_block_sequence
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.LimSupInf

The module `QuantumInfo.ForMathlib.LimSupInf`, [QuantumInfo/ForMathlib/LimSupInf.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean): 13 declarations, 2 with a docstring, 2 listed as significant.

> Several 'bespoke' facts about limsup and liminf on ENNReal / NNReal needed in SteinsLemma

**`exists_strictMono_seq_le`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L28).

```lean
lemma exists_strictMono_seq_le (y : ℝ≥0) (f : ℝ≥0 → ℕ → ℝ≥0∞) (hf : ∀ x > 0, Filter.atTop.liminf (f x) ≤ y) :
    ∃ n : ℕ → ℕ, StrictMono n ∧ ∀ k : ℕ, f ((k : ℝ≥0) + 1)⁻¹ (n k) ≤ (y : ℝ≥0∞) + ((k : ℝ≥0) + 1)⁻¹
```

**`exists_seq_bound`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L46).

```lean
lemma exists_seq_bound (y : ℝ≥0) (f : ℝ≥0 → ℕ → ℝ≥0∞) (hf : ∀ x > 0, Filter.atTop.limsup (f x) ≤ y) :
    ∃ M : ℕ → ℕ, StrictMono M ∧ ∀ k, ∀ n ≥ M k, f ((k + 1 : ℝ≥0)⁻¹) n ≤ y + (k + 1 : ℝ≥0∞)⁻¹
```

**`exists_liminf_zero_of_forall_liminf_le`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L74).

```lean
lemma exists_liminf_zero_of_forall_liminf_le (y : ℝ≥0) (f : ℝ≥0 → ℕ → ℝ≥0∞)
  (hf : ∀ x > 0, Filter.atTop.liminf (f x) ≤ y) :
    ∃ g : ℕ → ℝ≥0, (∀ x, g x > 0) ∧ Filter.atTop.Tendsto g (𝓝 0) ∧
      Filter.atTop.liminf (fun n ↦ f (g n) n) ≤ y
```

**`exists_liminf_zero_of_forall_liminf_le_with_UB`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L169).

```lean
lemma exists_liminf_zero_of_forall_liminf_le_with_UB (y : ℝ≥0) (f : ℝ≥0 → ℕ → ℝ≥0∞)
  {z : ℝ≥0} (hz : 0 < z)
  (hf : ∀ x, x > 0 → Filter.atTop.liminf (f x) ≤ y) :
    ∃ g : ℕ → ℝ≥0, (∀ x, g x > 0) ∧ (∀ x, g x < z) ∧ (Filter.atTop.Tendsto g (𝓝 0)) ∧
      (Filter.atTop.liminf (fun n ↦ f (g n) n) ≤ y)
```

**`exists_limsup_zero_of_forall_limsup_le`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L186).

```lean
lemma exists_limsup_zero_of_forall_limsup_le (y : ℝ≥0) (f : ℝ≥0 → ℕ → ℝ≥0∞)
  (hf : ∀ x, x > 0 → Filter.atTop.limsup (f x) ≤ y) :
    ∃ g : ℕ → ℝ≥0, (∀ x, g x > 0) ∧ (Filter.atTop.Tendsto g (𝓝 0)) ∧
      (Filter.atTop.limsup (fun n ↦ f (g n) n) ≤ y)
```

**`tendsto_of_block_sequence`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L247).

```lean
lemma tendsto_of_block_sequence {α : Type*} [TopologicalSpace α] {x : ℕ → α} {T : ℕ → ℕ}
    (hT : StrictMono T) {L : α} (hx : Filter.atTop.Tendsto x (𝓝 L)) (g : ℕ → α) (hg : ∀ k, ∀ n ∈ Set.Ico (T k) (T (k + 1)), g n = x k) :
      Filter.atTop.Tendsto g (𝓝 L)
```

**`exists_increasing_sequence_with_property`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L274).

```lean
lemma exists_increasing_sequence_with_property (M : ℕ → ℕ) (P : ℕ → ℕ → Prop) (hP : ∀ k L, ∃ n ≥ L, P k n) :
    ∃ T : ℕ → ℕ, StrictMono T ∧ (∀ k, T k ≥ M k) ∧ (∀ k, ∃ n ∈ Set.Ico (T k) (T (k + 1)), P k n)
```

**`liminf_le_of_block_sequence_witnesses`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L300).

```lean
lemma liminf_le_of_block_sequence_witnesses {α : Type*} (y : ℝ≥0) (f : α → ℕ → ℝ≥0∞)
    (T : ℕ → ℕ) (hT : StrictMono T) (x : ℕ → α) (g : ℕ → α)
    (hg : ∀ k, ∀ n ∈ Set.Ico (T k) (T (k + 1)), g n = x k)
    (hwit : ∀ k, ∃ n ∈ Set.Ico (T k) (T (k + 1)), f (x k) n ≤ (y : ℝ≥0∞) + (k + 1 : ℝ≥0)⁻¹) :
    Filter.atTop.liminf (fun n ↦ f (g n) n) ≤ y
```

**`limsup_le_of_block_sequence_bound`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L330).

```lean
lemma limsup_le_of_block_sequence_bound {α : Type*} (y : ℝ≥0) (f : α → ℕ → ℝ≥0∞)
  (T : ℕ → ℕ) (hT : StrictMono T) (x : ℕ → α) (g : ℕ → α)
  (hg : ∀ k, ∀ n ∈ Set.Ico (T k) (T (k + 1)), g n = x k)
  (hbound : ∀ k, ∀ n ∈ Set.Ico (T k) (T (k + 1)), f (x k) n ≤ (y : ℝ≥0∞) + (k + 1 : ℝ≥0)⁻¹) :
  Filter.atTop.limsup (fun n ↦ f (g n) n) ≤ y
```

**`exists_liminf_zero_of_forall_liminf_limsup_le_with_UB`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L369).

```lean
lemma exists_liminf_zero_of_forall_liminf_limsup_le_with_UB (y₁ y₂ : ℝ≥0) (f₁ f₂ : ℝ≥0 → ℕ → ℝ≥0∞)
    {z : ℝ≥0} (hz : 0 < z)
    (hf₁ : ∀ x > 0, Filter.atTop.liminf (f₁ x) ≤ y₁)
    (hf₂ : ∀ x > 0, Filter.atTop.limsup (f₂ x) ≤ y₂) :
      ∃ g : ℕ → ℝ≥0, (∀ x, g x > 0) ∧ (∀ x, g x < z) ∧
        Filter.atTop.Tendsto g (𝓝 0) ∧
        Filter.atTop.liminf (fun n ↦ f₁ (g n) n) ≤ y₁ ∧
      Filter.atTop.limsup (fun n ↦ f₂ (g n) n) ≤ y₂
```

**`extracted_limsup_inequality`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L477).

```lean
lemma extracted_limsup_inequality (z : ℝ≥0∞) (hz : z ≠ ⊤) (y x : ℕ → ℝ≥0∞) (h_lem5 : ∀ (n : ℕ), x n ≤ y n + z)
    : Filter.atTop.limsup (fun n ↦ x n / n) ≤ Filter.atTop.limsup (fun n ↦ y n / n)
```

**`Filter.tendsto_sub_atTop_iff_nat`**, a theorem, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L518). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Like `Filter.tendsto_add_atTop_iff_nat`, but with nat subtraction.

```lean
theorem _root_.Filter.tendsto_sub_atTop_iff_nat {α : Type*} {f : ℕ → α} {l : Filter α} (k : ℕ) :
    Tendsto (fun (n : ℕ) ↦ f (n - k)) atTop l ↔ Tendsto f atTop l
```

**`ENNReal.tendsto_sub_const_nhds_zero_iff`**, a theorem, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean#L528). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Sort of dual to `ENNReal.tendsto_const_sub_nhds_zero_iff`. Takes a substantially different form though, since
> we don't actually have equality of the limits, or even the fact that the other one converges, which is why we
> need to use `limsup`.

```lean
theorem _root_.ENNReal.tendsto_sub_const_nhds_zero_iff {α : Type*} {l : Filter α} {f : α → ℝ≥0∞} {a : ℝ≥0∞}
    : Tendsto (f · - a) l (𝓝 0) ↔ limsup f l ≤ a
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/LimSupInf.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LimSupInf.lean)
