---
declaration: module
origin: cited
lean: GaugeFieldData.BosonModule, GaugeFieldData.projBosonValue, GaugeFieldData.inclBosonValue, GaugeFieldData.projBosonValue_apply, GaugeFieldData.projBosonValue_inclBosonValue_self, GaugeFieldData.projBosonValue_inclBosonValue_of_ne, GaugeFieldData.sum_inclBosonValue_proj, GaugeFieldData.bosonModule_hom_ext
statement: formalized
proof: formalized
---

# The bosonic module of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.BosonModule`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean): 9 declarations, 7 with a docstring.

## i. Overview

> A `GaugeFieldData jets` records its bosons species by species, each with its own value
> space `(T.boson i).V`. This file assembles those into a single complex vector space, the
> **bosonic module**
>
> `T.BosonModule = ∀ i, (T.boson i).V`,
>
> in which one value of the whole bosonic content of the theory lives at once. For the
> Standard Model, whose only bosonic species is the Higgs doublet, this is that doublet
> again; a theory with a larger scalar sector — a second Higgs doublet, a singlet — has the
> column of all of them.
>
> It is the *value* space, not a space of component functions, and so it is not the
> `BosonGenerators` of `GaugeFieldData.Basic`: the latter is a direct sum of component
> spaces `JetComponentSpace`, one per species, and is infinite-dimensional because it
> carries a derivative label of every order. The bosonic module is finite-dimensional,
> with dimension the sum of the dimensions of the species, and it is the space on which
> `GaugeFieldData.bosonMatterField` puts the Lorentz, gauge and mass-weight structure of a
> single matter field.
>
> The species type is finite, so the product is also a direct sum: a bosonic
> configuration is the sum of its species components, `sum_inclBosonValue_proj` below, and
> the two descriptions of the module agree.

## ii. Key results

> - `GaugeFieldData.BosonModule` : the value space of all the bosons of the theory.
> - `GaugeFieldData.projBosonValue`, `GaugeFieldData.inclBosonValue` : the projection
>   onto and the inclusion of one species.
> - `GaugeFieldData.sum_inclBosonValue_proj` : a configuration is the sum of its species
>   components.
> - `GaugeFieldData.finrank_bosonModule` : its dimension is the sum of the dimensions of
>   the species.

## iv. References

> * None.

## A. The bosonic module

**`GaugeFieldData.BosonModule`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L81).

> **The bosonic module of a gauge theory**: the product, over the bosonic species,
> of their value spaces. One element of it is a value of the entire bosonic content of
> the theory — the column of all the boson fields — as opposed to
> `GaugeFieldData.BosonGenerators`, which is a space of component *functions* and is
> infinite-dimensional. Since the species type is finite the product is also their direct
> sum.

```lean
abbrev BosonModule : Type
```

### A.1. The species projections and inclusions

**`GaugeFieldData.projBosonValue`**, an abbrev, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L90).

> The component of a bosonic configuration in one species.

```lean
abbrev projBosonValue (i : T.BosonSpecies) :
    T.BosonModule →ₗ[ℂ] T.BosonValue i
```

**`GaugeFieldData.inclBosonValue`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L96).

> The inclusion of one bosonic species into the bosonic module, extending a value
> of that species by zero in every other.

```lean
abbrev inclBosonValue (i : T.BosonSpecies) :
    T.BosonValue i →ₗ[ℂ] T.BosonModule
```

**`GaugeFieldData.projBosonValue_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L103).

```lean
lemma projBosonValue_apply (i : T.BosonSpecies) (v : T.BosonModule) :
    T.projBosonValue i v = v i
```

**`GaugeFieldData.projBosonValue_inclBosonValue_self`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L106).

```lean
lemma projBosonValue_inclBosonValue_self (i : T.BosonSpecies)
    (v : T.BosonValue i) : T.projBosonValue i (T.inclBosonValue i v) = v
```

**`GaugeFieldData.projBosonValue_inclBosonValue_of_ne`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L112).

> A value of one species has no component in any other species: the inclusions of
> distinct species have disjoint supports.

```lean
lemma projBosonValue_inclBosonValue_of_ne {i j : T.BosonSpecies} (h : i ≠ j)
    (v : T.BosonValue j) : T.projBosonValue i (T.inclBosonValue j v) = 0
```

**`GaugeFieldData.sum_inclBosonValue_proj`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L119).

> **A bosonic configuration is the sum of its species components**. The product over
> the species is their direct sum, the species type being finite, so nothing is lost in
> describing the bosonic content of the theory by one module.

```lean
lemma sum_inclBosonValue_proj (v : T.BosonModule) :
    ∑ i, T.inclBosonValue i (v i) = v
```

**`GaugeFieldData.bosonModule_hom_ext`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L124).

> Two linear maps out of the bosonic module agreeing on every species are equal.

```lean
lemma bosonModule_hom_ext {N : Type} [AddCommGroup N] [Module ℂ N]
    {F F' : T.BosonModule →ₗ[ℂ] N}
    (h : ∀ i, F.comp (T.inclBosonValue i) = F'.comp (T.inclBosonValue i)) : F = F'
```

### A.2. The dimension of the bosonic module

**`GaugeFieldData.finrank_bosonModule`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean#L140).

> **The dimension of the bosonic module is the sum of the dimensions of the
> species**, each species contributing the number of complex components of its
> multiplet.

```lean
lemma finrank_bosonModule :
    Module.finrank ℂ T.BosonModule = ∑ i, Module.finrank ℂ (T.BosonValue i)
```

## Depends on

- [The field data of a gauge theory](gaugefielddata-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonModule.lean)
