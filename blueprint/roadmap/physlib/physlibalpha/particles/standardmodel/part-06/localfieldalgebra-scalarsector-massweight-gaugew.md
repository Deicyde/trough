---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightTwo, StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightFour, StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightSix, StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightEight, StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_eq, StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_higgs_zero, StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_higgs_one, StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_barHiggs_zero
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the Higgs mass-weight submodules

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.MassWeight.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean): 57 declarations, 57 with a docstring; 3 private, not shown.

> The gauge invariants of the scalar sector up to mass weight eight, through the torus weights
> and the isospin classifiers.

## i. Overview

> Each mass-weight submodule of the scalar sector up to weight eight has an explicit
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
> Higgs symbol is a family with a fundamental and an anti-fundamental isospin index — the conjugate
> symbol carries the fundamental isospin index and the Higgs symbol the anti-fundamental one, so it
> goes
> second — and the delta contraction, which spans its invariants, is the isospin contraction
> `dotGaugeHiggs`.  The quartic is a family with four fundamental indices once its two Higgs
> symbols are re-indexed by the antisymmetric symbol, and of its two epsilon contractions
> one is the square of the isospin contraction and the other vanishes, pairing commuting
> factors antisymmetrically.
>
> Sections F and G are reductions for the gauge group, stated modulo any gauge-stable
> submodule `S`, which is what lets the other sectors be carried along; taking `S` trivial in
> section H recovers the statements about the mass-weight submodules themselves.

## ii. Key results

> - `massWeightSubmoduleGaugeWeightTwo` up to `massWeightSubmoduleGaugeWeightEight` : the gauge
>   weight decompositions of the mass-weight submodules up to weight eight.
> - `massWeightSubmoduleGaugeWeightEight_piece_zero` : the weight-zero piece at mass weight eight.
> - `isEquivariant_isospinFundAntiFund_isoFamily`, `isEquivariant_isospinQuadFund_quadFamily` : the
>   Higgs symbols as isospin families.
> - `reducesInvariantsTo_massWeightSubmodule_four` up to
>   `reducesInvariantsTo_massWeightSubmodule_eight` : the gauge classification up to mass weight
>   eight, modulo a gauge-stable submodule.
> - `gaugeInvariantOfMassDim_four_eq_dotSpan` up to `gaugeInvariantOfMassDim_eight_eq_dotSpan` :
>   the gauge-invariant submodules up to mass weight eight.

## iv. References

> * None.

## A. The decompositions

> Every term of the Higgs algebra has even mass weight, so the odd mass-weight submodules
> vanish (`massWeightSubmodule_odd_eq_bot`). The even ones are built from the
> derivative submodules by the descriptions of `MassWeight/Basic.lean`. Weight two is a single
> derivative submodule, and the higher weights add the products which distribute the mass
> weight over several towers.

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightTwo`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L107).

> Weight two is the underived Higgs tower.

```lean
noncomputable def massWeightSubmoduleGaugeWeightTwo :
    GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule 2)
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightFour`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L115).

> Weight four is the once-derived tower together with the products of two underived
> ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFour :
    GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule 4)
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightSix`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L126).

> Weight six is the twice-derived tower, the once-derived tower against an underived
> one, and the products of three underived ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSix :
    GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule 6)
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightEight`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L143).

> Weight eight is the thrice-derived tower, the two ways of splitting the derivatives over
> two towers, the once-derived tower against two underived ones, and the products of four
> underived ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightEight :
    GaugeWeightDecomposition repGaugeGroupI (massWeightSubmodule 8)
```

## B. The pieces of a derivative submodule

