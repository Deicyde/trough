---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.transformsIn_higgsField, StandardModel.JetAlgebra.transformsIn_conjHiggsField, StandardModel.JetAlgebra.transformsIn_downSingletField, StandardModel.JetAlgebra.transformsIn_conjDownSingletField, StandardModel.JetAlgebra.transformsIn_upSingletField, StandardModel.JetAlgebra.transformsIn_conjUpSingletField, StandardModel.JetAlgebra.transformsIn_quarkDoubletField, StandardModel.JetAlgebra.transformsIn_conjQuarkDoubletField
statement: formalized
proof: formalized
---

# The transformation laws of the field symbols of the jet algebra

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.TransformsIn`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean): 24 declarations, 24 with a docstring; 5 private, not shown.

## i. Overview

> The thirteen families of derivative symbols of the jet algebra of the Standard Model
> carry two group actions: the jet gauge action `JetAlgebra.repJetGaugeGroupI` and the
> Lorentz action `JetAlgebra.repLorentzGroup`. This file establishes how each family
> transforms under each of them.
>
> The work is mechanical. The six sector restriction lemmas it rests on — the three sector
> inclusions being equivariant for each of the two actions — are proved where the two actions
> are defined, in `PhyslibAlpha.Particles.StandardModel.JetAlgebra.GaugeAction` and
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.LorentzAction`; with them every transformation
> law of a matter symbol is its sector's own law, pushed through an algebra map.
>
> These are the facts from which the transformation laws of an arbitrary Standard Model
> are obtained, by pushing them along the defining algebra map out of the jet algebra.

## ii. Key results

> - `JetAlgebra.transformsIn_higgsField` and its companions : the jet gauge transformation
>   of the thirteen families.
> - `JetAlgebra.isLorentzDerivTransforms_higgsField` and its companions : the Lorentz
>   transformation of the thirteen families.

## iv. References

> * None.

## A. The jet gauge transformation of the field symbols

> `TransformsIn` asks that a jet of gauge transformations mix a derivative symbol with the
> lower symbols by the all-orders Leibniz convolution of the base-point Taylor coefficients
> of the gauge jet. Each sector proves that law for its own symbols; the inclusions of
> section A carry it to the full algebra, and the species bridge of
> `PhyslibAlpha.Particles.StandardModel.Fermions.JetAlgebra.Species` moves the fermionic law from
> the total target space `FermionSpace` down to the individual species.

### A.1. The Higgs families

**`StandardModel.JetAlgebra.transformsIn_higgsField`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L87).

> The Higgs symbols transform in the jet gauge representation carried by the jets of the
> Higgs field.

```lean
lemma transformsIn_higgsField :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI HiggsVec.repJetGaugeGroupI
      higgsField
```

**`StandardModel.JetAlgebra.transformsIn_conjHiggsField`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L103).

> The conjugate Higgs symbols transform in the conjugate of the jet gauge representation
> carried by the jets of the Higgs field.

```lean
lemma transformsIn_conjHiggsField :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj HiggsVec.repJetGaugeGroupI)
      conjHiggsField
```

### A.2. The fermion families

**`StandardModel.JetAlgebra.transformsIn_downSingletField`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L210).

> The symbols of the `i`-th generation down-type quark singlet transform in the jet gauge
> representation carried by the jets of that species.

```lean
lemma transformsIn_downSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI DownSinglet.repJetGaugeGroupI
      (downSingletField i)
```

**`StandardModel.JetAlgebra.transformsIn_conjDownSingletField`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L218).

> The conjugate symbols of the `i`-th generation down-type quark singlet transform in the
> conjugate of the jet gauge representation carried by the jets of that species.

```lean
lemma transformsIn_conjDownSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj DownSinglet.repJetGaugeGroupI) (conjDownSingletField i)
```

**`StandardModel.JetAlgebra.transformsIn_upSingletField`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L227).

> The symbols of the `i`-th generation up-type quark singlet transform in the jet gauge
> representation carried by the jets of that species.

