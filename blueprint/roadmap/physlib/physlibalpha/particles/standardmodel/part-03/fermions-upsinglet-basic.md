---
declaration: module
origin: cited
lean: StandardModel.UpSinglet.basis, StandardModel.UpSinglet.jetValLinEquiv, StandardModel.UpSinglet.repJetGaugeGroupI, StandardModel.UpSinglet.jetValLinEquiv_smul, StandardModel.UpSinglet.repJetGaugeGroupI_smul, StandardModel.UpSinglet.repJetGaugeGroupI_ofConstant, StandardModel.UpSinglet.basis_eq_mk, StandardModel.UpSinglet.repLorentzGroup_apply_basis
statement: formalized
proof: formalized
---

# Up-type singlets

The module `PhyslibAlpha.Particles.StandardModel.Fermions.UpSinglet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean): 24 declarations (2 instances with no name), 22 with a docstring.

## i. Overview

> In this module we define the type corresponding to
> the target vector space of an up-type singlet quark field in the Standard Model.
>
> On this type we define a representation of the Lorentz group, and a
> representation of the Standard Model gauge group.

## ii. Key results

> - `basis` : a basis on the up singlets
> - `jetValLinEquiv` : absorbs the jet ring into the colour index: a jet of an up-type singlet is the
>   same thing as a right-handed Weyl spinor tensored with a `SpaceTimeAlgebra`-valued colour vector,
>   `SpaceTimeAlgebra ⊗[ℂ] UpSinglet ≃ RightHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3)`
> - `repJetGaugeGroupI` : the `(3, 1)_{4}` action of the jet gauge group on the jet space of the
>   up-type singlet
> - `jetValLinEquiv_smul` : the identification of the jets of the up-type singlet intertwines
>   multiplication by a scalar jet with the `SpaceTimeAlgebra`-scalar action on the colour coordinates

## iv. References

> * None.

## A. Equivalence with the underlying tensor product space

## B. The structure of a module

> The AddCommGroup and module instances are inherited from the underlying tensor product space.

## C. The basis of the up-singlet space

**`StandardModel.UpSinglet.basis`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L80).

> A basis on the up singlets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3) ℂ UpSinglet
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L84).

```lean
instance : Module.Finite ℂ UpSinglet
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L86).

```lean
instance : Module.Free ℂ UpSinglet
```

## D. Lorentz group representation

## E. The representation of the Standard Model gauge group

## F. The representation of the jet gauge group

**`StandardModel.UpSinglet.jetValLinEquiv`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L114).

> Absorbs the jet ring into the colour index: a jet of an up-type singlet is the
> same thing as a right-handed Weyl spinor tensored with a `SpaceTimeAlgebra`-valued colour
> vector,
>
>   `SpaceTimeAlgebra ⊗[ℂ] UpSinglet ≃ RightHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3)`.

```lean
noncomputable def jetValLinEquiv :
    SpaceTimeAlgebra ⊗[ℂ] UpSinglet ≃ₗ[ℂ]
      Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3)
```

**`StandardModel.UpSinglet.repJetGaugeGroupI`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L132).

> The `(3, 1)_{4}` action of the jet gauge group on the jet space of the up-type
> singlet. Through `jetValLinEquiv` the colour matrix of the gauge jet, carrying the
> `4` hypercharge phase `u ^ 4`, acts `SpaceTimeAlgebra`-linearly on the colour factor by
> matrix-vector multiplication, while the Weyl factor is untouched.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] UpSinglet)
```

**`StandardModel.UpSinglet.jetValLinEquiv_smul`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L184).

> The identification of the jets of the up-type singlet intertwines multiplication by
> a scalar jet with the `SpaceTimeAlgebra`-scalar action on the colour coordinates.

```lean
lemma jetValLinEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] UpSinglet) :
    jetValLinEquiv (χ • z)
      = Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3))
          Fermion.RightHandedWeyl
          ((LinearMap.lsmul SpaceTimeAlgebra
              (EuclideanSpace SpaceTimeAlgebra (Fin 3)) χ).restrictScalars ℂ)
          (jetValLinEquiv z)
```

**`StandardModel.UpSinglet.repJetGaugeGroupI_smul`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L219).

> **The jet gauge action on the jets of the up-type singlet is fibrewise**: it commutes
> with multiplication by scalar jets.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] UpSinglet) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

**`StandardModel.UpSinglet.repJetGaugeGroupI_ofConstant`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L249).

> On jets of constant gauge transformations the jet action reduces to the global
> gauge action on the fibre: the `(3, 1)_{4}` action on the up-singlet factor, and the
> trivial action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## G. Component transformation laws

> The basis of `UpSinglet` splits as a right-handed Weyl index and a colour index. The
> Lorentz group moves only the first, the gauge group only the second (up to the hypercharge
> scalar), so both actions are recorded as a single sum over the index they move. Dualising
> inverts and transposes the coefficient matrix, and conjugating stars it; the four
> combinations below are what a component of an up-singlet symbol needs.

**`StandardModel.UpSinglet.basis_eq_mk`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L301).

> The up-singlet basis vector as an explicit spinor–colour tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) : basis (k, c) =
    ⟨Fermion.RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c⟩
```

