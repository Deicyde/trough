---
declaration: theorem
origin: cited
lean: Erdos947.erdos_947
statement: formalized
---

# Erdős Problem 947

> *References:*
> - [erdosproblems.com/947](https://www.erdosproblems.com/947)
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory
>   day (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [Er50] Erdős, P., *On integers of the form $2^k+p$ and some related problems*. Summa Brasil.
>   Math. (1950), 113-123.

*Quoted from [FormalConjectures/ErdosProblems/947.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/947.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/947](https://www.erdosproblems.com/947).

The file states 1 research or textbook statement: 1 solved.

## `Erdos947.erdos_947`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos947.lean#L277](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos947.lean#L277).

> There is no exact covering system - that is, a finite collection of congruence classes
> $a_i\pmod{n_i}$ with distinct $n_i$ such that every integer satisfies exactly one of these
> congruence classes.
>
> This is true, and was proved independently by Mirsky and Newman and by Davenport and Rado; the
> Mirsky–Newman proof first appeared in [Er50]. See also [Er77c].
>
> A `StrictCoveringSystem ℤ` is a finite family of congruence classes with distinct moduli
> $n_i \geq 2$ covering $\mathbb{Z}$; the trivial exact covering system consisting of the single
> class $0 \pmod 1$ is therefore excluded.

```lean
theorem erdos_947 : ¬ ∃ c : StrictCoveringSystem ℤ, Pairwise (Disjoint on c.coset)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/947.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/947.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/947.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/947.lean)
- [erdosproblems.com/947](https://www.erdosproblems.com/947)
