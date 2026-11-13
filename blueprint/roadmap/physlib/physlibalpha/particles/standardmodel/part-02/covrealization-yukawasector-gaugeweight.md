---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.sectorMassWeightEightGaugeWeight, StandardModel.CovAlgebraRealization.piece_mul_sup_mul, StandardModel.CovAlgebraRealization.piece_mul_mul_sup, StandardModel.CovAlgebraRealization.mul_supp_hypercharge, StandardModel.CovAlgebraRealization.higgsSubmoduleGaugeWeight_hc, StandardModel.CovAlgebraRealization.barHiggsSubmoduleGaugeWeight_hc, StandardModel.CovAlgebraRealization.mul_speciesGaugeWeight_mul_piece_zero_neg_three, StandardModel.CovAlgebraRealization.mul_speciesGaugeWeight_mul_piece_zero_pos_three
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the Yukawa sector at mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.YukawaSector.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean): 10 declarations, 10 with a docstring.

## i. Overview

> Mass weight eight is where the Yukawa sector first has anything to say: by
> `sectorMassWeight_higgs_fermion_eight` the whole sector at that weight is one Higgs
> tower against two underived fermion towers, the weight of `H ψ ψ` itself.  Transporting
> the gauge weight decompositions of the two sectors along that identification decomposes
> the sector, and the question of which Yukawa couplings can exist becomes the question of
> which pieces survive at gauge weight zero.
>
> Almost none of them do, and the reason is hypercharge alone.  Writing `6Y` for the
> normalisation used throughout, a symbol carries the contragredient of its value space and
> so the negative of its charge: the Higgs symbols carry `-3` and their conjugates `+3`,
> while the ten fermion species carry
>
> `d = 2`, `bard = -2`, `u = -4`, `baru = 4`, `Q = -1`, `barQ = 1`, `L = 3`, `barL = -3`,
> `e = 6`, `bare = -6`.
>
> A block of the decomposition is a choice of one Higgs symbol and two fermion species, and
> it can reach gauge weight zero only if the three charges sum to zero.  Against the Higgs
> that asks the fermion pair to sum to `+3`, which happens only for `{d, barQ}`,
> `{baru, Q}` and `{barL, e}`; against the conjugate Higgs it asks for `-3`, which happens
> only for `{bard, Q}`, `{u, barQ}` and `{L, bare}`.  No species pairs with itself, since
> `2f = ±3` has no solution.  Each of the six pairs occurs in both orders inside the product
> of the two fermion towers, so of the `2 * 10 * 10 = 200` blocks exactly twelve survive and
> one hundred and eighty-eight are `⊥`.
>
> That is the whole content of this file: the surviving twelve are the Yukawa couplings
> `H d barQ`, `H baru Q`, `H barL e`, `barH bard Q`, `barH u barQ`, `barH L bare` and their
> transposes.  The colour and isospin structure eliminates nothing further here — it only
> decides which components inside a surviving block pair up, which is a later question.

## ii. Key results

> - `sectorMassWeightEightGaugeWeight` : the gauge weight decomposition of the Yukawa sector at mass
>   weight eight, transported along `sectorMassWeight_higgs_fermion_eight` from the product of the
>   Higgs derivative submodule with two copies of the underived fermion towers
> - `piece_mul_sup_mul` : if the first fermion factor of a triple product is a join `VA ⊔ VB`, its
>   weight-`w` piece splits along the join
> - `piece_mul_mul_sup` : if the second fermion factor of a triple product is a join `VA ⊔ VB`, its
>   weight-`w` piece splits along the join
> - `mul_supp_hypercharge` : two decompositions with constant hypercharge have a product of constant
>   hypercharge, the sum of the two: the support of a product is the pointwise sum of the supports,
>   and hypercharge is the fourth coordinate of a gauge weight

## iv. References

> * None.

## A. The sector at mass weight eight, decomposed

**`StandardModel.CovAlgebraRealization.sectorMassWeightEightGaugeWeight`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L98).

> The gauge weight decomposition of the Yukawa sector at mass weight eight, transported
> along `sectorMassWeight_higgs_fermion_eight` from the product of the Higgs derivative
> submodule with two copies of the underived fermion towers.

