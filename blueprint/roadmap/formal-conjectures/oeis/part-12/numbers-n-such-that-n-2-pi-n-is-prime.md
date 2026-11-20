---
declaration: theorem
origin: cited
lean: OeisA228828.conjecture
statement: formalized
---

# Numbers $n$ such that $n^2 + \pi(n)$ is prime

> *References:*
> - [A228828](https://oeis.org/A228828)

*Quoted from [FormalConjectures/OEIS/228828.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/228828.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `OeisA228828.conjecture`

Open: stated without proof.

> Conjecture: the sequence A228828 is infinite.

```lean
theorem conjecture : {a n | n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228828.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/228828.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228828.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/228828.lean)
- [A228828](https://oeis.org/A228828)
