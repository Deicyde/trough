---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.repJetGaugeGroupIFermion, StandardModel.JetAlgebra.repJetGaugeGroupIBoson, StandardModel.JetAlgebra.repJetGaugeGroupI, StandardModel.JetAlgebra.repJetGaugeGroupI_tmul, StandardModel.JetAlgebra.repJetGaugeGroupI_apply_mul, StandardModel.JetAlgebra.complexRepJetGaugeGroupI_apply_one, StandardModel.JetAlgebra.repJetGaugeGroupI_matter_one, StandardModel.JetAlgebra.repJetGaugeGroupI_includeConnection
statement: formalized
proof: formalized
---

# The jet gauge action on the jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.GaugeAction`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean): 13 declarations, 12 with a docstring.

## i. Overview

> The jet gauge group acts on the jet algebra of the Standard Model factor by factor. On the
> two matter factors it is the free-algebra functor applied to the species-wise action
> `fieldData.repJetFermion`, `fieldData.repJetBoson` on the generator spaces; on the
> connection factor it is the generic affine action `LocalGaugeFieldAlgebra.complexRepJet` of the
> Standard Model's local gauge data, whose linear part is the all-orders Leibniz convolution
> of the adjoint Taylor coefficients and whose constant part is the Maurer–Cartan shift. The
> action is multiplicative — a jet of gauge transformations acts on a Lagrangian term factor
> by factor — and restricts to each sector's own action through the sector inclusion.

## ii. Key results

> - `JetAlgebra.repJetGaugeGroupI` : the jet gauge action.
> - `JetAlgebra.repJetGaugeGroupI_apply_mul` : the action is multiplicative.
> - `JetAlgebra.repJetGaugeGroupI_includeConnection`,
>   `JetAlgebra.repJetGaugeGroupI_includeFermionFactor`,
>   `JetAlgebra.repJetGaugeGroupI_includeBosonFactor` : the restriction to each of the three
>   factors of the carrier.
> - `JetAlgebra.repJetGaugeGroupI_includeGauge`,
>   `JetAlgebra.repJetGaugeGroupI_includeFermion`,
>   `JetAlgebra.repJetGaugeGroupI_includeHiggs` : the restriction to each of the three
>   sectors, in the Standard Model presentation of them.

## iv. References

> * None.

## A. The action of the jet gauge group

**`StandardModel.JetAlgebra.repJetGaugeGroupIFermion`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L71).

> The jet gauge action on the fermionic factor: the exterior-algebra functor applied to
> the species-wise action on the fermionic generator space.

```lean
noncomputable abbrev repJetGaugeGroupIFermion :
    Representation ℂ JetGaugeGroupI (ExteriorAlgebra ℂ fieldData.FermionGenerators)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupIBoson`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L77).

> The jet gauge action on the bosonic factor: the symmetric-algebra functor applied to
> the species-wise action on the bosonic generator space.

```lean
noncomputable abbrev repJetGaugeGroupIBoson :
    Representation ℂ JetGaugeGroupI (SymmetricAlgebra ℂ fieldData.BosonGenerators)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L84).

> The jet gauge action on the jet algebra of the Standard Model. Matter is acted on
> species by species from `fieldData`; the connection factor carries the generic affine
> `LocalGaugeFieldAlgebra.complexRepJet` action of the Standard Model local gauge data.

```lean
noncomputable def repJetGaugeGroupI : Representation ℂ JetGaugeGroupI JetAlgebra
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_tmul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L89).

```lean
lemma repJetGaugeGroupI_tmul (U : JetGaugeGroupI)
    (w : ExteriorAlgebra ℂ fieldData.FermionGenerators ⊗[ℂ]
      SymmetricAlgebra ℂ fieldData.BosonGenerators)
    (g : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    repJetGaugeGroupI U (w ⊗ₜ[ℂ] g)
      = ((repJetGaugeGroupIFermion.tprod repJetGaugeGroupIBoson) U w)
          ⊗ₜ[ℂ] (_root_.LocalGaugeFieldAlgebra.complexRepJet localGaugeData U g)
```

### A.1. Multiplicativity

**`StandardModel.JetAlgebra.repJetGaugeGroupI_apply_mul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L105).

> The jet gauge action on the jet algebra is multiplicative: a jet of gauge
> transformations acts on a Lagrangian term factor by factor.

```lean
lemma repJetGaugeGroupI_apply_mul (U : JetGaugeGroupI) (x y : JetAlgebra) :
    repJetGaugeGroupI U (x * y) = repJetGaugeGroupI U x * repJetGaugeGroupI U y
