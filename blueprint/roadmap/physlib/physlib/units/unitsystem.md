---
declaration: module
origin: cited
lean: UnitSystem.ext, UnitMagnitudeCatalog, UnitSystem, UnitSystem.toScale, UnitSystem.toScale_scale, LTMCTUnitChoices.equivUnitSystem, LTMCTUnitChoices.toScale_equivUnitSystem, prod_univ_LTMCTDimensionBase
statement: formalized
proof: formalized
---

# Unit systems, parametrised in a dimension basis

The module `Physlib.Units.UnitSystem`, [Physlib/Units/UnitSystem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean): 10 declarations (1 instance with no name), 8 with a docstring, 1 listed as significant; 5 private, not shown.

> A **unit system** is the everyday physics object: a rule fixing one concrete unit for
> each base quantity. SI fixes the metre for length, the second for time, the kilogram for
> mass, …; CGS fixes the centimetre, second and gram. Choosing a system gives every quantity
> a numerical value; changing systems rescales those values.
>
> This module makes that notion work for *any* dimension basis `B` (matching the
> basis-generic `Dimension B`), while keeping units *typed*: the unit in the length slot has
> type `LengthUnit`, the one in the time slot `TimeUnit`, so the checker rejects a mass unit
> in a length slot.
>
> * `UnitMagnitudeCatalog B` — the **menu** for basis `B`. For each base dimension `b : B` it
>   gives a *type* `Unit b` of admissible units — so a dimension may offer many (length: metre,
>   kilometre, micrometre, …) — and a *function* `mag` assigning each unit its one positive-real
>   magnitude. The menu lists the options and picks none; many unit systems share one catalog.
> * `UnitSystem B` — the **pick**: a function choosing *exactly one* unit per base dimension. A
>   single unit system therefore fixes one length unit — metre *or* kilometre, never both — so
>   metre and kilometre are two menu entries selected by two different `UnitSystem`s over the
>   same catalog. SI and CGS are two such picks.
> * `UnitSystem.toScale : UnitSystem B → UnitScale B` — forget the unit *types*, keep only
>   the magnitudes, landing in the bare magnitude layer `UnitScale B` where the scaling
>   homomorphism `UnitScale.dimScale` is proved once.
>
> **Menu vs. pick.** The catalog is a menu, not a choice: it says which units exist and what
> each weighs, but selects none — a `UnitSystem` makes the selection. And in PhysLib a base
> unit *is* a positive real (`{ val : ℝ // 0 < val }`), i.e. its own magnitude, so the
> magnitude comes fixed with the unit; there is no separate "assign a magnitude" step. Hence
> metre, micrometre and kilometre are three *different* units on the one length menu, and
> "SI in metres" versus "the same in micrometres" are two different `UnitSystem`s over the
> **same** catalog — related by `UnitScale.dimScale`, which computes the 10⁶ factor between
> them. (The multiplicity one might expect from "many magnitudes" lives here, among the unit
> systems, not in many catalogs.)
>
> The `LTMCTDimensionBase` catalog recovers PhysLib's five named unit types, and
> `LTMCTUnitChoices ≃ UnitSystem LTMCTDimensionBase` exhibits the bespoke five-field record
> as that instance. Scaling laws are **not** re-proved here — they live once on `UnitScale B`,
> and the typed layer is a thin faithful wrapper projecting onto it via `toScale`.
>
> This is the typed, basis-generic layer discussed as "Option D" in the review of the
> dimension-parametrisation PR; it is the only design that keeps *both* basis-genericity and
> typed-unit safety.

**`UnitMagnitudeCatalog`**, a class, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L66).

> A **menu of typed units** for a basis `B`: for each base dimension `b : B`, a *type*
> `Unit b` of admissible units (a dimension may offer several — metre, kilometre, …) and a
> *function* `mag` giving each its single positive-real magnitude. It lists the options and
> picks none — a `UnitSystem` makes the pick. One catalog underlies many unit systems (SI,
> CGS, …); the magnitude is the data `toScale` reads to drive rescaling.

```lean
class UnitMagnitudeCatalog (B : Type) where
  /-- The typed unit type at each base dimension. -/
  Unit : B → Type
  /-- The positive-real magnitude of a typed unit. -/
  mag : {b : B} → Unit b → ℝ≥0
  /-- Every typed unit has a positive magnitude. -/
  mag_pos : ∀ {b : B} (u : Unit b), 0 < mag u
```

