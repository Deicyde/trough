---
declaration: theorem
origin: cited
lean: OeisA190363.conjecture
statement: formalized
---

# Sequence $a(n) = n + \lfloor n r / t \rfloor + \lfloor n s / t \rfloor$

> The sequence $a(n)$ is given by $a(n) = n + \lfloor n r / t \rfloor + \lfloor n s / t \rfloor$
> where $r = 1$, $s = \sqrt{5/4}$, and $t = \sqrt{4/5}$. Equivalently,
>
> $$a(n) = 2n + \lfloor n \sqrt{5/4} \rfloor + \lfloor n/4 \rfloor.$$
>
> *References:*
> - [A190363](https://oeis.org/A190363)

*Quoted from [FormalConjectures/OEIS/190363.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/190363.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA190363.conjecture`

Solved: stated here without proof.

> Conjecture: $a(n)$ satisfies the linear recurrence with constant coefficients
> $0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1$, i.e.,
> $a(n + 21) = a(n + 17) + a(n + 4) - a(n)$ for $n \ge 1$.
> - _Harvey P. Dale_, Jan 28 2025
>
> The conjecture is false: the recurrence first fails at $n = 140$, i.e. for the term
> $a(140 + 21) = a(161) = 543 \ne 542 = a(157) + a(144) - a(140)$.
>
> Since
> $\lim_{n\to\infty} \frac{a(n)}{n} = \frac{9}{4} + \frac{\sqrt{5}}{2}$ is irrational,
> no linear recurrence with constant integer coefficients can hold. Indeed, it follows
> from known results that if $a(n)$ satisfies a linear recurrence with constant integer coefficients
> and $\lim_{n \to \infty} \frac{a_n}{n} = \alpha$ exists, then $\alpha$ must be rational.

```lean
theorem conjecture :
    ¬ ∀ n : ℕ, 1 ≤ n → (a (n + 21) : ℤ) = a (n + 17) + a (n + 4) - a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/190363.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/190363.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/190363.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/190363.lean)
- [A190363](https://oeis.org/A190363)
