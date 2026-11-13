---
declaration: theorem
origin: cited
lean: GoodmanConjecture.goodman_conjecture
statement: formalized
---

# Goodman's conjecture on coefficients of $p$-valent functions

> A regular (analytic) function is **$p$-valent** on the unit disk if it assumes each value at most
> $p$ times there, and some value exactly $p$ times. For such a function $f(z) = \sum_{n \ge 1} b_n z^n$
> (so $f(0) = 0$), **Goodman's conjecture** (1948) asserts that its coefficients satisfy
>
> $$|b_n| \le \sum_{k=1}^{p} \frac{2k (n+p)!}{(p-k)!\,(p+k)!\,(n-p-1)!\,(n^2-k^2)} |b_k|
> \qquad (n > p).$$
>
> This generalises the classical coefficient bounds for univalent functions (the case $p = 1$,
> where the bound reads $|b_n| \le n\,|b_1|$, i.e. $|b_n| \le n$ under the classical normalisation
> $b_1 = 1$) to $p$-valent functions. It has been verified in several special cases, including
> $p$-valent typically-real functions.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Goodman%27s_conjecture)
> - Goodman, A. W., *On some determinants related to $p$-valent functions*,
>   Trans. Amer. Math. Soc. 63 (1948), 175–192.

*Quoted from [FormalConjectures/Wikipedia/GoodmanConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GoodmanConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `GoodmanConjecture.goodman_conjecture`

Open: stated without proof.

> **Goodman's conjecture.** For every $p$-valent normalised function $f$ on the unit disk and every
> $n > p$, the $n$-th coefficient is bounded by the Goodman bound:
>
> $$|b_n| \le \sum_{k=1}^{p} \frac{2k (n+p)!}{(p-k)!\,(p+k)!\,(n-p-1)!\,(n^2-k^2)} |b_k|.$$

```lean
theorem goodman_conjecture (f : ℂ → ℂ) (p n : ℕ) (hf : IsPValent f p)
    (hf' : IsNormalized f) (hn : p < n) :
    ‖coeff f n‖ ≤ goodmanBound f p n
```

Category `research open`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/GoodmanConjecture.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GoodmanConjecture.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GoodmanConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GoodmanConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Goodman%27s_conjecture)
