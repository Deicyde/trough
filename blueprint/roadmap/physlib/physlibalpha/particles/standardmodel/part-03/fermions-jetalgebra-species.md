---
declaration: module
origin: cited
lean: StandardModel.lTensor_comp_jetOfConstant, StandardModel.lTensor_comp_jetDeriv, StandardModel.lTensor_comp_jetIteratedDeriv, StandardModel.jetEval_comp_lTensor, StandardModel.repCoeff_comp, StandardModel.repDualCoeff_comp, StandardModel.FermionSpace.jetEquiv_leptonDoublet, StandardModel.FermionSpace.jetEquiv_leptonSinglet
statement: formalized
proof: formalized
---

# Species compatibility inside the fermionic target space

The module `PhyslibAlpha.Particles.StandardModel.Fermions.JetAlgebra.Species`, [PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean): 34 declarations, 34 with a docstring.

## i. Overview

> The fermionic jet algebra is built on `FermionSpace`, the product of the five fermion
> species; but each species carries its own Lorentz and jet gauge representation, and the
> Standard Model obligations are stated against those. This file is the bridge between the
> two levels.
>
> Everything rests on one fact: both actions on `FermionSpace` are species-diagonal — the
> jet gauge action through `FermionSpace.jetActionMap`, the Lorentz action through
> `Representation.pi` and `Representation.prod`. So each projection
> `FermionSpace →ₗ[ℂ] Species` intertwines the total action with the species' own, and hence
> also the base-point Taylor coefficients `GaugeAlgebraRealization.repCoeff` of the two.
>
> The third bridge runs the other way. Component functions are covectors, and a covector on
> the species pulls back along the projection to a covector on `FermionSpace`; since
> `FermionSpace` is a finite product, the identity is the sum over species and generations of
> inclusion after projection, so every covector is a sum of pulled-back ones. The pulled-back
> covectors therefore span, which is what lets an adjoin over the species covectors reach an
> adjoin over all of them.

## ii. Key results

> - `StandardModel.repCoeff_comp` : naturality of the base-point Taylor coefficients along a
>   map of value spaces intertwining the two jet gauge actions.
> - `FermionSpace.leptonDoubletProj_comp_repCoeff`, … : the gauge compatibility of the five
>   species.
> - `FermionSpace.leptonDoubletProj_comp_repLorentzGroup`, … : the Lorentz compatibility.
> - `FermionSpace.span_speciesDual_eq_top`, `span_speciesConjDual_eq_top` : the covectors
>   pulled back from the species span every covector.

## iv. References

> * None.

## A. Naturality of the value-space jet toolkit

### A.1. The pieces of `repCoeff`

**`StandardModel.lTensor_comp_jetOfConstant`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L88).

> Including a constant into value-space jets is natural in the value space.

```lean
lemma lTensor_comp_jetOfConstant (p : V →ₗ[ℂ] W) :
    (LinearMap.lTensor SpaceTimeAlgebra p).comp jetOfConstant = jetOfConstant.comp p
```

**`StandardModel.lTensor_comp_jetDeriv`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L94).

> The formal derivative on value-space jets is natural in the value space: it touches
> only the jet factor.

```lean
lemma lTensor_comp_jetDeriv (p : V →ₗ[ℂ] W) (μ : Fin 1 ⊕ Fin 3) :
    (LinearMap.lTensor SpaceTimeAlgebra p).comp (jetDeriv μ)
      = (jetDeriv μ).comp (LinearMap.lTensor SpaceTimeAlgebra p)
```

**`StandardModel.lTensor_comp_jetIteratedDeriv`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L100).

> The iterated formal derivative on value-space jets is natural in the value space.

```lean
lemma lTensor_comp_jetIteratedDeriv (p : V →ₗ[ℂ] W) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (LinearMap.lTensor SpaceTimeAlgebra p).comp (jetIteratedDeriv s)
      = (jetIteratedDeriv s).comp (LinearMap.lTensor SpaceTimeAlgebra p)
```

**`StandardModel.jetEval_comp_lTensor`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L112).

> Evaluation of a value-space jet at the base point is natural in the value space.

```lean
lemma jetEval_comp_lTensor (p : V →ₗ[ℂ] W) :
    (jetEval (V := W)).comp (LinearMap.lTensor SpaceTimeAlgebra p) = p.comp jetEval
```

