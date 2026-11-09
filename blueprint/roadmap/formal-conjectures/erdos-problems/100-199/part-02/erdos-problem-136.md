---
declaration: theorem
origin: cited
lean: Erdos136.erdos_136
statement: formalized
---

# Erdős Problem 136

> *References:*
> - [erdosproblems.com/136](https://www.erdosproblems.com/136)
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [BCDP22] Bennett, P. and Cushman, R. and Dudek, A. and Pralat, P., *The Erdős-Gyárfás function
>   $f(n,4,5)=\frac{5}{6}n+o(n)$ - so Gyárfás was right*. arXiv:2207.02920 (2022).
> - [JoMu22] Joos, F. and Mubayi, D., *Ramsey theory constructions from hypergraph matchings*.
>   arXiv:2208.12563 (2022).

*Quoted from [FormalConjectures/ErdosProblems/136.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/136.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/136](https://www.erdosproblems.com/136).

The file states 1 research or textbook statement: 1 solved.

## `Erdos136.erdos_136`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos136.lean#L49](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos136.lean#L49).

> Let $f(n)$ be the smallest number of colours required to colour the edges of $K_n$ such that every
> $K_4$ contains at least $5$ colours. Determine the size of $f(n)$.
>
> Asked by Erdős and Gyárfás [Er97b], who proved $\frac56 (n - 1) < f(n) < n$ and $f(9) = 8$; Erdős
> believed that the upper bound is closer to the truth. In fact $f(n) \sim \frac56 n$, as shown by
> Bennett, Cushman, Dudek and Pralat [BCDP22]; Joos and Mubayi [JoMu22] found a shorter proof.

```lean
theorem erdos_136 : Tendsto (fun n : ℕ ↦ (f n : ℝ) / (n : ℝ)) atTop (𝓝 (5 / 6 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/136.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/136.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/136.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/136.lean)
- [erdosproblems.com/136](https://www.erdosproblems.com/136)
