---
declaration: theorem
origin: cited
lean: Erdos771.erdos_771, Erdos771.erdos_771.variants.erdos_graham_lower, Erdos771.erdos_771.variants.alon_freiman_upper
statement: formalized
---

# Erdős Problem 771

> *References:*
> - [erdosproblems.com/771](https://www.erdosproblems.com/771)
> - [Er89] Erdős, P., *Some problems and results on combinatorial number theory*. Graph theory and
>   its applications: East and West (Jinan, 1986), Ann. New York Acad. Sci. 576 (1989), 132-145.
> - [AlFr88] Alon, N. and Freiman, G., *On sums of subsets of a set of integers*. Combinatorica 8
>   (1988), 297-306.

*Quoted from [FormalConjectures/ErdosProblems/771.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/771.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/771](https://www.erdosproblems.com/771).

The file states 3 research or textbook statements: 3 solved. It also has 3 API statements, counted here but not shown.

## `Erdos771.erdos_771`

Solved: stated here without proof.

> Let $f(n)$ be maximal such that, for every $m\geq 1$, there exists some
> $S\subseteq \{1,\ldots,n\}$ with $\lvert S\rvert=f(n)$ such that $m\neq \sum_{a\in A}a$ for all
> $A\subseteq S$.
>
> Is it true that
>
> $$f(n) = \left(\frac{1}{2}+o(1)\right)\frac{n}{\log n}?$$
>
> The answer is yes: the lower bound is due to Erdős and Graham and the upper bound to Alon and
> Freiman [AlFr88].

```lean
theorem erdos_771 :
    (fun n : ℕ ↦ (f n : ℝ)) ~[atTop] fun n : ℕ ↦ (n : ℝ) / (2 * Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/771.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/771.lean#L78).

## `Erdos771.erdos_771.variants.erdos_graham_lower`

Solved: stated here without proof.

> Erdős and Graham proved the lower bound
>
> $$f(n)\geq \left(\frac{1}{2}+o(1)\right)\frac{n}{\log n}.$$
>
> Their proof is to note that we can assume that $m< \binom{n+1}{2}$ and then, for any $m$, take
> $S=\{ kp : 1\leq k\lt \frac{n}{p}\}$ where $p$ is the least prime that does not divide $m$
> (so $p<(2+o(1))\log n$).

```lean
theorem erdos_771.variants.erdos_graham_lower :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, (1 / 2 - ε) * ((n : ℝ) / Real.log n) ≤ f n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/771.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/771.lean#L90).

## `Erdos771.erdos_771.variants.alon_freiman_upper`

Solved: stated here without proof.

> The complementary bound
>
> $$f(n) \leq \left(\frac{1}{2}+o(1)\right)\frac{n}{\log n}$$
>
> was proved by Alon and Freiman [AlFr88], who chose $m$ as the least common multiple of
> $\{1,\ldots,s\}$ where $s$ is maximal such that $m\leq \frac{n^2}{20(\log n)^2}$.

```lean
theorem erdos_771.variants.alon_freiman_upper :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, (f n : ℝ) ≤ (1 / 2 + ε) * ((n : ℝ) / Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/771.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/771.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/771.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/771.lean)
- [erdosproblems.com/771](https://www.erdosproblems.com/771)
