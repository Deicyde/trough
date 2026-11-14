---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.jetValLinEquiv, StandardModel.HiggsVec.jetValLinEquiv_tmul, StandardModel.HiggsVec.jetValLinEquiv_smul, StandardModel.HiggsVec.jetValLinEquiv_symm_smul, StandardModel.HiggsVec.jetGaugeMatrix, StandardModel.HiggsVec.jetGaugeMatrix_one, StandardModel.HiggsVec.jetGaugeMatrix_mul, StandardModel.HiggsVec.repJetGaugeGroupI
statement: formalized
proof: formalized
---

# The jet algebra of the Higgs field (Basic)

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.JetAlgebra.Basic`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean): 11 declarations, 6 with a docstring.

## i. Overview

> The Higgs field is a bosonic matter field valued in `HiggsVec`, so its jet algebra is the
> bosonic algebra `BosonicAlgebra HiggsVec`: the symmetric algebra on the component
> functions `∂_s H_α` and `∂_s H̄_α`, commuting as bosons do.
>
> The file first equips the jets `SpaceTimeAlgebra ⊗[ℂ] HiggsVec` of the Higgs field with the action
> of the jet gauge group, following the same pattern as the fermion species (see
> `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.Basic`): the `SU(2)` power-series matrix,
> scaled by the hypercharge power series `u ^ 3`, acts `SpaceTimeAlgebra`-linearly through the
> identification `SpaceTimeAlgebra ⊗[ℂ] HiggsVec ≃ EuclideanSpace SpaceTimeAlgebra (Fin 2)`.
> Everything the generic bosonic algebra provides — the total derivative, the Lorentz action (trivial:
> the Higgs is a Lorentz scalar), the jet gauge action, and the mass-weight scaling at the Higgs mass
> weight `2` — is then instantiated.

## ii. Key results

> - `HiggsVec.jetValLinEquiv` : the jets of the Higgs field as a `SpaceTimeAlgebra`-valued doublet.
> - `HiggsVec.repJetGaugeGroupI` : the jet gauge action on the jets of the Higgs field.
> - `HiggsVec.repJetGaugeGroupI_smul` : the action is fibrewise.
> - `HiggsVec.repJetGaugeGroupI_ofConstant` : constant jets act by the global gauge action.
> - `HiggsJetAlgebra` : the jet algebra of the Higgs field.
> - `HiggsJetAlgebra.ofHiggs`, `HiggsJetAlgebra.ofConjHiggs` : the component functions.
> - `HiggsJetAlgebra.repLorentzGroup`, `HiggsJetAlgebra.repJetGaugeGroupI` : the actions.
> - `HiggsJetAlgebra.massWeightScale` : the mass-dimension scaling at mass weight `2`.

## iv. References

> * None.

## A. The jet gauge action on the jets of the Higgs field

### A.1. The jets of the Higgs field

**`StandardModel.HiggsVec.jetValLinEquiv`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L81).

> Absorbs the jet ring into the weak index: a jet of the Higgs field is the same thing
> as a `SpaceTimeAlgebra`-valued weak doublet,
>
>   `SpaceTimeAlgebra ⊗[ℂ] HiggsVec ≃ EuclideanSpace SpaceTimeAlgebra (Fin 2)`.

```lean
noncomputable def jetValLinEquiv :
    SpaceTimeAlgebra ⊗[ℂ] HiggsVec ≃ₗ[ℂ] EuclideanSpace SpaceTimeAlgebra (Fin 2)
```

**`StandardModel.HiggsVec.jetValLinEquiv_tmul`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L88).

```lean
lemma jetValLinEquiv_tmul (f : SpaceTimeAlgebra) (v : HiggsVec) :
    jetValLinEquiv (f ⊗ₜ[ℂ] v) = WithLp.toLp 2 fun i => v.ofLp i • f
```

**`StandardModel.HiggsVec.jetValLinEquiv_smul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L93).

> The identification of the jets of the Higgs field is `SpaceTimeAlgebra`-linear: multiplying a
> jet by a scalar jet multiplies each of its weak components.

```lean
lemma jetValLinEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] HiggsVec) :
    jetValLinEquiv (χ • z) = χ • jetValLinEquiv z
```

**`StandardModel.HiggsVec.jetValLinEquiv_symm_smul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L104).

```lean
lemma jetValLinEquiv_symm_smul (χ : SpaceTimeAlgebra)
    (y : EuclideanSpace SpaceTimeAlgebra (Fin 2)) :
    jetValLinEquiv.symm (χ • y) = χ • jetValLinEquiv.symm y
```

### A.2. The action of the jet gauge group

**`StandardModel.HiggsVec.jetGaugeMatrix`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L119).

> The matrix of jets through which a jet of gauge transformations acts on the Higgs
> doublet: the `SU(2)` power-series matrix scaled by the hypercharge power series
> `u ^ 3`.

```lean
noncomputable def jetGaugeMatrix (U : JetGaugeGroupI) : Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra
```

**`StandardModel.HiggsVec.jetGaugeMatrix_one`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L124).

```lean
lemma jetGaugeMatrix_one : jetGaugeMatrix 1 = 1
```

**`StandardModel.HiggsVec.jetGaugeMatrix_mul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L127).

```lean
lemma jetGaugeMatrix_mul (U₁ U₂ : JetGaugeGroupI) :
    jetGaugeMatrix (U₁ * U₂) = jetGaugeMatrix U₁ * jetGaugeMatrix U₂
```

**`StandardModel.HiggsVec.repJetGaugeGroupI`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L145).

> The `2_{3}` action of the jet gauge group on the jets of the Higgs field. Through
> `jetValLinEquiv` the weak matrix of the gauge jet, carrying the `3` hypercharge phase
> `u ^ 3`, acts `SpaceTimeAlgebra`-linearly by matrix-vector multiplication.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] HiggsVec)
```

**`StandardModel.HiggsVec.repJetGaugeGroupI_apply`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L168).

```lean
lemma repJetGaugeGroupI_apply (U : JetGaugeGroupI) (z : SpaceTimeAlgebra ⊗[ℂ] HiggsVec) :
    repJetGaugeGroupI U z =
      jetValLinEquiv.symm
        (Matrix.toLpLinAlgEquiv 2 (jetGaugeMatrix U) (jetValLinEquiv z))
```

### A.3. Fibrewise linearity

**`StandardModel.HiggsVec.repJetGaugeGroupI_smul`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L183).

> **The jet gauge action on the jets of the Higgs field is fibrewise**: it commutes
> with multiplication by scalar jets, acting on the values of the field over the identity
> on spacetime. This is the hypothesis under which the action lifts to the bosonic
> algebra.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] HiggsVec) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

### A.4. Constant jets act by the global gauge action

**`StandardModel.HiggsVec.repJetGaugeGroupI_ofConstant`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean#L198).

> On jets of constant gauge transformations the jet action reduces to the global gauge
> action on the fibre: the action `HiggsVec.repGaugeGroupI` on the Higgs factor, and the
> trivial action on the jet ring.

```lean
lemma repJetGaugeGroupI_ofConstant (g : GaugeGroupI) :
    repJetGaugeGroupI (JetGaugeGroupI.ofConstant g) =
      TensorProduct.map LinearMap.id (repGaugeGroupI g)
```

## Depends on

- [The Higgs field](../../../../physlib/particles/standardmodel/higgsboson/basic.md)
- [The jet gauge group](../part-04/gaugegroup-jetgaugegroup-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/JetAlgebra/Basic.lean)
