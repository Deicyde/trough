---
declaration: module
origin: cited
lean: ProbabilisticTheory.Qubit, ProbabilisticTheory.Qubit.stateEquiv, ProbabilisticTheory.Qubit.toDualEquiv, ProbabilisticTheory.Qubit.blochVec, ProbabilisticTheory.Qubit.norm_blochVec, ProbabilisticTheory.Qubit.blochVec_injective, ProbabilisticTheory.Qubit.purePoint, ProbabilisticTheory.Qubit.image_toDualEquiv_closedBall
statement: formalized
proof: formalized
---

# The qubit, in Bloch-vector coordinates

The module `PhyslibAlpha.ProbabilisticTheory.Examples.Qubit`, [PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean): 11 declarations, 7 with a docstring.

> The qubit as the Euclidean norm cone over `ℝ³`: its states form the Bloch ball, not a simplex.

## i. Overview

> A qubit state is a density matrix `ρ = ½(r • I + x · σ)`, given by a number `r` and a Bloch
> vector `x ∈ ℝ³`, and `ρ` is positive exactly when `‖x‖ ≤ r`. So in Bloch coordinates the qubit is
> the norm cone over Euclidean `ℝ³`. Its states form the Bloch ball and every point of the Bloch
> sphere is a pure state. With infinitely many pure states, the state space is not a simplex: the
> qubit is not classical.

## ii. Key results

> - `ProbabilisticTheory.Qubit` : the qubit in Bloch coordinates.
> - `ProbabilisticTheory.Qubit.stateEquiv` : the states are the Bloch ball.
> - `ProbabilisticTheory.Qubit.isPure_purePoint` : unit Bloch vectors give pure states.
> - `ProbabilisticTheory.Qubit.not_isSimplex_stateSpace` : the state space is not a simplex.

## iv. References

> - J. Barrett, *Information processing in generalized probabilistic theories*, Phys. Rev. A 75,
>   032304 (2007).
> - P. Janotta and H. Lal, *Generalized probabilistic theories without the no-restriction
>   hypothesis*, Phys. Rev. A 87, 052131 (2013).

## A. The qubit as a norm cone

**`ProbabilisticTheory.Qubit`**, an abbrev, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L58).

> The qubit in Bloch coordinates: `ℝ × ℝ³` ordered by the Lorentz cone.

```lean
abbrev Qubit : Type
```

**`ProbabilisticTheory.Qubit.stateEquiv`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L65).

> The states of the qubit are the Bloch ball.

```lean
noncomputable def stateEquiv :
    𝓢[ℝ, Qubit] ≃ {a : Fin 3 → ℝ // ∑ i, |a i| ^ (2 : ℝ) ≤ 1}
```

## B. Infinitely many pure states

**`ProbabilisticTheory.Qubit.toDualEquiv`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L83).

> The Riesz isomorphism between `EuclideanSpace ℝ (Fin 3)` and its dual.

```lean
noncomputable def toDualEquiv :
    EuclideanSpace ℝ (Fin 3) ≃ₗᵢ[ℝ] (EuclideanSpace ℝ (Fin 3) →L[ℝ] ℝ)
```

**`ProbabilisticTheory.Qubit.blochVec`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L88).

> The Bloch vector `(t, √(1 - t²), 0)`, a unit vector for `t ∈ [0, 1]`.

```lean
noncomputable def blochVec (t : ℝ) : EuclideanSpace ℝ (Fin 3)
```

**`ProbabilisticTheory.Qubit.norm_blochVec`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L91).

```lean
lemma norm_blochVec {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t ≤ 1) : ‖blochVec t‖ = 1
```

**`ProbabilisticTheory.Qubit.blochVec_injective`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L103).

```lean
lemma blochVec_injective : Function.Injective fun t : Set.Icc (0 : ℝ) 1 => blochVec t
```

**`ProbabilisticTheory.Qubit.purePoint`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L111).

> The pure state dual to the Bloch vector at parameter `t ∈ [0, 1]`.

```lean
noncomputable def purePoint (t : Set.Icc (0 : ℝ) 1) : 𝓢[ℝ, Qubit]
```

**`ProbabilisticTheory.Qubit.image_toDualEquiv_closedBall`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L115).

```lean
lemma image_toDualEquiv_closedBall :
    toDualEquiv '' Metric.closedBall (0 : EuclideanSpace ℝ (Fin 3)) 1 = {g | ‖g‖ ≤ 1}
```

**`ProbabilisticTheory.Qubit.isPure_purePoint`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L124).

> Every state `purePoint t` is pure: its Bloch vector lies on the sphere, and the sphere
> consists of extreme points of the ball.

```lean
lemma isPure_purePoint (t : Set.Icc (0 : ℝ) 1) : (purePoint t).IsPure
```

**`ProbabilisticTheory.Qubit.purePoint_injective`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L130).

```lean
lemma purePoint_injective : Function.Injective purePoint
```

**`ProbabilisticTheory.Qubit.not_isSimplex_stateSpace`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean#L135).

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

- [PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/Qubit.lean)
