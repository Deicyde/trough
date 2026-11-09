---
declaration: theorem
origin: cited
lean: Arxiv.«math.0110202».banach_mazur_rotation_problem, Arxiv.«math.0110202».banach_mazur_rotation_problem.finite_dimensional
statement: formalized
---

# Banach-Mazur Rotation Problem

> *References:*
> - [arxiv/math.0110202](https://arxiv.org/abs/math/0110202)
>   **A note on Banach--Mazur problem** by *Beata Randrianantoanina*
> - [mathoverflow/41211](https://mathoverflow.net/questions/41211/easy-proof-of-the-fact-that-isotropic-spaces-are-euclidean)
>   **Easy proof of the fact that isotropic spaces are Euclidean**

*Quoted from [FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 API statements, counted here but not shown.

## `Arxiv.«math.0110202».banach_mazur_rotation_problem`

Open: stated without proof.

> The Banach--Mazur rotation problem asks whether every separable Banach space whose group of linear
> isometric equivalences acts transitively on the unit sphere is linearly isometric to a Hilbert
> space.

```lean
theorem banach_mazur_rotation_problem :
    ∀ (E : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [SeparableSpace E]
      [IsPretransitive (E ≃ₗᵢ[ℝ] E) (sphere (0 : E) 1)], ∃ (H : Type*) (_ : NormedAddCommGroup H)
      (_ : InnerProductSpace ℝ H),
      Nonempty (E ≃ₗᵢ[ℝ] H)
```

Category `research open`; AMS [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean#L90).

## `Arxiv.«math.0110202».banach_mazur_rotation_problem.finite_dimensional`

Solved: stated here without proof.

> Every finite-dimensional real normed space whose isometry group acts transitively on the
> unit sphere is Euclidean.

```lean
theorem banach_mazur_rotation_problem.finite_dimensional {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℝ E] [FiniteDimensional ℝ E] [IsPretransitive (E ≃ₗᵢ[ℝ] E) (sphere (0 : E) 1)] :
    InnerProductSpaceable E
```

Category `research solved`; AMS [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean)
- [arxiv/math.0110202](https://arxiv.org/abs/math/0110202)
