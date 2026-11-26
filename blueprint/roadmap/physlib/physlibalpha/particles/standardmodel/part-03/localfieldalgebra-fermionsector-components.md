---
declaration: module
origin: cited
lean: StandardModel.FermionSector.dComponent, StandardModel.FermionSector.bardComponent, StandardModel.FermionSector.uComponent, StandardModel.FermionSector.baruComponent, StandardModel.FermionSector.QComponent, StandardModel.FermionSector.barQComponent, StandardModel.FermionSector.LComponent, StandardModel.FermionSector.barLComponent
statement: formalized
proof: formalized
---

# The components of the fermion symbols

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.Components`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean): 71 declarations, 71 with a docstring.

> The components of the ten fermion symbols on a basis of their value spaces, and their gauge and
> Lorentz transformation laws.

## i. Overview

> The fermion sector of the covariant field algebra gives the ten species as linear maps out of
> the dual of a value space. Fixing a basis of that value space turns each map into a finite
> family of elements of the covariant field algebra, the components. This file records those
> components and the transformation laws they carry.
>
> Both laws are dictated by the variance. A symbol eats a covector, so it carries the
> contragredient of its value space. Its gauge charges are the negatives of the value
> space's, entering through the matrix entries of the inverse group element, transposed. The
> barred species carry the conjugate on top of that, which stars every coefficient. On the
> Lorentz side a right-handed value space contributes the entrywise conjugate of the inverse
> matrix and a left-handed one the inverse matrix itself, with the conjugates swapping the
> two.

## ii. Key results

> - `dComponent` ... `bareComponent` : the components of the ten fermion symbols.
> - `rep_dComponent` ... `rep_bareComponent` : the gauge transformation of a component,
>   expanded over components.
> - `repLorentz_dComponent` ... `repLorentz_bareComponent` : the Lorentz transformation of a
>   component carrying no derivatives, expanded over components.
> - `repGauge_gaugeTorusGen_dComponent` ... `repGauge_gaugeTorusGen_bareComponent` : the
>   specialisation of the gauge law to the four torus generators, reproducing the weights
>   already recorded for the fermion derivative submodules.
> - `repGauge_su3_d`, `repGauge_su2_d`, `repGauge_u1_d` and their companions for the other nine
>   species : the gauge law of each component read at the colour, isospin and hypercharge
>   factors.

## iv. References

> * None.

## A. The components of the ten fermion symbols

> Each species is evaluated on the dual basis of its value space. The generation index and
> the derivative slots ride along untouched; the new index is the basis index of the value
> space, which for the barred species is that of the conjugate basis.

**`StandardModel.FermionSector.dComponent`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L88).

> The component `∇_l d_i` of the down-singlet symbol against the basis vector `j` of
> `DownSinglet`.

```lean
noncomputable def dComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.bardComponent`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L95).

> The component `∇_l bard_i` of the conjugate down-singlet symbol against the basis
> vector `j` of `ConjModule DownSinglet`.

```lean
noncomputable def bardComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.uComponent`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L102).

> The component `∇_l u_i` of the up-singlet symbol against the basis vector `j` of
> `UpSinglet`.

```lean
noncomputable def uComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.baruComponent`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L109).

> The component `∇_l baru_i` of the conjugate up-singlet symbol against the basis vector
> `j` of `ConjModule UpSinglet`.

```lean
noncomputable def baruComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.QComponent`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L116).

> The component `∇_l Q_i` of the quark-doublet symbol against the basis vector `j` of
> `QuarkDoublet`.

```lean
noncomputable def QComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.barQComponent`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L123).

> The component `∇_l barQ_i` of the conjugate quark-doublet symbol against the basis
> vector `j` of `ConjModule QuarkDoublet`.

```lean
noncomputable def barQComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.LComponent`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L130).

> The component `∇_l L_i` of the lepton-doublet symbol against the basis vector `j` of
> `LeptonDoubletV`.

```lean
noncomputable def LComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.barLComponent`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L137).

> The component `∇_l barL_i` of the conjugate lepton-doublet symbol against the basis
> vector `j` of `ConjModule LeptonDoubletV`.

```lean
noncomputable def barLComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.eComponent`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L144).

> The component `∇_l e_i` of the lepton-singlet symbol against the basis vector `j` of
> `LeptonSinglet`.

```lean
noncomputable def eComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.bareComponent`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L150).

> The component `∇_l bare_i` of the conjugate lepton-singlet symbol against the basis
> vector `j` of `ConjModule LeptonSinglet`.

```lean
noncomputable def bareComponent
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) : fieldData.LocalCovFieldAlgebra
```

## B. The gauge transformation of a component

> A symbol eats a covector, so it carries the contragredient of its value space. The gauge
> charges are the negatives of the value space's, and the coefficients are the matrix entries
> of the inverse group element with its indices transposed. The barred species carry the
> conjugate on top of that, which stars every coefficient. Colour mixes only the colour
> index, weak isospin only the isospin index, and hypercharge is an overall scalar.

**`StandardModel.FermionSector.rep_dComponent`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L168).

> The gauge transformation of a down-singlet component. The colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹`, scaled by the conjugate hypercharge factor.

