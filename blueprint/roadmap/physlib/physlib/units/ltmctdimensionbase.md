---
declaration: module
origin: cited
lean: LTMCTDimensionBase, LTMCTDimensionBase.Exponents, Dimension.length, Dimension.time, Dimension.mass, Dimension.charge, Dimension.temperature, Dimension.exponent_length
statement: formalized
proof: formalized
---

# PhysLib's default dimension basis

The module `Physlib.Units.LTMCTDimensionBase`, [Physlib/Units/LTMCTDimensionBase.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean): 81 declarations (2 instances with no name), 18 with a docstring; 1 private, not shown.

> `LTMCTDimensionBase` is PhysLib's default basis of base dimensions — length, time,
> mass, charge and temperature. `Dimension LTMCTDimensionBase` is the familiar
> five-exponent dimension, and this module provides the concrete API on top of the
> generic `Dimension B`:
>
> * the `.length`, `.time`, `.mass`, `.charge`, `.temperature` exponent projections;
> * the `ofLTMCTDimensionBase` constructor from five exponents; and
> * the named generators `L𝓭`, `T𝓭`, `M𝓭`, `C𝓭`, `Θ𝓭`, shown to be the generic
>   `single` base vectors.
>
> This basis is *charge*-based with five generators, so it is deliberately **not** the
> SI/ISQ base-quantity set (which takes electric current as base and adds amount of
> substance and luminous intensity); see `ISQDimensionBase`.

**`LTMCTDimensionBase`**, an inductive, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L34).

> PhysLib's default basis of base dimensions — `length`, `time`, `mass`,
> `charge`, `temperature`. Note this is *charge*-based, so it is not the SI/ISQ
> base-quantity set; see `Dimension`.

```lean
inductive LTMCTDimensionBase where
  /-- The length base dimension. -/
  | length
  /-- The time base dimension. -/
  | time
  /-- The mass base dimension. -/
  | mass
  /-- The charge base dimension. -/
  | charge
  /-- The temperature base dimension. -/
  | temperature
```

**An instance with no name**, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L49).

```lean
instance : Fintype LTMCTDimensionBase
```

**`LTMCTDimensionBase.Exponents`**, an abbrev, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L55).

> The fixed five-component exponent tuple for PhysLib's default dimension basis.

```lean
abbrev Exponents
```

**An instance with no name**, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L57).

```lean
instance : DimensionBasis LTMCTDimensionBase
```

## The LTMCTDimensionBase projections

> The five base-dimension exponents of a `Dimension LTMCTDimensionBase`, provided so that
> the familiar `.length`, `.time`, `.mass`, `.charge`, `.temperature` API is available.

**`Dimension.length`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L82).

> The length exponent of a `LTMCTDimensionBase` dimension.

```lean
def length (d : Dimension LTMCTDimensionBase) : Exponent
```

**`Dimension.time`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L84).

> The time exponent of a `LTMCTDimensionBase` dimension.

```lean
def time (d : Dimension LTMCTDimensionBase) : Exponent
```

**`Dimension.mass`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L86).

> The mass exponent of a `LTMCTDimensionBase` dimension.

```lean
def mass (d : Dimension LTMCTDimensionBase) : Exponent
```

**`Dimension.charge`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L88).

> The charge exponent of a `LTMCTDimensionBase` dimension.

```lean
def charge (d : Dimension LTMCTDimensionBase) : Exponent
```

**`Dimension.temperature`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L90).

> The temperature exponent of a `LTMCTDimensionBase` dimension.

```lean
def temperature (d : Dimension LTMCTDimensionBase) : Exponent
```

**`Dimension.exponent_length`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L93).

```lean
lemma exponent_length (d : Dimension LTMCTDimensionBase) : d.exponent .length = d.length
```

**`Dimension.exponent_time`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L96).

```lean
lemma exponent_time (d : Dimension LTMCTDimensionBase) : d.exponent .time = d.time
```

**`Dimension.exponent_mass`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L99).

