---
declaration: theorem
origin: cited
lean: Mathoverflow17560.mathoverflow_17560, Mathoverflow17560.mathoverflow_17560.variants.all_nats, Mathoverflow17560.mathoverflow_17560.variants.with_5
statement: formalized
---

# Mathoverflow 17560

> *Reference:* [mathoverflow/17560](https://mathoverflow.net/questions/17560)
> asked by user [Alon-Amit](https://mathoverflow.net/users/25/alon-amit)

*Quoted from [FormalConjectures/Mathoverflow/17560.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/17560.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 textbook results.

## `Mathoverflow17560.mathoverflow_17560`

Open: stated without proof.

> If $2^x$ and $3^x$ are integers, then $x$ must be an integer.

```lean
theorem mathoverflow_17560 {x : ℝ} (hx : ∃ m : ℕ, (2 : ℝ) ^ x = m) (hx' : ∃ m : ℕ, (3 : ℝ) ^ x = m) :
    ∃ m : ℕ, x = m
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [13 Commutative algebra](../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Mathoverflow/17560.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/17560.lean#L35).

## `Mathoverflow17560.mathoverflow_17560.variants.all_nats`

Textbook result, stated without proof.

> If for each natural number $n$ the number $n^x$ is an integer then $x$ must also be an integer.

```lean
theorem mathoverflow_17560.variants.all_nats {x : ℝ} (hx : ∀ n : ℕ, ∃ m : ℕ, (n : ℝ) ^ x = m) :
    ∃ m : ℕ, x = m
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [13 Commutative algebra](../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Mathoverflow/17560.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/17560.lean#L43).

## `Mathoverflow17560.mathoverflow_17560.variants.with_5`

Textbook result, stated without proof.

> If $2^x$, $3^x$ and $5^x$ are integers, then $x$ must be an integer.

```lean
theorem mathoverflow_17560.variants.with_5 {x : ℝ} (hx : ∃ m : ℕ, (2 : ℝ) ^ x = m)
    (hx' : ∃ m : ℕ, (3 : ℝ) ^ x = m) (hx'' : ∃ m : ℕ, (5 : ℝ) ^ x = m) : ∃ m : ℕ, x = m
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [13 Commutative algebra](../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Mathoverflow/17560.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/17560.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/17560.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/17560.lean)
- [mathoverflow/17560](https://mathoverflow.net/questions/17560)
