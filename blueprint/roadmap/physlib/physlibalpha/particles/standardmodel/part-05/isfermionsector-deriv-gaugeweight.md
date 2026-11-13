---
declaration: module
origin: cited
lean: StandardModel.range_eq_iSup_span, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_d, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_bard, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_u, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_baru, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_Q, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_barQ, StandardModel.IsFermionSector.repGauge_gaugeTorusGen_L
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.Deriv.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean): 34 declarations, 33 with a docstring.

## i. Overview

> The gauge torus acts diagonally on the basis of each fermion value space, with
> weights given by the colour and isospin weights of the fundamental representations
> and the species' hypercharge. Through the dual (and, for the barred species, the
> conjugate-dual) this makes every symbol component a simultaneous eigenvector, and the
> derivative submodules of the fermion sector decompose by gauge weight
> (`derivSubmoduleGaugeWeight`), for every number of covariant derivatives.

## ii. Key results

> - `derivSubmoduleGaugeWeight` : the gauge weight decomposition of the fermion derivative submodules,
>   for any number of covariant derivatives: the join, over families, derivative slots and the ten
>   species, of the spans of the symbol components, each of pure gauge weight

## iv. References

> * None.

## A. The torus weights of the fermion value spaces

## B. The torus action on the value-space bases

## C. Ranges of symbol maps

**`StandardModel.range_eq_iSup_span`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L70).

```lean
lemma range_eq_iSup_span {M : Type} [AddCommGroup M] [Module ℂ M]
    (b : Module.Basis ι ℂ V) (f : Module.Dual ℂ V →ₗ[ℂ] M) :
    LinearMap.range f = ⨆ j, Submodule.span ℂ {f (b.coord j)}
```

