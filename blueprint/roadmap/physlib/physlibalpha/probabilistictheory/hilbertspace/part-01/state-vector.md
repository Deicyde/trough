---
declaration: module
origin: cited
lean: PositiveLinearMap.ofVec, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec_apply, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec_smul, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.norm_inner_lt_one_of_ofVec_ne
statement: formalized
proof: formalized
---

# Vector states

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.State.Vector`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean): 5 declarations, 5 with a docstring.

> A unit vector `ψ` defines the vector state `x ↦ ⟪ψ, x ψ⟫` on the bounded operators.

## i. Overview

> A unit vector `ψ` defines the vector state `x ↦ ⟪ψ, x ψ⟫` on the bounded operators.
> Multiplying `ψ` by a phase does not change its vector state, so two unit vectors with different
> vector states are not parallel: their overlap has norm `‖⟪ψ, φ⟫‖ < 1`.

## ii. Key results

> - `PositiveLinearMap.ofVec` : the positive functional of a vector.
> - `UnitalPositiveLinearMap.ofVec` : the vector state of a unit vector.
> - `UnitalPositiveLinearMap.ofVec_smul` : vector states do not see a global phase.
> - `UnitalPositiveLinearMap.norm_inner_lt_one_of_ofVec_ne` : unit vectors with different vector
>   states have overlap of norm less than one.

## iv. References

> * None.

## A. Vector states

**`PositiveLinearMap.ofVec`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean#L64).

> The vector functional associated with `ψ`.

```lean
def _root_.PositiveLinearMap.ofVec (ψ : H) : 𝓟[𝕜, H →L[𝕜] H]
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean#L72).

> The vector state associated with a unit vector.

```lean
def UnitalPositiveLinearMap.ofVec {ψ : H} (h : ‖ψ‖ = 1) : 𝓢[𝕜, H →L[𝕜] H]
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec_apply`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean#L77).

> Evaluation of a vector state is the corresponding quadratic form.

```lean
lemma UnitalPositiveLinearMap.ofVec_apply {ψ : H} (h : ‖ψ‖ = 1) (x : H →L[𝕜] H) :
    UnitalPositiveLinearMap.ofVec h x = ⟪ψ, x • ψ⟫_𝕜
```

## B. Phase invariance

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofVec_smul`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean#L87).

> Vector states do not see a global phase: `ofVec (c • ψ) = ofVec ψ` for `‖c‖ = 1`.

```lean
lemma UnitalPositiveLinearMap.ofVec_smul {ψ : H} (h : ‖ψ‖ = 1) {c : 𝕜} (hc : ‖c‖ = 1)
    (h' : ‖c • ψ‖ = 1) :
    UnitalPositiveLinearMap.ofVec (𝕜 := 𝕜) h' = UnitalPositiveLinearMap.ofVec (𝕜 := 𝕜) h
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.norm_inner_lt_one_of_ofVec_ne`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean#L97).

> Unit vectors with different vector states are not parallel: `‖⟪ψ, φ⟫‖ < 1`.

```lean
lemma UnitalPositiveLinearMap.norm_inner_lt_one_of_ofVec_ne {ψ φ : H} (hψ : ‖ψ‖ = 1)
    (hφ : ‖φ‖ = 1) (h : ofVec (𝕜 := 𝕜) hψ ≠ ofVec (𝕜 := 𝕜) hφ) : ‖⟪ψ, φ⟫_𝕜‖ < 1
```

## C. Example

## Depends on

- [Channels](../../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Vector.lean)
