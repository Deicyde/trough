---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.hasDerivAt_eval_mul_exp, PhyslibAlpha.Hydrogen.deriv_eval_mul_exp, PhyslibAlpha.Hydrogen.radialPoly, PhyslibAlpha.Hydrogen.radialU, PhyslibAlpha.Hydrogen.eval_radialPoly, PhyslibAlpha.Hydrogen.eval_derivative_radialPoly, PhyslibAlpha.Hydrogen.eval_derivative_derivative_radialPoly, PhyslibAlpha.Hydrogen.radialPoly_identity
statement: formalized
proof: formalized
---

# The radial functions of the hydrogen atom

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.RadialFunctions`, [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean): 29 declarations, 15 with a docstring.

> The bound-state radial functions of the three-dimensional hydrogen atom, the radial
> Schrödinger equation they solve, and the expectation values `⟨1/r⟩`, `⟨1/r²⟩`, `⟨1/r³⟩` and
> `|R(0)|²` that enter the fine structure.

## i. Overview

> In units of the Bohr radius, with principal quantum number `ν` and `l < ν`,
>
> `u_{νl}(ρ) = ρ^(l+1) e^(-ρ/ν) L_{ν-l-1}^(2l+1)(2ρ/ν)`.
>
> Writing `u = Q e^(-ρ/ν)` with the polynomial `Q`, the radial equation
> `u'' = (l(l+1)/ρ² - 2/ρ + 1/ν²) u` becomes a polynomial identity that follows from the Laguerre
> equation at `x = 2ρ/ν` together with `(ν - l - 1) + l + 1 = ν` (`radialU_ode`). In physical units
> this is the radial Schrödinger equation with eigenvalue `-Ry/ν²`, which is physlib's Bohr level
> `HydrogenAtom.energyLevel (ν - 1)` for `d = 3` (`radialFun_schrodinger`).
>
> The substitution `x = 2ρ/ν` turns the moments `∫ u² ρ^(-k) dρ` into the Laguerre integrals of
> `Laguerre.lean`, which gives
>
> - `⟨1/ρ⟩ = 1/ν²`,
> - `⟨1/ρ²⟩ = 1/(ν³ (l + 1/2))`,
> - `⟨1/ρ³⟩ = 1/(ν³ l (l + 1/2)(l + 1))` for `l ≥ 1`,
> - `|R_{ν0}(0)|²/‖u‖² = 4/ν³`.
>
> The functions are not normalised; all expectation values are quotients by `‖u‖²`. The
> separation of the three-dimensional Schrödinger equation into spherical harmonics is not part of
> this module.

## ii. Key results

> - `radialU`, `radialR`: the radial functions `u_{νl}` and `R_{νl} = u_{νl}/ρ`.
> - `radialU_ode`: the radial equation in atomic units.
> - `radialFun_schrodinger`: the radial Schrödinger equation in physical units.
> - `radialMoment_zero`: `‖u_{νl}‖² = (ν/2)^(2l+3) (ν + l)!/(ν - l - 1)! · 2ν`.
> - `radialMean_one`, `radialMean_two`, `radialMean_three`: the expectation values.
> - `radialR_zero_sq_div`: the density at the origin for `s` states.

## iv. References

> - H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*, Springer
>   (1957).
> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.7.

## A. Polynomial times exponential

**`PhyslibAlpha.Hydrogen.hasDerivAt_eval_mul_exp`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L79).

```lean
lemma hasDerivAt_eval_mul_exp (Q : ℝ[X]) (β ρ : ℝ) :
    HasDerivAt (fun ρ => Q.eval ρ * Real.exp (-(β * ρ)))
      ((derivative Q - C β * Q).eval ρ * Real.exp (-(β * ρ))) ρ
```

**`PhyslibAlpha.Hydrogen.deriv_eval_mul_exp`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L88).

```lean
lemma deriv_eval_mul_exp (Q : ℝ[X]) (β : ℝ) :
    deriv (fun ρ => Q.eval ρ * Real.exp (-(β * ρ))) =
      fun ρ => (derivative Q - C β * Q).eval ρ * Real.exp (-(β * ρ))
