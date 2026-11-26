---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_left, StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_mid, StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_right, StandardModel.LocalCovFieldAlgebra.repLorentz_mul_fixed_left, StandardModel.LocalCovFieldAlgebra.repGauge_su3_higgs, StandardModel.LocalCovFieldAlgebra.repGauge_su2_higgs, StandardModel.LocalCovFieldAlgebra.repGauge_u1_higgs, StandardModel.LocalCovFieldAlgebra.repGauge_su3_barHiggs
statement: formalized
proof: formalized
---

# The symbols of the Yukawa blocks

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.YukawaSector.Families.Symbols`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean): 37 declarations, 37 with a docstring.

> The symbols of the Yukawa blocks of the Standard Model's covariant field algebra.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> At mass weight eight a Yukawa block is a product of three underived symbols, one Higgs and
> two fermions, and every statement about such a block reduces to statements about its three
> factors. This file is that reduction. It reads the Higgs symbols at each factor of a gauge
> transformation (the fermion symbols are read in `FermionSector/Components.lean`), does the
> algebra of a triple product with one inert factor once for each position the inert factor can
> occupy, and records the closure of the index laws under the sums and differences a contraction
> performs.
>
> Two things here are easy to get wrong and are settled once. A gauge transformation is a
> triple and the three index laws each constrain one factor of it. Colour, isospin and
> Lorentz between them say nothing about hypercharge, so hypercharge is a fourth step and not
> a corollary of the other three, and `forall_repGauge_eq_self`, in `GaugeGroup/Basic.lean`,
> is what assembles the four into gauge invariance. And the twelve blocks come in two fermion
> orderings, but the fermion
> symbols anticommute, so the two orderings of a block span the same submodule and have the
> same weight pieces, and `mul_mul_piece_swap` is what makes the six transposed blocks a rewrite
> rather than six fresh derivations.

## ii. Key results

> - `repGauge_mul_fixed_left`, `repGauge_mul_fixed_mid`, `repGauge_mul_fixed_right`,
>   `repLorentz_mul_fixed_left` : the transformation of a triple product with one inert
>   factor.
> - `repGauge_su3_higgs`, `repGauge_su2_higgs`, `repGauge_u1_higgs` and their conjugates : the three
>   gauge laws of the Higgs symbols.
> - `mul_mul_piece_swap` : the two fermion orderings of a block have the same weight pieces.

## iv. References

> * None.

## A. Triple products with one inert factor

> Every block is a product of three symbols, and every classifier moves exactly two of them.
> The third is inert, being a colour singlet, an isospin singlet or a Lorentz scalar. The
> three lemmas here do the algebra once for each position the inert factor can occupy, and
> reduce a transformation law for a block to the laws of its factors.

**`StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_left`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L84).

> A triple product whose first factor is fixed and whose second and third move by given
> coefficients moves by the product of those coefficients.

```lean
lemma repGauge_mul_fixed_left (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : fieldData.LocalCovFieldAlgebra} {X : ι → fieldData.LocalCovFieldAlgebra}
    {Y : κ → fieldData.LocalCovFieldAlgebra}
    {x₀ : ι} {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hA : repGaugeGroupI g A = A) (hX : repGaugeGroupI g (X x₀) = ∑ x,
      cX x • X x)
    (hY : repGaugeGroupI g (Y y₀) = ∑ y, cY y • Y y) :
    repGaugeGroupI g (A * (X x₀ * Y y₀)) = ∑ x, ∑ y, (cX x * cY y) •
      (A * (X x * Y y))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_mid`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L100).

> A triple product whose second factor is fixed.

```lean
lemma repGauge_mul_fixed_mid (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : ι → fieldData.LocalCovFieldAlgebra} {X : fieldData.LocalCovFieldAlgebra}
    {Y : κ → fieldData.LocalCovFieldAlgebra}
    {a₀ : ι} {y₀ : κ} {cA : ι → ℂ} {cY : κ → ℂ}
    (hA : repGaugeGroupI g (A a₀) = ∑ a, cA a • A a)
      (hX : repGaugeGroupI g X = X)
    (hY : repGaugeGroupI g (Y y₀) = ∑ y, cY y • Y y) :
    repGaugeGroupI g (A a₀ * (X * Y y₀)) = ∑ a, ∑ y, (cA a * cY y) •
      (A a * (X * Y y))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_mul_fixed_right`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L116).

> A triple product whose third factor is fixed.

```lean
lemma repGauge_mul_fixed_right (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : ι → fieldData.LocalCovFieldAlgebra} {X : κ → fieldData.LocalCovFieldAlgebra}
    {Y : fieldData.LocalCovFieldAlgebra} {a₀ : ι}
    {x₀ : κ} {cA : ι → ℂ} {cX : κ → ℂ}
    (hA : repGaugeGroupI g (A a₀) = ∑ a, cA a • A a)
    (hX : repGaugeGroupI g (X x₀) = ∑ x, cX x • X x)
      (hY : repGaugeGroupI g Y = Y) :
    repGaugeGroupI g (A a₀ * (X x₀ * Y)) = ∑ a, ∑ x, (cA a * cX x) •
      (A a * (X x * Y))
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_mul_fixed_left`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L132).

> The Lorentz analogue of `repGauge_mul_fixed_left`, the Higgs factor being inert.

```lean
lemma repLorentz_mul_fixed_left (Λ : SL(2,ℂ)) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : fieldData.LocalCovFieldAlgebra} {X : ι → fieldData.LocalCovFieldAlgebra}
    {Y : κ → fieldData.LocalCovFieldAlgebra}
    {x₀ : ι} {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hA : repLorentzGroup Λ A = A) (hX : repLorentzGroup Λ (X x₀) = ∑ x,
      cX x • X x)
    (hY : repLorentzGroup Λ (Y y₀) = ∑ y, cY y • Y y) :
    repLorentzGroup Λ (A * (X x₀ * Y y₀)) = ∑ x, ∑ y, (cX x * cY y) •
      (A * (X x * Y y))
