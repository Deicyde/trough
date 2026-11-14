---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet.basis, StandardModel.LeptonSinglet.repLorentzGroup_apply_basis, StandardModel.LeptonSinglet.repLorentzGroup_dual_dualBasis, StandardModel.LeptonSinglet.repLorentzGroup_conj_apply_basis, StandardModel.LeptonSinglet.repLorentzGroup_conj_dual_dualBasis, StandardModel.LeptonSinglet.repLorentzGroup_neg_one, StandardModel.LeptonSinglet.repLorentzGroup_conj_neg_one, StandardModel.LeptonSinglet.repGaugeGroupI_apply_basis
statement: formalized
proof: formalized
---

# Charged-lepton singlets (PhyslibAlpha)

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean): 22 declarations (2 instances with no name), 20 with a docstring.

## i. Overview

> The Standard Model charged-lepton singlet is a right-handed Weyl spinor in the `(1, 1)_{-6}`
> representation. Here charges are normalized as `6Y`, so `-6` is the usual hypercharge
> `Y = -1`.
>
> `LeptonSinglet` is the target vector space of one charged-lepton singlet. Its only index is
> the Lorentz index carried by the Weyl spinor.
>
> The Lorentz and gauge actions are first defined separately. The gauge action is then computed
> on an arbitrary spinor, used to identify its kernel, and descended to each supported global
> form of the Standard Model gauge group.

## ii. Key results

> - `LeptonSinglet` : the target space of the `(1, 1)_{-6}` multiplet.
> - `repLorentzGroup` : the right-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_apply` : the gauge action on a spinor.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.

## iv. References

> * None.

## A. The charged-lepton-singlet space

> The Weyl spinor carries the right-handed Lorentz index, and it is the whole of the multiplet:
> a charged-lepton singlet has no colour index and no weak-isospin index.

## B. Linear structure

> The wrapper distinguishes charged-lepton singlets from other isomorphic vector spaces.
> The following equivalences transfer the linear structure of the Weyl-spinor space and expose
> that model when defining representations.

### B.1. The basis of the charged-lepton-singlet space

**`StandardModel.LeptonSinglet.basis`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L88).

> A basis on the charged-lepton singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2) ℂ LeptonSinglet
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L91).

```lean
instance : Module.Finite ℂ LeptonSinglet
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L93).

```lean
instance : Module.Free ℂ LeptonSinglet
```

## C. Lorentz action

> The Lorentz group acts through the right-handed Weyl representation, transported along the
> identification of a charged-lepton singlet with its spinor.

**`StandardModel.LeptonSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L107).

> The Lorentz action on the lepton-singlet basis: the right-handed Weyl
> action by the entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup Λ (basis α) = ∑ β, star (Λ.1 β α) • basis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L116).

> The lepton jet coordinates transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis α) =
      ∑ β, star ((Λ⁻¹).1 α β) • basis.dualBasis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L125).

> The Lorentz action on the conjugate lepton basis: the coefficients are the
> conjugates of those of the lepton action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) α) = ∑ β, Λ.1 β α • (Basis.conj basis) β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L133).

> The conjugate lepton jet coordinates transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (α : Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis α) =
      ∑ β, (Λ⁻¹).1 α β • (Basis.conj basis).dualBasis β
```

**`StandardModel.LeptonSinglet.repLorentzGroup_neg_one`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L143).

> **The centre of `SL(2,ℂ)` acts on the charged-lepton-singlet space by `-1`**: the value
> space carries a single Weyl-spinor index, and `-1` is not the identity on a half-integer
> spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.LeptonSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L151).

> The centre acts on the conjugate charged-lepton-singlet space by `-1` as well:
> conjugation does not move a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

## D. Global Gauge action

> The colour and weak factors act trivially, so the gauge group acts only through hypercharge.
> The `U(1)` action is `star z ^ 6`; since `z` is unitary, `star z = z⁻¹`, so this represents
> charge `-6`.
>
> The formulas below expose the scalar used to compare actions and compute the kernel.

**`StandardModel.LeptonSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L170).

> The gauge action on the lepton-singlet basis: multiplication by the hypercharge
> scalar, the colour and weak factors acting trivially.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI g (basis α) = (star g.toU1.1 ^ 6 : ℂ) • basis α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L179).

> The lepton-singlet coordinate functionals carry the contragredient gauge action: the
> hypercharge scalar of the inverse group element.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis α) =
      (star (g⁻¹).toU1.1 ^ 6 : ℂ) • basis.dualBasis α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L190).

> The gauge action on the conjugate lepton-singlet basis: the hypercharge scalar,
> conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) α) =
      star (star g.toU1.1 ^ 6 : ℂ) • (Basis.conj basis) α
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L198).

> The conjugate lepton-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (α : Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis α) =
      star (star (g⁻¹).toU1.1 ^ 6 : ℂ) • (Basis.conj basis).dualBasis α
```

