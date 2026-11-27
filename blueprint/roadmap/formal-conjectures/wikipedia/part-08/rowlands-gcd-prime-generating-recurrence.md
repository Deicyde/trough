---
declaration: theorem
origin: cited
lean: RowlandSequence.rowland_diff_eq_one_or_prime, RowlandSequence.rowland_generates_all_odd_primes
statement: formalized
---

# Rowland's GCD prime-generating recurrence

> Define $a(1) = 7$ and $a(n) = a(n - 1) + \gcd(n, a(n - 1))$ for $n \ge 2$ (`OEIS A106108`), with
> step increments $d(n) = a(n) - a(n - 1) = \gcd(n, a(n - 1))$ (`OEIS A132199` lists $d(n + 1)$ for
> $n \ge 1$). Eric S. Rowland established in 2008 that every $d(n)$ with $n \ge 2$ equals $1$ or an
> odd prime, and conjectured that every odd prime arises as $d(n)$ for some $n \ge 2$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Formula_for_primes#Rowland%27s_prime-generating_sequence)
> - [OEIS A106108](https://oeis.org/A106108)
> - [OEIS A132199](https://oeis.org/A132199)
> - E. S. Rowland, *A natural prime-generating recurrence*, J. Integer Seq. **11** (2008),
>   Article 08.2.8.

*Quoted from [FormalConjectures/Wikipedia/RowlandSequence.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RowlandSequence.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `RowlandSequence.rowland_diff_eq_one_or_prime`

Solved: stated here without proof.

> Rowland's theorem (2008): for every $n \ge 2$, the step $d(n) = a(n) - a(n - 1)$ equals $1$ or is
> prime.

```lean
theorem rowland_diff_eq_one_or_prime {n : ℕ} (hn : 2 ≤ n) :
    rowlandDiff n = 1 ∨ (rowlandDiff n).Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RowlandSequence.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RowlandSequence.lean#L73).

## `RowlandSequence.rowland_generates_all_odd_primes`

Open: stated without proof.

> Rowland's conjecture (2008): every odd prime $p$ occurs as $d(n) = a(n) - a(n - 1)$ at some index
> $n \ge 2$. The prime $2$ is excluded because $n$ and $a(n - 1)$ always have opposite parity, and
> $n \ge 2$ excludes the artifact `rowlandDiff 1 = 7`.

```lean
theorem rowland_generates_all_odd_primes {p : ℕ} (hp : p.Prime) (hodd : Odd p) :
    ∃ n : ℕ, 2 ≤ n ∧ rowlandDiff n = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RowlandSequence.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RowlandSequence.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RowlandSequence.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RowlandSequence.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Formula_for_primes#Rowland%27s_prime-generating_sequence)