> A derivative submodule is the join of a Higgs and a conjugate-Higgs submodule, and each of
> those is concentrated in two weights.  The four weights are distinct, so each piece of the
> join is the span of one of the four families of symbols, and every other weight — the zero
> weight in particular — has vanishing piece.

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_eq`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L179).

> The weight-`w` piece of a derivative submodule, as the join of the Higgs and
> conjugate-Higgs pieces.

```lean
lemma derivSubmoduleGaugeWeight_piece_eq (n : ℕ) (w : GaugeWeight) :
    (derivSubmoduleGaugeWeight n).piece w
      = (if w = ((0, 0, -1, -3) : GaugeWeight) then
          ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ higgs d 0
        else if w = ((0, 0, 1, -3) : GaugeWeight) then
          ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ higgs d 1
        else ⊥)
        ⊔ (if w = ((0, 0, 1, 3) : GaugeWeight) then
            ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ barHiggs d 0
          else if w = ((0, 0, -1, 3) : GaugeWeight) then
            ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ barHiggs d 1
          else ⊥)
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_higgs_zero`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L193).

> The piece at the weight of the upper Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_higgs_zero (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece (0, 0, -1, -3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ higgs d 0
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_higgs_one`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L200).

> The piece at the weight of the lower Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_higgs_one (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece (0, 0, 1, -3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ higgs d 1
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_barHiggs_zero`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L207).

> The piece at the weight of the upper conjugate-Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_barHiggs_zero (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece (0, 0, 1, 3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ barHiggs d 0
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_barHiggs_one`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L214).

> The piece at the weight of the lower conjugate-Higgs component.

```lean
lemma derivSubmoduleGaugeWeight_piece_barHiggs_one (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece (0, 0, -1, 3)
      = ⨆ d : Fin n → (Fin 1 ⊕ Fin 3), ℂ ∙ barHiggs d 1
```

**`StandardModel.ScalarSector.derivSubmoduleGaugeWeight_piece_zero`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L222).

> A derivative submodule has no weight-zero content, since every Higgs symbol carries
> hypercharge.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece 0 = ⊥
```

## C. The weight-zero pieces of the products

> Two derivative submodules pair to weight zero exactly by matching a Higgs symbol against a
> conjugate-Higgs symbol of the same isospin component, in either order, so the weight-zero
> piece of such a product is a join of four spans of pairings `∇H^i ∇H̄^i`.  Three of them
> cannot reach weight zero at all, because hypercharge is `± 3` on every generator, so an odd
> number of factors leaves an odd multiple of three.  Four of them reach weight zero on the
> three quartic monomials.

**`StandardModel.ScalarSector.higgsBarHiggsSpan`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L242).

> The span of the isospin-diagonal pairings of a Higgs symbol carrying `n` derivatives
> with a conjugate-Higgs symbol carrying `m` derivatives, at isospin component `i`.

```lean
noncomputable def higgsBarHiggsSpan
    (n m : ℕ) (i : Fin 2) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.quarticSpan`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L249).

> The span of the underived quartic monomial pairing the isospin components `i` and
> `j`.

```lean
noncomputable def quarticSpan
    (i j : Fin 2) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.derivSubmodule_mul_piece_zero`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L255).

> The weight-zero piece of a product of two derivative submodules is spanned by the
> isospin-diagonal pairings, taken in both orders of the two towers.

```lean
lemma derivSubmodule_mul_piece_zero (n m : ℕ) :
    GaugeWeightDecomposition.piece repGaugeGroupI (derivSubmodule n * derivSubmodule m) 0
      = higgsBarHiggsSpan n m 0 ⊔ higgsBarHiggsSpan n m 1
        ⊔ higgsBarHiggsSpan m n 0 ⊔ higgsBarHiggsSpan m n 1
```

**`StandardModel.ScalarSector.derivSubmodule_mul_mul_piece_zero`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L279).

> A product of three derivative submodules has no weight-zero content, since the hypercharge of
> three Higgs generators is an odd multiple of three.

```lean
lemma derivSubmodule_mul_mul_piece_zero (n m k : ℕ) :
    GaugeWeightDecomposition.piece repGaugeGroupI
      (derivSubmodule n * derivSubmodule m * derivSubmodule k) 0 = ⊥
