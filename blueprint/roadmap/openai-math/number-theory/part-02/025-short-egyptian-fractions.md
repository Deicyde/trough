---
declaration: section
origin: cited
lean: OAI.Problem337.egyptian_length_is_minimum, OAI.Problem337.main_double_log_order, OAI.Problem337.one_expansions_finite_and_bounded, OAI.Problem337.counting_double_log_order, OAI.Problem337.exact_marker_padding, OAI.Problem337.every_exact_marker_occurs, OAI.Problem337.quantitative_marked_length, OAI.Problem337.missing_denominator_semantics
statement: formalized
proof: formalized
---

# 025. Short Egyptian fractions

1 manuscript and 10 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every rational $a/b$ with $1\le a\lt b$ is a sum of $O(\log\log b)$ distinct positive unit fractions. The worst-case minimum number of terms has the same order, resolving Erdős’s conjecture on short Egyptian fractions.

## Short Egyptian fractions

We prove a conjecture of Erdős: for every sufficiently large integer *b*, every rational number $a/b$ with $1\le a\lt b$ is a sum of $O(\log\log b)$ distinct positive unit fractions, with an absolute implied constant. This order is best possible when the numerator varies. We also show that both the number of expansions of 1 with exactly *k* distinct terms and the least integer at least 2 that never occurs as a denominator in such an expansion grow doubly exponentially in *k*: their double logarithms have order *k*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

An Egyptian-fraction expansion writes a rational number as a sum of distinct unit fractions. The formalization proves that every $a/b$ with $1\le a<b$ has such an expansion and that the largest minimum length at denominator $b$ is $\Theta(\log\log b)$. If $F(k)$ counts exact $k$-term expansions of $1$, it also proves $\log\log F(k)=\Theta(k)$ and bounds every denominator in such an expansion.

Every integer $m\ge2$ occurs as a denominator in an expansion of $1$, with length eventually at most $(257/\log2+\varepsilon)\log\log m$ for every $\varepsilon>0$; padding can preserve that denominator. If $v(k)$ is the least integer at least $2$ absent from all exact $k$-term expansions of $1$, then eventually $e^{e^{k/600}}\le v(k)\le1+k^{2^{k-1}}$, and $\liminf_{k\to\infty}\log\log v(k)/k\ge\log2/257$.

## Lean: Short expansions, counting, and prescribed denominators

```lean
theorem egyptian_length_is_minimum :
    ∀ a b : ℕ, 1 ≤ a → a < b →
  (∃ n : Fin (egyptianLength a b) → ℕ,
    IsEgyptianExpansion ((a : ℚ) / (b : ℚ)) n) ∧
  (∀ k : ℕ, (∃ n : Fin k → ℕ,
    IsEgyptianExpansion ((a : ℚ) / (b : ℚ)) n) →
    egyptianLength a b ≤ k)
```

Stated in [EgyptianFractions.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L48). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L27).

```lean
theorem main_double_log_order :
    ∃ c1 c2 : ℝ, 0 < c1 ∧ 0 < c2 ∧ ∃ b0 : ℕ,
  ∀ b : ℕ, b0 ≤ b →
    c1 * Real.log (Real.log (b : ℝ)) ≤ (maxEgyptianLength b : ℝ) ∧
    (maxEgyptianLength b : ℝ) ≤ c2 * Real.log (Real.log (b : ℝ))
```

Stated in [EgyptianFractions.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L57). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 40](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L40). formalization.yaml lists it as one of the repository's main results.

```lean
theorem one_expansions_finite_and_bounded :
    (∀ k : ℕ, Set.Finite (OneExpansions k) ∧
    F k ≤ k ^ (2 ^ k - 1)) ∧
  (∀ k : ℕ, ∀ n : Fin k → ℕ, IsOneExpansion n →
    ∀ i : Fin k, n i ≤ k ^ (2 ^ i.val))
```

Stated in [EgyptianFractions.lean, line 64](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L64). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 61](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L61).

```lean
theorem counting_double_log_order :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∃ k0 : ℕ,
  ∀ k : ℕ, k0 ≤ k →
    c * (k : ℝ) ≤ Real.log (Real.log (F k : ℝ)) ∧
    Real.log (Real.log (F k : ℝ)) ≤ C * (k : ℝ)
```

