---
declaration: module
origin: cited
lean: H₁_nonneg, H₁_le_1, H₁_le_exp_m1, Hₛ_nonneg, Hₛ_le_log_d, Hₛ_constant_eq_zero, Hₛ_uniform, Hₛ_coin
statement: formalized
proof: formalized
---

# Shannon entropy

The module `QuantumInfo.ClassicalInfo.Entropy`, [QuantumInfo/ClassicalInfo/Entropy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean): 16 declarations, 14 with a docstring, 8 listed as significant.

> Definitions and facts about the Shannon entropy function -x*ln(x), both on a single
> variable and on a distribution.
>
> There is significant overlap with `Real.negMulLog` and `Real.binEntropy` in Mathlib,
> and probably these files could be combined in some form.

**`H₁`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L28).

> The one-event entropy function, H₁(p) = -p*ln(p). Uses nits.

```lean
def H₁ : Prob → ℝ
```

**`H₁_zero_eq_zero`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L33).

> H₁ of 0 is zero.

```lean
lemma H₁_zero_eq_zero : H₁ 0 = 0
```

**`H₁_one_eq_zero`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L38).

> H₁ of 1 is zero.

```lean
lemma H₁_one_eq_zero : H₁ 1 = 0
```

**`H₁_nonneg`**, a theorem, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L42). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Entropy is nonnegative.

```lean
theorem H₁_nonneg (p : Prob) : 0 ≤ H₁ p
```

**`H₁_le_1`**, a theorem, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L47). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Entropy is less than 1.

```lean
theorem H₁_le_1 (p : Prob) : H₁ p < 1
```

**`H₁_le_exp_m1`**, a theorem, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L57). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Entropy is at most 1/e.

```lean
theorem H₁_le_exp_m1 (p : Prob) : H₁ p ≤ Real.exp (-1)
```

**`H₁_concave`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L61).

```lean
lemma H₁_concave : ∀ (x y : Prob), ∀ (p : Prob), p[H₁ x ↔ H₁ y] ≤ H₁ (p[x ↔ y])
```

**`Hₛ`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L86).

> The Shannon entropy of a discrete distribution, H(X) = ∑ H₁(p\_x).

```lean
def Hₛ (d : ProbDistribution α) : ℝ
```

**`Hₛ_eq_expect_val`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L91).

> Shannon entropy is the expected negative logarithm of the outcome probability.
> Zero-probability outcomes contribute zero to the expectation.

```lean
lemma Hₛ_eq_expect_val (d : ProbDistribution α) :
    Hₛ d = ProbDistribution.expect_val ⟨fun x ↦ -Real.log (d x), d⟩
```

**`Hₛ_nonneg`**, a theorem, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L97). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Shannon entropy of a distribution is nonnegative.

```lean
theorem Hₛ_nonneg (d : ProbDistribution α) : 0 ≤ Hₛ d
```

**`Hₛ_concave`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L101).

> Shannon entropy is concave under convex mixtures of distributions.

```lean
lemma Hₛ_concave (d₁ d₂ : ProbDistribution α) (p : Prob) :
    p[Hₛ d₁ ↔ Hₛ d₂] ≤ Hₛ (p[d₁ ↔ d₂])
```

**`Hₛ_le_log_d`**, a theorem, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L108). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Shannon entropy of a distribution is at most ln d.

```lean
theorem Hₛ_le_log_d (d : ProbDistribution α) : Hₛ d ≤ Real.log (Fintype.card α)
```

**`Hₛ_constant_eq_zero`**, a theorem, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L129). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The shannon entropy of a constant variable is zero.

```lean
theorem Hₛ_constant_eq_zero {i : α} : Hₛ (ProbDistribution.constant i) = 0
```

**`Hₛ_uniform`**, a theorem, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L133). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Shannon entropy of a uniform distribution is ln d.

```lean
theorem Hₛ_uniform [Nonempty α] :
    Hₛ (ProbDistribution.uniform (α := α)) = Real.log (Finset.univ.card (α := α))
```

**`Hₛ_coin`**, a theorem, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L138). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Shannon entropy of two-event distribution.

```lean
theorem Hₛ_coin (p : Prob) : Hₛ (ProbDistribution.coin p) = Real.binEntropy p
```

**`Hₛ_eq_of_multiset_map_eq`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean#L141).

```lean
lemma Hₛ_eq_of_multiset_map_eq (d₁ : ProbDistribution α) (d₂ : ProbDistribution β)
    (h : Multiset.map d₁.prob Finset.univ.val = Multiset.map d₂.prob Finset.univ.val) :
    Hₛ d₁ = Hₛ d₂
```

## Depends on

- [Distributions on finite sets](distribution.md)

## Proof depends on

- [QuantumInfo.ClassicalInfo.ForMathlib.Analysis.SpecialFunctions.Log.NegMulLog](formathlib/analysis-specialfunctions-log-negmullog.md)

## Sources

- [QuantumInfo/ClassicalInfo/Entropy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Entropy.lean)
