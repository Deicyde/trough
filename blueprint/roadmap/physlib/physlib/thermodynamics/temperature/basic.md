---
declaration: module
origin: cited
lean: Temperature, Temperature.toReal, Temperature.ext, Temperature.β, Temperature.β_toReal, Temperature.ofβ, Temperature.ofβ_eq, Temperature.β_ofβ
statement: formalized
proof: formalized
---

# Temperature

The module `Physlib.Thermodynamics.Temperature.Basic`, [Physlib/Thermodynamics/Temperature/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean): 31 declarations (4 instances with no name), 17 with a docstring; 1 private, not shown.

> In this module we define the type `Temperature`, corresponding to the temperature in a given
> (but arbitrary) set of units which have absolute zero at zero.
>
> This is the version of temperature most often used in undergraduate and
> non-mathematical physics.
>
> The choice of units can be made on a case-by-case basis, as long as they are done consistently.

**`Temperature`**, a structure, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L32).

> The type `Temperature` represents the temperature in a given (but arbitrary) set of units
> (preserving zero). It currently wraps `ℝ≥0`, i.e., absolute temperature in nonnegative reals.

```lean
structure Temperature where
  /-- The nonnegative real value of the temperature. -/
  val : ℝ≥0
```

**An instance with no name**, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L41).

> Coercion to `ℝ≥0`.

```lean
instance : Coe Temperature ℝ≥0
```

**`Temperature.toReal`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L44).

> The underlying real-number associated with the temperature.

```lean
noncomputable def toReal (T : Temperature) : ℝ
```

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L47).

> Coercion to `ℝ`.

```lean
noncomputable instance : Coe Temperature ℝ
```

**An instance with no name**, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L50).

> Topology on `Temperature` induced from `ℝ≥0`.

```lean
instance : TopologicalSpace Temperature
```

**An instance with no name**, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L53).

```lean
instance : Zero Temperature
```

**`Temperature.ext`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L55).

```lean
lemma ext {T₁ T₂ : Temperature} (h : T₁.val = T₂.val) : T₁ = T₂
```

**`Temperature.β`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L60).

> The inverse temperature defined as `1/(kB * T)` in a given, but arbitrary set of units.
> This has the dimension of an inverse energy.

```lean
noncomputable def β (T : Temperature) : ℝ≥0
```

**`Temperature.β_toReal`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L63).

```lean
lemma β_toReal (T : Temperature) : (β kB T : ℝ) = 1 / ((kB : ℝ) * (T : ℝ))
```

**`Temperature.ofβ`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L66).

> The temperature associated with a given inverse temperature `β`.

```lean
noncomputable def ofβ (β : ℝ≥0) : Temperature
```

**`Temperature.ofβ_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L69).

```lean
lemma ofβ_eq : ofβ kB = fun β => ⟨⟨1 / ((kB : ℝ) * β), by
    apply div_nonneg
    · exact zero_le_one
    · apply mul_nonneg
      · exact kB.val_nonneg
      · exact β.2⟩⟩
```

**`Temperature.β_ofβ`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L78).

```lean
lemma β_ofβ (β' : ℝ≥0) : β kB (ofβ kB β') = β'
```

**`Temperature.ofβ_toReal`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L83).

```lean
lemma ofβ_toReal (β : ℝ≥0) : (ofβ kB β).toReal = 1 / ((kB : ℝ) * (β : ℝ))
```

**`Temperature.ofβ_β`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L86).

```lean
lemma ofβ_β (T : Temperature) : ofβ kB (β kB T) = T
```

**`Temperature.beta_pos`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L93).

> Positivity of `β` from positivity of temperature.

```lean
lemma beta_pos (T : Temperature) (hT_pos : 0 < T.val) : 0 < (T.β kB : ℝ)
```

### Regularity of `ofβ`

**`Temperature.ofβ_continuousOn`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L101).

```lean
lemma ofβ_continuousOn : ContinuousOn (ofβ kB : ℝ≥0 → Temperature) (Set.Ioi 0)
```

**`Temperature.ofβ_differentiableOn`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L112).

```lean
lemma ofβ_differentiableOn :
    DifferentiableOn ℝ (fun (x : ℝ) => ((ofβ kB (Real.toNNReal x)).val : ℝ)) (Set.Ioi 0)
```

### Convergence

**`Temperature.eventually_pos_ofβ`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L129).

> Eventually, `ofβ β` is positive as β → ∞`.

