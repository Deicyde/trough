---
declaration: module
origin: cited
lean: StandardModel.CovJetAlgebra.isHiggsSector, StandardModel.CovJetAlgebra.isGaugeSector, StandardModel.CovJetAlgebra.isFermionSector, StandardModel.CovJetAlgebra.F_comm_H, StandardModel.CovJetAlgebra.F_comm_barH, StandardModel.CovJetAlgebra.F_comm_d, StandardModel.CovJetAlgebra.F_comm_bard, StandardModel.CovJetAlgebra.F_comm_u
statement: formalized
proof: formalized
---

# The sectors of the covariant jet algebra

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.CovJetAlgebra.Sectors`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean): 35 declarations, 35 with a docstring.

## i. Overview

> The covariant jet algebra of `CovJetAlgebra.Basic` carries the thirteen covariant towers,
> the global gauge action, the Lorentz action and the mass-weight polynomial. This file
> records that they split into the three sectors — gauge, Higgs and fermion — and that the
> towers of different sectors commute: every gauge-equivariance, Lorentz, mass-weight and
> commutation law of the covariant form of the Standard Model holds there.
>
> Nothing new is proved. Each law is the corresponding law of `AlgebraRealization.id` — the
> jet algebra's own — read on the subalgebra, where equality is equality of underlying jet
> algebra elements. The transport lemmas the three shapes need are section E of
> [`Basic.lean`](jetalgebra-covjetalgebra-basic.md); this file assembles them.
>
> `CovJetAlgebra` is to the covariant theory what `JetAlgebra` is to the theory in the bare
> symbols: the object every other covariant Standard Model receives its fields from. That is
> the content of `CovAlgebraRealization`.

## ii. Key results

> - `StandardModel.CovJetAlgebra.isHiggsSector`, `StandardModel.CovJetAlgebra.isGaugeSector`,
>   `StandardModel.CovJetAlgebra.isFermionSector` : the three sectors of the covariant jet
>   algebra.
> - `StandardModel.CovJetAlgebra.F_comm_H` and its companions : the towers of different
>   sectors commute.

## iv. References

> * None.

## A. The three sectors and the cross-sector commutation rules

**`StandardModel.CovJetAlgebra.isHiggsSector`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L69).

> The Higgs sector of the covariant jet algebra: its Higgs towers are the covariant jet
> algebra of the Higgs field, included.

```lean
noncomputable def isHiggsSector :
    HiggsAlgebraCovRealization CovJetAlgebra repGaugeGroupI repLorentzGroup massWeightPoly
```

**`StandardModel.CovJetAlgebra.isGaugeSector`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L82).

> The gauge sector of the covariant jet algebra.

```lean
lemma isGaugeSector : IsGaugeSector CovJetAlgebra repGaugeGroupI repGaugeGroupI_mul
    repLorentzGroup repLorentzGroup_mul (fun {_n} l μ ν => fieldStrength l μ ν)
    massWeightPoly
```

**`StandardModel.CovJetAlgebra.isFermionSector`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L98).

> The fermion sector of the covariant jet algebra.

```lean
lemma isFermionSector : IsFermionSector CovJetAlgebra repGaugeGroupI repGaugeGroupI_mul
    repLorentzGroup repLorentzGroup_mul
    (fun {_n} i l => downSingletField i l) (fun {_n} i l => conjDownSingletField i l)
    (fun {_n} i l => upSingletField i l) (fun {_n} i l => conjUpSingletField i l)
    (fun {_n} i l => quarkDoubletField i l) (fun {_n} i l => conjQuarkDoubletField i l)
    (fun {_n} i l => leptonDoubletField i l) (fun {_n} i l => conjLeptonDoubletField i l)
    (fun {_n} i l => leptonSingletField i l) (fun {_n} i l => conjLeptonSingletField i l)
    massWeightPoly