```

## B. The transformation laws of the Higgs symbols

> Each Higgs symbol is read at the three factors of a gauge transformation in turn, and at the
> Lorentz group. Colour fixes it, isospin moves its isospin index, and hypercharge is an overall
> scalar, the power of which is the `6Y = ∓3` of the Higgs and its conjugate. The same laws for
> the ten fermion species are `FermionSector.repGauge_su3_d` and its companions, next to the
> components in `FermionSector/Components.lean`.

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_higgs`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L160).

> A colour transformation fixes a Higgs symbol.

```lean
lemma repGauge_su3_higgs (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (ScalarSector.higgs l i)
      = ScalarSector.higgs l i
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_higgs`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L169).

> An isospin transformation moves the isospin index of a Higgs symbol by the conjugate
> matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_higgs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (ScalarSector.higgs l i)
      = ∑ a, conj (V.1 a i) • ScalarSector.higgs l a
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_higgs`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L180).

> A hypercharge transformation scales a Higgs symbol by the cube of the conjugate
> scalar, the Higgs carrying `6Y = -3`.

```lean
lemma repGauge_u1_higgs (t : unitary ℂ) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (ScalarSector.higgs l i)
      = (star (t : ℂ)) ^ 3 • ScalarSector.higgs l i
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barHiggs`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L187).

> A colour transformation fixes a conjugate Higgs symbol.

```lean
lemma repGauge_su3_barHiggs (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (ScalarSector.barHiggs l i)
      = ScalarSector.barHiggs l i
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_barHiggs`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L196).

> An isospin transformation moves the isospin index of a conjugate Higgs symbol by the
> matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barHiggs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (ScalarSector.barHiggs l i)
      = ∑ a, V.1 a i • ScalarSector.barHiggs l a
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barHiggs`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L207).

