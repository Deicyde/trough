---
declaration: theorem
origin: cited
lean: Erdos321.erdos_321, Erdos321.erdos_321.variants.isTheta, Erdos321.erdos_321.variants.isBigO, Erdos321.erdos_321.variants.isLittleO, Erdos321.erdos_321.variants.lower, Erdos321.erdos_321.variants.upper
statement: formalized
---

# Erdős Problem 321

> *Reference:* [erdosproblems.com/321](https://www.erdosproblems.com/321)

*Quoted from [FormalConjectures/ErdosProblems/321.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/321](https://www.erdosproblems.com/321).

The file states 6 research or textbook statements: 4 open and 2 solved.

## `Erdos321.erdos_321`

Open: stated without proof.

> Let $R(N)$ be the size of the largest $A\subseteq\{1, ..., N\}$ such that all sums
> $\sum_{n\in S} \frac{1}{n}$ are distinct for $S\subseteq A$. What is $R(N)$?

```lean
theorem erdos_321 (N : ℕ) :
    R N = erdos_321.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L49).

## `Erdos321.erdos_321.variants.isTheta`

Open: stated without proof.

> Let $R(N)$ be the size of the largest $A\subseteq\{1, ..., N\}$ such that all sums
> $\sum_{n\in S} \frac{1}{n}$ are distinct for $S\subseteq A$. What is $\Theta(R(N))$?

```lean
theorem erdos_321.variants.isTheta :
    (fun N ↦ (R N : ℝ)) =Θ[atTop] erdos_321.variants.isTheta.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L69).

## `Erdos321.erdos_321.variants.isBigO`

Open: stated without proof.

> Let $R(N)$ be the size of the largest $A\subseteq\{1, ..., N\}$ such that all sums $\sum_{n\in S} \frac{1}{n}$ are distinct for $S\subseteq A$. Find the simplest $g(N)$ such that $R(N) = O(g(N))$.

```lean
theorem erdos_321.variants.isBigO :
    (fun N ↦ (R N : ℝ)) =O[atTop] erdos_321.variants.isBigO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L79).

## `Erdos321.erdos_321.variants.isLittleO`

Open: stated without proof.

> Let $R(N)$ be the size of the largest $A\subseteq\{1, ..., N\}$ such that all sums $\sum_{n\in S} \frac{1}{n}$ are distinct for $S\subseteq A$. Find the simplest $g(N)$ such that $R(N) = o(g(N))$.

```lean
theorem erdos_321.variants.isLittleO :
    (fun N ↦ (R N : ℝ)) =o[atTop] erdos_321.variants.isLittleO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L89).

## `Erdos321.erdos_321.variants.lower`

Solved: stated here without proof.

> Let $R(N)$ be the maximal such size. Results of Bleicher and Erdős from [BlEr75] and [BlEr76b] imply that
> $$
> \frac{N}{\log N} \prod_{i=3}^{k} \log_i N \le R(N),
> $$
> valid for any $k \ge 4$ with $\log_k N \ge k$ and any $r \ge 1$ with $\log_{2r} N \ge 1$. (In these bounds $\log_i n$ denotes the $i$-fold iterated logarithm.)
>
> [BlEr75] Bleicher, M. N. and Erdős, P., _The number of distinct subsums of $\sum \sb{1}\spN\,1/i$_. Math. Comp. (1975), 29-42.
> [BlEr76b] Bleicher, Michael N. and Erdős, Paul, _Denominators of Egyptian fractions. II_. Illinois J. Math. (1976), 598-613.

```lean
theorem erdos_321.variants.lower (N k : ℕ) (hk : 4 ≤ k) (hkN : k ≤ log^[k] N) :
    N / log N * ∏ i ∈ Finset.Icc 3 k, (log^[i] N) ≤ R N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L104).

## `Erdos321.erdos_321.variants.upper`

Solved: stated here without proof.

> Let $R(N)$ be the maximal such size. Results of Bleicher and Erdős from [BlEr75] and [BlEr76b] imply that
> $$
> R(N) \le \frac{1}{\log 2} \log_r N \left( \frac{N}{\log N} \prod_{i=3}^{r} \log_i N \right),
> $$
> valid for any $k \ge 4$ with $\log_k N \ge k$ and any $r \ge 1$ with $\log_{2r} N \ge 1$. (In these bounds $\log_i n$ denotes the $i$-fold iterated logarithm.)
>
> Since `Real.log` is defined on all of $\mathbb{R}$, the condition $\log_{2r} N \ge 1$ is
> formalised as $\log_i N \ge 1$ for all $i \le 2r$, which is equivalent to it for the
> genuine iterated logarithm and ensures that every intermediate iterate is positive.
>
> [BlEr75] Bleicher, M. N. and Erdős, P., _The number of distinct subsums of $\sum \sb{1}\spN\,1/i$_. Math. Comp. (1975), 29-42.
> [BlEr76b] Bleicher, Michael N. and Erdős, Paul, _Denominators of Egyptian fractions. II_. Illinois J. Math. (1976), 598-613.

```lean
theorem erdos_321.variants.upper (N r : ℕ) (hr : 1 ≤ r) (hrN : ∀ i ≤ 2 * r, 1 ≤ log^[i] N) :
    R N ≤ 1 / log 2 * log^[r] N * N / log N * ∏ i ∈ Finset.Icc 3 r, (log^[i] N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/321.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/321.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/321.lean)
- [erdosproblems.com/321](https://www.erdosproblems.com/321)
