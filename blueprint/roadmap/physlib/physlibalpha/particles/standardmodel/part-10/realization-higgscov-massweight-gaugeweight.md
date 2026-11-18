---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOdd, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOne, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightTwo, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightThree, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightFour, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightFive, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightSix, StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightSeven
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the Higgs mass-weight submodules

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.MassWeight.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean): 69 declarations, 69 with a docstring; 3 private, not shown.

## i. Overview

> Each mass-weight submodule of the Higgs sector up to weight eight has an explicit
> description in terms of the derivative submodules `derivSubmodule n`, and each derivative
> submodule carries a gauge weight decomposition.  Transporting the latter along the former
> decomposes every mass-weight submodule up to weight eight.
>
> The weights carried by a derivative submodule are the four weights of the Higgs doublet
> and its conjugate, `(0, 0, ∓1, -3)` and `(0, 0, ±1, 3)`.  Every one of them has
> hypercharge `± 3`, so a product of `k` derivative submodules can only reach gauge weight
> zero when `k` is even and the Higgs and conjugate-Higgs factors are equally many.  This
> is what makes the weight-zero pieces small: at mass weight four and six they are spanned
> by the isospin-diagonal pairings `∇H^i ∇H̄^i`, and at mass weight eight the quartic
> monomials `∇H^i ∇H̄^i ∇H^j ∇H̄^j` join them.
>
> The gauge weight alone cannot finish the job: it cannot separate the isospin singlet
> `∇H · ∇H̄` from the neutral component of the isospin triplet, which carries the same
> weight.  That separation is `SU(2)` mathematics and belongs to the isospin classifiers of
> `GaugeGroup.Invariants` rather than here.  What is left for this file is to present each
> surviving piece as a family those classifiers know.  A conjugate Higgs symbol against a
> Higgs symbol is an `IsSU2FundamentalAntiFundamental` family — the conjugate symbol carries
> the fundamental isospin index and the Higgs symbol the anti-fundamental one, so it goes
> second — and the delta contraction, which spans its invariants, is the isospin contraction
> `dotGaugeHiggs`.  The quartic is an `IsSU2QuadFundamental` family once its two Higgs
> symbols are re-indexed by the antisymmetric symbol, and of its two epsilon contractions
> one is the square of the isospin contraction and the other vanishes, pairing commuting
> factors antisymmetrically.
>
>
> Sections G and H are reductions for the gauge group, stated modulo any gauge-stable
> submodule `S`, which is what lets the other sectors be carried along; taking `S` trivial in
> section I recovers the statements about the mass-weight submodules themselves.

## ii. Key results

> - `massWeightSubmoduleGaugeWeightOdd` : the odd mass-weight submodules are trivial, so they carry
>   the empty decomposition
> - `massWeightSubmoduleGaugeWeightOne` : weight one is trivial
> - `massWeightSubmoduleGaugeWeightTwo` : weight two is the underived Higgs tower
> - `massWeightSubmoduleGaugeWeightThree` : weight three is trivial

## iv. References

> * None.

## A. The decompositions

> Every term of the Higgs algebra has even mass weight, so the odd mass-weight submodules
> vanish and are decomposed by the empty decomposition.  The even ones are built from the
> derivative submodules by the descriptions of `MassWeight.Basic`: weight two is a single
> derivative submodule, and the higher weights add the products which distribute the mass
> weight over several towers.

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOdd`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L104).

> The odd mass-weight submodules are trivial, so they carry the empty decomposition.

```lean
noncomputable def massWeightSubmoduleGaugeWeightOdd (n : ℕ) (hn : Odd n) :
    GaugeWeightDecomposition rep (h.massWeightSubmodule n)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOne`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L111).

> Weight one is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightOne :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 1)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightTwo`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L117).

> Weight two is the underived Higgs tower.

```lean
noncomputable def massWeightSubmoduleGaugeWeightTwo :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 2)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightThree`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L124).

> Weight three is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightThree :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 3)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightFour`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L131).

> Weight four is the once-derived tower together with the products of two underived
> ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFour :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 4)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightFive`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L141).

> Weight five is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFive :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 5)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightSix`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L148).

> Weight six is the twice-derived tower, the once-derived tower against an underived
> one, and the products of three underived ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSix :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 6)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightSeven`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L163).

> Weight seven is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSeven :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 7)
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightEight`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L171).

> Weight eight: the thrice-derived tower, the two ways of splitting the derivatives over
> two towers, the once-derived tower against two underived ones, and the products of four
> underived ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightEight :
    GaugeWeightDecomposition rep (h.massWeightSubmodule 8)
```

