---
declaration: module
origin: cited
lean: StandardModel.FermionSector.repGauge_gaugeTorusGen_d, StandardModel.FermionSector.repGauge_gaugeTorusGen_bard, StandardModel.FermionSector.repGauge_gaugeTorusGen_u, StandardModel.FermionSector.repGauge_gaugeTorusGen_baru, StandardModel.FermionSector.repGauge_gaugeTorusGen_Q, StandardModel.FermionSector.repGauge_gaugeTorusGen_barQ, StandardModel.FermionSector.repGauge_gaugeTorusGen_L, StandardModel.FermionSector.repGauge_gaugeTorusGen_barL
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.Deriv.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean): 33 declarations, 33 with a docstring.

> The fermion derivative submodules decompose by gauge weight, with the weights of the ten species.

## i. Overview

> The gauge torus acts diagonally on the basis of each fermion value space, with
> weights given by the colour and isospin weights of the fundamental representations
> and the species' hypercharge. Through the dual (and, for the barred species, the
> conjugate-dual) this makes every symbol component a simultaneous eigenvector, and the
> derivative submodules of the fermion sector decompose by gauge weight
> (`derivSubmoduleGaugeWeight`), for every number of covariant derivatives.

## ii. Key results

> - `derivSubmoduleGaugeWeight` : the gauge weight decomposition of the fermion derivative submodules,
>   for any number of covariant derivatives.
> - `derivSubmoduleGaugeWeight_supp` : its support, the gauge weights of the ten species.

## iv. References

> * None.

