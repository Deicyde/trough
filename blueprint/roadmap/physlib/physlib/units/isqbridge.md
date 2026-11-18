---
declaration: module
origin: cited
lean: Dimension.toISQFun, Dimension.toISQHom, Dimension.toISQHom_apply, Dimension.fromISQFun, Dimension.fromISQHom, Dimension.fromISQHom_apply, Dimension.fromISQHom_comp_toISQHom, Dimension.toISQHom_injective
statement: formalized
proof: formalized
---

# Bridging PhysLib's default basis and the ISQ basis

The module `Physlib.Units.ISQBridge`, [Physlib/Units/ISQBridge.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean): 13 declarations, 13 with a docstring.

> `LTMCTDimensionBase` (length, time, mass, charge, temperature) and `ISQDimensionBase`
> (the seven ISO/IEC 80000-1 base quantities) make different base/derived choices. This
> module relates them by the two truth-preserving directions of `Dimension.Embedding`
> and `Dimension.Projection`:
>
> * `ltmctToISQ : Dimension.Embedding LTMCTDimensionBase ISQDimensionBase` — the
>   dimension-preserving **inclusion** of PhysLib dimensions into ISQ dimensions. It
>   sends the charge generator to the *derived* ISQ charge `I · T` (`toISQHom_C𝓭`), so it
>   is faithful (`toISQHom_injective`) and physically correct, not a bare relabelling.
> * `isqToLTMCT : Dimension.Projection ISQDimensionBase LTMCTDimensionBase` — the
>   truth-preserving **reduction** of ISQ dimensions onto PhysLib's. It reads electric
>   current as charge/time and forgets amount of substance and luminous intensity (the
>   base quantities PhysLib does not track).
>
> The two fit together as a retraction, `isqToLTMCT ∘ ltmctToISQ = id`
> (`isqToLTMCT_comp_ltmctToISQ`): PhysLib's basis embeds faithfully into ISQ and is
> recovered exactly by the projection — but the reverse composite is *not* the identity,
> because amount of substance and luminous intensity cannot be recovered once dropped.
> That is the asymmetry: one can reduce ISQ to LTMCT, but not conjure the extra base
> quantities back without *adding* them.

**`Dimension.toISQFun`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L46).

> The function underlying `toISQHom`: fix length, mass, time and temperature, and
> send PhysLib's charge generator to the derived ISQ charge `I · T` (the current
> exponent is the charge exponent, and the time exponent absorbs it).

```lean
def toISQFun (d : Dimension LTMCTDimensionBase) : Dimension ISQDimensionBase
```

**`Dimension.toISQHom`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L57).

> The dimension-preserving embedding of PhysLib dimensions into the ISQ dimensions.

```lean
def toISQHom : Dimension LTMCTDimensionBase →* Dimension ISQDimensionBase
```

**`Dimension.toISQHom_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L66).

> `toISQHom` applied to a dimension is `toISQFun`.

```lean
lemma toISQHom_apply (d : Dimension LTMCTDimensionBase) : toISQHom d = toISQFun d
```

**`Dimension.fromISQFun`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L71).

> The function underlying `fromISQHom`: fix length, mass and temperature, read
> electric current as charge/time (the charge exponent is the current exponent, and the
> time exponent subtracts it), and drop amount of substance and luminous intensity.

```lean
def fromISQFun (d : Dimension ISQDimensionBase) : Dimension LTMCTDimensionBase
```

**`Dimension.fromISQHom`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L80).

> The truth-preserving reduction of ISQ dimensions onto PhysLib's.

```lean
def fromISQHom : Dimension ISQDimensionBase →* Dimension LTMCTDimensionBase
```

**`Dimension.fromISQHom_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L89).

> `fromISQHom` applied to a dimension is `fromISQFun`.

```lean
lemma fromISQHom_apply (d : Dimension ISQDimensionBase) : fromISQHom d = fromISQFun d
```

**`Dimension.fromISQHom_comp_toISQHom`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L93).

> The projection recovers PhysLib's basis from its image under the embedding:
> `fromISQHom ∘ toISQHom = id`.

```lean
lemma fromISQHom_comp_toISQHom :
    fromISQHom.comp toISQHom = MonoidHom.id (Dimension LTMCTDimensionBase)
```

**`Dimension.toISQHom_injective`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L101).

> `toISQHom` is injective: PhysLib dimensions include faithfully into ISQ.

```lean
lemma toISQHom_injective : Function.Injective toISQHom
```

**`Dimension.fromISQHom_surjective`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L121).

> `fromISQHom` is surjective: every PhysLib dimension is the reduction of some ISQ
> dimension (namely its own embedding).

```lean
lemma fromISQHom_surjective : Function.Surjective fromISQHom
```

**`Dimension.ltmctToISQ`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L125).

> PhysLib's dimensions embed into the ISQ dimensions (charge ↦ `I · T`).

```lean
def ltmctToISQ : Embedding LTMCTDimensionBase ISQDimensionBase
```

**`Dimension.isqToLTMCT`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L131).

> The ISQ dimensions project onto PhysLib's, reading current as charge/time and
> forgetting amount of substance and luminous intensity.

```lean
def isqToLTMCT : Projection ISQDimensionBase LTMCTDimensionBase
```

**`Dimension.isqToLTMCT_comp_ltmctToISQ`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L138).

> The projection is a retraction of the embedding: `isqToLTMCT ∘ ltmctToISQ = id`. So
> PhysLib's basis embeds faithfully into ISQ and is recovered by the projection, but not
> conversely — amount of substance and luminous intensity cannot be recovered.

```lean
lemma isqToLTMCT_comp_ltmctToISQ :
    isqToLTMCT.toHom.comp ltmctToISQ.toHom = MonoidHom.id (Dimension LTMCTDimensionBase)
```

**`Dimension.toISQHom_C𝓭`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean#L144).

> The embedding is physically faithful on charge: PhysLib's charge generator `C𝓭`
> maps to the *derived* ISQ charge `I · T`.

```lean
lemma toISQHom_C𝓭 : toISQHom C𝓭 = ISQDimensionBase.charge
```

## Depends on

- [The ISQ base quantities](isqdimensionbase.md)
- [PhysLib's default dimension basis](ltmctdimensionbase.md)

## Sources

- [Physlib/Units/ISQBridge.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ISQBridge.lean)
