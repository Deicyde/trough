---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.repGauge_mul_fixed_left, StandardModel.CovAlgebraRealization.repGauge_mul_fixed_mid, StandardModel.CovAlgebraRealization.repGauge_mul_fixed_right, StandardModel.CovAlgebraRealization.repLorentz_mul_fixed_left, StandardModel.CovAlgebraRealization.repGauge_su3_higgs, StandardModel.CovAlgebraRealization.repGauge_su2_higgs, StandardModel.CovAlgebraRealization.repGauge_u1_higgs, StandardModel.CovAlgebraRealization.repGauge_su3_barHiggs
statement: formalized
proof: formalized
---

# The symbols of the Yukawa blocks

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.YukawaSector.Families.Symbols`, [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean): 67 declarations, 67 with a docstring.

## i. Overview

> At mass weight eight a Yukawa block is a product of three underived symbols, one Higgs and
> two fermions, and every statement about such a block reduces to statements about its three
> factors. This file is that reduction: it reads each of the twelve symbols at each factor of
> a gauge transformation, does the algebra of a triple product with one inert factor once for
> each position the inert factor can occupy, and records the closure of the index laws under
> the sums and differences a contraction performs.
>
> Two things here are easy to get wrong and are settled once. A gauge transformation is a
> triple and the three index laws each constrain one factor of it: colour, isospin and
> Lorentz between them say nothing about hypercharge, so hypercharge is a fourth step and not
> a corollary of the other three, and `forall_repGauge_eq_self`, in `StandardModel.InvariantReduction`
> with the rest of the shared framework, is what assembles the four into gauge invariance.
> And the twelve blocks come in two fermion orderings, but the fermion
> symbols anticommute, so the two orderings of a block span the same submodule and have the
> same weight pieces: `mul_mul_piece_swap` is what makes the six transposed blocks a rewrite
> rather than six fresh derivations.

## ii. Key results

> - `repGauge_mul_fixed_left`, `repGauge_mul_fixed_mid`, `repGauge_mul_fixed_right`,
>   `repLorentz_mul_fixed_left` : the transformation of a triple product with one inert
>   factor.
> - `repGauge_su3_*`, `repGauge_su2_*`, `repGauge_u1_*` : the three gauge laws of each of the
>   twelve symbols.
> - `mul_mul_piece_swap` : the two fermion orderings of a block have the same weight pieces.

## iv. References

> * None.

## A. Triple products with one inert factor

> Every block is a product of three symbols, and every classifier moves exactly two of them:
> the third is inert, being a colour singlet, an isospin singlet or a Lorentz scalar.  The
> three lemmas here do the algebra once for each position the inert factor can occupy, and
> reduce a transformation law for a block to the laws of its factors.

**`StandardModel.CovAlgebraRealization.repGauge_mul_fixed_left`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L96).

> A triple product whose first factor is fixed and whose second and third move by given
> coefficients moves by the product of those coefficients.

```lean
lemma repGauge_mul_fixed_left (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : B} {X : ι → B} {Y : κ → B} {x₀ : ι} {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hA : repGauge g A = A) (hX : repGauge g (X x₀) = ∑ x, cX x • X x)
    (hY : repGauge g (Y y₀) = ∑ y, cY y • Y y) :
    repGauge g (A * (X x₀ * Y y₀)) = ∑ x, ∑ y, (cX x * cY y) • (A * (X x * Y y))
```

**`StandardModel.CovAlgebraRealization.repGauge_mul_fixed_mid`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L109).

> A triple product whose second factor is fixed.

```lean
lemma repGauge_mul_fixed_mid (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : ι → B} {X : B} {Y : κ → B} {a₀ : ι} {y₀ : κ} {cA : ι → ℂ} {cY : κ → ℂ}
    (hA : repGauge g (A a₀) = ∑ a, cA a • A a) (hX : repGauge g X = X)
    (hY : repGauge g (Y y₀) = ∑ y, cY y • Y y) :
    repGauge g (A a₀ * (X * Y y₀)) = ∑ a, ∑ y, (cA a * cY y) • (A a * (X * Y y))