```lean
lemma eventually_pos_ofβ :
    ∀ᶠ b : ℝ≥0 in atTop, ((Temperature.ofβ kB b : Temperature) : ℝ) > 0
```

**`Temperature.tendsto_toReal_ofβ_atTop`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L145).

> Core convergence: as β → ∞, `toReal (ofβ β) → 0` in `ℝ`.

```lean
lemma tendsto_toReal_ofβ_atTop :
    Tendsto (fun b : ℝ≥0 => (Temperature.ofβ kB b : ℝ))
      atTop (𝓝 (0 : ℝ))
```

**`Temperature.tendsto_ofβ_atTop`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L151).

> As β → ∞, T = ofβ β → 0+ in ℝ (within Ioi 0).

```lean
lemma tendsto_ofβ_atTop :
    Tendsto (fun b : ℝ≥0 => (Temperature.ofβ kB b : ℝ))
      atTop (nhdsWithin 0 (Set.Ioi 0))
```

### Conversion to and from `ℝ≥0`

**`Temperature.ofNNReal`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L160).

> Build a `Temperature` directly from a nonnegative real.

```lean
def ofNNReal (t : ℝ≥0) : Temperature
```

**`Temperature.ofNNReal_val`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L163).

```lean
lemma ofNNReal_val (t : ℝ≥0) : (ofNNReal t).val = t
```

**`Temperature.coe_ofNNReal_coe`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L166).

```lean
lemma coe_ofNNReal_coe (t : ℝ≥0) : ((ofNNReal t : Temperature) : ℝ≥0) = t
```

**`Temperature.coe_ofNNReal_real`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L169).

```lean
lemma coe_ofNNReal_real (t : ℝ≥0) : ((⟨t⟩ : Temperature) : ℝ) = t
```

**`Temperature.ofRealNonneg`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L173).

> Convenience: build a temperature from a real together with a proof of nonnegativity.

```lean
noncomputable def ofRealNonneg (t : ℝ) (ht : 0 ≤ t) : Temperature
```

**`Temperature.ofRealNonneg_val`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L177).

```lean
lemma ofRealNonneg_val {t : ℝ} (ht : 0 ≤ t) :
    (ofRealNonneg t ht).val = ⟨t, ht⟩
```

### Calculus relating T and β

**`Temperature.betaFromReal`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L187).

> Map a real `t` to the inverse temperature `β` corresponding to the temperature `Real.toNNReal t`
> (`max t 0`), returned as a real number.

```lean
noncomputable def betaFromReal (t : ℝ) : ℝ
```

**`Temperature.beta_fun_T_formula`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L191).

> Explicit closed-form for `Beta_fun_T t` when `t > 0`.

```lean
lemma beta_fun_T_formula (t : ℝ) (ht : 0 < t) :
    betaFromReal kB t = 1 / ((kB : ℝ) * t)
```

**`Temperature.beta_fun_T_eq_on_Ioi`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L196).

> On `Ioi 0`, `Beta_fun_T t` equals `1 / (kB * t)`.

```lean
lemma beta_fun_T_eq_on_Ioi :
    EqOn (betaFromReal kB) (fun t : ℝ => 1 / ((kB : ℝ) * t)) (Set.Ioi 0)
```

**`Temperature.deriv_beta_wrt_T`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L201).

```lean
lemma deriv_beta_wrt_T (T : Temperature) (hT_pos : 0 < T.val) :
    HasDerivWithinAt (betaFromReal kB) (-1 / ((kB : ℝ) * (T.val : ℝ)^2)) (Set.Ioi 0)
      (T.val : ℝ)
```

**`Temperature.chain_rule_T_beta`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean#L221).

> Chain rule for β(T) : d/dT F(β(T)) = F'(β(T)) * (-1 / (kB * T^2)), within `Ioi 0`.

```lean
lemma chain_rule_T_beta {F : ℝ → ℝ} {F' : ℝ}
    (T : Temperature) (hT_pos : 0 < T.val)
    (hF_deriv : HasDerivWithinAt F F' (Set.Ioi 0) (T.β kB : ℝ)) :
    HasDerivWithinAt (fun t : ℝ => F (betaFromReal kB t))
      (F' * (-1 / ((kB : ℝ) * (T.val : ℝ)^2))) (Set.Ioi 0) (T.val : ℝ)
```

## Depends on

- [Boltzmann constant](../../statisticalmechanics/boltzmannconstant.md)

## Sources

- [Physlib/Thermodynamics/Temperature/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/Temperature/Basic.lean)
