---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV, StandardModel.LeptonDoubletV.basis, StandardModel.LeptonDoubletV.basis_apply, StandardModel.LeptonDoubletV.repLorentzGroup, StandardModel.LeptonDoubletV.repLorentzGroup_tmul, StandardModel.LeptonDoubletV.repGaugeGroupI, StandardModel.LeptonDoubletV.repGaugeGroupI_tmul, StandardModel.LeptonDoubletV.repGaugeGroupI_apply_basis
statement: formalized
proof: formalized
---

# Lepton doublets (PhyslibAlpha)

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonDoublet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean): 27 declarations, 27 with a docstring; 2 private, not shown.

> The value space of the lepton doublet `(1, 2)_{-3}`, its Lorentz and gauge actions, their
> kernel and descent, and the actions and gauge weights on components.

## i. Overview

> The Standard Model lepton doublet is a left-handed Weyl spinor in the `(1, 2)_{-3}`
> representation. Here charges are normalized as `6Y`, so `-3` is the usual hypercharge
> `Y = -1/2`.
>
> `LeptonDoubletV` is its target space, a left-handed Weyl spinor tensored with the weak
> coordinates. The Lorentz group acts on the Weyl factor, the global gauge group on the weak
> factor by its `SU(2)` matrix scaled by the hypercharge phase.
>
> The gauge action is computed on a basis, used to identify its kernel, and descended to
> each supported global form of the Standard Model gauge group. Both actions are then written on
> the basis together with their dual, conjugate and conjugate-dual forms, which are what a
> component of a lepton-doublet symbol needs. The centre `-1` of `SL(2,ℂ)` acts by `-1`, as on
> any single Weyl-spinor index, and the gauge torus acts diagonally on the basis, with the isospin
> weights and hypercharge `-3`.

## ii. Key results

> - `LeptonDoubletV` : the target space of the `(1, 2)_{-3}` multiplet.
> - `repLorentzGroup` : the left-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_apply_basis` : the gauge action in the spinor–weak basis.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.
> - `repLorentzGroup_neg_one` : the centre of `SL(2,ℂ)` acts by `-1`.
> - `valueGaugeWeight` : the gauge weights of the basis, with
>   `repGaugeGroupI_gaugeTorusGen_basis`.

## iv. References

> * None.

## A. The lepton-doublet space

> The Weyl factor carries the left-handed Lorentz index, while the functions on `Fin 2`
> carry the weak index.

**`StandardModel.LeptonDoubletV`**, an abbrev, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L82).

> The target vector space of one Standard Model lepton doublet, a left-handed Weyl spinor
> tensored with the weak coordinates. It carries the `(1, 2)_{-3}` representation of the
> gauge group.

```lean
abbrev LeptonDoubletV : Type
```

## B. The basis

**`StandardModel.LeptonDoubletV.basis`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L94).

> A basis on the lepton doublets, the Weyl basis tensored with the coordinate basis of
> the weak index.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 2) ℂ LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.basis_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L98).

> The lepton-doublet basis vector as an explicit spinor–weak tensor.

```lean
lemma basis_apply (k j : Fin 2) :
    basis (k, j) = Fermion.LeftHandedWeyl.basis k ⊗ₜ[ℂ] Pi.single j 1
```

## C. Lorentz action

> The Lorentz group acts on the left-handed Weyl factor and leaves the weak index fixed.

**`StandardModel.LeptonDoubletV.repLorentzGroup`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L114).

> The left-handed Lorentz representation on lepton doublets, the left-handed Weyl action on
> the spinor factor and trivial on the weak index.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_tmul`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L119).

> The Lorentz action on a pure spinor–weak tensor is the left-handed action on the Weyl
> factor, the weak index untouched.

```lean
lemma repLorentzGroup_tmul (Λ : SL(2,ℂ)) (s : Fermion.LeftHandedWeyl) (v : Fin 2 → ℂ) :
    repLorentzGroup Λ (s ⊗ₜ v) = Fermion.LeftHandedWeyl.rep Λ s ⊗ₜ v
```

## D. Gauge action

> The colour factor acts trivially, while `SU(2)` acts on the weak index. The `U(1)` action
> is `star z ^ 3`; since `z` is unitary, `star z = z⁻¹`, so this represents charge `-3`.
>
> The tensor and basis formulas below expose the coefficients used to compare actions and
> compute the kernel.

**`StandardModel.LeptonDoubletV.repGaugeGroupI`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L138).

> The `(1, 2)_{-3}` action of the unquotiented Standard Model gauge group. The `SU(2)` matrix,
> scaled by the hypercharge factor `star u ^ 3`, acts on the weak index. Since `u` is unitary,
> `star u = u⁻¹`, so this is charge `-3`.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_tmul`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L152).

> On a pure spinor–weak tensor the `SU(2)` matrix, scaled by the hypercharge factor, acts on
> the weak index.

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (v : Fermion.LeftHandedWeyl) (w : Fin 2 → ℂ) :
    repGaugeGroupI g (v ⊗ₜ w) = v ⊗ₜ ((star g.toU1.1 ^ 3) • g.toSU2.1).mulVec w
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_apply_basis`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L159).

