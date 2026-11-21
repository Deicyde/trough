---
declaration: theorem
origin: cited
lean: OeisA145355.conjecture
statement: formalized
---

# Factorial distance to nearest square

> The sequence is defined as
>
> $$a(n) =
> \mathrm{round}\left(\frac{\mathrm{round}(\sqrt{n!})}{\left|(\mathrm{round}(\sqrt{n!}))^2 -
> n!\right|}\right)$$
>
> for $n \ge 2$.
>
> *References:*
> - [A145355](https://oeis.org/A145355)

*Quoted from [FormalConjectures/OEIS/145355.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/145355.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA145355.conjecture`

Open: stated without proof.

> This sequence suggests that the distance between a factorial and the closest power is
> tightly bounded.

```lean
theorem conjecture : ∃ C : ℕ, ∀ n : ℕ, 2 ≤ n → a n ≤ C
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/145355.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/145355.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/145355.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/145355.lean)
- [A145355](https://oeis.org/A145355)