## B. The pieces of a derivative submodule

> A derivative submodule is the join of a Higgs and a conjugate-Higgs submodule, and each of
> those is concentrated in two weights.  The four weights are distinct, so each piece of the
> join is the span of one of the four families of symbols, and every other weight — the zero
> weight in particular — has vanishing piece.

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_eq`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L207).

> The weight-`w` piece of a derivative submodule, as the join of the Higgs and
> conjugate-Higgs pieces.

```lean
lemma derivSubmoduleGaugeWeight_piece_eq (n : ℕ) (w : GaugeWeight) :
    (h.derivSubmoduleGaugeWeight n).piece w
      = (if w = ((0, 0, -1, -3) : GaugeWeight) then
          ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.higgs d 0
        else if w = ((0, 0, 1, -3) : GaugeWeight) then
          ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.higgs d 1
        else ⊥)
        ⊔ (if w = ((0, 0, 1, 3) : GaugeWeight) then
            ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.barHiggs d 0
          else if w = ((0, 0, -1, 3) : GaugeWeight) then
            ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.barHiggs d 1
          else ⊥)
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_higgs_zero`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L221).

> The piece at the weight of the upper Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_higgs_zero (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece (0, 0, -1, -3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.higgs d 0
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_higgs_one`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L228).

> The piece at the weight of the lower Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_higgs_one (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece (0, 0, 1, -3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.higgs d 1
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_barHiggs_zero`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L235).

> The piece at the weight of the upper conjugate-Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_barHiggs_zero (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece (0, 0, 1, 3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.barHiggs d 0
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_barHiggs_one`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L242).

> The piece at the weight of the lower conjugate-Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_barHiggs_one (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece (0, 0, -1, 3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ h.barHiggs d 1
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmoduleGaugeWeight_piece_zero`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L250).

> A derivative submodule has no weight-zero content: every Higgs symbol carries
> hypercharge.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece 0 = ⊥
```

## C. The weight-zero pieces of the products

> Two derivative submodules pair to weight zero exactly by matching a Higgs symbol against a
> conjugate-Higgs symbol of the same isospin component, in either order, so the weight-zero
> piece of such a product is a join of four spans of pairings `∇H^i ∇H̄^i`.  Three of them
> cannot reach weight zero at all, because hypercharge is `± 3` on every generator, so an odd
> number of factors leaves an odd multiple of three.  Four of them reach weight zero on the
> three quartic monomials.

**`StandardModel.HiggsAlgebraCovRealization.higgsBarHiggsSpan`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L270).

> The span of the isospin-diagonal pairings of a Higgs symbol carrying `n` derivatives
> with a conjugate-Higgs symbol carrying `m` derivatives, at isospin component `i`.

```lean
noncomputable def higgsBarHiggsSpan (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    (n m : ℕ) (i : Fin 2) : Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.quarticSpan`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L277).

> The span of the underived quartic monomial pairing the isospin components `i` and
> `j`.

```lean
noncomputable def quarticSpan (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    (i j : Fin 2) : Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmodule_mul_piece_zero`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L283).

> The weight-zero piece of a product of two derivative submodules: the isospin-diagonal
> pairings, taken in both orders of the two towers.

```lean
lemma derivSubmodule_mul_piece_zero (n m : ℕ) :
    GaugeWeightDecomposition.piece rep (h.derivSubmodule n * h.derivSubmodule m) 0
      = h.higgsBarHiggsSpan n m 0 ⊔ h.higgsBarHiggsSpan n m 1
        ⊔ h.higgsBarHiggsSpan m n 0 ⊔ h.higgsBarHiggsSpan m n 1
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmodule_mul_mul_piece_zero`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L307).

> A product of three derivative submodules has no weight-zero content: the hypercharge of
> three Higgs generators is an odd multiple of three.

```lean
lemma derivSubmodule_mul_mul_piece_zero (n m k : ℕ) :
    GaugeWeightDecomposition.piece rep
      (h.derivSubmodule n * h.derivSubmodule m * h.derivSubmodule k) 0 = ⊥
```

**`StandardModel.HiggsAlgebraCovRealization.derivSubmodule_zero_pow_four_piece_zero`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L320).

> The weight-zero piece of the product of four underived derivative submodules: the three
> quartic monomials, the ones pairing two Higgs symbols against two conjugate ones with
> matching isospin.

```lean
lemma derivSubmodule_zero_pow_four_piece_zero :
    GaugeWeightDecomposition.piece rep
      (h.derivSubmodule 0 * h.derivSubmodule 0 * h.derivSubmodule 0
        * h.derivSubmodule 0) 0
      = h.quarticSpan 0 0 ⊔ h.quarticSpan 0 1 ⊔ h.quarticSpan 1 1
```

