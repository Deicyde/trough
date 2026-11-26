---
declaration: module
origin: cited
lean: StandardModel.FermionSector.LeftIdx, StandardModel.FermionSector.RightIdx, StandardModel.FermionSector.leftComp, StandardModel.FermionSector.rightComp, StandardModel.FermionSector.repLorentz_leftComp, StandardModel.FermionSector.repLorentz_rightComp, StandardModel.FermionSector.leftSpan, StandardModel.FermionSector.rightSpan
statement: formalized
proof: formalized
---

# The invariants below mass weight eight (FermionSector/MassWeight/MassDimLTEight)

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.MassWeight.MassDimLTEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean): 30 declarations, 30 with a docstring.

## i. Overview

> The fermion sector carries nothing invariant below mass weight eight. Weights one, two
> and four are trivial submodules and weights three, five and seven are single fermion
> towers, which carry a nonzero hypercharge and so no gauge singlet. That leaves mass
> weight six, the products of two underived towers, and it is the interesting one: it is
> where a Dirac mass term `ψ̄ ψ` would sit, and the statement proved here is that no such
> term exists.
>
> The two symmetries cooperate. Gauge invariance cuts the hundred pairings of two fermion
> symbols down to the ten conjugate ones, `d bard`, `bard d`, `u baru`, ..., `bare e`,
> every other pairing having hypercharges that cannot cancel. This is
> `massWeightSubmoduleGaugeWeightSix_piece_zero` of the gauge weight decomposition. Each
> surviving pairing is then a product of two symbols of opposite chirality, one dotted and
> one undotted, since a species and its conjugate always sit in opposite Weyl
> representations. A pair of opposite-chirality spinor indices with nothing else to
> contract against admits no invariant at all — `complexLorentzTensor.invariants_upL_upR_eq_bot`
> — so each pairing contributes nothing and mass weight six is left empty.
>
> That is the absence of a Dirac mass term in the Standard Model, and it is why the fermion
> masses have to come from the Yukawa sector instead. The Higgs doublet supplies the missing
> index, and its own mass weight makes the Yukawa terms weight eight.
>
> The products of opposite-chirality one-index families, `Lorentz.isEquivariant_downLDownR_mul`
> and its swap, live in `PhyslibAlpha.Relativity.Fermions.Weyl.Metric`; they take
> the chirality law of each factor, contragredient to the left-handed Weyl representation or to
> its conjugate. The chirality bookkeeping
> of the species is done once here and reused at mass weight eight, in `MassDimEight`, which
> imports this file. The five undotted species are indexed by
> `LeftIdx` and the five dotted ones by `RightIdx`, and `leftComp` and `rightComp` list
> their components with the spinor index singled out.
>
> The final statement `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`
> needs `0 < w` as well as `w < 8`. At `w = 0` the mass-weight submodule contains the
> scalars, so `1` is an invariant of weight zero lying in no `S`.

## ii. Key results

> - `leftComp`, `rightComp` : the components of the five undotted and the five dotted species,
>   presented as two-element families in the spinor index.
> - `mem_of_invariant_of_mem_massWeightSubmoduleSix_sup` : mass weight six carries no invariant,
>   there being no Dirac mass term.
> - `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff` : the classification below
>   mass weight eight as an equivalence. An element of `massWeightSubmodule w ⊔ S` for `0 < w < 8`
>   is fixed by both groups exactly when it is itself an element of `S` fixed by both groups.

## iv. References

> * None.

## A. The five undotted and the five dotted species

> Each of the ten fermion species sits in one of the two Weyl representations, and a
> species and its conjugate always sit in opposite ones. The five undotted species are
> `bard`, `baru`, `Q`, `L` and `bare`, the five dotted ones `d`, `u`, `barQ`, `barL` and
> `e`. Indexing each list by the generation and the remaining internal indices, `leftComp`
> and `rightComp` present every fermion component as a two-element family in its spinor
> index, which is the shape the chirality laws `repLorentz_leftComp` and `repLorentz_rightComp`
> are stated in.

**`StandardModel.FermionSector.LeftIdx`**, an inductive, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L101).

> An index for the components of the five undotted fermion species, the generation
> together with the colour and isospin the species carries.

