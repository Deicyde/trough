---
declaration: theorem
origin: cited
lean: OeisA109905.conjecture
statement: formalized
---

# Conjectures associated with A109905

> $a(n)$ is the greatest prime of the form $k(n-k)+1$, where $k$ can take values from
> $1$ to $\lfloor n/2 \rfloor$. $a(n)=0$ if no such prime exists.
>
> *References:*
> - [A109905](https://oeis.org/A109905)

*Quoted from [FormalConjectures/OEIS/109905.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109905.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA109905.conjecture`

Open: stated without proof.

> $a(n) = 0$ for $n = 1$, $6$, $30$ and $54$. Are there any others?

```lean
theorem conjecture :
    ∃ n : ℕ, n > 0 ∧ a n = 0 ∧ n ∉ ({1, 6, 30, 54} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/109905.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109905.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/109905.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/109905.lean)
- [A109905](https://oeis.org/A109905)
