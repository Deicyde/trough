---
declaration: module
origin: cited
lean: Lorentz.cycDir, Lorentz.cycDir_inl, Lorentz.cycDir_inr, Lorentz.cycDir_comp_two, Lorentz.cycDir_comp_one, Lorentz.cycDir_comp_nil, Lorentz.cycDir_cycDir_cycDir, Lorentz.cycDir_injective
statement: formalized
proof: formalized
---

# The cyclic rotation and the half turns

The module `PhyslibAlpha.Relativity.SL2C.AxisRotations`, [PhyslibAlpha/Relativity/SL2C/AxisRotations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean): 18 declarations, 18 with a docstring.

> The rotation cycling the spatial axes, and the rotations by `π` about a coordinate axis.

## i. Overview

> `Physlib.Relativity.SL2C.AxisRotations` carries the rotations taking the `z`-axis to a chosen
> coordinate axis. Two further distinguished rotations are added here, both of which act on the
> Lorentz index by a permutation or a sign and so can be used to relabel the axes in a
> classification.
>
> The cyclic rotation `rotationCycle` is the rotation by `2π/3` about the diagonal spatial axis.
> Its Lorentz matrix is the permutation matrix of `cycDir`, the permutation fixing time and
> sending `x → y → z → x`. Since `cycDir` has order three, an index family not fixed by it has
> three distinct rotations, which is `cycDir_orbit_distinct`: that is what lets one axis of a
> three-axis statement be proved and the other two obtained by relabelling.
>
> The half turn `halfTurn k` is the rotation by `π` about the axis `k`, taken as the lift
> `-i σ_k`. Its Lorentz matrix is diagonal: it fixes time and the axis and negates the two
> transverse directions, with the signs recorded by `halfTurnSign`.
>
> The spatial-axis convention is `0 = x`, `1 = y`, `2 = z`.

## ii. Key results

> - `Lorentz.cycDir` : the cyclic permutation of Lorentz direction labels.
> - `Lorentz.cycDir_cycDir_cycDir`, `Lorentz.cycDir_orbit_distinct` : it has order three, and an
>   index family it does not fix has three distinct rotations.
> - `Lorentz.SL2C.rotationCycle` : the cyclic rotation in `SL(2, ℂ)`.
> - `Lorentz.SL2C.toLorentzGroup_rotationCycle_apply` : its Lorentz matrix is the permutation
>   matrix of `cycDir`.
> - `Lorentz.halfTurnSign`, `Lorentz.SL2C.halfTurn` : the half turn about a coordinate axis.
> - `Lorentz.SL2C.toLorentzGroup_halfTurn_apply` : its diagonal Lorentz matrix.

## iv. References

> The rotations from the `z`-axis to a coordinate axis are in
> `Physlib.Relativity.SL2C.AxisRotations`.

## A. The cyclic coordinate rotation

**`Lorentz.cycDir`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L69).

> The cyclic permutation of Lorentz direction labels: time is fixed and the spatial
> directions rotate as `x → y → z → x`.

```lean
def cycDir : Fin 1 ⊕ Fin 3 → Fin 1 ⊕ Fin 3
```

**`Lorentz.cycDir_inl`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L72).

> The cyclic permutation fixes the time direction.

```lean
lemma cycDir_inl : cycDir (Sum.inl 0) = Sum.inl 0
```

**`Lorentz.cycDir_inr`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L75).

> The cyclic permutation advances a spatial direction by one.

```lean
lemma cycDir_inr (m : Fin 3) : cycDir (Sum.inr m) = Sum.inr (m + 1)
```

**`Lorentz.cycDir_comp_two`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L78).

> Composing the cyclic permutation with a two-slot index vector rotates both entries.

```lean
lemma cycDir_comp_two (μ ν : Fin 1 ⊕ Fin 3) :
    (fun j => cycDir (![μ, ν] j)) = ![cycDir μ, cycDir ν]
```

**`Lorentz.cycDir_comp_one`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L84).

> Composing the cyclic permutation with a one-slot index vector rotates its entry.

```lean
lemma cycDir_comp_one (μ : Fin 1 ⊕ Fin 3) :
    (fun j => cycDir (![μ] j)) = ![cycDir μ]
```

**`Lorentz.cycDir_comp_nil`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L91).

> Composing the cyclic permutation with the empty index vector is the empty vector.

```lean
lemma cycDir_comp_nil : (fun j : Fin 0 => cycDir (![] j)) = ![]
```

**`Lorentz.cycDir_cycDir_cycDir`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L96).

> The cyclic permutation of Lorentz direction labels has order three.

```lean
lemma cycDir_cycDir_cycDir (μ : Fin 1 ⊕ Fin 3) : cycDir (cycDir (cycDir μ)) = μ
```