```lean
inductive LeftIdx
  | bard (f : Fin 3) (c : Fin 3)
  | baru (f : Fin 3) (c : Fin 3)
  | Q (f : Fin 3) (c : Fin 3) (s : Fin 2)
  | L (f : Fin 3) (s : Fin 2)
  | bare (f : Fin 3)
  deriving DecidableEq, Fintype
```

**`StandardModel.FermionSector.RightIdx`**, an inductive, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L111).

> An index for the components of the five dotted fermion species, the generation
> together with the colour and isospin the species carries.

```lean
inductive RightIdx
  | d (f : Fin 3) (c : Fin 3)
  | u (f : Fin 3) (c : Fin 3)
  | barQ (f : Fin 3) (c : Fin 3) (s : Fin 2)
  | barL (f : Fin 3) (s : Fin 2)
  | e (f : Fin 3)
  deriving DecidableEq, Fintype
```

**`StandardModel.FermionSector.leftComp`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L121).

> The components of the five undotted species at the derivative slots `l`, presented as
> a two-element family in the spinor index.

```lean
noncomputable def leftComp
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : LeftIdx → Fin 2 → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.rightComp`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L131).

> The components of the five dotted species at the derivative slots `l`, presented as a
> two-element family in the spinor index.

```lean
noncomputable def rightComp
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : RightIdx → Fin 2 → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.repLorentz_leftComp`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L141).

> Every undotted component family carries a dual undotted spinor index, at zero
> covariant derivatives.

```lean
lemma repLorentz_leftComp (i : LeftIdx) (Λ : SL(2,ℂ)) (a : Fin 2) :
    repLorentz Λ (leftComp ![] i a) = ∑ β, (Λ⁻¹).1 a β • leftComp ![] i β
```

**`StandardModel.FermionSector.repLorentz_rightComp`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L152).

> Every dotted component family carries a dual dotted spinor index, at zero covariant
> derivatives.

```lean
lemma repLorentz_rightComp (i : RightIdx) (Λ : SL(2,ℂ)) (a : Fin 2) :
    repLorentz Λ (rightComp ![] i a) = ∑ β, star ((Λ⁻¹).1 a β) • rightComp ![] i β
```

## B. The ranges of the symbol maps inside the chirality spans

> A symbol map is determined by its values on a basis of the dual of its value space, so
> its range is the join of the lines through its components
> (`LinearMap.range_eq_iSup_span_coord`).
> Collecting the ten ranges into the two chirality spans is then a matter of naming the
> right index.

**`StandardModel.FermionSector.leftSpan`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L175).

> The join of the lines through the components of the five undotted species.

```lean
noncomputable def leftSpan
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.rightSpan`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L180).

> The join of the lines through the components of the five dotted species.

```lean
noncomputable def rightSpan
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.range_bard_le_leftSpan`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L185).

> The range of the `bard` symbols lies in the undotted span.

```lean
lemma range_bard_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ leftSpan l
```

**`StandardModel.FermionSector.range_baru_le_leftSpan`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L194).

> The range of the `baru` symbols lies in the undotted span.

```lean
lemma range_baru_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ leftSpan l
```

**`StandardModel.FermionSector.range_Q_le_leftSpan`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L203).

> The range of the `Q` symbols lies in the undotted span.

```lean
lemma range_Q_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ leftSpan l
```

**`StandardModel.FermionSector.range_L_le_leftSpan`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L212).

> The range of the `L` symbols lies in the undotted span.

```lean
lemma range_L_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ leftSpan l
```

**`StandardModel.FermionSector.range_bare_le_leftSpan`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L221).

> The range of the `bare` symbols lies in the undotted span.

```lean
lemma range_bare_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ leftSpan l
```

**`StandardModel.FermionSector.range_d_le_rightSpan`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L230).

> The range of the `d` symbols lies in the dotted span.

```lean
lemma range_d_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ rightSpan l
```

**`StandardModel.FermionSector.range_u_le_rightSpan`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L239).

> The range of the `u` symbols lies in the dotted span.

```lean
lemma range_u_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ rightSpan l
```

**`StandardModel.FermionSector.range_barQ_le_rightSpan`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L248).

> The range of the `barQ` symbols lies in the dotted span.

```lean
lemma range_barQ_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ rightSpan l
```

**`StandardModel.FermionSector.range_barL_le_rightSpan`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L257).