```

**`StandardModel.CovJetAlgebra.F_comm_H`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L278).

> The cross-sector commutation rule `F_comm_H` in the covariant jet algebra.

```lean
lemma F_comm_H {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) :
    Commute (fieldStrength l μ ν ψ) (higgsField l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_barH`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L285).

> The cross-sector commutation rule `F_comm_barH` in the covariant jet algebra.

```lean
lemma F_comm_barH {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    Commute (fieldStrength l μ ν ψ) (conjHiggsField l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_d`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L292).

> The cross-sector commutation rule `F_comm_d` in the covariant jet algebra.

```lean
lemma F_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ DownSinglet) :
    Commute (fieldStrength l μ ν ψ) (downSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_bard`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L299).

> The cross-sector commutation rule `F_comm_bard` in the covariant jet algebra.

```lean
lemma F_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (fieldStrength l μ ν ψ) (conjDownSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_u`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L306).

> The cross-sector commutation rule `F_comm_u` in the covariant jet algebra.

```lean
lemma F_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ UpSinglet) :
    Commute (fieldStrength l μ ν ψ) (upSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_baru`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L313).

> The cross-sector commutation rule `F_comm_baru` in the covariant jet algebra.

```lean
lemma F_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (fieldStrength l μ ν ψ) (conjUpSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_Q`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L320).

> The cross-sector commutation rule `F_comm_Q` in the covariant jet algebra.

```lean
lemma F_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ QuarkDoublet) :
    Commute (fieldStrength l μ ν ψ) (quarkDoubletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_barQ`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L327).

> The cross-sector commutation rule `F_comm_barQ` in the covariant jet algebra.

```lean
lemma F_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (fieldStrength l μ ν ψ) (conjQuarkDoubletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_L`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L334).

> The cross-sector commutation rule `F_comm_L` in the covariant jet algebra.

```lean
lemma F_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonDoubletV) :
    Commute (fieldStrength l μ ν ψ) (leptonDoubletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_barL`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L341).

> The cross-sector commutation rule `F_comm_barL` in the covariant jet algebra.

```lean
lemma F_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (fieldStrength l μ ν ψ) (conjLeptonDoubletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_e`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L348).

> The cross-sector commutation rule `F_comm_e` in the covariant jet algebra.

```lean
lemma F_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonSinglet) :
    Commute (fieldStrength l μ ν ψ) (leptonSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.F_comm_bare`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L355).

> The cross-sector commutation rule `F_comm_bare` in the covariant jet algebra.

```lean
lemma F_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (fieldStrength l μ ν ψ) (conjLeptonSingletField i l' φ)
```

**`StandardModel.CovJetAlgebra.H_comm_d`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L362).

> The cross-sector commutation rule `H_comm_d` in the covariant jet algebra.

```lean
lemma H_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ DownSinglet) :
    Commute (higgsField l φ) (downSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_bard`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L369).

> The cross-sector commutation rule `H_comm_bard` in the covariant jet algebra.

```lean
lemma H_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (higgsField l φ) (conjDownSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_u`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L376).

> The cross-sector commutation rule `H_comm_u` in the covariant jet algebra.

```lean
lemma H_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ UpSinglet) :
    Commute (higgsField l φ) (upSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_baru`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L383).

> The cross-sector commutation rule `H_comm_baru` in the covariant jet algebra.

```lean
lemma H_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (higgsField l φ) (conjUpSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_Q`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L390).

> The cross-sector commutation rule `H_comm_Q` in the covariant jet algebra.

```lean
lemma H_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (higgsField l φ) (quarkDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_barQ`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L397).

> The cross-sector commutation rule `H_comm_barQ` in the covariant jet algebra.

```lean
lemma H_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (higgsField l φ) (conjQuarkDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_L`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L404).

> The cross-sector commutation rule `H_comm_L` in the covariant jet algebra.

```lean
lemma H_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (higgsField l φ) (leptonDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_barL`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L411).

> The cross-sector commutation rule `H_comm_barL` in the covariant jet algebra.

```lean
lemma H_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (higgsField l φ) (conjLeptonDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_e`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L418).

> The cross-sector commutation rule `H_comm_e` in the covariant jet algebra.

```lean
lemma H_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (higgsField l φ) (leptonSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.H_comm_bare`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L425).

> The cross-sector commutation rule `H_comm_bare` in the covariant jet algebra.

```lean
lemma H_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (higgsField l φ) (conjLeptonSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_d`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L432).

> The cross-sector commutation rule `barH_comm_d` in the covariant jet algebra.

```lean
lemma barH_comm_d {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ DownSinglet) :
    Commute (conjHiggsField l φ) (downSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_bard`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L439).

> The cross-sector commutation rule `barH_comm_bard` in the covariant jet algebra.

```lean
lemma barH_comm_bard {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (conjHiggsField l φ) (conjDownSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_u`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L446).

> The cross-sector commutation rule `barH_comm_u` in the covariant jet algebra.

```lean
lemma barH_comm_u {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ UpSinglet) :
    Commute (conjHiggsField l φ) (upSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_baru`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L453).

> The cross-sector commutation rule `barH_comm_baru` in the covariant jet algebra.

```lean
lemma barH_comm_baru {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (conjHiggsField l φ) (conjUpSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_Q`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L460).

> The cross-sector commutation rule `barH_comm_Q` in the covariant jet algebra.

```lean
lemma barH_comm_Q {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (conjHiggsField l φ) (quarkDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_barQ`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L467).

> The cross-sector commutation rule `barH_comm_barQ` in the covariant jet algebra.

```lean
lemma barH_comm_barQ {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (conjHiggsField l φ) (conjQuarkDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_L`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L474).

> The cross-sector commutation rule `barH_comm_L` in the covariant jet algebra.

```lean
lemma barH_comm_L {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (conjHiggsField l φ) (leptonDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_barL`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L481).

> The cross-sector commutation rule `barH_comm_barL` in the covariant jet algebra.

```lean
lemma barH_comm_barL {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (conjHiggsField l φ) (conjLeptonDoubletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_e`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L488).

> The cross-sector commutation rule `barH_comm_e` in the covariant jet algebra.

```lean
lemma barH_comm_e {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (conjHiggsField l φ) (leptonSingletField i l' φ')
```

**`StandardModel.CovJetAlgebra.barH_comm_bare`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean#L495).

> The cross-sector commutation rule `barH_comm_bare` in the covariant jet algebra.

```lean
lemma barH_comm_bare {n m : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) (i : Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (conjHiggsField l φ) (conjLeptonSingletField i l' φ')
```

## Depends on

- [The fermion sector](../part-05/isfermionsector-basic.md)
- [The gauge sector](../part-06/isgaugesector-basic.md)
- [The algebra valued Higgs boson](../part-10/realization-higgscov-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/CovJetAlgebra/Sectors.lean)
