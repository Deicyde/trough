---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet.colourWeakEquiv, StandardModel.QuarkDoublet.colourWeakEquiv_tmul, StandardModel.QuarkDoublet.basis, StandardModel.QuarkDoublet.basis_eq_mk, StandardModel.QuarkDoublet.repLorentzGroup_apply_basis, StandardModel.QuarkDoublet.repLorentzGroup_dual_dualBasis, StandardModel.QuarkDoublet.repLorentzGroup_conj_apply_basis, StandardModel.QuarkDoublet.repLorentzGroup_conj_dual_dualBasis
statement: formalized
proof: formalized
---

# Quark doublets

The module `PhyslibAlpha.Particles.StandardModel.Fermions.QuarkDoublet.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean): 20 declarations (2 instances with no name), 20 with a docstring.

> The basis of the quark doublet `(3, 2)_{1}`, its Lorentz and gauge actions on components, and
> the gauge weights of the components.

## i. Overview

> The Standard Model quark doublet is a left-handed Weyl spinor in the `(3, 2)_{1}`
> representation. Here charges are normalized as `6Y`, so `1` is the usual hypercharge
> `Y = 1/6`. Its value space `QuarkDoublet`, the Lorentz action `QuarkDoublet.repLorentzGroup`
> and the gauge action `QuarkDoublet.repGaugeGroupI` are in
> `Physlib.Particles.StandardModel.Fermions.QuarkDoublet`. The Weyl factor carries the Lorentz
> index, and the colour and weak-isospin factors the internal indices.
>
> The colour and weak indices are combined into the single index `Fin 3 × Fin 2` by
> `QuarkDoublet.colourWeakEquiv`, on which a gauge transformation acts through the Kronecker
> product of its `SU(3)` and `SU(2)` matrices. This file then writes both actions on the basis of
> spinor–colour–weak tensors, together with their dual, conjugate and conjugate-dual forms, which
> are what a component of a quark-doublet symbol needs. The centre `-1` of `SL(2,ℂ)` acts by
> `-1`, as on any single Weyl-spinor index. The gauge torus acts diagonally on the basis, with the
> colour and isospin weights and hypercharge `1`.

## ii. Key results

> - `StandardModel.QuarkDoublet.colourWeakEquiv` : the colour and weak factors combined into a
>   single factor over `Fin 3 × Fin 2`.
> - `StandardModel.QuarkDoublet.basis` : the basis of spinor–colour–weak tensors.
> - `StandardModel.QuarkDoublet.repLorentzGroup_apply_basis`,
>   `StandardModel.QuarkDoublet.repGaugeGroupI_apply_basis` : the Lorentz and gauge actions on
>   the basis, with their dual and conjugate forms.
> - `StandardModel.QuarkDoublet.repLorentzGroup_neg_one` : the centre of `SL(2,ℂ)` acts by `-1`.
> - `StandardModel.QuarkDoublet.valueGaugeWeight` : the gauge weights of the basis, with
>   `StandardModel.QuarkDoublet.repGaugeGroupI_gaugeTorusGen_basis`.

## iv. References

> * None.

## A. The combined colour and weak index

> The colour and weak indices are combined into the single index `Fin 3 × Fin 2`, on which
> the `SU(3)` and `SU(2)` matrices of a gauge transformation act together through their
> Kronecker product, scaled by the hypercharge phase.

**`StandardModel.QuarkDoublet.colourWeakEquiv`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L83).

> The colour and weak factors of the quark doublet combined into a single Euclidean
> factor over `Fin 3 × Fin 2`.

```lean
noncomputable def colourWeakEquiv :
    EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2) ≃ₗ[ℂ] (Fin 3 × Fin 2 → ℂ)
```

**`StandardModel.QuarkDoublet.colourWeakEquiv_tmul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L93).

> The combined index of a pure colour–weak tensor is the product of its components.