```

**`StandardModel.CovAlgebraRealization.repGauge_mul_fixed_right`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L122).

> A triple product whose third factor is fixed.

```lean
lemma repGauge_mul_fixed_right (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : ι → B} {X : κ → B} {Y : B} {a₀ : ι} {x₀ : κ} {cA : ι → ℂ} {cX : κ → ℂ}
    (hA : repGauge g (A a₀) = ∑ a, cA a • A a)
    (hX : repGauge g (X x₀) = ∑ x, cX x • X x) (hY : repGauge g Y = Y) :
    repGauge g (A a₀ * (X x₀ * Y)) = ∑ a, ∑ x, (cA a * cX x) • (A a * (X x * Y))
```

**`StandardModel.CovAlgebraRealization.repLorentz_mul_fixed_left`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L135).

> The Lorentz analogue of `repGauge_mul_fixed_left`, the Higgs factor being inert.

```lean
lemma repLorentz_mul_fixed_left (Λ : SL(2,ℂ)) {ι κ : Type} [Fintype ι] [Fintype κ]
    {A : B} {X : ι → B} {Y : κ → B} {x₀ : ι} {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hA : repLorentz Λ A = A) (hX : repLorentz Λ (X x₀) = ∑ x, cX x • X x)
    (hY : repLorentz Λ (Y y₀) = ∑ y, cY y • Y y) :
    repLorentz Λ (A * (X x₀ * Y y₀)) = ∑ x, ∑ y, (cX x * cY y) • (A * (X x * Y y))
```

## B. The transformation laws of the symbols

> Each symbol is read at the three factors of a gauge transformation in turn, and the Higgs
> symbols also at the Lorentz group.  Colour moves only a colour index, isospin only an
> isospin index, and hypercharge is an overall scalar, the power of which is the `6Y` of the
> species: `-3` for the Higgs symbols, `2` for the down singlet, `1` for the conjugate quark
> doublet, `4` for the conjugate up singlet, `-1` for the quark doublet, `-3` for the
> conjugate lepton doublet and `6` for the lepton singlet.  A symbol carrying no index of a
> given factor is fixed by it outright.

### B.1. The Higgs symbols

**`StandardModel.CovAlgebraRealization.repGauge_su3_higgs`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L167).

> A colour transformation fixes a Higgs symbol.

```lean
lemma repGauge_su3_higgs (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isHiggsSector.higgs l i)
      = h.isHiggsSector.higgs l i
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_higgs`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L176).

> An isospin transformation moves the isospin index of a Higgs symbol by the conjugate
> matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_higgs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isHiggsSector.higgs l i)
      = ∑ a, conj (V.1 a i) • h.isHiggsSector.higgs l a
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_higgs`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L187).

> A hypercharge transformation scales a Higgs symbol by the cube of the conjugate
> scalar, the Higgs carrying `6Y = -3`.

```lean
lemma repGauge_u1_higgs (t : unitary ℂ) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isHiggsSector.higgs l i)
      = (star (t : ℂ)) ^ 3 • h.isHiggsSector.higgs l i
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_barHiggs`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L194).

> A colour transformation fixes a conjugate Higgs symbol.

```lean
lemma repGauge_su3_barHiggs (U : specialUnitaryGroup (Fin 3) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isHiggsSector.barHiggs l i)
      = h.isHiggsSector.barHiggs l i
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barHiggs`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L203).

> An isospin transformation moves the isospin index of a conjugate Higgs symbol by the
> matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barHiggs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isHiggsSector.barHiggs l i)
      = ∑ a, V.1 a i • h.isHiggsSector.barHiggs l a
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barHiggs`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L214).

> A hypercharge transformation scales a conjugate Higgs symbol by the cube of the
> scalar, the conjugate Higgs carrying `6Y = 3`.

```lean
lemma repGauge_u1_barHiggs (t : unitary ℂ) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isHiggsSector.barHiggs l i)
      = (t : ℂ) ^ 3 • h.isHiggsSector.barHiggs l i
