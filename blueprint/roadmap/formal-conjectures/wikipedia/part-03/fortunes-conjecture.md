---
declaration: theorem
origin: cited
lean: FortuneConjecture.fortune_conjecture
statement: formalized
---

# Fortune's Conjecture

> A *Fortunate number* is the smallest integer $m > 1$ such that $p_n\\# + m$ is prime,
> where $p_n\\#$ denotes the primorial of the $n$-th prime — equivalently, the product
> of the first $n$ primes.
>
> **Fortune's Conjecture** asserts that every Fortunate number is prime — equivalently,
> that no Fortunate number is composite.
>
> The conjecture is named after the social anthropologist Reo Fortune, who proposed it.
> The first few Fortunate numbers are $3, 5, 7, 13, 23, 17, 19, 23, 37, 61, \ldots$
> (OEIS A005235); all known values are prime.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Fortunate_number)
> - [OEIS A005235](https://oeis.org/A005235)
> - [PrimePages glossary entry](https://primes.utm.edu/glossary/xpage/FortunateNumber.html)
> - [PlanetMath: Fortune's conjecture](https://planetmath.org/fortunesconjecture)

*Quoted from [FormalConjectures/Wikipedia/FortuneConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FortuneConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 API statements, counted here but not shown.

## `FortuneConjecture.fortune_conjecture`

Open: stated without proof.

> **Fortune's Conjecture**: Every Fortunate number is prime.

```lean
theorem fortune_conjecture :
    (∀ n : ℕ, Nat.Prime (fortunateNumber n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FortuneConjecture.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FortuneConjecture.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FortuneConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FortuneConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Fortunate_number)