```

**`StandardModel.ScalarSector.derivSubmodule_zero_pow_four_piece_zero`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L291).

> The weight-zero piece of the product of four underived derivative submodules is spanned by the
> three quartic monomials, the ones pairing two Higgs symbols against two conjugate ones with
> matching isospin.

```lean
lemma derivSubmodule_zero_pow_four_piece_zero :
    GaugeWeightDecomposition.piece repGaugeGroupI
      (derivSubmodule 0 * derivSubmodule 0 * derivSubmodule 0
        * derivSubmodule 0) 0
      = quarticSpan 0 0 ⊔ quarticSpan 0 1 ⊔ quarticSpan 1 1
```

## D. The weight-zero pieces of the mass-weight submodules

> Assembling section C along the descriptions of section A gives the weight-zero piece of
> each mass-weight submodule up to weight eight.  The odd weights and weight two are trivial,
> weight four is the underived pairing, weight six adds the pairings with one derivative on
> either factor, and weight eight adds the pairings with two derivatives, those with one
> derivative on each factor, and the three quartic monomials.

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightTwo_piece_zero`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L339).

> The weight-zero piece at mass weight two is trivial, since a single Higgs symbol carries
> hypercharge.

```lean
lemma massWeightSubmoduleGaugeWeightTwo_piece_zero :
    (massWeightSubmoduleGaugeWeightTwo).piece 0 = ⊥
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightFour_piece_zero`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L345).

> The weight-zero piece at mass weight four is spanned by the underived isospin-diagonal
> pairings.

```lean
lemma massWeightSubmoduleGaugeWeightFour_piece_zero :
    (massWeightSubmoduleGaugeWeightFour).piece 0
      = higgsBarHiggsSpan 0 0 0 ⊔ higgsBarHiggsSpan 0 0 1
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightSix_piece_zero`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L356).

> The weight-zero piece at mass weight six is spanned by the isospin-diagonal pairings carrying
> one derivative, on either of the two factors.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero :
    (massWeightSubmoduleGaugeWeightSix).piece 0
      = higgsBarHiggsSpan 1 0 0 ⊔ higgsBarHiggsSpan 1 0 1
        ⊔ higgsBarHiggsSpan 0 1 0 ⊔ higgsBarHiggsSpan 0 1 1
```

**`StandardModel.ScalarSector.massWeightSubmoduleGaugeWeightEight_piece_zero`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L369).

> The weight-zero piece at mass weight eight is spanned by the isospin-diagonal pairings carrying
> two derivatives on one factor or one on each, together with the three quartic monomials.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero :
    (massWeightSubmoduleGaugeWeightEight).piece 0
      = higgsBarHiggsSpan 2 0 0 ⊔ higgsBarHiggsSpan 2 0 1
        ⊔ higgsBarHiggsSpan 0 2 0 ⊔ higgsBarHiggsSpan 0 2 1
        ⊔ (higgsBarHiggsSpan 1 1 0 ⊔ higgsBarHiggsSpan 1 1 1)
        ⊔ (quarticSpan 0 0 ⊔ quarticSpan 0 1 ⊔ quarticSpan 1 1)
```

## E. The Higgs symbols as isospin families

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
> `fun l => barHiggs d' (l 0) * higgs d (l 1)`, conjugate symbol first, which is an
> family with a fundamental and an anti-fundamental isospin index; and its delta contraction, which
> spans its invariants, is the isospin contraction `dotGaugeHiggs`.  That identification is the whole
> point of the section: `dotSpan` is the span of delta contractions, and nothing else
> survives.
>
> The quartic needs four fundamental indices, so its two Higgs symbols must be re-indexed by
> the antisymmetric symbol first.  `tildeHiggs` is that re-index, `H̃⁰ = H¹` and
> `H̃¹ = -H⁰`, and it is fundamental because `SU(2)` is pseudo-real.  The quartic family is
> then a product of four fundamental families, and `IsospinQuadFund` classifies it.  Its
> two epsilon contractions come out as the square of the isospin contraction and zero:
> the second pairs the two conjugate symbols with each other and the two Higgs symbols with
> each other, and an antisymmetric contraction of two commuting factors vanishes.

