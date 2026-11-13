---
declaration: module
origin: cited
lean: StandardModel.DownSinglet.basis, StandardModel.DownSinglet.jetValLinEquiv, StandardModel.DownSinglet.repJetGaugeGroupI, StandardModel.DownSinglet.jetValLinEquiv_smul, StandardModel.DownSinglet.repJetGaugeGroupI_smul, StandardModel.DownSinglet.repJetGaugeGroupI_ofConstant, StandardModel.DownSinglet.basis_eq_mk, StandardModel.DownSinglet.repLorentzGroup_apply_basis
statement: formalized
proof: formalized
---

# Down-type singlets

The module `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean): 24 declarations (2 instances with no name), 22 with a docstring.

## i. Overview

> The Standard Model down-type singlet is a right-handed Weyl spinor in the `(3, 1)_{-2}`
> representation. Here charges are normalized as `6Y`, so `-2` is the usual hypercharge
> `Y = -1/3`.
>
> `DownSinglet` is the target vector space of one down-type quark multiplet. Its Weyl factor
> carries the Lorentz index and its three-dimensional factor carries the colour index. The absence
> of a weak factor makes it an `SU(2)` singlet.
>
> The Lorentz and gauge actions are first defined separately. The gauge action is then computed on a
> basis, used to identify its kernel, and descended to each supported global form of the Standard
> Model gauge group.

## ii. Key results

> - `DownSinglet` : the target space of the `(3, 1)_{-2}` multiplet.
> - `repLorentzGroup` : the right-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_tmul_basis_eq_sum` : the gauge action in a tensor-product basis.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.
> - `gaugeAlgebraAction` : the infinitesimal `(3, 1)_{-2}` action of the gauge algebra.
> - `repJetGaugeGroupI` : the jet gauge action on jets of the down singlet.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action.

## iv. References

> * None.

## A. The down-singlet space

> The Weyl factor carries the right-handed Lorentz index, while
> `EuclideanSpace ℂ (Fin 3)` carries the colour index.

## B. Linear structure

> `DownSinglet` wraps its tensor-product carrier as a distinct type. The equivalences below identify
> the two types and transport the additive and complex module structures to `DownSinglet`.

## C. The basis of the down-singlet space

**`StandardModel.DownSinglet.basis`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L95).

> A basis on the down singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3) ℂ DownSinglet
```

**An instance with no name**, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L99).

```lean
instance : Module.Finite ℂ DownSinglet
```

**An instance with no name**, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L101).

```lean
instance : Module.Free ℂ DownSinglet
```

## D. Lorentz action

> The Lorentz group acts on the right-handed Weyl factor and leaves the colour index fixed.

## E. Gauge action

> The `SU(3)` component acts on the colour index, while the `SU(2)` component acts trivially. The
> `U(1)` action is `star z ^ 2`; since `z` is unitary, `star z = z⁻¹`, so this represents charge
> `-2`.
>
> The tensor and basis formulas below expose the coefficients used to compare actions and compute the
> kernel.

## F. Kernel of the gauge action

> An element acts trivially when its colour action is scalar and that scalar cancels its `U(1)`
> phase. Its weak component is unrestricted because the down-type singlet is an `SU(2)` singlet.

## G. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its kernel. For
> the central `ℤ₆`, the colour phase is `x²` while the charge `-2` phase is `(star x)² = x⁻²`, so
> their product is one.

## H. The representation of the jet gauge group

**`StandardModel.DownSinglet.jetValLinEquiv`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L154).

> Absorbs the jet ring into the colour index: a jet of a down-type singlet is the
> same thing as a right-handed Weyl spinor tensored with a `SpaceTimeAlgebra`-valued colour
> vector,
>
>   `SpaceTimeAlgebra ⊗[ℂ] DownSinglet ≃
>     RightHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3)`.

```lean
noncomputable def jetValLinEquiv :
    SpaceTimeAlgebra ⊗[ℂ] DownSinglet ≃ₗ[ℂ]
      Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3)
```

**`StandardModel.DownSinglet.repJetGaugeGroupI`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L178).

> The `(3, 1)_{-2}` action of the jet gauge group on the jet space of the down-type
> singlet. Through `jetValLinEquiv` the colour matrix of the gauge jet, carrying the
> `-2` hypercharge phase `(star u) ^ 2`, acts `SpaceTimeAlgebra`-linearly on the colour factor by
> matrix-vector multiplication, while the Weyl factor is untouched.
>
> Both monoid laws come from bundled algebra maps — `Matrix.toLpLinAlgEquiv` and
> `Module.End.lTensorAlgHom` are morphisms of algebras — so only the multiplicativity of
> the colour-times-hypercharge matrix itself is checked. Note `Matrix.toLpLinAlgEquiv 2`
> is the same map as the `Matrix.toEuclideanLin` used by `repGaugeGroupI`, which is an
> abbreviation for `Matrix.toLpLin 2 2`, taken at the `CommRing` generality that
> `SpaceTimeAlgebra` needs.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] DownSinglet)
```

**`StandardModel.DownSinglet.jetValLinEquiv_smul`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L231).

> The identification of the jets of the down-type singlet intertwines multiplication by
> a scalar jet with the `SpaceTimeAlgebra`-scalar action on the colour coordinates.