```lean
lemma exponent_mass (d : Dimension LTMCTDimensionBase) : d.exponent .mass = d.mass
```

**`Dimension.exponent_charge`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L102).

```lean
lemma exponent_charge (d : Dimension LTMCTDimensionBase) : d.exponent .charge = d.charge
```

**`Dimension.exponent_temperature`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L105).

```lean
lemma exponent_temperature (d : Dimension LTMCTDimensionBase) :
    d.exponent .temperature = d.temperature
```

**`Dimension.ofLTMCTDimensionBase`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L110).

> Build a `LTMCTDimensionBase` dimension from its five exponents, in the order
> `⟨length, time, mass, charge, temperature⟩`.

```lean
def ofLTMCTDimensionBase (length time mass charge temperature : Exponent) :
    Dimension LTMCTDimensionBase
```

**`Dimension.ofLTMCTDimensionBase_length`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L115).

```lean
lemma ofLTMCTDimensionBase_length (l t m c θ : Exponent) :
    (ofLTMCTDimensionBase l t m c θ).length = l
```

**`Dimension.ofLTMCTDimensionBase_time`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L119).

```lean
lemma ofLTMCTDimensionBase_time (l t m c θ : Exponent) :
    (ofLTMCTDimensionBase l t m c θ).time = t
```

**`Dimension.ofLTMCTDimensionBase_mass`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L123).

```lean
lemma ofLTMCTDimensionBase_mass (l t m c θ : Exponent) :
    (ofLTMCTDimensionBase l t m c θ).mass = m
```

**`Dimension.ofLTMCTDimensionBase_charge`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L127).

```lean
lemma ofLTMCTDimensionBase_charge (l t m c θ : Exponent) :
    (ofLTMCTDimensionBase l t m c θ).charge = c
```

**`Dimension.ofLTMCTDimensionBase_temperature`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L131).

```lean
lemma ofLTMCTDimensionBase_temperature (l t m c θ : Exponent) :
    (ofLTMCTDimensionBase l t m c θ).temperature = θ
```

**`Dimension.time_mul`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L135).

```lean
lemma time_mul (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 * d2).time = d1.time + d2.time
```

**`Dimension.length_mul`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L139).

```lean
lemma length_mul (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 * d2).length = d1.length + d2.length
```

**`Dimension.mass_mul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L143).

```lean
lemma mass_mul (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 * d2).mass = d1.mass + d2.mass
```

**`Dimension.charge_mul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L147).

```lean
lemma charge_mul (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 * d2).charge = d1.charge + d2.charge
```

**`Dimension.temperature_mul`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L151).

```lean
lemma temperature_mul (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 * d2).temperature = d1.temperature + d2.temperature
```

**`Dimension.one_length`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L155).

```lean
lemma one_length : (1 : Dimension LTMCTDimensionBase).length = 0
```

**`Dimension.one_time`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L157).

```lean
lemma one_time : (1 : Dimension LTMCTDimensionBase).time = 0
```

**`Dimension.one_mass`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L160).

```lean
lemma one_mass : (1 : Dimension LTMCTDimensionBase).mass = 0
```

**`Dimension.one_charge`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L163).

```lean
lemma one_charge : (1 : Dimension LTMCTDimensionBase).charge = 0
```

**`Dimension.one_temperature`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L166).

```lean
lemma one_temperature : (1 : Dimension LTMCTDimensionBase).temperature = 0
```

**`Dimension.inv_length`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L169).

```lean
lemma inv_length (d : Dimension LTMCTDimensionBase) : d⁻¹.length = -d.length
```

**`Dimension.inv_time`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L172).

```lean
lemma inv_time (d : Dimension LTMCTDimensionBase) : d⁻¹.time = -d.time
```

**`Dimension.inv_mass`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L175).

```lean
lemma inv_mass (d : Dimension LTMCTDimensionBase) : d⁻¹.mass = -d.mass
```

**`Dimension.inv_charge`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L178).

