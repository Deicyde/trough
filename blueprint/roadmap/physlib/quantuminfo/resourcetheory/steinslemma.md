---
declaration: module
origin: cited
lean: SteinsLemma.Lemma7, SteinsLemma.Lemma7_gap, SteinsLemma.GeneralizedQSteinsLemma, SteinsLemma.limit_hypotesting_eq_limit_rel_entropy, SteinsLemma.Lemma6_σn, SteinsLemma.Lemma6_σn_IsFree, SteinsLemma.LemmaS2liminf, SteinsLemma.LemmaS2limsup
statement: formalized
proof: formalized
---

# QuantumInfo.ResourceTheory.SteinsLemma

The module `QuantumInfo.ResourceTheory.SteinsLemma`, [QuantumInfo/ResourceTheory/SteinsLemma.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean): 15 declarations, 7 with a docstring, 4 listed as significant; 44 private, not shown.

**`SteinsLemma.Lemma6_σn`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L29).

> The \tilde\{σ}\_n defined in Lemma 6, also in equation (S40) in Lemma 7.

```lean
noncomputable def Lemma6_σn (m : ℕ) (σf : MState (H i)) (σₘ : MState (H (i ^ m))) : (n : ℕ) → MState (H (i ^ n))
```

**`SteinsLemma.Lemma6_σn_IsFree`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L34).

```lean
lemma Lemma6_σn_IsFree {σ₁ : MState (H i)} {σₘ : (m : ℕ) → MState (H (i ^ m))} (hσ₁_free : σ₁ ∈ IsFree)
    (hσₘ : ∀ (m : ℕ), σₘ m ∈ IsFree) (m n : ℕ) : Lemma6_σn m σ₁ (σₘ m) n ∈ IsFree
```

**`SteinsLemma.LemmaS2liminf`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L192).

```lean
lemma LemmaS2liminf {ε3 : Prob} {ε4 : ℝ≥0} (hε4 : 0 < ε4)
  {d : ℕ → Type*} [∀ n, Fintype (d n)] [∀ n, DecidableEq (d n)] (ρ : (n : ℕ) → MState (d n)) (σ : (n : ℕ) → MState (d n))
  {Rinf : ℝ≥0} (hRinf : Rinf ≥ Filter.atTop.liminf (fun (n : ℕ) ↦ —log β_ ε3(ρ n‖{σ n}) / n))
  :
  (Filter.atTop.liminf (fun (n : ℕ) ↦ ⟪{(ρ n).M ≥ₚ (Real.exp (n * (Rinf + ε4))) • (σ n).M}, (ρ n).M⟫) ≤ 1 - ε3)
```

**`SteinsLemma.LemmaS2limsup`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L260).

```lean
lemma LemmaS2limsup {ε3 : Prob} {ε4 : ℝ≥0} (hε4 : 0 < ε4)
  {d : ℕ → Type*} [∀ n, Fintype (d n)] [∀ n, DecidableEq (d n)] (ρ : (n : ℕ) → MState (d n)) (σ : (n : ℕ) → MState (d n))
  {Rsup : ℝ≥0} (hRsup : Rsup ≥ Filter.atTop.limsup (fun (n : ℕ) ↦ —log β_ ε3(ρ n‖{σ n}) / n))
  :
  (Filter.atTop.limsup (fun (n : ℕ) ↦ ⟪{ρ n ≥ₚ (Real.exp (n * (Rsup + ε4))) • (σ n).M}, ρ n⟫) ≤ 1 - ε3)
```

**`SteinsLemma.R1`**, a def, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L412).

```lean
noncomputable def R1 (ρ : MState (H i)) (ε : Prob) : ℝ≥0∞
```

**`SteinsLemma.R2`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L415).

```lean
noncomputable def R2 (ρ : MState (H i)) : ((n : ℕ) → IsFree (i := i ^ n)) → ℝ≥0∞
```

**`SteinsLemma.σ₁`**, a def, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L677).

```lean
def σ₁ : MState (H i)
```

**`SteinsLemma.σ₁_mineig`**, a def, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L680).

```lean
def σ₁_mineig
```

**`SteinsLemma.σ₁_c`**, a def, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L684).

> The sequence c\_n given in (S44). In order to handle when c = 0, we've replaced the
> (Real.log 3) / n term with (Real.log 3) / (max n 1).

```lean
def σ₁_c (n : ℕ) : ℝ
```

**`SteinsLemma.σ₁_c_littleO`**, a lemma, [line 767](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L767).

```lean
lemma σ₁_c_littleO : (fun n : ℕ ↦ σ₁_c i n + Real.log 3) =o[Filter.atTop] (fun x ↦ (x : ℝ))
```