### A.2. Naturality of `repCoeff` and `repDualCoeff`

**`StandardModel.repCoeff_comp`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L127).

> The base-point Taylor coefficients of two jet gauge actions are intertwined by any map
> of value spaces intertwining the actions themselves: `repCoeff` is built from
> `jetOfConstant`, `jetIteratedDeriv` and `jetEval`, and each of those is natural.

```lean
lemma repCoeff_comp {repV : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    {repW : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] W)} (p : V →ₗ[ℂ] W)
    (hp : ∀ U : JetGaugeGroupI, (LinearMap.lTensor SpaceTimeAlgebra p).comp (repV U)
      = (repW U).comp (LinearMap.lTensor SpaceTimeAlgebra p))
    (U : JetGaugeGroupI) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    p.comp (GaugeAlgebraRealization.repCoeff repV U s)
      = (GaugeAlgebraRealization.repCoeff repW U s).comp p
```

**`StandardModel.repDualCoeff_comp`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L147).

> The transposed form of `repCoeff_comp`: the dual coefficients, which act on the
> component-function index, are intertwined the other way round.

```lean
lemma repDualCoeff_comp {repV : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    {repW : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] W)} (p : V →ₗ[ℂ] W)
    (hp : ∀ U : JetGaugeGroupI, (LinearMap.lTensor SpaceTimeAlgebra p).comp (repV U)
      = (repW U).comp (LinearMap.lTensor SpaceTimeAlgebra p))
    (U : JetGaugeGroupI) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (GaugeAlgebraRealization.repDualCoeff repV U s).comp (Module.Dual.transpose p)
      = (Module.Dual.transpose p).comp (GaugeAlgebraRealization.repDualCoeff repW U s)
```

## B. The jet gauge action is species-diagonal

### B.1. The species components of the splitting of the jets

> The splitting `FermionSpace.jetEquiv` of the jets of the total fermionic field is, in each
> species-and-generation slot, nothing but the projection applied to the value factor.

**`StandardModel.FermionSpace.jetEquiv_leptonDoublet`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L176).

> The lepton-doublet slot of the splitting of the jets is the projection on the value
> factor.

```lean
lemma jetEquiv_leptonDoublet (i : Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    (jetEquiv z).1 i = LinearMap.lTensor SpaceTimeAlgebra (leptonDoubletProj i) z
```

**`StandardModel.FermionSpace.jetEquiv_leptonSinglet`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L184).

> The charged-lepton-singlet slot of the splitting of the jets is the projection on the value
> factor.

```lean
lemma jetEquiv_leptonSinglet (i : Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    (jetEquiv z).2.1 i = LinearMap.lTensor SpaceTimeAlgebra (leptonSingletProj i) z
```

**`StandardModel.FermionSpace.jetEquiv_quarkDoublet`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L192).

> The quark-doublet slot of the splitting of the jets is the projection on the value
> factor.

```lean
lemma jetEquiv_quarkDoublet (i : Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    (jetEquiv z).2.2.1 i = LinearMap.lTensor SpaceTimeAlgebra (quarkDoubletProj i) z
```

**`StandardModel.FermionSpace.jetEquiv_upSinglet`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L200).

> The up-type-quark-singlet slot of the splitting of the jets is the projection on the value
> factor.

```lean
lemma jetEquiv_upSinglet (i : Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    (jetEquiv z).2.2.2.1 i = LinearMap.lTensor SpaceTimeAlgebra (upSingletProj i) z
```

**`StandardModel.FermionSpace.jetEquiv_downSinglet`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L208).

> The down-type-quark-singlet slot of the splitting of the jets is the projection on the value
> factor.

```lean
lemma jetEquiv_downSinglet (i : Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    (jetEquiv z).2.2.2.2 i = LinearMap.lTensor SpaceTimeAlgebra (downSingletProj i) z
```

### B.2. The projections intertwine the jet gauge actions

> `FermionSpace.jetActionMap` is a product of the species actions, slot by slot, so through
> the splitting of B.1 each projection carries the total jet gauge action to the species'
> own.

**`StandardModel.FermionSpace.lTensor_leptonDoubletProj_repJetGaugeGroupI`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L226).

> The lepton-doublet projection intertwines the total jet gauge action with the
> lepton doublet's own.

