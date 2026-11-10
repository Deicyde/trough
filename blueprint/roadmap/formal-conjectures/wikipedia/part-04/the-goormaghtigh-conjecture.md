---
declaration: theorem
origin: cited
lean: Goormaghtigh.goormaghtigh_conjecture
statement: formalized
---

# The Goormaghtigh conjecture

> A repunit is a number whose digits in some base are all $1$. Here a nontrivial representation has
> at least three digits. The Goormaghtigh conjecture says that $31$ and $8191$ are the only numbers
> having nontrivial repunit representations in two different bases.
>
> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Goormaghtigh_conjecture)
> * J. Grantham,
>   [No new Goormaghtigh primes up to $10^{700}$](https://math.colgate.edu/~integers/y98/y98.pdf)

*Quoted from [FormalConjectures/Wikipedia/Goormaghtigh.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Goormaghtigh.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `Goormaghtigh.goormaghtigh_conjecture`

Open: stated without proof.

> The only Goormaghtigh numbers are $31$ and $8191$.

```lean
theorem goormaghtigh_conjecture (N : ℕ) (hN : IsGoormaghtighNumber N) :
    N = 31 ∨ N = 8191
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Goormaghtigh.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Goormaghtigh.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Goormaghtigh.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Goormaghtigh.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Goormaghtigh_conjecture)