```lean
lemma rep_dComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (dComponent i l j) =
      ∑ c, (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) • dComponent i l (j.1, c)
```

**`StandardModel.FermionSector.rep_bardComponent`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L177).

> The gauge transformation of a conjugate down-singlet component has the coefficients of
> the down-singlet law, conjugated.

```lean
lemma rep_bardComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (bardComponent i l j) =
      ∑ c, star (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) •
        bardComponent i l (j.1, c)
```

**`StandardModel.FermionSector.rep_uComponent`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L188).

> The gauge transformation of an up-singlet component. The colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹`, scaled by the hypercharge factor.

```lean
lemma rep_uComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (uComponent i l j) =
      ∑ c, ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) • uComponent i l (j.1, c)
```

**`StandardModel.FermionSector.rep_baruComponent`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L197).

> The gauge transformation of a conjugate up-singlet component has the coefficients of the
> up-singlet law, conjugated.

```lean
lemma rep_baruComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (baruComponent i l j) =
      ∑ c, star ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) •
        baruComponent i l (j.1, c)
```

**`StandardModel.FermionSector.rep_QComponent`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L208).

> The gauge transformation of a quark-doublet component. The colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹` and the isospin index by the transposed `SU(2)`
> matrix, scaled by the hypercharge factor.

```lean
lemma rep_QComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge g (QComponent i l j) =
      ∑ c, ∑ w, ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        QComponent i l (j.1, c, w)
```

**`StandardModel.FermionSector.rep_barQComponent`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L220).

> The gauge transformation of a conjugate quark-doublet component has the coefficients of
> the quark-doublet law, conjugated.

```lean
lemma rep_barQComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge g (barQComponent i l j) =
      ∑ c, ∑ w, star ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        barQComponent i l (j.1, c, w)
```

**`StandardModel.FermionSector.rep_LComponent`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L233).

> The gauge transformation of a lepton-doublet component. The isospin index mixes by the
> transposed `SU(2)` matrix of `g⁻¹`, scaled by the conjugate hypercharge factor.

```lean
lemma rep_LComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge g (LComponent i l j) =
      ∑ w, (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) • LComponent i l (j.1, w)
```

**`StandardModel.FermionSector.rep_barLComponent`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L242).

> The gauge transformation of a conjugate lepton-doublet component has the coefficients of
> the lepton-doublet law, conjugated.

```lean
lemma rep_barLComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge g (barLComponent i l j) =
      ∑ w, star (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) •
        barLComponent i l (j.1, w)
```

**`StandardModel.FermionSector.rep_eComponent`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L253).

> The gauge transformation of a lepton-singlet component. Colour and isospin act
> trivially, so the sum over components collapses to the conjugate hypercharge scalar.

