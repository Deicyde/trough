---
declaration: theorem
origin: cited
lean: OeisA11545.conjecture1, OeisA11545.conjecture2
statement: formalized
---

# $a(n)$ is the integer whose decimal digits are the first $n+1$ decimal digits of $\pi$

> *References:*
> - [A011545](https://oeis.org/A011545)

*Quoted from [FormalConjectures/OEIS/11545.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/11545.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 4 test statements, counted here but not shown.

## `OeisA11545.conjecture1`

Open: stated without proof.

> Wolfgang Haken (1977) conjectured that no term of this sequence is a perfect square,
> and estimated the probability that this conjecture is false to be smaller than $10^-9$.

```lean
theorem conjecture1 : ∀ n, ¬ IsSquare (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/11545.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/11545.lean#L70).

## `OeisA11545.conjecture2`

Open: stated without proof.

> Number of collisions occurring in a system consisting of an infinitely massive,
> rigid wall at the origin, a ball with mass m stationary at position $x_1 > 0$,
> and a ball with mass $(10^2n)m$ at position $x_2 > x_1$ and rolling toward the origin,
> assuming perfectly elastic collisions and no friction.
>
> Strictly speaking, this property, which is equivalent to the statement that the interval
> $(m\pi, \pi/\textrm{arctan}(1/m))$ does not contain an integer for all $m = 10^n$, is not
> known to be true for sure. In other words, we do not know for certain that A332045 does not
> contain a power of $10$.

```lean
theorem conjecture2 :
    ∀ n : ℕ, ¬ ∃ (k : ℤ),
      (Real.pi * (10 : ℝ) ^ n.cast < k.cast) ∧
      (k.cast < Real.pi / Real.arctan (1 / (10 : ℝ) ^ n.cast))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/11545.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/11545.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/11545.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/11545.lean)
- [A011545](https://oeis.org/A011545)
