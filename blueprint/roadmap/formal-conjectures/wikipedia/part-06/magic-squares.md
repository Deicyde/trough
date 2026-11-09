---
declaration: theorem
origin: cited
lean: MagicSquares.exists_magic_square_squares, MagicSquares.exists_semi_magic_square_cubes
statement: formalized
---

# Magic Squares

> *References:*
>
> * [Magic Square of Squares - Wikipedia](https://en.wikipedia.org/wiki/Magic_square_of_squares)
> * [multimagie.com](http://www.multimagie.com/English/SquaresOfSquaresSearch.htm)
> * [Semi-Magic Square of Cubes](https://unsolvedproblems.org/index_files/SquareofCubes.htm)
> * [Magic Square of Squares](https://static.nsta.org/pdfs/QuantumV6N3.pdf)

*Quoted from [FormalConjectures/Wikipedia/MagicSquares.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MagicSquares.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `MagicSquares.exists_magic_square_squares`

Open: stated without proof.

> Does there exist a $3 \times 3$ matrix such that every entry is a distinct square,
> and all rows, columns, and diagonals add up to the same value?
>
> 0 is excluded, as a Magic Square of Squares with 0 and 8 distinct squares is know is knownn.
> See [Magic Square of Squares](https://static.nsta.org/pdfs/QuantumV6N3.pdf)

```lean
theorem exists_magic_square_squares :
    ∃ m : Fin 3 → Fin 3 → ℕ, ∃ t : ℕ,
       m.Injective2 ∧
       (∀ i j, 0 < (m i j) ∧ IsSquare (m i j)) ∧
       (∀ i, ∑ j, m i j = t) ∧
       (∀ j, ∑ i, m i j = t) ∧
       m 0 0 + m 1 1 + m 2 2 = t ∧
       m 0 2 + m 1 1 + m 2 0 = t
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MagicSquares.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MagicSquares.lean#L43).

## `MagicSquares.exists_semi_magic_square_cubes`

Open: stated without proof.

> Does there exist a $3 \times 3$ semi-magic square whose entries are all distinct positive
> integer cubes? A square is semi-magic if all rows and columns sum to the same total.
>
> More precisely, we seek a $3 \times 3$ matrix with entries $a_{ij}$ such that each
> $a_{ij} = n_{ij}^3$ for some positive integer $n_{ij}$, all nine cubes are distinct,
> and all row sums and column sums are equal.
>
> *Reference:*
> [Semi-Magic Square of Cubes](https://unsolvedproblems.org/index_files/SquareofCubes.htm)

```lean
theorem exists_semi_magic_square_cubes :
    ∃ m : Fin 3 → Fin 3 → ℕ, ∃ t : ℕ,
       m.Injective2 ∧
       (∀ i j, ∃ n : ℕ, 0 < n ∧ m i j = n ^ 3) ∧
       (∀ i, ∑ j, m i j = t) ∧
       (∀ j, ∑ i, m i j = t)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MagicSquares.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MagicSquares.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MagicSquares.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/MagicSquares.lean)
- [Magic Square of Squares - Wikipedia](https://en.wikipedia.org/wiki/Magic_square_of_squares)