```lean
noncomputable def sectorMassWeightEightGaugeWeight :
    GaugeWeightDecomposition repGauge
      (h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8)
```

## B. Splitting a Higgs-fermion-fermion product along its joins

> The two fermion factors are each a join over ten species, so the product has to be
> distributed over both before any species-level statement can be made.  The left factor is
> handled by `IsFermionSector.piece_sup_mul`; the two lemmas here reach the inner factors of
> a triple product, which that lemma cannot see.

**`StandardModel.CovAlgebraRealization.piece_mul_sup_mul`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L121).

> If the first fermion factor of a triple product is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_mul_sup_mul {VX VA VB VZ : Submodule ℂ B}
    (dX : GaugeWeightDecomposition repGauge VX) (dA : GaugeWeightDecomposition repGauge VA)
    (dB : GaugeWeightDecomposition repGauge VB) (dZ : GaugeWeightDecomposition repGauge VZ)
    (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dX)
        (d' := GaugeWeightDecomposition.mul
          (d := GaugeWeightDecomposition.sup (d := dA) (d' := dB)) (d' := dZ))).piece w
      = (GaugeWeightDecomposition.mul (d := dX)
            (d' := GaugeWeightDecomposition.mul (d := dA) (d' := dZ))).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dX)
            (d' := GaugeWeightDecomposition.mul (d := dB) (d' := dZ))).piece w
```

**`StandardModel.CovAlgebraRealization.piece_mul_mul_sup`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L145).

> If the second fermion factor of a triple product is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_mul_mul_sup {VX VY VA VB : Submodule ℂ B}
    (dX : GaugeWeightDecomposition repGauge VX) (dY : GaugeWeightDecomposition repGauge VY)
    (dA : GaugeWeightDecomposition repGauge VA) (dB : GaugeWeightDecomposition repGauge VB)
    (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dX)
        (d' := GaugeWeightDecomposition.mul (d := dY)
          (d' := GaugeWeightDecomposition.sup (d := dA) (d' := dB)))).piece w
      = (GaugeWeightDecomposition.mul (d := dX)
            (d' := GaugeWeightDecomposition.mul (d := dY) (d' := dA))).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dX)
            (d' := GaugeWeightDecomposition.mul (d := dY) (d' := dB))).piece w
```

## C. Hypercharge adds across a product

> `IsFermionSector.mul_piece_zero_eq_bot_of_hypercharge` kills a product of two
> decompositions whose constant hypercharges do not cancel.  To use it on a triple product
> the two fermion factors have to be read as a single decomposition, and the only thing
> needed about them is that their hypercharges add.

**`StandardModel.CovAlgebraRealization.mul_supp_hypercharge`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L181).

> Two decompositions with constant hypercharge have a product of constant hypercharge,
> the sum of the two: the support of a product is the pointwise sum of the supports, and
> hypercharge is the fourth coordinate of a gauge weight.

```lean
lemma mul_supp_hypercharge {V V' : Submodule ℂ B}
    {dV : GaugeWeightDecomposition repGauge V} {dV' : GaugeWeightDecomposition repGauge V'}
    {hc hc' : ℤ} (hV : ∀ w ∈ dV.supp, w.2.2.2 = hc) (hV' : ∀ w ∈ dV'.supp, w.2.2.2 = hc') :
    ∀ w ∈ (GaugeWeightDecomposition.mul (d := dV) (d' := dV')).supp, w.2.2.2 = hc + hc'
```

## D. The two Higgs hypercharges

**`StandardModel.CovAlgebraRealization.higgsSubmoduleGaugeWeight_hc`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L199).

> The Higgs symbols carry hypercharge `-3`, independent of isospin and of the number of
> derivatives: the two weights in the support are `(0, 0, ∓1, -3)`.

```lean
lemma higgsSubmoduleGaugeWeight_hc (n : ℕ) :
    ∀ w ∈ (h.isHiggsSector.higgsSubmoduleGaugeWeight n).supp, w.2.2.2 = -3
```

**`StandardModel.CovAlgebraRealization.barHiggsSubmoduleGaugeWeight_hc`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L207).

> The conjugate-Higgs symbols carry hypercharge `3`, independent of isospin and of the
> number of derivatives: the two weights in the support are `(0, 0, ±1, 3)`.

