---
declaration: theorem
origin: cited
lean: OeisA91591.conjecture
statement: formalized
---

# Number of pairs of twin primes between $n^2$ and $(n+1)^2$

> $a(n)$ is the number of pairs of twin primes between $n^2$ and $(n+1)^2$.
> This counts the number of primes $p$ such that $p$ and $p+2$ are both prime,
> and the entire twin prime pair $(p, p+2)$ lies strictly between $n^2$ and $(n+1)^2$.
> That is, $n^2 < p$ and $p + 2 < (n+1)^2$.
>
> *References:*
> - [A091591](https://oeis.org/A091591)

*Quoted from [FormalConjectures/OEIS/91591.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/91591.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA91591.conjecture`

Open: stated without proof.

> It is conjectured that $a(n)>0$ for all $n>122$.
> Proving this would also prove Legendre's conjecture that there is a prime
> between $n^2$ and $(n+1)^2$. - _T. D. Noe_, Feb 28 2007

```lean
theorem conjecture :
    ∀ n : ℕ, n > 122 → a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/91591.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/91591.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/91591.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/91591.lean)
- [A091591](https://oeis.org/A091591)