> A hypercharge transformation scales a conjugate Higgs symbol by the cube of the
> scalar, the conjugate Higgs carrying `6Y = 3`.

```lean
lemma repGauge_u1_barHiggs (t : unitary ℂ) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (ScalarSector.barHiggs l i)
      = (t : ℂ) ^ 3 • ScalarSector.barHiggs l i
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_higgs_zero`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L214).

> A Higgs symbol carrying no derivatives is Lorentz invariant.

```lean
lemma repLorentz_higgs_zero (Λ : SL(2,ℂ)) (l : Fin 0 → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repLorentzGroup Λ (ScalarSector.higgs l i) = ScalarSector.higgs l i
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_barHiggs_zero`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L221).

> A conjugate Higgs symbol carrying no derivatives is Lorentz invariant.

```lean
lemma repLorentz_barHiggs_zero (Λ : SL(2,ℂ)) (l : Fin 0 → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repLorentzGroup Λ (ScalarSector.barHiggs l i) = ScalarSector.barHiggs l i
```

## C. The symbols inside the derivative submodules

> A block is a product of three underived symbols, and by
> `sectorMassWeight_higgs_fermion_eight` the sector at mass weight eight is the product of
> the Higgs derivative submodule with two copies of the fermion one.  So a block sits at mass
> weight eight as soon as each of its three symbols is seen inside the matching derivative
> submodule.  The ten ranges are recorded as inclusions rather than as memberships, since
> section F needs the inclusion and the membership of a component follows from it.

**`StandardModel.LocalCovFieldAlgebra.higgs_mem_derivSubmodule`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L241).

> A Higgs symbol lies in the Higgs derivative submodule.

```lean
lemma higgs_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    ScalarSector.higgs l i ∈ ScalarSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.barHiggs_mem_derivSubmodule`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L246).

> A conjugate Higgs symbol lies in the Higgs derivative submodule.

```lean
lemma barHiggs_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    ScalarSector.barHiggs l i ∈ ScalarSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_d_le_derivSubmodule`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L251).

> The range of a down-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_d_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (downSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_bard_le_derivSubmodule`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L258).

> The range of a conjugate down-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_bard_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (conjDownSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_u_le_derivSubmodule`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L265).

> The range of an up-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_u_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (upSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_baru_le_derivSubmodule`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L272).

> The range of a conjugate up-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_baru_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (conjUpSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_Q_le_derivSubmodule`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L278).

> The range of a quark-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_Q_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (quarkDoubletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_barQ_le_derivSubmodule`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L284).

> The range of a conjugate quark-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_barQ_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (conjQuarkDoubletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_L_le_derivSubmodule`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L290).

> The range of a lepton-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_L_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (leptonDoubletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_barL_le_derivSubmodule`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L295).

> The range of a conjugate lepton-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_barL_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (conjLeptonDoubletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_e_le_derivSubmodule`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L300).

> The range of a lepton-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_e_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (leptonSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.range_bare_le_derivSubmodule`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L305).

> The range of a conjugate lepton-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_bare_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (conjLeptonSingletField f l) ≤ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.dComponent_mem_derivSubmodule`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L310).

> A `d` component lies in the fermion derivative submodule.

```lean
lemma dComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    FermionSector.dComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.bardComponent_mem_derivSubmodule`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L316).

> A `bard` component lies in the fermion derivative submodule.

```lean
lemma bardComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    FermionSector.bardComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.uComponent_mem_derivSubmodule`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L322).

> A `u` component lies in the fermion derivative submodule.

```lean
lemma uComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    FermionSector.uComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.baruComponent_mem_derivSubmodule`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L328).

> A `baru` component lies in the fermion derivative submodule.

```lean
lemma baruComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    FermionSector.baruComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.QComponent_mem_derivSubmodule`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L334).

> A `Q` component lies in the fermion derivative submodule.

