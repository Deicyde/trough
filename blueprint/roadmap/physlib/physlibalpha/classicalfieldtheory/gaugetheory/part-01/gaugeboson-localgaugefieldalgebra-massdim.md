---
declaration: module
origin: cited
lean: GaugeBoson.FieldDerivSpace.massWeightScale, GaugeBoson.FieldDerivSpace.massWeightScale_tmul, GaugeBoson.FieldDerivSpace.massWeightScale_jetDeriv, LocalGaugeFieldAlgebra.massWeightScale, LocalGaugeFieldAlgebra.massWeightScale_ι, LocalGaugeFieldAlgebra.massWeightScale_ofA, LocalGaugeFieldAlgebra.massWeightScale_jetDeriv, LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv
statement: formalized
proof: formalized
---

# Mass dimension on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.MassDim`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean): 8 declarations, 6 with a docstring.

> The scaling of the gauge-boson jet algebra by mass weight.

## i. Overview

> The mass dimension of the gauge bosons is tracked multiplicatively through the
> *mass-weight scaling*, the algebra endomorphism multiplying each generator `∂_s A_μ^φ` by
> `c ^ (2 + 2 |s|)`. The gauge field has mass dimension one, that is mass weight two, and each
> derivative adds mass weight two. A monomial of total mass weight `n` is scaled by `c ^ n`,
> so the scaling records the mass-weight grading of the jet algebra. This is the gauge-boson
> part of the scaling `GaugeFieldData.massWeightScale` of a full local field algebra, on the
> real, single-half component space of the gauge bosons.

## ii. Key results

> - `GaugeBoson.FieldDerivSpace.massWeightScale` : the scaling on the component space.
> - `LocalGaugeFieldAlgebra.massWeightScale` : the mass-weight scaling.
> - `LocalGaugeFieldAlgebra.massWeightScale_ofA` : the gauge field carries mass weight two.
> - `LocalGaugeFieldAlgebra.massWeightScale_jetDeriv` : a derivative adds mass weight two.
> - `LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv` : `∂_s` adds mass weight `2 |s|`.

## iv. References

> * None.

## A. The mass-weight scaling on the component space

**`GaugeBoson.FieldDerivSpace.massWeightScale`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L66).

> The mass-weight scaling on the field-derivative space of the gauge bosons. The generator
> `∂_s A_μ^φ` is scaled by `c ^ (2 + 2 |s|)`, through the derivative-degree scaling
> `SpaceTimeDerivAlgebraℝ.gradeScale` on the derivative label.

```lean
noncomputable def FieldDerivSpace.massWeightScale (c : ℝ) :
    (FieldDerivSpace G) →ₗ[ℝ] (FieldDerivSpace G)
```

**`GaugeBoson.FieldDerivSpace.massWeightScale_tmul`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L70).

```lean
lemma FieldDerivSpace.massWeightScale_tmul (c : ℝ) (a : SpaceTimeDerivAlgebraℝ)
    (φ : Module.Dual ℝ (GaugeBoson G)) :
    (FieldDerivSpace.massWeightScale G) c (a ⊗ₜ[ℝ] φ)
      = c ^ 2 • (SpaceTimeDerivAlgebraℝ.gradeScale (c ^ 2) a ⊗ₜ[ℝ] φ)
```

**`GaugeBoson.FieldDerivSpace.massWeightScale_jetDeriv`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L76).

> The derivative shift carries mass weight two on the component space.

```lean
lemma FieldDerivSpace.massWeightScale_jetDeriv (c : ℝ) (μ : Fin 1 ⊕ Fin 3)
    (v : (FieldDerivSpace G)) :
    (FieldDerivSpace.massWeightScale G) c ((FieldDerivSpace.jetDeriv G) μ v)
      = c ^ 2 • (FieldDerivSpace.jetDeriv G) μ ((FieldDerivSpace.massWeightScale G) c v)
```

## B. The mass-weight scaling on the jet algebra

**`LocalGaugeFieldAlgebra.massWeightScale`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L104).

> The mass-weight scaling on the gauge-boson jet algebra, the algebra endomorphism
> scaling the generator `∂_s A_μ^φ` by `c ^ (2 + 2 |s|)`, the functorial lift of the
> scaling on the field-derivative space.

```lean
noncomputable def massWeightScale (c : ℝ) :
    (LocalGaugeFieldAlgebra G) →ₐ[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.massWeightScale_ι`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L109).

```lean
lemma massWeightScale_ι (c : ℝ) (x : (GaugeBoson.FieldDerivSpace G)) :
    (massWeightScale G) c (SymmetricAlgebra.ι ℝ _ x)
      = SymmetricAlgebra.ι ℝ _ ((GaugeBoson.FieldDerivSpace.massWeightScale G) c x)
```

## C. The mass weight of the gauge field and its derivatives

**`LocalGaugeFieldAlgebra.massWeightScale_ofA`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L122).

> The gauge field carries mass weight two — mass dimension one.

```lean
lemma massWeightScale_ofA (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (massWeightScale G) c ((ofA G) μ φ) = c ^ 2 • (ofA G) μ φ
```

**`LocalGaugeFieldAlgebra.massWeightScale_jetDeriv`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L128).

> A total derivative adds mass weight two.

```lean
lemma massWeightScale_jetDeriv (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (x : (LocalGaugeFieldAlgebra G)) :
    (massWeightScale G) c ((jetDeriv G) μ x) = c ^ 2 • (jetDeriv G) μ
      ((massWeightScale G) c x)
```

**`LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean#L144).

> The iterated derivative `∂_s` adds mass weight `2 |s|`.

```lean
lemma massWeightScale_iteratedJetDeriv (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : (LocalGaugeFieldAlgebra G)) :
    (massWeightScale G) c ((iteratedJetDeriv G) s x)
      = c ^ (2 * Multiset.card s) • (iteratedJetDeriv G) s ((massWeightScale G) c x)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-jetderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassDim.lean)
