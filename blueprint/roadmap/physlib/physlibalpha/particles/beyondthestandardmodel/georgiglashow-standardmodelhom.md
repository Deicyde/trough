---
declaration: module
origin: cited
lean: GeorgiGlashow.standardModelBlocks, GeorgiGlashow.standardModelHom, GeorgiGlashow.standardModelHom_val, GeorgiGlashow.standardModelHom_gaugeGroupℤ₆OfRoot, GeorgiGlashow.standardModelHom_ker, GeorgiGlashow.standardModelQuotientHom, GeorgiGlashow.standardModelQuotientHom_mk, GeorgiGlashow.standardModelQuotientHom_injective
statement: formalized
proof: formalized
---

# The Standard Model gauge homomorphism into SU(5)

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.GeorgiGlashow.StandardModelHom`, [PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean): 8 declarations, 7 with a docstring; 4 private, not shown.

> The weak and colour factors act on complementary subspaces of the Georgi–Glashow fundamental
> representation.

## i. Overview

> Write a Standard Model gauge transformation as `(h, g, α)` with `h ∈ SU(3)`, `g ∈ SU(2)`
> and `α ∈ U(1)`. On the decomposition `ℂ⁵ = ℂ² ⊕ ℂ³`, the weak doublet transforms by
> `α³ g` and the colour triplet by `α⁻² h`. The two blocks are unitary. Their determinants
> are `α⁶` and `α⁻⁶`, so the transformation belongs to `SU(5)`. Both blocks are the identity
> precisely for the central `ℤ₆` subgroup, so the homomorphism embeds the quotient by `ℤ₆`
> into `SU(5)`.

## ii. Key results

> - `GeorgiGlashow.standardModelHom` is the group homomorphism from the unquotiented Standard
>   Model gauge group to `SU(5)`.
> - `GeorgiGlashow.standardModelHom_ker` identifies the kernel with the central `ℤ₆` subgroup.
> - `GeorgiGlashow.standardModelQuotientHom_injective` gives faithfulness on the quotient.

## iv. References

> * J. Baez and J. Huerta, [The Algebra of Grand Unified Theories, pp. 34, 37](
>   https://math.ucr.edu/home/baez/guts.pdf#page=34). [ref: baez\_guts\_notes]

## A. The Standard Model gauge homomorphism

**`GeorgiGlashow.standardModelBlocks`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L57).

> The gauge transformation on the weak doublet and the colour triplet, in block coordinates.

```lean
noncomputable def standardModelBlocks (g : StandardModel.GaugeGroupI) :
    Matrix (Fin 2 ⊕ Fin 3) (Fin 2 ⊕ Fin 3) ℂ
```

**`GeorgiGlashow.standardModelHom`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L90).

> The Georgi–Glashow homomorphism from the unquotiented Standard Model gauge group to `SU(5)`.
> The first two coordinates carry weak isospin and the last three carry colour.

```lean
noncomputable def standardModelHom :
    StandardModel.GaugeGroupI →* specialUnitaryGroup (Fin 5) ℂ
```

**`GeorgiGlashow.standardModelHom_val`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L107).

> In the weak and colour basis the homomorphism has two diagonal blocks.

```lean
lemma standardModelHom_val (g : StandardModel.GaugeGroupI) :
    (standardModelHom g).1 = reindex finSumFinEquiv finSumFinEquiv (standardModelBlocks g)
```

## B. The kernel and the quotient embedding

**`GeorgiGlashow.standardModelHom_gaugeGroupℤ₆OfRoot`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L145).

> Each central sixth root of unity acts trivially on the weak and colour blocks.

```lean
lemma standardModelHom_gaugeGroupℤ₆OfRoot (α : rootsOfUnity 6 ℂ) :
    standardModelHom (gaugeGroupℤ₆OfRoot α) = 1
```

**`GeorgiGlashow.standardModelHom_ker`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L162).

> The kernel of the Georgi–Glashow homomorphism is the central `ℤ₆` of the Standard Model.

```lean
lemma standardModelHom_ker : standardModelHom.ker = gaugeGroupℤ₆SubGroup
```

**`GeorgiGlashow.standardModelQuotientHom`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L170).

> The homomorphism of the Standard Model gauge group modulo `ℤ₆` into `SU(5)`.

```lean
noncomputable def standardModelQuotientHom : GaugeGroupℤ₆ →* specialUnitaryGroup (Fin 5) ℂ
```

**`GeorgiGlashow.standardModelQuotientHom_mk`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L174).

```lean
lemma standardModelQuotientHom_mk (g : GaugeGroupI) :
    standardModelQuotientHom (GaugeGroupℤ₆.mk g) = standardModelHom g
```

**`GeorgiGlashow.standardModelQuotientHom_injective`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean#L178).

> The induced homomorphism embeds the quotient gauge group in `SU(5)`.

```lean
lemma standardModelQuotientHom_injective : Function.Injective standardModelQuotientHom
```

## Depends on

- [The Standard Model Gauge Group](../../../physlib/particles/standardmodel/gaugegroup/basic.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/BeyondTheStandardModel/GeorgiGlashow/StandardModelHom.lean)
