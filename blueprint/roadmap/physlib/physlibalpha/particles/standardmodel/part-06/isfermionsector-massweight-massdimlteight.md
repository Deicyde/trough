---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.IsDualLeftWeyl, StandardModel.IsFermionSector.IsDualRightWeyl, StandardModel.IsFermionSector.IsVectorDualLeftWeyl, StandardModel.IsFermionSector.IsVectorDualRightWeyl, StandardModel.IsFermionSector.isDualLeftRightWeyl_mul, StandardModel.IsFermionSector.isDualLeftRightWeyl_mul_swap, StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_mul, StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_mul_swap
statement: formalized
proof: formalized
---

# The invariants below mass weight eight (IsFermionSector/MassWeight/MassDimLTEight)

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.MassWeight.MassDimLTEight`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean): 41 declarations, 41 with a docstring.

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
> every other pairing having hypercharges that cannot cancel; this is
> `massWeightSubmoduleGaugeWeightSix_piece_zero` of the gauge weight decomposition. Each
> surviving pairing is then a product of two symbols of opposite chirality, one dotted and
> one undotted, since a species and its conjugate always sit in opposite Weyl
> representations. A pair of opposite-chirality spinor indices with nothing else to
> contract against admits no invariant at all — `Lorentz.IsDualLeftRightWeyl.eq_zero_of_invariant`
> — so each pairing contributes nothing and mass weight six is left empty.
>
> That is the absence of a Dirac mass term in the Standard Model, and it is why the fermion
> masses have to come from the Yukawa sector instead: the Higgs doublet supplies the missing
> index, and its own mass weight makes the Yukawa terms weight eight.
>
> The chirality bookkeeping is done once and reused at mass weight eight, in
> `MassDimEight`, which imports this file: the five undotted species are indexed by
> `LeftIdx` and the five dotted ones by `RightIdx`, and `leftComp` and `rightComp` list
> their components with the spinor index singled out.
>
>
> The final statement `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`
> needs `0 < w` as well as `w < 8`: at `w = 0` the mass-weight submodule contains the
> scalars, so `1` is an invariant of weight zero lying in no `S`.

## ii. Key results

> - `LeftIdx` : an index for the components of the five undotted fermion species: the generation
>   together with the colour and isospin the species carries
> - `RightIdx` : an index for the components of the five dotted fermion species: the generation
>   together with the colour and isospin the species carries
> - `leftComp` : the components of the five undotted species at the derivative slots `l`, presented as
>   a two-element family in the spinor index
> - `rightComp` : the components of the five dotted species at the derivative slots `l`, presented as
>   a two-element family in the spinor index
> - `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff` : the classification below
>   mass weight eight as an equivalence, in the shape of
>   `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`: an element of
>   `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is itself an
>   element of `S` fixed by both groups

## iv. References

> * None.

## A. Chiral component families

> A fermion symbol carries exactly one spinor index, and which of the two Weyl
> representations it sits in is fixed by the species. Freezing every other index leaves a
> two-element family of elements of `B`, and the two possible transformation laws are
> recorded here. Both are contragredient, the symbols eating a covector of their value
> space; the dotted law carries the extra complex conjugation.

**`StandardModel.IsFermionSector.IsDualLeftWeyl`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L108).

> A two-element family `X` of elements of `B` carries a dual undotted spinor index: it
> transforms by the contragredient of the left-handed Weyl representation.

```lean
def IsDualLeftWeyl (repLorentz : Representation ℂ SL(2,ℂ) B) (X : Fin 2 → B) : Prop
```

**`StandardModel.IsFermionSector.IsDualRightWeyl`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L114).

> A two-element family `Y` of elements of `B` carries a dual dotted spinor index: it
> transforms by the contragredient of the right-handed Weyl representation, which is the
> conjugate of the undotted law.

```lean
def IsDualRightWeyl (repLorentz : Representation ℂ SL(2,ℂ) B) (Y : Fin 2 → B) : Prop
```

**`StandardModel.IsFermionSector.IsVectorDualLeftWeyl`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L121).

> A family `X` carrying one four-vector index and one dual undotted spinor index: the
> once-derived form of `IsDualLeftWeyl`, the derivative slot moving by the columns of the
> Lorentz matrix. Only the value index of a fermion symbol is dualised, so the derivative
> slot keeps the plain Lorentz law.

```lean
def IsVectorDualLeftWeyl (repLorentz : Representation ℂ SL(2,ℂ) B)
    (X : (Fin 1 ⊕ Fin 3) → Fin 2 → B) : Prop
```