```lean
lemma lTensor_leptonDoubletProj_repJetGaugeGroupI (i : Fin 3) (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (leptonDoubletProj i)).comp (repJetGaugeGroupI U)
      = (LeptonDoubletV.repJetGaugeGroupI U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (leptonDoubletProj i))
```

**`StandardModel.FermionSpace.lTensor_leptonSingletProj_repJetGaugeGroupI`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L243).

> The charged-lepton-singlet projection intertwines the total jet gauge action with the
> charged-lepton singlet's own.

```lean
lemma lTensor_leptonSingletProj_repJetGaugeGroupI (i : Fin 3) (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (leptonSingletProj i)).comp (repJetGaugeGroupI U)
      = (LeptonSinglet.repJetGaugeGroupI U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (leptonSingletProj i))
```

**`StandardModel.FermionSpace.lTensor_quarkDoubletProj_repJetGaugeGroupI`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L260).

> The quark-doublet projection intertwines the total jet gauge action with the
> quark doublet's own.

```lean
lemma lTensor_quarkDoubletProj_repJetGaugeGroupI (i : Fin 3) (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (quarkDoubletProj i)).comp (repJetGaugeGroupI U)
      = (QuarkDoublet.repJetGaugeGroupI U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (quarkDoubletProj i))
```

**`StandardModel.FermionSpace.lTensor_upSingletProj_repJetGaugeGroupI`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L277).

> The up-type-quark-singlet projection intertwines the total jet gauge action with the
> up-type quark singlet's own.

```lean
lemma lTensor_upSingletProj_repJetGaugeGroupI (i : Fin 3) (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (upSingletProj i)).comp (repJetGaugeGroupI U)
      = (UpSinglet.repJetGaugeGroupI U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (upSingletProj i))
```

**`StandardModel.FermionSpace.lTensor_downSingletProj_repJetGaugeGroupI`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L294).

> The down-type-quark-singlet projection intertwines the total jet gauge action with the
> down-type quark singlet's own.

```lean
lemma lTensor_downSingletProj_repJetGaugeGroupI (i : Fin 3) (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (downSingletProj i)).comp (repJetGaugeGroupI U)
      = (DownSinglet.repJetGaugeGroupI U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (downSingletProj i))
```

### B.3. The species compatibility of `repCoeff`

**`StandardModel.FermionSpace.leptonDoubletProj_comp_repCoeff`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L317).

> The lepton-doublet projection intertwines the base-point Taylor coefficients of
> the total jet gauge action with those of the lepton doublet's own.

```lean
lemma leptonDoubletProj_comp_repCoeff (i : Fin 3) (U : JetGaugeGroupI)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (leptonDoubletProj i).comp (GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U s)
      = (GaugeAlgebraRealization.repCoeff LeptonDoubletV.repJetGaugeGroupI U s).comp
          (leptonDoubletProj i)
```

**`StandardModel.FermionSpace.leptonSingletProj_comp_repCoeff`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L326).

> The charged-lepton-singlet projection intertwines the base-point Taylor coefficients of
> the total jet gauge action with those of the charged-lepton singlet's own.

```lean
lemma leptonSingletProj_comp_repCoeff (i : Fin 3) (U : JetGaugeGroupI)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (leptonSingletProj i).comp (GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U s)
      = (GaugeAlgebraRealization.repCoeff LeptonSinglet.repJetGaugeGroupI U s).comp
          (leptonSingletProj i)
```

**`StandardModel.FermionSpace.quarkDoubletProj_comp_repCoeff`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L335).

> The quark-doublet projection intertwines the base-point Taylor coefficients of
> the total jet gauge action with those of the quark doublet's own.

```lean
lemma quarkDoubletProj_comp_repCoeff (i : Fin 3) (U : JetGaugeGroupI)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (quarkDoubletProj i).comp (GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U s)
      = (GaugeAlgebraRealization.repCoeff QuarkDoublet.repJetGaugeGroupI U s).comp
          (quarkDoubletProj i)
```

**`StandardModel.FermionSpace.upSingletProj_comp_repCoeff`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L344).

> The up-type-quark-singlet projection intertwines the base-point Taylor coefficients of
> the total jet gauge action with those of the up-type quark singlet's own.

```lean
lemma upSingletProj_comp_repCoeff (i : Fin 3) (U : JetGaugeGroupI)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (upSingletProj i).comp (GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U s)
      = (GaugeAlgebraRealization.repCoeff UpSinglet.repJetGaugeGroupI U s).comp
          (upSingletProj i)
```