Stated in [EgyptianFractions.lean, line 71](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L71). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 120](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L120). formalization.yaml lists it as one of the repository's main results.

```lean
theorem exact_marker_padding :
    ∀ r : ℕ, 3 ≤ r → ∀ n : Fin r → ℕ, IsOneExpansion n →
  ∀ m : ℕ, (∃ i : Fin r, n i = m) →
    ∃ n' : Fin (r + 1) → ℕ,
      IsOneExpansion n' ∧ ∃ i : Fin (r + 1), n' i = m
```

Stated in [EgyptianFractions.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L78). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L73).

```lean
theorem every_exact_marker_occurs :
    ∀ m : ℕ, 2 ≤ m → ∃ k : ℕ, m ∈ D k
```

Stated in [EgyptianFractions.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L85). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 80](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L80).

```lean
theorem quantitative_marked_length :
    ∀ ε : ℝ, 0 < ε → ∃ mε : ℕ, 2 ≤ mε ∧
  ∀ m : ℕ, mε ≤ m →
    ∃ k : ℕ, ∃ n : Fin k → ℕ,
      IsOneExpansion n ∧
      (∃ i : Fin k, n i = m) ∧
      (k : ℝ) ≤ (257 / Real.log 2 + ε) * Real.log (Real.log (m : ℝ))
```

Stated in [EgyptianFractions.lean, line 89](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L89). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L84).

```lean
theorem missing_denominator_semantics :
    ∀ k : ℕ,
  Set.Finite (D k) ∧
  (∃ m : ℕ, m ∈ missingDenominators k) ∧
  2 ≤ v k ∧ v k ∉ D k ∧
  (∀ m : ℕ, 2 ≤ m → m < v k → m ∈ D k) ∧
  (1 ≤ k → v k ≤ 1 + k ^ (2 ^ (k - 1)))
```

Stated in [EgyptianFractions.lean, line 98](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L98). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 93](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L93).

```lean
theorem prescribed_denominator_corollary :
    (∃ k0 : ℕ, ∀ k : ℕ, k0 ≤ k →
    Real.exp (Real.exp ((k : ℝ) / 600)) ≤ (v k : ℝ) ∧
    v k ≤ 1 + k ^ (2 ^ (k - 1))) ∧
  (Real.log 2 / 257 ≤ Filter.liminf prescribedSlope Filter.atTop ∧
    Filter.liminf prescribedSlope Filter.atTop ≤
      Filter.limsup prescribedSlope Filter.atTop ∧
    Filter.limsup prescribedSlope Filter.atTop ≤ Real.log 2) ∧
  (∀ c : ℝ, c < Real.log 2 / 257 → ∃ k0 : ℕ,
    ∀ k : ℕ, k0 ≤ k →
      Real.exp (Real.exp (c * (k : ℝ))) ≤ (v k : ℝ))
```

Stated in [EgyptianFractions.lean, line 107](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EgyptianFractions.lean#L107). Proved in [lean/OAI/NumberTheory/EgyptianFractions/Main.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/EgyptianFractions/Main.lean#L103). formalization.yaml lists it as one of the repository's main results.

## Lean: Optimal order of the shortest Egyptian-fraction expansions

```lean
theorem main :
    (∀ a b : ℕ, 1 ≤ a → a < b → ∃ ns : List ℕ, IsExpansion a b ns) ∧
    ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ 0 < c₂ ∧ ∃ b₀ : ℕ, 2 ≤ b₀ ∧
      ∀ b : ℕ, b₀ ≤ b →
        c₁ * Real.log (Real.log (b : ℝ)) ≤ (maxMinLength b : ℝ) ∧
        (maxMinLength b : ℝ) ≤ c₂ * Real.log (Real.log (b : ℝ))
```

Stated in [ShortEgyptianFractions.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ShortEgyptianFractions.lean#L17). Proved in [lean/OAI/NumberTheory/ShortEgyptian/Main.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/ShortEgyptian/Main.lean#L33).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/025.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/025.md)