```lean
lemma QComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    FermionSector.QComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.barQComponent_mem_derivSubmodule`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L340).

> A `barQ` component lies in the fermion derivative submodule.

```lean
lemma barQComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    FermionSector.barQComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.LComponent_mem_derivSubmodule`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L346).

> A `L` component lies in the fermion derivative submodule.

```lean
lemma LComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    FermionSector.LComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.barLComponent_mem_derivSubmodule`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L352).

> A `barL` component lies in the fermion derivative submodule.

```lean
lemma barLComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    FermionSector.barLComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.eComponent_mem_derivSubmodule`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L358).

> A `e` component lies in the fermion derivative submodule.

```lean
lemma eComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    FermionSector.eComponent f l j ∈ FermionSector.derivSubmodule n
```

**`StandardModel.LocalCovFieldAlgebra.bareComponent_mem_derivSubmodule`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L364).

> A `bare` component lies in the fermion derivative submodule.

```lean
lemma bareComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    FermionSector.bareComponent f l j ∈ FermionSector.derivSubmodule n
```

## D. The two fermion orderings

> The twelve blocks of the mass-weight-eight decomposition are six choices of a Higgs symbol
> and a fermion pair, each occurring in both fermion orderings.  The two orderings are not
> the same element — the fermion symbols anticommute, so one is minus the other — but they
> span the same submodule, and therefore have the same weight pieces.  So a classification of
> one ordering is a classification of the other, and the six transposed blocks need no
> argument of their own.

**`StandardModel.LocalCovFieldAlgebra.mul_comm_of_le_derivSubmodule`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L384).

> Two submodules of fermion derivative submodules commute, the fermion symbols
> anticommuting and a submodule being closed under negation.

```lean
lemma mul_comm_of_le_derivSubmodule {n m : ℕ} {V W : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hV : V ≤ FermionSector.derivSubmodule n)
    (hW : W ≤ FermionSector.derivSubmodule m) : V * W = W * V
```

**`StandardModel.LocalCovFieldAlgebra.mul_mul_piece_swap`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L397).

> Swapping the two fermion factors of a block leaves every weight piece unchanged. The
> two fermion factors commute as submodules, so the two orderings of the block are the same
> submodule. This is what makes the six transposed blocks of the mass-weight-eight
> decomposition a rewrite rather than six fresh classifications.

```lean
lemma mul_mul_piece_swap {VH VX VY : Submodule ℂ fieldData.LocalCovFieldAlgebra} {n m : ℕ}
    (dH : GaugeWeightDecomposition repGaugeGroupI VH)
    (dX : GaugeWeightDecomposition repGaugeGroupI VX)
    (dY : GaugeWeightDecomposition repGaugeGroupI VY)
    (hX : VX ≤ FermionSector.derivSubmodule n)
    (hY : VY ≤ FermionSector.derivSubmodule m) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dH)
        (d' := GaugeWeightDecomposition.mul (d := dX) (d' := dY))).piece w
      = (GaugeWeightDecomposition.mul (d := dH)
        (d' := GaugeWeightDecomposition.mul (d := dY) (d' := dX))).piece w
```

**`StandardModel.LocalCovFieldAlgebra.mul_mul_swap_eq_neg`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean#L415).

> Swapping the two fermion factors of a block negates it.

```lean
lemma mul_mul_swap_eq_neg {n m : ℕ} (a : fieldData.LocalCovFieldAlgebra)
    {x y : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ FermionSector.derivSubmodule n)
    (hy : y ∈ FermionSector.derivSubmodule m) :
    a * (y * x) = -(a * (x * y))
```

## Depends on

- [The components of the fermion symbols](../part-03/localfieldalgebra-fermionsector-components.md)
- [The derivative submodules of the scalar sector](../part-05/localfieldalgebra-scalarsector-derivsubmodule-ba.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Symbols.lean)
