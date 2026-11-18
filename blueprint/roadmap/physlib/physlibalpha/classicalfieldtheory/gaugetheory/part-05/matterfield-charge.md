---
declaration: module
origin: cited
lean: MatterField.chargePow, MatterField.chargePow_one, MatterField.chargePow_mul, MatterField.chargeRep, MatterField.chargeRep_tmul, MatterField.chargeRep_smul, MatterField.charged, MatterField.charged_V
statement: formalized
proof: formalized
---

# Charged matter fields under `U(1)` jets

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Charge`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean): 8 declarations, 4 with a docstring.

## i. Overview

> A field valued in a complex vector space `V` with integer charge `n` transforms under a
> `U(1)` gauge transformation `U = e^{iχ}` by `ψ ↦ U^n ψ`. On jets this is multiplication of the
> jet-ring factor of `SpaceTimeAlgebra ⊗[ℂ] V` by the unitary power series `U^n`; the action is
> manifestly fibrewise. `MatterField.charged` packages a Lorentz representation, a charge,
> a mass weight and a declared statistic into a matter field for the jet gauge group
> `unitary SpaceTimeAlgebra` of `U(1)`.

## ii. Key results

> - `MatterField.chargeRep` : the charge-`n` action of `U(1)` jets on the jets of a field.
> - `MatterField.chargeRep_smul` : the action is fibrewise.
> - `MatterField.charged` : the matter field of charge `n`, over a supplied
>   infinitesimal action of the gauge algebra.

## iv. References

> * None.

## A. Powers of a unitary jet

**`MatterField.chargePow`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L55).

> The unitary power series `U ^ n` of a `U(1)` jet, for an integer charge `n`.

```lean
noncomputable def chargePow (n : ℤ) (U : unitary SpaceTimeAlgebra) : SpaceTimeAlgebra
```

**`MatterField.chargePow_one`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L58).

```lean
lemma chargePow_one (n : ℤ) : chargePow n 1 = 1
```

**`MatterField.chargePow_mul`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L61).

```lean
lemma chargePow_mul (n : ℤ) (U W : unitary SpaceTimeAlgebra) :
    chargePow n (U * W) = chargePow n U * chargePow n W
```

## B. The charge action on jets

**`MatterField.chargeRep`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L73).

> **The charge-`n` action of `U(1)` jets on the jets of a `V`-valued field**:
> multiplication of the jet-ring factor by `U ^ n`.

```lean
noncomputable def chargeRep (n : ℤ) (V : Type) [AddCommGroup V] [Module ℂ V] :
    Representation ℂ (unitary SpaceTimeAlgebra) (SpaceTimeAlgebra ⊗[ℂ] V)
```

**`MatterField.chargeRep_tmul`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L87).

```lean
lemma chargeRep_tmul (n : ℤ) (U : unitary SpaceTimeAlgebra) (f : SpaceTimeAlgebra) (v : V) :
    chargeRep n V U (f ⊗ₜ[ℂ] v) = (chargePow n U * f) ⊗ₜ[ℂ] v
```

**`MatterField.chargeRep_smul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L92).

> **The charge action is fibrewise**: it commutes with multiplication by scalar jets.

```lean
lemma chargeRep_smul (n : ℤ) (U : unitary SpaceTimeAlgebra) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    chargeRep n V U (χ • z) = χ • chargeRep n V U z
```

## C. Charged matter fields

**`MatterField.charged`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L118).

> **The charged matter field**: a field with values in `V`, Lorentz representation
> `repLorentz`, electric charge `n`, mass weight `w` and declared statistic `σ`, as a matter
> field for the jets of `U(1)`, in any gauge context `jets` whose jet group is
> `unitary SpaceTimeAlgebra`.
>
> The infinitesimal action `act` of the gauge algebra is supplied, not constructed. For a
> charge-`n` field it is `c ↦ (i n φ(c)) • id` for the functional `φ` reading off the
> `u(1)` component of `c`, and no such functional is available: `jets` relates the gauge
> algebra `𝔤` to the jets only through `evalLie` and `maurerCartan`, neither of which
> identifies a `u(1)` direction in an arbitrary `𝔤`. The rest of the data does not depend
> on `jets` beyond its jet group, so it is supplied polymorphically.

```lean
noncomputable def charged {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    (jets : LocalGaugeData G₀ 𝔤 (unitary SpaceTimeAlgebra) 𝔤J) [Module.Free ℂ V] [Module.Finite ℂ V]
    (repLorentz : Representation ℂ SL(2,ℂ) V) (n : ℤ) (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (hact : jets.IsInfinitesimalActionOf act (chargeRep n V)) (w : ℕ) (σ : FieldStatistic) :
    MatterField jets
```

**`MatterField.charged_V`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean#L134).

```lean
lemma charged_V {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    (jets : LocalGaugeData G₀ 𝔤 (unitary SpaceTimeAlgebra) 𝔤J) [Module.Free ℂ V] [Module.Finite ℂ V]
    (repLorentz : Representation ℂ SL(2,ℂ) V) (n : ℤ) (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (hact : jets.IsInfinitesimalActionOf act (chargeRep n V)) (w : ℕ) (σ : FieldStatistic) :
    (charged jets repLorentz n act hact w σ).V = V
```

## Depends on

- [Matter fields of a gauge theory](matterfield-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Charge.lean)
