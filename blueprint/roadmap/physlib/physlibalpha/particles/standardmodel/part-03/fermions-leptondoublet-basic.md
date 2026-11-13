---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV, StandardModel.LeptonDoubletV.basis, StandardModel.LeptonDoubletV.basis_apply, StandardModel.LeptonDoubletV.repLorentzGroup, StandardModel.LeptonDoubletV.repLorentzGroup_tmul, StandardModel.LeptonDoubletV.doubletMatrix, StandardModel.LeptonDoubletV.doubletMatrix_eq, StandardModel.LeptonDoubletV.doubletMatrix_ofConstant_map_constantCoeff
statement: formalized
proof: formalized
---

# Lepton doublets

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonDoublet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean): 35 declarations, 35 with a docstring.

## i. Overview

> The Standard Model lepton doublet is a left-handed Weyl spinor in the `(1, 2)_{-3}`
> representation. Here charges are normalized as `6Y`, so `-3` is the usual hypercharge
> `Y = -1/2`.
>
> The lepton doublet is the datum `StandardModel.Model.leptonDoublet`,
> `(.L, .singlet, .fund, -3)`, of the Standard Model table. `LeptonDoubletV` is its target
> space, a left-handed Weyl spinor tensored with the weak coordinates, and every action on
> it — Lorentz, global gauge, jet gauge — is the one the general theory derives from the
> datum. The hand-built definitions are kept in comments.
>
> The gauge action is computed on a basis, used to identify its kernel, and descended to
> each supported global form of the Standard Model gauge group.

## ii. Key results

> - `LeptonDoubletV` : the target space of the `(1, 2)_{-3}` multiplet.
> - `repLorentzGroup` : the left-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_apply_basis` : the gauge action in the spinor–weak basis.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.
> - `repJetGaugeGroupI` : the action of the jet gauge group on the jets of the doublet.

## iv. References

> * None.

## A. The lepton-doublet space

> The Weyl factor carries the left-handed Lorentz index, while the functions on `Fin 2`
> carry the weak index.

**`StandardModel.LeptonDoubletV`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L77).

> The target vector space of one Standard Model lepton doublet: the target space of the
> datum `StandardModel.Model.leptonDoublet`, a left-handed Weyl spinor tensored with the
> weak coordinates. It carries the `(1, 2)_{-3}` representation of the gauge group.

```lean
abbrev LeptonDoubletV : Type
```

## B. The basis

**`StandardModel.LeptonDoubletV.basis`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L92).

> A basis on the lepton doublets: the Weyl basis tensored with the coordinate basis of
> the weak index.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 2) ℂ LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.basis_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L96).

> The lepton-doublet basis vector as an explicit spinor–weak tensor.

```lean
lemma basis_apply (k j : Fin 2) :
    basis (k, j) = Fermion.LeftHandedWeyl.basis k ⊗ₜ[ℂ] Pi.single j 1
```

## C. Lorentz action

> The Lorentz group acts on the left-handed Weyl factor and leaves the weak index fixed.

**`StandardModel.LeptonDoubletV.repLorentzGroup`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L112).

> The left-handed Lorentz representation on lepton doublets: the Lorentz action the
> general theory derives from the datum.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_tmul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L133).

> The Lorentz action on a pure spinor–weak tensor: the left-handed action on the Weyl
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

**`StandardModel.LeptonDoubletV.doubletMatrix`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L151).

> The `SpaceTimeAlgebra`-valued weak matrix of the jet gauge action on the lepton doublet: the
> matrix of jets by which a gauge jet acts on the datum.

```lean
noncomputable def doubletMatrix (U : JetGaugeGroupI) : Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra
```

**`StandardModel.LeptonDoubletV.doubletMatrix_eq`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L157).

> The weak matrix of a gauge jet is its `SU(2)` matrix carrying the `-3` hypercharge
> phase `(star u) ^ 3`.

```lean
lemma doubletMatrix_eq (U : JetGaugeGroupI) :
    doubletMatrix U = ((star ((U.2.2 : unitary SpaceTimeAlgebra) : SpaceTimeAlgebra)) ^ 3) •
      ((U.2.1 : specialUnitaryGroup (Fin 2) SpaceTimeAlgebra) : Matrix (Fin 2)
          (Fin 2) SpaceTimeAlgebra)
