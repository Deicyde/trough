---
declaration: theorem
origin: cited
lean: Singmaster.singmaster
statement: formalized
---

# Singmaster's conjecture

> Singmaster's conjecture says that for any integer $t>1$, the number of solutions to the equation:
>
> $\binom{n}{k} = t,\quad 1 \le k < n,$
>
> with $\binom{n}{k}$ being the numbers that appear in Pascal's triangle, is bounded by a global
> constant $O(1)$.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Singmaster%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Singmaster.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Singmaster.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Singmaster.singmaster`

Open: stated without proof.

> Singmaster's conjecture: the number of times any number $t > 1$ appears in
> Pascal's triangle is bounded.

```lean
theorem singmaster: ∃ (C : ℕ), ∀ (t : ℕ), t > 1 →
    (Singmaster.solutions t).Finite ∧ (Singmaster.solutions t).ncard ≤ C
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Singmaster.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Singmaster.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Singmaster.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Singmaster.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Singmaster%27s_conjecture)