## D. The weight-zero pieces of the mass-weight submodules

> Assembling section C along the descriptions of section A gives the weight-zero piece of
> each mass-weight submodule up to weight eight.  The odd weights and weight two are trivial,
> weight four is the underived pairing, weight six adds the pairings with one derivative on
> either factor, and weight eight adds the pairings with two derivatives, those with one
> derivative on each factor, and the three quartic monomials.

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightOdd_piece_zero`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L366).

> The weight-zero piece at an odd mass weight: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightOdd_piece_zero (n : ℕ) (hn : Odd n) :
    (h.massWeightSubmoduleGaugeWeightOdd n hn).piece 0 = ⊥
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightTwo_piece_zero`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L371).

> The weight-zero piece at mass weight two: a single Higgs symbol carries
> hypercharge.

```lean
lemma massWeightSubmoduleGaugeWeightTwo_piece_zero :
    (h.massWeightSubmoduleGaugeWeightTwo).piece 0 = ⊥
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightFour_piece_zero`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L376).

> The weight-zero piece at mass weight four: the underived isospin-diagonal pairings.

```lean
lemma massWeightSubmoduleGaugeWeightFour_piece_zero :
    (h.massWeightSubmoduleGaugeWeightFour).piece 0
      = h.higgsBarHiggsSpan 0 0 0 ⊔ h.higgsBarHiggsSpan 0 0 1
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightSix_piece_zero`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L387).

> The weight-zero piece at mass weight six: the isospin-diagonal pairings carrying one
> derivative, on either of the two factors.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero :
    (h.massWeightSubmoduleGaugeWeightSix).piece 0
      = h.higgsBarHiggsSpan 1 0 0 ⊔ h.higgsBarHiggsSpan 1 0 1
        ⊔ h.higgsBarHiggsSpan 0 1 0 ⊔ h.higgsBarHiggsSpan 0 1 1
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmoduleGaugeWeightEight_piece_zero`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L400).

> The weight-zero piece at mass weight eight: the isospin-diagonal pairings carrying two
> derivatives on one factor or one on each, together with the three quartic monomials.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero :
    (h.massWeightSubmoduleGaugeWeightEight).piece 0
      = h.higgsBarHiggsSpan 2 0 0 ⊔ h.higgsBarHiggsSpan 2 0 1
        ⊔ h.higgsBarHiggsSpan 0 2 0 ⊔ h.higgsBarHiggsSpan 0 2 1
        ⊔ (h.higgsBarHiggsSpan 1 1 0 ⊔ h.higgsBarHiggsSpan 1 1 1)
        ⊔ (h.quarticSpan 0 0 ⊔ h.quarticSpan 0 1 ⊔ h.quarticSpan 1 1)
```

## E. The gauge sieve

> A gauge-invariant element is fixed by the gauge torus, so it sits in the weight-zero piece
> of any decomposition of a submodule containing it.  Section D therefore bounds the
> invariants of each mass-weight submodule up to weight eight.  The bound is a sieve, not a
> characterisation: the gauge torus cannot separate the isospin singlet from the neutral
> component of the isospin triplet, and that separation needs the Weyl element of `SU(2)`.

**`StandardModel.HiggsAlgebraCovRealization.eq_zero_of_invariant_massWeightSubmodule_odd`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L433).

> A gauge-invariant term of odd mass weight vanishes.

```lean
lemma eq_zero_of_invariant_massWeightSubmodule_odd (n : ℕ) (hn : Odd n) {x : B}
    (hx : x ∈ h.massWeightSubmodule n) : x = 0
```

**`StandardModel.HiggsAlgebraCovRealization.eq_zero_of_invariant_massWeightSubmodule_two`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L439).

> A gauge-invariant term of mass weight two vanishes: a single Higgs symbol carries
> hypercharge, so nothing at that weight is neutral.

```lean
lemma eq_zero_of_invariant_massWeightSubmodule_two {x : B}
    (hx : x ∈ h.massWeightSubmodule 2) (hg : ∀ g : GaugeGroupI, rep g x = x) : x = 0
```

**`StandardModel.HiggsAlgebraCovRealization.mem_of_invariant_massWeightSubmodule_four`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L447).

> A gauge-invariant term of mass weight four is a combination of the two underived
> isospin-diagonal pairings.

```lean
lemma mem_of_invariant_massWeightSubmodule_four {x : B}
    (hx : x ∈ h.massWeightSubmodule 4) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.higgsBarHiggsSpan 0 0 0 ⊔ h.higgsBarHiggsSpan 0 0 1
```

