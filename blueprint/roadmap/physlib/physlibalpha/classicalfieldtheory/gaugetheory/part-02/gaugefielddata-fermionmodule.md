---
declaration: module
origin: cited
lean: GaugeFieldData.FermionModule, GaugeFieldData.projFermionValue, GaugeFieldData.inclFermionValue, GaugeFieldData.sum_inclFermionValue_proj, GaugeFieldData.finrank_fermionModule
statement: formalized
proof: formalized
---

# The fermionic module of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.FermionModule`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean): 5 declarations, 5 with a docstring.

> The value space of all the fermionic species of a gauge theory at once.

## i. Overview

> A `GaugeFieldData G` records its fermions species by species, each with its own value
> space `(T.fermion i).V`. This file assembles those into a single complex vector space, the
> fermionic module
>
> `T.FermionModule = ∀ i, (T.fermion i).V`,
>
> in which one value of the whole fermionic content of the theory lives at once. For the
> Standard Model this is the space that a physicist writes as the column of all the fermion
> fields.
>
> It is the *value* space, not a space of component functions, and so it is not the
> `GaugeFieldData.FermionGenerators` of the sibling file. The latter is a direct sum of component
> spaces `FieldDerivSpace`, one per species, and is infinite-dimensional because it
> carries a derivative label of every order. The fermionic module is finite-dimensional,
> with dimension the sum of the dimensions of the species, and it is the space on which
> `GaugeFieldData.fermionMatterField` puts the Lorentz, gauge and mass-weight structure of a
> single matter field.
>
> The species type is finite, so the product is also a direct sum. A fermionic
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

**`GaugeFieldData.FermionModule`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L80).

> The fermionic module of a gauge theory, the product over the fermionic species of their
> value spaces. One element of it is a value of the entire fermionic content of the theory, the
> column of all the fermion fields. This is as opposed to
> `GaugeFieldData.FermionGenerators`, which is a space of component *functions* and is
> infinite-dimensional. Since the species type is finite the product is also their direct
> sum.

```lean
abbrev FermionModule : Type
```

### A.1. The species projections and inclusions

**`GaugeFieldData.projFermionValue`**, an abbrev, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L89).

> The component of a fermionic configuration in one species.

```lean
abbrev projFermionValue (i : T.FermionSpecies) :
    T.FermionModule →ₗ[ℂ] T.FermionValue i
```

**`GaugeFieldData.inclFermionValue`**, an abbrev, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L95).

> The inclusion of one fermionic species into the fermionic module, extending a value
> of that species by zero in every other.

```lean
abbrev inclFermionValue (i : T.FermionSpecies) :
    T.FermionValue i →ₗ[ℂ] T.FermionModule
```

**`GaugeFieldData.sum_inclFermionValue_proj`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L104).

> A fermionic configuration is the sum of its species components. The product over
> the species is their direct sum, the species type being finite, so nothing is lost in
> describing the fermionic content of the theory by one module.

```lean
lemma sum_inclFermionValue_proj (v : T.FermionModule) :
    ∑ i, T.inclFermionValue i (v i) = v
```

### A.2. The dimension of the fermionic module

**`GaugeFieldData.finrank_fermionModule`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean#L119).

> The dimension of the fermionic module is the sum of the dimensions of the
> species, each species contributing the number of complex components of its
> multiplet.

```lean
lemma finrank_fermionModule :
    Module.finrank ℂ T.FermionModule = ∑ i, Module.finrank ℂ (T.FermionValue i)
```

## Depends on

- [The field data of a gauge theory](../part-01/gaugefielddata-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionModule.lean)