```lean
lemma inv_charge (d : Dimension LTMCTDimensionBase) : d⁻¹.charge = -d.charge
```

**`Dimension.inv_temperature`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L181).

```lean
lemma inv_temperature (d : Dimension LTMCTDimensionBase) : d⁻¹.temperature = -d.temperature
```

**`Dimension.component_epow`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L192).

```lean
lemma component_epow (component : Dimension LTMCTDimensionBase → Exponent)
    (b : LTMCTDimensionBase) (h : ∀ d, d.exponent b = component d)
    (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    component (d ^ c) = component d * c
```

**`Dimension.div_length`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L202).

```lean
lemma div_length (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 / d2).length = d1.length - d2.length
```

**`Dimension.div_time`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L206).

```lean
lemma div_time (d1 d2 : Dimension LTMCTDimensionBase) : (d1 / d2).time = d1.time - d2.time
```

**`Dimension.div_mass`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L209).

```lean
lemma div_mass (d1 d2 : Dimension LTMCTDimensionBase) : (d1 / d2).mass = d1.mass - d2.mass
```

**`Dimension.div_charge`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L212).

```lean
lemma div_charge (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 / d2).charge = d1.charge - d2.charge
```

**`Dimension.div_temperature`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L216).

```lean
lemma div_temperature (d1 d2 : Dimension LTMCTDimensionBase) :
    (d1 / d2).temperature = d1.temperature - d2.temperature
```

**`Dimension.npow_length`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L220).

```lean
lemma npow_length (d : Dimension LTMCTDimensionBase) (n : ℕ) : (d ^ n).length = n • d.length
```

**`Dimension.npow_time`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L224).

```lean
lemma npow_time (d : Dimension LTMCTDimensionBase) (n : ℕ) : (d ^ n).time = n • d.time
```

**`Dimension.npow_mass`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L228).

```lean
lemma npow_mass (d : Dimension LTMCTDimensionBase) (n : ℕ) : (d ^ n).mass = n • d.mass
```

**`Dimension.npow_charge`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L232).

```lean
lemma npow_charge (d : Dimension LTMCTDimensionBase) (n : ℕ) : (d ^ n).charge = n • d.charge
```

**`Dimension.npow_temperature`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L236).

```lean
lemma npow_temperature (d : Dimension LTMCTDimensionBase) (n : ℕ) :
    (d ^ n).temperature = n • d.temperature
```

**`Dimension.epow_length`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L244).

> The length component of an `Exponent` power. Since `Pow (Dimension B) Exponent` is the
> default instance, an unascribed numeric exponent elaborates to this power rather than to
> the `ℕ` one, so `npow_length` does not apply to it and this lemma is what `simp` needs.

```lean
lemma epow_length (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    (d ^ c).length = d.length * c
```

**`Dimension.epow_time`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L250).

> The time component of an `Exponent` power.

```lean
lemma epow_time (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    (d ^ c).time = d.time * c
```

**`Dimension.epow_mass`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L256).

> The mass component of an `Exponent` power.

```lean
lemma epow_mass (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    (d ^ c).mass = d.mass * c
```

**`Dimension.epow_charge`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L262).

> The charge component of an `Exponent` power.

```lean
lemma epow_charge (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    (d ^ c).charge = d.charge * c
```

**`Dimension.epow_temperature`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L268).

> The temperature component of an `Exponent` power.

```lean
lemma epow_temperature (d : Dimension LTMCTDimensionBase) (c : Exponent) :
    (d ^ c).temperature = d.temperature * c
```

**`Dimension.L𝓭`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L273).

> The dimension corresponding to length.

```lean
def L𝓭 : Dimension LTMCTDimensionBase
```

**`Dimension.L𝓭_length`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L276).

```lean
lemma L𝓭_length : L𝓭.length = 1
```

**`Dimension.L𝓭_time`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L279).

```lean
lemma L𝓭_time : L𝓭.time = 0
```

**`Dimension.L𝓭_mass`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L282).

```lean
lemma L𝓭_mass : L𝓭.mass = 0
```