**`StandardModel.IsFermionSector.IsVectorDualRightWeyl`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L128).

> A family `Y` carrying one four-vector index and one dual dotted spinor index: the
> once-derived form of `IsDualRightWeyl`.

```lean
def IsVectorDualRightWeyl (repLorentz : Representation ℂ SL(2,ℂ) B)
    (Y : (Fin 1 ⊕ Fin 3) → Fin 2 → B) : Prop
```

## B. The products of an opposite-chirality pair

> Multiplying an undotted family by a dotted one gives a family of two opposite-chirality
> spinor indices, which is what `Lorentz.IsDualLeftRightWeyl` classifies, and the four
> lemmas here supply that classification in each of the four arrangements that the fermion
> sector produces: the two orders of the product, each with and without a derivative on the
> second factor. The representation being multiplicative is all that is needed, the two
> factors transforming independently.

**`StandardModel.IsFermionSector.isDualLeftRightWeyl_mul`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L152).

> An undotted family times a dotted one is a dual left-right Weyl family.

```lean
lemma isDualLeftRightWeyl_mul {X Y : Fin 2 → B} (hX : IsDualLeftWeyl repLorentz X)
    (hY : IsDualRightWeyl repLorentz Y) :
    IsDualLeftRightWeyl B repLorentz
      (ofPairComponents (k := .downL) (k' := .downR) fun a b => X a * Y b)
```

**`StandardModel.IsFermionSector.isDualLeftRightWeyl_mul_swap`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L166).

> A dotted family times an undotted one is a dual left-right Weyl family, the two
> spinor slots exchanged.

```lean
lemma isDualLeftRightWeyl_mul_swap {X Y : Fin 2 → B} (hX : IsDualRightWeyl repLorentz X)
    (hY : IsDualLeftWeyl repLorentz Y) :
    IsDualLeftRightWeyl B repLorentz
      (ofPairComponents (k := .downL) (k' := .downR) fun a b => X b * Y a)
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_mul`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L181).

> An undotted family times a once-derived dotted one is a vector dual left-right Weyl
> family: the derivative supplies the four-vector index.

```lean
lemma isVectorDualLeftRightWeyl_mul {X : Fin 2 → B} {Y : (Fin 1 ⊕ Fin 3) → Fin 2 → B}
    (hX : IsDualLeftWeyl repLorentz X) (hY : IsVectorDualRightWeyl repLorentz Y) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p => X p.2.1 * Y p.1 p.2.2)
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_mul_swap`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L199).

> A dotted family times a once-derived undotted one is a vector dual left-right Weyl
> family, the two spinor slots exchanged.

```lean
lemma isVectorDualLeftRightWeyl_mul_swap {X : Fin 2 → B} {Y : (Fin 1 ⊕ Fin 3) → Fin 2 → B}
    (hX : IsDualRightWeyl repLorentz X) (hY : IsVectorDualLeftWeyl repLorentz Y) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p => X p.2.2 * Y p.1 p.2.1)
```

## C. Peeling the pair spans off a Lorentz-stable submodule

> A dual left-right Weyl family carries no invariant, so the span of its components, here the
> join of the lines through them, reduces to `⊥`. Each such span is stable under the Lorentz
> group, so `ReducesInvariantsTo.biSup` combines the reductions over a finite family of them,
> as in the gauge sector, and a whole join is discarded from a Lorentz-stable submodule.