```lean
lemma transformsIn_upSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI UpSinglet.repJetGaugeGroupI
      (upSingletField i)
```

**`StandardModel.JetAlgebra.transformsIn_conjUpSingletField`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L235).

> The conjugate symbols of the `i`-th generation up-type quark singlet transform in the
> conjugate of the jet gauge representation carried by the jets of that species.

```lean
lemma transformsIn_conjUpSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj UpSinglet.repJetGaugeGroupI) (conjUpSingletField i)
```

**`StandardModel.JetAlgebra.transformsIn_quarkDoubletField`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L244).

> The symbols of the `i`-th generation quark doublet transform in the jet gauge
> representation carried by the jets of that species.

```lean
lemma transformsIn_quarkDoubletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI QuarkDoublet.repJetGaugeGroupI
      (quarkDoubletField i)
```

**`StandardModel.JetAlgebra.transformsIn_conjQuarkDoubletField`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L252).

> The conjugate symbols of the `i`-th generation quark doublet transform in the
> conjugate of the jet gauge representation carried by the jets of that species.

```lean
lemma transformsIn_conjQuarkDoubletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj QuarkDoublet.repJetGaugeGroupI) (conjQuarkDoubletField i)
```

**`StandardModel.JetAlgebra.transformsIn_leptonDoubletField`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L261).

> The symbols of the `i`-th generation lepton doublet transform in the jet gauge
> representation carried by the jets of that species.

```lean
lemma transformsIn_leptonDoubletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI LeptonDoubletV.repJetGaugeGroupI
      (leptonDoubletField i)
```

**`StandardModel.JetAlgebra.transformsIn_conjLeptonDoubletField`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L269).

> The conjugate symbols of the `i`-th generation lepton doublet transform in the
> conjugate of the jet gauge representation carried by the jets of that species.

```lean
lemma transformsIn_conjLeptonDoubletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj LeptonDoubletV.repJetGaugeGroupI) (conjLeptonDoubletField i)
```

**`StandardModel.JetAlgebra.transformsIn_leptonSingletField`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L278).

> The symbols of the `i`-th generation charged-lepton singlet transform in the jet gauge
> representation carried by the jets of that species.

```lean
lemma transformsIn_leptonSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI LeptonSinglet.repJetGaugeGroupI
      (leptonSingletField i)
```

**`StandardModel.JetAlgebra.transformsIn_conjLeptonSingletField`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L286).

> The conjugate symbols of the `i`-th generation charged-lepton singlet transform in the
> conjugate of the jet gauge representation carried by the jets of that species.

```lean
lemma transformsIn_conjLeptonSingletField (i : Fin 3) :
    LocalGaugeData.TransformsIn (B := JetAlgebra) repJetGaugeGroupI
      (JetComponentSpace.repConj LeptonSinglet.repJetGaugeGroupI) (conjLeptonSingletField i)
```

## B. The Lorentz transformation of the field symbols

> `IsLorentzDerivTransforms` asks that each derivative slot of a symbol mix into all tuples
> of directions by the columns of the Lorentz matrix, while the value index transforms by the
> contragredient of the species' Lorentz representation. The mixing of the slots is
> `IsLorentzDeriv.rep_iteratedD_ofFn`, available because the total derivative on the jet
> algebra is a Lorentz vector; what is left is the undifferentiated law at `n = 0`, which is
> the equivariance of the component functions of each sector.

### B.1. The Higgs families

> The Higgs is a Lorentz scalar, so its value index carries the trivial representation and
> the conjugate index its conjugate.

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_higgsField`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L314).

> The Higgs symbols transform as the derivative symbols of a Lorentz scalar.

```lean
lemma isLorentzDerivTransforms_higgsField :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      (Representation.trivial ℂ SL(2,ℂ) HiggsVec) higgsField
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjHiggsField`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L338).

> The conjugate Higgs symbols transform as the derivative symbols of the conjugate of a
> Lorentz scalar.

```lean
lemma isLorentzDerivTransforms_conjHiggsField :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      (Representation.trivial ℂ SL(2,ℂ) HiggsVec).conj conjHiggsField
```

### B.2. The fermion families

> The Lorentz action on `FermionSpace` is species-diagonal, so the contragredient action on a
> covector pulled back from a species is the pullback of the species' own contragredient
> action; that identity is definitional, and it is the only input the species need beyond the
> law for the total fermionic symbols.

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_downSingletField`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L443).

