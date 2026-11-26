---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet.basis, StandardModel.LeptonSinglet.basis_eq_mk, StandardModel.LeptonSinglet.repLorentzGroup_apply_basis, StandardModel.LeptonSinglet.repLorentzGroup_dual_dualBasis, StandardModel.LeptonSinglet.repLorentzGroup_conj_apply_basis, StandardModel.LeptonSinglet.repLorentzGroup_conj_dual_dualBasis, StandardModel.LeptonSinglet.repLorentzGroup_neg_one, StandardModel.LeptonSinglet.repLorentzGroup_conj_neg_one
statement: formalized
proof: formalized
---

# Charged-lepton singlets (PhyslibAlpha)

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean): 18 declarations (2 instances with no name), 18 with a docstring.

> The basis of the charged-lepton singlet `(1, 1)_{-6}`, its Lorentz and gauge actions on
> components, and the gauge weights of the components.

## i. Overview

> The Standard Model charged-lepton singlet is a right-handed Weyl spinor in the `(1, 1)_{-6}`
> representation. Here charges are normalized as `6Y`, so `-6` is the usual hypercharge
> `Y = -1`. Its value space `LeptonSinglet`, the Lorentz action `LeptonSinglet.repLorentzGroup`
> and the gauge action `LeptonSinglet.repGaugeGroupI` are in
> `Physlib.Particles.StandardModel.Fermions.LeptonSinglet`. The Weyl spinor carries the Lorentz
> index and is the whole of the multiplet, a charged-lepton singlet having no colour and no
> weak-isospin index.
>
> This file writes both actions on the Weyl basis, together with their dual, conjugate and
> conjugate-dual forms, which are what a component of a lepton-singlet symbol needs. The centre
> `-1` of `SL(2,ℂ)` acts by `-1`, as on any single Weyl-spinor index. The gauge group acts by the
> hypercharge scalar alone, so the gauge torus acts diagonally with weight hypercharge `-6`.

## ii. Key results

> - `StandardModel.LeptonSinglet.basis` : the Weyl basis.
> - `StandardModel.LeptonSinglet.repLorentzGroup_apply_basis`,
>   `StandardModel.LeptonSinglet.repGaugeGroupI_apply_basis` : the Lorentz and gauge actions on
>   the basis, with their dual and conjugate forms.
> - `StandardModel.LeptonSinglet.repLorentzGroup_neg_one` : the centre of `SL(2,ℂ)` acts by `-1`.
> - `StandardModel.LeptonSinglet.valueGaugeWeight` : the gauge weights of the basis, with
>   `StandardModel.LeptonSinglet.repGaugeGroupI_gaugeTorusGen_basis`.

## iv. References

> * None.

## A. The basis

**`StandardModel.LeptonSinglet.basis`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L71).

> A basis on the charged-lepton singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2) ℂ LeptonSinglet
```

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L75).

> The charged-lepton-singlet space is finite-dimensional.

```lean
instance : Module.Finite ℂ LeptonSinglet
```

**An instance with no name**, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L78).

> The charged-lepton-singlet space is free.

```lean
instance : Module.Free ℂ LeptonSinglet
```

**`StandardModel.LeptonSinglet.basis_eq_mk`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L81).

> The charged-lepton-singlet basis vector as an explicit Weyl spinor.

```lean
lemma basis_eq_mk (α : Fin 2) : basis α = ⟨Fermion.RightHandedWeyl.basis α⟩
```

## B. The Lorentz action on components

> The Lorentz group acts through the right-handed Weyl representation. Dualising inverts and
> transposes the coefficient matrix, and conjugating stars it.

**`StandardModel.LeptonSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L96).

> The Lorentz action on the lepton-singlet basis is the right-handed Weyl action, by the
> entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup Λ (basis α) = ∑ β, star (Λ.1 β α) • basis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L105).

> The lepton-singlet coordinate functionals transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis α) =
      ∑ β, star ((Λ⁻¹).1 α β) • basis.dualBasis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L114).

> The Lorentz action on the conjugate lepton-singlet basis. The coefficients are the
> conjugates of those of the lepton action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) α) = ∑ β, Λ.1 β α • (Basis.conj basis) β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L122).

> The conjugate lepton-singlet coordinate functionals transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis α) =
      ∑ β, (Λ⁻¹).1 α β • (Basis.conj basis).dualBasis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_neg_one`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L132).

> The centre of `SL(2,ℂ)` acts on the charged-lepton-singlet space by `-1`. The value
> space carries a single Weyl-spinor index, and `-1` is not the identity on a half-integer
> spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L140).

> The centre acts on the conjugate charged-lepton-singlet space by `-1` as well,
> conjugation not moving a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

## C. The gauge action on components

> The gauge group acts by the hypercharge scalar alone, the colour and weak factors acting
> trivially.

**`StandardModel.LeptonSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L157).

> The gauge action on the lepton-singlet basis is multiplication by the hypercharge
> scalar, the colour and weak factors acting trivially.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI g (basis α) = (star g.toU1.1 ^ 6 : ℂ) • basis α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L163).

> The lepton-singlet coordinate functionals carry the contragredient gauge action, the
> hypercharge scalar of the inverse group element.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis α) =
      (star (g⁻¹).toU1.1 ^ 6 : ℂ) • basis.dualBasis α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L174).

> The gauge action on the conjugate lepton-singlet basis is the hypercharge scalar,
> conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) α) =
      star (star g.toU1.1 ^ 6 : ℂ) • (Basis.conj basis) α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L182).

> The conjugate lepton-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis α) =
      star (star (g⁻¹).toU1.1 ^ 6 : ℂ) • (Basis.conj basis).dualBasis α
```

## D. The gauge weights of the components

> The gauge torus acts diagonally on the basis of `LeptonSinglet`. The weights are recorded by
> `LeptonSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.LeptonSinglet.valueGaugeWeight`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L202).

> The gauge weight of the lepton-singlet basis, hypercharge `-6`.

```lean
def valueGaugeWeight (_ : Fin 2) : GaugeWeight
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L207).

> The gauge torus acts diagonally on the basis of `LeptonSinglet`, with the weights
> `LeptonSinglet.valueGaugeWeight`.

```lean
lemma repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI (gaugeTorusGen i) (LeptonSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) •
        LeptonSinglet.basis j
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L219).

> The dual action of the gauge torus on the coordinate functionals of
> `LeptonSinglet` negates the weights.

```lean
lemma repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (LeptonSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i))) •
        LeptonSinglet.basis.coord j
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L229).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `LeptonSinglet`. The two negations cancel and the weights are those of
> the value space.

```lean
lemma repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj LeptonSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) •
        ((Basis.conj LeptonSinglet.basis)).coord j
```

## Depends on

- [Charged-lepton singlets (Physlib)](../../../../physlib/particles/standardmodel/fermions-leptonsinglet.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean)