**`StandardModel.IsFermionSector.mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L237).

> A finite join of the spans of dual left-right Weyl families carries no Lorentz
> invariant modulo a Lorentz-stable submodule: such a family has no invariant, so each span
> reduces to `⊥`, and `ReducesInvariantsTo.biSup` combines the reductions. A Lorentz
> invariant of the join together with `S` lies in `S`.

```lean
lemma mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span {ι : Type} [DecidableEq ι]
    {T : ι → Fin 2 × Fin 2 → B} (hT : ∀ i, IsDualLeftRightWeyl B repLorentz
      (ofPairComponents (k := .downL) (k' := .downR) fun a b => T i (a, b)))
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (s : Finset ι)
    {x : B} (hx : x ∈ (⨆ i ∈ s, ⨆ l, ℂ ∙ T i l) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_lorentz_invariant_iSup_dualLeftRightWeyl_span`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L252).

> The version of `mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span` joining over a
> whole finite index type.

```lean
lemma mem_of_lorentz_invariant_iSup_dualLeftRightWeyl_span {ι : Type} [Fintype ι]
    [DecidableEq ι] {T : ι → Fin 2 × Fin 2 → B}
    (hT : ∀ i, IsDualLeftRightWeyl B repLorentz
      (ofPairComponents (k := .downL) (k' := .downR) fun a b => T i (a, b))) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, ⨆ l, ℂ ∙ T i l) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## D. The five undotted and the five dotted species

> Each of the ten fermion species sits in one of the two Weyl representations, and a
> species and its conjugate always sit in opposite ones. The five undotted species are
> `bard`, `baru`, `Q`, `L` and `bare`, the five dotted ones `d`, `u`, `barQ`, `barL` and
> `e`. Indexing each list by the generation and the remaining internal indices, `leftComp`
> and `rightComp` present every fermion component as a two-element family in its spinor
> index, which is the shape section A asks for.

**`StandardModel.IsFermionSector.LeftIdx`**, an inductive, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L281).

> An index for the components of the five undotted fermion species: the generation
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

**`StandardModel.IsFermionSector.RightIdx`**, an inductive, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L291).

> An index for the components of the five dotted fermion species: the generation
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

**`StandardModel.IsFermionSector.leftComp`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L328).

> The components of the five undotted species at the derivative slots `l`, presented as
> a two-element family in the spinor index.

```lean
noncomputable def leftComp (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : LeftIdx → Fin 2 → B
```

**`StandardModel.IsFermionSector.rightComp`**, a def, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L340).

> The components of the five dotted species at the derivative slots `l`, presented as a
> two-element family in the spinor index.

```lean
noncomputable def rightComp (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : RightIdx → Fin 2 → B
```

**`StandardModel.IsFermionSector.isDualLeftWeyl_leftComp`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L351).

> Every undotted component family carries a dual undotted spinor index, at zero
> covariant derivatives.

```lean
lemma isDualLeftWeyl_leftComp (i : LeftIdx) :
    IsDualLeftWeyl repLorentz (h.leftComp ![] i)
```

**`StandardModel.IsFermionSector.isDualRightWeyl_rightComp`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L362).

> Every dotted component family carries a dual dotted spinor index, at zero covariant
> derivatives.

```lean
lemma isDualRightWeyl_rightComp (i : RightIdx) :
    IsDualRightWeyl repLorentz (h.rightComp ![] i)
```

## E. The ranges of the symbol maps inside the chirality spans

> A symbol map is determined by its values on a basis of the dual of its value space, so
> its range is the join of the lines through its components; `range_eq_iSup_span` says so.
> Collecting the ten ranges into the two chirality spans is then a matter of naming the
> right index.

**`StandardModel.IsFermionSector.leftSpan`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L384).

> The join of the lines through the components of the five undotted species.

```lean
noncomputable def leftSpan (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : Submodule ℂ B
```

**`StandardModel.IsFermionSector.rightSpan`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L390).

> The join of the lines through the components of the five dotted species.

```lean
noncomputable def rightSpan (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly)
    {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) : Submodule ℂ B
```

**`StandardModel.IsFermionSector.dualBasis_apply`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L396).

> A basis vector of the dual basis is the matching coordinate functional.

```lean
lemma dualBasis_apply {ι M : Type} [AddCommGroup M] [Module ℂ M] [Fintype ι]
    [DecidableEq ι] (b : Module.Basis ι ℂ M) (j : ι) : b.dualBasis j = b.coord j
```

**`StandardModel.IsFermionSector.range_bard_le_leftSpan`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L401).

> The range of the `bard` symbols lies in the undotted span.

```lean
lemma range_bard_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ h.leftSpan l
```

**`StandardModel.IsFermionSector.range_baru_le_leftSpan`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L410).

> The range of the `baru` symbols lies in the undotted span.

```lean
lemma range_baru_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ h.leftSpan l
```

**`StandardModel.IsFermionSector.range_Q_le_leftSpan`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L419).

> The range of the `Q` symbols lies in the undotted span.

```lean
lemma range_Q_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ h.leftSpan l
```

**`StandardModel.IsFermionSector.range_L_le_leftSpan`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L428).

> The range of the `L` symbols lies in the undotted span.

```lean
lemma range_L_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ h.leftSpan l
```

**`StandardModel.IsFermionSector.range_bare_le_leftSpan`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L437).

> The range of the `bare` symbols lies in the undotted span.

```lean
lemma range_bare_le_leftSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ h.leftSpan l
```

**`StandardModel.IsFermionSector.range_d_le_rightSpan`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L446).

> The range of the `d` symbols lies in the dotted span.

