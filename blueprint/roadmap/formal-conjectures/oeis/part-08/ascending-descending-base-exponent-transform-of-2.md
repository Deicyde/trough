---
declaration: theorem
origin: cited
lean: OeisA113258.conjecture
statement: formalized
---

# Ascending descending base exponent transform of factorials

> *References:*
> - [A113258](https://oeis.org/A113258)

*Quoted from [FormalConjectures/OEIS/113258.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/113258.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA113258.conjecture`

Open: stated without proof.

> Is there a nontrivial power after $a(4) = 5^3$?

```lean
theorem conjecture :
  ∃ n > 4, ∃ b > 1, ∃ e > 1, a n = b ^ e
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113258.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/113258.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113258.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/113258.lean)
- [A113258](https://oeis.org/A113258)