**`StandardModel.ScalarSector.rep_su2_higgs`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L428).

> An isospin transformation moves the isospin index of a Higgs symbol by the conjugate
> matrix, the index of a Higgs symbol is anti-fundamental.

```lean
lemma rep_su2_higgs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (higgs d i)
      = ∑ a, conj (V.1 a i) • higgs d a
```

**`StandardModel.ScalarSector.rep_su2_barHiggs`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L441).

> An isospin transformation moves the isospin index of a conjugate Higgs symbol by the
> matrix itself, the index of a conjugate Higgs symbol is fundamental.

```lean
lemma rep_su2_barHiggs (V : specialUnitaryGroup (Fin 2) ℂ) {n : ℕ}
    (d : Fin n → (Fin 1 ⊕ Fin 3)) (i : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (barHiggs d i)
      = ∑ a, V.1 a i • barHiggs d a
```

**`StandardModel.ScalarSector.rep_mul_pair`**, a lemma, [line 454](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L454).

> A product of two symbols each moving by given coefficients moves by the product of
> those coefficients.

```lean
lemma rep_mul_pair (g : GaugeGroupI) {ι κ : Type} [Fintype ι] [Fintype κ]
    {X : ι → fieldData.LocalCovFieldAlgebra} {Y : κ → fieldData.LocalCovFieldAlgebra} {x₀ : ι}
    {y₀ : κ} {cX : ι → ℂ} {cY : κ → ℂ}
    (hX : repGaugeGroupI g (X x₀) = ∑ x, cX x • X x)
    (hY : repGaugeGroupI g (Y y₀) = ∑ y, cY y • Y y) :
    repGaugeGroupI g (X x₀ * Y y₀) = ∑ x, ∑ y, (cX x * cY y) • (X x * Y y)
```

**`StandardModel.ScalarSector.higgs_mul_barHiggs_comm`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L464).

> A Higgs symbol commutes with a conjugate Higgs symbol, in the components.

```lean
lemma higgs_mul_barHiggs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    higgs d i * barHiggs d' j = barHiggs d' j * higgs d i
```

**`StandardModel.ScalarSector.higgs_mul_higgs_comm`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L470).

> Two Higgs symbols commute, in the components.

```lean
lemma higgs_mul_higgs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    higgs d i * higgs d' j = higgs d' j * higgs d i
```

**`StandardModel.ScalarSector.barHiggs_mul_barHiggs_comm`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L476).

> Two conjugate Higgs symbols commute, in the components.

```lean
lemma barHiggs_mul_barHiggs_comm {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (i j : Fin 2) :
    barHiggs d i * barHiggs d' j = barHiggs d' j * barHiggs d i
```

**`StandardModel.ScalarSector.isoFamily`**, a def, [line 484](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L484).

> The isospin family of a Higgs tower carrying `n` derivatives against a conjugate tower
> carrying `m`. The conjugate symbol supplies the fundamental index and so goes in the
> first slot, the Higgs symbol the anti-fundamental one.

```lean
noncomputable def isoFamily
    {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) : (Fin 2 → Fin 2) → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.isEquivariant_isospinFundAntiFund_isoFamily`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L490).

> The isospin family carries one fundamental and one anti-fundamental isospin index.

```lean
lemma isEquivariant_isospinFundAntiFund_isoFamily {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((isoFamily d d') ∘ fundAntiFundIdx))
```

**`StandardModel.ScalarSector.deltaContraction_isoFamily`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L501).