**`StandardModel.HiggsAlgebraCovRealization.mem_of_invariant_massWeightSubmodule_six`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L455).

> A gauge-invariant term of mass weight six is a combination of the isospin-diagonal
> pairings carrying one derivative, on either factor.

```lean
lemma mem_of_invariant_massWeightSubmodule_six {x : B}
    (hx : x ∈ h.massWeightSubmodule 6) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.higgsBarHiggsSpan 1 0 0 ⊔ h.higgsBarHiggsSpan 1 0 1
      ⊔ h.higgsBarHiggsSpan 0 1 0 ⊔ h.higgsBarHiggsSpan 0 1 1
```

**`StandardModel.HiggsAlgebraCovRealization.mem_of_invariant_massWeightSubmodule_eight`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L464).

> A gauge-invariant term of mass weight eight is a combination of the isospin-diagonal
> pairings carrying two derivatives and of the three quartic monomials.

```lean
lemma mem_of_invariant_massWeightSubmodule_eight {x : B}
    (hx : x ∈ h.massWeightSubmodule 8) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.higgsBarHiggsSpan 2 0 0 ⊔ h.higgsBarHiggsSpan 2 0 1
      ⊔ h.higgsBarHiggsSpan 0 2 0 ⊔ h.higgsBarHiggsSpan 0 2 1
      ⊔ (h.higgsBarHiggsSpan 1 1 0 ⊔ h.higgsBarHiggsSpan 1 1 1)
      ⊔ (h.quarticSpan 0 0 ⊔ h.quarticSpan 0 1 ⊔ h.quarticSpan 1 1)
```

## F. The Higgs symbols as isospin families

> The gauge weight has done all it can.  What it cannot see is the difference between the
> isospin singlet `∇H · ∇H̄` and the neutral component of the isospin triplet: both are
> neutral under the torus, so both sit in the weight-zero piece, and only the non-abelian
> part of `SU(2)` tells them apart.  That is what the isospin classifiers of
> `GaugeGroup.Invariants` are for, and this section presents the surviving pieces as
> families they classify.
>
> The variance has to be read off correctly, and it is opposite to what the notation
> suggests.  A conjugate Higgs symbol carries a fundamental isospin index — an isospin
> transformation moves it by the matrix of the `SU(2)` element, with the summed index in the
> row slot — and a Higgs symbol carries an anti-fundamental one, moved by the conjugate
> matrix.  So the pairing span of section C is the span of the components of
> `fun l => h.barHiggs d' (l 0) * h.higgs d (l 1)`, conjugate symbol first, which is an
> `IsSU2FundamentalAntiFundamental` family; and its delta contraction, which spans its
> invariants, is the isospin contraction `dotGaugeHiggs`.  That identification is the whole
> point of the section: `dotSpan` is the span of delta contractions, and nothing else
> survives.
>
> The quartic needs four fundamental indices, so its two Higgs symbols must be re-indexed by
> the antisymmetric symbol first.  `tildeHiggs` is that re-index, `H̃⁰ = H¹` and
> `H̃¹ = -H⁰`, and it is fundamental because `SU(2)` is pseudo-real.  The quartic family is
> then a product of four fundamental families, and `IsSU2QuadFundamental` classifies it.  Its
> two epsilon contractions come out as the square of the isospin contraction and zero:
> the second pairs the two conjugate symbols with each other and the two Higgs symbols with
> each other, and an antisymmetric contraction of two commuting factors vanishes.

**`StandardModel.HiggsAlgebraCovRealization.su2_inv_apply`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L507).

> The entries of the inverse of an `SU(2)` element are the conjugated transposed
> entries, the inverse of a unitary matrix being its conjugate transpose.

```lean
lemma su2_inv_apply (V : specialUnitaryGroup (Fin 2) ℂ) (a b : Fin 2) :
    (V⁻¹).1 a b = conj (V.1 b a)
```

**`StandardModel.HiggsAlgebraCovRealization.rep_su2_higgs`**, a lemma, [line 515](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L515).

> An isospin transformation moves the isospin index of a Higgs symbol by the conjugate
> matrix: the index of a Higgs symbol is anti-fundamental.

```lean
lemma rep_su2_higgs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    rep ((1, V, 1) : GaugeGroupI) (h.higgs d i)
      = ∑ a, conj (V.1 a i) • h.higgs d a
```

**`StandardModel.HiggsAlgebraCovRealization.rep_su2_barHiggs`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L529).

> An isospin transformation moves the isospin index of a conjugate Higgs symbol by the
> matrix itself: the index of a conjugate Higgs symbol is fundamental.

