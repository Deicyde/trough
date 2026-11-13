---
declaration: theorem
origin: cited
lean: EulerBrick.perfect_euler_brick_existence, EulerBrick.four_dim_euler_brick_existence, EulerBrick.n_dim_euler_brick_existence, EulerBrick.cuboidOne, EulerBrick.cuboidTwo, EulerBrick.cuboidThree, EulerBrick.cuboid_perfect_euler_brick
statement: formalized
---

# Open questions regarding the existence of Euler bricks

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Euler_brick)
> - [stackexchange](https://math.stackexchange.com/questions/2264401/euler-bricks-and-the-4th-dimension)
> - [Sh12] Sharipov, Ruslan. Perfect cuboids and irreducible polynomials. https://arxiv.org/abs/1108.5348

*Quoted from [FormalConjectures/Wikipedia/EulerBrick.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 5 open and 2 solved.

## `EulerBrick.perfect_euler_brick_existence`

Open: stated without proof.

> Is there a perfect Euler brick?

```lean
theorem perfect_euler_brick_existence :
    ∃ a b c : ℕ+, IsPerfectCuboid a b c
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L55).

## `EulerBrick.four_dim_euler_brick_existence`

Open: stated without proof.

> Is there an Euler brick in $4$-dimensional space?

```lean
theorem four_dim_euler_brick_existence :
    ∃ sides : Fin 4 → ℕ+, IsEulerHyperBrick 4 sides
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L63).

## `EulerBrick.n_dim_euler_brick_existence`

Open: stated without proof.

> Is there an Euler brick in $n$-dimensional space for any $n > 3$?

```lean
theorem n_dim_euler_brick_existence :
∀ n > 3, ∃ sides : Fin n → ℕ+, IsEulerHyperBrick n sides
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L71).

## `EulerBrick.cuboidOne`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/34c93bbad127a9a5354b9d53478d338eb65edb88/FormalConjectures/Wikipedia/EulerBrick.lean#L1804](https://github.com/google-deepmind/formal-conjectures/blob/34c93bbad127a9a5354b9d53478d338eb65edb88/FormalConjectures/Wikipedia/EulerBrick.lean#L1804).

> The first Cuboid conjecture
>
> The DeepMind prover agent has found a formal proof of this statement.
>
> An (independent) informal solution can be found here:
> *Reference:* [arxiv/2510.11768](https://arxiv.org/abs/2510.11768) **Irreducibility of the Cuboid Polynomial P_{a,u}(t) via a Rank-Zero Elliptic Curve** by *Valery Asiryan*

```lean
theorem cuboidOne : CuboidOne
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L106).

## `EulerBrick.cuboidTwo`

Open: stated without proof.

> The second Cuboid conjecture

```lean
theorem cuboidTwo : CuboidTwo
```

Category `research open`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L124).

## `EulerBrick.cuboidThree`

Open: stated without proof.

> The third Cuboid conjecture

```lean
theorem cuboidThree : CuboidThree
```

Category `research open`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L146).

## `EulerBrick.cuboid_perfect_euler_brick`

Solved: stated here without proof.

> In [Sh12], Ruslan notes that a perfect Euler brick does not exist
> if all three Cuboid conjectures hold.

```lean
theorem cuboid_perfect_euler_brick (h₁ : CuboidOne) (h₂ : CuboidTwo) (h₃ : CuboidThree) :
    ¬ ∃ a b c : ℕ+, IsPerfectCuboid a b c
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/EulerBrick.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean#L152).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/EulerBrick.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/EulerBrick.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Euler_brick)
