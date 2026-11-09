---
declaration: theorem
origin: cited
lean: OeisA182126.conjecture1, OeisA182126.conjecture2, OeisA182126.conjecture3
statement: formalized
---

# Product of two consecutive primes modulo the next prime

> The sequence is defined by
> $$a(n) = \mathrm{prime}(n) \cdot \mathrm{prime}(n+1) \bmod \mathrm{prime}(n+2),$$
> where $\mathrm{prime}(k)$ is the $k$-th prime number ($\mathrm{prime}(1)=2$).
>
> *References:*
> - [A182126](https://oeis.org/A182126)

*Quoted from [FormalConjectures/OEIS/182126.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182126.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 4 test statements, counted here but not shown.

## `OeisA182126.conjecture1`

Open: stated without proof.

> Conjecture: For $x > 10^9$, the most frequent value in $a(n)$, $n=1\dots x$, has form $120k$.

```lean
theorem conjecture1 (x : ℕ) (hx : 10 ^ 9 < x) (v₀ : ℕ) (hv : IsMostFrequent x v₀) :
    120 ∣ v₀
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/182126.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182126.lean#L86).

## `OeisA182126.conjecture2`

Open: stated without proof.

> Let $b = \mathrm{prime}(n+2) - \mathrm{prime}(n)$ and $c = \mathrm{prime}(n+2) - \mathrm{prime}(n+1)$.
> Conjecture: for $n > 61$, $a(n) = b \cdot c$.
> - _Charles R Greathouse IV_, May 11 2012

```lean
theorem conjecture2 (n : ℕ) (hn : 61 < n) :
    let b := prime (n + 2) - prime n
    let c := prime (n + 2) - prime (n + 1)
    a n = b * c
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/182126.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182126.lean#L96).

## `OeisA182126.conjecture3`

Open: stated without proof.

> Are 2, 7, 11, 13, 29 the only primes in this sequence?
> - _Hugo Pfoertner_, Sep 22 2025

```lean
theorem conjecture3 (n : ℕ) (hn : 0 < n) :
    (a n).Prime ↔ a n ∈ ([2, 7, 11, 13, 29] : List ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/182126.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182126.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/182126.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182126.lean)
- [A182126](https://oeis.org/A182126)
