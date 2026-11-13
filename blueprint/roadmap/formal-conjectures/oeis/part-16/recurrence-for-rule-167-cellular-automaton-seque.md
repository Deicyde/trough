---
declaration: theorem
origin: cited
lean: OeisA267581.a_recurrence
statement: formalized
---

# Recurrence for Rule 167 cellular automaton sequence

> Decimal representation of the middle column of the "Rule 167" elementary cellular automaton
> starting with a single ON (black) cell.
>
> *References:*
> - [A267581](https://oeis.org/A267581)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/267581.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/267581.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA267581.a_recurrence`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/267581.wip.lean#L190](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/267581.wip.lean#L190).

> Conjecture: $a(n) = 2 a(n-1) + 1 - \lfloor (1/2)^{2^{n+1} \bmod n} \rfloor$ for $n \ge 2$. - _Andres Cicuttin_, Mar 29 2016
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_recurrence (n : ℕ) (hn : 2 ≤ n) : a n = 2 * a (n - 1) + 1 - oeisFloorTerm n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/267581.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/267581.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/267581.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/267581.lean)
- [A267581](https://oeis.org/A267581)
