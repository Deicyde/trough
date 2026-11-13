---
declaration: theorem
origin: cited
lean: Erdos288.erdos_288, Erdos288.erdos_288.variants.i2_card_eq_1, Erdos288.erdos_288.variants.k_intervals, Erdos288.erdos_288.variants.exists_k_gt_2
statement: formalized
---

# Erdős Problem 288

> *Reference:* [erdosproblems.com/288](https://www.erdosproblems.com/288)

*Quoted from [FormalConjectures/ErdosProblems/288.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/288](https://www.erdosproblems.com/288).

The file states 4 research or textbook statements: 4 open.

## `Erdos288.erdos_288`

Open: stated without proof.

> Is it true that there are only finitely many pairs of intervals $I_1$, $I_2$ such that
>
> $$
> \sum_{n_1 \in I_1} \frac{1}{n_1} + \sum_{n_2 \in I_2} \frac{1}{n_2} \in \mathbb{N}?
> $$

```lean
theorem erdos_288 : Set.Finite { I : Fin 2 → ℕ+ × ℕ+ |
    ∀ j, (I j).1 ≤ (I j).2 ∧
      ∃ n : ℕ+, (∑ j : Fin 2, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/288.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean#L37).

## `Erdos288.erdos_288.variants.i2_card_eq_1`

Open: stated without proof.

> This is still open even if $|I_2| = 1$.

```lean
theorem erdos_288.variants.i2_card_eq_1 : Set.Finite { (I, n₂) : (ℕ+ × ℕ+) × ℕ+ |
    I.1 ≤ I.2 ∧ ∃ n : ℕ+, ∑ n₁ ∈ Set.Icc I.1 I.2, (n₁⁻¹ : ℚ) + (n₂⁻¹ : ℚ) = n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/288.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean#L46).

## `Erdos288.erdos_288.variants.k_intervals`

Open: stated without proof.

> It is perhaps true with two intervals replaced by any $k$ intervals.

```lean
theorem erdos_288.variants.k_intervals : ∀ k, Set.Finite { I : Fin k → ℕ+ × ℕ+ |
    ∀ j, (I j).1 ≤ (I j).2 ∧
      ∃ n : ℕ+, (∑ j : Fin k, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/288.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean#L54).

## `Erdos288.erdos_288.variants.exists_k_gt_2`

Open: stated without proof.

> Is it true for any $k > 2$ that only finitely many $k$ intervals satisfy this condition?

```lean
theorem erdos_288.variants.exists_k_gt_2 :
    ∃ k > 2, Set.Finite { I : Fin k → ℕ+ × ℕ+ |
      ∀ j, (I j).1 ≤ (I j).2 ∧
        ∃ n : ℕ+, (∑ j : Fin k, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/288.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/288.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/288.lean)
- [erdosproblems.com/288](https://www.erdosproblems.com/288)