> The symbols of the `i`-th generation down-type quark singlet transform as the derivative
> symbols of a Weyl spinor in that species' Lorentz representation.

```lean
lemma isLorentzDerivTransforms_downSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      DownSinglet.repLorentzGroup (downSingletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjDownSingletField`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L451).

> The conjugate symbols of the `i`-th generation down-type quark singlet transform as the
> derivative symbols of the conjugate Weyl spinor.

```lean
lemma isLorentzDerivTransforms_conjDownSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      DownSinglet.repLorentzGroup.conj (conjDownSingletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_upSingletField`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L460).

> The symbols of the `i`-th generation up-type quark singlet transform as the derivative
> symbols of a Weyl spinor in that species' Lorentz representation.

```lean
lemma isLorentzDerivTransforms_upSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      UpSinglet.repLorentzGroup (upSingletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjUpSingletField`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L468).

> The conjugate symbols of the `i`-th generation up-type quark singlet transform as the
> derivative symbols of the conjugate Weyl spinor.

```lean
lemma isLorentzDerivTransforms_conjUpSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      UpSinglet.repLorentzGroup.conj (conjUpSingletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_quarkDoubletField`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L477).

> The symbols of the `i`-th generation quark doublet transform as the derivative
> symbols of a Weyl spinor in that species' Lorentz representation.

```lean
lemma isLorentzDerivTransforms_quarkDoubletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      QuarkDoublet.repLorentzGroup (quarkDoubletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjQuarkDoubletField`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L485).

> The conjugate symbols of the `i`-th generation quark doublet transform as the
> derivative symbols of the conjugate Weyl spinor.

```lean
lemma isLorentzDerivTransforms_conjQuarkDoubletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      QuarkDoublet.repLorentzGroup.conj (conjQuarkDoubletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_leptonDoubletField`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L494).

> The symbols of the `i`-th generation lepton doublet transform as the derivative
> symbols of a Weyl spinor in that species' Lorentz representation.

```lean
lemma isLorentzDerivTransforms_leptonDoubletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      LeptonDoubletV.repLorentzGroup (leptonDoubletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjLeptonDoubletField`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L502).

> The conjugate symbols of the `i`-th generation lepton doublet transform as the
> derivative symbols of the conjugate Weyl spinor.

```lean
lemma isLorentzDerivTransforms_conjLeptonDoubletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      LeptonDoubletV.repLorentzGroup.conj (conjLeptonDoubletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_leptonSingletField`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L511).

> The symbols of the `i`-th generation charged-lepton singlet transform as the derivative
> symbols of a Weyl spinor in that species' Lorentz representation.

```lean
lemma isLorentzDerivTransforms_leptonSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      LeptonSinglet.repLorentzGroup (leptonSingletField i)
```

**`StandardModel.JetAlgebra.isLorentzDerivTransforms_conjLeptonSingletField`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean#L519).

> The conjugate symbols of the `i`-th generation charged-lepton singlet transform as the
> derivative symbols of the conjugate Weyl spinor.

```lean
lemma isLorentzDerivTransforms_conjLeptonSingletField (i : Fin 3) :
    IsLorentzDerivTransforms (A := JetAlgebra) repLorentzGroup
      LeptonSinglet.repLorentzGroup.conj (conjLeptonSingletField i)
```

## Depends on

- [The generators of the jet algebra of the Standard Model](../part-07/jetalgebra-generators.md)

## Proof depends on

- [The field algebra of the Standard Model is everything](../part-07/jetalgebra-fieldalgebra.md)
- [The transformation law of the bosonic generators](matter-bosonic-transformsin.md)
- [The transformation law of the fermionic generators](../part-09/matter-fermionic-transformsin.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/TransformsIn.lean)
