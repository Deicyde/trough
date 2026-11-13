---
declaration: theorem
origin: cited
lean: WieferichPrime.infinite_isWieferichPrime, WieferichPrime.isWieferichPrime_iff, WieferichPrime.infinite_isWieferichPrimeBase, WieferichPrime.exists_isWieferichPrimeBase_47
statement: formalized
---

# Wieferich primes

> A Wieferich prime is a prime $p$ with $2^{p-1} \equiv 1 \pmod{p^2}$. The only known examples are
> $1093$ and $3511$. It is conjectured that there are infinitely many Wieferich primes; a heuristic
> argument suggests that the number of Wieferich primes up to $x$ grows like $\log \log x$.
>
> More generally, a prime $p$ is a Wieferich prime to base $a$ if $a^{p-1} \equiv 1 \pmod{p^2}$.
> Wikipedia's list of unsolved problems also asks whether there are infinitely many Wieferich primes
> to every base $a > 0$, and whether there is any Wieferich prime to base $47$. It is also not known
> whether there is any Wieferich prime besides $1093$ and $3511$.
>
> *References:*
> * [Wikipedia, List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)
> * [Wikipedia, Wieferich prime](https://en.wikipedia.org/wiki/Wieferich_prime)
> * [OEIS A001220](https://oeis.org/A001220)
> * P. Ribenboim, *Die Welt der Primzahlen*, 2nd ed., Springer (2006), pp. 242–243.
> * [PrimeGrid, Wieferich and Wall–Sun–Sun Prime Search](https://www.primegrid.com/stats_ww.php)

*Quoted from [FormalConjectures/Wikipedia/WieferichPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 3 test statements, counted here but not shown.

## `WieferichPrime.infinite_isWieferichPrime`

Open: stated without proof.

> There are infinitely many Wieferich primes.

```lean
theorem infinite_isWieferichPrime : {p : ℕ | IsWieferichPrime p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichPrime.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean#L46).

## `WieferichPrime.isWieferichPrime_iff`

Open: stated without proof.

> Are $1093$ and $3511$ the only Wieferich primes? They are the only known ones: PrimeGrid's search,
> completed in 2022, shows that any other Wieferich prime exceeds $2^{64}$. On the other hand, the
> heuristic count of $\log \log x$ Wieferich primes up to $x$ predicts that there are infinitely
> many, see `infinite_isWieferichPrime`.

```lean
theorem isWieferichPrime_iff :
    ∀ p, IsWieferichPrime p ↔ p = 1093 ∨ p = 3511
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichPrime.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean#L56).

## `WieferichPrime.infinite_isWieferichPrimeBase`

Open: stated without proof.

> For any given integer $a > 0$, are there infinitely many primes $p$ such that
> $a^{p-1} \equiv 1 \pmod{p^2}$? The case $a = 1$ is trivial, since every prime qualifies
> (`isWieferichPrimeBase_one_iff`). So is the case $a = 0$ under our definition
> (`isWieferichPrimeBase_zero_iff`), which is why the source's restriction to $a > 0$ is dropped.

```lean
theorem infinite_isWieferichPrimeBase :
    ∀ a : ℕ, {p : ℕ | IsWieferichPrimeBase a p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichPrime.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean#L67).

## `WieferichPrime.exists_isWieferichPrimeBase_47`

Open: stated without proof.

> Are there any Wieferich primes to base $47$? None is currently known.

```lean
theorem exists_isWieferichPrimeBase_47 : ∃ p, IsWieferichPrimeBase 47 p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WieferichPrime.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WieferichPrime.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WieferichPrime.lean)
- [Wikipedia, List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)