```lean
lemma rep_su2_barHiggs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    rep ((1, V, 1) : GaugeGroupI) (h.barHiggs d i)
      = ∑ a, V.1 a i • h.barHiggs d a
```

**`StandardModel.HiggsAlgebraCovRealization.rep_mul_pair`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L543).

> A product of two symbols each moving by given coefficients moves by the product of
> those coefficients.

```lean
lemma rep_mul_pair (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {X : ι → B} {Y : κ → B} {x₀ : ι} {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hX : rep g (X x₀) = ∑ x, cX x • X x) (hY : rep g (Y y₀) = ∑ y, cY y • Y y) :
    rep g (X x₀ * Y y₀) = ∑ x, ∑ y, (cX x * cY y) • (X x * Y y)
```

**`StandardModel.HiggsAlgebraCovRealization.higgs_mul_barHiggs_comm`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L552).

> A Higgs symbol commutes with a conjugate Higgs symbol, in the components.

```lean
lemma higgs_mul_barHiggs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    h.higgs d i * h.barHiggs d' j = h.barHiggs d' j * h.higgs d i
```

**`StandardModel.HiggsAlgebraCovRealization.higgs_mul_higgs_comm`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L559).

> Two Higgs symbols commute, in the components.

```lean
lemma higgs_mul_higgs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    h.higgs d i * h.higgs d' j = h.higgs d' j * h.higgs d i
```

**`StandardModel.HiggsAlgebraCovRealization.barHiggs_mul_barHiggs_comm`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L566).

> Two conjugate Higgs symbols commute, in the components.

```lean
lemma barHiggs_mul_barHiggs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    h.barHiggs d i * h.barHiggs d' j = h.barHiggs d' j * h.barHiggs d i
```

**`StandardModel.HiggsAlgebraCovRealization.isoFamily`**, a def, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L574).

> The isospin family of a Higgs tower carrying `n` derivatives against a conjugate tower
> carrying `m`: the conjugate symbol supplies the fundamental index and so goes in the
> first slot, the Higgs symbol the anti-fundamental one.

```lean
noncomputable def isoFamily (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) : (Fin 2 → Fin 2) → B
```

**`StandardModel.HiggsAlgebraCovRealization.isSU2FundamentalAntiFundamental_isoFamily`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L581).

> The isospin family carries one fundamental and one anti-fundamental isospin index.

```lean
lemma isSU2FundamentalAntiFundamental_isoFamily {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) : IsSU2FundamentalAntiFundamental B rep (h.isoFamily d d')
```

**`StandardModel.HiggsAlgebraCovRealization.deltaContraction_isoFamily`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L590).

> The delta contraction of the isospin family, which spans its isospin invariants, is the
> isospin contraction: the Higgs mass term of the two towers.

```lean
lemma deltaContraction_isoFamily {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) :
    IsSU2FundamentalAntiFundamental.deltaContraction (h.isoFamily d d') = h.dotGaugeHiggs d d'
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan`**, a def, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L600).

> The span of the isospin contractions of a Higgs tower carrying `n` derivatives against
> a conjugate tower carrying `m`: the gauge invariants the isospin classification leaves
> at those two derivative orders.

```lean
noncomputable def dotSpan (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    (n m : ℕ) : Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.isoFamily_span_stable`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L607).

> The span of the isospin family is stable under the whole gauge group: each factor of a
> component goes to a combination of the factors of components.

```lean
lemma isoFamily_span_stable {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (g : GaugeGroupI) {y : B}
    (hy : y ∈ Submodule.span ℂ (Set.range (h.isoFamily d d'))) :
    rep g y ∈ Submodule.span ℂ (Set.range (h.isoFamily d d'))
```

**`StandardModel.HiggsAlgebraCovRealization.higgsBarHiggsSpan_le_isoFamily_span`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L623).

> The isospin-diagonal pairing spans of section C sit inside the span of the isospin
> family: a diagonal pairing is one of the four components, the two factors commuting.

```lean
lemma higgsBarHiggsSpan_le_isoFamily_span (n m : ℕ) :
    h.higgsBarHiggsSpan n m 0 ⊔ h.higgsBarHiggsSpan n m 1
      ≤ ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (d' : Fin m → (Fin 1 ⊕ Fin 3)),
        Submodule.span ℂ (Set.range (h.isoFamily d d'))
```

**`StandardModel.HiggsAlgebraCovRealization.tildeHiggs`**, a def, [line 642](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L642).

