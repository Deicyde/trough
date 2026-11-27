---
declaration: theorem
origin: cited
lean: ProthPrime.proth_primality_criterion, ProthPrime.infinitely_many_proth_primes, ProthPrime.infinitely_many_proth_primes_multiplier_three
statement: formalized
---

# Proth primes

> A *Proth number* is an integer $N = k \cdot 2^n + 1$ where $k$ is odd and $1 \le k < 2^n$. A Proth
> number that is prime is called a *Proth prime*. Proth proved in 1878 that a Proth number $N$ is
> prime if and only if $-1$ is an $((N - 1)/2)$-th power modulo $N$. It remains open whether
> infinitely many Proth primes exist, and in particular whether any fixed odd multiplier such as
> $k = 3$ produces infinitely many primes $3 \cdot 2^n + 1$.
>
> *References:*
> - [Wikipedia: Proth prime](https://en.wikipedia.org/wiki/Proth_prime)
> - [Wikipedia: Thabit number](https://en.wikipedia.org/wiki/Thabit_number)
> - [OEIS A080076](https://oeis.org/A080076)
> - [OEIS A002253](https://oeis.org/A002253)
> - [Pr1878] Proth, F. (1878). *Théorèmes sur les nombres premiers*, C. R. Acad. Sci. Paris 87, 926.
> - [CP05] Crandall, R. and Pomerance, C. (2005). *Prime Numbers: A Computational Perspective*, 2nd
>   ed., Springer, New York.

*Quoted from [FormalConjectures/Wikipedia/ProthPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ProthPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 4 test statements and 1 API statement, counted here but not shown.

## `ProthPrime.proth_primality_criterion`

Textbook result, stated without proof.

> **Proth's primality theorem** [Pr1878, CP05]: a Proth number $N = k \cdot 2^n + 1$ ($k$ odd,
> $k < 2^n$) is prime precisely when some residue $a \in \mathbb{Z}/N\mathbb{Z}$ satisfies
> $a^{(N - 1) / 2} = -1$.

```lean
theorem proth_primality_criterion (N : ℕ) (hN : IsProthNumber N) :
    N.Prime ↔ ∃ a : ZMod N, a ^ ((N - 1) / 2) = -1
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ProthPrime.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ProthPrime.lean#L91).

## `ProthPrime.infinitely_many_proth_primes`

Open: stated without proof.

> There are infinitely many Proth primes ([OEIS A080076](https://oeis.org/A080076)).
>
> *Reference:* [Wikipedia: Proth prime](https://en.wikipedia.org/wiki/Proth_prime)

```lean
theorem infinitely_many_proth_primes : {N : ℕ | IsProthPrime N}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ProthPrime.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ProthPrime.lean#L101).

## `ProthPrime.infinitely_many_proth_primes_multiplier_three`

Open: stated without proof.

> There are infinitely many integers $n \ge 2$ such that $3 \cdot 2^n + 1$ is a Proth prime.
>
> Primes of the form $3 \cdot 2^n + 1$ are also called *Thabit primes of the second kind*
> ([Wikipedia: Thabit number](https://en.wikipedia.org/wiki/Thabit_number)). Their exponents are
> listed in [OEIS A002253](https://oeis.org/A002253), which also includes $n = 1$ ($3 \cdot 2^1 + 1 =
> 7$ is prime, whereas $n \ge 2$ ensures $3 < 2^n$).

```lean
theorem infinitely_many_proth_primes_multiplier_three :
    {n : ℕ | 2 ≤ n ∧ (3 * 2 ^ n + 1).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ProthPrime.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ProthPrime.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ProthPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ProthPrime.lean)
- [Wikipedia: Proth prime](https://en.wikipedia.org/wiki/Proth_prime)