**`StandardModel.UpSinglet.repLorentzGroup_apply_basis`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L309).

> The Lorentz action on the up-singlet basis: the colour index is inert and the
> spinor index transforms by the entrywise conjugate matrix.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup Λ (basis j) = ∑ β, star (Λ.1 β j.1) • basis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L323).

> The up-singlet coordinate functionals transform contragrediently, by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • basis.dualBasis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L336).

> The Lorentz action on the conjugate up-singlet basis: the coefficients are the
> conjugates of those of the up-singlet action, that is, the matrix itself.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j)
      = ∑ β, Λ.1 β j.1 • (Basis.conj basis) (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L345).

> The conjugate up-singlet coordinate functionals transform by the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • (Basis.conj basis).dualBasis (β, j.2)
```

**`StandardModel.UpSinglet.repLorentzGroup_neg_one`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L358).

> **The centre of `SL(2,ℂ)` acts on the up-singlet space by `-1`**: the value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.UpSinglet.repLorentzGroup_conj_neg_one`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L368).

> The centre acts on the conjugate up-singlet space by `-1` as well: conjugation does not
> move a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

**`StandardModel.UpSinglet.repGaugeGroupI_apply_basis`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L378).

> The gauge action on the up-singlet basis: the spinor index is inert and the colour
> index transforms by the `SU(3)` matrix, scaled by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI g (basis j) =
      ∑ c, (g.toU1.1 ^ 4 * g.toSU3.1 c j.2) • basis (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L387).

> The up-singlet coordinate functionals carry the contragredient gauge action: the
> hypercharge and `SU(3)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) • basis.dualBasis (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L401).

> The gauge action on the conjugate up-singlet basis: the coefficients of the
> up-singlet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, star (g.toU1.1 ^ 4 * g.toSU3.1 c j.2) • (Basis.conj basis) (j.1, c)
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L411).

> The conjugate up-singlet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, star ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) •
        (Basis.conj basis).dualBasis (j.1, c)
```

## H. The gauge weight of the UpSinglet components

> The gauge torus acts diagonally on the basis of `UpSinglet`; the weights are recorded by
> `UpSinglet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.UpSinglet.valueGaugeWeight`**, a def, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L438).

> The gauge weight of the up-singlet basis: the colour weights and hypercharge
> `4`.

```lean
def UpSinglet.valueGaugeWeight (j : Fin 2 × Fin 3) : GaugeWeight
```

**`StandardModel.UpSinglet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L443).

> The gauge torus acts diagonally on the basis of `UpSinglet`, with the weights
> `UpSinglet.valueGaugeWeight`.

```lean
lemma UpSinglet.repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI (gaugeTorusGen i) (UpSinglet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) •
        UpSinglet.basis j
```

**`StandardModel.UpSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L463).

> The dual action of the gauge torus on the coordinate functionals of
> `UpSinglet`: the weights are negated.

```lean
lemma UpSinglet.repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI.dual (gaugeTorusGen i) (UpSinglet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i))) •
        UpSinglet.basis.coord j
```

**`StandardModel.UpSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L473).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `UpSinglet`: the two negations cancel and the weights are those of
> the value space.

```lean
lemma UpSinglet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4) (j : Fin 2 × Fin 3) :
    UpSinglet.repGaugeGroupI.conj.dual (gaugeTorusGen i) (((Basis.conj UpSinglet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) •
        ((Basis.conj UpSinglet.basis)).coord j
```

## I. The boost weight of the UpSinglet components

**`StandardModel.upSinglet_repLorentzGroup_boostAxis_two_basis`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean#L491).

> The up-singlet basis diagonalises the `z`-boost.

```lean
lemma upSinglet_repLorentzGroup_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0)
    (j : Fin 2 × Fin 3) :
    UpSinglet.repLorentzGroup (SL2C.boostAxis 2 t ht) (UpSinglet.basis j)
      = ((t : ℝ) : ℂ) ^ (weylWeight j.1) • UpSinglet.basis j
```

## Depends on

- [Up-type singlets](../../../../physlib/particles/standardmodel/fermions-upsinglet.md)
- [Gauge weight decompositions](../part-04/gaugegroup-gaugeweight.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)
- [The boost weights of a Weyl spinor](../../../relativity/fermions/weyl-boostweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/Basic.lean)
