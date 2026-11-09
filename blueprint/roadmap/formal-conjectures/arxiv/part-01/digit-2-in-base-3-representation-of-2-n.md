---
declaration: theorem
origin: cited
lean: Arxiv.«2107.12475».CollatzLike
statement: formalized
---

# Digit $2$ in base $3$ representation of $2^n$

> *References:*
> - [Some Unconventional Problems in Number Theory](https://doi.org/10.2307/2689842)
>   by *Paul Erdös*, Mathematics Magazine 52, no. 2, p. 67, 1979
> - [arxiv/2107.12475](https://arxiv.org/abs/2107.12475)
>   **Hardness of busy beaver value BB(15)** by *Tristan Stérin, Damien Woods*
> - [Hardness of Busy Beaver Value BB(15)](https://doi.org/10.1007/978-3-031-72621-7_9)
>   by *Tristan Stérin, Damien Woods*, Reachability Problems, Lecture Notes in Computer Science
>   15050, Springer, Cham (2024)

*Quoted from [FormalConjectures/Arxiv/2107.12475/CollatzLike.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2107.12475/CollatzLike.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Arxiv.«2107.12475».CollatzLike`

Open: stated without proof.

> For $n > 8$, $2^n$ is not the sum of distinct powers of $3$. Expressed here in terms of the base $3$ digits of $2^n$.
>
> This conjecture is equivalent to the non-halting of a $15$-state $2$-symbol Turing Machine.
> The Turing Machine version is formalized in
> [cryptids](https://github.com/google-deepmind/cryptids/blob/main/Cryptids/Semantics/ErdosTernary15.lean):
> `ConjectureMachines.ErdosTernary15.halts_erdosTernary15_iff_exists_counterexample` proves that
> this machine halts on the blank tape if and only if some $2^n$ with $n > 8$ has no digit $2$ in
> base $3$. The repository also proves this for Tristan Stérin's $14$-state machine.
>
> Source: *Hardness of Busy Beaver Value BB(15)*: https://link.springer.com/chapter/10.1007/978-3-031-72621-7_9
> This is also https://arxiv.org/abs/2107.12475.

```lean
theorem CollatzLike (n : ℕ) (hn : 8 < n) : 2 ∈ Nat.digits 3 (2^n)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2107.12475/CollatzLike.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2107.12475/CollatzLike.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2107.12475/CollatzLike.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2107.12475/CollatzLike.lean)
- [Some Unconventional Problems in Number Theory](https://doi.org/10.2307/2689842)