```

**`StandardModel.CovAlgebraRealization.repLorentz_higgs_zero`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L221).

> A Higgs symbol carrying no derivatives is Lorentz invariant.

```lean
lemma repLorentz_higgs_zero (Λ : SL(2,ℂ)) (l : Fin 0 → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repLorentz Λ (h.isHiggsSector.higgs l i) = h.isHiggsSector.higgs l i
```

**`StandardModel.CovAlgebraRealization.repLorentz_barHiggs_zero`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L228).

> A conjugate Higgs symbol carrying no derivatives is Lorentz invariant.

```lean
lemma repLorentz_barHiggs_zero (Λ : SL(2,ℂ)) (l : Fin 0 → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    repLorentz Λ (h.isHiggsSector.barHiggs l i) = h.isHiggsSector.barHiggs l i
```

### B.2. The down singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_d`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L242).

> A colour transformation moves the colour index of a down-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_d (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.dComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • h.isFermionSector.dComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_d`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L252).

> An isospin transformation fixes a down-singlet symbol, which carries no isospin.

```lean
lemma repGauge_su2_d (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.dComponent f l j)
      = h.isFermionSector.dComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_d`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L261).

> A hypercharge transformation scales a down-singlet symbol by the square of the scalar,
> the down singlet carrying `6Y = 2`.

```lean
lemma repGauge_u1_d (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.dComponent f l j)
      = (t : ℂ) ^ 2 • h.isFermionSector.dComponent f l j
```

### B.3. The conjugate down singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_bard`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L276).

> A colour transformation moves the colour index of a conjugate down-singlet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_bard (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.bardComponent f l (s, c))
      = ∑ a, U.1 a c • h.isFermionSector.bardComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_bard`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L286).

> An isospin transformation fixes a conjugate down-singlet symbol.

```lean
lemma repGauge_su2_bard (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.bardComponent f l j)
      = h.isFermionSector.bardComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_bard`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L295).

> A hypercharge transformation scales a conjugate down-singlet symbol by the square of
> the conjugate scalar, the conjugate down singlet carrying `6Y = -2`.

```lean
lemma repGauge_u1_bard (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.bardComponent f l j)
      = (star (t : ℂ)) ^ 2 • h.isFermionSector.bardComponent f l j
```

### B.4. The up singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_u`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L310).

> A colour transformation moves the colour index of an up-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_u (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.uComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • h.isFermionSector.uComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_u`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L320).

> An isospin transformation fixes an up-singlet symbol.

```lean
lemma repGauge_su2_u (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.uComponent f l j)
      = h.isFermionSector.uComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_u`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L329).

> A hypercharge transformation scales an up-singlet symbol by the fourth power of the
> conjugate scalar, the up singlet carrying `6Y = -4`.

```lean
lemma repGauge_u1_u (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.uComponent f l j)
      = (star (t : ℂ)) ^ 4 • h.isFermionSector.uComponent f l j
```

### B.5. The conjugate up singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_baru`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L344).

> A colour transformation moves the colour index of a conjugate up-singlet symbol by the
> matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_baru (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.baruComponent f l (s, c))
      = ∑ a, U.1 a c • h.isFermionSector.baruComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_baru`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L354).

> An isospin transformation fixes a conjugate up-singlet symbol.

```lean
lemma repGauge_su2_baru (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.baruComponent f l j)
      = h.isFermionSector.baruComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_baru`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L363).

> A hypercharge transformation scales a conjugate up-singlet symbol by the fourth power
> of the scalar, the conjugate up singlet carrying `6Y = 4`.

```lean
lemma repGauge_u1_baru (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.baruComponent f l j)
      = (t : ℂ) ^ 4 • h.isFermionSector.baruComponent f l j
```

### B.6. The quark doublet

**`StandardModel.CovAlgebraRealization.repGauge_su3_Q`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L378).

> A colour transformation moves the colour index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_Q (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.QComponent f l (s, c, w))
      = ∑ a, conj (U.1 a c) • h.isFermionSector.QComponent f l (s, a, w)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_Q`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L389).