> The re-index of an underived Higgs symbol by the antisymmetric symbol, `H̃⁰ = H¹` and
> `H̃¹ = -H⁰`.  `SU(2)` is pseudo-real, so this turns the anti-fundamental index of a Higgs
> symbol into a fundamental one, which is what the quartic family needs.

```lean
noncomputable def tildeHiggs (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
  (i : Fin 2) : B
```

**`StandardModel.HiggsAlgebraCovRealization.tildeHiggs_zero`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L647).

> The re-index at isospin zero is the Higgs symbol of isospin one.

```lean
lemma tildeHiggs_zero :
    h.tildeHiggs 0 = h.higgs (![] : Fin 0 → (Fin 1 ⊕ Fin 3)) 1
```

**`StandardModel.HiggsAlgebraCovRealization.tildeHiggs_one`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L652).

> The re-index at isospin one is minus the Higgs symbol of isospin zero.

```lean
lemma tildeHiggs_one :
    h.tildeHiggs 1 = -h.higgs (![] : Fin 0 → (Fin 1 ⊕ Fin 3)) 0
```

**`StandardModel.HiggsAlgebraCovRealization.rep_su2_tildeHiggs`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L659).

> The re-indexed Higgs symbol carries a fundamental isospin index: the four entry
> identities of `GaugeGroup.SU2Conjugation` remove every complex conjugate.

```lean
lemma rep_su2_tildeHiggs (V : specialUnitaryGroup (Fin 2) ℂ) (i : Fin 2) :
    rep ((1, V, 1) : GaugeGroupI) (h.tildeHiggs i)
      = ∑ a, V.1 a i • h.tildeHiggs a
```

**`StandardModel.HiggsAlgebraCovRealization.quadFamily`**, a def, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L677).

> The quartic isospin family: two conjugate Higgs symbols against two re-indexed Higgs
> symbols, each of the four carrying a fundamental isospin index.

```lean
noncomputable def quadFamily (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) :
    (Fin 4 → Fin 2) → B
```

**`StandardModel.HiggsAlgebraCovRealization.isSU2QuadFundamental_quadFamily`**, a lemma, [line 685](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L685).

> The quartic family carries four fundamental isospin indices.

```lean
lemma isSU2QuadFundamental_quadFamily : IsSU2QuadFundamental B rep h.quadFamily
```

**`StandardModel.HiggsAlgebraCovRealization.epsilonContraction₁₂_quadFamily`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L721).

> The first epsilon contraction of the quartic family is the square of the isospin
> contraction: pairing the first conjugate symbol with the first Higgs symbol, and the
> second with the second, is pairing each `H̄` with an `H`.

```lean
lemma epsilonContraction₁₂_quadFamily :
    IsSU2QuadFundamental.epsilonContraction₁₂ h.quadFamily
      = h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![]
```

**`StandardModel.HiggsAlgebraCovRealization.epsilonContraction₁₃_quadFamily`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L735).

> The second epsilon contraction of the quartic family vanishes: it pairs the two
> conjugate symbols with each other and the two Higgs symbols with each other, and an
> antisymmetric contraction of two commuting factors is zero.

```lean
lemma epsilonContraction₁₃_quadFamily :
    IsSU2QuadFundamental.epsilonContraction₁₃ h.quadFamily = 0
```

**`StandardModel.HiggsAlgebraCovRealization.quarticSpan_le_quadFamily_span`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L746).

> The three quartic monomials of section C lie in the span of the components of the
> quartic family, each being one of those components up to a sign.

```lean
lemma quarticSpan_le_quadFamily_span :
    h.quarticSpan 0 0 ⊔ h.quarticSpan 0 1 ⊔ h.quarticSpan 1 1
      ≤ Submodule.span ℂ (Set.range h.quadFamily)
```

## G. The isospin spans reduce to the isospin contractions

> The classification is wanted not for the mass-weight submodule alone but modulo a
> submodule `S` gathering the other sectors, so every step is a reduction in the sense of
> `ReducesInvariantsTo`: a gauge invariant of `V ⊔ S`, for `S` gauge stable, lies in `W ⊔ S`.
>
> The weight-zero pieces of section D are joins of spans of isospin families.
> `IsSU2FundamentalAntiFundamental.reducesInvariantsTo_span_deltaContraction` reduces each
> span, for the isospin factor and hence for the gauge group, to the line through its delta
> contraction, and `ReducesInvariantsTo.iSup` joins the families. The join asks each span to
> be gauge stable, which is `isoFamily_span_stable` and is why the enlargement is `isoSpan`
> rather than the pairing span of section C: the pairing span keeps only the diagonal
> components and a gauge transformation does not. It asks the target to be gauge stable too,
> and the isospin contractions are gauge invariant.

