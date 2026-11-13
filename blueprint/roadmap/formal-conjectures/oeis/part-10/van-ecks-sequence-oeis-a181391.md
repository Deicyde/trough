---
declaration: theorem
origin: cited
lean: OeisA181391.conjecture
statement: formalized
---

# Van Eck's sequence (OEIS A181391)

> Van Eck's sequence starts with zero. If the current value has occurred before, the next value is
> the distance to its most recent earlier occurrence; otherwise the next value is zero.
>
> *References:*
> - [OEIS A181391](https://oeis.org/A181391)
> - N. J. A. Sloane, [Some Open Problems](https://neilsloane.com/doc/EMMay2016.pdf#page=14)

*Quoted from [FormalConjectures/OEIS/181391.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/181391.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements and 1 API statement, counted here but not shown.

## `OeisA181391.conjecture`

Open: stated without proof.

> [OEIS A181391](https://oeis.org/A181391) conjectures: "every number eventually appears."

```lean
theorem conjecture : Function.Surjective a
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/181391.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/181391.lean#L109).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/181391.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/181391.lean)
- [OEIS A181391](https://oeis.org/A181391)
