---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.repLorentzGroupFermion, StandardModel.JetAlgebra.repLorentzGroupBoson, StandardModel.JetAlgebra.repLorentzGroup, StandardModel.JetAlgebra.repLorentzGroup_tmul, StandardModel.JetAlgebra.repLorentzGroup_apply_mul, StandardModel.JetAlgebra.complexRepLorentzGroup_apply_one, StandardModel.JetAlgebra.repLorentzGroup_matter_one, StandardModel.JetAlgebra.repLorentzGroup_includeConnection
statement: formalized
proof: formalized
---

# The Lorentz action on the jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.LorentzAction`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean): 15 declarations, 14 with a docstring; 1 private, not shown.

## i. Overview

> The Lorentz group acts on the jet algebra of the Standard Model factor by factor: on the
> two matter factors by the free-algebra functor applied to the species-wise Lorentz action
> on the generator spaces of the field datum, and on the connection factor by the generic
> complexified gauge-boson action. The action is multiplicative, restricts to the gauge
> sector's own action through the sector inclusion, and intertwines the total derivative
> through the columns of the Lorentz matrix — the total derivative is a Lorentz vector,
> packaged as a `Lorentz.IsLorentzDeriv` instance.
>
> The covariance of the derivative is assembled from the factor facts through an abstract
> two-factor lemma proved at small types and instantiated, which keeps the proof outside the
> full tensor product. On each free-algebra factor it comes from the
> general covariance of the derivation extending a linear endomorphism, which is proved by
> induction on the algebra: a derivation is not an algebra map, so extensionality of algebra
> maps would not settle it.

## ii. Key results

> - `JetAlgebra.repLorentzGroup` : the Lorentz action.
> - `JetAlgebra.repLorentzGroup_apply_mul` : the action is multiplicative.
> - `JetAlgebra.repLorentzGroup_includeGauge`,
>   `JetAlgebra.repLorentzGroup_includeFermion`, `JetAlgebra.repLorentzGroup_includeHiggs` :
>   the restriction to each of the three sectors.
> - `JetAlgebra.repLorentzGroup_jetDeriv`, `JetAlgebra.instIsLorentzDeriv` : the total
>   derivative is a Lorentz vector.

## iv. References

> * None.

## A. The action of the Lorentz group

**`StandardModel.JetAlgebra.repLorentzGroupFermion`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L75).

> The Lorentz action on the fermionic factor: the exterior-algebra functor applied to
> the species-wise Lorentz action on the fermionic generator space.

```lean
noncomputable abbrev repLorentzGroupFermion :
    Representation ℂ SL(2,ℂ) (ExteriorAlgebra ℂ fieldData.FermionGenerators)
```

**`StandardModel.JetAlgebra.repLorentzGroupBoson`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L80).

> The Lorentz action on the bosonic factor.

```lean
noncomputable abbrev repLorentzGroupBoson :
    Representation ℂ SL(2,ℂ) (SymmetricAlgebra ℂ fieldData.BosonGenerators)
```

**`StandardModel.JetAlgebra.repLorentzGroup`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L86).

> The Lorentz action on the jet algebra of the Standard Model: the three factors
> transform independently.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) JetAlgebra
```

**`StandardModel.JetAlgebra.repLorentzGroup_tmul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L91).

```lean
lemma repLorentzGroup_tmul (Λ : SL(2,ℂ))
    (w : ExteriorAlgebra ℂ fieldData.FermionGenerators ⊗[ℂ]
      SymmetricAlgebra ℂ fieldData.BosonGenerators)
    (g : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    repLorentzGroup Λ (w ⊗ₜ[ℂ] g)
      = ((repLorentzGroupFermion.tprod repLorentzGroupBoson) Λ w)
          ⊗ₜ[ℂ] (_root_.LocalGaugeFieldAlgebra.complexRepLorentzGroup GaugeAlgebra Λ g)
```

### A.1. Multiplicativity

**`StandardModel.JetAlgebra.repLorentzGroup_apply_mul`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L106).

> The Lorentz action on the jet algebra is multiplicative.

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : JetAlgebra) :
    repLorentzGroup Λ (x * y) = repLorentzGroup Λ x * repLorentzGroup Λ y
```

### A.2. The action on the three factors

**`StandardModel.JetAlgebra.complexRepLorentzGroup_apply_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L122).

> The Lorentz action on the complexified gauge sector fixes the unit.