```

**`StandardModel.LeptonDoubletV.doubletMatrix_ofConstant_map_constantCoeff`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L166).

> The constant term of the weak matrix of a constant gauge jet: the `SU(2)` matrix of
> the gauge transformation carrying its `-3` hypercharge phase.

```lean
lemma doubletMatrix_ofConstant_map_constantCoeff (g : GaugeGroupI) :
    (doubletMatrix (JetGaugeGroupI.ofConstant g)).map (constantCoeff : SpaceTimeAlgebra → ℂ)
      = (star g.toU1.1 ^ 3) • g.toSU2.1
```

**`StandardModel.LeptonDoubletV.doubletMatrix_ofConstant`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L179).

> The weak matrix of a constant gauge jet is constant.

```lean
lemma doubletMatrix_ofConstant (g : GaugeGroupI) :
    doubletMatrix (JetGaugeGroupI.ofConstant g)
      = ((doubletMatrix (JetGaugeGroupI.ofConstant g)).map
          (constantCoeff : SpaceTimeAlgebra → ℂ)).map
          (MvPowerSeries.C : ℂ → SpaceTimeAlgebra)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L195).

> The `(1, 2)_{-3}` action of the unquotiented Standard Model gauge group: the global
> action the general theory derives from the datum, the constant term of the jet action.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_tmul`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L218).

> The gauge action on a pure spinor–weak tensor: the `SU(2)` matrix, scaled by the
> hypercharge factor, acts on the weak index.

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (v : Fermion.LeftHandedWeyl) (w : Fin 2 → ℂ) :
    repGaugeGroupI g (v ⊗ₜ w) = v ⊗ₜ ((star g.toU1.1 ^ 3) • g.toSU2.1).mulVec w
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_apply_basis`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L225).

> The gauge action on the lepton-doublet basis: the spinor index is inert and the weak
> index transforms by the `SU(2)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI g (basis j) =
      ∑ w, (star g.toU1.1 ^ 3 * g.toSU2.1 w j.2) • basis (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L239).

> Expands the lepton-doublet gauge action on a tensor-product basis vector.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k j : Fin 2) :
    repGaugeGroupI g (basis (k, j)) =
      ∑ j' : Fin 2, (star g.toU1.1 ^ 3 * g.toSU2.1 j' j) • basis (k, j')
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L246).

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

**`StandardModel.LeptonDoubletV.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L271).

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

**`StandardModel.LeptonDoubletV.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L313).

> The central `ℤ₆` subgroup acts trivially on `(1, 2)_{-3}`.

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoubletV.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L327).

> Every supported quotient subgroup acts trivially on the lepton doublet.

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoubletV.repGaugeGroup`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L333).

> The `(1, 2)_{-3}` representation for every supported global form of the
> Standard Model gauge group.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) LeptonDoubletV
```

## G. Jet gauge action

> The `(1, 2)_{-3}` representation extends to jets: the `SU(2)` power-series matrix of a
> jet of gauge transformations, scaled by the hypercharge power series `star u ^ 3`, acts
> `SpaceTimeAlgebra`-linearly on the weak factor. On jets of constant gauge transformations the
> action reduces to the global gauge action. Both are the general theory's, for the datum.

**`StandardModel.LeptonDoubletV.repJetGaugeGroupI`**, a def, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L353).

> The `(1, 2)_{-3}` action of the jet gauge group on the jet space of the lepton
> doublet: the jet action the general theory derives from the datum.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] LeptonDoubletV)
```

**`StandardModel.LeptonDoubletV.repJetGaugeGroupI_smul`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L389).

> **The jet gauge action on the jets of the lepton doublet is fibrewise**: it commutes
> with multiplication by scalar jets.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] LeptonDoubletV) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

**`StandardModel.LeptonDoubletV.repJetGaugeGroupI_ofConstant`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L397).

> On jets of constant gauge transformations the jet action reduces to the global
> gauge action on the fibre: the `(1, 2)_{-3}` action on the lepton-doublet factor, and
> the trivial action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## H. Component transformation laws

