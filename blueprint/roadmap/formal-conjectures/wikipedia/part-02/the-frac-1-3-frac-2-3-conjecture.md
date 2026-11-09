---
declaration: theorem
origin: cited
lean: Conjecture_1_3_to_2_3.conjecture_1_3_to_2_3
statement: formalized
---

# The $\frac 1 3$–$\frac 2 3$ conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture)

*Quoted from [FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Conjecture_1_3_to_2_3.conjecture_1_3_to_2_3`

Open: stated without proof.

> Does every finite partially ordered set that is not totally ordered
> contain two elements $x$ and $y$ such that the probability that
> $x$ appears before $y$ in a random linear extension is between $\frac 1 3$ and $\frac 2 3$?
>
> The set of all total order extensions is represented as order preserving
> bijections $P$ of $1, ..., n$.

```lean
theorem conjecture_1_3_to_2_3 : ∀ (P : Type) [Finite P] [PartialOrder P]
    (not_total : ¬ Std.Total (α := P) (· ≤ ·)) (total_ext : Set <| OrderHom P ℕ)
    (total_ext_def : ∀ σ, σ ∈ total_ext ↔ Set.range σ = Set.Icc 1 (Nat.card P)),
    ∃ x y : P, ({σ ∈ total_ext | σ x < σ y}.ncard / total_ext.ncard : ℚ)
      ∈ Set.Icc (1/3) (2/3)
```

Category `research open`; AMS [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/conjecture_1_3_to_2_3.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/1/3%E2%80%932/3_conjecture)
