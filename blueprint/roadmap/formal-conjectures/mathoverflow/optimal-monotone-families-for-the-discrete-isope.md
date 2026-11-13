---
declaration: theorem
origin: cited
lean: Mathoverflow10799.mathoverflow_10799, Mathoverflow10799.mathoverflow_10799.variants.kahn_kalai_conjecture_7, Mathoverflow10799.mathoverflow_10799.variants.weak_kahn_kalai, Mathoverflow10799.discrete_isoperimetric_inequality
statement: formalized
---

# Optimal monotone families for the discrete isoperimetric inequality

> *References:*
> - [mathoverflow/10799](https://mathoverflow.net/questions/10799)
>   asked by user [*Gil Kalai*](https://mathoverflow.net/users/1532/gil-kalai)
> - [Optimal Monotone Families for the Discrete Isoperimetric Inequality](https://gilkalai.wordpress.com/ai/optimal-monotone-families-for-the-discrete-isoperimetric-inequality/)
>   by *Gil Kalai* (2026), a Polymath project with AI agents
> - [An Isoperimetric Inequality for the Hamming Cube and Integrality Gaps in Bounded-Degree
>   Graphs](https://arxiv.org/abs/math/0603218) by *Jeff Kahn* and *Gil Kalai* (2006)
> - [A Proof of the Kahn–Kalai Conjecture](https://arxiv.org/abs/2203.17207) by *Jinyoung Park*
>   and *Huy Tuan Pham* (2022)

*Quoted from [FormalConjectures/Mathoverflow/10799.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 solved and 1 textbook result. It also has 9 test statements, counted here but not shown.

## `Mathoverflow10799.mathoverflow_10799`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/408f53dc0856c0882a5e77acd24fc83b978f0bc9/FormalConjectures/Mathoverflow/10799.lean#L252](https://github.com/mo271/formal-conjectures/blob/408f53dc0856c0882a5e77acd24fc83b978f0bc9/FormalConjectures/Mathoverflow/10799.lean#L252).

> Problem: For every monotone increasing family $F$, given an interval $[s,t]$ of real numbers so
> that $t/s > 1000 \log n$ we have some $p$ in the interval $[s,t]$ so that $F$ is optimal with
> respect to $\mu_p$.
>
> This was a "missing lemma" in the work of Kahn and Kalai on threshold behavior of monotone
> properties. The related [Kahn–Kalai conjecture](https://arxiv.org/abs/math/0603218) was
> [settled by Park and Pham](https://arxiv.org/abs/2203.17207).
>
> **This conjecture is false** without the additional assumption $\mu_t(F) = 1/2$.
> A counterexample was found by Shlomo Perles (April 7, 2026).

```lean
theorem mathoverflow_10799 :
    ¬ ∀ (n : ℕ) (_ : 2 ≤ n)
    (F : Finset (Finset (Fin n))) (_ : IsMonotoneIncreasing F)
    (s t : ℝ) (_ : 0 < s) (_ : s ≤ t) (_ : t < 1)
    (_ : t / s > 1000 * Real.log n),
    ∃ p, s ≤ p ∧ p ≤ t ∧ IsOptimal p F
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Mathoverflow/10799.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean#L178).

## `Mathoverflow10799.mathoverflow_10799.variants.kahn_kalai_conjecture_7`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/kahn-kalai-conjecture-7-counterexample/blob/5446d2f/lean/MO10799CounterexampleFC.lean#L2597-L2604](https://github.com/KitaKen1/kahn-kalai-conjecture-7-counterexample/blob/5446d2f/lean/MO10799CounterexampleFC.lean#L2597-L2604).

> Conjecture 7 from Kahn–Kalai 2006: a fixed-`1000` variant of the original
> conjecture, with the additional assumption that $t$ is the critical probability for $F$,
> namely $\mu_t(F) = 1/2$.
>
> This variant is false by a counterexample due to Sahar Diskin and Uri Kreitner;
> see the [MathOverflow discussion](https://mathoverflow.net/questions/10799/optimal-monotone-families-for-the-discrete-isoperimetric-inequality)
> and the [counterexample note](https://gilkalai.wordpress.com/wp-content/uploads/2026/06/dual_tribes_more_readable.pdf).
> Their construction was adapted to this exact Formal Conjectures statement and
> [formalized in Lean](https://github.com/KitaKen1/kahn-kalai-conjecture-7-counterexample)
> by Kenta Kitamura (KitaKen1).

```lean
theorem mathoverflow_10799.variants.kahn_kalai_conjecture_7 :
    ¬ ∀ (n : ℕ) (_ : 2 ≤ n)
    (F : Finset (Finset (Fin n))) (_ : IsMonotoneIncreasing F)
    (s t : ℝ) (_ : 0 < s) (_ : s ≤ t) (_ : t < 1)
    (_ : μFamily t F = 1 / 2)
    (_ : t / s > 1000 * Real.log n),
    ∃ p, s ≤ p ∧ p ≤ t ∧ IsOptimal p F
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Mathoverflow/10799.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean#L202).

## `Mathoverflow10799.mathoverflow_10799.variants.weak_kahn_kalai`

Solved: stated here without proof.

> Weaker version proven by Kahn–Kalai (2006): for every fixed $\varepsilon > 0$ there is a constant
> $C = C_\varepsilon$ such that for every monotone increasing family $F$ with critical probability
> $t$, i.e. $\mu_t(F) = 1/2$, there is some $p \in [n^{-\varepsilon} t, t]$ for which $F$ is
> $(C \log(1/p), p)$-optimal.

```lean
theorem mathoverflow_10799.variants.weak_kahn_kalai :
    ∀ ε > (0 : ℝ), ∃ C > (0 : ℝ), ∀ (n : ℕ) (_ : 2 ≤ n)
    (F : Finset (Finset (Fin n))) (_ : IsMonotoneIncreasing F)
    (t : ℝ) (_ : 0 < t) (_ : t < 1) (_ : μFamily t F = 1 / 2),
    ∃ p, (n : ℝ) ^ (-ε) * t ≤ p ∧ p ≤ t ∧ IsOptimalWith C p F
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Mathoverflow/10799.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean#L218).

## `Mathoverflow10799.discrete_isoperimetric_inequality`

Textbook result, stated without proof.

> Now a famous isoperimetric relation asserts that
> (IR) $I^p(F) \ge \frac{1}{p} \mu_p(F) \log_p \mu_p(F)$
> This relation holds for monotone increasing families $F$ and $0 < p < 1$.
> It is especially famous and simple when
> $p=1/2$ and $\mu_p(F)=1/2$. In this case, it says that given a set of half the vertices of the
> discrete cube $2^X$, the number of edges between $F$ and its complement is at least $2^{n-1}$.
>
> *Note on translation:* We use `Real.logb p m` to represent the logarithm base $p$ directly.
> The factor of $p$ in the denominator (equivalent to $1/p$ in front) is consistent with the
> definition of `IsOptimal` used in the counterexample proof.

```lean
theorem discrete_isoperimetric_inequality (n : ℕ) (p : ℝ) (hp : 0 < p) (hp' : p < 1)
    (F : Finset (Finset (Fin n))) (hF : IsMonotoneIncreasing F) :
    let m := μFamily p F
    edgeBoundary n p F ≥ m * Real.logb p m / p
```

Category `textbook`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Mathoverflow/10799.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean#L238).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/10799.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/10799.lean)
- [mathoverflow/10799](https://mathoverflow.net/questions/10799)
