---
declaration: theorem
origin: cited
lean: Dickson.dickson_conjecture, Dickson.generalized_twin_primes, Dickson.infinite_safe_primes, Dickson.infinite_cousin_primes, Dickson.infinite_sexy_primes
statement: formalized
---

# Dickson's conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Dickson%27s_conjecture)
> - [PrimePages glossary](https://t5k.org/glossary/xpage/DicksonsConjecture.html)
> - [OEIS Wiki](https://oeis.org/wiki/Dickson%27s_conjecture)
> - [MathWorld](https://mathworld.wolfram.com/DicksonsConjecture.html)
> - [Leonard Eugene Dickson, *History of the Theory of Numbers, Vol. I: Divisibility and Primality*](https://archive.org/details/historyoftheoryo01dickuoft)
> - [Arxiv](https://arxiv.org/pdf/0906.3850)

*Quoted from [FormalConjectures/Wikipedia/Dickson.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open.

## `Dickson.dickson_conjecture`

Open: stated without proof.

> **Dickson's conjecture**
> If a finite set of linear integer forms $f_i(n) = a_i n+b_i$ satisfies Schinzel condition,
> there exist infinitely many natural numbers $m$ such that $f_i(m)$ are primes for all $i$.

```lean
theorem dickson_conjecture (fs : Finset ℤ[X]) (hfs : ∀ f ∈ fs, f.degree = 1 ∧ BunyakovskyCondition f)
    (hfs' : SchinzelCondition fs) : Infinite {n : ℕ | ∀ f ∈ fs, (f.eval (n : ℤ)).natAbs.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Dickson.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean#L43).

## `Dickson.generalized_twin_primes`

Open: stated without proof.

> **The generalized twin-prime conjecture**
> For any positive integer $k$ there are infinitely many primes $p$ such that $p + 2k$ is prime.

```lean
theorem generalized_twin_primes (k : ℕ) (hk : 0 < k) :
    Infinite {p : ℕ | p.Prime ∧ (p + 2 * k).Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Dickson.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean#L54).

## `Dickson.infinite_safe_primes`

Open: stated without proof.

> **The infinitude of Sophie Germain primes**
> There are infinitely many primes $p$ such that $2p + 1$ is prime.

```lean
theorem infinite_safe_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (2 * p + 1)}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Dickson.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean#L63).

## `Dickson.infinite_cousin_primes`

Open: stated without proof.

> **The infinitude of cousin primes**
> There are infinitely many primes $p$ such that $p + 4$ is prime.

```lean
theorem infinite_cousin_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (p + 4)}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Dickson.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean#L72).

## `Dickson.infinite_sexy_primes`

Open: stated without proof.

> **The infinitude of sexy primes**
> There are infinitely many primes $p$ such that $p + 6$ is prime.

```lean
theorem infinite_sexy_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (p + 6)}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Dickson.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Dickson.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Dickson.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Dickson%27s_conjecture)