```lean
lemma colourWeakEquiv_tmul (c : EuclideanSpace ℂ (Fin 3)) (w : EuclideanSpace ℂ (Fin 2))
    (p : Fin 3 × Fin 2) :
    colourWeakEquiv (c ⊗ₜ[ℂ] w) p = c.ofLp p.1 * w.ofLp p.2
```

## B. The basis

> The basis of `QuarkDoublet` is the tensor product of the left-handed Weyl basis and the
> standard colour and weak bases.

**`StandardModel.QuarkDoublet.basis`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L108).

> A basis on the quark doublets.

```lean
noncomputable def basis : Module.Basis (Fin 2 × Fin 3 × Fin 2) ℂ QuarkDoublet
```

**An instance with no name**, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L115).

> The quark-doublet space is finite-dimensional.

```lean
instance : Module.Finite ℂ QuarkDoublet
```

**An instance with no name**, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L118).

> The quark-doublet space is free.

```lean
instance : Module.Free ℂ QuarkDoublet
```

**`StandardModel.QuarkDoublet.basis_eq_mk`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L121).

> The quark-doublet basis vector as an explicit spinor–colour–weak tensor.

```lean
lemma basis_eq_mk (k : Fin 2) (c : Fin 3) (w : Fin 2) : basis (k, c, w) =
    ⟨Fermion.LeftHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ c
      ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 2) ℂ w⟩
```

## C. The Lorentz action on components

> The Lorentz group moves only the spinor index. Dualising inverts and transposes the coefficient
> matrix, and conjugating stars it.

**`StandardModel.QuarkDoublet.repLorentzGroup_apply_basis`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L140).

> The Lorentz action on the quark-doublet basis. The colour and weak indices are inert
> and the spinor index transforms by the matrix itself.

```lean
lemma repLorentzGroup_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup Λ (basis j) = ∑ β, Λ.1 β j.1 • basis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_dual_dualBasis`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L153).

> The quark-doublet coordinate functionals transform contragrediently, by the inverse
> matrix.

```lean
lemma repLorentzGroup_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.dual Λ (basis.dualBasis j) =
      ∑ β, (Λ⁻¹).1 j.1 β • basis.dualBasis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_apply_basis`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L166).

> The Lorentz action on the conjugate quark-doublet basis. The coefficients are the
> conjugates of those of the quark-doublet action.

```lean
lemma repLorentzGroup_conj_apply_basis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.conj Λ ((Basis.conj basis) j) =
      ∑ β, star (Λ.1 β j.1) • (Basis.conj basis) (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_dual_dualBasis`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L176).

> The conjugate quark-doublet coordinate functionals transform by the entrywise
> conjugate of the inverse matrix.

```lean
lemma repLorentzGroup_conj_dual_dualBasis (Λ : SL(2,ℂ)) (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentzGroup.conj.dual Λ ((Basis.conj basis).dualBasis j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • (Basis.conj basis).dualBasis (β, j.2.1, j.2.2)
```

**`StandardModel.QuarkDoublet.repLorentzGroup_neg_one`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L189).

> The centre of `SL(2,ℂ)` acts on the quark-doublet space by `-1`. The value space carries a
> single Weyl-spinor index, and `-1` is not the identity on a half-integer spin.

```lean
lemma repLorentzGroup_neg_one : repLorentzGroup (-1) = -LinearMap.id
```

**`StandardModel.QuarkDoublet.repLorentzGroup_conj_neg_one`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L199).

> The centre acts on the conjugate quark-doublet space by `-1` as well, conjugation not
> moving a real sign.

```lean
lemma repLorentzGroup_conj_neg_one : repLorentzGroup.conj (-1) = -LinearMap.id
```

## D. The gauge action on components

> The gauge group moves only the colour and weak indices, up to the hypercharge scalar.

**`StandardModel.QuarkDoublet.repGaugeGroupI_apply_basis`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L218).

> The gauge action on the quark-doublet basis. The spinor index is inert, the colour
> index transforms by the `SU(3)` matrix and the weak index by the `SU(2)` matrix, scaled
> by the hypercharge factor.

