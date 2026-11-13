---
declaration: theorem
origin: cited
lean: PollocksConjecture.pollock_tetrahedral, PollocksConjecture.pollock_tetrahedral.salzer_levine, PollocksConjecture.pollock_tetrahedral.ncard_exceptions
statement: formalized
---

# Pollock's (tetrahedral numbers) conjecture

> Every positive integer is the sum of at most 5 tetrahedral numbers.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Pollock%27s_conjectures)
> - [A797](https://oeis.org/A797)
> - L. E. Dickson, *History of the Theory of Numbers, Vol. II: Diophantine Analysis*, Dover (2005), pp. 22–23
> - Frederick Pollock, *On the extension of the principle of Fermat's theorem on the polygonal numbers to the higher order of series whose ultimate differences are constant*, Abstracts of the Papers Communicated to the Royal Society of London **5** (1850), 922–924
> - H. E. Salzer and N. Levine, *Table of integers not exceeding 100000 that are not expressible as the sum of four tetrahedral numbers*, Math. Comp. **12** (1958), 141–144
> - [MathWorld: Pollock's Conjecture](https://mathworld.wolfram.com/PollocksConjecture.html)

*Quoted from [FormalConjectures/Wikipedia/PollocksConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PollocksConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 textbook result.

## `PollocksConjecture.pollock_tetrahedral`

Open: stated without proof.

> Pollock's (tetrahedral numbers) conjecture:
> every integer is the sum of at most $5$ tetrahedral numbers.

```lean
theorem pollock_tetrahedral (N : ℕ) :
    ∃ f : Fin 5 → ℕ, N = ∑ i, tetrahedral (f i)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PollocksConjecture.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PollocksConjecture.lean#L59).

## `PollocksConjecture.pollock_tetrahedral.salzer_levine`

Open: stated without proof.

> Salzer–Levine strengthening (as stated on Wikipedia/OEIS):
> there are exactly $241$ integers that are not a sum of $4$ tetrahedral numbers, and the largest is $343867$.

```lean
theorem pollock_tetrahedral.salzer_levine :
    IsGreatest NotSumOfFourTetrahedral 343867
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PollocksConjecture.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PollocksConjecture.lean#L68).

## `PollocksConjecture.pollock_tetrahedral.ncard_exceptions`

Textbook result, stated without proof.

> As stated on Wikipedia/OEIS (A797), the set of exceptions has cardinality $241$.

```lean
theorem pollock_tetrahedral.ncard_exceptions :
    type_of% pollock_tetrahedral.salzer_levine ↔
    NotSumOfFourTetrahedral.ncard = 241
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PollocksConjecture.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PollocksConjecture.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PollocksConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PollocksConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Pollock%27s_conjectures)
