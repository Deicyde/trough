---
declaration: theorem
origin: cited
lean: OeisA212334.conjecture_1, OeisA212334.conjecture_2
statement: formalized
---

# Balanced walks on a 4-dimensional cubic lattice with neighbor steps

> The sequence $a(n)$ counts the words over a $4$-ary alphabet (either empty or starting with the
> first letter) in which each letter occurs $n$ times and adjacent letters are equal or adjacent in
> the alphabet. Equivalently,
>
> $$a(n) = \sum_{k=0}^{n-1} \binom{n}{k} \binom{n-1}{k} \binom{n+k-1}{k}^2$$
>
> for $n \ge 1$ and $a(0) = 1$.
>
> *References:*
> - [A212334](https://oeis.org/A212334)

*Quoted from [FormalConjectures/OEIS/212334.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212334.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA212334.conjecture_1`

Open: stated without proof.

> "It appears that for primes $p \ge 5$, $a(p) \equiv 1 \pmod{p^5}$."
> - _Peter Bala_, Dec 12 2021

```lean
theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hp5 : 5 ≤ p) :
    a p % (p ^ 5) = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212334.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212334.lean#L66).

## `OeisA212334.conjecture_2`

Open: stated without proof.

> "Conjecture: for $r \ge 2$, and all primes $p \ge 5$,
> $a(p^r) \equiv a(p^{r-1}) \pmod{p^{3r+3}}$."
> - _Peter Bala_, Oct 13 2022

```lean
theorem conjecture_2 (p r : ℕ) (hp : p.Prime) (hp5 : 5 ≤ p) (hr2 : 2 ≤ r) :
    a (p ^ r) % (p ^ (3 * r + 3)) = a (p ^ (r - 1)) % (p ^ (3 * r + 3))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212334.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212334.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/212334.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212334.lean)
- [A212334](https://oeis.org/A212334)