```lean
lemma repGaugeGroupI_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI g (basis j) =
      ∑ c, ∑ w, (g.toU1.1 * g.toSU3.1 c j.2.1 * g.toSU2.1 w j.2.2) • basis (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_dual_dualBasis`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L227).

> The quark-doublet coordinate functionals carry the contragredient gauge action, by the
> hypercharge, `SU(3)` and `SU(2)` factors of the inverse group element, transposed.

```lean
lemma repGaugeGroupI_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.dual g (basis.dualBasis j) =
      ∑ c, ∑ w, ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        basis.dualBasis (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_apply_basis`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L242).

> The gauge action on the conjugate quark-doublet basis has the coefficients of the
> quark-doublet action, conjugated.

```lean
lemma repGaugeGroupI_conj_apply_basis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.conj g ((Basis.conj basis) j) =
      ∑ c, ∑ w, star (g.toU1.1 * g.toSU3.1 c j.2.1 * g.toSU2.1 w j.2.2) •
        (Basis.conj basis) (j.1, c, w)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_dual_dualBasis`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L255).

> The conjugate quark-doublet coordinate functionals carry the conjugate of the
> contragredient gauge action.

```lean
lemma repGaugeGroupI_conj_dual_dualBasis (g : GaugeGroupI) (j : Fin 2 × Fin 3 × Fin 2) :
    repGaugeGroupI.conj.dual g ((Basis.conj basis).dualBasis j) =
      ∑ c, ∑ w, star ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        (Basis.conj basis).dualBasis (j.1, c, w)
```

## E. The gauge weights of the components

> The gauge torus acts diagonally on the basis of `QuarkDoublet`. The weights are recorded by
> `QuarkDoublet.valueGaugeWeight`, and pass to the dual and conjugate-dual coordinate
> functionals with the expected signs.

**`StandardModel.QuarkDoublet.valueGaugeWeight`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L280).

> The gauge weight of the quark-doublet basis, colour and isospin weights and
> hypercharge `1`.

```lean
def valueGaugeWeight (j : Fin 2 × Fin 3 × Fin 2) : GaugeWeight
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_gaugeTorusGen_basis`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L285).

> The gauge torus acts diagonally on the basis of `QuarkDoublet`, with the weights
> `QuarkDoublet.valueGaugeWeight`.

```lean
lemma repGaugeGroupI_gaugeTorusGen_basis (i : Fin 4) (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI (gaugeTorusGen i) (QuarkDoublet.basis j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) •
        QuarkDoublet.basis j
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_dual_gaugeTorusGen_coord`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L300).

> The dual action of the gauge torus on the coordinate functionals of
> `QuarkDoublet` negates the weights.

```lean
lemma repGaugeGroupI_dual_gaugeTorusGen_coord (i : Fin 4)
    (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI.dual (gaugeTorusGen i) (QuarkDoublet.basis.coord j)
      = ((expI : ℂ) ^ (-(GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i))) •
        QuarkDoublet.basis.coord j
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_conj_dual_gaugeTorusGen_coord`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean#L311).

> The dual of the conjugate action of the gauge torus on the coordinate functionals
> of the conjugate of `QuarkDoublet`. The two negations cancel and the weights are those of
> the value space.

```lean
lemma repGaugeGroupI_conj_dual_gaugeTorusGen_coord (i : Fin 4)
    (j : Fin 2 × Fin 3 × Fin 2) :
    QuarkDoublet.repGaugeGroupI.conj.dual (gaugeTorusGen i)
      (((Basis.conj QuarkDoublet.basis)).coord j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) •
        ((Basis.conj QuarkDoublet.basis)).coord j
```

## Depends on

- [The type corresponding to quark doublets](../../../../physlib/particles/standardmodel/fermions-quarkdoublet.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Proof depends on

- [Dual representations on a dual basis](../../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/Basic.lean)
