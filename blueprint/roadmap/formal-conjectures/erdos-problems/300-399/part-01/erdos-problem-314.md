---
declaration: theorem
origin: cited
lean: Erdos314.erdos_314
statement: formalized
---

# Erdős Problem 314

> *References:*
> - [erdosproblems.com/314](https://www.erdosproblems.com/314)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [LiSt24] J. Lim and Steinerberger, S., *On differences of two harmonic numbers*.
>   arXiv:2405.11354 (2024).

*Quoted from [FormalConjectures/ErdosProblems/314.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/314.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/314](https://www.erdosproblems.com/314).

The file states 1 research or textbook statement: 1 solved.

## `Erdos314.erdos_314`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos314.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos314.lean).

> Let $n\geq 1$ and let $m$ be minimal such that $\sum_{n\leq k\leq m}\frac{1}{k}\geq 1$. We define
>
> $$\epsilon(n) = \sum_{n\leq k\leq m}\frac{1}{k}-1.$$
>
> How small can $\epsilon(n)$ be? Is it true that
>
> $$\liminf n^2\epsilon(n)=0?$$
>
> This is true, and shown by Lim and Steinerberger [LiSt24], who further proved that, for any
> $\delta>0$, there exist infinitely many $n$ and $m$ such that
>
> $$n^2\left\lvert \sum_{n\leq k\leq m}\frac{1}{k}-1\right\rvert\ll \frac{1}{(\log n)^{5/4-\delta}}.$$
>
> Erdős and Graham (and also Lim and Steinerberger) believe that the exponent of $2$ is best
> possible here, in that $\liminf \epsilon(n) n^{2+\delta}=\infty$ for all $\delta>0$.

```lean
theorem erdos_314 :
    atTop.liminf (fun n : ℕ => (n : ℝ) ^ 2 * epsilon n) = 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/314.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/314.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/314.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/314.lean)
- [erdosproblems.com/314](https://www.erdosproblems.com/314)
