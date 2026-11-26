---
declaration: module
origin: cited
lean: StandardModel.DownSinglet.basis, StandardModel.DownSinglet.basis_eq_mk, StandardModel.DownSinglet.repLorentzGroup_apply_basis, StandardModel.DownSinglet.repLorentzGroup_dual_dualBasis, StandardModel.DownSinglet.repLorentzGroup_conj_apply_basis, StandardModel.DownSinglet.repLorentzGroup_conj_dual_dualBasis, StandardModel.DownSinglet.repLorentzGroup_neg_one, StandardModel.DownSinglet.repLorentzGroup_conj_neg_one
statement: formalized
proof: formalized
---

# Down-type singlets (PhyslibAlpha)

The module `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean): 18 declarations (2 instances with no name), 18 with a docstring.

> The basis of the down-type singlet `(3, 1)_{-2}`, its Lorentz and gauge actions on components,
> and the gauge weights of the components.

## i. Overview

> The Standard Model down-type singlet is a right-handed Weyl spinor in the `(3, 1)_{-2}`
> representation. Here charges are normalized as `6Y`, so `-2` is the usual hypercharge
> `Y = -1/3`. Its value space `DownSinglet`, the Lorentz action `DownSinglet.repLorentzGroup` and
> the gauge action `DownSinglet.repGaugeGroupI` are in
> `Physlib.Particles.StandardModel.Fermions.DownSinglet`. The Weyl factor carries the Lorentz
> index and the three-dimensional factor the colour index. The absence of a weak factor makes it
> an `SU(2)` singlet.
>
> This file writes both actions on the basis of spinor–colour tensors, together with their dual,
> conjugate and conjugate-dual forms, which are what a component of a down-singlet symbol needs.
> The centre `-1` of `SL(2,ℂ)` acts by `-1`, as on any single Weyl-spinor index. The gauge torus
> acts diagonally on the basis, with the colour weights and hypercharge `-2`.

## ii. Key results

> - `StandardModel.DownSinglet.basis` : the basis of spinor–colour tensors.
> - `StandardModel.DownSinglet.repLorentzGroup_apply_basis`,
>   `StandardModel.DownSinglet.repGaugeGroupI_apply_basis` : the Lorentz and gauge actions on the
>   basis, with their dual and conjugate forms.
> - `StandardModel.DownSinglet.repLorentzGroup_neg_one` : the centre of `SL(2,ℂ)` acts by `-1`.
> - `StandardModel.DownSinglet.valueGaugeWeight` : the gauge weights of the basis, with
>   `StandardModel.DownSinglet.repGaugeGroupI_gaugeTorusGen_basis`.

## iv. References

> * None.

## A. The basis

> The basis of `DownSinglet` is the tensor product of the right-handed Weyl basis and the standard
> colour basis.

**`StandardModel.DownSinglet.basis`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L76).

> A basis on the down singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3) ℂ DownSinglet
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L81).

> The down-singlet space is finite-dimensional.

```lean
instance : Module.Finite ℂ DownSinglet
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L84).

> The down-singlet space is free.

```lean
instance : Module.Free ℂ DownSinglet
```

**`StandardModel.DownSinglet.basis_eq_mk`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L87).

> The down-singlet basis vector as an explicit spinor–colour tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) : basis (k, c) =
    ⟨Fermion.RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c⟩
```

## B. The Lorentz action on components

> The Lorentz group moves only the spinor index. Dualising inverts and transposes the coefficient
> matrix, and conjugating stars it.

**`StandardModel.DownSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L104).

> The Lorentz action on the down-singlet basis. The colour index is inert and the spinor
> index transforms by the entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup Λ (basis j) = ∑ β, star (Λ.1 β j.1) • basis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L118).

> The down-singlet coordinate functionals transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • basis.dualBasis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L131).

> The Lorentz action on the conjugate down-singlet basis. The coefficients are the
> conjugates of those of the down-singlet action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, Λ.1 β j.1 • (Basis.conj basis) (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L140).

> The conjugate down-singlet coordinate functionals transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_neg_one`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L153).

> The centre of `SL(2,ℂ)` acts on the down-singlet space by `-1`. The value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L163).

> The centre acts on the conjugate down-singlet space by `-1` as well, conjugation not moving
> a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

## C. The gauge action on components

> The gauge group moves only the colour index, up to the hypercharge scalar.

**`StandardModel.DownSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L181).

> The gauge action on the down-singlet basis. The spinor index is inert and the colour index
> transforms by the `SU(3)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI g (basis j) =
      ∑ c, (star g.toU1.1 ^ 2 * g.toSU3.1 c j.2) • basis (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L190).

> The down-singlet coordinate functionals carry the contragredient gauge action, by the
> hypercharge and `SU(3)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) • basis.dualBasis (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L204).

> The gauge action on the conjugate down-singlet basis has the coefficients of the
> down-singlet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, star (star g.toU1.1 ^ 2 * g.toSU3.1 c j.2) • (Basis.conj basis) (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L214).

> The conjugate down-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, star (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) •
        (Basis.conj basis).dualBasis (j.1, c)
```

## D. The gauge weights of the components

> The gauge torus acts diagonally on the basis of `DownSinglet`. The weights are recorded by
> `DownSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.DownSinglet.valueGaugeWeight`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L238).

> The gauge weight of the down-singlet basis, the colour weights and hypercharge `-2`.

```lean
def valueGaugeWeight (j : Fin 2 × Fin 3) : GaugeWeight
```

**`StandardModel.DownSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L243).

> The gauge torus acts diagonally on the basis of `DownSinglet`, with the weights
> `DownSinglet.valueGaugeWeight`.

```lean
lemma repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI (gaugeTorusGen i) (DownSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) •
        DownSinglet.basis j
```

**`StandardModel.DownSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L258).

> The dual action of the gauge torus on the coordinate functionals of `DownSinglet` negates
> the weights.

```lean
lemma repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (DownSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i))) •
        DownSinglet.basis.coord j
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L268).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `DownSinglet`. The two negations cancel and the weights are those of
> the value space.

```lean
lemma repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj DownSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) •
        ((Basis.conj DownSinglet.basis)).coord j
```

## Depends on

- [Down-type singlets (Physlib)](../../../../physlib/particles/standardmodel/fermions-downsinglet.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean)
