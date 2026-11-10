---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.resolution_of_singularities, AlgebraicGeometry.resolution_of_singularities_of_charZero, AlgebraicGeometry.resolution_of_singularities_of_topologicalKrullDim_le_three, AlgebraicGeometry.exists_not_hasResolution_of_not_perfectField
statement: formalized
---

# Resolution of singularities

> A variety $X$ over a field $k$ admits a resolution of singularities if there is a smooth
> $k$-variety $Y$ and a proper birational morphism $Y \to X$. Hironaka proved that every variety
> over a field of characteristic zero admits one. In positive characteristic this is known over a
> perfect field in dimension at most three, and is open from dimension four on. Perfectness of $k$
> cannot be dropped from the statement in this form: over an imperfect field it fails already in
> dimension zero, see `exists_not_hasResolution_of_not_perfectField` below. Over an arbitrary field
> one asks instead that $Y$ be regular.
>
> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Resolution_of_singularities)
> * [Hir1964] H. Hironaka, Resolution of singularities of an algebraic variety over a field of
>   characteristic zero, [I](https://doi.org/10.2307/1970486) and
>   [II](https://doi.org/10.2307/1970547), Ann. of Math. 79 (1964), 109--203 and 205--326.
> * [Kol2007] J. Kollár, [Resolution of singularities -- Seattle
>   lecture](https://arxiv.org/abs/math/0508332), Theorem 36.
> * [Hau2010] H. Hauser, [On the problem of resolution of singularities in positive characteristic
>   (or: a proof we are still waiting for)](https://doi.org/10.1090/S0273-0979-09-01274-9),
>   Bull. Amer. Math. Soc. 47 (2010), 1--30.
> * [Lip1978] J. Lipman, [Desingularization of two-dimensional
>   schemes](https://doi.org/10.2307/1971141), Ann. of Math. 107 (1978), 151--207.
> * [CP2008] V. Cossart and O. Piltant, [Resolution of singularities of threefolds in positive
>   characteristic I](https://doi.org/10.1016/j.jalgebra.2008.03.032), J. Algebra 320 (2008),
>   1051--1082.
> * [CP2009] V. Cossart and O. Piltant, [Resolution of singularities of threefolds in positive
>   characteristic II](https://doi.org/10.1016/j.jalgebra.2008.11.030), J. Algebra 321 (2009),
>   1836--1976.
> * [CP2019] V. Cossart and O. Piltant, [Resolution of singularities of arithmetical
>   threefolds](https://doi.org/10.1016/j.jalgebra.2019.02.017), J. Algebra 529 (2019), 268--535.

*Quoted from [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result. It also has 1 test statement and 1 API statement, counted here but not shown.

## `AlgebraicGeometry.resolution_of_singularities`

Open: stated without proof.

> **Resolution of singularities in positive characteristic.**
> Let $k$ be a perfect field of characteristic $p > 0$ and let $X$ be an integral scheme that is
> separated and of finite type over $k$. Then there is an integral scheme $Y$ that is smooth over
> $k$ together with a proper birational morphism $Y \to X$.
>
> This is open from dimension four on; see [Hau2010]. Perfectness of $k$ is needed for the
> conclusion as stated; see `exists_not_hasResolution_of_not_perfectField`.

```lean
theorem resolution_of_singularities (k : Type u) [Field k] [PerfectField k] (p : ℕ)
    [Fact p.Prime] [CharP k p] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k)) [IsIntegral X]
    [LocallyOfFiniteType sX] [QuasiCompact sX] [IsSeparated sX] :
    Scheme.HasResolution sX
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean#L105).

## `AlgebraicGeometry.resolution_of_singularities_of_charZero`

Solved: stated here without proof.

> **Hironaka's theorem.** Every integral scheme that is separated and of finite type over a field
> of characteristic zero admits a resolution of singularities. This is the main theorem of
> [Hir1964]; see [Kol2007], Theorem 36, for a statement in the generality used here.

```lean
theorem resolution_of_singularities_of_charZero (k : Type u) [Field k] [CharZero k]
    {X : Scheme.{u}} (sX : X ⟶ Spec (.of k)) [IsIntegral X] [LocallyOfFiniteType sX]
    [QuasiCompact sX] [IsSeparated sX] :
    Scheme.HasResolution sX
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean#L117).

## `AlgebraicGeometry.resolution_of_singularities_of_topologicalKrullDim_le_three`

Solved: stated here without proof.

> Resolution of singularities holds in dimension at most three over any perfect field. In
> characteristic zero this is [Hir1964]. In positive characteristic, dimension at most two is
> [Lip1978] and dimension three is due to Cossart and Piltant: [CP2008] and [CP2009] prove it for
> quasi-projective varieties over a field that is differentially finite over a perfect subfield,
> and [CP2019], Theorem 1.1, removes both restrictions, resolving every reduced separated
> Noetherian quasi-excellent scheme of dimension at most three in any characteristic. That theorem
> gives an everywhere regular source, which over a perfect field is the same as a smooth one. The
> problem is open in positive characteristic from dimension four on.

```lean
theorem resolution_of_singularities_of_topologicalKrullDim_le_three (k : Type u) [Field k]
    [PerfectField k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k)) [IsIntegral X]
    [LocallyOfFiniteType sX] [QuasiCompact sX] [IsSeparated sX]
    (hX : topologicalKrullDim X ≤ 3) :
    Scheme.HasResolution sX
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean#L134).

## `AlgebraicGeometry.exists_not_hasResolution_of_not_perfectField`

Textbook result, stated without proof.

> **Resolution of singularities fails over imperfect fields.**
> If the field $k$ is not perfect, then there is an integral scheme $X$ of dimension zero that is
> separated and of finite type over $k$ and has no resolution of singularities: no integral scheme
> smooth over $k$ admits a proper birational morphism to $X$.
>
> A witness: $k$ has characteristic $p > 0$ and there is some $a \in k \setminus k^p$. Take
> $X = \operatorname{Spec} k(a^{1/p})$. Every integral scheme birational to $X$ has function field
> $k(a^{1/p})$, which is not separable over $k$, whereas the function field of an integral scheme
> smooth over $k$ is separable over $k$.
>
> So the hypothesis `PerfectField k` cannot be dropped from `resolution_of_singularities` or from
> `resolution_of_singularities_of_topologicalKrullDim_le_three`.

```lean
theorem exists_not_hasResolution_of_not_perfectField (k : Type u) [Field k]
    (hk : ¬ PerfectField k) :
    ∃ (X : Scheme.{u}) (sX : X ⟶ Spec (.of k)), IsIntegral X ∧ LocallyOfFiniteType sX ∧
      QuasiCompact sX ∧ IsSeparated sX ∧ topologicalKrullDim X = 0 ∧
      ¬ Scheme.HasResolution sX
```

Category `textbook`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ResolutionOfSingularities.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ResolutionOfSingularities.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Resolution_of_singularities)