## E. Kernel of the gauge action

> An element acts trivially exactly when its hypercharge scalar is one. Its colour and weak
> components are unrestricted, since neither appears in the action.

## F. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its kernel.
> The `U(1)` component of a central element is a sixth root of unity, so conjugating and raising
> to the sixth power gives one, and charge `-6` therefore acts trivially.

## G. The representation of the jet gauge group

> The charged-lepton singlet carries no colour or weak index, so a jet of gauge
> transformations acts on its jets purely through the hypercharge power series
> `(star u) ^ 6`, multiplying the jet-ring factor and leaving the Weyl factor untouched.

**`StandardModel.LeptonSinglet.repJetGaugeGroupI`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L238).

> The `(1, 1)_{-6}` action of the jet gauge group on the jet space of the charged-lepton
> singlet: multiplication of the jet-ring factor by the hypercharge power series
> `(star u) ^ 6`.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] LeptonSinglet)
```

**`StandardModel.LeptonSinglet.repJetGaugeGroupI_tmul`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L268).

> The jet gauge action on a pure tensor of the jet space of the charged-lepton
> singlet.

```lean
lemma repJetGaugeGroupI_tmul (U : JetGaugeGroupI) (f : SpaceTimeAlgebra) (ψ : LeptonSinglet) :
    repJetGaugeGroupI U (f ⊗ₜ[ℂ] ψ)
      = ((star ((U.2.2 : unitary SpaceTimeAlgebra) : SpaceTimeAlgebra)) ^ 6 * f) ⊗ₜ[ℂ] ψ
```

**`StandardModel.LeptonSinglet.repJetGaugeGroupI_smul`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L276).

> **The jet gauge action on the jets of the charged-lepton singlet is fibrewise**: it
> commutes with multiplication by scalar jets.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] LeptonSinglet) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

**`StandardModel.LeptonSinglet.repJetGaugeGroupI_ofConstant`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L289).

> On jets of constant gauge transformations the jet action reduces to the global
> gauge action on the fibre: the `(1, 1)_{-6}` action on the lepton-singlet factor, and
> the trivial action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## H. The gauge weight of the LeptonSinglet components

> The gauge torus acts diagonally on the basis of `LeptonSinglet`; the weights are recorded by
> `LeptonSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.LeptonSinglet.valueGaugeWeight`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L319).

> The gauge weight of the lepton-singlet basis: hypercharge `-6`.

```lean
def LeptonSinglet.valueGaugeWeight (_ : Fin 2) : GaugeWeight
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L324).

> The gauge torus acts diagonally on the basis of `LeptonSinglet`, with the weights
> `LeptonSinglet.valueGaugeWeight`.

```lean
lemma LeptonSinglet.repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI (gaugeTorusGen i) (LeptonSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) •
        LeptonSinglet.basis j
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L339).

> The dual action of the gauge torus on the coordinate functionals of
> `LeptonSinglet`: the weights are negated.

```lean
lemma LeptonSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (LeptonSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i))) •
        LeptonSinglet.basis.coord j
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L349).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `LeptonSinglet`: the two negations cancel and the weights are those of
> the value space.

```lean
lemma LeptonSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2) :
    LeptonSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj LeptonSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) •
        ((Basis.conj LeptonSinglet.basis)).coord j
```

## I. The boost weight of the LeptonSinglet components

**`StandardModel.leptonSinglet_repLorentzGroup_boostAxis_two_basis`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean#L369).

> The charged-lepton-singlet basis diagonalises the `z`-boost.

```lean
lemma leptonSinglet_repLorentzGroup_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0) (j : Fin 2) :
    LeptonSinglet.repLorentzGroup (SL2C.boostAxis 2 t ht) (LeptonSinglet.basis j)
      = ((t : ℝ) : ℂ) ^ (weylWeight j) • LeptonSinglet.basis j
```

## Depends on

- [Charged-lepton singlets (Physlib)](../../../../physlib/particles/standardmodel/fermions-leptonsinglet.md)
- [Gauge weight decompositions](../part-04/gaugegroup-gaugeweight.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)
- [The boost weights of a Weyl spinor](../../../relativity/fermions/weyl-boostweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/Basic.lean)