```lean
lemma rep_eComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge g (eComponent i l j) =
      (star (g⁻¹).toU1.1 ^ 6 : ℂ) • eComponent i l j
```

**`StandardModel.FermionSector.rep_bareComponent`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L261).

> The gauge transformation of a conjugate lepton-singlet component has the scalar of the
> lepton-singlet law, conjugated.

```lean
lemma rep_bareComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge g (bareComponent i l j) =
      star (star (g⁻¹).toU1.1 ^ 6 : ℂ) • bareComponent i l j
```

## C. The Lorentz transformation of a component

> A tower with `n` covariant derivatives mixes into every assignment of `n` derivative
> directions, so its Lorentz law is a sum over such assignments. At `n = 0` there is exactly
> one assignment and the product of Lorentz factors is empty, leaving only the action on the
> value index. That is the case recorded here. A right-handed value space contributes the
> entrywise conjugate of the inverse matrix and a left-handed one the inverse matrix itself,
> with the conjugate species swapping the two.

**`StandardModel.FermionSector.univ_derivIndex_zero`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L283).

> At zero covariant derivatives the assignments of derivative directions form a
> one-element type, so the Lorentz law of a tower has a single term.

```lean
lemma univ_derivIndex_zero (l : Fin 0 → Fin 1 ⊕ Fin 3) :
    (Finset.univ : Finset (Fin 0 → Fin 1 ⊕ Fin 3)) = {l}
```

**`StandardModel.FermionSector.repLorentz_dComponent`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L290).

> The Lorentz transformation of a down-singlet component carrying no derivatives. The
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_dComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (dComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • dComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_bardComponent`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L302).

> The Lorentz transformation of a conjugate down-singlet component carrying no
> derivatives has the coefficients of the down-singlet law, conjugated.

```lean
lemma repLorentz_bardComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (bardComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • bardComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_uComponent`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L314).

> The Lorentz transformation of an up-singlet component carrying no derivatives. The
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_uComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (uComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • uComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_baruComponent`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L326).

> The Lorentz transformation of a conjugate up-singlet component carrying no
> derivatives has the coefficients of the up-singlet law, conjugated.

```lean
lemma repLorentz_baruComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (baruComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • baruComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_QComponent`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L338).

> The Lorentz transformation of a quark-doublet component carrying no derivatives. The
> left-handed spinor index transforms by the inverse matrix.

```lean
lemma repLorentz_QComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentz Λ (QComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • QComponent i l (β, j.2.1, j.2.2)
```

**`StandardModel.FermionSector.repLorentz_barQComponent`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L350).

> The Lorentz transformation of a conjugate quark-doublet component carrying no
> derivatives has the coefficients of the quark-doublet law, conjugated.

```lean
lemma repLorentz_barQComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentz Λ (barQComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • barQComponent i l (β, j.2.1, j.2.2)
```

**`StandardModel.FermionSector.repLorentz_LComponent`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L362).

> The Lorentz transformation of a lepton-doublet component carrying no derivatives. The
> left-handed spinor index transforms by the inverse matrix.

```lean
lemma repLorentz_LComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repLorentz Λ (LComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • LComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_barLComponent`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L374).

> The Lorentz transformation of a conjugate lepton-doublet component carrying no
> derivatives has the coefficients of the lepton-doublet law, conjugated.

```lean
lemma repLorentz_barLComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repLorentz Λ (barLComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • barLComponent i l (β, j.2)
```

**`StandardModel.FermionSector.repLorentz_eComponent`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L386).

> The Lorentz transformation of a lepton-singlet component carrying no derivatives. The
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_eComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    repLorentz Λ (eComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j β) • eComponent i l β
```

**`StandardModel.FermionSector.repLorentz_bareComponent`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L398).

> The Lorentz transformation of a conjugate lepton-singlet component carrying no
> derivatives has the coefficients of the lepton-singlet law, conjugated.

```lean
lemma repLorentz_bareComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    repLorentz Λ (bareComponent i l j) =
      ∑ β, (Λ⁻¹).1 j β • bareComponent i l β