```

## B. The radial functions and the radial equation

**`PhyslibAlpha.Hydrogen.radialPoly`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L102).

> The polynomial `ρ^(l+1) L_{ν-l-1}^(2l+1)(2ρ/ν)`.

```lean
def radialPoly : ℝ[X]
```

**`PhyslibAlpha.Hydrogen.radialU`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L108).

> The reduced radial function `u_{νl}(ρ) = ρ^(l+1) e^(-ρ/ν) L_{ν-l-1}^(2l+1)(2ρ/ν)` of the
> hydrogen atom, in units of the Bohr radius and not normalised; `ν` is the principal quantum
> number. The radial wave function is `R_{νl}(ρ) = u_{νl}(ρ)/ρ`.

```lean
def radialU (ρ : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.eval_radialPoly`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L112).

```lean
lemma eval_radialPoly (ρ : ℝ) :
    (radialPoly ν l).eval ρ =
      ρ ^ (l + 1) * (laguerre (ν - l - 1) (2 * l + 1)).eval (2 / (ν : ℝ) * ρ)
```

**`PhyslibAlpha.Hydrogen.eval_derivative_radialPoly`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L117).

```lean
lemma eval_derivative_radialPoly (ρ : ℝ) :
    (derivative (radialPoly ν l)).eval ρ =
      ((l : ℝ) + 1) * ρ ^ l * (laguerre (ν - l - 1) (2 * l + 1)).eval (2 / (ν : ℝ) * ρ) +
        2 / (ν : ℝ) * ρ ^ (l + 1) *
          (derivative (laguerre (ν - l - 1) (2 * l + 1))).eval (2 / (ν : ℝ) * ρ)
```

**`PhyslibAlpha.Hydrogen.eval_derivative_derivative_radialPoly`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L125).

```lean
lemma eval_derivative_derivative_radialPoly (ρ : ℝ) :
    (derivative (derivative (radialPoly ν l))).eval ρ =
      ((l : ℝ) + 1) * l * ρ ^ (l - 1) *
          (laguerre (ν - l - 1) (2 * l + 1)).eval (2 / (ν : ℝ) * ρ) +
        2 * ((l : ℝ) + 1) * (2 / (ν : ℝ)) * ρ ^ l *
          (derivative (laguerre (ν - l - 1) (2 * l + 1))).eval (2 / (ν : ℝ) * ρ) +
        (2 / (ν : ℝ)) ^ 2 * ρ ^ (l + 1) *
          (derivative (derivative (laguerre (ν - l - 1) (2 * l + 1)))).eval
            (2 / (ν : ℝ) * ρ)
```

**`PhyslibAlpha.Hydrogen.radialPoly_identity`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L139).

> The polynomial identity behind the radial equation:
> `ρ² (Q'' - 2Q'/ν + Q/ν²) = (l(l+1) - 2ρ + ρ²/ν²) Q` for `Q = radialPoly ν l`.

```lean
lemma radialPoly_identity (hl : l < ν) (ρ : ℝ) :
    ρ ^ 2 * ((derivative (derivative (radialPoly ν l))).eval ρ -
        2 * (1 / (ν : ℝ)) * (derivative (radialPoly ν l)).eval ρ +
          (1 / (ν : ℝ)) ^ 2 * (radialPoly ν l).eval ρ) =
      ((l : ℝ) * (l + 1) - 2 * ρ + (1 / (ν : ℝ)) ^ 2 * ρ ^ 2) * (radialPoly ν l).eval ρ
```

**`PhyslibAlpha.Hydrogen.deriv_deriv_radialU`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L165).

```lean
lemma deriv_deriv_radialU (ρ : ℝ) :
    deriv (deriv (radialU ν l)) ρ =
      ((derivative (derivative (radialPoly ν l))).eval ρ -
        2 * (1 / (ν : ℝ)) * (derivative (radialPoly ν l)).eval ρ +
          (1 / (ν : ℝ)) ^ 2 * (radialPoly ν l).eval ρ) * Real.exp (-(1 / (ν : ℝ) * ρ))
```

**`PhyslibAlpha.Hydrogen.radialU_ode`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L179).

> **The radial Schrödinger equation of hydrogen.** In units of the Bohr radius and the
> Rydberg energy, `u_{νl}'' = (l(l+1)/ρ² - 2/ρ + 1/ν²) u_{νl}`, i.e. `u_{νl}` is an eigenfunction
> of `-d²/dρ² + l(l+1)/ρ² - 2/ρ` with eigenvalue `-1/ν²`.