```lean
lemma range_d_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ h.rightSpan l
```

**`StandardModel.IsFermionSector.range_u_le_rightSpan`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L455).

> The range of the `u` symbols lies in the dotted span.

```lean
lemma range_u_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ h.rightSpan l
```

**`StandardModel.IsFermionSector.range_barQ_le_rightSpan`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L464).

> The range of the `barQ` symbols lies in the dotted span.

```lean
lemma range_barQ_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ h.rightSpan l
```

**`StandardModel.IsFermionSector.range_barL_le_rightSpan`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L473).

> The range of the `barL` symbols lies in the dotted span.

```lean
lemma range_barL_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ h.rightSpan l
```

**`StandardModel.IsFermionSector.range_e_le_rightSpan`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L482).

> The range of the `e` symbols lies in the dotted span.

```lean
lemma range_e_le_rightSpan (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ h.rightSpan l
```

## F. Gauge invariants and the weight-zero piece

> Gauge invariance is what selects the conjugate pairings. A gauge-invariant element lies
> in the weight-zero piece of the gauge weight decomposition, and modulo a gauge-stable
> submodule the same holds with the submodule joined on: the torus generators scale every
> other weight, and `GaugeWeightDecomposition.reducesInvariantsTo_piece_zero` deletes them
> one piece at a time. Unlike the single-tower case, the generator has to be chosen weight by
> weight: a product like `Q barQ` at two different colours has vanishing hypercharge and
> nonzero colour, so no one generator sees every weight.

## G. Mass weight six: no Dirac mass term

> Mass weight six is the product of two underived fermion towers. Gauge invariance puts
> such an invariant in the weight-zero piece, which section F of the gauge weight
> decomposition writes as the ten conjugate pairings, and every one of those is an undotted
> component times a dotted one. Section B turns each into a dual left-right Weyl family and
> section C peels the lot off, leaving nothing.
>
> The physics is that the Standard Model has no Dirac mass term. A mass term pairs a
> left-handed field with a right-handed one, and while such a pair is exactly what survives
> the gauge cut, its two spinor indices have nothing to contract against: a dotted index
> and an undotted one carry no invariant pairing, only the symplectic form pairs two indices
> of the same chirality. The fermion masses have to come from somewhere else, and they do —
> from the Yukawa sector, where the Higgs doublet supplies the missing index.

**`StandardModel.IsFermionSector.mul_le_iSup_span_pair`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L526).

> If `V` lies in the join of the lines through an undotted family and `W` in the join
> for a dotted one, the product lies in the join of the spans of the pair families.

```lean
lemma mul_le_iSup_span_pair {ι κ : Type} {X : ι → Fin 2 → B} {Y : κ → Fin 2 → B}
    {V W : Submodule ℂ B} (hV : V ≤ ⨆ (i : ι) (a : Fin 2), ℂ ∙ X i a)
    (hW : W ≤ ⨆ (j : κ) (a : Fin 2), ℂ ∙ Y j a) :
    V * W ≤ ⨆ (p : ι × κ) (l : Fin 2 × Fin 2), ℂ ∙ (X p.1 l.1 * Y p.2 l.2)
```

**`StandardModel.IsFermionSector.mul_le_iSup_span_pair_swap`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L538).

> The mirror of `mul_le_iSup_span_pair` with the two spinor slots exchanged, for a
> product whose left factor is the dotted one.

```lean
lemma mul_le_iSup_span_pair_swap {ι κ : Type} {X : ι → Fin 2 → B} {Y : κ → Fin 2 → B}
    {V W : Submodule ℂ B} (hV : V ≤ ⨆ (i : ι) (a : Fin 2), ℂ ∙ X i a)
    (hW : W ≤ ⨆ (j : κ) (a : Fin 2), ℂ ∙ Y j a) :
    V * W ≤ ⨆ (p : ι × κ) (l : Fin 2 × Fin 2), ℂ ∙ (X p.1 l.2 * Y p.2 l.1)
```

**`StandardModel.IsFermionSector.sixFamily`**, a def, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L551).

> The mass-weight six families: a product of two underived components of opposite
> chirality, in either order.

```lean
noncomputable def sixFamily (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) :
    (LeftIdx × RightIdx) ⊕ (RightIdx × LeftIdx) → Fin 2 × Fin 2 → B
```

**`StandardModel.IsFermionSector.sixSpan`**, a def, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L558).

> The join of the spans of the mass-weight six families.

```lean
noncomputable def sixSpan (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isDualLeftRightWeyl_sixFamily`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L567).

