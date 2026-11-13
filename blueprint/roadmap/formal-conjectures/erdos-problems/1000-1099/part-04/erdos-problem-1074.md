---
declaration: theorem
origin: cited
lean: Erdos1074.erdos_1074.parts.i, Erdos1074.erdos_1074.parts.ii, Erdos1074.erdos_1074.parts.iii, Erdos1074.erdos_1074.parts.iv, Erdos1074.erdos_1074.variants.EHSNumbers_infinite, Erdos1074.erdos_1074.variants.PillaiPrimes_infinite, Erdos1074.erdos_1074.variants.EHSNumbers_one
statement: formalized
---

# Erdős Problem 1074

> *Reference:* [erdosproblems.com/1074](https://www.erdosproblems.com/1074)

*Quoted from [FormalConjectures/ErdosProblems/1074.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1074](https://www.erdosproblems.com/1074).

The file states 7 research or textbook statements: 5 open and 2 solved. It also has 5 test statements, counted here but not shown.

## `Erdos1074.erdos_1074.parts.i`

Open: stated without proof.

> Let $S$ be the set of all $m\geq 1$ such that there exists a prime $p\not\equiv 1\pmod{m}$ such
> that $m! + 1 \equiv 0\pmod{p}$. Does
>
> $$
>   \lim\frac{|S\cap[1, x]|}{x}
> $$
>
> exist?

```lean
theorem erdos_1074.parts.i : ∃ c, EHSNumbers.HasDensity c
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L60).

## `Erdos1074.erdos_1074.parts.ii`

Open: stated without proof.

> Let $S$ be the set of all $m\geq 1$ such that there exists a prime $p\not\equiv 1\pmod{m}$ such
> that $m! + 1 \equiv 0\pmod{p}$. What is
>
> $$
>   \lim\frac{|S\cap[1, x]|}{x}?
> $$

```lean
theorem erdos_1074.parts.ii : EHSNumbers.HasDensity erdos_1074.parts.ii.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L71).

## `Erdos1074.erdos_1074.parts.iii`

Open: stated without proof.

> Similarly, if $P$ is the set of all primes $p$ such that there exists an $m$ with
> $p\not\equiv 1\pmod{m}$ such that $m! + 1 \equiv 0\pmod{p}$, then does
>
> $$
>   \lim\frac{|P\cap[1, x]|}{\pi(x)}
> $$
>
> exist?

```lean
theorem erdos_1074.parts.iii : ∃ c, PillaiPrimes.HasDensity c {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L81).

## `Erdos1074.erdos_1074.parts.iv`

Open: stated without proof.

> Similarly, if $P$ is the set of all primes $p$ such that there exists an $m$ with
> $p\not\equiv 1\pmod{m}$ such that $m! + 1 \equiv 0\pmod{p}$, then what is
>
> $$
>   \lim\frac{|P\cap[1, x]|}{\pi(x)}?
> $$

```lean
theorem erdos_1074.parts.iv :
    PillaiPrimes.HasDensity erdos_1074.parts.iv.answer {p | p.Prime}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L92).

## `Erdos1074.erdos_1074.variants.EHSNumbers_infinite`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/3dec597bd1a73778760b761712a1fc5fb24bc5d7/FormalConjectures/ErdosProblems/1074.lean#L99](https://github.com/mzhorvath1/formal-conjectures/blob/3dec597bd1a73778760b761712a1fc5fb24bc5d7/FormalConjectures/ErdosProblems/1074.lean#L99).

> Erdős, Hardy, and Subbarao proved that $S$ is infinite.
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem erdos_1074.variants.EHSNumbers_infinite : EHSNumbers.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L111).

## `Erdos1074.erdos_1074.variants.PillaiPrimes_infinite`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos1074_erdos_1074_variants_PillaiPrimes_infinite.lean#L178](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos1074_erdos_1074_variants_PillaiPrimes_infinite.lean#L178).

> Erdős, Hardy, and Subbarao proved that $P$ is infinite.

```lean
theorem erdos_1074.variants.PillaiPrimes_infinite : PillaiPrimes.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L117).

## `Erdos1074.erdos_1074.variants.EHSNumbers_one`

Open: stated without proof.

> Regarding the first question, Hardy and Subbarao computed all EHS numbers up to $2^{10}$, and
> write "...if this trend conditions we expect [the limit] to be around 0.5, if it exists. The
> frequency with which the EHS numbers occur - most often in long sequences of consecutive integers -
> makes us believe that their asymptotic density exists and is unity. Erdős, though initially
> hesitant, later agreed with this view." That is, the conjecture is that $S$ has density $1$.

```lean
theorem erdos_1074.variants.EHSNumbers_one : EHSNumbers.HasDensity 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1074.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1074.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1074.lean)
- [erdosproblems.com/1074](https://www.erdosproblems.com/1074)