```lean
lemma barHiggsSubmoduleGaugeWeight_hc (n : ℕ) :
    ∀ w ∈ (h.isHiggsSector.barHiggsSubmoduleGaugeWeight n).supp, w.2.2.2 = 3
```

## E. The hypercharge sieve on two fermions against one Higgs

> Everything the Standard Model gauge group has to say about which Yukawa couplings exist is
> already said by hypercharge.  A block of the mass-weight-eight decomposition is a Higgs
> symbol against a pair of fermion species, and the three hypercharges have to cancel.  Since
> the Higgs contributes `∓3`, the fermion pair must contribute `±3`, and the ten species
> charges `2, -2, -4, 4, -1, 1, 3, -3, 6, -6` admit only three unordered pairs of each sign.
>
> The two lemmas below are stated for an arbitrary decomposition `dV` of constant hypercharge
> rather than for the Higgs submodules themselves, since that is all the argument uses; the
> Higgs and conjugate-Higgs cases are then two applications.  No species pairs with itself:
> `2f = ±3` has no integer solution.

**`StandardModel.CovAlgebraRealization.mul_speciesGaugeWeight_mul_piece_zero_neg_three`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L236).

> The hypercharge sieve against a Higgs symbol. If `dV` has constant hypercharge `-3`,
> as the Higgs symbols do, then of the hundred species pairings in a product of two fermion
> towers only the six whose hypercharges sum to `+3` survive at gauge weight zero: `d barQ`,
> `baru Q` and `barL e`, each in both orders. The other ninety-four pairings leave a nonzero
> hypercharge behind and so contribute nothing.

```lean
lemma mul_speciesGaugeWeight_mul_piece_zero_neg_three {V : Submodule ℂ B}
    {dV : GaugeWeightDecomposition repGauge V} (hV : ∀ w ∈ dV.supp, w.2.2.2 = -3)
    {n m : ℕ} (f f' : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3)
    (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := dV)
        (d' := GaugeWeightDecomposition.mul
          (d := h.isFermionSector.speciesGaugeWeight f l)
          (d' := h.isFermionSector.speciesGaugeWeight f' l'))).piece 0
      = (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightD f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarQ f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarQ f l)
              (d' := h.isFermionSector.rangeGaugeWeightD f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarU f l)
              (d' := h.isFermionSector.rangeGaugeWeightQ f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightQ f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarU f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarL f l)
              (d' := h.isFermionSector.rangeGaugeWeightE f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightE f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarL f' l'))).piece 0
```

**`StandardModel.CovAlgebraRealization.mul_speciesGaugeWeight_mul_piece_zero_pos_three`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L391).

> The hypercharge sieve against a conjugate-Higgs symbol. If `dV` has constant
> hypercharge `3`, as the conjugate-Higgs symbols do, then of the hundred species pairings
> only the six whose hypercharges sum to `-3` survive at gauge weight zero: `bard Q`,
> `u barQ` and `L bare`, each in both orders.

```lean
lemma mul_speciesGaugeWeight_mul_piece_zero_pos_three {V : Submodule ℂ B}
    {dV : GaugeWeightDecomposition repGauge V} (hV : ∀ w ∈ dV.supp, w.2.2.2 = 3)
    {n m : ℕ} (f f' : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3)
    (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := dV)
        (d' := GaugeWeightDecomposition.mul
          (d := h.isFermionSector.speciesGaugeWeight f l)
          (d' := h.isFermionSector.speciesGaugeWeight f' l'))).piece 0
      = (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarD f l)
              (d' := h.isFermionSector.rangeGaugeWeightQ f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightQ f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarD f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightU f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarQ f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarQ f l)
              (d' := h.isFermionSector.rangeGaugeWeightU f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightL f l)
              (d' := h.isFermionSector.rangeGaugeWeightBarE f' l'))).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := dV)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarE f l)
              (d' := h.isFermionSector.rangeGaugeWeightL f' l'))).piece 0
```

## F. The twelve surviving blocks

