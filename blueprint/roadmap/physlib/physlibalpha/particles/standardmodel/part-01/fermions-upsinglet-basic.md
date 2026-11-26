---
declaration: module
origin: cited
lean: StandardModel.UpSinglet.basis, StandardModel.UpSinglet.basis_eq_mk, StandardModel.UpSinglet.repLorentzGroup_apply_basis, StandardModel.UpSinglet.repLorentzGroup_dual_dualBasis, StandardModel.UpSinglet.repLorentzGroup_conj_apply_basis, StandardModel.UpSinglet.repLorentzGroup_conj_dual_dualBasis, StandardModel.UpSinglet.repLorentzGroup_neg_one, StandardModel.UpSinglet.repLorentzGroup_conj_neg_one
statement: formalized
proof: formalized
---

# Up-type singlets (PhyslibAlpha)

The module `PhyslibAlpha.Particles.StandardModel.Fermions.UpSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean): 18 declarations (2 instances with no name), 18 with a docstring.

> The basis of the up-type singlet `(3, 1)_{4}`, its Lorentz and gauge actions on components,
> and the gauge weights of the components.

## i. Overview

> The Standard Model up-type singlet is a right-handed Weyl spinor in the `(3, 1)_{4}`
> representation. Here charges are normalized as `6Y`, so `4` is the usual hypercharge
> `Y = 2/3`. Its value space `UpSinglet`, the Lorentz action `UpSinglet.repLorentzGroup` and the
> gauge action `UpSinglet.repGaugeGroupI` are in `Physlib.Particles.StandardModel.Fermions.UpSinglet`.
> The Weyl factor carries the Lorentz index and the three-dimensional factor the colour index.
>
> This file writes both actions on the basis of spinor–colour tensors, together with their dual,
> conjugate and conjugate-dual forms, which are what a component of an up-singlet symbol needs.
> The centre `-1` of `SL(2,ℂ)` acts by `-1`, as on any single Weyl-spinor index. The gauge torus
> acts diagonally on the basis, with the colour weights and hypercharge `4`.

## ii. Key results

> - `StandardModel.UpSinglet.basis` : the basis of spinor–colour tensors.
> - `StandardModel.UpSinglet.repLorentzGroup_apply_basis`,
>   `StandardModel.UpSinglet.repGaugeGroupI_apply_basis` : the Lorentz and gauge actions on the
>   basis, with their dual and conjugate forms.
> - `StandardModel.UpSinglet.repLorentzGroup_neg_one` : the centre of `SL(2,ℂ)` acts by `-1`.
> - `StandardModel.UpSinglet.valueGaugeWeight` : the gauge weights of the basis, with
>   `StandardModel.UpSinglet.repGaugeGroupI_gaugeTorusGen_basis`.

## iv. References

> * None.

## A. The basis

> The basis of `UpSinglet` is the tensor product of the right-handed Weyl basis and the standard
> colour basis.

**`StandardModel.UpSinglet.basis`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L74).

> A basis on the up singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3) ℂ UpSinglet
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L79).

> The up-singlet space is finite-dimensional.

```lean
instance : Module.Finite ℂ UpSinglet
```

**An instance with no name**, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L82).

> The up-singlet space is free.

```lean
instance : Module.Free ℂ UpSinglet
```

**`StandardModel.UpSinglet.basis_eq_mk`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L85).

> The up-singlet basis vector as an explicit spinor–colour tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) : basis (k, c) =
    ⟨Fermion.RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c⟩
```

## B. The Lorentz action on components

> The Lorentz group moves only the spinor index. Dualising inverts and transposes the coefficient
> matrix, and conjugating stars it.

**`StandardModel.UpSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L102).

> The Lorentz action on the up-singlet basis. The colour index is inert and the
> spinor index transforms by the entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup Λ (basis j) = ∑ β, star (Λ.1 β j.1) • basis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L116).

> The up-singlet coordinate functionals transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • basis.dualBasis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L129).

> The Lorentz action on the conjugate up-singlet basis. The coefficients are the
> conjugates of those of the up-singlet action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, Λ.1 β j.1 • (Basis.conj basis) (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L138).

> The conjugate up-singlet coordinate functionals transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_neg_one`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L151).

> The centre of `SL(2,ℂ)` acts on the up-singlet space by `-1`. The value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L161).

> The centre acts on the conjugate up-singlet space by `-1` as well, conjugation not
> moving a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

## C. The gauge action on components

> The gauge group moves only the colour index, up to the hypercharge scalar.

**`StandardModel.UpSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L179).

> The gauge action on the up-singlet basis. The spinor index is inert and the colour
> index transforms by the `SU(3)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI g (basis j) =
      ∑ c, (g.toU1.1 ^ 4 * g.toSU3.1 c j.2) • basis (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L188).

> The up-singlet coordinate functionals carry the contragredient gauge action, by the
> hypercharge and `SU(3)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) • basis.dualBasis (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L202).

> The gauge action on the conjugate up-singlet basis has the coefficients of the
> up-singlet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, star (g.toU1.1 ^ 4 * g.toSU3.1 c j.2) • (Basis.conj basis) (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L212).

> The conjugate up-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, star ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) •
        (Basis.conj basis).dualBasis (j.1, c)
```

## D. The gauge weights of the components

> The gauge torus acts diagonally on the basis of `UpSinglet`. The weights are recorded by
> `UpSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.UpSinglet.valueGaugeWeight`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L237).

> The gauge weight of the up-singlet basis, colour weights and hypercharge
> `4`.

```lean
def valueGaugeWeight (j : Fin 2 × Fin 3) : GaugeWeight
```

**`StandardModel.UpSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L242).

> The gauge torus acts diagonally on the basis of `UpSinglet`, with the weights
> `UpSinglet.valueGaugeWeight`.

```lean
lemma repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI (gaugeTorusGen i) (UpSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) •
        UpSinglet.basis j
```

**`StandardModel.UpSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L257).

> The dual action of the gauge torus on the coordinate functionals of
> `UpSinglet` negates the weights.

```lean
lemma repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (UpSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i))) •
        UpSinglet.basis.coord j
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L267).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `UpSinglet`. The two negations cancel and the weights are those of
> the value space.

```lean
lemma repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i) (((Basis.conj UpSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) •
        ((Basis.conj UpSinglet.basis)).coord j
```

## Depends on

- [Up-type singlets (Physlib)](../../../../physlib/particles/standardmodel/fermions-upsinglet.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean)