```lean
lemma jetValLinEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] DownSinglet) :
    jetValLinEquiv (χ • z)
      = Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3))
          Fermion.RightHandedWeyl
          ((LinearMap.lsmul SpaceTimeAlgebra
              (EuclideanSpace SpaceTimeAlgebra (Fin 3)) χ).restrictScalars ℂ)
          (jetValLinEquiv z)
```

**`StandardModel.DownSinglet.repJetGaugeGroupI_smul`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L267).

> **The jet gauge action on the jets of the down-type singlet is fibrewise**: it
> commutes with multiplication by scalar jets, acting on the values of the field over the
> identity on spacetime.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] DownSinglet) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

**`StandardModel.DownSinglet.repJetGaugeGroupI_ofConstant`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L297).

> On jets of constant gauge transformations the jet action reduces to the global
> gauge action on the fibre: the `(3, 1)_{-2}` action on the down-singlet factor, and the
> trivial action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## I. Component transformation laws

> The basis of `DownSinglet` splits as a right-handed Weyl index and a colour index. The
> Lorentz group moves only the first, the gauge group only the second (up to the hypercharge
> scalar), so both actions are recorded as a single sum over the index they move. Dualising
> inverts and transposes the coefficient matrix, and conjugating stars it; the four
> combinations below are what a component of a down-singlet symbol needs.

**`StandardModel.DownSinglet.basis_eq_mk`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L353).

> The down-singlet basis vector as an explicit spinor–colour tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) : basis (k, c) =
    ⟨Fermion.RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c⟩
```

**`StandardModel.DownSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L361).

> The Lorentz action on the down-singlet basis: the colour index is inert and the
> spinor index transforms by the entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup Λ (basis j) = ∑ β, star (Λ.1 β j.1) • basis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L375).

> The down-singlet coordinate functionals transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • basis.dualBasis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L388).

> The Lorentz action on the conjugate down-singlet basis: the coefficients are the
> conjugates of those of the down-singlet action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, Λ.1 β j.1 • (Basis.conj basis) (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L397).

> The conjugate down-singlet coordinate functionals transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.DownSinglet.repLorentzGroup_neg_one`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L410).

> **The centre of `SL(2,ℂ)` acts on the down-singlet space by `-1`**: the value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.DownSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L420).

> The centre acts on the conjugate down-singlet space by `-1` as well: conjugation does not
> move a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

**`StandardModel.DownSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L430).

> The gauge action on the down-singlet basis: the spinor index is inert and the colour
> index transforms by the `SU(3)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI g (basis j) =
      ∑ c, (star g.toU1.1 ^ 2 * g.toSU3.1 c j.2) • basis (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L439).

> The down-singlet coordinate functionals carry the contragredient gauge action: the
> hypercharge and `SU(3)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) • basis.dualBasis (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L453).

> The gauge action on the conjugate down-singlet basis: the coefficients of the
> down-singlet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, star (star g.toU1.1 ^ 2 * g.toSU3.1 c j.2) • (Basis.conj basis) (j.1, c)
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L463).

> The conjugate down-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, star (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) •
        (Basis.conj basis).dualBasis (j.1, c)
```

## J. The gauge weight of the DownSinglet components

> The gauge torus acts diagonally on the basis of `DownSinglet`; the weights are recorded by
> `DownSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.DownSinglet.valueGaugeWeight`**, a def, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L490).

> The gauge weight of the down-singlet basis: the colour weights and hypercharge
> `-2`.

```lean
def DownSinglet.valueGaugeWeight (j : Fin 2 × Fin 3) : GaugeWeight
```

**`StandardModel.DownSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L495).

> The gauge torus acts diagonally on the basis of `DownSinglet`, with the weights
> `DownSinglet.valueGaugeWeight`.

```lean
lemma DownSinglet.repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI (gaugeTorusGen i) (DownSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) •
        DownSinglet.basis j
```

**`StandardModel.DownSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 515](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L515).

> The dual action of the gauge torus on the coordinate functionals of
> `DownSinglet`: the weights are negated.

```lean
lemma DownSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (DownSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i))) •
        DownSinglet.basis.coord j
```

**`StandardModel.DownSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L525).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `DownSinglet`: the two negations cancel and the weights are those of
> the value space.

```lean
lemma DownSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    DownSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj DownSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) •
        ((Basis.conj DownSinglet.basis)).coord j
```

## K. The boost weight of the DownSinglet components

**`StandardModel.downSinglet_repLorentzGroup_boostAxis_two_basis`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean#L546).

> The down-singlet basis diagonalises the `z`-boost: the colour index is inert, so the
> weight is the Weyl weight of the spinor index.

```lean
lemma downSinglet_repLorentzGroup_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0)
    (j : Fin 2 × Fin 3) :
    DownSinglet.repLorentzGroup (SL2C.boostAxis 2 t ht) (DownSinglet.basis j)
      = ((t : ℝ) : ℂ) ^ (weylWeight j.1) • DownSinglet.basis j
```

## Depends on

- [Down-type singlets](../../../../physlib/particles/standardmodel/fermions-downsinglet.md)
- [Gauge weight decompositions](../part-04/gaugegroup-gaugeweight.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)
- [The boost weights of a Weyl spinor](../../../relativity/fermions/weyl-boostweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/Basic.lean)
