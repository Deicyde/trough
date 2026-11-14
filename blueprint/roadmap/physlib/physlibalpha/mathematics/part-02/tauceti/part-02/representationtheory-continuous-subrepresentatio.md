---
declaration: module
origin: cited
lean: ContRepresentation.subrepresentation, ContRepresentation.coe_subrepresentation_apply, ContRepresentation.subrepresentationInclusion, ContRepresentation.subrepresentationInclusion_apply, ContRepresentation.mem_invariants_subrepresentation, ContRepresentation.toRepresentation_subrepresentation, Subrepresentation.toRepresentation_subrepresentation_toSubmodule, ContRepresentation.quotient
statement: formalized
proof: formalized
---

# Restricting a continuous representation to an invariant submodule

The module `PhyslibAlpha.Mathematics.TauCeti.RepresentationTheory.Continuous.Subrepresentation`, [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean): 11 declarations, 11 with a docstring.

> This file restricts a continuous representation of a monoid to a submodule preserved by every action
> operator, the continuous counterpart of Mathlib's `Representation.subrepresentation`, and descends
> it to the quotient by such a submodule, the continuous counterpart of `Representation.quotient`.

## i. Overview

> This file restricts a continuous representation of a monoid to a submodule preserved by every
> action operator, the continuous counterpart of Mathlib's `Representation.subrepresentation`, and
> descends it to the quotient by such a submodule, the continuous counterpart of
> `Representation.quotient`.

## ii. Key results

> * `ContRepresentation.subrepresentation`: the restriction of a continuous representation to
>   an invariant submodule.
> * `ContRepresentation.subrepresentationInclusion`: the continuous intertwiner including a
>   subrepresentation into its ambient representation.
> * `ContRepresentation.quotient`: a continuous representation descended to the quotient by an
>   invariant submodule, the continuous counterpart of `Representation.quotient`.
>
> * `ContRepresentation.mem_invariants_subrepresentation`: a vector of the submodule is
>   invariant for the restricted representation exactly when it is invariant for the ambient one.
> * `ContRepresentation.toRepresentation_subrepresentation`: the underlying representation of
>   a restricted continuous representation is the restriction of the underlying representation.
> * `Subrepresentation.toRepresentation_subrepresentation_toSubmodule`: restricting to the
>   submodule a subrepresentation carries has that subrepresentation's own representation underneath.
> * `ContRepresentation.toRepresentation_quotient`: the underlying representation of a descended
>   continuous representation is the descended underlying representation.
> * `ContRepresentation.continuous_subrepresentation`: the restriction of a continuous
>   representation to an invariant submodule is again continuous.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`ContRepresentation.subrepresentation`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L68).

> The restriction of a continuous representation to an invariant submodule. This is the
> continuous counterpart of `Representation.subrepresentation`.

```lean
def subrepresentation (π : ContRepresentation R G V) (W : Submodule R V)
    (hW : ∀ g, ∀ v ∈ W, π g v ∈ W) : ContRepresentation R G W
```

**`ContRepresentation.coe_subrepresentation_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L79).

> The restricted action is the ambient action, read on the underlying vectors.

```lean
lemma coe_subrepresentation_apply (g : G) (v : W) :
    ((subrepresentation π W hW g v : W) : V) = π g (v : V)
```

**`ContRepresentation.subrepresentationInclusion`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L85).

> The inclusion of a subrepresentation into its ambient continuous representation, packaged as a
> continuous intertwiner.

```lean
noncomputable def subrepresentationInclusion
    (π : ContRepresentation R G V) (σ : Subrepresentation π.toRepresentation) :
    ContIntertwiningMap
      (subrepresentation π σ.toSubmodule
        (fun g _ hv ↦ σ.apply_mem_toSubmodule g hv)) π
```

**`ContRepresentation.subrepresentationInclusion_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L97).

> The subrepresentation inclusion sends a vector to the same vector in the ambient space.

```lean
lemma subrepresentationInclusion_apply (π : ContRepresentation R G V)
    (σ : Subrepresentation π.toRepresentation) (v : σ.toSubmodule) :
    π.subrepresentationInclusion σ v = (v : V)
```

**`ContRepresentation.mem_invariants_subrepresentation`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L109).

> A vector of an invariant submodule is invariant for the restricted representation exactly when
> it is invariant for the ambient one: the restricted action is the ambient action.

```lean
lemma mem_invariants_subrepresentation {x : W} :
    x ∈ (subrepresentation π W hW).invariants ↔ (x : V) ∈ π.invariants
```

**`ContRepresentation.toRepresentation_subrepresentation`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L116).

> The underlying representation of a restricted continuous representation is the restriction of
> the underlying representation.

```lean
lemma toRepresentation_subrepresentation :
    (subrepresentation π W hW).toRepresentation
      = π.toRepresentation.subrepresentation W fun g _ hv => hW g _ hv
```

**`Subrepresentation.toRepresentation_subrepresentation_toSubmodule`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L128).

> Restricting `π` to the submodule a subrepresentation `σ` of `π.toRepresentation` carries has
> `σ.toRepresentation` as its underlying representation: both restrict the ambient action to the
> same submodule.

```lean
lemma _root_.Subrepresentation.toRepresentation_subrepresentation_toSubmodule
    (σ : Subrepresentation π.toRepresentation) :
    (subrepresentation π σ.toSubmodule
      (fun g _ hv ↦ σ.apply_mem_toSubmodule g hv)).toRepresentation = σ.toRepresentation
```

**`ContRepresentation.quotient`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L143).

> A continuous representation descended to the quotient by an invariant submodule, which
> carries the quotient topology. This is the continuous counterpart of `Representation.quotient`.

```lean
def quotient (π : ContRepresentation R G V) (W : Submodule R V)
    (hW : ∀ g, ∀ v ∈ W, π g v ∈ W) : ContRepresentation R G (V ⧸ W)
```

**`ContRepresentation.quotient_apply_mk`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L160).

> The descended action on the class of `v` is the class of the ambient action on `v`.

```lean
lemma quotient_apply_mk (g : G) (v : V) :
    quotient π W hW g (Submodule.Quotient.mk v) = Submodule.Quotient.mk (π g v)
```

**`ContRepresentation.toRepresentation_quotient`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L167).

> The underlying representation of a descended continuous representation is the descended
> underlying representation.

```lean
lemma toRepresentation_quotient :
    (quotient π W hW).toRepresentation
      = π.toRepresentation.quotient W fun g _ hv => hW g _ hv
```

**`ContRepresentation.continuous_subrepresentation`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean#L186).

> Restricting a continuous representation to an invariant submodule preserves continuity: from
> continuity of `g ↦ π g` as a map into the continuous linear endomorphisms of `V`, the restricted
> action `g ↦ subrepresentation π W hW g` is continuous into those of `W`. This supplies the
> continuity argument that `matrixCoeff` and the rest of the continuous-representation API take
> explicitly, so a subrepresentation can be used wherever a continuous representation is expected.

```lean
lemma continuous_subrepresentation (hπ : Continuous π) :
    Continuous (subrepresentation π W hW)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Subrepresentation.lean)