**`SteinsLemma.Lemma7`**, a theorem, [line 1752](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L1752). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Lemma 7 from the paper. We write `ε'` for their `\tilde{ε}`.

```lean
theorem Lemma7 (ρ : MState (H i)) {ε : Prob} (hε : 0 < ε ∧ ε < 1) (σ : (n : ℕ) → IsFree (i := i ^ n)) :
    (R2 ρ σ ≥ R1 ρ ε) →
    ∀ ε' : Prob, (hε' : 0 < ε' ∧ ε' < ε) → -- ε' is written as \tilde{ε} in the paper.
    ∃ σ' : (n : ℕ) → IsFree (i := i ^ n),
    R2 ρ σ' - R1 ρ ε ≤ .ofNNReal (1 - ε' : Prob) * (R2 ρ σ - R1 ρ ε)
```

**`SteinsLemma.Lemma7_improver`**, a def, [line 1953](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L1953).

> Lemma 7 gives us a way to repeatedly "improve" a sequence σ to one with a smaller gap between R2 and R1.
> The paper paints this as pretty much immediate from Lemma7, but we need to handle the case where R2 is below
> R1.

```lean
noncomputable def Lemma7_improver (ρ : MState (H i)) {ε : Prob} (hε : 0 < ε ∧ ε < 1) {ε' : Prob} (hε' : 0 < ε' ∧ ε' < ε) :
    --The parameters above are the "fixed" parameters that we'll improve
    --It takes one sequence of free states, `(n : ℕ) → IsFree (i := i ^ n)`, and gives a new one
    ((n : ℕ) → IsFree (i := i ^ n)) → ((n : ℕ) → IsFree (i := i ^ n))
```

**`SteinsLemma.Lemma7_gap`**, a theorem, [line 1964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L1964). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Lemma7\_improver does its job at shrinking the gap.

```lean
theorem Lemma7_gap (ρ : MState (H i)) {ε : Prob} (hε : 0 < ε ∧ ε < 1) {ε' : Prob} (hε' : 0 < ε' ∧ ε' < ε) :
    ∀ σ,
      letI σ' := Lemma7_improver ρ hε hε' σ;
      R2 ρ σ' - R1 ρ ε ≤ .ofNNReal (1 - ε' : Prob) * (R2 ρ σ - R1 ρ ε)
```

**`SteinsLemma.GeneralizedQSteinsLemma`**, a theorem, [line 1980](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L1980). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Theorem 1 in https://arxiv.org/pdf/2408.02722v3

```lean
theorem GeneralizedQSteinsLemma {i : ι} (ρ : MState (H i)) {ε : Prob} (hε : 0 < ε ∧ ε < 1) :
    Filter.atTop.Tendsto (fun n ↦ —log β_ ε(ρ ⊗ᵣ^[n]‖IsFree) / n) (𝓝 (𝑅ᵣ∞ ρ))
```

**`SteinsLemma.limit_hypotesting_eq_limit_rel_entropy`**, a theorem, [line 2114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean#L2114). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Theorem 4, which is also called the Generalized quantum Stein's lemma in Hayashi & Yamasaki.
> What they state as an equality of limits, which don't exist per se in Mathlib, we state as the existence
> of a number (which happens to be `RegularizedRelativeEntResource`) to which both sides converge.

```lean
theorem limit_hypotesting_eq_limit_rel_entropy (ρ : MState (H i)) (ε : Prob) (hε : 0 < ε ∧ ε < 1) :
    ∃ d : ℝ≥0,
      Filter.atTop.Tendsto (fun n ↦ —log β_ ε(ρ ⊗ᵣ^[n]‖IsFree) / n) (𝓝 d)
      ∧
      Filter.atTop.Tendsto (fun n ↦ (⨅ σ ∈ IsFree, 𝐃(ρ ⊗ᵣ^[n]‖σ)) / n) (𝓝 d)
```

## Depends on

- [QuantumInfo.ResourceTheory.FreeState](freestate.md)
- [QuantumInfo.ResourceTheory.HypothesisTesting](hypothesistesting.md)

## Proof depends on

- [Pinching channels](../channels/pinching.md)
- [QuantumInfo.ForMathlib.Filter](../formathlib/filter.md)
- [QuantumInfo.ForMathlib.HermitianMat.Jordan](../formathlib/hermitianmat/jordan.md)
- [QuantumInfo.ForMathlib.LimSupInf](../formathlib/limsupinf.md)

## Sources

- [QuantumInfo/ResourceTheory/SteinsLemma.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/SteinsLemma.lean)