```lean
lemma radialU_ode (hl : l < ν) {ρ : ℝ} (hρ : ρ ≠ 0) :
    deriv (deriv (radialU ν l)) ρ =
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + 1 / (ν : ℝ) ^ 2) * radialU ν l ρ
```

## C. Radial moments and expectation values

**`PhyslibAlpha.Hydrogen.integral_pow_mul_exp_mul_laguerre_sq_comp`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L193).

```lean
lemma integral_pow_mul_exp_mul_laguerre_sq_comp (e N α : ℕ) {b : ℝ} (hb : 0 < b) :
    ∫ ρ in Ioi (0 : ℝ), ρ ^ e * Real.exp (-(b * ρ)) * ((laguerre N α).eval (b * ρ)) ^ 2 =
      b⁻¹ * (b⁻¹ ^ e *
        ∫ x in Ioi (0 : ℝ), x ^ e * Real.exp (-x) * ((laguerre N α).eval x) ^ 2)
```

**`PhyslibAlpha.Hydrogen.radialU_sq_div_pow`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L208).

```lean
lemma radialU_sq_div_pow {k : ℕ} (hk : k ≤ 2 * l + 2) {ρ : ℝ} (hρ : 0 < ρ) :
    radialU ν l ρ ^ 2 / ρ ^ k = ρ ^ (2 * l + 2 - k) * Real.exp (-(2 / (ν : ℝ) * ρ)) *
      ((laguerre (ν - l - 1) (2 * l + 1)).eval (2 / (ν : ℝ) * ρ)) ^ 2
```

**`PhyslibAlpha.Hydrogen.radialMoment`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L221).

> The radial moment `∫₀^∞ u_{νl}(ρ)² ρ^(-k) dρ`. For `k = 0` this is the squared norm.

```lean
def radialMoment (ν l k : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialMean`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L224).

> The expectation value `⟨ρ^(-k)⟩` in the state `u_{νl}`.

```lean
def radialMean (ν l k : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialMoment_eq`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L226).

```lean
lemma radialMoment_eq (hl : l < ν) {k : ℕ} (hk : k ≤ 2 * l + 2) :
    radialMoment ν l k = ((ν : ℝ) / 2) * (((ν : ℝ) / 2) ^ (2 * l + 2 - k) *
      ∫ x in Ioi (0 : ℝ), x ^ (2 * l + 2 - k) * Real.exp (-x) *
        ((laguerre (ν - l - 1) (2 * l + 1)).eval x) ^ 2)
```

**`PhyslibAlpha.Hydrogen.radialMoment_zero`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L237).

> The squared norm `∫ u_{νl}² dρ = (ν/2)^(2l+3) (ν+l)!/(ν-l-1)! · 2ν`.

```lean
lemma radialMoment_zero (hl : l < ν) :
    radialMoment ν l 0 = ((ν : ℝ) / 2) ^ (2 * l + 3) *
      (((ν + l).factorial : ℝ) / (ν - l - 1).factorial * (2 * ν))
```

**`PhyslibAlpha.Hydrogen.radialMoment_one`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L247).

```lean
lemma radialMoment_one (hl : l < ν) :
    radialMoment ν l 1 = ((ν : ℝ) / 2) ^ (2 * l + 2) *
      (((ν + l).factorial : ℝ) / (ν - l - 1).factorial)
```

**`PhyslibAlpha.Hydrogen.radialMoment_two`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L254).

```lean
lemma radialMoment_two (hl : l < ν) :
    radialMoment ν l 2 = ((ν : ℝ) / 2) ^ (2 * l + 1) *
      (((ν + l).factorial : ℝ) / ((ν - l - 1).factorial * (2 * l + 1)))
```

**`PhyslibAlpha.Hydrogen.radialMoment_three`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L263).

```lean
lemma radialMoment_three (hl : l < ν) (hl1 : 1 ≤ l) :
    radialMoment ν l 3 = ((ν : ℝ) / 2) ^ (2 * l) *
      (((ν + l).factorial : ℝ) * (2 * ν) /
        ((ν - l - 1).factorial * (2 * l * (2 * l + 1) * (2 * l + 2))))
```

