---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet.basis, StandardModel.QuarkDoublet.colourWeakEquiv, StandardModel.QuarkDoublet.colourWeakEquiv_tmul, StandardModel.QuarkDoublet.jetValLinEquiv, StandardModel.QuarkDoublet.jetGaugeMatrix, StandardModel.QuarkDoublet.jetGaugeMatrix_one, StandardModel.QuarkDoublet.jetGaugeMatrix_mul, StandardModel.QuarkDoublet.repJetGaugeGroupI
statement: formalized
proof: formalized
---

# The type corresponding to quark doublets

The module `PhyslibAlpha.Particles.StandardModel.Fermions.QuarkDoublet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean): 30 declarations (2 instances with no name), 25 with a docstring.

## i. Overview

> In this module we define the type corresponding to
> the target vector space of a quark field in the Standard Model.
>
> On this type we define a representation of the Lorentz group, and a
> representation of the Standard Model gauge group.

## ii. Key results

> - `basis` : a basis on the quark doublets
> - `colourWeakEquiv` : the colour and weak factors of the quark doublet combined into a single
>   Euclidean factor over `Fin 3 × Fin 2`
> - `colourWeakEquiv_tmul`
> - `jetValLinEquiv`

## iv. References

> * None.

## A. Equivalence with the underlying tensor product space

## B. The structure of a module

> The AddCommGroup and module instances are inherited from the underlying tensor product space.

## C. The basis of the quark doublet space

**`StandardModel.QuarkDoublet.basis`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L77).

> A basis on the quark doublets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3 × Fin 2) ℂ QuarkDoublet
```

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L83).

```lean
instance : Module.Finite ℂ QuarkDoublet
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L85).

```lean
instance : Module.Free ℂ QuarkDoublet
```

## D. Lorentz group representation

## E. The representation of the Standard Model gauge group

## F. The representation of the jet gauge group

> The colour and weak indices are combined into the single index `Fin 3 × Fin 2`, on which
> the `SU(3)` and `SU(2)` power-series matrices of a jet of gauge transformations act
> together through their Kronecker product, scaled by the hypercharge power series `u`.

**`StandardModel.QuarkDoublet.colourWeakEquiv`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L114).

> The colour and weak factors of the quark doublet combined into a single Euclidean
> factor over `Fin 3 × Fin 2`.

```lean
noncomputable def colourWeakEquiv :
    EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2) ≃ₗ[ℂ] (Fin 3 × Fin 2 → ℂ)
```

**`StandardModel.QuarkDoublet.colourWeakEquiv_tmul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L123).

```lean
lemma colourWeakEquiv_tmul (c : EuclideanSpace ℂ (Fin 3)) (w : EuclideanSpace ℂ (Fin 2))
    (p : Fin 3 × Fin 2) :
    colourWeakEquiv (c ⊗ₜ[ℂ] w) p = c.ofLp p.1 * w.ofLp p.2
```

**`StandardModel.QuarkDoublet.jetValLinEquiv`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L136).

> Absorbs the jet ring into the combined colour–weak index: a jet of a quark doublet is
> the same thing as a left-handed Weyl spinor tensored with a `SpaceTimeAlgebra`-valued
> colour–weak vector,
>
>   `SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet ≃
>     LeftHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3 × Fin 2)`.

```lean
noncomputable def jetValLinEquiv :
    SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet ≃ₗ[ℂ]
      Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 3 × Fin 2)
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L153).

> The matrix of jets through which a jet of gauge transformations acts on the combined
> colour–weak index of the quark doublet: the Kronecker product of the `SU(3)` and `SU(2)`
> power-series matrices, scaled by the hypercharge power series `u`.

```lean
noncomputable def jetGaugeMatrix (U : JetGaugeGroupI) :
    Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) SpaceTimeAlgebra
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix_one`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L161).

```lean
lemma jetGaugeMatrix_one : jetGaugeMatrix 1 = 1
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix_mul`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L170).

```lean
lemma jetGaugeMatrix_mul (U₁ U₂ : JetGaugeGroupI) :
    jetGaugeMatrix (U₁ * U₂) = jetGaugeMatrix U₁ * jetGaugeMatrix U₂
```

**`StandardModel.QuarkDoublet.repJetGaugeGroupI`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L196).

> The `(3, 2)_{1}` action of the jet gauge group on the jet space of the quark doublet.
> Through `jetValLinEquiv` the Kronecker matrix of the gauge jet, carrying the hypercharge
> phase `u`, acts `SpaceTimeAlgebra`-linearly on the combined colour–weak factor by matrix-vector
> multiplication, while the Weyl factor is untouched.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet)
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix_ofConstant`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L221).

> The entries of the gauge matrix of a jet of a constant gauge transformation are the
> constant power series with the global gauge coefficients.

```lean
lemma jetGaugeMatrix_ofConstant (g : GaugeGroupI) (p q : Fin 3 × Fin 2) :
    jetGaugeMatrix (JetGaugeGroupI.ofConstant g) p q =
      MvPowerSeries.C ((g.toU1.1 : ℂ) * (g.toSU3.1 p.1 q.1 * g.toSU2.1 p.2 q.2))
```

**`StandardModel.QuarkDoublet.jetValLinEquiv_smul`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L238).

> The identification of the jets of the quark doublet intertwines multiplication by a
> scalar jet with the `SpaceTimeAlgebra`-scalar action on the colour–weak coordinates.

