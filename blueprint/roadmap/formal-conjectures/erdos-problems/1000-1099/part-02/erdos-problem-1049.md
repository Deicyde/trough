---
declaration: theorem
origin: cited
lean: Erdos1049.erdos_1049, Erdos1049.erdos_1049.variants.geq_2_integer, Erdos1049.lambert_series_eq_num_divisor_sum
statement: formalized
---

# Erdős Problem 1049

> *References:*
> - [erdosproblems.com/1049](https://www.erdosproblems.com/1049)
> - [Er48] Erdős, P., On arithmetical properties of Lambert series. J. Indian Math. Soc. (N.S.)
>   (1948), 63-66.

*Quoted from [FormalConjectures/ErdosProblems/1049.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1049.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1049](https://www.erdosproblems.com/1049).

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result.

## `Erdos1049.erdos_1049`

Open: stated without proof.

> Let $t>1$ be a rational number. Is
> $\sum_{n=1}^\infty\frac{1}{t^n-1}=\sum_{n=1}^\infty \frac{\tau(n)}{t^n}$ irrational, where
> $\tau(n)$ counts the divisors of $n$?
>
> A conjecture of Chowla.

```lean
theorem erdos_1049 :
    ∀ t : ℚ, t > 1 → Irrational (∑' n : ℕ+, 1 / ((t : ℝ) ^ (n : ℕ) - 1))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1049.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1049.lean#L43).

## `Erdos1049.erdos_1049.variants.geq_2_integer`

Solved: stated here; a Lean proof is at [https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L96-L107](https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L96-L107).

> Erdős [Er48] proved that this is true if $t\geq 2$ is an integer.

```lean
theorem erdos_1049.variants.geq_2_integer :
     ∀ t : ℤ, t ≥ 2 → Irrational (∑' n : ℕ+, 1 / ((t : ℝ) ^ (n : ℕ) - 1))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1049.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1049.lean#L53).

## `Erdos1049.lambert_series_eq_num_divisor_sum`

Textbook result, proved here.

> The classical Lambert series identity: $\sum_{n=1}^\infty \frac{1}{t^n - 1} =
> \sum_{n=1}^\infty \frac{\tau(n)}{t^n}$, where $\tau(n)$ counts the divisors of $n$.

```lean
theorem lambert_series_eq_num_divisor_sum : ∀ t : ℚ,
     ∑' n : ℕ+, 1 / ((t : ℝ) ^ (n : ℕ) - 1) =
     ∑' n : ℕ+, (n : ℕ).divisors.card / ((t : ℝ) ^ (n : ℕ))
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1049.lean, line 250](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1049.lean#L250).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1049.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1049.lean)
- [erdosproblems.com/1049](https://www.erdosproblems.com/1049)
