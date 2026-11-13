---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.dComponent, StandardModel.IsFermionSector.bardComponent, StandardModel.IsFermionSector.uComponent, StandardModel.IsFermionSector.baruComponent, StandardModel.IsFermionSector.QComponent, StandardModel.IsFermionSector.barQComponent, StandardModel.IsFermionSector.LComponent, StandardModel.IsFermionSector.barLComponent
statement: formalized
proof: formalized
---

# The components of the fermion symbols

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.Components`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean): 44 declarations, 44 with a docstring.

## i. Overview

> A fermion sector gives the ten species as linear maps out of the dual of a value space.
> Fixing a basis of that value space turns each map into a finite family of elements of `B`:
> the components. This file records those components and the transformation laws they carry.
>
> Both laws are dictated by the variance. A symbol eats a covector, so it carries the
> contragredient of its value space: its gauge charges are the negatives of the value
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

## iv. References

> * None.

## A. The components of the ten fermion symbols

> Each species is evaluated on the dual basis of its value space. The generation index and
> the derivative slots ride along untouched; the new index is the basis index of the value
> space, which for the barred species is that of the conjugate basis.

**`StandardModel.IsFermionSector.dComponent`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L100).

> The component `∇_l d_i` of the down-singlet symbol against the basis vector `j` of
> `DownSinglet`.

```lean
noncomputable def dComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) : B
```

**`StandardModel.IsFermionSector.bardComponent`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L109).

> The component `∇_l bard_i` of the conjugate down-singlet symbol against the basis
> vector `j` of `ConjModule DownSinglet`.

```lean
noncomputable def bardComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) : B
```

**`StandardModel.IsFermionSector.uComponent`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L118).

> The component `∇_l u_i` of the up-singlet symbol against the basis vector `j` of
> `UpSinglet`.

```lean
noncomputable def uComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) : B
```

**`StandardModel.IsFermionSector.baruComponent`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L127).

> The component `∇_l baru_i` of the conjugate up-singlet symbol against the basis vector
> `j` of `ConjModule UpSinglet`.

```lean
noncomputable def baruComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) : B
```

**`StandardModel.IsFermionSector.QComponent`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L136).

> The component `∇_l Q_i` of the quark-doublet symbol against the basis vector `j` of
> `QuarkDoublet`.

```lean
noncomputable def QComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) : B
```

**`StandardModel.IsFermionSector.barQComponent`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L145).

> The component `∇_l barQ_i` of the conjugate quark-doublet symbol against the basis
> vector `j` of `ConjModule QuarkDoublet`.

```lean
noncomputable def barQComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) : B
```

**`StandardModel.IsFermionSector.LComponent`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L154).

> The component `∇_l L_i` of the lepton-doublet symbol against the basis vector `j` of
> `LeptonDoubletV`.

```lean
noncomputable def LComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) : B
```

**`StandardModel.IsFermionSector.barLComponent`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L163).

> The component `∇_l barL_i` of the conjugate lepton-doublet symbol against the basis
> vector `j` of `ConjModule LeptonDoubletV`.

```lean
noncomputable def barLComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) : B
```

**`StandardModel.IsFermionSector.eComponent`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L172).

> The component `∇_l e_i` of the lepton-singlet symbol against the basis vector `j` of
> `LeptonSinglet`.

```lean
noncomputable def eComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) : B
```

**`StandardModel.IsFermionSector.bareComponent`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L181).

> The component `∇_l bare_i` of the conjugate lepton-singlet symbol against the basis
> vector `j` of `ConjModule LeptonSinglet`.

```lean
noncomputable def bareComponent (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) : B
```

## B. The gauge transformation of a component

> A symbol eats a covector, so it carries the contragredient of its value space: the gauge
> charges are the negatives of the value space's, and the coefficients are the matrix entries
> of the inverse group element with its indices transposed. The barred species carry the
> conjugate on top of that, which stars every coefficient. Colour mixes only the colour
> index, weak isospin only the isospin index, and hypercharge is an overall scalar.

**`StandardModel.IsFermionSector.rep_dComponent`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L200).

> The gauge transformation of a down-singlet component: the colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹`, scaled by the conjugate hypercharge factor.