> The delta contraction of the isospin family, which spans its isospin invariants, is the
> isospin contraction, the Higgs mass term of the two towers.

```lean
lemma deltaContraction_isoFamily {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) :
    IsospinFundAntiFund.deltaContraction (isoFamily d d') = dotGaugeHiggs d d'
```

**`StandardModel.ScalarSector.dotSpan`**, a def, [line 511](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L511).

> The span of the isospin contractions of a Higgs tower carrying `n` derivatives against
> a conjugate tower carrying `m`, the gauge invariants the isospin classification leaves
> at those two derivative orders.

```lean
noncomputable def dotSpan
    (n m : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.isoFamily_span_stable`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L517).

> The span of the isospin family is stable under the whole gauge group, since each factor of a
> component goes to a combination of the factors of components.

```lean
lemma isoFamily_span_stable {n m : ℕ} (d : Fin n → (Fin 1 ⊕ Fin 3))
    (d' : Fin m → (Fin 1 ⊕ Fin 3)) (g : GaugeGroupI) {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ Submodule.span ℂ (Set.range (isoFamily d d'))) :
    repGaugeGroupI g y ∈ Submodule.span ℂ (Set.range (isoFamily d d'))
```

**`StandardModel.ScalarSector.higgsBarHiggsSpan_le_isoFamily_span`**, a lemma, [line 533](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L533).

> The isospin-diagonal pairing spans of section C sit inside the span of the isospin
> family. A diagonal pairing is one of the four components, the two factors commuting.

```lean
lemma higgsBarHiggsSpan_le_isoFamily_span (n m : ℕ) :
    higgsBarHiggsSpan n m 0 ⊔ higgsBarHiggsSpan n m 1
      ≤ ⨆ (d : Fin n → (Fin 1 ⊕ Fin 3)) (d' : Fin m → (Fin 1 ⊕ Fin 3)),
        Submodule.span ℂ (Set.range (isoFamily d d'))
```

**`StandardModel.ScalarSector.tildeHiggs`**, a def, [line 552](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L552).

> The re-index of an underived Higgs symbol by the antisymmetric symbol, `H̃⁰ = H¹` and
> `H̃¹ = -H⁰`.  `SU(2)` is pseudo-real, so this turns the anti-fundamental index of a Higgs
> symbol into a fundamental one, which is what the quartic family needs.

```lean
noncomputable def tildeHiggs
  (i : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.tildeHiggs_zero`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L557).

> The re-index at isospin zero is the Higgs symbol of isospin one.

```lean
lemma tildeHiggs_zero :
    tildeHiggs 0 = higgs (![] : Fin 0 → (Fin 1 ⊕ Fin 3)) 1
```

**`StandardModel.ScalarSector.tildeHiggs_one`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L562).

> The re-index at isospin one is minus the Higgs symbol of isospin zero.

```lean
lemma tildeHiggs_one :
    tildeHiggs 1 = -higgs (![] : Fin 0 → (Fin 1 ⊕ Fin 3)) 0
```

**`StandardModel.ScalarSector.rep_su2_tildeHiggs`**, a lemma, [line 568](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L568).

> The re-indexed Higgs symbol carries a fundamental isospin index, since the four entry
> identities of `GaugeGroup.SU2Conjugation` remove every complex conjugate.

```lean
lemma rep_su2_tildeHiggs (V : specialUnitaryGroup (Fin 2) ℂ) (i : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (tildeHiggs i)
      = ∑ a, V.1 a i • tildeHiggs a
```

**`StandardModel.ScalarSector.quadFamily`**, a def, [line 586](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L586).

> The quartic isospin family, two conjugate Higgs symbols against two re-indexed Higgs
> symbols, each of the four carrying a fundamental isospin index.

```lean
noncomputable def quadFamily :
    (Fin 4 → Fin 2) → fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.isEquivariant_isospinQuadFund_quadFamily`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L593).

> The quartic family carries four fundamental isospin indices.