**`UnitSystem`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L78).

> A **unit system** over a basis `B` with a `UnitMagnitudeCatalog`: one typed unit chosen
> per base dimension — the pick off the catalog's menu, and the formal counterpart of SI,
> CGS, …. Over the default basis, `u .length : LengthUnit`, and a `MassUnit` cannot be
> placed in the length slot.

```lean
def UnitSystem (B : Type) [UnitMagnitudeCatalog B]
```

**`UnitSystem.ext`**, a theorem, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L87). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two unit systems agree once they pick the same unit at every base dimension: `UnitSystem`
> is extensional, as befits a choice-per-dimension.

```lean
theorem ext {u v : UnitSystem B} (h : ∀ b, u b = v b) : u = v
```

**`UnitSystem.toScale`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L91).

> Forget a unit system to its magnitude layer `UnitScale B`: keep each chosen unit's
> magnitude, drop its type — the layer where `UnitScale.dimScale` is already proved.

```lean
noncomputable def toScale (u : UnitSystem B) : UnitScale B
```

**`UnitSystem.toScale_scale`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L96).

```lean
lemma toScale_scale (u : UnitSystem B) (b : B) :
    (toScale u).scale b = UnitMagnitudeCatalog.mag (u b)
```

## The `LTMCTDimensionBase` catalog

> The default basis's `UnitMagnitudeCatalog` recovers exactly PhysLib's five named typed unit
> types, so `UnitSystem LTMCTDimensionBase` is the typed five-slot unit system and
> `u .length : LengthUnit`, `LengthUnit.meters`, … all still work — and a `MassUnit` cannot
> be placed in the length slot.

**An instance with no name**, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L112).

```lean
noncomputable instance : UnitMagnitudeCatalog LTMCTDimensionBase
```

## `LTMCTUnitChoices` is `UnitSystem LTMCTDimensionBase`

> The bespoke five-field record and the generic unit system over the default basis carry
> the same data.

**`LTMCTUnitChoices.equivUnitSystem`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L150).

> The bespoke five-field `LTMCTUnitChoices` and the generic `UnitSystem LTMCTDimensionBase`
> are the same data.

```lean
def equivUnitSystem : LTMCTUnitChoices ≃ UnitSystem LTMCTDimensionBase
```

**`LTMCTUnitChoices.toScale_equivUnitSystem`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L169).

> The typed generic projection agrees with the bespoke `LTMCTUnitChoices.toScale`: reading
> `LTMCTUnitChoices` as a `UnitSystem` and forgetting to the magnitude layer is the same as
> the bespoke `toScale`.

```lean
lemma toScale_equivUnitSystem (u : LTMCTUnitChoices) :
    (equivUnitSystem u).toScale = u.toScale
```

## The bespoke scaling law is the generic fold

> `LTMCTUnitChoices.dimScale` — the five explicit `rpow` factors written out by hand in
> `Basic.lean` — is exactly the generic `UnitScale.dimScale` fold (a `Finset.prod` over the
> basis) at the `LTMCTDimensionBase` instance, applied to `toScale`. This is what makes the
> typed layer a *faithful* wrapper rather than a second, independent statement of the
> scaling law: there is one source of truth, the generic fold on `UnitScale B`.

**`prod_univ_LTMCTDimensionBase`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L193).

> The product over the five default base quantities, in canonical enumeration order — a
> reusable fact about the `Fintype` enumeration of `LTMCTDimensionBase`, for folding
> `Finset.prod` over the default basis (e.g. in a hand-rolled scaling law).

```lean
lemma prod_univ_LTMCTDimensionBase {M : Type} [CommMonoid M]
    (f : LTMCTDimensionBase → M) :
    ∏ b, f b = f .length * f .time * f .mass * f .charge * f .temperature
```

**`LTMCTUnitChoices.dimScale_eq_toScale_dimScale`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean#L227).

> The hand-rolled five-factor `LTMCTUnitChoices.dimScale` equals the basis-generic
> `UnitScale.dimScale` fold at `LTMCTDimensionBase`, applied to `toScale`. The scaling law
> therefore has a single source of truth on the magnitude layer `UnitScale B`.

```lean
lemma dimScale_eq_toScale_dimScale (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    u1.dimScale u2 d = UnitScale.dimScale u1.toScale u2.toScale d
```

## Depends on

- [The unit side, parametrised in the same basis](parametricunits.md)

## Sources

- [Physlib/Units/UnitSystem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitSystem.lean)
