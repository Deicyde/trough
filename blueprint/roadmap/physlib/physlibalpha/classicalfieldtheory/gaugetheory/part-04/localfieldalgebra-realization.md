---
declaration: module
origin: cited
lean: GaugeFieldData.Realization, GaugeFieldData.Realization.id, GaugeFieldData.Realization.map_repJet, GaugeFieldData.Realization.map_repLorentz, GaugeFieldData.Realization.repJet_mul, GaugeFieldData.Realization.repLorentz_mul, GaugeFieldData.Realization.transformsAsGaugeField_mapGaugeField, GaugeFieldData.Realization.toAlgHom_covDerivFieldStrength
statement: formalized
proof: formalized
---

# Realizations of the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean): 8 declarations, 8 with a docstring.

> Equivariant algebra maps out of the local field algebra of a gauge theory.

## i. Overview

> A complex algebra `B` carries the fields of a gauge-field datum when the local field
> algebra `J(T)` maps into it by a complex algebra map equivariant for the jet gauge group
> and the Lorentz group, both acting on `B` by algebra endomorphisms. Such a map is a
> `GaugeFieldData.Realization`. The gauge-field symbols of a realization are those of the
> gauge-boson jet algebra carried along the composite of the inclusion of the connection factor
> with the map, `mapGaugeField (h.toAlgHom.comp T.includeConnection)`. They transform as a gauge
> field, so the gauge-boson symbol theory applies to them, and the realized field-strength tower
> is identified with their covariant tower.

## ii. Key results

> - `GaugeFieldData.Realization` : an algebra carrying the fields of a datum.
> - `GaugeFieldData.Realization.id` : the local field algebra realized in itself.
> - `GaugeFieldData.Realization.transformsAsGaugeField_mapGaugeField` : the gauge-field symbols
>   of a realization transform as a gauge field.
> - `GaugeFieldData.Realization.toAlgHom_covDerivFieldStrength` : the realized field-strength
>   tower is the covariant tower of the realized symbols.

## iv. References

> * None.

## A. Realizations

**`GaugeFieldData.Realization`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L71).

> A complex algebra `B` carrying the fields of the datum `T`, through a complex algebra map out
> of the local field algebra, equivariant for the jet gauge group and the Lorentz group,
> both acting on the whole of `B` by algebra endomorphisms. No commutativity, injectivity
> or surjectivity is assumed, and no derivative operator on `B` is involved. It is built
> from the fields `toAlgHom`, `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of
> `Representation.EquivariantAlgHom`, which the lemmas `map_repJet`, `map_repLorentz`,
> `repJet_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (T : GaugeFieldData G) (B : Type) [Ring B] [Algebra ℂ B]
    (repJet : Representation ℂ G.gaugeJetGroup B) (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.Realization.id`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L83).

> The local field algebra realized in itself, by the identity.

```lean
noncomputable def id : Realization T T.LocalFieldAlgebra T.repJet T.repLorentzGroup
```

**`GaugeFieldData.Realization.map_repJet`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L90).

> The map is equivariant for the jet gauge group.

```lean
lemma map_repJet (U : G.gaugeJetGroup) (x : T.LocalFieldAlgebra) :
    h.toAlgHom (T.repJet U x) = repJet U (h.toAlgHom x)
```

**`GaugeFieldData.Realization.map_repLorentz`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L95).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : T.LocalFieldAlgebra) :
    h.toAlgHom (T.repLorentzGroup Λ x) = repLorentz Λ (h.toAlgHom x)
```

**`GaugeFieldData.Realization.repJet_mul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L101).

> The jet gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repJet_mul (U : G.gaugeJetGroup) (b₁ b₂ : B) :
    repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
```

**`GaugeFieldData.Realization.repLorentz_mul`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L107).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. The gauge bosons of a realization

**`GaugeFieldData.Realization.transformsAsGaugeField_mapGaugeField`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L119).

> The gauge-field symbols of a realization, those of `J(T)` carried along the map, transform
> as a gauge field.

```lean
lemma transformsAsGaugeField_mapGaugeField :
    GaugeBoson.TransformsAsGaugeField G repJet
      (mapGaugeField (h.toAlgHom.comp T.includeConnection))
```

**`GaugeFieldData.Realization.toAlgHom_covDerivFieldStrength`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean#L127).

> The map of a realization carries the included field-strength tower to the covariant
> tower of the realized gauge-field symbols.

```lean
lemma toAlgHom_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    h.toAlgHom (T.covDerivFieldStrength l μ ν φ)
      = iteratedCovDerivAdjoint (mapGaugeField (h.toAlgHom.comp T.includeConnection)) l
        (fieldStrength (mapGaugeField (h.toAlgHom.comp T.includeConnection)) μ ν) 0 φ
```

## Depends on

- [The covariant derivatives in the local field algebra](localfieldalgebra-covariantderiv.md)
- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization.lean)