> An isospin transformation moves the isospin index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_Q (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.QComponent f l (s, c, w))
      = ∑ a, conj (V.1 a w) • h.isFermionSector.QComponent f l (s, c, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_Q`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L400).

> A hypercharge transformation scales a quark-doublet symbol by the conjugate scalar,
> the quark doublet carrying `6Y = -1`.

```lean
lemma repGauge_u1_Q (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.QComponent f l (s, c, w))
      = star (t : ℂ) • h.isFermionSector.QComponent f l (s, c, w)
```

### B.7. The conjugate quark doublet

**`StandardModel.CovAlgebraRealization.repGauge_su3_barQ`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L415).

> A colour transformation moves the colour index of a conjugate quark-doublet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_barQ (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.barQComponent f l (s, c, w))
      = ∑ a, U.1 a c • h.isFermionSector.barQComponent f l (s, a, w)
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barQ`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L427).

> An isospin transformation moves the isospin index of a conjugate quark-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barQ (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.barQComponent f l (s, c, w))
      = ∑ a, V.1 a w • h.isFermionSector.barQComponent f l (s, c, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barQ`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L438).

> A hypercharge transformation scales a conjugate quark-doublet symbol by the scalar,
> the conjugate quark doublet carrying `6Y = 1`.

```lean
lemma repGauge_u1_barQ (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.barQComponent f l (s, c, w))
      = (t : ℂ) • h.isFermionSector.barQComponent f l (s, c, w)
```

### B.8. The lepton doublet

**`StandardModel.CovAlgebraRealization.repGauge_su3_L`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L453).

> A colour transformation fixes a lepton-doublet symbol, which carries no colour.

```lean
lemma repGauge_su3_L (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.LComponent f l j)
      = h.isFermionSector.LComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_L`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L462).

> An isospin transformation moves the isospin index of a lepton-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_L (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.LComponent f l (s, w))
      = ∑ a, conj (V.1 a w) • h.isFermionSector.LComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_L`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L473).

> A hypercharge transformation scales a lepton-doublet symbol by the cube of the scalar,
> the lepton doublet carrying `6Y = 3`.

```lean
lemma repGauge_u1_L (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.LComponent f l j)
      = (t : ℂ) ^ 3 • h.isFermionSector.LComponent f l j
```

### B.9. The conjugate lepton doublet

**`StandardModel.CovAlgebraRealization.repGauge_su3_barL`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L488).

> A colour transformation fixes a conjugate lepton-doublet symbol, which carries no
> colour.

```lean
lemma repGauge_su3_barL (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.barLComponent f l j)
      = h.isFermionSector.barLComponent f l j
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barL`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L497).

> An isospin transformation moves the isospin index of a conjugate lepton-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barL (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.barLComponent f l (s, w))
      = ∑ a, V.1 a w • h.isFermionSector.barLComponent f l (s, a)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barL`**, a lemma, [line 508](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L508).

> A hypercharge transformation scales a conjugate lepton-doublet symbol by the cube of
> the conjugate scalar, the conjugate lepton doublet carrying `6Y = -3`.

```lean
lemma repGauge_u1_barL (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.barLComponent f l (s, w))
      = (star (t : ℂ)) ^ 3 • h.isFermionSector.barLComponent f l (s, w)
```

### B.10. The lepton singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_e`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L523).

> A colour transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su3_e (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.eComponent f l s)
      = h.isFermionSector.eComponent f l s
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_e`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L531).

> An isospin transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su2_e (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.eComponent f l s)
      = h.isFermionSector.eComponent f l s
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_e`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L540).

> A hypercharge transformation scales a lepton-singlet symbol by the sixth power of the
> scalar, the lepton singlet carrying `6Y = 6`.

```lean
lemma repGauge_u1_e (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.eComponent f l s)
      = (t : ℂ) ^ 6 • h.isFermionSector.eComponent f l s
```

