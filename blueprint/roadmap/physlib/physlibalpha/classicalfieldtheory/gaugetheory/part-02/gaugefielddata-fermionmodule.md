---
declaration: module
origin: cited
lean: GaugeFieldData.FermionModule, GaugeFieldData.projFermionValue, GaugeFieldData.inclFermionValue, GaugeFieldData.projFermionValue_apply, GaugeFieldData.projFermionValue_inclFermionValue_self, GaugeFieldData.projFermionValue_inclFermionValue_of_ne, GaugeFieldData.sum_inclFermionValue_proj, GaugeFieldData.fermionModule_hom_ext
statement: formalized
proof: formalized
---

# The fermionic module of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.FermionModule`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean): 9 declarations, 7 with a docstring.

## i. Overview

> A `GaugeFieldData jets` records its fermions species by species, each with its own value
> space `(T.fermion i).V`. This file assembles those into a single complex vector space, the
> **fermionic module**
>
> `T.FermionModule = ∀ i, (T.fermion i).V`,
>
> in which one value of the whole fermionic content of the theory lives at once. For the
> Standard Model this is the sixteen-complex-dimensional space (fifteen Weyl components in
> each of three generations, with the doublets counted with their gauge multiplicity) that a
> physicist writes as the column of all the fermion fields.
>
> It is the *value* space, not a space of component functions, and so it is not the
> `FermionGenerators` of `GaugeFieldData.Basic`: the latter is a direct sum of component
> spaces `JetComponentSpace`, one per species, and is infinite-dimensional because it
> carries a derivative label of every order. The fermionic module is finite-dimensional,
> with dimension the sum of the dimensions of the species, and it is the space on which
> `GaugeFieldData.fermionMatterField` puts the Lorentz, gauge and mass-weight structure of a
> single matter field.
>
> The species type is finite, so the product is also a direct sum: a fermionic
> configuration is the sum of its species components, `sum_inclFermionValue_proj` below, and
> the two descriptions of the module agree.

## ii. Key results

> - `GaugeFieldData.FermionModule` : the value space of all the fermions of the theory.
> - `GaugeFieldData.projFermionValue`, `GaugeFieldData.inclFermionValue` : the projection
>   onto and the inclusion of one species.
> - `GaugeFieldData.sum_inclFermionValue_proj` : a configuration is the sum of its species
>   components.
> - `GaugeFieldData.finrank_fermionModule` : its dimension is the sum of the dimensions of
>   the species.

## iv. References

> * None.

## A. The fermionic module

**`GaugeFieldData.FermionModule`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L81).

> **The fermionic module of a gauge theory**: the product, over the fermionic species,
> of their value spaces. One element of it is a value of the entire fermionic content of
> the theory — the column of all the fermion fields — as opposed to
> `GaugeFieldData.FermionGenerators`, which is a space of component *functions* and is
> infinite-dimensional. Since the species type is finite the product is also their direct
> sum.

```lean
abbrev FermionModule : Type
```

### A.1. The species projections and inclusions

**`GaugeFieldData.projFermionValue`**, an abbrev, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L90).

> The component of a fermionic configuration in one species.

```lean
abbrev projFermionValue (i : T.FermionSpecies) :
    T.FermionModule →ₗ[ℂ] T.FermionValue i
```

**`GaugeFieldData.inclFermionValue`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L96).

> The inclusion of one fermionic species into the fermionic module, extending a value
> of that species by zero in every other.

```lean
abbrev inclFermionValue (i : T.FermionSpecies) :
    T.FermionValue i →ₗ[ℂ] T.FermionModule
```

**`GaugeFieldData.projFermionValue_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L103).

```lean
lemma projFermionValue_apply (i : T.FermionSpecies) (v : T.FermionModule) :
    T.projFermionValue i v = v i
```

**`GaugeFieldData.projFermionValue_inclFermionValue_self`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L106).

```lean
lemma projFermionValue_inclFermionValue_self (i : T.FermionSpecies)
    (v : T.FermionValue i) : T.projFermionValue i (T.inclFermionValue i v) = v
```

**`GaugeFieldData.projFermionValue_inclFermionValue_of_ne`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L112).

> A value of one species has no component in any other species: the inclusions of
> distinct species have disjoint supports.

```lean
lemma projFermionValue_inclFermionValue_of_ne {i j : T.FermionSpecies} (h : i ≠ j)
    (v : T.FermionValue j) : T.projFermionValue i (T.inclFermionValue j v) = 0
```

**`GaugeFieldData.sum_inclFermionValue_proj`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L119).

> **A fermionic configuration is the sum of its species components**. The product over
> the species is their direct sum, the species type being finite, so nothing is lost in
> describing the fermionic content of the theory by one module.

```lean
lemma sum_inclFermionValue_proj (v : T.FermionModule) :
    ∑ i, T.inclFermionValue i (v i) = v
```

**`GaugeFieldData.fermionModule_hom_ext`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L124).

> Two linear maps out of the fermionic module agreeing on every species are equal.

```lean
lemma fermionModule_hom_ext {N : Type} [AddCommGroup N] [Module ℂ N]
    {F F' : T.FermionModule →ₗ[ℂ] N}
    (h : ∀ i, F.comp (T.inclFermionValue i) = F'.comp (T.inclFermionValue i)) : F = F'
```

### A.2. The dimension of the fermionic module

**`GaugeFieldData.finrank_fermionModule`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L140).

> **The dimension of the fermionic module is the sum of the dimensions of the
> species**, each species contributing the number of complex components of its
> multiplet.

```lean
lemma finrank_fermionModule :
    Module.finrank ℂ T.FermionModule = ∑ i, Module.finrank ℂ (T.FermionValue i)
```

## Depends on

- [The field data of a gauge theory](gaugefielddata-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean)
