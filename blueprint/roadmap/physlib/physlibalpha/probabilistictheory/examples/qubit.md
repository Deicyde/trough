---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Qubit, PhyslibAlpha.ProbabilisticTheory.Qubit.stateEquiv, PhyslibAlpha.ProbabilisticTheory.Qubit.toDualEquiv, PhyslibAlpha.ProbabilisticTheory.Qubit.blochVec, PhyslibAlpha.ProbabilisticTheory.Qubit.norm_blochVec, PhyslibAlpha.ProbabilisticTheory.Qubit.blochVec_injective, PhyslibAlpha.ProbabilisticTheory.Qubit.purePoint, PhyslibAlpha.ProbabilisticTheory.Qubit.image_toDualEquiv_closedBall
statement: formalized
proof: formalized
---

# The qubit, in Bloch-vector coordinates

The module `PhyslibAlpha.ProbabilisticTheory.Examples.Qubit`, [PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean): 11 declarations, 7 with a docstring.

> The qubit as the Euclidean norm cone over `ℝ³`: its states form the Bloch ball, not a simplex.

## i. Overview

> A qubit state is a density matrix `ρ = ½(r • I + x · σ)`, given by a number `r` and a Bloch
> vector `x ∈ ℝ³`, and `ρ` is positive exactly when `‖x‖ ≤ r`. So in Bloch coordinates the qubit is
> the norm cone over Euclidean `ℝ³`. Its states form the Bloch ball and every point of the Bloch
> sphere is a pure state. With infinitely many pure states, the state space is not a simplex: the
> qubit is not classical.

## ii. Key results

> - `PhyslibAlpha.ProbabilisticTheory.Qubit` : the qubit in Bloch coordinates.
> - `PhyslibAlpha.ProbabilisticTheory.Qubit.stateEquiv` : the states are the Bloch ball.
> - `PhyslibAlpha.ProbabilisticTheory.Qubit.isPure_purePoint` : unit Bloch vectors give pure states.
> - `PhyslibAlpha.ProbabilisticTheory.Qubit.not_isSimplex_stateSpace` : the state space is not
>   a simplex.

## iv. References

> - J. Barrett, *Information processing in generalized probabilistic theories*, Phys. Rev. A 75,
>   032304 (2007).
> - P. Janotta and H. Lal, *Generalized probabilistic theories without the no-restriction
>   hypothesis*, Phys. Rev. A 87, 052131 (2013).

## A. The qubit as a norm cone

**`PhyslibAlpha.ProbabilisticTheory.Qubit`**, an abbrev, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L59).

> The qubit in Bloch coordinates: `ℝ × ℝ³` ordered by the Lorentz cone.

```lean
abbrev Qubit : Type
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.stateEquiv`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L66).

> The states of the qubit are the Bloch ball.

```lean
noncomputable def stateEquiv :
    𝓢[ℝ, Qubit] ≃ {a : Fin 3 → ℝ // ∑ i, |a i| ^ (2 : ℝ) ≤ 1}
```

## B. Infinitely many pure states

**`PhyslibAlpha.ProbabilisticTheory.Qubit.toDualEquiv`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L84).

> The Riesz isomorphism between `EuclideanSpace ℝ (Fin 3)` and its dual.

```lean
noncomputable def toDualEquiv :
    EuclideanSpace ℝ (Fin 3) ≃ₗᵢ[ℝ] (EuclideanSpace ℝ (Fin 3) →L[ℝ] ℝ)
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.blochVec`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L89).

> The Bloch vector `(t, √(1 - t²), 0)`, a unit vector for `t ∈ [0, 1]`.

```lean
noncomputable def blochVec (t : ℝ) : EuclideanSpace ℝ (Fin 3)
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.norm_blochVec`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L92).

```lean
lemma norm_blochVec {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t ≤ 1) : ‖blochVec t‖ = 1
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.blochVec_injective`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L104).

```lean
lemma blochVec_injective : Function.Injective fun t : Set.Icc (0 : ℝ) 1 => blochVec t
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.purePoint`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L112).

> The pure state dual to the Bloch vector at parameter `t ∈ [0, 1]`.

```lean
noncomputable def purePoint (t : Set.Icc (0 : ℝ) 1) : 𝓢[ℝ, Qubit]
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.image_toDualEquiv_closedBall`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L116).

```lean
lemma image_toDualEquiv_closedBall :
    toDualEquiv '' Metric.closedBall (0 : EuclideanSpace ℝ (Fin 3)) 1 = {g | ‖g‖ ≤ 1}
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.isPure_purePoint`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L125).

> Every state `purePoint t` is pure: its Bloch vector lies on the sphere, and the sphere
> consists of extreme points of the ball.

```lean
lemma isPure_purePoint (t : Set.Icc (0 : ℝ) 1) : (purePoint t).IsPure
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.purePoint_injective`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L131).

```lean
lemma purePoint_injective : Function.Injective purePoint
```

**`PhyslibAlpha.ProbabilisticTheory.Qubit.not_isSimplex_stateSpace`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L136).

> **The qubit is not classical**: it has infinitely many pure states, while a simplex has
> finitely many extreme points.

```lean
lemma not_isSimplex_stateSpace :
    ¬ IsSimplex (UnitalPositiveLinearMap.algebraicStateSpace (E := Qubit))
```

## Depends on

- [Simplices](../../mathematics/part-02/geometry/simplex.md)
- [Order-unit spaces built from a normed vector space](normcone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean)
