---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.GBit, PhyslibAlpha.ProbabilisticTheory.GBit.stateEquiv, PhyslibAlpha.ProbabilisticTheory.GBit.dualEquiv, PhyslibAlpha.ProbabilisticTheory.GBit.dualEquiv_symm_image_ball, PhyslibAlpha.ProbabilisticTheory.GBit.purePoint, PhyslibAlpha.ProbabilisticTheory.GBit.isPure_purePoint, PhyslibAlpha.ProbabilisticTheory.GBit.purePoint_injective, PhyslibAlpha.ProbabilisticTheory.GBit.finrank_eq_four
statement: formalized
proof: formalized
---

# The generalized bit

The module `PhyslibAlpha.ProbabilisticTheory.Examples.GBit`, [PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean): 9 declarations, 5 with a docstring.

> The generalized bit: the sup-norm cone over `ℝ³`, with an octahedral, non-simplex state space.

## i. Overview

> The generalized bit is the norm cone over `ℝ³` with the sup norm in place of the Euclidean norm
> of the qubit. Its states form an octahedron with `6` pure states, its vertices. That is finitely
> many, but too many for a simplex in a `4`-dimensional space. So the gbit is not classical, and
> not a qubit either: the shape of the cone matters, not just the dimension.

## ii. Key results

> - `GBit` : the generalized bit.
> - `GBit.stateEquiv` : the states are the octahedron.
> - `GBit.isPure_purePoint` : the vertices of the octahedron are pure states.
> - `GBit.not_isSimplex_stateSpace` : the state space is not a simplex.

## iv. References

> - J. Barrett, *Information processing in generalized probabilistic theories*, Phys. Rev. A 75,
>   032304 (2007).
> - P. Janotta and H. Lal, *Generalized probabilistic theories without the no-restriction
>   hypothesis*, Phys. Rev. A 87, 052131 (2013).

## A. The gbit as a norm cone

**`PhyslibAlpha.ProbabilisticTheory.GBit`**, an abbrev, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L57).

> The generalized bit: `ℝ × ℝ³` ordered by the sup-norm cone.

```lean
abbrev GBit : Type
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.stateEquiv`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L64).

> The states of the gbit are the octahedron `∑ i, |a i| ≤ 1`.

```lean
noncomputable def stateEquiv : 𝓢[ℝ, GBit] ≃ {a : Fin 3 → ℝ // ∑ i, |a i| ≤ 1}
```

## B. Too many pure states

**`PhyslibAlpha.ProbabilisticTheory.GBit.dualEquiv`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L73).

> A functional on `Fin 3 → ℝ` is its vector of values on the standard basis.

```lean
noncomputable abbrev dualEquiv : ((Fin 3 → ℝ) →L[ℝ] ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ)
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.dualEquiv_symm_image_ball`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L76).

```lean
lemma dualEquiv_symm_image_ball :
    dualEquiv.symm '' {a : Fin 3 → ℝ | ∑ i, |a i| ≤ 1} = {f | ‖f‖ ≤ 1}
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.purePoint`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L82).

> The pure state whose functional is `±1` times a coordinate.

```lean
noncomputable def purePoint (j : Fin 3 × Bool) : 𝓢[ℝ, GBit]
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.isPure_purePoint`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L89).

```lean
lemma isPure_purePoint (j : Fin 3 × Bool) : (purePoint j).IsPure
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.purePoint_injective`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L93).

```lean
lemma purePoint_injective : Function.Injective purePoint
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.finrank_eq_four`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L96).

```lean
lemma finrank_eq_four : Module.finrank ℝ GBit = 4
```

**`PhyslibAlpha.ProbabilisticTheory.GBit.not_isSimplex_stateSpace`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean#L102).

> **The gbit is not classical**: it has `6` pure states in a `4`-dimensional space, too many
> for a simplex.

```lean
lemma not_isSimplex_stateSpace :
    ¬ IsSimplex (UnitalPositiveLinearMap.algebraicStateSpace (E := GBit))
```

## Depends on

- [Extreme points of `ℓq` balls](../../mathematics/part-01/convex/lpball.md)
- [Simplices](../../mathematics/part-02/geometry/simplex.md)
- [Order-unit spaces built from a normed vector space](normcone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Examples/GBit.lean)
