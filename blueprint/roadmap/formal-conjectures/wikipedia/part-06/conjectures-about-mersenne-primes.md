---
declaration: theorem
origin: cited
lean: Mersenne.new_mersenne_conjecture, Mersenne.new_mersenne_conjecture_of_prime, Mersenne.new_mersenne_conjecture.variants.prime, Mersenne.infinitely_many_mersenne_primes, Mersenne.catalans_mersenne_conjecture, Mersenne.squarefree_mersenne_of_prime, Mersenne.sq_dvd_mersenne_iff_isWieferichPrime, Mersenne.rotkiewicz_infinite_non_wieferich_of_squarefree_mersenne
statement: formalized
---

# Conjectures about Mersenne primes

> *References:*
> - [Wikipedia: Mersenne conjectures](https://en.wikipedia.org/wiki/Mersenne_conjectures)
> - [Wikipedia: Catalan's Mersenne conjecture](https://en.wikipedia.org/wiki/Catalan%27s_Mersenne_conjecture)
> - [Wikipedia: List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Prime_numbers)
> - [Wikipedia: Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
> - [MathWorld: Catalan-Mersenne Number](https://mathworld.wolfram.com/Catalan-MersenneNumber.html)
> - A. Rotkiewicz, *Sur les nombres de Mersenne dépourvus de diviseurs carrés et sur les nombres
>   naturels $n$, tels que $n^2 \mid 2^n - 2$*, Mat. Vesnik **2** (17) (1965), 78–80.

*Quoted from [FormalConjectures/Wikipedia/Mersenne.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 5 open, 1 solved and 2 textbook results. It also has 3 test statements, counted here but not shown.

## `Mersenne.new_mersenne_conjecture`

Open: stated without proof.

> For any odd natural number `p` if two of the following conditions hold,
> then all three must hold:
> 1. $2^p-1$ is prime
> 2. $(2^p+1)/3$ is prime
> 3. Exists a number `k` such that $p = 2^k \\pm 1$ or $p = 4^k \\pm 3$

```lean
theorem new_mersenne_conjecture (p : ℕ) (hp : Odd p) :
    NewMersenneConjectureStatement p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L84).

## `Mersenne.new_mersenne_conjecture_of_prime`

Textbook result, proved here.

> It suffices to check this conjecture for odd primes. The statement fails at `p = 2`:
> `mersenne 2 = 3` is prime and `2 = 2 ^ 0 + 1`, but `2` gives no Wagstaff prime.

```lean
theorem new_mersenne_conjecture_of_prime :
    (∀ p, p.Prime → Odd p → NewMersenneConjectureStatement p) →
    ∀ p, Odd p → NewMersenneConjectureStatement p
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L91).

## `Mersenne.new_mersenne_conjecture.variants.prime`

Open: stated without proof.

> The New Mersenne Conjecture statement holds for odd primes.

```lean
theorem new_mersenne_conjecture.variants.prime (p : ℕ) (hp : p.Prime) (h : Odd p) :
    NewMersenneConjectureStatement p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L131).

## `Mersenne.infinitely_many_mersenne_primes`

Open: stated without proof.

> Are there infinitely many Mersenne primes?

```lean
theorem infinitely_many_mersenne_primes :
  Set.Infinite { p : ℕ | (mersenne p).Prime }
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L139).

## `Mersenne.catalans_mersenne_conjecture`

Open: stated without proof.

> The first five Catalan-Mersenne numbers $c_0, \ldots, c_4$ are known to be prime.
> Catalan conjectured that they are prime "up to a certain limit".
> Are all Catalan-Mersenne numbers $c_n$ with $n \geq 5$ prime?

```lean
theorem catalans_mersenne_conjecture :
    ∀ n ≥ 5, Nat.Prime (catalanMersenne n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L149).

## `Mersenne.squarefree_mersenne_of_prime`

Open: stated without proof.

> Is $M_p = 2^p - 1$ squarefree for every prime $p$?

```lean
theorem squarefree_mersenne_of_prime :
    ∀ p : ℕ, p.Prime → Squarefree (mersenne p)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L180).

## `Mersenne.sq_dvd_mersenne_iff_isWieferichPrime`

Textbook result, stated without proof.

> For primes $q$ and $p$ with $p \mid M_q$, the square $p^2$ divides $M_q = 2^q - 1$ precisely when
> `IsWieferichPrime p` holds. The unsolved-problems source states the forward direction from
> $p^2 \mid M_q$ to `IsWieferichPrime p`; the converse under $p \mid M_q$ is added here.

```lean
theorem sq_dvd_mersenne_iff_isWieferichPrime
    {q p : ℕ} (hq : q.Prime) (hp : p.Prime) (hdvd : p ∣ mersenne q) :
    p ^ 2 ∣ mersenne q ↔ IsWieferichPrime p
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L190).

## `Mersenne.rotkiewicz_infinite_non_wieferich_of_squarefree_mersenne`

Solved: stated here without proof.

> Rotkiewicz's theorem (1965): if infinitely many values $M_n = 2^n - 1$ are squarefree, then
> infinitely many primes fail `IsWieferichPrime`. Allowing $n$ to range over all natural numbers
> rather than only primes gives the stronger form of this implication.

```lean
theorem rotkiewicz_infinite_non_wieferich_of_squarefree_mersenne :
    {n : ℕ | Squarefree (mersenne n)}.Infinite →
      {p : ℕ | p.Prime ∧ ¬ IsWieferichPrime p}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 201](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean#L201).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Mersenne.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/Mersenne.lean)
- [Wikipedia: Mersenne conjectures](https://en.wikipedia.org/wiki/Mersenne_conjectures)
