---
declaration: theorem
origin: cited
lean: Erdos15.erdos_15
statement: formalized
---

# Erdős Problem 15: Convergence of Series with Primes

> *Reference:* [erdosproblems.com/15](https://www.erdosproblems.com/15)

*Quoted from [FormalConjectures/ErdosProblems/15.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/15.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/15](https://www.erdosproblems.com/15).

The file states 1 research or textbook statement: 1 open.

## `Erdos15.erdos_15`

Open: stated without proof.

> Is it true that $\sum_{n=1}^\infty(-1)^n\frac{n}{p_n}$ converges,
> where $p_n$ is the sequence of primes?
>
> Note: In the problem statement, $p_n$ is the $n$-th prime, indexed such that $p_1=2, p_2=3, \ldots$.
> We 0-index here to reflect how Nat.nth works.
>
> Note: convergence here is convergence of the sequence of partial sums, which is what the
> problem asks about. `Summable` would be the wrong notion: it is unconditional summability,
> equivalent over $\mathbb{R}$ to absolute convergence, and $\sum_n n/p_n$ diverges.

```lean
theorem erdos_15 :
    ∃ l : ℝ, Tendsto (fun N => ∑ k ∈ Finset.range N,
      (-1 : ℝ) ^ (k + 1) * (k + 1) / (k.nth Nat.Prime)) atTop (𝓝 l)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/15.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/15.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/15.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/15.lean)
- [erdosproblems.com/15](https://www.erdosproblems.com/15)