**`StandardModel.HiggsAlgebraCovRealization.isoSpan`**, a def, [line 796](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L796).

> The span of the components of all the isospin families of a Higgs tower carrying `n`
> derivatives against a conjugate tower carrying `m`.  This is the gauge-stable
> enlargement of the pairing span of section C.

```lean
noncomputable def isoSpan (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    (n m : ℕ) : Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.isStableUnder_isoSpan`**, a lemma, [line 803](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L803).

> The isospin span is stable under the gauge group.

```lean
lemma isStableUnder_isoSpan (n m : ℕ) :
    IsStableUnder (fun g : GaugeGroupI => rep g) (h.isoSpan n m)
```

**`StandardModel.HiggsAlgebraCovRealization.isFixedBy_dotSpan`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L810).

> The span of the isospin contractions is fixed pointwise by the gauge group.

```lean
lemma isFixedBy_dotSpan (n m : ℕ) :
    IsFixedBy (fun g : GaugeGroupI => rep g) (h.dotSpan n m)
```

**`StandardModel.HiggsAlgebraCovRealization.higgsBarHiggsSpan_le_isoSpan'`**, a lemma, [line 816](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L816).

> Each isospin-diagonal pairing span of section C sits inside the isospin span.

```lean
lemma higgsBarHiggsSpan_le_isoSpan' (n m : ℕ) (i : Fin 2) :
    h.higgsBarHiggsSpan n m i ≤ h.isoSpan n m
```

**`StandardModel.HiggsAlgebraCovRealization.higgsBarHiggsSpan_le_isoSpan`**, a lemma, [line 826](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L826).

> The pairing span of section C sits inside the isospin span.

```lean
lemma higgsBarHiggsSpan_le_isoSpan (n m : ℕ) :
    h.higgsBarHiggsSpan n m 0 ⊔ h.higgsBarHiggsSpan n m 1 ≤ h.isoSpan n m
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_isoSpan`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L834).

> The isospin span reduces, for the gauge group, to the span of the isospin contractions:
> each family's span reduces to the line through its delta contraction, which is the
> isospin contraction of the two towers.

```lean
lemma reducesInvariantsTo_isoSpan (n m : ℕ) :
    ReducesInvariantsTo (fun g : GaugeGroupI => rep g) (h.isoSpan n m) (h.dotSpan n m)
```

## H. The gauge classification up to mass weight eight

> Section G is now run at each weight in turn, after the torus has put a gauge invariant in
> the weight-zero piece (`GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`). Weight
> two dies outright, its weight-zero piece being trivial: a single Higgs symbol carries
> hypercharge. Weights four and six are joins of isospin spans and nothing else, so what is
> left are the isospin contractions of the towers occurring at that weight: the Higgs mass
> term at weight four, and its once-derived companions at weight six.
>
> Weight eight adds the quartic. `IsSU2QuadFundamental` reduces its span to the two epsilon
> contractions, the first the square of the underived isospin contraction and the second
> zero. The quartic span is joined with the three isospin spans by `ReducesInvariantsTo.sup`,
> which asks stability of the isospin spans only, not of the quartic span.

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_massWeightSubmodule_two`**, a lemma, [line 872](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L872).

> Mass weight two reduces to `⊥` for the gauge group: a single Higgs symbol carries
> hypercharge, so the weight-zero piece is trivial.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_two :
    ReducesInvariantsTo (fun g : GaugeGroupI => rep g) (h.massWeightSubmodule 2) ⊥
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_massWeightSubmodule_four`**, a lemma, [line 881](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L881).

> Mass weight four reduces, for the gauge group, to the underived isospin contraction,
> the Higgs mass term.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_four :
    ReducesInvariantsTo (fun g : GaugeGroupI => rep g) (h.massWeightSubmodule 4)
      (h.dotSpan 0 0)
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_massWeightSubmodule_six`**, a lemma, [line 893](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L893).

> Mass weight six reduces, for the gauge group, to the isospin contractions carrying one
> derivative, on either factor.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_six :
    ReducesInvariantsTo (fun g : GaugeGroupI => rep g) (h.massWeightSubmodule 6)
      (h.dotSpan 1 0 ⊔ h.dotSpan 0 1)
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_massWeightSubmodule_eight`**, a lemma, [line 909](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L909).

> Mass weight eight reduces, for the gauge group, to the isospin contractions carrying two
> derivatives and the square of the underived one, the quartic potential.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_eight :
    ReducesInvariantsTo (fun g : GaugeGroupI => rep g) (h.massWeightSubmodule 8)
      (h.dotSpan 2 0 ⊔ h.dotSpan 0 2 ⊔ h.dotSpan 1 1
        ⊔ ℂ ∙ (h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![]))