```lean
lemma rep_dComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (h.dComponent i l j) =
      ∑ c, (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) • h.dComponent i l (j.1, c)
```

**`StandardModel.IsFermionSector.rep_bardComponent`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L209).

> The gauge transformation of a conjugate down-singlet component: the coefficients of
> the down-singlet law, conjugated.

```lean
lemma rep_bardComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (h.bardComponent i l j) =
      ∑ c, star (star (g⁻¹).toU1.1 ^ 2 * (g⁻¹).toSU3.1 j.2 c) •
        h.bardComponent i l (j.1, c)
```

**`StandardModel.IsFermionSector.rep_uComponent`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L220).

> The gauge transformation of an up-singlet component: the colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹`, scaled by the hypercharge factor.

```lean
lemma rep_uComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (h.uComponent i l j) =
      ∑ c, ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) • h.uComponent i l (j.1, c)
```

**`StandardModel.IsFermionSector.rep_baruComponent`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L229).

> The gauge transformation of a conjugate up-singlet component: the coefficients of the
> up-singlet law, conjugated.

```lean
lemma rep_baruComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge g (h.baruComponent i l j) =
      ∑ c, star ((g⁻¹).toU1.1 ^ 4 * (g⁻¹).toSU3.1 j.2 c) •
        h.baruComponent i l (j.1, c)
```

**`StandardModel.IsFermionSector.rep_QComponent`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L240).

> The gauge transformation of a quark-doublet component: the colour index mixes by the
> transposed `SU(3)` matrix of `g⁻¹` and the isospin index by the transposed `SU(2)`
> matrix, scaled by the hypercharge factor.

```lean
lemma rep_QComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge g (h.QComponent i l j) =
      ∑ c, ∑ w, ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        h.QComponent i l (j.1, c, w)
```

**`StandardModel.IsFermionSector.rep_barQComponent`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L252).

> The gauge transformation of a conjugate quark-doublet component: the coefficients of
> the quark-doublet law, conjugated.

```lean
lemma rep_barQComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge g (h.barQComponent i l j) =
      ∑ c, ∑ w, star ((g⁻¹).toU1.1 * (g⁻¹).toSU3.1 j.2.1 c * (g⁻¹).toSU2.1 j.2.2 w) •
        h.barQComponent i l (j.1, c, w)
```

**`StandardModel.IsFermionSector.rep_LComponent`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L265).

> The gauge transformation of a lepton-doublet component: the isospin index mixes by the
> transposed `SU(2)` matrix of `g⁻¹`, scaled by the conjugate hypercharge factor.

```lean
lemma rep_LComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge g (h.LComponent i l j) =
      ∑ w, (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) • h.LComponent i l (j.1, w)
```

**`StandardModel.IsFermionSector.rep_barLComponent`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L274).

> The gauge transformation of a conjugate lepton-doublet component: the coefficients of
> the lepton-doublet law, conjugated.

```lean
lemma rep_barLComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge g (h.barLComponent i l j) =
      ∑ w, star (star (g⁻¹).toU1.1 ^ 3 * (g⁻¹).toSU2.1 j.2 w) •
        h.barLComponent i l (j.1, w)
```

**`StandardModel.IsFermionSector.rep_eComponent`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L285).

> The gauge transformation of a lepton-singlet component: colour and isospin act
> trivially, so the sum over components collapses to the conjugate hypercharge scalar.

```lean
lemma rep_eComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge g (h.eComponent i l j) =
      (star (g⁻¹).toU1.1 ^ 6 : ℂ) • h.eComponent i l j
```

**`StandardModel.IsFermionSector.rep_bareComponent`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L293).

> The gauge transformation of a conjugate lepton-singlet component: the scalar of the
> lepton-singlet law, conjugated.

```lean
lemma rep_bareComponent (g : GaugeGroupI) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge g (h.bareComponent i l j) =
      star (star (g⁻¹).toU1.1 ^ 6 : ℂ) • h.bareComponent i l j
