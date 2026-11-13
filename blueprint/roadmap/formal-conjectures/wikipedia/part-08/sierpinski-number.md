---
declaration: theorem
origin: cited
lean: SierpinskiNumber.selfridge_78557, SierpinskiNumber.selfridge_conjecture, SierpinskiNumber.prime_sierpinski_problem, SierpinskiNumber.extended_sierpinski_problem
statement: formalized
---

# Sierpiński number

> *References:*
> - [Wikipedia, Sierpiński number](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_number)
> - [Si60] Sierpiński, W., Elementary Theory of Numbers. Państwowe Wydawnictwo Naukowe,
>   Warsaw (1960).
>
> A positive odd integer $k$ is a *Sierpiński number* if $k \cdot 2^n + 1$ is composite for all
> natural numbers $n$. In 1960, Sierpiński proved that there are infinitely many such numbers.
> John Selfridge proved in 1962 that 78557 is a Sierpiński number. It is conjectured to be the
> smallest.
>
> ## Sierpiński problem
>
> The *Sierpiński problem* asks: is 78557 the smallest Sierpiński number?
>
> ## Prime Sierpiński problem
>
> The *prime Sierpiński problem* asks: is 271129 the smallest *prime* Sierpiński number?
>
> ## Extended Sierpiński problem
>
> The *extended Sierpiński problem* asks: is 271129 the second-smallest Sierpiński number?

*Quoted from [FormalConjectures/Wikipedia/SierpinskiNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved.

## `SierpinskiNumber.selfridge_78557`

Proved here.

> Selfridge proved in 1962 that 78557 is a Sierpiński number by showing that all numbers of the
> form $78557 \cdot 2^n + 1$ have a factor in the covering set $\{3, 5, 7, 13, 19, 37, 73\}$.

```lean
theorem selfridge_78557 : Nat.IsSierpinskiNumber 78557
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiNumber.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean#L56).

## `SierpinskiNumber.selfridge_conjecture`

Open: stated without proof.

> **The Sierpiński problem (Selfridge's conjecture).** Is 78557 the smallest Sierpiński number?
>
> Selfridge conjectured that 78557 is the smallest Sierpiński number. He proved in 1962 that
> 78557 is indeed a Sierpiński number by showing that all numbers of the form $78557 \cdot 2^n + 1$
> have a factor in the covering set $\{3, 5, 7, 13, 19, 37, 73\}$.

```lean
theorem selfridge_conjecture :
    IsLeast {k | k.IsSierpinskiNumber} 78557
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiNumber.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean#L87).

## `SierpinskiNumber.prime_sierpinski_problem`

Open: stated without proof.

> **The prime Sierpiński problem.** Is 271129 the smallest prime Sierpiński number?
>
> In 1976, Nathan Mendelsohn determined that the second provable Sierpiński number is the prime
> $k = 271129$.

```lean
theorem prime_sierpinski_problem :
    IsLeast {k | k.IsSierpinskiNumber ∧ k.Prime} 271129
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiNumber.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean#L98).

## `SierpinskiNumber.extended_sierpinski_problem`

Open: stated without proof.

> **The extended Sierpiński problem.** Is 271129 the second-smallest Sierpiński number?
>
> Even if 78557 is confirmed as the smallest Sierpiński number, there could exist a composite
> Sierpiński number $k$ with $78557 < k < 271129$. We formalize "second-smallest" as: the
> least Sierpiński number $k$ such that there exists exactly one Sierpiński number below it.

```lean
theorem extended_sierpinski_problem :
    IsLeast {k | k.IsSierpinskiNumber ∧
      ∃ k', k'.IsSierpinskiNumber ∧ k' < k} 271129
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiNumber.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SierpinskiNumber.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SierpinskiNumber.lean)
- [Wikipedia, Sierpiński number](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_number)