> The gauge action on the lepton-doublet basis. The spinor index is inert and the weak
> index transforms by the `SU(2)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI g (basis j) =
      ∑ w, (star g.toU1.1 ^ 3 * g.toSU2.1 w j.2) • basis (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L173).

> Expands the lepton-doublet gauge action on a tensor-product basis vector.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k j : Fin 2) :
    repGaugeGroupI g (basis (k, j)) =
      ∑ j' : Fin 2, (star g.toU1.1 ^ 3 * g.toSU2.1 j' j) • basis (k, j')
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L180).

> Two gauge elements induce the same action exactly when their weak-basis coefficients
> agree.

```lean
lemma repGaugeGroupI_eq_iff_mul_eq {g₁ g₂ : GaugeGroupI} :
    repGaugeGroupI g₁ = repGaugeGroupI g₂ ↔ ∀ j j',
    star g₁.toU1.1 ^ 3 * g₁.toSU2.1 j' j =
      star g₂.toU1.1 ^ 3 * g₂.toSU2.1 j' j
```

## E. Kernel of the gauge action

> An element acts trivially when its weak action is scalar and that scalar cancels its
> `U(1)` phase. Its colour component is unrestricted because the lepton doublet is an
> `SU(3)` singlet.

**`StandardModel.LeptonDoubletV.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L205).

> Characterizes the full-group elements acting trivially on the lepton doublet.

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ ∃ a : ℂ, g.toSU2.1 = a • 1 ∧
      a * star g.toU1.1 ^ 3 = 1
```

## F. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its
> kernel. For the central `ℤ₆`, the weak central phase and charge `-3` phase combine to a
> sixth power and therefore act trivially.

**`StandardModel.LeptonDoubletV.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L247).

> The central `ℤ₆` subgroup acts trivially on `(1, 2)_{-3}`.

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoubletV.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L261).

> Every supported quotient subgroup acts trivially on the lepton doublet.

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoubletV.repGaugeGroup`**, a def, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L267).

> The `(1, 2)_{-3}` representation for every supported global form of the
> Standard Model gauge group.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) LeptonDoubletV
```

## G. Component transformation laws

> The basis of `LeptonDoubletV` splits as a left-handed Weyl index and a weak-isospin index.
> The Lorentz group moves only the first, the gauge group only the second (up to the
> hypercharge scalar), so both actions are recorded as a single sum over the index they move.
> Dualising inverts and transposes the coefficient matrix, and conjugating stars it. The four
> combinations below are what a component of a lepton-doublet symbol needs.

**`StandardModel.LeptonDoubletV.repLorentzGroup_apply_basis`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L288).

> The Lorentz action on the lepton-doublet basis. The weak index is inert and the
> spinor index transforms by the matrix itself.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup Λ (basis j) = ∑ β, Λ.1 β j.1 • basis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_dual_dualBasis`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L314).

> The lepton-doublet coordinate functionals transform contragrediently, by the
> inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • basis.dualBasis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_apply_basis`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L327).

> The Lorentz action on the conjugate lepton-doublet basis. The coefficients are the
> conjugates of those of the lepton-doublet action.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, star (Λ.1 β j.1) • (Basis.conj basis) (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L337).

> The conjugate lepton-doublet coordinate functionals transform by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_neg_one`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L351).

> The centre of `SL(2,ℂ)` acts on the lepton-doublet space by `-1`. The value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_neg_one`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L361).

> The centre acts on the conjugate lepton-doublet space by `-1` as well, conjugation not
> moving a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L371).

> The lepton-doublet coordinate functionals carry the contragredient gauge action, by the
> hypercharge and `SU(2)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ w, (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) • basis.dualBasis (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L385).

> The gauge action on the conjugate lepton-doublet basis has the coefficients of the
> lepton-doublet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ w, star (star g.toU1.1 ^ 3 * g.toSU2.1 w j.2) • (Basis.conj basis) (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L395).

> The conjugate lepton-doublet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ w, star (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) •
        (Basis.conj basis).dualBasis (j.1, w)
```

## H. The gauge weights of the components

> The gauge torus acts diagonally on the basis of `LeptonDoubletV`. The weights are recorded by
> `LeptonDoubletV.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.LeptonDoubletV.valueGaugeWeight`**, a def, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L421).

> The gauge weight of the lepton-doublet basis, isospin weight and hypercharge
> `-3`.

```lean
def valueGaugeWeight (j : Fin 2 × Fin 2) : GaugeWeight
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L426).

> The gauge torus acts diagonally on the basis of `LeptonDoubletV`, with the weights
> `LeptonDoubletV.valueGaugeWeight`.

```lean
lemma repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI (gaugeTorusGen i) (LeptonDoubletV.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) •
        LeptonDoubletV.basis j
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L440).

> The dual action of the gauge torus on the coordinate functionals of
> `LeptonDoubletV` negates the weights.

```lean
lemma repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI.dual (gaugeTorusGen i) (LeptonDoubletV.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i))) •
        LeptonDoubletV.basis.coord j
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L450).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `LeptonDoubletV`. The two negations cancel and the weights are those of
> the value space.

```lean
lemma repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj LeptonDoubletV.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) •
        ((Basis.conj LeptonDoubletV.basis)).coord j
```

## Depends on

- [Left handed Weyl fermions](../../../../physlib/relativity/fermions/weyl/lefthanded.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean)