**`Dimension.L𝓭_charge`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L285).

```lean
lemma L𝓭_charge : L𝓭.charge = 0
```

**`Dimension.L𝓭_temperature`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L288).

```lean
lemma L𝓭_temperature : L𝓭.temperature = 0
```

**`Dimension.T𝓭`**, a def, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L291).

> The dimension corresponding to time.

```lean
def T𝓭 : Dimension LTMCTDimensionBase
```

**`Dimension.T𝓭_length`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L294).

```lean
lemma T𝓭_length : T𝓭.length = 0
```

**`Dimension.T𝓭_time`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L297).

```lean
lemma T𝓭_time : T𝓭.time = 1
```

**`Dimension.T𝓭_mass`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L300).

```lean
lemma T𝓭_mass : T𝓭.mass = 0
```

**`Dimension.T𝓭_charge`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L303).

```lean
lemma T𝓭_charge : T𝓭.charge = 0
```

**`Dimension.T𝓭_temperature`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L306).

```lean
lemma T𝓭_temperature : T𝓭.temperature = 0
```

**`Dimension.M𝓭`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L309).

> The dimension corresponding to mass.

```lean
def M𝓭 : Dimension LTMCTDimensionBase
```

**`Dimension.M𝓭_length`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L312).

```lean
lemma M𝓭_length : M𝓭.length = 0
```

**`Dimension.M𝓭_time`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L315).

```lean
lemma M𝓭_time : M𝓭.time = 0
```

**`Dimension.M𝓭_mass`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L318).

```lean
lemma M𝓭_mass : M𝓭.mass = 1
```

**`Dimension.M𝓭_charge`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L321).

```lean
lemma M𝓭_charge : M𝓭.charge = 0
```

**`Dimension.M𝓭_temperature`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L324).

```lean
lemma M𝓭_temperature : M𝓭.temperature = 0
```

**`Dimension.C𝓭`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L327).

> The dimension corresponding to charge.

```lean
def C𝓭 : Dimension LTMCTDimensionBase
```

**`Dimension.Θ𝓭`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L330).

> The dimension corresponding to temperature.

```lean
def Θ𝓭 : Dimension LTMCTDimensionBase
```

**`Dimension.Θ𝓭_length`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L333).

```lean
lemma Θ𝓭_length : Θ𝓭.length = 0
```

**`Dimension.Θ𝓭_time`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L336).

```lean
lemma Θ𝓭_time : Θ𝓭.time = 0
```

**`Dimension.Θ𝓭_mass`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L339).

```lean
lemma Θ𝓭_mass : Θ𝓭.mass = 0
```

**`Dimension.Θ𝓭_charge`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L342).

```lean
lemma Θ𝓭_charge : Θ𝓭.charge = 0
```

**`Dimension.Θ𝓭_temperature`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L345).

```lean
lemma Θ𝓭_temperature : Θ𝓭.temperature = 1
```

## The named generators are the base vectors

> Each named generator `L𝓭`, `T𝓭`, … is the generic `single` base vector at the
> corresponding base dimension, exhibiting them as instances of the basis-generic API.

**`Dimension.L𝓭_eq_single`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L356).

```lean
lemma L𝓭_eq_single : L𝓭 = single .length
```

**`Dimension.T𝓭_eq_single`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L358).

```lean
lemma T𝓭_eq_single : T𝓭 = single .time
```

**`Dimension.M𝓭_eq_single`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L360).

```lean
lemma M𝓭_eq_single : M𝓭 = single .mass
```

**`Dimension.C𝓭_eq_single`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L362).

```lean
lemma C𝓭_eq_single : C𝓭 = single .charge
```

**`Dimension.Θ𝓭_eq_single`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean#L364).

```lean
lemma Θ𝓭_eq_single : Θ𝓭 = single .temperature
```

## Depends on

- [Dimension](dimension.md)

## Sources

- [Physlib/Units/LTMCTDimensionBase.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/LTMCTDimensionBase.lean)