## D. The gauge weight decomposition of the derivative submodules

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_d`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L115).

> The gauge torus acts diagonally on the `d` symbol components.

```lean
lemma repGauge_gaugeTorusGen_d (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (d f l ((DownSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(DownSinglet.valueGaugeWeight j)) i) • d f l
        ((DownSinglet.basis).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_bard`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L125).

> The gauge torus acts diagonally on the `bard` symbol components.

```lean
lemma repGauge_gaugeTorusGen_bard (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (bard f l (((Basis.conj DownSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) • bard f l
        (((Basis.conj DownSinglet.basis)).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_u`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L134).

> The gauge torus acts diagonally on the `u` symbol components.

```lean
lemma repGauge_gaugeTorusGen_u (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (u f l ((UpSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(UpSinglet.valueGaugeWeight j)) i) • u f l
        ((UpSinglet.basis).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_baru`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L144).

> The gauge torus acts diagonally on the `baru` symbol components.

```lean
lemma repGauge_gaugeTorusGen_baru (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (baru f l (((Basis.conj UpSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) • baru f l
        (((Basis.conj UpSinglet.basis)).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_Q`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L153).

> The gauge torus acts diagonally on the `Q` symbol components.

```lean
lemma repGauge_gaugeTorusGen_Q (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen i) (Q f l ((QuarkDoublet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(QuarkDoublet.valueGaugeWeight j)) i) • Q f l
        ((QuarkDoublet.basis).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_barQ`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L163).

> The gauge torus acts diagonally on the `barQ` symbol components.

```lean
lemma repGauge_gaugeTorusGen_barQ (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen i) (barQ f l (((Basis.conj QuarkDoublet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) • barQ f l
        (((Basis.conj QuarkDoublet.basis)).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_L`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L172).

> The gauge torus acts diagonally on the `L` symbol components.

```lean
lemma repGauge_gaugeTorusGen_L (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen i) (L f l ((LeptonDoubletV.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonDoubletV.valueGaugeWeight j)) i) • L f l
        ((LeptonDoubletV.basis).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_barL`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L182).

> The gauge torus acts diagonally on the `barL` symbol components.

```lean
lemma repGauge_gaugeTorusGen_barL (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen i) (barL f l (((Basis.conj LeptonDoubletV.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) • barL f l
        (((Basis.conj LeptonDoubletV.basis)).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_e`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L191).

> The gauge torus acts diagonally on the `e` symbol components.

```lean
lemma repGauge_gaugeTorusGen_e (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen i) (e f l ((LeptonSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonSinglet.valueGaugeWeight j)) i) • e f l
        ((LeptonSinglet.basis).coord j)
```

**`StandardModel.IsFermionSector.repGauge_gaugeTorusGen_bare`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L201).

> The gauge torus acts diagonally on the `bare` symbol components.

```lean
lemma repGauge_gaugeTorusGen_bare (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen i) (bare f l (((Basis.conj LeptonSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) • bare f l
        (((Basis.conj LeptonSinglet.basis)).coord j)
```

**`StandardModel.IsFermionSector.rangeGaugeWeightD`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L210).

> The gauge weight decomposition of the range of the `d` symbols.

```lean
noncomputable def rangeGaugeWeightD (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (d f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarD`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L221).

> The gauge weight decomposition of the range of the `bard` symbols.

```lean
noncomputable def rangeGaugeWeightBarD (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (bard f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightU`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L232).

> The gauge weight decomposition of the range of the `u` symbols.

```lean
noncomputable def rangeGaugeWeightU (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (u f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarU`**, a def, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L243).

> The gauge weight decomposition of the range of the `baru` symbols.

```lean
noncomputable def rangeGaugeWeightBarU (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (baru f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightQ`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L254).

> The gauge weight decomposition of the range of the `Q` symbols.

```lean
noncomputable def rangeGaugeWeightQ (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (Q f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarQ`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L265).

> The gauge weight decomposition of the range of the `barQ` symbols.

```lean
noncomputable def rangeGaugeWeightBarQ (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (barQ f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightL`**, a def, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L276).

> The gauge weight decomposition of the range of the `L` symbols.

```lean
noncomputable def rangeGaugeWeightL (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (L f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarL`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L287).

> The gauge weight decomposition of the range of the `barL` symbols.

```lean
noncomputable def rangeGaugeWeightBarL (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (barL f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightE`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L298).

> The gauge weight decomposition of the range of the `e` symbols.

```lean
noncomputable def rangeGaugeWeightE (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (e f l))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarE`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L309).

> The gauge weight decomposition of the range of the `bare` symbols.

```lean
noncomputable def rangeGaugeWeightBarE (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (bare f l))
```

**`StandardModel.IsFermionSector.derivSubmoduleGaugeWeight`**, an instance, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L328).

> **The gauge weight decomposition of the fermion derivative submodules**, for any
> number of covariant derivatives: the join, over families, derivative slots and the
> ten species, of the spans of the symbol components, each of pure gauge weight.
>
> This is an instance: its statement mentions `h`, so unification against the goal
> recovers the sector and with it all the implicit data of `IsFermionSector`.  The
> `rangeGaugeWeight*` decompositions above cannot be instances for exactly that
> reason — their statements name only the symbol maps, leaving the rest of the
> structure's parameters undetermined.

```lean
noncomputable instance derivSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGauge (h.derivSubmodule n)
```

## E. The support of the decomposition

**`StandardModel.IsFermionSector.fermionGaugeWeights`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L364).

> The gauge weights carried by the fermion symbols: for each species the image of
> its value weights, negated for the unbarred species (the symbols pair with the dual
> of the value space) and taken as they are for the barred ones.

```lean
def fermionGaugeWeights : Finset GaugeWeight
```

**`StandardModel.IsFermionSector.rangeGaugeWeightD_supp`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L377).

> The support of the `d` range decomposition.

```lean
lemma rangeGaugeWeightD_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightD f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => -(DownSinglet.valueGaugeWeight j))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarD_supp`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L382).

> The support of the `bard` range decomposition.

```lean
lemma rangeGaugeWeightBarD_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightBarD f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => DownSinglet.valueGaugeWeight j)
```

**`StandardModel.IsFermionSector.rangeGaugeWeightU_supp`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L387).

> The support of the `u` range decomposition.

```lean
lemma rangeGaugeWeightU_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightU f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => -(UpSinglet.valueGaugeWeight j))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarU_supp`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L392).

> The support of the `baru` range decomposition.

```lean
lemma rangeGaugeWeightBarU_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightBarU f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => UpSinglet.valueGaugeWeight j)
```

**`StandardModel.IsFermionSector.rangeGaugeWeightQ_supp`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L397).

> The support of the `Q` range decomposition.

```lean
lemma rangeGaugeWeightQ_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightQ f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 × Fin 2 => -(QuarkDoublet.valueGaugeWeight j))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarQ_supp`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L402).

> The support of the `barQ` range decomposition.

```lean
lemma rangeGaugeWeightBarQ_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightBarQ f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 × Fin 2 => QuarkDoublet.valueGaugeWeight j)
```

**`StandardModel.IsFermionSector.rangeGaugeWeightL_supp`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L407).

> The support of the `L` range decomposition.

```lean
lemma rangeGaugeWeightL_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightL f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 2 => -(LeptonDoubletV.valueGaugeWeight j))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarL_supp`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L412).

> The support of the `barL` range decomposition.

```lean
lemma rangeGaugeWeightBarL_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightBarL f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 2 => LeptonDoubletV.valueGaugeWeight j)
```

**`StandardModel.IsFermionSector.rangeGaugeWeightE_supp`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L417).

> The support of the `e` range decomposition.

```lean
lemma rangeGaugeWeightE_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightE f l).supp
      = Finset.univ.image (fun j : Fin 2 => -(LeptonSinglet.valueGaugeWeight j))
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarE_supp`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L422).

> The support of the `bare` range decomposition.

```lean
lemma rangeGaugeWeightBarE_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeightBarE f l).supp
      = Finset.univ.image (fun j : Fin 2 => LeptonSinglet.valueGaugeWeight j)
```

**`StandardModel.IsFermionSector.derivSubmoduleGaugeWeight_supp`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean#L430).

> **The support of the gauge weight decomposition of the fermion derivative
> submodules**: the gauge weights of the ten species, independent of the number of
> covariant derivatives.

```lean
lemma derivSubmoduleGaugeWeight_supp (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).supp = fermionGaugeWeights
```

## Depends on

- [Down-type singlets](../part-03/fermions-downsinglet-basic.md)
- [Charged-lepton singlets](../part-03/fermions-leptonsinglet-basic.md)
- [The type corresponding to quark doublets](../part-03/fermions-quarkdoublet-basic.md)
- [Up-type singlets](../part-03/fermions-upsinglet-basic.md)
- [The fermion sector](isfermionsector-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/Deriv/GaugeWeight.lean)
