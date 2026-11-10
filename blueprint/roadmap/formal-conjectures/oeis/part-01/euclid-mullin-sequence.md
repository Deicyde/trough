---
declaration: theorem
origin: cited
lean: OeisA945.every_prime_occurs
statement: formalized
---

# Euclid-Mullin sequence

> The Euclid-Mullin sequence starts with $a(1) = 2$. Each subsequent term is the smallest prime
> factor of one plus the product of all preceding terms. We extend the sequence by $a(0) = 1$ and
> write $b(n)$ for the product of the first $n$ official terms.
>
>
> *References:*
> - [A000945](https://oeis.org/A000945)
> - [Mullin63] A. A. Mullin,
>   ["Research Problem 8 (ii)"](https://doi.org/10.1090/S0002-9904-1963-11017-4),
>   *Bull. Amer. Math. Soc.* **69** (1963), p. 737.
> - [Wagstaff93] S. S. Wagstaff, Jr.,
>   ["Computing Euclid's primes"](https://oeis.org/A000945/a000945_4.pdf),
>   *Bull. Institute Combin. Applications* **8** (1993), pp. 23-32.
> - [CrandallPomerance01] R. Crandall and C. Pomerance,
>   *Prime Numbers: A Computational Perspective*, Springer (2001), p. 6.
> - A. R. Booker, "A variant of the Euclid-Mullin sequence containing every prime,"
>   [arXiv:1605.08929](https://arxiv.org/abs/1605.08929), *Journal of Integer Sequences* **19**
>   (2016), Article 16.6.4.

*Quoted from [FormalConjectures/OEIS/945.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/945.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `OeisA945.every_prime_occurs`

Open: stated without proof.

> "Does the sequence ... contain every prime? ... [It] was considered by Guy and Nowakowski
> and later by Shanks, [Wagstaff93] computed the sequence through the 43rd term. The
> computational problem inherent in continuing the sequence further is the enormous size of the
> numbers that must be factored. Already the number $a(1) \cdots a(43) + 1$ has 180 digits."
> - [CrandallPomerance01]
>
> See also [Mullin63].

```lean
theorem every_prime_occurs :
    ∀ p, p.Prime → ∃ n ≥ 1, a n = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/945.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/945.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/945.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/945.lean)
- [A000945](https://oeis.org/A000945)
