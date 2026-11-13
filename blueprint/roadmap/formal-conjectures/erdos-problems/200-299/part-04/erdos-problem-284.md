---
declaration: theorem
origin: cited
lean: Erdos284.erdos_284
statement: formalized
---

# Erdős Problem 284

> *References:*
> - [erdosproblems.com/284](https://www.erdosproblems.com/284)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique 28 (1980).
> - [Cr01] Croot, III, Ernest S., *On unit fractions with denominators in short intervals*. Acta
>   Arith. 99 (2001), 99-114. [arXiv:math/9904181](https://arxiv.org/abs/math/9904181)

*Quoted from [FormalConjectures/ErdosProblems/284.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/284.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/284](https://www.erdosproblems.com/284).

The file states 1 research or textbook statement: 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos284.erdos_284`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos284.lean#L97](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos284.lean#L97).

> Let $f(k)$ be the maximal value of $n_1$ such that there exist $n_1\lt n_2\lt \cdots \lt n_k$ with
>
> $$1=\frac{1}{n_1}+\cdots+\frac{1}{n_k}.$$
>
> Is it true that
>
> $$f(k)=(1+o(1))\frac{k}{e-1}?$$
>
> Asked by Erdős and Graham [ErGr80, p. 33]. We state it as $f(k)/k\to 1/(e-1)$, which is
> equivalent. Essentially solved by Croot [Cr01], who showed that for any $N>1$ there exists some
> $k\geq 1$ and
>
> $$N\lt n_1\lt \cdots \lt n_k \leq (e+o(1))N$$
>
> with $1=\sum \frac{1}{n_i}$. See also [erdosproblems.com/286](https://www.erdosproblems.com/286).

```lean
theorem erdos_284 :
    Tendsto (fun k : ℕ ↦ (f k : ℝ) / k) atTop (nhds (1 / (Real.exp 1 - 1)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/284.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/284.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/284.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/284.lean)
- [erdosproblems.com/284](https://www.erdosproblems.com/284)
