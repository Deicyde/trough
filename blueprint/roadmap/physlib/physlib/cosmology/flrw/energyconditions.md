---
declaration: module
origin: cited
lean: Cosmology.CosmicFluid.NullEnergyCondition, Cosmology.CosmicFluid.WeakEnergyCondition, Cosmology.CosmicFluid.StrongEnergyCondition, Cosmology.CosmicFluid.DominantEnergyCondition, Cosmology.CosmicFluid.DominantEnergyCondition.weakEnergyCondition, Cosmology.CosmicFluid.WeakEnergyCondition.nullEnergyCondition, Cosmology.CosmicFluid.StrongEnergyCondition.nullEnergyCondition
statement: formalized
proof: formalized
---

# Energy conditions of the cosmic fluid

The module `Physlib.Cosmology.FLRW.EnergyConditions`, [Physlib/Cosmology/FLRW/EnergyConditions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean): 7 declarations, 7 with a docstring.

## i. Overview

> The null, weak, strong and dominant energy conditions of a cosmic fluid `F : CosmicFluid`
> (`Physlib.Cosmology.FLRW.Basic`), described by its total energy density `F.ρ` and its pressure
> `F.p`, at one time `t`, `c : SpeedOfLight` being the speed of light, and the implications between
> them. They are used in `Physlib.Cosmology.FLRW.FriedmannSolution` to state the acceleration
> criterion.

## ii. Key results

> - `CosmicFluid.NullEnergyCondition`, `CosmicFluid.WeakEnergyCondition`,
>   `CosmicFluid.StrongEnergyCondition`, `CosmicFluid.DominantEnergyCondition`: the four energy
>   conditions.
> - `CosmicFluid.DominantEnergyCondition.weakEnergyCondition`,
>   `CosmicFluid.WeakEnergyCondition.nullEnergyCondition`,
>   `CosmicFluid.StrongEnergyCondition.nullEnergyCondition`: the implications between them.

## iv. References

> * None.

## A. The energy conditions

**`Cosmology.CosmicFluid.NullEnergyCondition`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L57).

> The null energy condition at time `t`, `0 ≤ ρ + p / c²`, for the total energy density `ρ`
> and the pressure `p` of the cosmic fluid, `c` being the speed of light.

```lean
def NullEnergyCondition : Prop
```

**`Cosmology.CosmicFluid.WeakEnergyCondition`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L61).

> The weak energy condition at time `t`, `0 ≤ ρ ∧ 0 ≤ ρ + p / c²`, for the total energy density
> `ρ` and the pressure `p` of the cosmic fluid, `c` being the speed of light.

```lean
def WeakEnergyCondition : Prop
```

**`Cosmology.CosmicFluid.StrongEnergyCondition`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L65).

> The strong energy condition at time `t`, `0 ≤ ρ + p / c² ∧ 0 ≤ ρ + 3 p / c²`, for the total
> energy density `ρ` and the pressure `p` of the cosmic fluid, `c` being the speed of light.

```lean
def StrongEnergyCondition : Prop
```

**`Cosmology.CosmicFluid.DominantEnergyCondition`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L70).

> The dominant energy condition at time `t`, `0 ≤ ρ ∧ |p| ≤ ρ c²`, for the total energy density
> `ρ` and the pressure `p` of the cosmic fluid, `c` being the speed of light.

```lean
def DominantEnergyCondition : Prop
```

## B. Implications between the energy conditions

**`Cosmology.CosmicFluid.DominantEnergyCondition.weakEnergyCondition`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L81).

> The dominant energy condition implies the weak energy condition.

```lean
lemma DominantEnergyCondition.weakEnergyCondition (h : F.DominantEnergyCondition c t) :
    F.WeakEnergyCondition c t
```

**`Cosmology.CosmicFluid.WeakEnergyCondition.nullEnergyCondition`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L94).

> The weak energy condition implies the null energy condition.

```lean
lemma WeakEnergyCondition.nullEnergyCondition (h : F.WeakEnergyCondition c t) :
    F.NullEnergyCondition c t
```

**`Cosmology.CosmicFluid.StrongEnergyCondition.nullEnergyCondition`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean#L99).

> The strong energy condition implies the null energy condition.

```lean
lemma StrongEnergyCondition.nullEnergyCondition (h : F.StrongEnergyCondition c t) :
    F.NullEnergyCondition c t
```

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Sources

- [Physlib/Cosmology/FLRW/EnergyConditions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/EnergyConditions.lean)