```lean
lemma isEquivariant_isospinQuadFund_quadFamily :
    (suTensor 2).IsEquivariant (fun _ : Fin 4 => .fund) (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents quadFamily)
```

**`StandardModel.ScalarSector.epsilonContraction₁₂_quadFamily`**, a lemma, [line 632](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L632).

> The first epsilon contraction of the quartic family is the square of the isospin
> contraction. Pairing the first conjugate symbol with the first Higgs symbol, and the
> second with the second, is pairing each `H̄` with an `H`.

```lean
lemma epsilonContraction₁₂_quadFamily :
    IsospinQuadFund.epsilonContraction₁₂ quadFamily
      = dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![]
```

**`StandardModel.ScalarSector.epsilonContraction₁₃_quadFamily`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L646).

> The second epsilon contraction of the quartic family vanishes. It pairs the two
> conjugate symbols with each other and the two Higgs symbols with each other, and an
> antisymmetric contraction of two commuting factors is zero.

```lean
lemma epsilonContraction₁₃_quadFamily :
    IsospinQuadFund.epsilonContraction₁₃ quadFamily = 0
```

**`StandardModel.ScalarSector.quarticSpan_le_quadFamily_span`**, a lemma, [line 657](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L657).

> The three quartic monomials of section C lie in the span of the components of the
> quartic family, each being one of those components up to a sign.

```lean
lemma quarticSpan_le_quadFamily_span :
    quarticSpan 0 0 ⊔ quarticSpan 0 1 ⊔ quarticSpan 1 1
      ≤ Submodule.span ℂ (Set.range quadFamily)
```

## F. The isospin spans reduce to the isospin contractions

> The classification is wanted not for the mass-weight submodule alone but modulo a
> submodule `S` gathering the other sectors, so every step is a reduction in the sense of
> `ReducesInvariantsTo`: a gauge invariant of `V ⊔ S`, for `S` gauge stable, lies in `W ⊔ S`.
>
> The weight-zero pieces of section D are joins of spans of isospin families.
> `IsospinFundAntiFund.reducesInvariantsTo_span_deltaContraction` reduces each
> span, for the isospin factor and hence for the gauge group, to the line through its delta
> contraction, and `ReducesInvariantsTo.iSup` joins the families. The join asks each span to
> be gauge stable, which is `isoFamily_span_stable` and is why the enlargement is `isoSpan`
> rather than the pairing span of section C: the pairing span keeps only the diagonal
> components and a gauge transformation does not. It asks the target to be gauge stable too,
> and the isospin contractions are gauge invariant.

**`StandardModel.ScalarSector.isoSpan`**, a def, [line 707](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L707).

> The span of the components of all the isospin families of a Higgs tower carrying `n`
> derivatives against a conjugate tower carrying `m`.  This is the gauge-stable
> enlargement of the pairing span of section C.

```lean
noncomputable def isoSpan
    (n m : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.isStableUnder_isoSpan`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L713).

> The isospin span is stable under the gauge group.

```lean
lemma isStableUnder_isoSpan (n m : ℕ) :
    IsStableUnder (fun g : GaugeGroupI => repGaugeGroupI g) (isoSpan n m)
```

**`StandardModel.ScalarSector.isFixedBy_dotSpan`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L719).

> The span of the isospin contractions is fixed pointwise by the gauge group.

```lean
lemma isFixedBy_dotSpan (n m : ℕ) :
    IsFixedBy (fun g : GaugeGroupI => repGaugeGroupI g) (dotSpan n m)
```

**`StandardModel.ScalarSector.higgsBarHiggsSpan_le_isoSpan'`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L725).

> Each isospin-diagonal pairing span of section C sits inside the isospin span.

```lean
lemma higgsBarHiggsSpan_le_isoSpan' (n m : ℕ) (i : Fin 2) :
    higgsBarHiggsSpan n m i ≤ isoSpan n m
```