```

## C. The Lorentz transformation of a component

> A tower with `n` covariant derivatives mixes into every assignment of `n` derivative
> directions, so its Lorentz law is a sum over such assignments. At `n = 0` there is exactly
> one assignment and the product of Lorentz factors is empty, leaving only the action on the
> value index. That is the case recorded here: a right-handed value space contributes the
> entrywise conjugate of the inverse matrix and a left-handed one the inverse matrix itself,
> with the conjugate species swapping the two.

**`StandardModel.IsFermionSector.univ_derivIndex_zero`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L315).

> At zero covariant derivatives the assignments of derivative directions form a
> one-element type, so the Lorentz law of a tower has a single term.

```lean
lemma univ_derivIndex_zero (l : Fin 0 → Fin 1 ⊕ Fin 3) :
    (Finset.univ : Finset (Fin 0 → Fin 1 ⊕ Fin 3)) = {l}
```

**`StandardModel.IsFermionSector.repLorentz_dComponent`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L322).

> The Lorentz transformation of a down-singlet component carrying no derivatives: the
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_dComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (h.dComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • h.dComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_bardComponent`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L334).

> The Lorentz transformation of a conjugate down-singlet component carrying no
> derivatives: the coefficients of the down-singlet law, conjugated.

```lean
lemma repLorentz_bardComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (h.bardComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • h.bardComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_uComponent`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L346).

> The Lorentz transformation of an up-singlet component carrying no derivatives: the
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_uComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (h.uComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • h.uComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_baruComponent`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L358).

> The Lorentz transformation of a conjugate up-singlet component carrying no
> derivatives: the coefficients of the up-singlet law, conjugated.

```lean
lemma repLorentz_baruComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repLorentz Λ (h.baruComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • h.baruComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_QComponent`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L370).

> The Lorentz transformation of a quark-doublet component carrying no derivatives: the
> left-handed spinor index transforms by the inverse matrix.

```lean
lemma repLorentz_QComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentz Λ (h.QComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • h.QComponent i l (β, j.2.1, j.2.2)
```

**`StandardModel.IsFermionSector.repLorentz_barQComponent`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L382).

> The Lorentz transformation of a conjugate quark-doublet component carrying no
> derivatives: the coefficients of the quark-doublet law, conjugated.

```lean
lemma repLorentz_barQComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    repLorentz Λ (h.barQComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • h.barQComponent i l (β, j.2.1, j.2.2)
```

**`StandardModel.IsFermionSector.repLorentz_LComponent`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L394).

> The Lorentz transformation of a lepton-doublet component carrying no derivatives: the
> left-handed spinor index transforms by the inverse matrix.

```lean
lemma repLorentz_LComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repLorentz Λ (h.LComponent i l j) =
      ∑ β, (Λ⁻¹).1 j.1 β • h.LComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_barLComponent`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L406).

> The Lorentz transformation of a conjugate lepton-doublet component carrying no
> derivatives: the coefficients of the lepton-doublet law, conjugated.

```lean
lemma repLorentz_barLComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repLorentz Λ (h.barLComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j.1 β) • h.barLComponent i l (β, j.2)
```

**`StandardModel.IsFermionSector.repLorentz_eComponent`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L418).

> The Lorentz transformation of a lepton-singlet component carrying no derivatives: the
> right-handed spinor index transforms by the entrywise conjugate of the inverse matrix.

```lean
lemma repLorentz_eComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    repLorentz Λ (h.eComponent i l j) =
      ∑ β, star ((Λ⁻¹).1 j β) • h.eComponent i l β
```

**`StandardModel.IsFermionSector.repLorentz_bareComponent`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L430).

> The Lorentz transformation of a conjugate lepton-singlet component carrying no
> derivatives: the coefficients of the lepton-singlet law, conjugated.

```lean
lemma repLorentz_bareComponent (Λ : SL(2,ℂ)) (i : Fin 3) (l : Fin 0 → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    repLorentz Λ (h.bareComponent i l j) =
      ∑ β, (Λ⁻¹).1 j β • h.bareComponent i l β
```

## D. The torus specialisation and the recorded gauge weights

> Restricting the gauge law of section B to the four torus generators must return the gauge
> weights already recorded for the fermion derivative submodules: the negative of the value
> space's weight for an unbarred species, and the value space's own weight for a barred one.
> The lemmas below derive exactly those weights from the full-group laws, so the variance of
> section B and the weight bookkeeping of the derivative submodules agree.

### D.1. The inverses of the torus generators

**`StandardModel.expI_inv_coe`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L459).

> The inverse of the unitary `exp i` is its conjugate.

```lean
lemma _root_.StandardModel.expI_inv_coe : ((expI⁻¹ : unitary ℂ) : ℂ) = star (expI : ℂ)
```

**`StandardModel.su3ExpIOne_inv_coe`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L462).

> The inverse of the first colour torus generator, `diag (exp (-i), exp i, 1)`.

```lean
lemma _root_.StandardModel.su3ExpIOne_inv_coe :
    (su3ExpIOne⁻¹ : specialUnitaryGroup (Fin 3) ℂ).1
      = Matrix.diagonal ![star (expI : ℂ), (expI : ℂ), 1]
```

**`StandardModel.su3ExpITwo_inv_coe`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L470).

> The inverse of the second colour torus generator, `diag (1, exp (-i), exp i)`.

```lean
lemma _root_.StandardModel.su3ExpITwo_inv_coe :
    (su3ExpITwo⁻¹ : specialUnitaryGroup (Fin 3) ℂ).1
      = Matrix.diagonal ![1, star (expI : ℂ), (expI : ℂ)]
```

### D.2. The weights of the ten components

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_dComponent`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L484).

> The `d` components carry the negative of the down-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_dComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (h.dComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(DownSinglet.valueGaugeWeight j)) t) •
        h.dComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_bardComponent`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L498).

> The `bard` components carry the down-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_bardComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (h.bardComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) t) •
        h.bardComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_uComponent`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L512).

> The `u` components carry the negative of the up-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_uComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (h.uComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(UpSinglet.valueGaugeWeight j)) t) •
        h.uComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_baruComponent`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L526).

> The `baru` components carry the up-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_baruComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen t) (h.baruComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) t) •
        h.baruComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_QComponent`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L540).