```lean
lemma jetValLinEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) :
    jetValLinEquiv (χ • z)
      = Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3 × Fin 2))
          Fermion.LeftHandedWeyl
          ((LinearMap.lsmul SpaceTimeAlgebra
            (EuclideanSpace SpaceTimeAlgebra (Fin 3 × Fin 2)) χ).restrictScalars ℂ)
          (jetValLinEquiv z)
```

**`StandardModel.QuarkDoublet.repJetGaugeGroupI_smul`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L285).

> **The jet gauge action on the jets of the quark doublet is fibrewise**: it commutes
> with multiplication by scalar jets.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

**`StandardModel.QuarkDoublet.repJetGaugeGroupI_ofConstant`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L312).

> On jets of constant gauge transformations the jet action reduces to the global gauge
> action on the fibre: the `(3, 2)_{1}` action on the quark-doublet factor, and the trivial
> action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## G. Component transformation laws

> The basis of `QuarkDoublet` splits as a left-handed Weyl index, a colour index and a
> weak-isospin index. The Lorentz group moves only the first, the gauge group only the last
> two (up to the hypercharge scalar), so each action is recorded as a sum over the indices it
> moves. Dualising inverts and transposes the coefficient matrices, and conjugating stars
> them; the four combinations below are what a component of a quark-doublet symbol needs.

**`StandardModel.QuarkDoublet.basis_eq_mk`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L377).

> The quark-doublet basis vector as an explicit spinor–colour–weak tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) (w : Fin 2) : basis (k, c, w) =
    ⟨Fermion.LeftHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c
      ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 2) ℂ w⟩
```

**`StandardModel.QuarkDoublet.repLorentzGroup_apply_basis`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L387).

> The Lorentz action on the quark-doublet basis: the colour and weak indices are inert
> and the spinor index transforms by the matrix itself.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup Λ (basis j) = ∑ β, Λ.1 β j.1 • basis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L400).

> The quark-doublet coordinate functionals transform contragrediently, by the inverse
> matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • basis.dualBasis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L413).

> The Lorentz action on the conjugate quark-doublet basis: the coefficients are the
> conjugates of those of the quark-doublet action.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j) =
      ∑ β, star (Λ.1 β j.1) • (Basis.conj basis) (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L423).

> The conjugate quark-doublet coordinate functionals transform by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • (Basis.conj basis).dualBasis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_neg_one`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L436).

> **The centre of `SL(2,ℂ)` acts on the quark-doublet space by `-1`**: the value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_neg_one`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L446).

> The centre acts on the conjugate quark-doublet space by `-1` as well: conjugation does not
> move a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_apply_basis`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L457).

> The gauge action on the quark-doublet basis: the spinor index is inert, the colour
> index transforms by the `SU(3)` matrix and the weak index by the `SU(2)` matrix, scaled
> by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI g (basis j) =
      ∑ c, ∑ w, (g.toU1.1 * g.toSU3.1 c j.2.1 * g.toSU2.1 w j.2.2) • basis (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L466).

> The quark-doublet coordinate functionals carry the contragredient gauge action: the
> hypercharge, `SU(3)` and `SU(2)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, ∑ w, ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        basis.dualBasis (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L481).

> The gauge action on the conjugate quark-doublet basis: the coefficients of the
> quark-doublet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, ∑ w, star (g.toU1.1 * g.toSU3.1 c j.2.1 * g.toSU2.1 w j.2.2) •
        (Basis.conj basis) (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L494).

> The conjugate quark-doublet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, ∑ w, star ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        (Basis.conj basis).dualBasis (j.1, c, w)
```

## H. The gauge weight of the QuarkDoublet components

> The gauge torus acts diagonally on the basis of `QuarkDoublet`; the weights are recorded by
> `QuarkDoublet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.QuarkDoublet.valueGaugeWeight`**, a def, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L521).

> The gauge weight of the quark-doublet basis: the colour and isospin weights and
> hypercharge `1`.

```lean
def QuarkDoublet.valueGaugeWeight (j : Fin 2 × Fin 3 × Fin 2) : GaugeWeight
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L526).

> The gauge torus acts diagonally on the basis of `QuarkDoublet`, with the weights
> `QuarkDoublet.valueGaugeWeight`.

```lean
lemma QuarkDoublet.repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI (gaugeTorusGen i) (QuarkDoublet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) •
        QuarkDoublet.basis j
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L548).

> The dual action of the gauge torus on the coordinate functionals of
> `QuarkDoublet`: the weights are negated.

```lean
lemma QuarkDoublet.repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4)
    (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI.dual (gaugeTorusGen i) (QuarkDoublet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i))) •
        QuarkDoublet.basis.coord j
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L559).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `QuarkDoublet`: the two negations cancel and the weights are those of
> the value space.

```lean
lemma QuarkDoublet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4)
    (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj QuarkDoublet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) •
        ((Basis.conj QuarkDoublet.basis)).coord j
```

## I. The boost weight of the QuarkDoublet components

**`StandardModel.quarkDoublet_repLorentzGroup_boostAxis_two_basis`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L581).

> The quark-doublet basis diagonalises the `z`-boost: the colour and isospin indices are
> inert.

```lean
lemma quarkDoublet_repLorentzGroup_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0)
    (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repLorentzGroup (SL2C.boostAxis 2 t ht) (QuarkDoublet.basis j)
      = ((t : ℝ) : ℂ) ^ (weylWeight j.1) • QuarkDoublet.basis j
```

## Depends on

- [The type corresponding to quark doublets](../../../../physlib/particles/standardmodel/fermions-quarkdoublet.md)
- [Gauge weight decompositions](../part-04/gaugegroup-gaugeweight.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)
- [The boost weights of a Weyl spinor](../../../relativity/fermions/weyl-boostweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean)