```

### A.2. The action on the three factors

**`StandardModel.JetAlgebra.complexRepJetGaugeGroupI_apply_one`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L121).

> The jet gauge action on the complexified gauge sector fixes the unit.

```lean
lemma complexRepJetGaugeGroupI_apply_one (U : JetGaugeGroupI) :
    (_root_.LocalGaugeFieldAlgebra.complexRepJet localGaugeData) U
      (1 : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) = 1
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_matter_one`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L130).

> The matter factor of the jet gauge action fixes the unit. The proof instantiates the
> abstract `Representation.tprod_apply_one`, so that the unit of the matter factor is never
> unfolded: its two free algebras are quotients by congruences.

```lean
lemma repJetGaugeGroupI_matter_one (U : JetGaugeGroupI) :
    (repJetGaugeGroupIFermion.tprod repJetGaugeGroupIBoson) U
        (1 : fieldData.MatterAlgebra) = 1
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeConnection`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L139).

> The jet gauge action restricts to the generic connection factor, where it is the
> generic affine action of the Standard Model local gauge data.

```lean
lemma repJetGaugeGroupI_includeConnection (U : JetGaugeGroupI)
    (y : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    repJetGaugeGroupI U (fieldData.includeConnection y)
      = fieldData.includeConnection
          (_root_.LocalGaugeFieldAlgebra.complexRepJet localGaugeData U y)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeFermionFactor`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L154).

> The jet gauge action restricts to the fermionic factor, where it is the
> exterior-algebra functor applied to the species-wise action of the datum. The factor
> inclusions are unfolded through the generic `GaugeFieldData` rules rather than by `rfl`:
> at the Standard Model datum the definitional unfolding of the units has to see through
> the unexposed ring congruence of the symmetric algebra.

```lean
lemma repJetGaugeGroupI_includeFermionFactor (U : JetGaugeGroupI)
    (a : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    repJetGaugeGroupI U (fieldData.includeFermion a)
      = fieldData.includeFermion (repJetGaugeGroupIFermion U a)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeBosonFactor`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L169).

> The jet gauge action restricts to the bosonic factor, where it is the
> symmetric-algebra functor applied to the species-wise action of the datum.

```lean
lemma repJetGaugeGroupI_includeBosonFactor (U : JetGaugeGroupI)
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    repJetGaugeGroupI U (fieldData.includeBoson b)
      = fieldData.includeBoson (repJetGaugeGroupIBoson U b)
```

### A.3. The action on the three sectors

> The two matter sector inclusions factor through the sector equivalences, which intertwine
> the two presentations of the jet gauge action by section C of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Structure`; so the action restricts
> to each sector's own action under its existing name.

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeGauge`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L196).

> The jet gauge action restricts to the gauge sector's own action. The gauge sector
> inclusion is the connection inclusion of the datum, the Standard Model gauge bosons being
> the generic ones at `GaugeAlgebra`.

```lean
lemma repJetGaugeGroupI_includeGauge (U : JetGaugeGroupI)
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    repJetGaugeGroupI U (includeGauge y)
      = includeGauge (_root_.LocalGaugeFieldAlgebra.complexRepJet localGaugeData U y)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeFermion`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L203).

> The jet gauge action restricts to the fermionic sector's own action.

```lean
lemma repJetGaugeGroupI_includeFermion (U : JetGaugeGroupI) (f : FermionJetAlgebra) :
    repJetGaugeGroupI U (includeFermion f)
      = includeFermion (FermionJetAlgebra.repJetGaugeGroupI U f)
```

**`StandardModel.JetAlgebra.repJetGaugeGroupI_includeHiggs`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean#L211).

> The jet gauge action restricts to the Higgs sector's own action.

```lean
lemma repJetGaugeGroupI_includeHiggs (U : JetGaugeGroupI) (h : HiggsJetAlgebra) :
    repJetGaugeGroupI U (includeHiggs h)
      = includeHiggs (HiggsJetAlgebra.repJetGaugeGroupI U h)
```

## Depends on

- [The jet algebra of the Standard Model](jetalgebra-basic.md)

## Proof depends on

- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)
- [The generator identifications respect the transformation data](../part-08/jetalgebra-sectorequiv-structure.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/GaugeAction.lean)
