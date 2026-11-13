---
declaration: theorem
origin: cited
lean: Erdos839.erdos_839.parts.i, Erdos839.erdos_839.parts.ii
statement: formalized
---

# Erdős Problem 839

> *References:*
> - [erdosproblems.com/839](https://www.erdosproblems.com/839)
> - [Er78f] Erdős, P., *Problems in number theory and combinatorics*, Proc. Sixth Manitoba Conf. on
>   Numerical Math. (1978), 35-58.
> - [Er92c] Erdős, P., *Some of my favourite unsolved problems*, J. Combin. Theory Ser. A (1992).
>
> See also [Erdős Problem 359](https://www.erdosproblems.com/359) and
> [Erdős Problem 867](https://www.erdosproblems.com/867).

*Quoted from [FormalConjectures/ErdosProblems/839.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/839.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/839](https://www.erdosproblems.com/839).

The file states 2 research or textbook statements: 2 open.

## `Erdos839.erdos_839.parts.i`

Open: stated without proof.

> Erdős Problem 839 (Part 1) [Er78f][Er92c]:
>
> Let $1 \leq a_1 < a_2 < \cdots$ be a strictly increasing sequence of positive integers
> such that no $a_i$ is the sum of consecutive $a_j$ for $j < i$.
> Is it true that $\limsup a_n / n = \infty$?

```lean
theorem erdos_839.parts.i :
    ∀ (a : ℕ → ℕ), (∀ n, 1 ≤ a n) → StrictMono a → SumOfConsecutiveFree a →
    atTop.limsup (fun n : ℕ => (a n : ℝ≥0∞) / n) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/839.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/839.lean#L55).

## `Erdos839.erdos_839.parts.ii`

Open: stated without proof.

> Erdős Problem 839 (Part 2, stronger) [Er78f][Er92c]:
>
> Let $1 \leq a_1 < a_2 < \cdots$ be a strictly increasing sequence of positive integers
> such that no $a_i$ is the sum of consecutive $a_j$ for $j < i$.
> Is it true that $\lim_{x \to \infty} \frac{1}{\log x} \sum_{a_n < x} \frac{1}{a_n} = 0$?
>
> This is equivalent to asking whether the range $\{a_1,a_2,\ldots\}$ has logarithmic density zero
> (see `Set.HasLogDensity`).

```lean
theorem erdos_839.parts.ii :
    ∀ (a : ℕ → ℕ), (∀ n, 1 ≤ a n) → StrictMono a → SumOfConsecutiveFree a →
    Set.HasLogDensity (Set.range a) 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/839.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/839.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/839.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/839.lean)
- [erdosproblems.com/839](https://www.erdosproblems.com/839)
