---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.volQuantum, CondensedMatter.TightBindingChain.volQuantum_eq_zero_iff, CondensedMatter.TightBindingChain.volQuantum_pos, CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_x, CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_y, CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_z, CondensedMatter.TightBindingChain.volQuantum_lt
statement: formalized
proof: formalized
---

# The volumetric quantum of the open tight binding cube

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Cube.VolumetricQuantum`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean): 7 declarations, 7 with a docstring.

## i. Overview

> A cube `Nx × Ny × Nz` carries one constant `C` per axis (`uncertaintyRatio_alongX`,
> `uncertaintyRatio_alongY`, `uncertaintyRatio_alongZ`), so its volumetric quantum is the product
> `δ(Nx) δ(Ny) δ(Nz)` of the dimensional quanta `δ = C - 1` of its axes: it vanishes iff some axis
> has `2` or `3` sites, is positive from `4 × 4 × 4` on, grows strictly in each axis and stays
> below `(√(π² / 3 - 2) - 1)³`.

## ii. Key results

> - `volQuantum` : the volumetric quantum `δ(Nx) δ(Ny) δ(Nz)` of the cube.
> - `volQuantum_eq_zero_iff`, `volQuantum_pos` : it vanishes iff some axis has `2` or `3` sites.
> - `volQuantum_lt_volQuantum_x` (and `y`, `z`), `volQuantum_lt` : strict growth in each axis,
>   below its limit.

## iv. References

> * H. P. Robertson, *A general formulation of the uncertainty principle and its classical
>   interpretation*, Phys. Rev. 35 (1930) 667.

## A. The volumetric quantum

**`CondensedMatter.TightBindingChain.volQuantum`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L57).

> The volumetric quantum of the cube `Nx × Ny × Nz`: the product of the dimensional quanta of
> its axes, each axis carrying its own `C` (`uncertaintyRatio_alongX`, `uncertaintyRatio_alongY`,
> `uncertaintyRatio_alongZ`).

```lean
noncomputable def volQuantum : ℝ
```

**`CondensedMatter.TightBindingChain.volQuantum_eq_zero_iff`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L62).

> The volumetric quantum vanishes iff some axis has `2` or `3` sites.

```lean
lemma volQuantum_eq_zero_iff (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) :
    volQuantum Tx Ty Tz = 0 ↔
      (Tx.N = 2 ∨ Tx.N = 3) ∨ (Ty.N = 2 ∨ Ty.N = 3) ∨ (Tz.N = 2 ∨ Tz.N = 3)
```

**`CondensedMatter.TightBindingChain.volQuantum_pos`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L70).

> From `4 × 4 × 4` on, the volumetric quantum is positive.

```lean
lemma volQuantum_pos (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N) : 0 < volQuantum Tx Ty Tz
```

**`CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_x`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L76).

> From `4 × 4 × 4` on, the volumetric quantum grows strictly along `x`.

```lean
lemma volQuantum_lt_volQuantum_x {Tx' : TightBindingChain} (hx : Tx.t ≠ 0) (hx' : Tx'.t ≠ 0)
    (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0) (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N)
    (h : Tx.N < Tx'.N) : volQuantum Tx Ty Tz < volQuantum Tx' Ty Tz
```

**`CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_y`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L86).

> From `4 × 4 × 4` on, the volumetric quantum grows strictly along `y`.

```lean
lemma volQuantum_lt_volQuantum_y {Ty' : TightBindingChain} (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0)
    (hy' : Ty'.t ≠ 0) (hz : Tz.t ≠ 0) (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N)
    (h : Ty.N < Ty'.N) : volQuantum Tx Ty Tz < volQuantum Tx Ty' Tz
```

**`CondensedMatter.TightBindingChain.volQuantum_lt_volQuantum_z`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L96).

> From `4 × 4 × 4` on, the volumetric quantum grows strictly along `z`.

```lean
lemma volQuantum_lt_volQuantum_z {Tz' : TightBindingChain} (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0)
    (hz : Tz.t ≠ 0) (hz' : Tz'.t ≠ 0) (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N)
    (h : Tz.N < Tz'.N) : volQuantum Tx Ty Tz < volQuantum Tx Ty Tz'
```

**`CondensedMatter.TightBindingChain.volQuantum_lt`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean#L106).

> From `4 × 4 × 4` on, the volumetric quantum stays below `(√(π² / 3 - 2) - 1)³`.

```lean
lemma volQuantum_lt (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N) :
    volQuantum Tx Ty Tz < (√(Real.pi ^ 2 / 3 - 2) - 1) ^ 3
```

## Depends on

- [The fluctuation angle of the maximal current state](maxcurrentstate-fluctuationangle.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/VolumetricQuantum.lean)
