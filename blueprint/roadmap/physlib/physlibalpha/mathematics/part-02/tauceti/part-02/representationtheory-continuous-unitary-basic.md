---
declaration: module
origin: cited
lean: ContRepresentation.IsUnitary, ContRepresentation.isUnitary_iff_norm_map, ContRepresentation.isUnitary_iff_isometry, ContRepresentation.IsUnitary.inner_map_map, ContRepresentation.IsUnitary.norm_map, ContRepresentation.IsUnitary.norm_le_one, ContRepresentation.IsUnitary.exists_norm_le, ContRepresentation.IsUnitary.isometry
statement: formalized
proof: formalized
---

# Unitary continuous representations

The module `PhyslibAlpha.Mathematics.TauCeti.RepresentationTheory.Continuous.Unitary.Basic`, [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean): 20 declarations, 20 with a docstring; 1 private, not shown.

> This file defines when a continuous representation preserves a real or complex inner product.

## i. Overview

> This file defines when a continuous representation preserves a real or complex inner product. It
> characterizes unitarity through norm preservation, isometries, and Mathlib's `unitary` submonoid of
> continuous linear operators, and records the basic inner-product identities, the coefficient bound,
> and that unitarity passes to restrictions.
>
> The operator characterizations reuse Mathlib's adjoint and unitary-operator theory.
>
> The mathematical development follows Daniel Bump, *Lie Groups*, second edition, Chapters 2–4.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`ContRepresentation.IsUnitary`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L65).

> A continuous representation is unitary when every action operator preserves the inner
> product.

```lean
def IsUnitary (π : ContRepresentation 𝕜 G V) : Prop
```

**`ContRepresentation.isUnitary_iff_norm_map`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L69).

> A representation is unitary exactly when every action map preserves norms.

```lean
lemma isUnitary_iff_norm_map (π : ContRepresentation 𝕜 G V) :
    IsUnitary π ↔ ∀ g v, ‖π g v‖ = ‖v‖
```

**`ContRepresentation.isUnitary_iff_isometry`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L78).

> A representation is unitary exactly when every action map is an isometry.

```lean
lemma isUnitary_iff_isometry (π : ContRepresentation 𝕜 G V) :
    IsUnitary π ↔ ∀ g, Isometry (π g)
```

**`ContRepresentation.IsUnitary.inner_map_map`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L89).

> A unitary representation preserves the inner product.

```lean
lemma inner_map_map (hπ : IsUnitary π) (g : G) (v w : V) :
    ⟪π g v, π g w⟫_𝕜 = ⟪v, w⟫_𝕜
```

**`ContRepresentation.IsUnitary.norm_map`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L95).

> Every action map of a unitary representation preserves norms.

```lean
lemma norm_map (hπ : IsUnitary π) (g : G) (v : V) :
    ‖π g v‖ = ‖v‖
```

**`ContRepresentation.IsUnitary.norm_le_one`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L100).

> Every action operator of a unitary representation has operator norm at most `1`.

```lean
lemma norm_le_one (hπ : IsUnitary π) (g : G) : ‖π g‖ ≤ 1
```

**`ContRepresentation.IsUnitary.exists_norm_le`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L105).

> The action operators of a unitary representation are uniformly bounded, in the form taken
> by the integrated-form API.

```lean
lemma exists_norm_le (hπ : IsUnitary π) : ∃ C, ∀ g, ‖π g‖ ≤ C
```

**`ContRepresentation.IsUnitary.isometry`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L109).

> Every action map of a unitary representation is an isometry.

```lean
lemma isometry (hπ : IsUnitary π) (g : G) : Isometry (π g)
```

**`ContRepresentation.IsUnitary.injective`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L113).

> Every action map of a unitary representation is injective.

```lean
lemma injective (hπ : IsUnitary π) (g : G) : Function.Injective (π g)
```

**`ContRepresentation.IsUnitary.restrict`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L117).

> Restriction along a monoid homomorphism preserves unitarity.

```lean
lemma restrict {H : Type*} [Monoid H] (hπ : IsUnitary π) (φ : H →* G) :
    IsUnitary (π.restrict φ)
```

**`ContRepresentation.IsUnitary.subrepresentation`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L122).

> The restriction of a unitary representation to an invariant submodule is unitary.

```lean
lemma subrepresentation (hπ : IsUnitary π) {W : Submodule 𝕜 V}
    (hW : ∀ g, ∀ v ∈ W, π g v ∈ W) : IsUnitary (subrepresentation π W hW)
```

**`ContRepresentation.IsUnitary.norm_inner_map_le`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L130).

> A matrix coefficient of a unitary representation is bounded by the product of the vector
> norms.

```lean
lemma norm_inner_map_le (hπ : IsUnitary π) (g : G) (v w : V) :
    ‖⟪π g v, w⟫_𝕜‖ ≤ ‖v‖ * ‖w‖
```

**`ContRepresentation.IsUnitary.adjoint_comp_self`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L141).

> The adjoint of a unitary action operator is a left inverse.

```lean
lemma adjoint_comp_self (hπ : IsUnitary π) (g : G) :
    (ContinuousLinearMap.adjoint (π g)).comp (π g) = 1
```

**`ContRepresentation.isUnitary_trivial`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L150).

> The trivial continuous representation is unitary.

```lean
lemma isUnitary_trivial :
    IsUnitary (ContRepresentation.trivial 𝕜 G V)
```

**`ContRepresentation.isUnitary_iff_mem_unitary`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L165).

> For a group representation, inner-product preservation is equivalent to every action operator
> belonging to Mathlib's unitary submonoid.

```lean
lemma isUnitary_iff_mem_unitary (π : ContRepresentation 𝕜 G V) :
    IsUnitary π ↔ ∀ g, π g ∈ unitary (V →L[𝕜] V)
```

**`ContRepresentation.IsUnitary.mem_unitary`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L179).

> Every action operator of a unitary group representation belongs to Mathlib's `unitary`
> submonoid.

```lean
lemma mem_unitary (hπ : IsUnitary π) (g : G) :
    π g ∈ unitary (V →L[𝕜] V)
```

**`ContRepresentation.IsUnitary.self_comp_adjoint`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L184).

> The adjoint of a unitary action operator is a right inverse.

```lean
lemma self_comp_adjoint (hπ : IsUnitary π) (g : G) :
    (π g).comp (ContinuousLinearMap.adjoint (π g)) = 1
```

**`ContRepresentation.IsUnitary.inner_map_left`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L193).

> Moving a unitary action from the first inner-product argument to the second replaces the group
> element by its inverse.

```lean
lemma inner_map_left (hπ : IsUnitary π) (g : G) (v w : V) :
    ⟪π g v, w⟫_𝕜 = ⟪v, π g⁻¹ w⟫_𝕜
```

**`ContRepresentation.IsUnitary.inner_map_right`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L200).

> Moving a unitary action from the second inner-product argument to the first replaces the group
> element by its inverse.

```lean
lemma inner_map_right (hπ : IsUnitary π) (g : G) (v w : V) :
    ⟪v, π g w⟫_𝕜 = ⟪π g⁻¹ v, w⟫_𝕜
```

**`ContRepresentation.IsUnitary.adjoint_eq_inv`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean#L206).

> The adjoint of a unitary action operator is the action of the inverse group element.

```lean
lemma adjoint_eq_inv (hπ : IsUnitary π) (g : G) :
    ContinuousLinearMap.adjoint (π g) = π g⁻¹
```

## Depends on

- [Restricting a continuous representation to an invariant submodule](representationtheory-continuous-subrepresentatio.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Unitary/Basic.lean)
