---
declaration: theorem
origin: cited
lean: OeisA105210.conjecture_disjoint_starting_values, OeisA105210.conjecture
statement: formalized
---

# Conjectures associated with A105210

> $a(1) = 393$; for $n > 1$, $a(n) = a(n-1)$ + 1 + sum of distinct prime factors of $a(n-1)$
> that are $< a(n-1)$.
>
> *References:*
> - [A105210](https://oeis.org/A105210)

*Quoted from [FormalConjectures/OEIS/105210.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105210.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA105210.conjecture_disjoint_starting_values`

Open: stated without proof.

> Cormier and Selfridge found 5 starting values for which the sequences appear to not merge.
> The sequences were checked up to 10^8.

```lean
theorem conjecture_disjoint_starting_values :
    ∀ j k : ℕ,
      j ∈ ({1, 393, 412, 668, 932} : Set ℕ) →
      k ∈ ({1, 393, 412, 668, 932} : Set ℕ) →
      j ≠ k →
      sequenceSet j ∩ sequenceSet k = ∅
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105210.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105210.lean#L88).

## `OeisA105210.conjecture`

Open: stated without proof.

> This suggests that there may be infinitely many different (non-merging) sequences obtained
> by choosing different starting values.

```lean
theorem conjecture :
  ∃ K : Set ℕ,
    Set.Infinite K ∧
    (∀ k ∈ K, 1 ≤ k) ∧
    (∀ j k : ℕ,
      j ∈ K → k ∈ K → j ≠ k →
      sequenceSet j ∩ sequenceSet k = ∅)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105210.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105210.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105210.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105210.lean)
- [A105210](https://oeis.org/A105210)