> The `Q` components carry the negative of the quark-doublet weight.

```lean
lemma repGauge_gaugeTorusGen_QComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen t) (h.QComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(QuarkDoublet.valueGaugeWeight j)) t) •
        h.QComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_barQComponent`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L554).

> The `barQ` components carry the quark-doublet weight itself.

```lean
lemma repGauge_gaugeTorusGen_barQComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen t) (h.barQComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) t) •
        h.barQComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_LComponent`**, a lemma, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L568).

> The `L` components carry the negative of the lepton-doublet weight.

```lean
lemma repGauge_gaugeTorusGen_LComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen t) (h.LComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonDoubletV.valueGaugeWeight j)) t) •
        h.LComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_barLComponent`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L581).

> The `barL` components carry the lepton-doublet weight itself.

```lean
lemma repGauge_gaugeTorusGen_barLComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen t) (h.barLComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) t) •
        h.barLComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_eComponent`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L595).

> The `e` components carry the negative of the lepton-singlet weight.

```lean
lemma repGauge_gaugeTorusGen_eComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen t) (h.eComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonSinglet.valueGaugeWeight j)) t) •
        h.eComponent i l j
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_bareComponent`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean#L606).

> The `bare` components carry the lepton-singlet weight itself.

```lean
lemma repGauge_gaugeTorusGen_bareComponent (t : Fin 4) (i : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen t) (h.bareComponent i l j)
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) t) •
        h.bareComponent i l j
```

## Depends on

- [Down-type singlets](../part-03/fermions-downsinglet-basic.md)
- [Charged-lepton singlets](../part-03/fermions-leptonsinglet-basic.md)
- [The type corresponding to quark doublets](../part-03/fermions-quarkdoublet-basic.md)
- [Up-type singlets](../part-03/fermions-upsinglet-basic.md)
- [The fermion sector](isfermionsector-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Components.lean)
