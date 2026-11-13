---
declaration: theorem
origin: cited
lean: Arxiv.«2104.00502».barker_conjecture
statement: formalized
---

# Barker sequences

> A Barker sequence is a finite sequence of $\pm 1$ values whose nontrivial aperiodic
> autocorrelations all have magnitude at most one. The Barker conjecture says that no such sequence
> has length greater than $13$.
>
> *References:*
> * J. Willms, [A note on Barker sequences of even length](https://arxiv.org/abs/2104.00502)
> * [Barker code](https://en.wikipedia.org/wiki/Barker_code)
> * [OEIS A091704](https://oeis.org/A091704)

*Quoted from [FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `Arxiv.«2104.00502».barker_conjecture`

Open: stated without proof.

> Every Barker sequence has length at most $13$.

```lean
theorem barker_conjecture (a : List ℤ) (ha : IsBarkerSequence a) : a.length ≤ 13
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [94 Information and communication, circuits](../../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean)
- [A note on Barker sequences of even length](https://arxiv.org/abs/2104.00502)
