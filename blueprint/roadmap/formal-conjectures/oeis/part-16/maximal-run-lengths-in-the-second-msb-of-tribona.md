---
declaration: theorem
origin: cited
lean: OeisA271591.maximal_run_lengths
statement: formalized
---

# Maximal run lengths in the second MSB of Tribonacci numbers $T(n)$

> The Tribonacci numbers $T_n$ (A000073).
> $T_0=0, T_1=0, T_2=1$, and $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ for $n \ge 3$.
>
> Second most significant bit of the tribonacci number A000073(n).
> This is formalized by extracting the bit at position $\lfloor \log_2 T_n \rfloor - 1$.
>
> *References:*
> - [A271591](https://oeis.org/A271591)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A000073](https://oeis.org/A000073)

*Quoted from [FormalConjectures/OEIS/271591.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/271591.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA271591.maximal_run_lengths`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/271591.wip.lean#L497](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/271591.wip.lean#L497).

> It is conjectured that after the first two 0's, the number of consecutive 0's is only 4 or 5, and the number of consecutive 1's is only 3 or 4 (tested up to $n = 10^4$).
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem maximal_run_lengths : (∀ n L, IsMaximalRun 0 n L → (L = 4 ∨ L = 5)) ∧
    (∀ n L, IsMaximalRun 1 n L → (L = 3 ∨ L = 4))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/271591.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/271591.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/271591.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/271591.lean)
- [A271591](https://oeis.org/A271591)