```

## D. The torus specialisation and the recorded gauge weights

> Restricting the gauge law of section B to the four torus generators must return the gauge
> weights already recorded for the fermion derivative submodules, the negative of the value
> space's weight for an unbarred species, and the value space's own weight for a barred one.
> The lemmas below derive exactly those weights from the full-group laws, so the variance of
> section B and the weight bookkeeping of the derivative submodules agree.

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_dComponent`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L421).

> The `d` components carry the negative of the down-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_dComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (dComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(DownSinglet.valueGaugeWeight j)) t) •
        dComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_bardComponent`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L435).

> The `bard` components carry the down-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_bardComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (bardComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) t) •
        bardComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_uComponent`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L449).

> The `u` components carry the negative of the up-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_uComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (uComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(UpSinglet.valueGaugeWeight j)) t) •
        uComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_baruComponent`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L463).

> The `baru` components carry the up-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_baruComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (baruComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) t) •
        baruComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_QComponent`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L477).

> The `Q` components carry the negative of the quark-doublet weight.

```lean
lemma repGauge_gaugeTorusGen_QComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen t) (QComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(QuarkDoublet.valueGaugeWeight j)) t) •
        QComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_barQComponent`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L491).

> The `barQ` components carry the quark-doublet weight itself.

```lean
lemma repGauge_gaugeTorusGen_barQComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen t) (barQComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) t) •
        barQComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_LComponent`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L505).

> The `L` components carry the negative of the lepton-doublet weight.

```lean
lemma repGauge_gaugeTorusGen_LComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen t) (LComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonDoubletV.valueGaugeWeight j)) t) •
        LComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_barLComponent`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L518).

> The `barL` components carry the lepton-doublet weight itself.

```lean
lemma repGauge_gaugeTorusGen_barLComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen t) (barLComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) t) •
        barLComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_eComponent`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L532).

> The `e` components carry the negative of the lepton-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_eComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen t) (eComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonSinglet.valueGaugeWeight j)) t) •
        eComponent i l j
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_bareComponent`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L543).

> The `bare` components carry the lepton-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_bareComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen t) (bareComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) t) •
        bareComponent i l j
```

## E. The gauge laws of the components at each factor

> A gauge transformation is a triple, and each of the three index laws that classify a block
> constrains one factor of it. So each of the ten symbols is read at each factor in turn:
> colour moves only a colour index, isospin only an isospin index, and hypercharge is an
> overall scalar whose power is the `6Y` of the species. A symbol eats a covector, so it
> carries the contragredient of its value space. The unbarred species come out
> anti-fundamental in colour and isospin and the barred ones fundamental, which is what makes
> every conjugate pair a fundamental against an anti-fundamental.

### E.1. The down singlet

**`StandardModel.FermionSector.repGauge_su3_d`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L577).