> The range of the `barL` symbols lies in the dotted span.

```lean
lemma range_barL_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ rightSpan l
```

**`StandardModel.FermionSector.range_e_le_rightSpan`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L266).

> The range of the `e` symbols lies in the dotted span.

```lean
lemma range_e_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ rightSpan l
```

## C. Mass weight six with no Dirac mass term

> Gauge invariance is what selects the conjugate pairings. A gauge-invariant element lies
> in the weight-zero piece of the gauge weight decomposition, and modulo a gauge-stable
> submodule the same holds with the submodule joined on. The torus generators scale every
> other weight, and `GaugeWeightDecomposition.reducesInvariantsTo_piece_zero` deletes them
> one piece at a time. Unlike the single-tower case, the generator has to be chosen weight by
> weight, since a product like `Q barQ` at two different colours has vanishing hypercharge and
> nonzero colour, so no one generator sees every weight.
>
> Mass weight six is the product of two underived fermion towers. Gauge invariance puts
> such an invariant in the weight-zero piece, which `massWeightSubmoduleGaugeWeightSix_piece_zero`
> writes as the ten conjugate pairings, and every one of those is an undotted
> component times a dotted one. `Lorentz.isEquivariant_downLDownR_mul` turns each into a dual
> left-right Weyl family and `Lorentz.mem_of_lorentz_invariant_iSup_dualLeftRightWeyl_span`
> peels the lot off, leaving nothing.
>
> The physics is that the Standard Model has no Dirac mass term. A mass term pairs a
> left-handed field with a right-handed one, and while such a pair is exactly what survives
> the gauge cut, its two spinor indices have nothing to contract against. A dotted index
> and an undotted one carry no invariant pairing, and only the symplectic form pairs two indices
> of the same chirality. The fermion masses have to come from somewhere else, and they do,
> from the Yukawa sector, where the Higgs doublet supplies the missing index.

**`StandardModel.FermionSector.mul_le_iSup_span_pair`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L305).

> If `V` lies in the join of the lines through an undotted family and `W` in the join
> for a dotted one, the product lies in the join of the spans of the pair families.

```lean
lemma mul_le_iSup_span_pair {ι κ : Type}
    {X : ι → Fin 2 → fieldData.LocalCovFieldAlgebra}
    {Y : κ → Fin 2 → fieldData.LocalCovFieldAlgebra}
    {V W : Submodule ℂ fieldData.LocalCovFieldAlgebra} (hV : V ≤ ⨆ (i : ι) (a : Fin 2), ℂ ∙ X i a)
    (hW : W ≤ ⨆ (j : κ) (a : Fin 2), ℂ ∙ Y j a) :
    V * W ≤ ⨆ (p : ι × κ) (l : Fin 2 × Fin 2), ℂ ∙ (X p.1 l.1 * Y p.2 l.2)
```

**`StandardModel.FermionSector.mul_le_iSup_span_pair_swap`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L319).

> The mirror of `mul_le_iSup_span_pair` with the two spinor slots exchanged, for a
> product whose left factor is the dotted one.

```lean
lemma mul_le_iSup_span_pair_swap {ι κ : Type}
    {X : ι → Fin 2 → fieldData.LocalCovFieldAlgebra}
    {Y : κ → Fin 2 → fieldData.LocalCovFieldAlgebra}
    {V W : Submodule ℂ fieldData.LocalCovFieldAlgebra} (hV : V ≤ ⨆ (i : ι) (a : Fin 2), ℂ ∙ X i a)
    (hW : W ≤ ⨆ (j : κ) (a : Fin 2), ℂ ∙ Y j a) :
    V * W ≤ ⨆ (p : ι × κ) (l : Fin 2 × Fin 2), ℂ ∙ (X p.1 l.2 * Y p.2 l.1)
```

**`StandardModel.FermionSector.sixFamily`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L333).

> The mass-weight six families, a product of two underived components of opposite
> chirality, in either order.

```lean
noncomputable def sixFamily :
    (LeftIdx × RightIdx) ⊕ (RightIdx × LeftIdx) → Fin 2 × Fin 2 → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.sixSpan`**, a def, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L339).

> The join of the spans of the mass-weight six families.

```lean
noncomputable def sixSpan :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_downLDownR_sixFamily`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L346).

