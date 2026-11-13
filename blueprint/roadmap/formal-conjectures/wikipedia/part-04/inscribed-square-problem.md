---
declaration: theorem
origin: cited
lean: InscribedSquare.inscribed_square_problem, InscribedSquare.inscribed_rectangle_problem, InscribedSquare.exists_inscribed_rectangle, InscribedSquare.exists_inscribed_rectangle_of_smooth, InscribedSquare.exists_inscribed_square_of_C2
statement: formalized
---

# Inscribed square problem

> The *inscribed square problem* or *Toeplitz conjecture* asks whether every Jordan curve (i.e. simple
> close curve in ℝ²) admits an inscribed square, i.e. a square whose vertices all lie on the curve.
> There are several open and solved variants of this conjecture.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Inscribed_square_problem)
>  - [A Survey on the Square Peg Problem](https://www.researchgate.net/publication/274622766_A_Survey_on_the_Square_Peg_Problem)
>    by *Benjamin Matschke*
>  - [arxiv/2005.09193](https://arxiv.org/abs/2005.09193)

*Quoted from [FormalConjectures/Wikipedia/InscribedSquare.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `InscribedSquare.inscribed_square_problem`

Open: stated without proof.

> **Inscribed square problem**
> Does every Jordan curve admit an inscribed square?

```lean
theorem inscribed_square_problem :
    ∀ (γ : Circle → ℝ²) (hγ : IsEmbedding γ),
      ∃ t₁ t₂ t₃ t₄, IsRectangle (γ t₁) (γ t₂) (γ t₃) (γ t₄) 1
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/InscribedSquare.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean#L57).

## `InscribedSquare.inscribed_rectangle_problem`

Open: stated without proof.

> **Inscribed rectangle problem**
> Does every Jordan curve admit inscribed rectangles of any given aspect ratio?

```lean
theorem inscribed_rectangle_problem :
    ∀ (γ : Circle → ℝ²) (hγ : IsEmbedding γ) (r : ℝ) (hr : r > 0),
      ∃ t₁ t₂ t₃ t₄, IsRectangle (γ t₁) (γ t₂) (γ t₃) (γ t₄) r
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/InscribedSquare.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean#L67).

## `InscribedSquare.exists_inscribed_rectangle`

Solved: stated here without proof.

> It is known that every Jordan curve admits at least one inscribed rectangle.

```lean
theorem exists_inscribed_rectangle (γ : Circle → ℝ²) (hγ : IsEmbedding γ) :
    ∃ t₁ t₂ t₃ t₄ r, IsRectangle (γ t₁) (γ t₂) (γ t₃) (γ t₄) r
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/InscribedSquare.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean#L76).

## `InscribedSquare.exists_inscribed_rectangle_of_smooth`

Solved: stated here without proof.

> It is known that every *smooth* Jordan curve admits inscribed rectangles of all aspect ratios.
> Here a smooth Jordan curve is a smooth embedding of the circle into the plane, i.e. a smooth
> simple closed curve with nowhere vanishing velocity.

```lean
theorem exists_inscribed_rectangle_of_smooth (γ : Circle → ℝ²)
    (hγ : IsSmoothEmbedding (𝓡 1) (𝓡 2) ∞ γ) (r : ℝ) (hr : r > 0) :
    ∃ t₁ t₂ t₃ t₄, IsRectangle (γ t₁) (γ t₂) (γ t₃) (γ t₄) r
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/InscribedSquare.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean#L86).

## `InscribedSquare.exists_inscribed_square_of_C2`

Solved: stated here without proof.

> It is also known that every $C^2$ Jordan curve admits an inscribed square.
> Here a $C^2$ Jordan curve is a $C^2$ embedding of the circle into the plane, i.e. a $C^2$
> simple closed curve with nowhere vanishing velocity.

```lean
theorem exists_inscribed_square_of_C2 (γ : Circle → ℝ²)
    (hγ : IsSmoothEmbedding (𝓡 1) (𝓡 2) 2 γ) :
    ∃ t₁ t₂ t₃ t₄, IsRectangle (γ t₁) (γ t₂) (γ t₃) (γ t₄) 1
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/InscribedSquare.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/InscribedSquare.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InscribedSquare.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Inscribed_square_problem)