### B.11. The conjugate lepton singlet

**`StandardModel.CovAlgebraRealization.repGauge_su3_bare`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L554).

> A colour transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su3_bare (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.isFermionSector.bareComponent f l s)
      = h.isFermionSector.bareComponent f l s
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_bare`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L562).

> An isospin transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su2_bare (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.isFermionSector.bareComponent f l s)
      = h.isFermionSector.bareComponent f l s
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_bare`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L571).

> A hypercharge transformation scales a conjugate lepton-singlet symbol by the sixth
> power of the conjugate scalar, the conjugate lepton singlet carrying `6Y = -6`.

```lean
lemma repGauge_u1_bare (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.isFermionSector.bareComponent f l s)
      = (star (t : ℂ)) ^ 6 • h.isFermionSector.bareComponent f l s
```

## C. The symbols inside the derivative submodules

> A block is a product of three underived symbols, and by
> `sectorMassWeight_higgs_fermion_eight` the sector at mass weight eight is the product of
> the Higgs derivative submodule with two copies of the fermion one.  So a block sits at mass
> weight eight as soon as each of its three symbols is seen inside the matching derivative
> submodule.  The ten ranges are recorded as inclusions rather than as memberships, since
> section F needs the inclusion and the membership of a component follows from it.

**`StandardModel.CovAlgebraRealization.higgs_mem_derivSubmodule`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L592).

> A Higgs symbol lies in the Higgs derivative submodule.

```lean
lemma higgs_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    h.isHiggsSector.higgs l i ∈ h.isHiggsSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.barHiggs_mem_derivSubmodule`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L597).

> A conjugate Higgs symbol lies in the Higgs derivative submodule.

```lean
lemma barHiggs_mem_derivSubmodule {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (i : Fin 2) :
    h.isHiggsSector.barHiggs l i ∈ h.isHiggsSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_d_le_derivSubmodule`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L602).

> The range of a down-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_d_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covD f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_bard_le_derivSubmodule`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L609).

> The range of a conjugate down-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_bard_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarD f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_u_le_derivSubmodule`**, a lemma, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L616).

> The range of an up-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_u_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covU f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_baru_le_derivSubmodule`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L623).

> The range of a conjugate up-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_baru_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarU f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_Q_le_derivSubmodule`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L629).

> The range of a quark-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_Q_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covQ f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_barQ_le_derivSubmodule`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L635).

> The range of a conjugate quark-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_barQ_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarQ f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_L_le_derivSubmodule`**, a lemma, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L641).

> The range of a lepton-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_L_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covL f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_barL_le_derivSubmodule`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L646).

> The range of a conjugate lepton-doublet symbol map lies in the fermion derivative submodule.

```lean
lemma range_barL_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarL f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_e_le_derivSubmodule`**, a lemma, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L651).

> The range of a lepton-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_e_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covE f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.range_bare_le_derivSubmodule`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L656).

> The range of a conjugate lepton-singlet symbol map lies in the fermion derivative submodule.

```lean
lemma range_bare_le_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (h.covBarE f l) ≤ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.dComponent_mem_derivSubmodule`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L661).

> A `d` component lies in the fermion derivative submodule.

```lean
lemma dComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    h.isFermionSector.dComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.bardComponent_mem_derivSubmodule`**, a lemma, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L667).

> A `bard` component lies in the fermion derivative submodule.

```lean
lemma bardComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    h.isFermionSector.bardComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.uComponent_mem_derivSubmodule`**, a lemma, [line 673](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L673).

> A `u` component lies in the fermion derivative submodule.

```lean
lemma uComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    h.isFermionSector.uComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.baruComponent_mem_derivSubmodule`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L679).

> A `baru` component lies in the fermion derivative submodule.

```lean
lemma baruComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    h.isFermionSector.baruComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.QComponent_mem_derivSubmodule`**, a lemma, [line 685](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L685).

> A `Q` component lies in the fermion derivative submodule.

