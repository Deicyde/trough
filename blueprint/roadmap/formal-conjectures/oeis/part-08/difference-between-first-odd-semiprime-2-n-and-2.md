---
declaration: theorem
origin: cited
lean: OeisA114137.conjecture1, OeisA114137.conjecture2
statement: formalized
---

# Difference between first odd semiprime $> 2^n$ and $2^n$

> *References:*
> - [A114137](https://oeis.org/A114137)

*Quoted from [FormalConjectures/OEIS/114137.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114137.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements and 1 API statement, counted here but not shown.

## `OeisA114137.conjecture1`

Open: stated without proof.

> In this powers of 2 sequence, does 1 occur infinitely often?

```lean
theorem conjecture1 :
  Set.Infinite {n : ℕ | a n = 1}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114137.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114137.lean#L106).

## `OeisA114137.conjecture2`

Open: stated without proof.

> Does every odd number occur?

```lean
theorem conjecture2 :
  ∀ k : ℕ, Odd k → ∃ n : ℕ, a n = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/114137.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114137.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/114137.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/114137.lean)
- [A114137](https://oeis.org/A114137)