**`StandardModel.ScalarSector.higgsBarHiggsSpan_le_isoSpan`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L735).

> The pairing span of section C sits inside the isospin span.

```lean
lemma higgsBarHiggsSpan_le_isoSpan (n m : ℕ) :
    higgsBarHiggsSpan n m 0 ⊔ higgsBarHiggsSpan n m 1 ≤ isoSpan n m
```

**`StandardModel.ScalarSector.reducesInvariantsTo_isoSpan`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L742).

> The isospin span reduces, for the gauge group, to the span of the isospin contractions.
> Each family's span reduces to the line through its delta contraction, which is the
> isospin contraction of the two towers.

```lean
lemma reducesInvariantsTo_isoSpan (n m : ℕ) :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (isoSpan n m) (dotSpan n m)
```

## G. The gauge classification up to mass weight eight

> Section F is now run at each weight in turn, after the torus has put a gauge invariant in
> the weight-zero piece (`GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`). Weight
> two dies outright, its weight-zero piece being trivial: a single Higgs symbol carries
> hypercharge. Weights four and six are joins of isospin spans and nothing else, so what is
> left are the isospin contractions of the towers occurring at that weight: the Higgs mass
> term at weight four, and its once-derived companions at weight six.
>
> Weight eight adds the quartic. `IsospinQuadFund` reduces its span to the two epsilon
> contractions, the first the square of the underived isospin contraction and the second
> zero. The quartic span is joined with the three isospin spans by `ReducesInvariantsTo.sup`,
> which asks stability of the isospin spans only, not of the quartic span.

**`StandardModel.ScalarSector.reducesInvariantsTo_massWeightSubmodule_two`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L779).

> Mass weight two reduces to `⊥` for the gauge group, since a single Higgs symbol carries
> hypercharge, so the weight-zero piece is trivial.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_two :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (massWeightSubmodule 2) ⊥
```

**`StandardModel.ScalarSector.reducesInvariantsTo_massWeightSubmodule_four`**, a lemma, [line 787](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L787).

> Mass weight four reduces, for the gauge group, to the underived isospin contraction,
> the Higgs mass term.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_four :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (massWeightSubmodule 4)
      (dotSpan 0 0)
```

**`StandardModel.ScalarSector.reducesInvariantsTo_massWeightSubmodule_six`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L798).

> Mass weight six reduces, for the gauge group, to the isospin contractions carrying one
> derivative, on either factor.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_six :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (massWeightSubmodule 6)
      (dotSpan 1 0 ⊔ dotSpan 0 1)
```

**`StandardModel.ScalarSector.reducesInvariantsTo_massWeightSubmodule_eight`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L813).

> Mass weight eight reduces, for the gauge group, to the isospin contractions carrying two
> derivatives and the square of the underived one, the quartic potential.

```lean
lemma reducesInvariantsTo_massWeightSubmodule_eight :
    ReducesInvariantsTo (fun g : GaugeGroupI => repGaugeGroupI g) (massWeightSubmodule 8)
      (dotSpan 2 0 ⊔ dotSpan 0 2 ⊔ dotSpan 1 1
        ⊔ ℂ ∙ (dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![]))
```

## H. The gauge-invariant submodules up to mass weight eight

> Taking the stable submodule to be the trivial one turns section G into a statement about
> the mass-weight submodules themselves, and both inclusions are then available: section G
> bounds the invariants from above, and the isospin contractions are themselves gauge
> invariant and of the right mass weight, which bounds them from below.  The two meet, so
> the gauge-invariant part of each mass-weight submodule up to weight eight is exactly
> described.

**`StandardModel.ScalarSector.mem_dotSpan_of_invariant_massWeightSubmodule_four`**, a lemma, [line 870](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L870).

> A gauge-invariant term of mass weight four is a multiple of the underived isospin
> contraction.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_four {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule 4) (hg : ∀ g : GaugeGroupI, repGaugeGroupI g x = x) :
    x ∈ dotSpan 0 0
```