**`StandardModel.FermionSpace.downSingletProj_comp_repCoeff`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L353).

> The down-type-quark-singlet projection intertwines the base-point Taylor coefficients of
> the total jet gauge action with those of the down-type quark singlet's own.

```lean
lemma downSingletProj_comp_repCoeff (i : Fin 3) (U : JetGaugeGroupI)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (downSingletProj i).comp (GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U s)
      = (GaugeAlgebraRealization.repCoeff DownSinglet.repJetGaugeGroupI U s).comp
          (downSingletProj i)
```

## C. The Lorentz action is species-diagonal

> `FermionSpace.repLorentzGroup` is a `Representation.prod` of `Representation.pi`s of the
> species representations, so each projection intertwines it with the species' own Lorentz
> action on the nose.

**`StandardModel.FermionSpace.leptonDoubletProj_comp_repLorentzGroup`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L372).

> The lepton-doublet projection intertwines the total Lorentz action with the
> lepton doublet's own.

```lean
lemma leptonDoubletProj_comp_repLorentzGroup (i : Fin 3) (Λ : SL(2,ℂ)) :
    (leptonDoubletProj i).comp (repLorentzGroup Λ)
      = (LeptonDoubletV.repLorentzGroup Λ).comp (leptonDoubletProj i)
```

**`StandardModel.FermionSpace.leptonSingletProj_comp_repLorentzGroup`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L378).

> The charged-lepton-singlet projection intertwines the total Lorentz action with the
> charged-lepton singlet's own.

```lean
lemma leptonSingletProj_comp_repLorentzGroup (i : Fin 3) (Λ : SL(2,ℂ)) :
    (leptonSingletProj i).comp (repLorentzGroup Λ)
      = (LeptonSinglet.repLorentzGroup Λ).comp (leptonSingletProj i)
```

**`StandardModel.FermionSpace.quarkDoubletProj_comp_repLorentzGroup`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L384).

> The quark-doublet projection intertwines the total Lorentz action with the
> quark doublet's own.

```lean
lemma quarkDoubletProj_comp_repLorentzGroup (i : Fin 3) (Λ : SL(2,ℂ)) :
    (quarkDoubletProj i).comp (repLorentzGroup Λ)
      = (QuarkDoublet.repLorentzGroup Λ).comp (quarkDoubletProj i)
```

**`StandardModel.FermionSpace.upSingletProj_comp_repLorentzGroup`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L390).

> The up-type-quark-singlet projection intertwines the total Lorentz action with the
> up-type quark singlet's own.

```lean
lemma upSingletProj_comp_repLorentzGroup (i : Fin 3) (Λ : SL(2,ℂ)) :
    (upSingletProj i).comp (repLorentzGroup Λ)
      = (UpSinglet.repLorentzGroup Λ).comp (upSingletProj i)
```

**`StandardModel.FermionSpace.downSingletProj_comp_repLorentzGroup`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L396).

> The down-type-quark-singlet projection intertwines the total Lorentz action with the
> down-type quark singlet's own.

```lean
lemma downSingletProj_comp_repLorentzGroup (i : Fin 3) (Λ : SL(2,ℂ)) :
    (downSingletProj i).comp (repLorentzGroup Λ)
      = (DownSinglet.repLorentzGroup Λ).comp (downSingletProj i)
```

## D. Covectors pulled back from the species

### D.1. The decomposition of the identity

**`StandardModel.FermionSpace.sum_incl_proj`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L414).

> The identity on the total fermionic target space is the sum, over the five species and
> the three generations, of the inclusion after the projection.

```lean
lemma sum_incl_proj (v : FermionSpace) :
    (∑ i, leptonDoubletIncl i (leptonDoubletProj i v))
      + (∑ i, leptonSingletIncl i (leptonSingletProj i v))
      + (∑ i, quarkDoubletIncl i (quarkDoubletProj i v))
      + (∑ i, upSingletIncl i (upSingletProj i v))
      + (∑ i, downSingletIncl i (downSingletProj i v)) = v
```

**`StandardModel.FermionSpace.sum_conj_incl_proj`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L429).

> The conjugate form of `sum_incl_proj`: conjugation leaves the underlying additive
> group and the underlying maps alone.

