---
declaration: theorem
origin: cited
lean: OeisA113258.conjecture
statement: formalized
---

# Ascending descending base exponent transform of factorials

> *References:*
> - [A113258](https://oeis.org/A113258)

*Quoted from [FormalConjectures/OEIS/113258.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113258.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA113258.conjecture`

Open: stated without proof.

> Is there a nontrivial power after $a(4) = 5^3$?

```lean
theorem conjecture :
  ∃ n > 4, ∃ b > 1, ∃ e > 1, a n = b ^ e
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113258.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113258.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113258.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113258.lean)
- [A113258](https://oeis.org/A113258)
