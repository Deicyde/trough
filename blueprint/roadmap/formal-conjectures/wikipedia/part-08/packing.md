---
declaration: theorem
origin: cited
lean: SquarePacking.eleven_square_packing_in_square_bound, SquarePacking.least_eleven_square_packing_in_square, SquarePacking.seventeen_square_packing_in_square_bound, SquarePacking.least_seventeen_square_packing_in_square, SquarePacking.three_square_packing_in_circle_bound, SquarePacking.least_three_square_packing_in_circle, SquarePacking.twenty_one_circle_packing_in_square_bound, SquarePacking.least_twenty_one_circle_packing_in_square, SquarePacking.fifteen_circle_packing_in_circle_bound, SquarePacking.least_fifteen_circle_packing_in_circle
statement: formalized
---

# Packing

> This file contains a number of open problems related to the minimal size of a square (or circle)
> that can contain a given number of unit squares (or circles).
> In each case, we provide a known upper bound, and ask for the least such size.
>
> *References:*
> - [Wikipedia on packing of squares](https://en.wikipedia.org/wiki/Square_packing)
> - [Wikipedia on packing of circles in a circle](https://en.wikipedia.org/wiki/Circle_packing_in_a_circle)
> - [Wikipedia on packing of circles in a square](https://en.wikipedia.org/wiki/Circle_packing_in_a_square)
> - Friedman, Erich (2009), "Packing unit squares in squares: a survey and new results",
>   Electronic Journal of Combinatorics, 1000, Dynamic Survey 7
> - Pirl, U. (1969),
>   ["Der Mindestabstand von $n$ in der Einheitskreisscheibe gelegenen Punkten"](https://doi.org/10.1002/mana.19690400110),
>   Mathematische Nachrichten, 40: 111–124
> - A website with visualizations of packings:
>   [link](https://erich-friedman.github.io/packing/)
> - [Erich Friedman, Squares in Circles](https://erich-friedman.github.io/packing/squincir/)
> - [The-Anh Vu-Le, Lean 4 proof of Squares in Circles](https://github.com/vltanh/lean4-squares-in-circles)
> - [Kenta Kitamura, Lean proof of the exact three-square minimum for Formal Conjectures](https://github.com/KitaKen1/three-squares-in-a-circle-lean/blob/87bd2b6915933cf608a3cae6263c2500fe81f7ec/lean/ThreeSquares/Compressed/Main.lean#L216-L219)

*Quoted from [FormalConjectures/Wikipedia/SquarePacking.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 4 open, 1 solved and 5 textbook results. It also has 1 test statement, counted here but not shown.

## `SquarePacking.eleven_square_packing_in_square_bound`

Textbook result, stated without proof.

> Eleven unit squares can be packed into a square of side length < 3.877084.
>
> Reference: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_square)

```lean
theorem eleven_square_packing_in_square_bound :
    Nonempty (Packing 11 UnitSquare (Square 3.877084))
```

Category `textbook`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L109).

## `SquarePacking.least_eleven_square_packing_in_square`

Open: stated without proof.

> What is the smallest square that can contain 11 unit squares?
>
> Reference: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_square)

```lean
theorem least_eleven_square_packing_in_square :
    IsLeast {x : ℝ | Nonempty (Packing 11 UnitSquare (Square x))}
      least_eleven_square_packing_in_square.answer
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L121).

## `SquarePacking.seventeen_square_packing_in_square_bound`

Textbook result, stated without proof.

> Seventeen unit squares can be packed into a square of side length < 4.6756.
>
> Reference: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_square)

```lean
theorem seventeen_square_packing_in_square_bound :
    Nonempty (Packing 17 UnitSquare (Square 4.6756))
```

Category `textbook`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L132).

## `SquarePacking.least_seventeen_square_packing_in_square`

Open: stated without proof.

> What is the smallest square that can contain 17 unit squares?
>
> Reference: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_square)

```lean
theorem least_seventeen_square_packing_in_square :
    IsLeast {x : ℝ | Nonempty (Packing 17 UnitSquare (Square x))}
      least_seventeen_square_packing_in_square.answer
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L144).

## `SquarePacking.three_square_packing_in_circle_bound`

Textbook result, stated without proof.

> Three unit squares can be packed into a circle of radius $(5 \sqrt{17}) / 16 \approx 1.288$.
>
> Reference: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_circle)

```lean
theorem three_square_packing_in_circle_bound :
    Nonempty (Packing 3 UnitSquare (Circle ((5 * NNReal.sqrt 17) / 16)))
```

Category `textbook`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L155).

## `SquarePacking.least_three_square_packing_in_circle`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/three-squares-in-a-circle-lean/blob/87bd2b6915933cf608a3cae6263c2500fe81f7ec/lean/ThreeSquares/Compressed/Main.lean#L216-L219](https://github.com/KitaKen1/three-squares-in-a-circle-lean/blob/87bd2b6915933cf608a3cae6263c2500fe81f7ec/lean/ThreeSquares/Compressed/Main.lean#L216-L219).

> What is the smallest circle that can contain 3 unit squares?
>
> The least radius is $5\sqrt{17}/16$. The-Anh Vu-Le proved optimality in
> September 2026. Kenta Kitamura gave a separate Lean proof of this exact
> `IsLeast` statement using the `SquarePacking` definitions in this file.
>
> References: [Wikipedia](https://en.wikipedia.org/wiki/Square_packing#In_a_circle),
> [Friedman's table](https://erich-friedman.github.io/packing/squincir/),
> [Vu-Le's Lean proof](https://github.com/vltanh/lean4-squares-in-circles), and
> [Kitamura's FC-target Lean proof](https://github.com/KitaKen1/three-squares-in-a-circle-lean/blob/87bd2b6915933cf608a3cae6263c2500fe81f7ec/lean/ThreeSquares/Compressed/Main.lean#L216-L219).

```lean
theorem least_three_square_packing_in_circle :
    IsLeast {r : ℝ≥0 | Nonempty (Packing 3 UnitSquare (Circle r))}
      least_three_square_packing_in_circle.answer
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 177](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L177).

## `SquarePacking.twenty_one_circle_packing_in_square_bound`

Textbook result, stated without proof.

> Twenty-one unit circles can be packed into a square of side length < 9.359.
>
> Reference: [Visualizations](https://erich-friedman.github.io/packing/cirinsqu/)

```lean
theorem twenty_one_circle_packing_in_square_bound :
    Nonempty (Packing 21 UnitCircle (Square 9.359))
```

Category `textbook`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 188](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L188).

## `SquarePacking.least_twenty_one_circle_packing_in_square`

Open: stated without proof.

> What is the smallest square that can contain 21 unit circles?

```lean
theorem least_twenty_one_circle_packing_in_square :
    IsLeast {x : ℝ | Nonempty (Packing 21 UnitCircle (Square x))}
      least_twenty_one_circle_packing_in_square.answer
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L198).

## `SquarePacking.fifteen_circle_packing_in_circle_bound`

Textbook result, stated without proof.

> Fifteen unit circles can be packed into a circle of radius
> $1 + \sqrt{6 + 2/\sqrt{5} + 4 \sqrt{1 + 2/\sqrt{5}}} \approx 4.521$.
>
> Reference:
> Graham RL, Lubachevsky BD, Nurmela KJ, Ostergard PRJ.
> Dense packings of congruent circles in a circle. Discrete Math 1998;181:139–154.

```lean
theorem fifteen_circle_packing_in_circle_bound :
    Nonempty (Packing 15 UnitCircle
      (Circle (1 + NNReal.sqrt (6 + 2 / NNReal.sqrt 5 +
        4 * NNReal.sqrt (1 + 2 / NNReal.sqrt 5)))))
```

Category `textbook`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 212](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L212).

## `SquarePacking.least_fifteen_circle_packing_in_circle`

Open: stated without proof.

> What is the smallest circle that can contain 15 unit circles?
>
> Reference:
> Graham RL, Lubachevsky BD, Nurmela KJ, Ostergard PRJ.
> Dense packings of congruent circles in a circle. Discrete Math 1998;181:139–154.
> [Pirl (1969)](https://doi.org/10.1002/mana.19690400110) conjectured this configuration to be optimal.

```lean
theorem least_fifteen_circle_packing_in_circle :
    IsLeast {r : ℝ≥0 | Nonempty (Packing 15 UnitCircle (Circle r))}
      least_fifteen_circle_packing_in_circle.answer
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SquarePacking.lean, line 229](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean#L229).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SquarePacking.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquarePacking.lean)
- [Wikipedia on packing of squares](https://en.wikipedia.org/wiki/Square_packing)