```lean
lemma sum_conj_incl_proj (v : ConjModule FermionSpace) :
    (∑ i, ConjModule.map (leptonDoubletIncl i)
        (ConjModule.map (leptonDoubletProj i) v))
      + (∑ i, ConjModule.map (leptonSingletIncl i)
          (ConjModule.map (leptonSingletProj i) v))
      + (∑ i, ConjModule.map (quarkDoubletIncl i)
          (ConjModule.map (quarkDoubletProj i) v))
      + (∑ i, ConjModule.map (upSingletIncl i)
          (ConjModule.map (upSingletProj i) v))
      + (∑ i, ConjModule.map (downSingletIncl i)
          (ConjModule.map (downSingletProj i) v)) = v
```

### D.2. Covectors

**`StandardModel.FermionSpace.dual_eq_sum`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L451).

> Every covector on the total fermionic target space is the sum, over the five species
> and the three generations, of its restriction to that species and generation pulled back
> along the corresponding projection.

```lean
lemma dual_eq_sum (φ : Module.Dual ℂ FermionSpace) :
    φ = (∑ i, Module.Dual.transpose (leptonDoubletProj i)
          (Module.Dual.transpose (leptonDoubletIncl i) φ))
      + (∑ i, Module.Dual.transpose (leptonSingletProj i)
          (Module.Dual.transpose (leptonSingletIncl i) φ))
      + (∑ i, Module.Dual.transpose (quarkDoubletProj i)
          (Module.Dual.transpose (quarkDoubletIncl i) φ))
      + (∑ i, Module.Dual.transpose (upSingletProj i)
          (Module.Dual.transpose (upSingletIncl i) φ))
      + (∑ i, Module.Dual.transpose (downSingletProj i)
          (Module.Dual.transpose (downSingletIncl i) φ))
```

**`StandardModel.FermionSpace.speciesDual`**, a def, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L470).

> The covectors on the total fermionic target space that are pulled back from a single
> species and generation.

```lean
def speciesDual : Set (Module.Dual ℂ FermionSpace)
```

**`StandardModel.FermionSpace.span_speciesDual_eq_top`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L485).

> The covectors pulled back from the individual species and generations span every
> covector on the total fermionic target space. This is what lets an adjoin taken over the
> species covectors reach an adjoin taken over all of them.

```lean
lemma span_speciesDual_eq_top : Submodule.span ℂ speciesDual = ⊤
```

### D.3. Conjugate covectors

**`StandardModel.FermionSpace.conjDual_eq_sum`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L510).

> The conjugate form of `dual_eq_sum`: every covector on the conjugate of the total
> fermionic target space is the sum of the covectors pulled back from the species and
> generations.

```lean
lemma conjDual_eq_sum (φ : Module.Dual ℂ (ConjModule FermionSpace)) :
    φ = (∑ i, Module.Dual.transpose (ConjModule.map (leptonDoubletProj i))
          (Module.Dual.transpose (ConjModule.map (leptonDoubletIncl i)) φ))
      + (∑ i, Module.Dual.transpose (ConjModule.map (leptonSingletProj i))
          (Module.Dual.transpose (ConjModule.map (leptonSingletIncl i)) φ))
      + (∑ i, Module.Dual.transpose (ConjModule.map (quarkDoubletProj i))
          (Module.Dual.transpose (ConjModule.map (quarkDoubletIncl i)) φ))
      + (∑ i, Module.Dual.transpose (ConjModule.map (upSingletProj i))
          (Module.Dual.transpose (ConjModule.map (upSingletIncl i)) φ))
      + (∑ i, Module.Dual.transpose (ConjModule.map (downSingletProj i))
          (Module.Dual.transpose (ConjModule.map (downSingletIncl i)) φ))
```

**`StandardModel.FermionSpace.speciesConjDual`**, a def, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L529).

> The covectors on the conjugate of the total fermionic target space that are pulled
> back from a single species and generation.

```lean
def speciesConjDual : Set (Module.Dual ℂ (ConjModule FermionSpace))
```

**`StandardModel.FermionSpace.span_speciesConjDual_eq_top`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean#L543).

> The conjugate covectors pulled back from the individual species and generations span
> every covector on the conjugate of the total fermionic target space.

```lean
lemma span_speciesConjDual_eq_top : Submodule.span ℂ speciesConjDual = ⊤
```

## Depends on

- [The fermionic jet algebra of the Standard Model](fermions-jetalgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Species.lean)