**`PhyslibAlpha.Hydrogen.radialMean_one`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L277).

> `⟨1/ρ⟩ = 1/ν²`, the virial theorem for hydrogen.

```lean
lemma radialMean_one (hl : l < ν) : radialMean ν l 1 = 1 / (ν : ℝ) ^ 2
```

**`PhyslibAlpha.Hydrogen.radialMean_two`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L284).

> `⟨1/ρ²⟩ = 1/(ν³ (l + 1/2))`.

```lean
lemma radialMean_two (hl : l < ν) :
    radialMean ν l 2 = 1 / ((ν : ℝ) ^ 3 * (l + 1 / 2))
```

**`PhyslibAlpha.Hydrogen.radialMean_three`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L292).

> `⟨1/ρ³⟩ = 1/(ν³ l (l + 1/2) (l + 1))` for `l ≥ 1`.

```lean
lemma radialMean_three (hl : l < ν) (hl1 : 1 ≤ l) :
    radialMean ν l 3 = 1 / ((ν : ℝ) ^ 3 * (l * (l + 1 / 2) * (l + 1)))
```

## D. The value at the origin

**`PhyslibAlpha.Hydrogen.radialR`**, a def, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L307).

> The radial wave function `R_{νl}(ρ) = u_{νl}(ρ)/ρ = ρ^l e^(-ρ/ν) L_{ν-l-1}^(2l+1)(2ρ/ν)`.

```lean
def radialR (ν l : ℕ) (ρ : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialU_eq_mul_radialR`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L310).

```lean
lemma radialU_eq_mul_radialR (ρ : ℝ) : radialU ν l ρ = ρ * radialR ν l ρ
```

**`PhyslibAlpha.Hydrogen.radialR_zero_sq_div`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L315).

> For an `s` state the normalised density at the nucleus is `|R_{ν0}(0)|²/‖u‖² = 4/ν³`.

```lean
lemma radialR_zero_sq_div (hν : 0 < ν) :
    radialR ν 0 0 ^ 2 / radialMoment ν 0 0 = 4 / (ν : ℝ) ^ 3
```

## E. Physical units

**`PhyslibAlpha.Hydrogen.bohrRadius`**, a def, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L340).

> The Bohr radius `a = ℏ²/(m k)` of a hydrogen atom.

```lean
def bohrRadius (H : HydrogenAtom d) : ℝ
```

**`PhyslibAlpha.Hydrogen.bohrRadius_pos`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L342).

```lean
lemma bohrRadius_pos (H : HydrogenAtom d) (hk : 0 < H.k) : 0 < bohrRadius H
```

**`PhyslibAlpha.Hydrogen.radialFun`**, a def, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L346).

> The reduced radial function `u_{νl}(r/a)` in physical units.

```lean
def radialFun (H : HydrogenAtom d) (ν l : ℕ) (r : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialFun_schrodinger`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean#L352).

> **The radial Schrödinger equation of hydrogen in physical units.** For `d = 3` and an
> attractive potential, `u_{νl}(r/a)` solves
> `-ℏ²/(2m) u'' + (ℏ² l(l+1)/(2m r²) - k/r) u = E u` with `E = -Ry/ν²`, the Bohr level
> `H.energyLevel (ν - 1)` of physlib.

```lean
lemma radialFun_schrodinger (H : HydrogenAtom 3) (hk : 0 < H.k) (hl : l < ν)
    {r : ℝ} (hr : r ≠ 0) :
    -((ℏ : ℝ) ^ 2 / (2 * H.m)) * deriv (deriv (radialFun H ν l)) r +
        ((ℏ : ℝ) ^ 2 * ((l : ℝ) * (l + 1)) / (2 * H.m * r ^ 2) - H.k / r) * radialFun H ν l r =
      H.energyLevel (ν - 1) * radialFun H ν l r
```

## Depends on

- [The Rydberg formula and the spectral series of the hydrogen atom](../../../physlib/quantummechanics/hydrogen/rydberg.md)
- [Generalised Laguerre polynomials](../../mathematics/part-02/specialfunctions/laguerre.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialFunctions.lean)
