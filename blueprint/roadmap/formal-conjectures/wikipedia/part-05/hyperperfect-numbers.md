---
declaration: theorem
origin: cited
lean: HyperperfectNumber.mccranie_odd_hyperperfect_conjecture, HyperperfectNumber.two_hyperperfect_characterization, HyperperfectNumber.minoli_bear_hyperperfect_conjecture, HyperperfectNumber.infinitely_many_hyperperfect_numbers
statement: formalized
---

# Hyperperfect numbers

> An integer $n > 1$ is called $k$-hyperperfect ($k \ge 1$, Minoli and Bear 1975) when
> $n = 1 + k \cdot (\sigma_1(n) - n - 1)$, or equivalently $n + k(n + 1) = 1 + k \sigma_1(n)$;
> setting $k = 1$ recovers `Nat.Perfect` (cf. `PerfectNumbers.infinitely_many_perfect`). Judson S.
> McCranie (2000) conjectured that every $k$-hyperperfect integer with odd $k > 1$ has the form
> $p^2 q$ for primes $p = (3k + 1) / 2$ and $q = 3k + 4$. At $k = 2$ (`OEIS A007593`), Alexander
> Violette (June 2026) found a four-prime-factor $2$-hyperperfect counterexample outside the family
> $n = 3^m(3^{m+1} - 2)$. Guy (2004, §B2, pp. 74–75) also cites Minoli and Bear's (1975)
> conjecture that every $k \ge 1$ admits at least one $k$-hyperperfect integer; because
> $n - 1 = k(\sigma_1(n) - n - 1)$ fixes $k$ uniquely for $n > 1$, this conjecture entails infinitely
> many non-perfect hyperperfect integers ($k \ge 2$, `OEIS A007592`).
>
> *References:*
> - [Wikipedia: Hyperperfect number](https://en.wikipedia.org/wiki/Hyperperfect_number)
> - [OEIS A007592](https://oeis.org/A007592) (non-perfect hyperperfect integers, $k \ge 2$)
> - [OEIS A007593](https://oeis.org/A007593) ($2$-hyperperfect integers, including A. Violette's June
>   2026 counterexample)
> - D. Minoli and R. Bear (1975), *Hyperperfect numbers*, Pi Mu Epsilon J. **6**, no. 3, 153–157.
> - [J. S. McCranie (2000)](https://cs.uwaterloo.ca/journals/JIS/VOL3/mccranie.html), J. Integer Seq.
>   **3**, Article 00.1.3.
> - R. K. Guy (2004), *Unsolved Problems in Number Theory*, 3rd ed., Springer, §B2, pp. 74–75
>   (ISBN `978-0-387-20860-2`).

*Quoted from [FormalConjectures/Wikipedia/HyperperfectNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `HyperperfectNumber.mccranie_odd_hyperperfect_conjecture`

Open: stated without proof.

> McCranie's odd-$k$ conjecture (2000): for odd $k > 1$, every $k$-hyperperfect integer $n$ satisfies
> $n = p^2 q$ with primes $p = (3k + 1)/2$ and $q = 3k + 4$.

```lean
theorem mccranie_odd_hyperperfect_conjecture {k n : ℕ} (hk_odd : Odd k) (hk : 1 < k)
    (hn : IsHyperperfect k n) :
    ((3 * k + 1) / 2).Prime ∧ (3 * k + 4).Prime ∧ n = ((3 * k + 1) / 2) ^ 2 * (3 * k + 4)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HyperperfectNumber.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean#L92).

## `HyperperfectNumber.two_hyperperfect_characterization`

Solved: stated here without proof.

> Not every $2$-hyperperfect integer has the form $3^m(3^{m+1} - 2)$ with $m \ge 1$ and $3^{m+1} - 2$
> prime: Alexander Violette (June 2026, [OEIS A007593](https://oeis.org/A007593)) found the
> four-prime-factor $2$-hyperperfect counterexample
> $n = 3^{16} \cdot 129140227 \cdot 256572153302107 \cdot 225205396855537107298933866373$.

```lean
theorem two_hyperperfect_characterization :
    ¬ ∀ n : ℕ, IsHyperperfect 2 n →
      ∃ m ≥ 1, (3 ^ (m + 1) - 2).Prime ∧ n = 3 ^ m * (3 ^ (m + 1) - 2)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HyperperfectNumber.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean#L104).

## `HyperperfectNumber.minoli_bear_hyperperfect_conjecture`

Open: stated without proof.

> Minoli and Bear's conjecture (1975; Guy 2004, §B2, pp. 74–75): for every integer $k \ge 1$, at
> least one $k$-hyperperfect integer exists.

```lean
theorem minoli_bear_hyperperfect_conjecture :
    ∀ k ≥ 1, ∃ n, IsHyperperfect k n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HyperperfectNumber.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean#L114).

## `HyperperfectNumber.infinitely_many_hyperperfect_numbers`

Open: stated without proof.

> Infinitely many non-perfect hyperperfect integers ($k \ge 2$, listed in
> [OEIS A007592](https://oeis.org/A007592)) exist. This follows from
> `minoli_bear_hyperperfect_conjecture` (Guy 2004, §B2, pp. 74–75), because
> $n - 1 = k(\sigma_1(n) - n - 1)$ uniquely fixes $k$ for any $n > 1$ (for $k = 1$, cf.
> `PerfectNumbers.infinitely_many_perfect`).

```lean
theorem infinitely_many_hyperperfect_numbers :
    {n : ℕ | ∃ k ≥ 2, IsHyperperfect k n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HyperperfectNumber.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean#L126).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/HyperperfectNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/HyperperfectNumber.lean)
- [Wikipedia: Hyperperfect number](https://en.wikipedia.org/wiki/Hyperperfect_number)
