---
declaration: theorem
origin: cited
lean: Erdos521.erdos_521
statement: formalized
---

# Erdős Problem 521

> *Reference:* [erdosproblems.com/521](https://www.erdosproblems.com/521)

*Quoted from [FormalConjectures/ErdosProblems/521.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/521.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/521](https://www.erdosproblems.com/521).

The file states 1 research or textbook statement: 1 solved. It also has 2 API statements, counted here but not shown.

## `Erdos521.erdos_521`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-521/Research/LateFourthFinal.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-521/Research/LateFourthFinal.lean).

> Let $(\epsilon_k)_{k\geq 0}$ be independently uniformly chosen at random from
> $\{-1,1\}$. If $R_n$ counts the number of real roots of
> $f_n(z)=\sum_{0\leq k\leq n}\epsilon_k z^k$ then is it true that, almost surely,
> $$\lim_{n\to \infty}\frac{R_n}{\log n}=\frac{2}{\pi}?$$
>
> The answer is no: this almost-sure limit fails. This result was obtained first by others, who
> deserve the credit for the problem; the link is to an independent machine-checked proof by
> Star Fleet Math.

```lean
theorem erdos_521 : ¬ Claim
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/521.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/521.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/521.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/521.lean)
- [erdosproblems.com/521](https://www.erdosproblems.com/521)
