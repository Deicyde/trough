---
declaration: theorem
origin: cited
lean: OeisA110854.conjecture
statement: formalized
---

# Conjectures associated with A110854

> $a(n) = \mathrm{prime}(2n+2) - \mathrm{prime}(2n+1) - \mathrm{prime}(2n) + \mathrm{prime}(2n-1)$,
> where $\mathrm{prime}(k)$ is the $k$-th prime number.
>
> *References:*
> - [A110854](https://oeis.org/A110854)

*Quoted from [FormalConjectures/OEIS/110854.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/110854.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements and 5 API statements, counted here but not shown.

## `OeisA110854.conjecture`

Open: stated without proof.

> Do the absolute values cover A004275?
> A004275 is $1$ together with the nonnegative even numbers.
> The conjecture asks whether every member of A004275 occurs as $|a(n)|$ for some
> term of the sequence.

```lean
theorem conjecture :
  ∀ d : ℕ, (d = 1 ∨ Even d) → ∃ n > 0, d = (a n).natAbs
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/110854.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/110854.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/110854.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/110854.lean)
- [A110854](https://oeis.org/A110854)