```lean
lemma QComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    h.isFermionSector.QComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.barQComponent_mem_derivSubmodule`**, a lemma, [line 691](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L691).

> A `barQ` component lies in the fermion derivative submodule.

```lean
lemma barQComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3 × Fin 2) :
    h.isFermionSector.barQComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.LComponent_mem_derivSubmodule`**, a lemma, [line 697](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L697).

> A `L` component lies in the fermion derivative submodule.

```lean
lemma LComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    h.isFermionSector.LComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.barLComponent_mem_derivSubmodule`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L703).

> A `barL` component lies in the fermion derivative submodule.

```lean
lemma barLComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    h.isFermionSector.barLComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.eComponent_mem_derivSubmodule`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L709).

> A `e` component lies in the fermion derivative submodule.

```lean
lemma eComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    h.isFermionSector.eComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

**`StandardModel.CovAlgebraRealization.bareComponent_mem_derivSubmodule`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L715).

> A `bare` component lies in the fermion derivative submodule.

```lean
lemma bareComponent_mem_derivSubmodule (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2) :
    h.isFermionSector.bareComponent f l j ∈ h.isFermionSector.derivSubmodule n
```

## D. The two fermion orderings

> The twelve blocks of the mass-weight-eight decomposition are six choices of a Higgs symbol
> and a fermion pair, each occurring in both fermion orderings.  The two orderings are not
> the same element — the fermion symbols anticommute, so one is minus the other — but they
> span the same submodule, and therefore have the same weight pieces.  So a classification of
> one ordering is a classification of the other, and the six transposed blocks need no
> argument of their own.

**`StandardModel.CovAlgebraRealization.mul_comm_of_le_derivSubmodule`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L735).

> Two submodules of fermion derivative submodules commute, the fermion symbols
> anticommuting and a submodule being closed under negation.

```lean
lemma mul_comm_of_le_derivSubmodule {n m : ℕ} {V W : Submodule ℂ B}
    (hV : V ≤ h.isFermionSector.derivSubmodule n)
    (hW : W ≤ h.isFermionSector.derivSubmodule m) : V * W = W * V
```

**`StandardModel.CovAlgebraRealization.mul_mul_piece_swap`**, a lemma, [line 748](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L748).

> Swapping the two fermion factors of a block leaves every weight piece unchanged: the
> two fermion factors commute as submodules, so the two orderings of the block are the same
> submodule. This is what makes the six transposed blocks of the mass-weight-eight
> decomposition a rewrite rather than six fresh classifications.

```lean
lemma mul_mul_piece_swap {VH VX VY : Submodule ℂ B} {n m : ℕ}
    (dH : GaugeWeightDecomposition repGauge VH)
    (dX : GaugeWeightDecomposition repGauge VX)
    (dY : GaugeWeightDecomposition repGauge VY)
    (hX : VX ≤ h.isFermionSector.derivSubmodule n)
    (hY : VY ≤ h.isFermionSector.derivSubmodule m) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dH)
        (d' := GaugeWeightDecomposition.mul (d := dX) (d' := dY))).piece w
      = (GaugeWeightDecomposition.mul (d := dH)
        (d' := GaugeWeightDecomposition.mul (d := dY) (d' := dX))).piece w
```

**`StandardModel.CovAlgebraRealization.mul_mul_swap_eq_neg`**, a lemma, [line 766](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean#L766).

> Swapping the two fermion factors of a block negates it.

```lean
lemma mul_mul_swap_eq_neg {n m : ℕ} (a : B) {x y : B}
    (hx : x ∈ h.isFermionSector.derivSubmodule n)
    (hy : y ∈ h.isFermionSector.derivSubmodule m) :
    a * (y * x) = -(a * (x * y))
```

## Depends on

- [The covariant algebra valued Standard Model](../part-01/covrealization-basic.md)
- [The components of the fermion symbols](../part-05/isfermionsector-components.md)
- [The derivative submodules of the Higgs sector](../part-10/realization-higgscov-derivsubmodule-basic.md)

## Proof depends on

- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Symbols.lean)