> The basis of `LeptonDoubletV` splits as a left-handed Weyl index and a weak-isospin index.
> The Lorentz group moves only the first, the gauge group only the second (up to the
> hypercharge scalar), so both actions are recorded as a single sum over the index they move.
> Dualising inverts and transposes the coefficient matrix, and conjugating stars it; the four
> combinations below are what a component of a lepton-doublet symbol needs.

**`StandardModel.LeptonDoubletV.repLorentzGroup_apply_basis`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L417).

> The Lorentz action on the lepton-doublet basis: the weak index is inert and the
> spinor index transforms by the matrix itself.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup Λ (basis j) = ∑ β, Λ.1 β j.1 • basis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_dual_dualBasis`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L427).

> The lepton-doublet coordinate functionals transform contragrediently, by the
> inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • basis.dualBasis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_apply_basis`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L440).

> The Lorentz action on the conjugate lepton-doublet basis: the coefficients are the
> conjugates of those of the lepton-doublet action.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, star (Λ.1 β j.1) • (Basis.conj basis) (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L450).

> The conjugate lepton-doublet coordinate functionals transform by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_neg_one`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L463).

> **The centre of `SL(2,ℂ)` acts on the lepton-doublet space by `-1`**: the value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.LeptonDoubletV.repLorentzGroup_conj_neg_one`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L473).

> The centre acts on the conjugate lepton-doublet space by `-1` as well: conjugation does not
> move a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L483).

> The lepton-doublet coordinate functionals carry the contragredient gauge action: the
> hypercharge and `SU(2)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ w, (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) • basis.dualBasis (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L497).

> The gauge action on the conjugate lepton-doublet basis: the coefficients of the
> lepton-doublet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ w, star (star g.toU1.1 ^ 3 * g.toSU2.1 w j.2) • (Basis.conj basis) (j.1, w)
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L507).

> The conjugate lepton-doublet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ w, star (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) •
        (Basis.conj basis).dualBasis (j.1, w)
```

## I. The gauge weight of the LeptonDoubletV components

> The gauge torus acts diagonally on the basis of `LeptonDoubletV`; the weights are recorded by
> `LeptonDoubletV.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.LeptonDoubletV.valueGaugeWeight`**, a def, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L534).

> The gauge weight of the lepton-doublet basis: the isospin weight and hypercharge
> `-3`.

```lean
def LeptonDoubletV.valueGaugeWeight (j : Fin 2 × Fin 2) : GaugeWeight
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L539).

> The gauge torus acts diagonally on the basis of `LeptonDoubletV`, with the weights
> `LeptonDoubletV.valueGaugeWeight`.

```lean
lemma LeptonDoubletV.repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI (gaugeTorusGen i) (LeptonDoubletV.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) •
        LeptonDoubletV.basis j
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L553).

> The dual action of the gauge torus on the coordinate functionals of
> `LeptonDoubletV`: the weights are negated.

```lean
lemma LeptonDoubletV.repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI.dual (gaugeTorusGen i) (LeptonDoubletV.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i))) •
        LeptonDoubletV.basis.coord j
```

**`StandardModel.LeptonDoubletV.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L563).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `LeptonDoubletV`: the two negations cancel and the weights are those of
> the value space.

```lean
lemma LeptonDoubletV.repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj LeptonDoubletV.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) •
        ((Basis.conj LeptonDoubletV.basis)).coord j
```

## J. The boost weight of the LeptonDoubletV components

**`StandardModel.leptonDoublet_repLorentzGroup_boostAxis_two_basis`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean#L583).

> The lepton-doublet basis diagonalises the `z`-boost: the isospin index is inert.

```lean
lemma leptonDoublet_repLorentzGroup_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0)
    (j : Fin 2 × Fin 2) :
    LeptonDoubletV.repLorentzGroup (SL2C.boostAxis 2 t ht) (LeptonDoubletV.basis j)
      = ((t : ℝ) : ℂ) ^ (weylWeight j.1) • LeptonDoubletV.basis j
```

## Depends on

- [The Standard Model](../part-01/basic.md)
- [Gauge weight decompositions](../part-04/gaugegroup-gaugeweight.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)
- [The boost weights of a Weyl spinor](../../../relativity/fermions/weyl-boostweight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/Basic.lean)
