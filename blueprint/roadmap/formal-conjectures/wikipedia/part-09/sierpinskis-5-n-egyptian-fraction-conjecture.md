---
declaration: theorem
origin: cited
lean: SierpinskiEgyptianFractionConjecture.sierpinski_counterexamples_hasDensity_zero, SierpinskiEgyptianFractionConjecture.sierpinski_egyptian_fraction_conjecture
statement: formalized
---

# Sierpiński's $5/n$ Egyptian Fraction Conjecture

> Analogously to the $4/n$ problem (`Erdos242.erdos_242` in `FormalConjectures.ErdosProblems.«242»`),
> Wacław Sierpiński [Si56] conjectured in 1956 that each integer $n \ge 2$ admits positive integers
> $x, y, z \ge 1$ satisfying $5 / n = 1 / x + 1 / y + 1 / z$ (see
> `Erdos242.erdos_242.variants.schinzel_generalization` for Andrzej Schinzel's asymptotic
> generalization to arbitrary numerators). Sieve methods due to William A. Webb [We70] and Robert C.
> Vaughan [Va70] establish sublinear upper bounds on the count of unexpandable denominators $n \le N$,
> implying natural density zero, yet Sierpiński's conjecture for all $n \ge 2$ remains open.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture#Generalizations)
> - [Si56] W. Sierpiński (1956), *Mathesis* **65**, 16–32.
> - [We70] W. A. Webb (1970), *Proc. Amer. Math. Soc.* **25**, 578–584.
> - [Va70] R. C. Vaughan (1970), *Mathematika* **17**, 193–198.

*Quoted from [FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `SierpinskiEgyptianFractionConjecture.sierpinski_counterexamples_hasDensity_zero`

Solved: stated here without proof.

> **Webb–Vaughan Density Bound** [We70, Va70]: Denominators $n$ lacking a three-term unit-fraction
> decomposition of $5 / n$ grow sublinearly up to $N$, hence have natural density $0$.

```lean
theorem sierpinski_counterexamples_hasDensity_zero :
    {n : ℕ | ¬ HasSierpinskiDecomposition n}.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean#L76).

## `SierpinskiEgyptianFractionConjecture.sierpinski_egyptian_fraction_conjecture`

Open: stated without proof.

> **Sierpiński's $5 / n$ Conjecture** [Si56]: Each integer $n \ge 2$ admits positive integers
> $x, y, z \ge 1$ satisfying $5 / n = 1 / x + 1 / y + 1 / z$.

```lean
theorem sierpinski_egyptian_fraction_conjecture {n : ℕ} (hn : 2 ≤ n) :
    HasSierpinskiDecomposition n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/SierpinskiEgyptianFractionConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture#Generalizations)