```

## I. The gauge-invariant submodules up to mass weight eight

> Taking the stable submodule to be the trivial one turns section H into a statement about
> the mass-weight submodules themselves, and both inclusions are then available: section H
> bounds the invariants from above, and the isospin contractions are themselves gauge
> invariant and of the right mass weight, which bounds them from below.  The two meet, so
> the gauge-invariant part of each mass-weight submodule up to weight eight is exactly
> described.

**`StandardModel.HiggsAlgebraCovRealization.mem_dotSpan_of_invariant_massWeightSubmodule_four`**, a lemma, [line 967](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L967).

> A gauge-invariant term of mass weight four is a multiple of the underived isospin
> contraction.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_four {x : B}
    (hx : x ∈ h.massWeightSubmodule 4) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.dotSpan 0 0
```

**`StandardModel.HiggsAlgebraCovRealization.mem_dotSpan_of_invariant_massWeightSubmodule_six`**, a lemma, [line 976](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L976).

> A gauge-invariant term of mass weight six is a combination of the isospin contractions
> carrying one derivative, on either factor.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_six {x : B}
    (hx : x ∈ h.massWeightSubmodule 6) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.dotSpan 1 0 ⊔ h.dotSpan 0 1
```

**`StandardModel.HiggsAlgebraCovRealization.mem_dotSpan_of_invariant_massWeightSubmodule_eight`**, a lemma, [line 985](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L985).

> A gauge-invariant term of mass weight eight is a combination of the isospin
> contractions carrying two derivatives and of the square of the underived contraction.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_eight {x : B}
    (hx : x ∈ h.massWeightSubmodule 8) (hg : ∀ g : GaugeGroupI, rep g x = x) :
    x ∈ h.dotSpan 2 0 ⊔ h.dotSpan 0 2 ⊔ h.dotSpan 1 1
      ⊔ ℂ ∙ (h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![])
```

**`StandardModel.HiggsAlgebraCovRealization.dotGaugeHiggs_mem_massWeightSubmodule`**, a lemma, [line 994](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L994).

> An isospin contraction has the mass weight of its two towers together.

```lean
lemma dotGaugeHiggs_mem_massWeightSubmodule {n1 n2 : ℕ} (d1 : Fin n1 → (Fin 1 ⊕ Fin 3))
    (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    h.dotGaugeHiggs d1 d2 ∈ h.massWeightSubmodule (2 * (1 + n1) + 2 * (1 + n2))
```

**`StandardModel.HiggsAlgebraCovRealization.gaugeInvariantOfMassDim_four_eq_dotSpan`**, a lemma, [line 1008](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L1008).

> The gauge invariants of mass weight four: the underived isospin contraction.

```lean
lemma gaugeInvariantOfMassDim_four_eq_dotSpan :
    h.gaugeInvariantOfMassDim 4 = h.dotSpan 0 0
```

**`StandardModel.HiggsAlgebraCovRealization.gaugeInvariantOfMassDim_six_eq_dotSpan`**, a lemma, [line 1020](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L1020).

> The gauge invariants of mass weight six: the isospin contractions with one derivative
> on either factor.

```lean
lemma gaugeInvariantOfMassDim_six_eq_dotSpan :
    h.gaugeInvariantOfMassDim 6 = h.dotSpan 1 0 ⊔ h.dotSpan 0 1
```

**`StandardModel.HiggsAlgebraCovRealization.gaugeInvariantOfMassDim_eight_eq_dotSpan`**, a lemma, [line 1034](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean#L1034).

> The gauge invariants of mass weight eight: the isospin contractions with two
> derivatives distributed over the two factors, together with the square of the underived
> contraction — the quartic potential.

```lean
lemma gaugeInvariantOfMassDim_eight_eq_dotSpan :
    h.gaugeInvariantOfMassDim 8 = h.dotSpan 2 0 ⊔ h.dotSpan 0 2 ⊔ h.dotSpan 1 1
      ⊔ ℂ ∙ (h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![])
```

## Depends on

- [Families of colour and isospin components and their invariants](../part-04/gaugegroup-invariants-basic.md)
- [The antisymmetric symbol and complex conjugation in `SU(2)`](../part-04/gaugegroup-su2conjugation.md)
- [The gauge weight decomposition of the Higgs sector](realization-higgscov-derivsubmodule-gaugeweight.md)
- [The mass-weight grading of the Higgs sector, in derivative submodules](realization-higgscov-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/GaugeWeight.lean)