```lean
lemma complexRepLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    (_root_.LocalGaugeFieldAlgebra.complexRepLorentzGroup GaugeAlgebra) Λ
      (1 : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) = 1
```

**`StandardModel.JetAlgebra.repLorentzGroup_matter_one`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L131).

> The matter factor of the Lorentz action fixes the unit, by the same abstract
> instantiation as in the gauge action.

```lean
lemma repLorentzGroup_matter_one (Λ : SL(2,ℂ)) :
    (repLorentzGroupFermion.tprod repLorentzGroupBoson) Λ
        (1 : fieldData.MatterAlgebra) = 1
```

**`StandardModel.JetAlgebra.repLorentzGroup_includeConnection`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L139).

> The Lorentz action restricts to the generic connection factor.

```lean
lemma repLorentzGroup_includeConnection (Λ : SL(2,ℂ))
    (y : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    repLorentzGroup Λ (fieldData.includeConnection y)
      = fieldData.includeConnection
          (_root_.LocalGaugeFieldAlgebra.complexRepLorentzGroup GaugeAlgebra Λ y)
```

**`StandardModel.JetAlgebra.repLorentzGroup_includeFermionFactor`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L151).

> The Lorentz action restricts to the fermionic factor, where it is the
> exterior-algebra functor applied to the species-wise action of the datum.

```lean
lemma repLorentzGroup_includeFermionFactor (Λ : SL(2,ℂ))
    (a : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    repLorentzGroup Λ (fieldData.includeFermion a)
      = fieldData.includeFermion (repLorentzGroupFermion Λ a)
```

**`StandardModel.JetAlgebra.repLorentzGroup_includeBosonFactor`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L166).

> The Lorentz action restricts to the bosonic factor, where it is the
> symmetric-algebra functor applied to the species-wise action of the datum.

```lean
lemma repLorentzGroup_includeBosonFactor (Λ : SL(2,ℂ))
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    repLorentzGroup Λ (fieldData.includeBoson b)
      = fieldData.includeBoson (repLorentzGroupBoson Λ b)
```

### A.3. The action on the three sectors

**`StandardModel.JetAlgebra.repLorentzGroup_includeGauge`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L188).

> The Lorentz action restricts to the gauge sector's own action. The gauge sector
> inclusion is the connection inclusion of the datum, the Standard Model gauge bosons being
> the generic ones at `GaugeAlgebra`.

```lean
lemma repLorentzGroup_includeGauge (Λ : SL(2,ℂ))
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    repLorentzGroup Λ (includeGauge y)
      = includeGauge (_root_.LocalGaugeFieldAlgebra.complexRepLorentzGroup GaugeAlgebra Λ y)
```

**`StandardModel.JetAlgebra.repLorentzGroup_includeFermion`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L195).

> The Lorentz action restricts to the fermionic sector's own action.

```lean
lemma repLorentzGroup_includeFermion (Λ : SL(2,ℂ)) (f : FermionJetAlgebra) :
    repLorentzGroup Λ (includeFermion f)
      = includeFermion (FermionJetAlgebra.repLorentzGroup Λ f)
```

**`StandardModel.JetAlgebra.repLorentzGroup_includeHiggs`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L202).

> The Lorentz action restricts to the Higgs sector's own action.

```lean
lemma repLorentzGroup_includeHiggs (Λ : SL(2,ℂ)) (h : HiggsJetAlgebra) :
    repLorentzGroup Λ (includeHiggs h)
      = includeHiggs (HiggsJetAlgebra.repLorentzGroup Λ h)
```

## B. The total derivative is a Lorentz vector

**`StandardModel.JetAlgebra.repLorentzGroup_jetDeriv`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L249).

> **The total derivative on the jet algebra is a Lorentz vector.**

```lean
lemma repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (x : JetAlgebra) :
    repLorentzGroup Λ (jetDeriv μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        jetDeriv a (repLorentzGroup Λ x)
```

**`StandardModel.JetAlgebra.instIsLorentzDeriv`**, an instance, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean#L303).

> The total derivatives on the jet algebra form a Lorentz derivative.

```lean
instance instIsLorentzDeriv : Lorentz.IsLorentzDeriv repLorentzGroup jetDeriv
```

## Depends on

- [The total derivative on the jet algebra of the Standard Model](jetalgebra-jetderiv.md)

## Proof depends on

- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)
- [The generator identifications respect the transformation data](../part-08/jetalgebra-sectorequiv-structure.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/LorentzAction.lean)