> Each mass-weight six family carries one dual undotted and one dual dotted spinor
> index.

```lean
lemma isEquivariant_downLDownR_sixFamily
    (i : (LeftIdx × RightIdx) ⊕ (RightIdx × LeftIdx)) :
    complexLorentzTensor.IsEquivariant ![.downL, .downR] repLorentz
      (liftComponents (sixFamily i ∘ pairIdx))
```

**`StandardModel.FermionSector.mul_le_sixSpan_left`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L359).

> An undotted range times a dotted one lies in the mass-weight six span.

```lean
lemma mul_le_sixSpan_left {V W : Submodule ℂ fieldData.LocalCovFieldAlgebra} (hV : V ≤ leftSpan ![])
    (hW : W ≤ rightSpan ![]) : V * W ≤ sixSpan
```

**`StandardModel.FermionSector.mul_le_sixSpan_right`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L365).

> A dotted range times an undotted one lies in the mass-weight six span.

```lean
lemma mul_le_sixSpan_right {V W : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hV : V ≤ rightSpan ![])
    (hW : W ≤ leftSpan ![]) : V * W ≤ sixSpan
```

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightSix_piece_zero_le`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L374).

> The weight-zero piece at mass weight six lies in the span of the mass-weight six families, since
> each of the ten conjugate pairings is a product of an undotted range with a dotted one, in one
> order or the other.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero_le :
    (massWeightSubmoduleGaugeWeightSix).piece 0 ≤ sixSpan
```

**`StandardModel.FermionSector.mem_of_invariant_of_mem_massWeightSubmoduleSix_sup`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L405).

> Mass weight six carries no invariant modulo a stable submodule, there being no Dirac
> mass term. A gauge- and Lorentz-invariant element of `massWeightSubmodule 6 ⊔ S` lies
> in `S`, gauge invariance cutting the hundred pairings of two fermion symbols down to
> the ten conjugate ones and Lorentz invariance killing each of those, its two spinor
> indices being of opposite chirality.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleSix_sup
    {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hS : ∀ (g : GaugeGroupI) (y : fieldData.LocalCovFieldAlgebra), y ∈ S → repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule 6 ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## D. The classification below mass weight eight

> The seven weights between zero and eight are now settled. Weights one, two and four are
> trivial submodules, weights three, five and seven are single fermion towers and carry a
> nonzero hypercharge, and weight six is section F. So between weight zero and weight eight
> the fermion sector has no invariant beyond what `S` already supplies, and the equivalence
> records it.
>
> The lower bound `0 < w` cannot be dropped. Weight zero contains the scalars by
> `one_le_massWeightSubmodule_zero`, and `1` is fixed by both groups, the two
> representations being multiplicative, without lying in any given `S`.

**`StandardModel.FermionSector.mem_of_invariant_massWeightSubmodule_lt_eight_sup`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L440).

> Between mass weight zero and mass weight eight the fermion sector carries no
> invariant. An element of `massWeightSubmodule w ⊔ S` for `0 < w < 8` fixed by both
> groups lies in `S`. Weights one, two and four are trivial, weights three, five and
> seven carry no gauge singlet, and weight six is the missing Dirac mass term.

```lean
lemma mem_of_invariant_massWeightSubmodule_lt_eight_sup (w : ℕ) (hw0 : 0 < w)
    (hw : w < 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.FermionSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L462).

> The classification below mass weight eight as an equivalence, in the shape of
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`. An element of
> `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is
> itself an element of `S` fixed by both groups. The span of invariants that the weight
> eight statement leaves over is here the trivial one, so `x - y` lies in it exactly when
> `x = y`.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.FermionSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean#L481).

> The same classification without the existential. Below mass weight eight an element
> of `massWeightSubmodule w ⊔ S` fixed by both groups is an element of `S` fixed by both
> groups, and conversely.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [The components of the fermion symbols](../part-03/localfieldalgebra-fermionsector-components.md)
- [The gauge weight decomposition of the fermion mass-weight submodules](../part-03/localfieldalgebra-fermionsector-massweight-gauge.md)
- [Equivariant maps out of the tensors of a species](../../../relativity/tensors/equivariant.md)

## Proof depends on

- [The complexified Lorentz group acting on Weyl tensors](../../../relativity/bispinors/complexifiedaction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimLTEight.lean)