> Each mass-weight six family carries one dual undotted and one dual dotted spinor
> index.

```lean
lemma isDualLeftRightWeyl_sixFamily
    (i : (LeftIdx × RightIdx) ⊕ (RightIdx × LeftIdx)) :
    IsDualLeftRightWeyl B repLorentz
      (ofPairComponents (k := .downL) (k' := .downR) fun a b => h.sixFamily i (a, b))
```

**`StandardModel.IsFermionSector.mul_le_sixSpan_left`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L581).

> An undotted range times a dotted one lies in the mass-weight six span.

```lean
lemma mul_le_sixSpan_left {V W : Submodule ℂ B} (hV : V ≤ h.leftSpan ![])
    (hW : W ≤ h.rightSpan ![]) : V * W ≤ h.sixSpan
```

**`StandardModel.IsFermionSector.mul_le_sixSpan_right`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L588).

> A dotted range times an undotted one lies in the mass-weight six span.

```lean
lemma mul_le_sixSpan_right {V W : Submodule ℂ B} (hV : V ≤ h.rightSpan ![])
    (hW : W ≤ h.leftSpan ![]) : V * W ≤ h.sixSpan
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSix_piece_zero_le`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L597).

> The weight-zero piece at mass weight six lies in the span of the mass-weight six
> families: each of the ten conjugate pairings is a product of an undotted range with a
> dotted one, in one order or the other.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero_le :
    (h.massWeightSubmoduleGaugeWeightSix).piece 0 ≤ h.sixSpan
```

**`StandardModel.IsFermionSector.mem_of_invariant_of_mem_massWeightSubmoduleSix_sup`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L629).

> Mass weight six carries no invariant modulo a stable submodule: there is no Dirac
> mass term. A gauge- and Lorentz-invariant element of `massWeightSubmodule 6 ⊔ S` lies
> in `S`, gauge invariance cutting the hundred pairings of two fermion symbols down to
> the ten conjugate ones and Lorentz invariance killing each of those, its two spinor
> indices being of opposite chirality.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleSix_sup {S : Submodule ℂ B}
    (hS : ∀ (g : GaugeGroupI) (y : B), y ∈ S → repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule 6 ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## H. The classification below mass weight eight

> The seven weights between zero and eight are now settled: weights one, two and four are
> trivial submodules, weights three, five and seven are single fermion towers and carry a
> nonzero hypercharge, and weight six is section G. So between weight zero and weight eight
> the fermion sector has no invariant beyond what `S` already supplies, and the equivalence
> records it.
>
> The lower bound `0 < w` cannot be dropped. Weight zero contains the scalars by
> `one_le_massWeightSubmodule_zero`, and `1` is fixed by both groups, the two
> representations being multiplicative, without lying in any given `S`.

**`StandardModel.IsFermionSector.mem_of_invariant_massWeightSubmodule_lt_eight_sup`**, a lemma, [line 664](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L664).

> Between mass weight zero and mass weight eight the fermion sector carries no
> invariant: an element of `massWeightSubmodule w ⊔ S` for `0 < w < 8` fixed by both
> groups lies in `S`. Weights one, two and four are trivial, weights three, five and
> seven carry no gauge singlet, and weight six is the missing Dirac mass term.

```lean
lemma mem_of_invariant_massWeightSubmodule_lt_eight_sup (w : ℕ) (hw0 : 0 < w)
    (hw : w < 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L687).

> The classification below mass weight eight as an equivalence, in the shape of
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`: an element of
> `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is
> itself an element of `S` fixed by both groups. The span of invariants that the weight
> eight statement leaves over is here the trivial one, so `x - y` lies in it exactly when
> `x = y`.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.IsFermionSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 707](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean#L707).

> The same classification without the existential: below mass weight eight an element
> of `massWeightSubmodule w ⊔ S` fixed by both groups is an element of `S` fixed by both
> groups, and conversely.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [The components of the fermion symbols](../part-05/isfermionsector-components.md)
- [The gauge weight decomposition of the fermion mass-weight submodules](../part-05/isfermionsector-massweight-gaugeweight.md)
- [Lorentz invariants of two Weyl indices of the same kind](../../../relativity/lorentzgroup/invariants-isbileftweyl.md)
- [Lorentz invariants of a left-handed and a right-handed Weyl index](../../../relativity/lorentzgroup/invariants-isleftrightweyl.md)
- [Lorentz invariants of a four-vector index and a left-right Weyl pair](../../../relativity/lorentzgroup/invariants-isvectorleftrightweyl.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimLTEight.lean)
