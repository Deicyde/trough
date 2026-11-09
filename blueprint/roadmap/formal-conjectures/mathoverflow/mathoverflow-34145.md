---
declaration: theorem
origin: cited
lean: Mathoverflow34145.rectangles_cover_unit_square, Mathoverflow34145.rectangles_pack_unit_square, Mathoverflow34145.rectangles_pack_square_133_div_132, Mathoverflow34145.rectangles_pack_square_501_div_500
statement: formalized
---

# Mathoverflow 34145

> Can the unit square be covered by $1/k$-by-$1/(k+1)$ rectangles (across $1 \le k$ natural)?
>
> I am deliberately not requiring that the rotations can only be $0^\circ, 90^\circ, 180^\circ, \text{ or } 270^\circ$.
>
> Because of indexing, since `n : ℕ` starts at 0, we change the side lengths to $1 / (n + 1)$ and
> $1 / (n + 2)$, so that the first rectangle is $1/1$ by $1/2$, the second is $1/2$ by $1/3$, etc.
>
> *Reference:* [mathoverflow/34145](https://mathoverflow.net/q/34145)
> asked by user [*Kaveh*](https://mathoverflow.net/users/7507/kaveh)

*Quoted from [FormalConjectures/Mathoverflow/34145.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 6 test statements, counted here but not shown.

## `Mathoverflow34145.rectangles_cover_unit_square`

Open: stated without proof.

> Can a unit square be covered by rectangles of width `1 / (n + 1)` and height `1 / (n + 2)`?

```lean
theorem rectangles_cover_unit_square :
    ∃ c : Configuration, ∀ p ∈ unitSquare, ∃ n, p ∈ (c.rect n).toSet
```

Category `research open`; AMS [51 Geometry](../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Mathoverflow/34145.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean#L146).

## `Mathoverflow34145.rectangles_pack_unit_square`

Open: stated without proof.

> Equivalently, can a unit square be packed with rectangles of width `1 / (n + 1)` and height
> `1 / (n + 2)`?

```lean
theorem rectangles_pack_unit_square :
    ∃ c : Configuration, (∀ n, (c.rect n).toSet ⊆ unitSquare) ∧ c.IsPacking
```

Category `research open`; AMS [51 Geometry](../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Mathoverflow/34145.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean#L153).

## `Mathoverflow34145.rectangles_pack_square_133_div_132`

Solved: stated here without proof.

> It is known that packing the rectangles into a square of side length `133/132` is possible.
>
> Reference: https://www.sciencedirect.com/science/article/pii/0097316594901163

```lean
theorem rectangles_pack_square_133_div_132 :
    (∃ c : Configuration,
      (∀ n, (c.rect n).toSet ⊆ Rectangle.toSet ⟨133/132, 133/132, (0, 0), 0⟩) ∧
      c.IsPacking)
```

Category `research solved`; AMS [51 Geometry](../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Mathoverflow/34145.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean#L162).

## `Mathoverflow34145.rectangles_pack_square_501_div_500`

Solved: stated here without proof.

> It is known that packing the rectangles into a square of side length `501/500` is possible.
>
> Reference: https://www.sciencedirect.com/science/article/pii/S0167506008706009

```lean
theorem rectangles_pack_square_501_div_500 :
    (∃ c : Configuration,
      (∀ n, (c.rect n).toSet ⊆ Rectangle.toSet ⟨501/500, 501/500, (0, 0), 0⟩) ∧
      c.IsPacking)
```

Category `research solved`; AMS [51 Geometry](../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Mathoverflow/34145.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean#L173).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/34145.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/34145.lean)
- [mathoverflow/34145](https://mathoverflow.net/q/34145)