**`StandardModel.ScalarSector.mem_dotSpan_of_invariant_massWeightSubmodule_six`**, a lemma, [line 878](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L878).

> A gauge-invariant term of mass weight six is a combination of the isospin contractions
> carrying one derivative, on either factor.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_six {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule 6) (hg : ∀ g : GaugeGroupI, repGaugeGroupI g x = x) :
    x ∈ dotSpan 1 0 ⊔ dotSpan 0 1
```

**`StandardModel.ScalarSector.mem_dotSpan_of_invariant_massWeightSubmodule_eight`**, a lemma, [line 886](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L886).

> A gauge-invariant term of mass weight eight is a combination of the isospin
> contractions carrying two derivatives and of the square of the underived contraction.

```lean
lemma mem_dotSpan_of_invariant_massWeightSubmodule_eight {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule 8) (hg : ∀ g : GaugeGroupI, repGaugeGroupI g x = x) :
    x ∈ dotSpan 2 0 ⊔ dotSpan 0 2 ⊔ dotSpan 1 1
      ⊔ ℂ ∙ (dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![])
```

**`StandardModel.ScalarSector.dotGaugeHiggs_mem_massWeightSubmodule`**, a lemma, [line 894](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L894).

> An isospin contraction has the mass weight of its two towers together.

```lean
lemma dotGaugeHiggs_mem_massWeightSubmodule {n1 n2 : ℕ} (d1 : Fin n1 → (Fin 1 ⊕ Fin 3))
    (d2 : Fin n2 → (Fin 1 ⊕ Fin 3)) :
    dotGaugeHiggs d1 d2 ∈ massWeightSubmodule (2 * (1 + n1) + 2 * (1 + n2))
```

**`StandardModel.ScalarSector.gaugeInvariantOfMassDim_four_eq_dotSpan`**, a lemma, [line 908](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L908).

> The gauge invariants of mass weight four are the underived isospin contraction.

```lean
lemma gaugeInvariantOfMassDim_four_eq_dotSpan :
    gaugeInvariantOfMassDim 4 = dotSpan 0 0
```

**`StandardModel.ScalarSector.gaugeInvariantOfMassDim_six_eq_dotSpan`**, a lemma, [line 920](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L920).

> The gauge invariants of mass weight six are the isospin contractions with one derivative
> on either factor.

```lean
lemma gaugeInvariantOfMassDim_six_eq_dotSpan :
    gaugeInvariantOfMassDim 6 = dotSpan 1 0 ⊔ dotSpan 0 1
```

**`StandardModel.ScalarSector.gaugeInvariantOfMassDim_eight_eq_dotSpan`**, a lemma, [line 934](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean#L934).

> The gauge invariants of mass weight eight are the isospin contractions with two
> derivatives distributed over the two factors, together with the square of the underived
> contraction — the quartic potential.

```lean
lemma gaugeInvariantOfMassDim_eight_eq_dotSpan :
    gaugeInvariantOfMassDim 8 = dotSpan 2 0 ⊔ dotSpan 0 2 ⊔ dotSpan 1 1
      ⊔ ℂ ∙ (dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![])
```

## Depends on

- [Families of colour and isospin components and their invariants](../part-02/gaugegroup-invariants-basic.md)
- [The antisymmetric symbol and complex conjugation in `SU(2)`](../part-02/gaugegroup-su2conjugation.md)
- [The gauge weight decomposition of the scalar sector](../part-05/localfieldalgebra-scalarsector-derivsubmodule-ga.md)
- [The mass-weight grading of the scalar sector, in derivative submodules](../part-05/localfieldalgebra-scalarsector-massweight-basic.md)

## Proof depends on

- [A cube root of unity and the factors of a gauge transformation](../part-02/gaugegroup-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/GaugeWeight.lean)
