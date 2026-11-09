---
declaration: theorem
origin: cited
lean: Erdos175.erdos_175
statement: formalized
---

# Erdős Problem 175

> *References:*
> - [erdosproblems.com/175](https://www.erdosproblems.com/175)
> - [Sa85] A. Sárközy, *On divisors of binomial coefficients, I*, J. Number Theory 20
>   (1985), 70–80.
> - [GrRa96] A. Granville and O. Ramaré, *Explicit bounds on exponential sums and the scarcity
>   of squarefree binomial coefficients*, Mathematika 43 (1996), 73–107.
> - [Ve95] G. Velammal, *Is the binomial coefficient $\binom{2n}{n}$ square free?*,
>   Hardy-Ramanujan Journal 18 (1995), 23–45.
>
> Sárközy proved the assertion for all sufficiently large `n`; Granville--Ramaré and Velammal
> independently proved the full range `n ≥ 5`.

*Quoted from [FormalConjectures/ErdosProblems/175.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/175.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/175](https://www.erdosproblems.com/175).

The file states 1 research or textbook statement: 1 solved.

## `Erdos175.erdos_175`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos175.lean#L678](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos175.lean#L678).

> Show that, for any $n\geq 5$, the binomial coefficient $\binom{2n}{n}$ is not squarefree.

```lean
theorem erdos_175 (n : ℕ) (hn : 5 ≤ n) :
    ¬ Squarefree ((2 * n).choose n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/175.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/175.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/175.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/175.lean)
- [erdosproblems.com/175](https://www.erdosproblems.com/175)