> The pieces now assemble.  Unfolding the Higgs derivative submodule into its Higgs and
> conjugate-Higgs halves and the fermion towers into a join over families splits the product
> into blocks indexed by a Higgs choice and two families, and the sieve of section E reduces
> each block to six terms.  Twelve survive in all, and they are exactly the Yukawa couplings
> of the Standard Model: the down-type coupling `H d barQ`, the up-type coupling `H baru Q`,
> the charged-lepton coupling `H barL e`, their conjugates `barH bard Q`, `barH u barQ` and
> `barH L bare`, and the transpose of each, the two fermion towers being interchangeable.
>
> Nothing here constrains the families: all nine pairs `(f, f')` occur, which is where the
> Yukawa matrices come from.

**`StandardModel.CovAlgebraRealization.sectorMassWeightEightGaugeWeight_piece_zero`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L564).

> The weight-zero piece of the Yukawa sector at mass weight eight: the join, over pairs
> of families, of the twelve blocks that hypercharge allows.  Of the two hundred ways of
> choosing one Higgs symbol and two fermion species, only these twelve have vanishing total
> hypercharge; the remaining one hundred and eighty-eight are killed by
> `mul_speciesGaugeWeight_mul_piece_zero_neg_three` and
> `mul_speciesGaugeWeight_mul_piece_zero_pos_three`.

```lean
lemma sectorMassWeightEightGaugeWeight_piece_zero :
    h.sectorMassWeightEightGaugeWeight.piece 0
      = ⨆ (f : Fin 3) (f' : Fin 3),
        (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightD f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarQ f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarQ f ![])
              (d' := h.isFermionSector.rangeGaugeWeightD f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarU f ![])
              (d' := h.isFermionSector.rangeGaugeWeightQ f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightQ f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarU f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarL f ![])
              (d' := h.isFermionSector.rangeGaugeWeightE f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.higgsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightE f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarL f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarD f ![])
              (d' := h.isFermionSector.rangeGaugeWeightQ f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightQ f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarD f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightU f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarQ f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarQ f ![])
              (d' := h.isFermionSector.rangeGaugeWeightU f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightL f ![])
              (d' := h.isFermionSector.rangeGaugeWeightBarE f' ![]))).piece 0
        ⊔ (GaugeWeightDecomposition.mul
            (d := h.isHiggsSector.barHiggsSubmoduleGaugeWeight 0)
            (d' := GaugeWeightDecomposition.mul
              (d := h.isFermionSector.rangeGaugeWeightBarE f ![])
              (d' := h.isFermionSector.rangeGaugeWeightL f' ![]))).piece 0
```

## G. Invariants modulo a gauge-stable submodule

> A gauge-invariant element sits in the weight-zero piece, and the same holds modulo a
> submodule `S` stable under the torus: an invariant lying in the sector joined with `S`
> lies in the weight-zero piece joined with `S`.  This is what turns the twelve blocks of
> section F into a statement about the invariants themselves, the remaining work being to
> peel the blocks apart, which is not done here.
>
> The statement is `GaugeWeightDecomposition.mem_piece_zero_sup_of_invariant`, which chooses
> the separating torus generator weight by weight.  That matters here: at
> mass weight eight the sector carries weights of vanishing hypercharge and nonzero colour or
> isospin — `H d bard` is one — so, unlike the fermion sector, no single generator sees every
> weight.

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeightEight_piece_zero_sup_of_invariant`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean#L703).

> A gauge-invariant element of the Yukawa sector at mass weight eight joined with a
> torus-stable `S` lies in the weight-zero piece joined with `S`, so the twelve blocks of
> `sectorMassWeightEightGaugeWeight_piece_zero` are all that a Yukawa invariant can be
> built from.

```lean
lemma mem_sectorMassWeightEight_piece_zero_sup_of_invariant {S : Submodule ℂ B}
    (hS : ∀ (i : Fin 4) (y : B), y ∈ S → repGauge (gaugeTorusGen i) y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) :
    x ∈ h.sectorMassWeightEightGaugeWeight.piece 0 ⊔ S
```

## Depends on

- [The Yukawa sector's mass-weight submodules](covrealization-yukawasector-basic.md)
- [The gauge weight decomposition of the fermion mass-weight submodules](../part-05/isfermionsector-massweight-gaugeweight.md)
- [The gauge weight decomposition of the Higgs sector](../part-10/realization-higgscov-derivsubmodule-gaugeweight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/GaugeWeight.lean)
