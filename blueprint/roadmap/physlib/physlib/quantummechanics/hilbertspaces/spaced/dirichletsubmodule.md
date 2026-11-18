---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSchwartzMap, QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn, QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn.mem_iff, QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn.le_schwartzSubmoduleOn
statement: formalized
proof: formalized
---

# Dirichlet submodule

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.DirichletSubmodule`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean): 4 declarations, 2 with a docstring.

## i. Overview

> In this module we define the Dirichlet submodule of `SpaceDHilbertSpaceOn Ω μ` consisting of
> equivalence classes of Schwartz maps which vanish on `frontier Ω`. The frontier (or boundary)
> of a set `Ω` contains all points whose neighborhoods always intersect with both `Ω` and `Ωᶜ`.
>
> These serve as a convenient dense domain for operators acting on wavefunctions satisfying
> homogeneous Dirichlet boundary conditions on `Ω`.

## ii. Key results

> - `DirichletSubmoduleOn Ω μ`: The subspace of `SchwartzSubmodule d μ` consisting of Schwartz maps
>   which vanish on the frontier of `Ω`.

## iv. References

> * None.

## A. Definitions

**`QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSchwartzMap`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean#L54).

> The Schwartz maps which vanish on `frontier Ω`.

```lean
def DirichletSchwartzMap : Submodule ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean#L62).

> The submodule of the Hilbert space on `Ω` consisting of the equivalence classes
> of Schwartz maps which vanish on `frontier Ω`.

```lean
abbrev DirichletSubmoduleOn : Submodule ℂ (SpaceDHilbertSpaceOn Ω μ)
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn.mem_iff`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean#L68).

```lean
lemma mem_iff {ψ : SpaceDHilbertSpaceOn Ω μ} :
    ψ ∈ DirichletSubmoduleOn Ω μ ↔
      ∃ f : DirichletSchwartzMap Ω, subspaceProjection Ω μ (schwartzIncl μ f) = ψ
```

## B. Contained in SchwartzSubmoduleOn

**`QuantumMechanics.SpaceDHilbertSpaceOn.DirichletSubmoduleOn.le_schwartzSubmoduleOn`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean#L77).

```lean
lemma le_schwartzSubmoduleOn : DirichletSubmoduleOn Ω μ ≤ SchwartzSubmoduleOn Ω μ
```

## C. Density

## Depends on

- [Schwartz submodule](schwartzsubmodule.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/DirichletSubmodule.lean)