**`Lorentz.cycDir_injective`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L108).

> The cyclic permutation of Lorentz direction labels is injective: applying it twice
> more returns the original label.

```lean
lemma cycDir_injective : Function.Injective cycDir
```

**`Lorentz.cycDir_orbit_distinct`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L112).

> An index not fixed by the rotation has three distinct rotations.

```lean
lemma cycDir_orbit_distinct {ι : Type*} (d : ι → Fin 1 ⊕ Fin 3)
    (hd : (fun s => cycDir (d s)) ≠ d) :
    (fun s => cycDir (cycDir (d s))) ≠ d
      ∧ (fun s => cycDir (cycDir (d s))) ≠ (fun s => cycDir (d s))
```

**`Lorentz.SL2C.rotationCycle`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L129).

> The cyclic rotation `x → y → z → x` in `SL(2,ℂ)`, realized as the rotation by
> `2π/3` about the diagonal spatial axis.

```lean
noncomputable def rotationCycle : SL(2,ℂ)
```

**`Lorentz.SL2C.toLorentzGroup_rotationCycle_apply`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L137).

> The Lorentz matrix of `rotationCycle`: it is the permutation matrix associated with
> `cycDir`.

```lean
lemma toLorentzGroup_rotationCycle_apply (a b : Fin 1 ⊕ Fin 3) :
    (toLorentzGroup rotationCycle).1 a b = if a = cycDir b then 1 else 0
```

## B. Half turns about the coordinate axes

> The half turn about the axis `k` is the rotation by `π` about it. It has two lifts to
> `SL(2,ℂ)`, `-i σ_k` and `i σ_k`, which differ by the central element `-1` and have the same
> Lorentz matrix. The chosen lift `halfTurn k` is `-i σ_k`, the value at `θ = π` of
> `cos (θ / 2) - i sin (θ / 2) σ_k`, the convention `rotationCycle` also follows. Its Lorentz
> matrix is diagonal: it fixes time and the axis and negates the two transverse directions, with
> the signs recorded by `halfTurnSign`.

**`Lorentz.halfTurnSign`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L168).

> The sign the half turn about the axis `k` gives a direction: `1` on time and on the axis,
> `-1` on the two transverse directions.

```lean
def halfTurnSign (k : Fin 3) (μ : Fin 1 ⊕ Fin 3) : ℤ
```

**`Lorentz.SL2C.halfTurn`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L177).

> The half turn about the axis `k`, the rotation by `π` about it, as the element `-i σ_k` of
> `SL(2,ℂ)`. The other lift `i σ_k` is `-halfTurn k`.

```lean
noncomputable def halfTurn : Fin 3 → SL(2,ℂ)
```

**`Lorentz.SL2C.halfTurn_zero_apply`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L189).

> The matrix entries of the half turn about the `x`-axis, `-i σ_x`.

```lean
lemma halfTurn_zero_apply (j k : Fin 2) :
    (halfTurn 0).1 j k = (!![0, -Complex.I; -Complex.I, 0]) j k
```

**`Lorentz.SL2C.halfTurn_one_apply`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L193).

> The matrix entries of the half turn about the `y`-axis, `-i σ_y`.

```lean
lemma halfTurn_one_apply (j k : Fin 2) :
    (halfTurn 1).1 j k = (!![0, -1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ) j k
```

**`Lorentz.SL2C.halfTurn_two_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L197).

> The matrix entries of the half turn about the `z`-axis, `-i σ_z`.

```lean
lemma halfTurn_two_apply (j k : Fin 2) :
    (halfTurn 2).1 j k = (!![-Complex.I, 0; 0, Complex.I]) j k
```

**`Lorentz.SL2C.toLorentzGroup_halfTurn_apply`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L202).

> The Lorentz matrix of the half turn about the axis `k` is diagonal, with the signs
> `halfTurnSign k`: it fixes time and the axis and negates the two transverse directions.

```lean
lemma toLorentzGroup_halfTurn_apply (k : Fin 3) (a b : Fin 1 ⊕ Fin 3) :
    (toLorentzGroup (halfTurn k)).1 a b = if a = b then (halfTurnSign k a : ℝ) else 0
```

**`Lorentz.SL2C.toLorentzGroup_halfTurn_symm`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean#L211).

> The Lorentz matrix of the half turn is diagonal, hence symmetric.

```lean
lemma toLorentzGroup_halfTurn_symm (k : Fin 3) (a b : Fin 1 ⊕ Fin 3) :
    (toLorentzGroup (halfTurn k)).1 a b = (toLorentzGroup (halfTurn k)).1 b a
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../physlib/relativity/sl2c/basic.md)

## Sources

- [PhyslibAlpha/Relativity/SL2C/AxisRotations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/SL2C/AxisRotations.lean)
