---
declaration: theorem
origin: cited
lean: OeisA224515.exists_xor_sq_eq
statement: formalized
---

# Existence of integers $k$ with $k^2 \operatorname{XOR} (k+1)^2 = (2n+1)^2$

> a: $a(n) = \text{least } k \text{ such that } \sqrt{k^2 \operatorname{XOR} (k+1)^2} = 2n+1$,
> $a(n) = -1 \text{ if there is no such } k$.
> This is equivalent to finding the smallest $k \in \mathbb{N}$
> such that $k^2 \oplus (k+1)^2 = (2n+1)^2$.
> We use the set infimum ($\operatorname{sInf}$) to denote the least element
> of the set of natural numbers satisfying the condition.
> Since Mathlib's `sInf` on a subset of `ℕ` gives a result in `ℕ`, this definition
> is only completely faithful to the OEIS when the set is non-empty.
> The OEIS definition implies that the set of k's is non-empty for all n.
>
> *References:*
> - [A224515](https://oeis.org/A224515)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/224515.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/224515.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 1 API statement, counted here but not shown.

## `OeisA224515.exists_xor_sq_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/224515.wip.lean#L268](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/224515.wip.lean#L268).

> Conjecture: $a(n) \ge 0$, i.e., for every $n$ there exists $k$ such that $\sqrt{k^2 \oplus (k+1)^2} = 2n+1$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem exists_xor_sq_eq (n : ℕ) : ∃ k : ℕ, Nat.xor (k ^ 2) ((k + 1) ^ 2) = (2 * n + 1) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/224515.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/224515.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/224515.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/224515.lean)
- [A224515](https://oeis.org/A224515)
