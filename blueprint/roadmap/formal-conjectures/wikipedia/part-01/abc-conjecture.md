---
declaration: theorem
origin: cited
lean: ABC.abc, ABC.abc.variants.lt_constant_mul, ABC.abc.variants.quality
statement: formalized
---

# \*abc\* conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Abc_conjecture)

*Quoted from [FormalConjectures/Wikipedia/ABC.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ABC.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 3 test statements, counted here but not shown.

## `ABC.abc`

Open: stated without proof.

> For every positive real number `ε`, there exist only finitely many triples `(a, b, c)` of coprime positive integers, with `a + b = c`, such that `c > rad(abc)^(1+ε)`

```lean
theorem abc (ε : ℝ) (hε : 0 < ε) :
    {(a, b, c) : ℕ × ℕ × ℕ | 0 < a ∧ 0 < b ∧ 0 < c ∧ ({a, b, c} : Set ℕ).Pairwise Nat.Coprime ∧
    a + b = c ∧ (radical <| a * b * c : ℝ)^(1 + ε) < c}.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ABC.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ABC.lean#L63).

## `ABC.abc.variants.lt_constant_mul`

Open: stated without proof.

> For every positive real number ε, there exists a constant `K_ε` such that for all triples (a, b, c) of coprime positive integers, with a + b = c we have `c < K_ε rad(abc)^(1+ε)`.

```lean
theorem abc.variants.lt_constant_mul (ε : ℝ) (hε : 0 < ε) : ∃ K,
    ∀ (a b c : ℕ), 0 < a → 0 < b → 0 < c → ({a, b, c} : Set ℕ).Pairwise Nat.Coprime → a + b = c →
    c < K * (radical <| a * b * c : ℝ)^(1 + ε)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ABC.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ABC.lean#L72).

## `ABC.abc.variants.quality`

Open: stated without proof.

> For every positive real number ε, there exist only finitely many triples `(a, b, c)` of coprime positive integers with `a + b = c` such that `q(a, b, c) > 1 + ε`.

```lean
theorem abc.variants.quality (ε : ℝ) (hε : 0 < ε) :
    {(a, b, c) : ℕ × ℕ × ℕ | 0 < a ∧ 0 < b ∧ 0 < c ∧ ({a, b, c} : Set ℕ).Pairwise Nat.Coprime ∧
    a + b = c ∧ quality a b c > (1 + ε)}.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ABC.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ABC.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ABC.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ABC.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Abc_conjecture)
