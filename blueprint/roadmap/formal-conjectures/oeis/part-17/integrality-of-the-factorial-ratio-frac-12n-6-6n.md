---
declaration: theorem
origin: cited
lean: OeisA368692.a_is_int
statement: formalized
---

# Integrality of the factorial ratio $\frac{(12n+6)! (6n+9)!}{108 (4n+2)! (2n+3)! ((6n+5)!)^2}$

> The factorial ratio
>
> $$a(n) = \frac{(12n + 6)! \cdot (6n + 9)!}{108 \cdot (4n + 2)! \cdot
> (2n + 3)! \cdot ((6n + 5)!)^2}$$
>
> It is conjectured that $a(n)$ are integers.
>
> *References:*
> - [A368692](https://oeis.org/A368692)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/368692.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368692.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA368692.a_is_int`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/368692.wip.lean#L158](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/368692.wip.lean#L158).

> It is conjectured here that $a(n)$ are integers.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_is_int (n : ℕ) : 108 * ((4 * n + 2)! * (2 * n + 3)! * ((6 * n + 5)!) ^ 2) ∣
    (12 * n + 6)! * (6 * n + 9)!
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/368692.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368692.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/368692.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/368692.lean)
- [A368692](https://oeis.org/A368692)