> A colour transformation moves the colour index of a down-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_d (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (dComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • dComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_su2_d`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L587).

> An isospin transformation fixes a down-singlet symbol, which carries no isospin.

```lean
lemma repGauge_su2_d (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (dComponent f l j)
      = dComponent f l j
```

**`StandardModel.FermionSector.repGauge_u1_d`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L596).

> A hypercharge transformation scales a down-singlet symbol by the square of the scalar,
> the down singlet carrying `6Y = 2`.

```lean
lemma repGauge_u1_d (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (dComponent f l j)
      = (t : ℂ) ^ 2 • dComponent f l j
```

### E.2. The conjugate down singlet

**`StandardModel.FermionSector.repGauge_su3_bard`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L611).

> A colour transformation moves the colour index of a conjugate down-singlet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_bard (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (bardComponent f l (s, c))
      = ∑ a, U.1 a c • bardComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_su2_bard`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L621).

> An isospin transformation fixes a conjugate down-singlet symbol.

```lean
lemma repGauge_su2_bard (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (bardComponent f l j)
      = bardComponent f l j
```

**`StandardModel.FermionSector.repGauge_u1_bard`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L630).

> A hypercharge transformation scales a conjugate down-singlet symbol by the square of
> the conjugate scalar, the conjugate down singlet carrying `6Y = -2`.

```lean
lemma repGauge_u1_bard (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (bardComponent f l j)
      = (star (t : ℂ)) ^ 2 • bardComponent f l j
```

### E.3. The up singlet

**`StandardModel.FermionSector.repGauge_su3_u`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L645).

> A colour transformation moves the colour index of an up-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_u (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (uComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • uComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_su2_u`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L655).

> An isospin transformation fixes an up-singlet symbol.

```lean
lemma repGauge_su2_u (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (uComponent f l j)
      = uComponent f l j
```

**`StandardModel.FermionSector.repGauge_u1_u`**, a lemma, [line 664](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L664).

> A hypercharge transformation scales an up-singlet symbol by the fourth power of the
> conjugate scalar, the up singlet carrying `6Y = -4`.

```lean
lemma repGauge_u1_u (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (uComponent f l j)
      = (star (t : ℂ)) ^ 4 • uComponent f l j
```

### E.4. The conjugate up singlet

**`StandardModel.FermionSector.repGauge_su3_baru`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L679).

> A colour transformation moves the colour index of a conjugate up-singlet symbol by the
> matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_baru (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (baruComponent f l (s, c))
      = ∑ a, U.1 a c • baruComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_su2_baru`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L689).

> An isospin transformation fixes a conjugate up-singlet symbol.

```lean
lemma repGauge_su2_baru (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (baruComponent f l j)
      = baruComponent f l j
```

**`StandardModel.FermionSector.repGauge_u1_baru`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L698).

> A hypercharge transformation scales a conjugate up-singlet symbol by the fourth power
> of the scalar, the conjugate up singlet carrying `6Y = 4`.

```lean
lemma repGauge_u1_baru (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (baruComponent f l j)
      = (t : ℂ) ^ 4 • baruComponent f l j
```

### E.5. The quark doublet

**`StandardModel.FermionSector.repGauge_su3_Q`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L713).

> A colour transformation moves the colour index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_Q (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (QComponent f l (s, c, w))
      = ∑ a, conj (U.1 a c) • QComponent f l (s, a, w)
```

**`StandardModel.FermionSector.repGauge_su2_Q`**, a lemma, [line 724](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L724).

> An isospin transformation moves the isospin index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_Q (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (QComponent f l (s, c, w))
      = ∑ a, conj (V.1 a w) • QComponent f l (s, c, a)
```

**`StandardModel.FermionSector.repGauge_u1_Q`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L735).

> A hypercharge transformation scales a quark-doublet symbol by the conjugate scalar,
> the quark doublet carrying `6Y = -1`.

```lean
lemma repGauge_u1_Q (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (QComponent f l (s, c, w))
      = star (t : ℂ) • QComponent f l (s, c, w)
```

### E.6. The conjugate quark doublet

**`StandardModel.FermionSector.repGauge_su3_barQ`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L750).

> A colour transformation moves the colour index of a conjugate quark-doublet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_barQ (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (barQComponent f l (s, c, w))
      = ∑ a, U.1 a c • barQComponent f l (s, a, w)
```

**`StandardModel.FermionSector.repGauge_su2_barQ`**, a lemma, [line 762](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L762).

> An isospin transformation moves the isospin index of a conjugate quark-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barQ (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (barQComponent f l (s, c, w))
      = ∑ a, V.1 a w • barQComponent f l (s, c, a)
```

**`StandardModel.FermionSector.repGauge_u1_barQ`**, a lemma, [line 773](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L773).

> A hypercharge transformation scales a conjugate quark-doublet symbol by the scalar,
> the conjugate quark doublet carrying `6Y = 1`.

```lean
lemma repGauge_u1_barQ (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (barQComponent f l (s, c, w))
      = (t : ℂ) • barQComponent f l (s, c, w)
```

### E.7. The lepton doublet

**`StandardModel.FermionSector.repGauge_su3_L`**, a lemma, [line 788](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L788).

> A colour transformation fixes a lepton-doublet symbol, which carries no colour.

```lean
lemma repGauge_su3_L (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (LComponent f l j)
      = LComponent f l j
```

**`StandardModel.FermionSector.repGauge_su2_L`**, a lemma, [line 797](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L797).

> An isospin transformation moves the isospin index of a lepton-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_L (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (LComponent f l (s, w))
      = ∑ a, conj (V.1 a w) • LComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_u1_L`**, a lemma, [line 808](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L808).

> A hypercharge transformation scales a lepton-doublet symbol by the cube of the scalar,
> the lepton doublet carrying `6Y = 3`.

```lean
lemma repGauge_u1_L (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (LComponent f l j)
      = (t : ℂ) ^ 3 • LComponent f l j
```

### E.8. The conjugate lepton doublet

**`StandardModel.FermionSector.repGauge_su3_barL`**, a lemma, [line 823](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L823).

> A colour transformation fixes a conjugate lepton-doublet symbol, which carries no
> colour.

```lean
lemma repGauge_su3_barL (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (barLComponent f l j)
      = barLComponent f l j
```

**`StandardModel.FermionSector.repGauge_su2_barL`**, a lemma, [line 832](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L832).

> An isospin transformation moves the isospin index of a conjugate lepton-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barL (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (barLComponent f l (s, w))
      = ∑ a, V.1 a w • barLComponent f l (s, a)
```

**`StandardModel.FermionSector.repGauge_u1_barL`**, a lemma, [line 843](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L843).

> A hypercharge transformation scales a conjugate lepton-doublet symbol by the cube of
> the conjugate scalar, the conjugate lepton doublet carrying `6Y = -3`.

```lean
lemma repGauge_u1_barL (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (barLComponent f l (s, w))
      = (star (t : ℂ)) ^ 3 • barLComponent f l (s, w)
```

### E.9. The lepton singlet

**`StandardModel.FermionSector.repGauge_su3_e`**, a lemma, [line 858](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L858).

> A colour transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su3_e (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (eComponent f l s)
      = eComponent f l s
```

**`StandardModel.FermionSector.repGauge_su2_e`**, a lemma, [line 866](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L866).

> An isospin transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su2_e (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (eComponent f l s)
      = eComponent f l s
```

**`StandardModel.FermionSector.repGauge_u1_e`**, a lemma, [line 875](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L875).

> A hypercharge transformation scales a lepton-singlet symbol by the sixth power of the
> scalar, the lepton singlet carrying `6Y = 6`.

```lean
lemma repGauge_u1_e (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (eComponent f l s)
      = (t : ℂ) ^ 6 • eComponent f l s
```

### E.10. The conjugate lepton singlet

**`StandardModel.FermionSector.repGauge_su3_bare`**, a lemma, [line 889](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L889).

> A colour transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su3_bare (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (bareComponent f l s)
      = bareComponent f l s
```

**`StandardModel.FermionSector.repGauge_su2_bare`**, a lemma, [line 897](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L897).

> An isospin transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su2_bare (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (bareComponent f l s)
      = bareComponent f l s
```

**`StandardModel.FermionSector.repGauge_u1_bare`**, a lemma, [line 906](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean#L906).

> A hypercharge transformation scales a conjugate lepton-singlet symbol by the sixth
> power of the conjugate scalar, the conjugate lepton singlet carrying `6Y = -6`.

```lean
lemma repGauge_u1_bare (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (bareComponent f l s)
      = (star (t : ℂ)) ^ 6 • bareComponent f l s
```

## Depends on

- [The fermion sector](../part-02/localfieldalgebra-fermionsector-basic.md)

## Proof depends on

- [A cube root of unity and the factors of a gauge transformation](../part-02/gaugegroup-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Components.lean)
