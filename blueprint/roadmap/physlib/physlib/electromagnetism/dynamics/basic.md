---
declaration: module
origin: cited
lean: Electromagnetism.FreeSpace, Electromagnetism.FreeSpace.ε₀_nonneg, Electromagnetism.FreeSpace.μ₀_nonneg, Electromagnetism.FreeSpace.ε₀_ne_zero, Electromagnetism.FreeSpace.μ₀_ne_zero, Electromagnetism.FreeSpace.c, Electromagnetism.FreeSpace.c_val, Electromagnetism.FreeSpace.c_sq
statement: formalized
proof: formalized
---

# Free space

The module `Physlib.Electromagnetism.Dynamics.Basic`, [Physlib/Electromagnetism/Dynamics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean): 9 declarations, 2 with a docstring.

## i. Overview

> In this module we define a type `FreeSpace` which encapsulates the
> electric permittivity and magnetic permeability of free space, that is
> the physical constants which make it up.
>
> We prove basic properties from this definition, and define the speed of light
> in free space in terms of these constants.

## ii. Key results

> - `FreeSpace` : The structure encapsulating the electric permittivity
>   and magnetic permeability of free space.
> - `FreeSpace.c` : The speed of light in free space.

## iv. References

> * None.

## A. The definition of the free space type

**`Electromagnetism.FreeSpace`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L51).

> Free space consists of the specification of the
> electric permittivity and the magnetic permeability.

```lean
structure FreeSpace where
  /-- The permittivity. -/
  ε₀ : ℝ
  /-- The permeability. -/
  μ₀ : ℝ
  ε₀_pos : 0 < ε₀
  μ₀_pos : 0 < μ₀
```

## B. Positivity properties

**`Electromagnetism.FreeSpace.ε₀_nonneg`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L70).

```lean
lemma ε₀_nonneg : 0 ≤ 𝓕.ε₀
```

**`Electromagnetism.FreeSpace.μ₀_nonneg`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L73).

```lean
lemma μ₀_nonneg : 0 ≤ 𝓕.μ₀
```

**`Electromagnetism.FreeSpace.ε₀_ne_zero`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L76).

```lean
lemma ε₀_ne_zero : 𝓕.ε₀ ≠ 0
```

**`Electromagnetism.FreeSpace.μ₀_ne_zero`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L79).

```lean
lemma μ₀_ne_zero : 𝓕.μ₀ ≠ 0
```

## C. The speed of light

**`Electromagnetism.FreeSpace.c`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L88).

> The speed of light in free space.

```lean
noncomputable def c : SpeedOfLight
```

**`Electromagnetism.FreeSpace.c_val`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L95).

```lean
lemma c_val : (𝓕.c : ℝ) = 1 / √(𝓕.ε₀ * 𝓕.μ₀)
```

**`Electromagnetism.FreeSpace.c_sq`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L97).

```lean
lemma c_sq : (𝓕.c : ℝ) ^ 2 = 1 / (𝓕.ε₀ * 𝓕.μ₀)
```

**`Electromagnetism.FreeSpace.c_abs`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean#L105).

```lean
lemma c_abs : abs (𝓕.c : ℝ) = 𝓕.c
```

## Depends on

- [The Speed of Light](../../relativity/speedoflight.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Basic.lean)
