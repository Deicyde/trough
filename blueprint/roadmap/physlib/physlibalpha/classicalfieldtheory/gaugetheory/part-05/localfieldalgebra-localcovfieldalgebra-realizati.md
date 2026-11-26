---
declaration: module
origin: cited
lean: GaugeFieldData.LocalCovFieldAlgebra.Realization, GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repValue, GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repLorentz, GaugeFieldData.LocalCovFieldAlgebra.Realization.repGauge_mul, GaugeFieldData.LocalCovFieldAlgebra.Realization.repLorentz_mul, GaugeFieldData.Realization.restrict, GaugeFieldData.Realization.restrict_toAlgHom_apply
statement: formalized
proof: formalized
---

# Realizations of the covariant field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.LocalCovFieldAlgebra.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean): 7 declarations, 6 with a docstring.

> Equivariant algebra maps out of the covariant field algebra of a gauge theory.

## i. Overview

> A complex algebra `B` carries the covariant expressions of a gauge-field datum when the
> covariant field algebra maps into it by a complex algebra map equivariant for the ordinary
> gauge group `G.group` and for the Lorentz group, both acting on `B` by algebra endomorphisms.
> Such a map is a `GaugeFieldData.LocalCovFieldAlgebra.Realization`. The gauge compatibility is
> with `G.group` alone because the source action of the ordinary gauge group is the jet action at
> the constant jets. The Lorentz action of the source exists only under
> `GaugeFieldData.GaugeLorentzCompatible`, which is therefore a parameter.
>
> A realization of the local field algebra restricts to one of the covariant field algebra
> (`GaugeFieldData.Realization.restrict`), with `G.group` acting on the target through the
> constant jets. The converse extension is not claimed.

## ii. Key results

> - `GaugeFieldData.LocalCovFieldAlgebra.Realization` : an algebra carrying the covariant
>   field algebra, with the equivariance laws `map_repValue` and `map_repLorentz`.
> - `GaugeFieldData.Realization.restrict` : restriction to the covariant field algebra.

## iv. References

> * None.

## A. Realizations

**`GaugeFieldData.LocalCovFieldAlgebra.Realization`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L71).

> A complex algebra `B` carrying the covariant expressions of the datum `T`, through a complex
> algebra map out of the covariant field algebra, equivariant for the ordinary gauge group
> and the Lorentz group, both acting on the whole of `B` by algebra endomorphisms. The
> Lorentz action of the source needs `GaugeFieldData.GaugeLorentzCompatible`, which is a
> parameter. No other species condition is used. It is built from the fields `toAlgHom`,
> `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of `Representation.EquivariantAlgHom`, which
> the lemmas `map_repValue`, `map_repLorentz`, `repGauge_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (T : GaugeFieldData G) (hGL : T.GaugeLorentzCompatible) (B : Type)
    [Semiring B] [Algebra ℂ B] (repGauge : Representation ℂ G.group B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repValue`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L84).

> The map is equivariant for the ordinary gauge group.

```lean
lemma map_repValue (g : G.group) (x : ↥T.LocalCovFieldAlgebra) :
    k.toAlgHom (repValue T g x) = repGauge g (k.toAlgHom x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repLorentz`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L89).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : ↥T.LocalCovFieldAlgebra) :
    k.toAlgHom (repLorentzGroup T hGL Λ x) = repLorentz Λ (k.toAlgHom x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.repGauge_mul`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L95).

> The ordinary gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repGauge_mul (g : G.group) (b₁ b₂ : B) :
    repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.repLorentz_mul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L101).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. Restriction from the local field algebra

**`GaugeFieldData.Realization.restrict`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L124).

> The restriction of a realization of the local field algebra to the covariant field
> algebra, along the inclusion; the ordinary gauge group acts on the target through the
> constant jets. No species condition beyond `hGL` is used.

```lean
noncomputable def restrict :
    LocalCovFieldAlgebra.Realization T hGL B (repJet.comp G.gaugeJetOfConstant) repLorentz
```

**`GaugeFieldData.Realization.restrict_toAlgHom_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean#L132).

```lean
lemma restrict_toAlgHom_apply (x : ↥T.LocalCovFieldAlgebra) :
    (h.restrict hGL).toAlgHom x = h.toAlgHom x
```

## Depends on

- [The covariant field algebra of a gauge theory](localfieldalgebra-localcovfieldalgebra-basic.md)
- [Realizations of the local field algebra](../part-04/localfieldalgebra-realization.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/Realization.lean)
