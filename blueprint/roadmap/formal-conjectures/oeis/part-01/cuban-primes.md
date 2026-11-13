---
declaration: theorem
origin: cited
lean: OeisA2407.conjecture
statement: formalized
---

# Cuban Primes

> OEIS A002407 lists the primes that are differences of two consecutive positive cubes. The
> sequence is conjectured to be infinite.
>
> *References:*
> - [OEIS A002407](https://oeis.org/A002407)

*Quoted from [FormalConjectures/OEIS/2407.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2407.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA2407.conjecture`

Open: stated without proof.

> This sequence is believed to be infinite.

```lean
theorem conjecture : {p : ℕ | A p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/2407.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2407.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2407.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/2407.lean)
- [OEIS A002407](https://oeis.org/A002407)
