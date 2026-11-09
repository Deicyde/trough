---
declaration: theorem
origin: cited
lean: OeisA191004.conjecture_1, OeisA191004.conjecture_2, OeisA191004.conjecture_3
statement: formalized
---

# Representations of $n = p + q + (n \bmod 2)q$ with Jacobi symbol constraints

> The sequence $a(n)$ counts the number of ways to write $n = p + q + (n \bmod 2)q$, where $p$ is an
> odd prime and $q \le n/2$ is a prime such that $\left(\frac{q}{n}\right) = 1$ if $n$ is odd, and
> $\left(\frac{(q+1)/2}{n+1}\right) = 1$ if $n$ is even.
>
> *References:*
> - [A191004](https://oeis.org/A191004)
> - [Conjectures involving primes and quadratic forms](https://arxiv.org/abs/1211.1588)
>   by *Zhi-Wei Sun*, arXiv:1211.1588 (2012)

*Quoted from [FormalConjectures/OEIS/191004.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/191004.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 7 test statements, counted here but not shown.

## `OeisA191004.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 5$.
> - _Zhi-Wei Sun_, Dec 30 2012

```lean
theorem conjecture_1 (n : ℕ) (hn : 5 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/191004.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/191004.lean#L80).

## `OeisA191004.conjecture_2`

Open: stated without proof.

> Refinement conjecture (odd case): Any odd number $2n+1 > 64$ not among $105, 247, 255, 1105$ can be
> written as $p + 2q$, where $p$ and $q$ are primes, and $\left(\frac{q}{p'}\right) = 1$ for any prime
> divisor $p'$ of $2n+1$.
> - _Zhi-Wei Sun_, Dec 30 2012

```lean
theorem conjecture_2 (m : ℕ) (hm : 64 < m) (hodd : Odd m)
    (hnot : m ∉ ({105, 247, 255, 1105} : Finset ℕ)) :
    ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ m = p + 2 * q ∧
      ∀ p' ∈ m.primeFactors, jacobiSym (q : ℤ) p' = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/191004.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/191004.lean#L90).

## `OeisA191004.conjecture_3`

Open: stated without proof.

> Refinement conjecture (even case): Any even number $m = 2n > 8$ not among $32$ and $152$ can be
> written as $p + q$, where $p$ and $q \le m/2$ are primes, and
> $\left(\frac{(q+1)/2}{p'}\right) = 1$ for any prime divisor $p'$ of $m+1$.
> (The OEIS comment writes $q \le n/2$ after renaming the argument of $a(\cdot)$ to $2n$, which is a
> slip for $q \le (2n)/2 = n = m/2$, matching the bound in the definition of $a(2n)$ and yielding the
> stated exceptional set $\{32, 152\}$.)
> - _Zhi-Wei Sun_, Dec 30 2012

```lean
theorem conjecture_3 (m : ℕ) (hm : 8 < m) (heven : Even m)
    (hnot : m ∉ ({32, 152} : Finset ℕ)) :
    ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ m = p + q ∧ q ≤ m / 2 ∧
      ∀ p' ∈ (m + 1).primeFactors, jacobiSym (((q + 1) / 2) : ℤ) p' = 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/191004.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/191004.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/191004.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/191004.lean)
- [A191004](https://oeis.org/A191004)
