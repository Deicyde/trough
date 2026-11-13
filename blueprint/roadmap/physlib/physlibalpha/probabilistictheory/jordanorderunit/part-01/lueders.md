---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra.effectSqrt, ProbabilisticTheory.NormedJordanAlgebra.luedersMap, ProbabilisticTheory.NormedJordanAlgebra.luedersMap_apply, ProbabilisticTheory.NormedJordanAlgebra.luedersMap_one, ProbabilisticTheory.NormedJordanAlgebra.luedersOperation, ProbabilisticTheory.NormedJordanAlgebra.luedersOperation_apply, ProbabilisticTheory.NormedJordanAlgebra.luedersOperation_outcomeEffect, ProbabilisticTheory.NormedJordanAlgebra.effectSqrt_toEffect_of_projection
statement: formalized
proof: formalized
---

# Lüders operations

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Lueders`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean): 14 declarations, 12 with a docstring.

> Lüders operations `x ↦ U_{√e} x` of effects and the states conditioned on effects.

## i. Overview

> An effect `e` of an ordered JB-algebra has a positive square root. The Lüders operation of `e` is
> the quadratic representation `x ↦ U_{√e} x`, and conditioning a state on `e` is `x ↦ ω(U\_\{√e} x) /
> ω(e)`. For a projection this is conditioning on the projection.

## ii. Key results

> - `NormedJordanAlgebra.luedersMap` : the Lüders map of an effect.
> - `NormedJordanAlgebra.luedersOperation` : the Lüders operation.
> - `NormedJordanAlgebra.luedersCondition` : the state conditioned on an effect.
> - `NormedJordanAlgebra.luedersCondition_isNormal` : conditioning preserves normality.

## iv. References

> * None.

## A. The Lüders operation

**`ProbabilisticTheory.NormedJordanAlgebra.effectSqrt`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L59).

> The intrinsic positive square root selected by the JB continuous functional calculus for an
> effect.

```lean
noncomputable def effectSqrt (e : Effect E) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersMap`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L64).

> The Lüders operation of an effect: the positive quadratic operation induced by its square
> root.  In a special Jordan algebra it is precisely `x ↦ sqrt(e) x sqrt(e)`.

```lean
noncomputable def luedersMap (e : Effect E) : E →ₚ[ℝ] E
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersMap_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L68).

```lean
lemma luedersMap_apply (e : Effect E) (x : E) : luedersMap e x = U (effectSqrt e) x
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersMap_one`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L73).

> A Lüders operation sends the order unit to its effect.  Thus its probability in a state is
> exactly the probability assigned to that effect.

```lean
lemma luedersMap_one (e : Effect E) : luedersMap e (1 : E) = e
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersOperation`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L80).

> The Lüders map is an operation: it is positive and its outcome probability never exceeds
> certainty.  Its outcome effect is the original effect, so this is the intrinsic Jordan analogue
> of a single-Kraus measurement operation.

```lean
noncomputable def luedersOperation (e : Effect E) : Operation E
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersOperation_apply`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L84).

```lean
lemma luedersOperation_apply (e : Effect E) (x : E) : luedersOperation e x = luedersMap e x
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersOperation_outcomeEffect`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L88).

> The effect recorded by the Lüders operation is exactly the effect it implements.

```lean
lemma luedersOperation_outcomeEffect (e : Effect E) :
    (Operation.outcomeEffect (luedersOperation e) : E) = e
```

## B. Lüders operations of projections

**`ProbabilisticTheory.NormedJordanAlgebra.effectSqrt_toEffect_of_projection`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L97).

> The CFC square root of a sharp Jordan event is the event itself.  This is the point where
> the general effect operation recovers projection compression.

```lean
lemma effectSqrt_toEffect_of_projection {p : E} (hp : IsJordanProjection p) :
    effectSqrt hp.toEffect = p
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersMap_toEffect_of_projection`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L103).

> Lüders filtering by a sharp event is exactly quadratic compression by that projection.

```lean
lemma luedersMap_toEffect_of_projection {p : E} (hp : IsJordanProjection p) :
    luedersMap hp.toEffect = quadRepPositiveLinearMap p
```

## C. Lüders conditioning

**`ProbabilisticTheory.NormedJordanAlgebra.luedersCondition`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L110).

> The normalized post-measurement state associated with an effect of nonzero probability.

```lean
noncomputable def luedersCondition (ω : 𝓢[ℝ, E]) (e : Effect E) (hmass : 0 < ω e) :
    𝓢[ℝ, E]
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersCondition_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L117).

> Formula for the normalized state after the Lüders operation.

```lean
lemma luedersCondition_apply (ω : 𝓢[ℝ, E]) (e : Effect E) (hmass : 0 < ω e) (x : E) :
    luedersCondition ω e hmass x = (ω e)⁻¹ * ω (U (effectSqrt e) x)
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersCondition_one`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L125).

> The normalized Lüders state evaluates the unit to one.

```lean
lemma luedersCondition_one (ω : 𝓢[ℝ, E]) (e : Effect E) (hmass : 0 < ω e) :
    luedersCondition ω e hmass 1 = 1
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersCondition_isNormal`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L132).

> In a JBW application, once the Lüders operation is known to preserve directed suprema,
> conditioning a normal state by a nonzero-probability effect remains normal.  Normality of the
> quadratic operation itself is the remaining intrinsic JBW quadratic-order theorem.

```lean
lemma luedersCondition_isNormal (ω : 𝓢[ℝ, E]) (e : Effect E) (hmass : 0 < ω e)
    (hOp : (luedersOperation e).IsNormal) (hω : ω.IsNormal) :
    (luedersCondition ω e hmass).IsNormal
```

**`ProbabilisticTheory.NormedJordanAlgebra.luedersCondition_toEffect_of_projection`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean#L139).

> For a projection, conditioning on the effect is conditioning on the projection.

```lean
lemma luedersCondition_toEffect_of_projection {p : E} (hp : IsJordanProjection p)
    (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p) :
    luedersCondition ω hp.toEffect hmass = hp.conditionOfQuadraticPositive ω hmass
```

## Depends on

- [Operations](../../channel/operation.md)
- [Conditioning a state on a projection](conditioning.md)
- [Continuous functional calculus in JB-algebras](../part-02/jb-generatedbyone-cfc.md)

## Proof depends on

- [Uniqueness of the positive square root](../part-02/jb-generatedbyone-sqrtuniqueness.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Lueders.lean)
