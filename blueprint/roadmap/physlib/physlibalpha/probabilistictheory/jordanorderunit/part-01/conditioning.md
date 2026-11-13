---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_apply, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_one, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_nonneg, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_self, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_apply_of_jordanOrthogonal, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_complement, ProbabilisticTheory.JordanAlgebra.IsJordanProjection.conditionOfQuadraticPositive
statement: formalized
proof: formalized
---

# Conditioning a state on a projection

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Conditioning`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean): 9 declarations, 5 with a docstring.

> Conditioning a state on a Jordan projection `p`: the state `x ↦ ω(U_p x) / ω(p)`.

## i. Overview

> For a Jordan projection `p` with positive quadratic representation `U_p`, and a state `ω` with `ω(p)
> ≠ 0`, the functional `x ↦ ω(U\_p x) / ω(p)` is a state: `ω` conditioned on the outcome `p`.

## ii. Key results

> - `JordanAlgebra.IsJordanProjection.condition` : the conditioned state.
> - `JordanAlgebra.IsJordanProjection.condition_self` : the conditioned state assigns probability `1`
>   to `p`.
> - `JordanAlgebra.IsJordanProjection.condition_complement` : the conditioned state assigns
>   probability `0` to the complement `1 - p`.
> - `JordanAlgebra.IsJordanProjection.conditionOfQuadraticPositive` : conditioning when all
>   quadratic representations are positive.

## iv. References

> * None.

## A. Quadratic conditioning

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L57).

> Condition a state on a Jordan projection.  Positivity of the quadratic representation is
> kept explicit, since it does not follow from the weak `IsJordanOrderUnit` interface.

```lean
noncomputable def IsJordanProjection.condition {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L71).

```lean
lemma IsJordanProjection.condition_apply {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) (x : E) :
    hp.condition ω hmass hU x = (ω p)⁻¹ * ω (U p x)
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_one`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L77).

```lean
lemma IsJordanProjection.condition_one {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) :
    hp.condition ω hmass hU 1 = 1
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_nonneg`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L84).

```lean
lemma IsJordanProjection.condition_nonneg {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) {x : E} (hx : 0 ≤ x) :
    0 ≤ hp.condition ω hmass hU x
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_self`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L91).

> Conditioning on `p` makes `p` certain.

```lean
lemma IsJordanProjection.condition_self {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) :
    hp.condition ω hmass hU p = 1
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_apply_of_jordanOrthogonal`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L99).

> Conditioning on `p` assigns probability zero to every projection Jordan-orthogonal to `p`.

```lean
lemma IsJordanProjection.condition_apply_of_jordanOrthogonal {p q : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) (horth : p * q = 0) :
    hp.condition ω hmass hU q = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.condition_complement`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L106).

> Conditioning on a projection assigns probability zero to its algebraic complement.

```lean
lemma IsJordanProjection.condition_complement {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    (hU : ∀ x, 0 ≤ x → 0 ≤ U p x) :
    hp.condition ω hmass hU (1 - p) = 0
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.conditionOfQuadraticPositive`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L115).

> Condition a state on a Jordan projection using the ambient quadratic-order capability.
> This is the physics-facing form of `condition`: its only non-algebraic input is exactly the
> positivity of quadratic representations, bundled by `IsQuadraticallyPositive`.

```lean
noncomputable def IsJordanProjection.conditionOfQuadraticPositive {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    [IsQuadraticallyPositive E] : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.JordanAlgebra.IsJordanProjection.conditionOfQuadraticPositive_apply`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean#L121).

```lean
lemma IsJordanProjection.conditionOfQuadraticPositive_apply {p : E}
    (hp : IsJordanProjection p) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω p)
    [IsQuadraticallyPositive E] (x : E) :
    hp.conditionOfQuadraticPositive ω hmass x = (ω p)⁻¹ * ω (U p x)
```

## Depends on

- [Moments, variance and Jordan projections](observable.md)
- [Positive quadratic representations](../part-02/quadratic-order.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Conditioning.lean)