## A. The gauge weight decomposition of the derivative submodules

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_d`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L55).

> The gauge torus acts diagonally on the `d` symbol components.

```lean
lemma repGauge_gaugeTorusGen_d (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (d f l ((DownSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(DownSinglet.valueGaugeWeight j)) i) • d f l
        ((DownSinglet.basis).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_bard`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L64).

> The gauge torus acts diagonally on the `bard` symbol components.

```lean
lemma repGauge_gaugeTorusGen_bard (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (bard f l (((Basis.conj DownSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (DownSinglet.valueGaugeWeight j) i) • bard f l
        (((Basis.conj DownSinglet.basis)).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_u`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L72).

> The gauge torus acts diagonally on the `u` symbol components.

```lean
lemma repGauge_gaugeTorusGen_u (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (u f l ((UpSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(UpSinglet.valueGaugeWeight j)) i) • u f l
        ((UpSinglet.basis).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_baru`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L81).

> The gauge torus acts diagonally on the `baru` symbol components.

```lean
lemma repGauge_gaugeTorusGen_baru (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge (gaugeTorusGen i) (baru f l (((Basis.conj UpSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (UpSinglet.valueGaugeWeight j) i) • baru f l
        (((Basis.conj UpSinglet.basis)).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_Q`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L89).

> The gauge torus acts diagonally on the `Q` symbol components.

```lean
lemma repGauge_gaugeTorusGen_Q (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen i) (Q f l ((QuarkDoublet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(QuarkDoublet.valueGaugeWeight j)) i) • Q f l
        ((QuarkDoublet.basis).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_barQ`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L98).

> The gauge torus acts diagonally on the `barQ` symbol components.

```lean
lemma repGauge_gaugeTorusGen_barQ (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3 × Fin 2) :
    repGauge (gaugeTorusGen i) (barQ f l (((Basis.conj QuarkDoublet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (QuarkDoublet.valueGaugeWeight j) i) • barQ f l
        (((Basis.conj QuarkDoublet.basis)).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_L`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L106).

> The gauge torus acts diagonally on the `L` symbol components.

```lean
lemma repGauge_gaugeTorusGen_L (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen i) (L f l ((LeptonDoubletV.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonDoubletV.valueGaugeWeight j)) i) • L f l
        ((LeptonDoubletV.basis).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_barL`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L115).

> The gauge torus acts diagonally on the `barL` symbol components.

```lean
lemma repGauge_gaugeTorusGen_barL (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge (gaugeTorusGen i) (barL f l (((Basis.conj LeptonDoubletV.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonDoubletV.valueGaugeWeight j) i) • barL f l
        (((Basis.conj LeptonDoubletV.basis)).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_e`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L123).

> The gauge torus acts diagonally on the `e` symbol components.

```lean
lemma repGauge_gaugeTorusGen_e (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen i) (e f l ((LeptonSinglet.basis).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (-(LeptonSinglet.valueGaugeWeight j)) i) • e f l
        ((LeptonSinglet.basis).coord j)
```

**`StandardModel.FermionSector.repGauge_gaugeTorusGen_bare`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L132).

> The gauge torus acts diagonally on the `bare` symbol components.

```lean
lemma repGauge_gaugeTorusGen_bare (i : Fin 4) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2) :
    repGauge (gaugeTorusGen i) (bare f l (((Basis.conj LeptonSinglet.basis)).coord j))
      = ((expI : ℂ) ^ GaugeWeight.coord (LeptonSinglet.valueGaugeWeight j) i) • bare f l
        (((Basis.conj LeptonSinglet.basis)).coord j)
```

**`StandardModel.FermionSector.rangeGaugeWeightD`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L141).

> The gauge weight decomposition of the range of the `d` symbols.

```lean
noncomputable def rangeGaugeWeightD (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (d f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarD`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L152).

> The gauge weight decomposition of the range of the `bard` symbols.

```lean
noncomputable def rangeGaugeWeightBarD (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (bard f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightU`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L163).

> The gauge weight decomposition of the range of the `u` symbols.

```lean
noncomputable def rangeGaugeWeightU (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (u f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarU`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L174).

> The gauge weight decomposition of the range of the `baru` symbols.

```lean
noncomputable def rangeGaugeWeightBarU (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (baru f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightQ`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L185).

> The gauge weight decomposition of the range of the `Q` symbols.

```lean
noncomputable def rangeGaugeWeightQ (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (Q f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarQ`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L196).

> The gauge weight decomposition of the range of the `barQ` symbols.

```lean
noncomputable def rangeGaugeWeightBarQ (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (barQ f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightL`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L207).

> The gauge weight decomposition of the range of the `L` symbols.

```lean
noncomputable def rangeGaugeWeightL (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (L f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarL`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L218).

> The gauge weight decomposition of the range of the `barL` symbols.

```lean
noncomputable def rangeGaugeWeightBarL (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (barL f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightE`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L229).

> The gauge weight decomposition of the range of the `e` symbols.

```lean
noncomputable def rangeGaugeWeightE (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (e f l))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarE`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L240).

> The gauge weight decomposition of the range of the `bare` symbols.

```lean
noncomputable def rangeGaugeWeightBarE (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge (LinearMap.range (bare f l))
```

**`StandardModel.FermionSector.derivSubmoduleGaugeWeight`**, an instance, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L257).

> The gauge weight decomposition of the fermion derivative submodules, for any
> number of covariant derivatives. It is the join, over families, derivative slots and the
> ten species, of the spans of the symbol components, each of pure gauge weight.
>
> This is an instance, so the weight decomposition of `derivSubmodule n` is found by
> instance search. The `rangeGaugeWeight*` decompositions above name only a single symbol
> map each, so they are left as plain definitions.

```lean
noncomputable instance derivSubmoduleGaugeWeight (n : ℕ) :
    GaugeWeightDecomposition repGauge (derivSubmodule n)
```

## B. The support of the decomposition

**`StandardModel.FermionSector.fermionGaugeWeights`**, a def, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L293).

> The gauge weights carried by the fermion symbols, for each species the image of
> its value weights, negated for the unbarred species (the symbols pair with the dual
> of the value space) and taken as they are for the barred ones.

```lean
def fermionGaugeWeights : Finset GaugeWeight
```

**`StandardModel.FermionSector.rangeGaugeWeightD_supp`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L306).

> The support of the `d` range decomposition.

```lean
lemma rangeGaugeWeightD_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightD f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => -(DownSinglet.valueGaugeWeight j))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarD_supp`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L311).

> The support of the `bard` range decomposition.

```lean
lemma rangeGaugeWeightBarD_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightBarD f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => DownSinglet.valueGaugeWeight j)
```

**`StandardModel.FermionSector.rangeGaugeWeightU_supp`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L316).

> The support of the `u` range decomposition.

```lean
lemma rangeGaugeWeightU_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightU f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => -(UpSinglet.valueGaugeWeight j))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarU_supp`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L321).

> The support of the `baru` range decomposition.

```lean
lemma rangeGaugeWeightBarU_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightBarU f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 => UpSinglet.valueGaugeWeight j)
```

**`StandardModel.FermionSector.rangeGaugeWeightQ_supp`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L326).

> The support of the `Q` range decomposition.

```lean
lemma rangeGaugeWeightQ_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightQ f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 × Fin 2 => -(QuarkDoublet.valueGaugeWeight j))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarQ_supp`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L331).

> The support of the `barQ` range decomposition.

```lean
lemma rangeGaugeWeightBarQ_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightBarQ f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 3 × Fin 2 => QuarkDoublet.valueGaugeWeight j)
```

**`StandardModel.FermionSector.rangeGaugeWeightL_supp`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L336).

> The support of the `L` range decomposition.

```lean
lemma rangeGaugeWeightL_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightL f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 2 => -(LeptonDoubletV.valueGaugeWeight j))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarL_supp`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L341).

> The support of the `barL` range decomposition.

```lean
lemma rangeGaugeWeightBarL_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightBarL f l).supp
      = Finset.univ.image (fun j : Fin 2 × Fin 2 => LeptonDoubletV.valueGaugeWeight j)
```

**`StandardModel.FermionSector.rangeGaugeWeightE_supp`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L346).

> The support of the `e` range decomposition.

```lean
lemma rangeGaugeWeightE_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightE f l).supp
      = Finset.univ.image (fun j : Fin 2 => -(LeptonSinglet.valueGaugeWeight j))
```

**`StandardModel.FermionSector.rangeGaugeWeightBarE_supp`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L351).

> The support of the `bare` range decomposition.

```lean
lemma rangeGaugeWeightBarE_supp (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    (rangeGaugeWeightBarE f l).supp
      = Finset.univ.image (fun j : Fin 2 => LeptonSinglet.valueGaugeWeight j)
```

**`StandardModel.FermionSector.derivSubmoduleGaugeWeight_supp`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean#L359).

> The support of the gauge weight decomposition of the fermion derivative
> submodules is the set of gauge weights of the ten species, independent of the number of
> covariant derivatives.

```lean
lemma derivSubmoduleGaugeWeight_supp (n : ℕ) :
    (derivSubmoduleGaugeWeight n).supp = fermionGaugeWeights
```

## Depends on

- [The fermion sector](../part-02/localfieldalgebra-fermionsector-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/Deriv/GaugeWeight.lean)
