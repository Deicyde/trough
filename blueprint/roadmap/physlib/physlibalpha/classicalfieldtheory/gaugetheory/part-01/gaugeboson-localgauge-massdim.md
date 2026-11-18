---
declaration: module
origin: cited
lean: GaugeBoson.JetComponentSpace.massWeightScale, GaugeBoson.JetComponentSpace.massWeightScale_tmul, GaugeBoson.JetComponentSpace.massWeightScale_jetDeriv, LocalGaugeFieldAlgebra.massWeightScale, LocalGaugeFieldAlgebra.massWeightScale_ι, LocalGaugeFieldAlgebra.massWeightScale_ofA, LocalGaugeFieldAlgebra.massWeightScale_jetDeriv, LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv
statement: formalized
proof: formalized
---

# Mass dimension on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.MassDim`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean): 8 declarations, 6 with a docstring.

## i. Overview

> The mass dimension of the gauge bosons is tracked multiplicatively through the
> *mass-weight scaling*: the algebra endomorphism multiplying each generator `∂_s A_μ^φ` by
> `c ^ (2 + 2 |s|)` — the gauge field has mass dimension one, i.e. mass weight two, and each
> derivative adds mass weight two. A monomial of total mass weight `n` is scaled by `c ^ n`,
> so the scaling records the mass-weight grading of the jet algebra. This mirrors
> `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.MassDim`, on the real,
> single-half component space of the gauge bosons.

## ii. Key results

> - `GaugeBoson.JetComponentSpace.massWeightScale` : the scaling on the component space.
> - `LocalGaugeFieldAlgebra.massWeightScale` : the mass-weight scaling.
> - `LocalGaugeFieldAlgebra.massWeightScale_ofA` : the gauge field carries mass weight two.
> - `LocalGaugeFieldAlgebra.massWeightScale_jetDeriv` : a derivative adds mass weight two.
> - `LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv` : `∂_s` adds mass weight `2 |s|`.

## iv. References

> * None.

## A. The mass-weight scaling on the component space

**`GaugeBoson.JetComponentSpace.massWeightScale`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L64).

> The mass-weight scaling on the jet component space of the gauge bosons: the generator
> `∂_s A_μ^φ` is scaled by `c ^ (2 + 2 |s|)`, through the derivative-degree scaling
> `SpaceTimeDerivAlgebraℝ.gradeScale` on the derivative label.

```lean
noncomputable def JetComponentSpace.massWeightScale (c : ℝ) :
    (JetComponentSpace 𝔤) →ₗ[ℝ] (JetComponentSpace 𝔤)
```

**`GaugeBoson.JetComponentSpace.massWeightScale_tmul`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L69).

```lean
lemma JetComponentSpace.massWeightScale_tmul (c : ℝ) (a : SpaceTimeDerivAlgebraℝ)
    (φ : Module.Dual ℝ (GaugeBoson 𝔤)) :
    (JetComponentSpace.massWeightScale 𝔤) c (a ⊗ₜ[ℝ] φ)
      = c ^ 2 • (SpaceTimeDerivAlgebraℝ.gradeScale (c ^ 2) a ⊗ₜ[ℝ] φ)
```

**`GaugeBoson.JetComponentSpace.massWeightScale_jetDeriv`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L76).

> **The derivative shift carries mass weight two** on the component space.

```lean
lemma JetComponentSpace.massWeightScale_jetDeriv (c : ℝ) (μ : Fin 1 ⊕ Fin 3)
    (v : (JetComponentSpace 𝔤)) :
    (JetComponentSpace.massWeightScale 𝔤) c ((JetComponentSpace.jetDeriv 𝔤) μ v)
      = c ^ 2 • (JetComponentSpace.jetDeriv 𝔤) μ ((JetComponentSpace.massWeightScale 𝔤) c v)
```

## B. The mass-weight scaling on the jet algebra

**`LocalGaugeFieldAlgebra.massWeightScale`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L104).

> **The mass-weight scaling on the gauge-boson jet algebra**: the algebra endomorphism
> scaling the generator `∂_s A_μ^φ` by `c ^ (2 + 2 |s|)`, the functorial lift of the
> scaling on the jet component space.

```lean
noncomputable def massWeightScale (c : ℝ) :
    (LocalGaugeFieldAlgebra 𝔤) →ₐ[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.massWeightScale_ι`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L110).

```lean
lemma massWeightScale_ι (c : ℝ) (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    (massWeightScale 𝔤) c (SymmetricAlgebra.ι ℝ _ x)
      = SymmetricAlgebra.ι ℝ _ ((GaugeBoson.JetComponentSpace.massWeightScale 𝔤) c x)
```

## C. The mass weight of the gauge field and its derivatives

**`LocalGaugeFieldAlgebra.massWeightScale_ofA`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L124).

> **The gauge field carries mass weight two** — mass dimension one.

```lean
lemma massWeightScale_ofA (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (massWeightScale 𝔤) c ((ofA 𝔤) μ φ) = c ^ 2 • (ofA 𝔤) μ φ
```

**`LocalGaugeFieldAlgebra.massWeightScale_jetDeriv`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L131).

> **A total derivative adds mass weight two.**

```lean
lemma massWeightScale_jetDeriv (c : ℝ) (μ : Fin 1 ⊕ Fin 3) (x : (LocalGaugeFieldAlgebra 𝔤)) :
    (massWeightScale 𝔤) c ((jetDeriv 𝔤) μ x) = c ^ 2 • (jetDeriv 𝔤) μ
      ((massWeightScale 𝔤) c x)
```

**`LocalGaugeFieldAlgebra.massWeightScale_iteratedJetDeriv`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean#L148).

> **The iterated derivative `∂_s` adds mass weight `2 |s|`.**

```lean
lemma massWeightScale_iteratedJetDeriv (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : (LocalGaugeFieldAlgebra 𝔤)) :
    (massWeightScale 𝔤) c ((iteratedJetDeriv 𝔤) s x)
      = c ^ (2 * Multiset.card s) • (iteratedJetDeriv 𝔤) s ((massWeightScale 𝔤) c x)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgauge-jetderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassDim.lean)
