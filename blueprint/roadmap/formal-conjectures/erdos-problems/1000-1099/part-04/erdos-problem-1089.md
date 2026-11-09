---
declaration: theorem
origin: cited
lean: Erdos1089.erdos_1089, Erdos1089.erdos_1089.variants.bounds_and_limit
statement: formalized
---

# Erdős Problem 1089

> *References:*
> - [erdosproblems.com/1089](https://www.erdosproblems.com/1089)
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat. Pura
>   Appl. (4) (1975), 99-108.
> - [BBS83] Bannai, Eiichi and Bannai, Etsuko and Stanton, Dennis, *An upper bound for the
>   cardinality of an $s$-distance subset in real Euclidean space. II*. Combinatorica (1983),
>   147-152.

*Quoted from [FormalConjectures/ErdosProblems/1089.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1089.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1089](https://www.erdosproblems.com/1089).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1089.erdos_1089`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1089.lean#L769](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1089.lean#L769).

> Let $g_d(n)$ be minimal such that every collection of $g_d(n)$ points in $\mathbb{R}^d$ determines
> at least $n$ many distinct distances. Estimate $g_d(n)$. In particular, does
>
> $$\lim_{d \to \infty} \frac{g_d(n)}{d^{n-1}}$$
>
> exist?
>
> A problem of Erdős [Er75f, p.105]. The answer is yes: for $n \ge 2$,
>
> $$\binom{d+1}{n-1} + 1 \le g_d(n) \le \binom{d+n-1}{n-1} + 1,$$
>
> where the upper bound is due to Bannai, Bannai and Stanton [BBS83] and the lower bound to a
> construction of Aletheia (generalising constructions for Problem 502), so that
> $g_d(n) / d^{n-1} \to 1/(n-1)!$ as $d \to \infty$.

```lean
theorem erdos_1089 :
    ∀ n : ℕ, 2 ≤ n → ∃ L : ℝ,
      Tendsto (fun d : ℕ => (g d n : ℝ) / (d : ℝ) ^ (n - 1)) atTop (𝓝 L)
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1089.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1089.lean#L60).

## `Erdos1089.erdos_1089.variants.bounds_and_limit`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1089.lean#L769](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1089.lean#L769).

> For $n \ge 2$ one has $\binom{d+1}{n-1} + 1 \le g_d(n) \le \binom{d+n-1}{n-1} + 1$ for all
> $d \ge 1$, and $g_d(n) / d^{n-1} \to 1/(n-1)!$ as $d \to \infty$.

```lean
theorem erdos_1089.variants.bounds_and_limit (n : ℕ) (hn : 2 ≤ n) :
    (∀ d, 1 ≤ d → (d + 1).choose (n - 1) + 1 ≤ g d n ∧ g d n ≤ (d + n - 1).choose (n - 1) + 1) ∧
      Tendsto (fun d : ℕ => (g d n : ℝ) / (d : ℝ) ^ (n - 1)) atTop
        (𝓝 ((1 : ℝ) / (n - 1).factorial))
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1089.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1089.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1089.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1089.lean)
- [erdosproblems.com/1089](https://www.erdosproblems.com/1089)
