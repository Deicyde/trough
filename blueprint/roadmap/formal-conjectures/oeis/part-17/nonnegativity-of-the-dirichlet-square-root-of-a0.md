---
declaration: theorem
origin: cited
lean: OeisA317940.f_nonnegative
statement: formalized
---

# Nonnegativity of the Dirichlet square root of A046644

> A317940 is the integer sequence whose value `a n` is the numerator of the
> rational sequence `f n`, where the Dirichlet convolution square of `f` is
> A046644. The auxiliary sequence A046644 is multiplicative and takes the value
> $2^{\operatorname{A005187}(e)}$ on a prime power $p^e$.
>
> The conjecture asks whether `f n` is nonnegative for every positive `n`.
> The proof reduces the problem to prime powers and constructs positive rational
> coefficients $c(e)$ satisfying
>
> $$\sum_{i=0}^e c(i)c(e-i)=2^{\operatorname{A005187}(e)}.$$
>
> The coefficients are obtained from formal power series. A positive series
> $A$ is defined by the first-order differential equation
> $A' = \frac12 D A$. A second explicitly defined series $B$ satisfies
> $B' = D B$ and has the same constant term as $A^2$; uniqueness of the
> coefficient recurrence therefore gives $A^2=B$. After rescaling the
> coefficients by $4^e$, this becomes the displayed prime-power convolution
> identity.
>
> Extending $c(e)$ multiplicatively over prime factorizations gives a positive
> arithmetic function `root` with `root * root = a046644`. Finally, the recursive
> definition of `f` is shown to be the unique Dirichlet square root with value
> one at $1$, so `f = root` and every positive-index value of `f` is positive.
>
> This route was found by first exploiting the multiplicativity recorded in the
> OEIS entry, reducing the recurrence to the exponent of a single prime, and
> then recognizing the resulting coefficient identities as a formal-power-series
> differential equation.
>
> *References:*
> - [A317940](https://oeis.org/A317940)
> - [A046644](https://oeis.org/A046644)
> - [A005187](https://oeis.org/A005187)

*Quoted from [FormalConjectures/OEIS/317940.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/317940.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA317940.f_nonnegative`

Solved: stated here; a Lean proof is at [https://domthedeveloper.github.io/crl/math/a317940/proof/A317940_verified.lean](https://domthedeveloper.github.io/crl/math/a317940/proof/A317940_verified.lean).

> "No negative terms among the first 2^20 terms. Is the sequence nonnegative?"
>
> Equivalently, the rational Dirichlet square root `f` is nonnegative at every
> positive index. Informally, the proof constructs a strictly positive
> multiplicative square root prime-power by prime-power using formal power
> series, and then identifies it with the recursively defined sequence `f`.
>
> The proof was obtained by exploiting the multiplicativity of A046644 and
> reducing the problem to its values on prime powers. The resulting convolution
> recurrence for the prime-power coefficients was recognized as a
> formal-power-series identity. A positive coefficient sequence was constructed
> through a differential equation for the generating series, extended
> multiplicatively to all positive integers, and finally identified with the
> recursively defined Dirichlet square root by uniqueness.

```lean
theorem f_nonnegative (n : ℕ) (h : n > 0) : f n ≥ 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/317940.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/317940.lean#L202).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/317940.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/317940.lean)
- [A317940](https://oeis.org/A317940)
