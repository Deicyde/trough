---
declaration: module
origin: cited
lean: Space.IsDistBounded, Space.IsDistBounded.aestronglyMeasurable, Space.IsDistBounded.aeStronglyMeasurable_schwartzMap_smul, Space.IsDistBounded.aeStronglyMeasurable_fderiv_schwartzMap_smul, Space.IsDistBounded.aeStronglyMeasurable_inv_pow, Space.IsDistBounded.aeStronglyMeasurable_time_schwartzMap_smul, Space.IsDistBounded.integrable_space, Space.IsDistBounded.integrable_space_mul
statement: formalized
proof: formalized
---

# Functions on `Space d` which can be made into distributions

The module `Physlib.SpaceAndTime.Space.IsDistBounded`, [Physlib/SpaceAndTime/Space/IsDistBounded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean): 64 declarations (1 instance with no name), 1 with a docstring.

## i. Overview

> In this module, for functions `f : Space d → F`, we define the property `IsDistBounded f`.
> Functions satisfying this property can be used to create distributions `Space d →d[ℝ] F`
> by integrating them against Schwartz maps.
>
> The condition `IsDistBounded f` essentially says that `f` is bounded by a finite sum of terms
> of the form `c * ‖x + g‖ ^ p` for constants `c`, `g` and `- (d - 1) ≤ p ` where `d` is the dimension
> of the space.

## ii. Key results

> - `IsDistBounded` : The boundedness condition on functions `Space d → F` for them to
>   form distributions.
> - `IsDistBounded.integrable_space` : If `f` satisfies `IsDistBounded f`, then
>   `fun x => η x • f x` is integrable for any Schwartz map `η : 𝓢(Space d, ℝ)`.
> - `IsDistBounded.integrable_time_space` : If `f` satisfies `IsDistBounded f`, then
>   `fun x => η x • f x.2` is integrable for any Schwartz map
>   `η : 𝓢(Time × Space d, ℝ)`.
> - `IsDistBounded.mono` : If `f₁` satisfies `IsDistBounded f₁` and
>   `‖f₂ x‖ ≤ ‖f₁ x‖` for all `x`, then `f₂` satisfies `IsDistBounded f₂`.

## iv. References

> * None.

## A. The predicate `IsDistBounded f`

**`Space.IsDistBounded`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L90).

> The boundedness condition on a function `Space d → F`
> for it to form a distribution.

```lean
def IsDistBounded {d : ℕ} (f : Space d → F) : Prop
```

## B. Integrability properties of functions satisfying `IsDistBounded f`

### B.1. `AEStronglyMeasurable` conditions

**`Space.IsDistBounded.aestronglyMeasurable`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L113).

```lean
lemma aestronglyMeasurable {d : ℕ} {f : Space d → F} (hf : IsDistBounded f) :
    AEStronglyMeasurable (fun x => f x) volume
```

**`Space.IsDistBounded.aeStronglyMeasurable_schwartzMap_smul`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L117).

```lean
lemma aeStronglyMeasurable_schwartzMap_smul {d : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) :
    AEStronglyMeasurable (fun x => η x • f x)
```

**`Space.IsDistBounded.aeStronglyMeasurable_fderiv_schwartzMap_smul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L123).

```lean
lemma aeStronglyMeasurable_fderiv_schwartzMap_smul {d : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) (y : Space d) :
    AEStronglyMeasurable (fun x => fderiv ℝ η x y • f x)
```

**`Space.IsDistBounded.aeStronglyMeasurable_inv_pow`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L129).

```lean
lemma aeStronglyMeasurable_inv_pow {d r : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) :
    AEStronglyMeasurable (fun x => ‖((1 + ‖x‖) ^ r)⁻¹‖ • f x)
```

**`Space.IsDistBounded.aeStronglyMeasurable_time_schwartzMap_smul`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L135).

```lean
lemma aeStronglyMeasurable_time_schwartzMap_smul {d : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) (η : 𝓢(Time × Space d, ℝ)) :
    AEStronglyMeasurable (fun x => η x • f x.2)
```

### B.2. Integrability with respect to Schwartz maps on space

**`Space.IsDistBounded.integrable_space`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L147).

```lean
lemma integrable_space {d : ℕ} {f : Space d → F} (hf : IsDistBounded f)
    (η : 𝓢(Space d, ℝ)) :
    Integrable (fun x : Space d => η x • f x) volume
```

**`Space.IsDistBounded.integrable_space_mul`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L214).

```lean
lemma integrable_space_mul {d : ℕ} {f : Space d → ℝ} (hf : IsDistBounded f)
    (η : 𝓢(Space d, ℝ)) :
    Integrable (fun x : Space d => η x * f x) volume
```

**`Space.IsDistBounded.integrable_space_fderiv`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L220).

```lean
lemma integrable_space_fderiv {d : ℕ} {f : Space d → F} (hf : IsDistBounded f)
    (η : 𝓢(Space d, ℝ)) (y : Space d) :
    Integrable (fun x : Space d => fderiv ℝ η x y • f x) volume
```

**`Space.IsDistBounded.integrable_space_fderiv_mul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L226).

```lean
lemma integrable_space_fderiv_mul {d : ℕ} {f : Space d → ℝ} (hf : IsDistBounded f)
    (η : 𝓢(Space d, ℝ)) (y : Space d) :
    Integrable (fun x : Space d => fderiv ℝ η x y * f x) volume
```

### B.3. Integrability with respect to Schwartz maps on time and space

**An instance with no name**, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L237).

```lean
instance {D1 : Type} [NormedAddCommGroup D1] [MeasurableSpace D1]
    {D2 : Type} [NormedAddCommGroup D2] [MeasurableSpace D2]
    (μ1 : Measure D1) (μ2 : Measure D2)
    [Measure.HasTemperateGrowth μ1] [Measure.HasTemperateGrowth μ2]
    [OpensMeasurableSpace (D1 × D2)] :
    Measure.HasTemperateGrowth (μ1.prod μ2)
```

**`Space.IsDistBounded.integrable_time_space`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L266).

```lean
lemma integrable_time_space {d : ℕ} {f : Space d → F} (hf : IsDistBounded f)
    (η : 𝓢(Time × Space d, ℝ)) :
    Integrable (fun x : Time × Space d => η x • f x.2) volume
```

### B.4. Integrability with respect to inverse powers

**`Space.IsDistBounded.integrable_mul_inv_pow`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L365).

```lean
lemma integrable_mul_inv_pow {d : ℕ}
    {f : Space d → F} (hf : IsDistBounded f) :
    ∃ r, Integrable (fun x => ‖((1 + ‖x‖) ^ r)⁻¹‖ • f x) volume
```

## C. Integral on Schwartz maps is bounded by seminorms

**`Space.IsDistBounded.integral_mul_schwartzMap_bounded`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L457).

```lean
lemma integral_mul_schwartzMap_bounded {d : ℕ} {f : Space d → F} (hf : IsDistBounded f) :
    ∃ (s : Finset (ℕ × ℕ)) (C : ℝ),
    0 ≤ C ∧ ∀ (η : 𝓢(Space d, ℝ)),
    ‖∫ (x : Space d), η x • f x‖ ≤ C * (s.sup (schwartzSeminormFamily ℝ (Space d) ℝ)) η
```

## D. Construction rules for `IsDistBounded f`

**`Space.IsDistBounded.zero`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L501).

```lean
lemma zero {d} : IsDistBounded (0 : Space d → F)
```

### D.1. Addition

**`Space.IsDistBounded.add`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L510).

```lean
lemma add {d : ℕ} {f g : Space d → F}
    (hf : IsDistBounded f) (hg : IsDistBounded g) : IsDistBounded (f + g)
```

**`Space.IsDistBounded.fun_add`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L528).

```lean
lemma fun_add {d : ℕ} {f g : Space d → F}
    (hf : IsDistBounded f) (hg : IsDistBounded g) : IsDistBounded (fun x => f x + g x)
```

### D.2. Finite sums

**`Space.IsDistBounded.sum`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L538).

```lean
lemma sum {ι : Type*} {s : Finset ι} {d : ℕ} {f : ι → Space d → F}
    (hf : ∀ i ∈ s, IsDistBounded (f i)) : IsDistBounded (∑ i ∈ s, f i)
```

**`Space.IsDistBounded.sum_fun`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L547).

```lean
lemma sum_fun {ι : Type*} {s : Finset ι} {d : ℕ} {f : ι → Space d → F}
    (hf : ∀ i ∈ s, IsDistBounded (f i)) : IsDistBounded (fun x => ∑ i ∈ s, f i x)
```

### D.3. Scalar multiplication

**`Space.IsDistBounded.const_smul`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L558).

```lean
lemma const_smul {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) (c : ℝ) : IsDistBounded (c • f)
```

**`Space.IsDistBounded.neg`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L567).

```lean
lemma neg {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) : IsDistBounded (fun x => - f x)
```

**`Space.IsDistBounded.const_fun_smul`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L572).

```lean
lemma const_fun_smul {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) (c : ℝ) : IsDistBounded (fun x => c • f x)
```

**`Space.IsDistBounded.const_mul_fun`**, a lemma, [line 576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L576).

```lean
lemma const_mul_fun {d : ℕ}
    {f : Space d → ℝ}
    (hf : IsDistBounded f) (c : ℝ) : IsDistBounded (fun x => c * f x)
```

**`Space.IsDistBounded.mul_const_fun`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L581).

```lean
lemma mul_const_fun {d : ℕ}
    {f : Space d → ℝ}
    (hf : IsDistBounded f) (c : ℝ) : IsDistBounded (fun x => f x * c)
```

### D.4. Components of functions

**`Space.IsDistBounded.pi_comp`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L593).

```lean
lemma pi_comp {d n : ℕ}
    {f : Space d → EuclideanSpace ℝ (Fin n)}
    (hf : IsDistBounded f) (j : Fin n) : IsDistBounded (fun x => f x j)
```

**`Space.IsDistBounded.vector_component`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L600).

```lean
lemma vector_component {d n : ℕ} {f : Space d → Lorentz.Vector n}
    (hf : IsDistBounded f) (j : Fin 1 ⊕ Fin n) : IsDistBounded (fun x => f x j)
```

### D.5. Compositions with additions and subtractions

**`Space.IsDistBounded.comp_add_right`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L612).

```lean
lemma comp_add_right {d : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) (c : Space d) :
    IsDistBounded (fun x => f (x + c))
```

**`Space.IsDistBounded.comp_sub_right`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L621).

```lean
lemma comp_sub_right {d : ℕ} {f : Space d → F}
    (hf : IsDistBounded f) (c : Space d) :
    IsDistBounded (fun x => f (x - c))
```

### D.6. Congruence with respect to the norm

**`Space.IsDistBounded.congr`**, a lemma, [line 632](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L632).

```lean
lemma congr {d : ℕ} {f : Space d → F}
    {g : Space d → F'}
    (hf : IsDistBounded f) (hae : AEStronglyMeasurable g) (hfg : ∀ x, ‖g x‖ = ‖f x‖) :
      IsDistBounded g
```

### D.7. Monotonicity with respect to the norm

**`Space.IsDistBounded.mono`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L646).

```lean
lemma mono {d : ℕ} {f : Space d → F}
    {g : Space d → F'}
    (hf : IsDistBounded f) (hae : AEStronglyMeasurable g)
    (hfg : ∀ x, ‖g x‖ ≤ ‖f x‖) : IsDistBounded g
```

### D.8. Inner products

**`Space.IsDistBounded.inner_left`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L661).

```lean
lemma inner_left {d n : ℕ}
    {f : Space d → EuclideanSpace ℝ (Fin n) }
    (hf : IsDistBounded f) (y : EuclideanSpace ℝ (Fin n)) :
    IsDistBounded (fun x => ⟪f x, y⟫_ℝ)
```

### D.9. Scalar multiplication with constant

**`Space.IsDistBounded.smul_const`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L678).

```lean
lemma smul_const {d : ℕ} [NormedSpace ℝ F] {c : Space d → ℝ}
    (hc : IsDistBounded c) (f : F) : IsDistBounded (fun x => c x • f)
```

## E. Specific functions that are `IsDistBounded`

### E.1. Constant functions

**`Space.IsDistBounded.const`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L694).

```lean
lemma const {d : ℕ} (f : F) :
    IsDistBounded (d := d) (fun _ : Space d => f)
```

### E.2. Powers of norms

**`Space.IsDistBounded.pow`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L705).

```lean
lemma pow {d : ℕ} (n : ℤ) (hn : - (d - 1 : ℕ) ≤ n) :
    IsDistBounded (d := d) (fun x => ‖x‖ ^ n)
```

**`Space.IsDistBounded.pow_shift`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L711).

```lean
lemma pow_shift {d : ℕ} (n : ℤ)
    (g : Space d) (hn : - (d - 1 : ℕ) ≤ n) :
    IsDistBounded (d := d) (fun x => ‖x - g‖ ^ n)
```

**`Space.IsDistBounded.inv_shift`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L718).

```lean
lemma inv_shift {d : ℕ} (g : Space d) (hd : 2 ≤ d := by omega) :
    IsDistBounded (d := d) (fun x => ‖x - g‖⁻¹)
```

**`Space.IsDistBounded.nat_pow`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L722).

```lean
lemma nat_pow {d : ℕ} (n : ℕ) :
    IsDistBounded (d := d) (fun x => ‖x‖ ^ n)
```

**`Space.IsDistBounded.norm_add_nat_pow`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L727).

```lean
lemma norm_add_nat_pow {d : ℕ} (n : ℕ) (a : ℝ) :
    IsDistBounded (d := d) (fun x => (‖x‖ + a) ^ n)
```

**`Space.IsDistBounded.norm_add_pos_nat_zpow`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L733).

```lean
lemma norm_add_pos_nat_zpow {d : ℕ} (n : ℤ) (a : ℝ) (ha : 0 < a) :
    IsDistBounded (d := d) (fun x => (‖x‖ + a) ^ n)
```

**`Space.IsDistBounded.nat_pow_shift`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L745).

```lean
lemma nat_pow_shift {d : ℕ} (n : ℕ)
    (g : Space d) :
    IsDistBounded (d := d) (fun x => ‖x - g‖ ^ n)
```

**`Space.IsDistBounded.norm_sub`**, a lemma, [line 751](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L751).

```lean
lemma norm_sub {d : ℕ} (g : Space d) :
    IsDistBounded (d := d) (fun x => ‖x - g‖)
```

**`Space.IsDistBounded.norm_add`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L756).

```lean
lemma norm_add {d : ℕ} (g : Space d) :
    IsDistBounded (d := d) (fun x => ‖x + g‖)
```

**`Space.IsDistBounded.inv`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L761).

```lean
lemma inv {d : ℕ} (hd: 2 ≤ d := by omega):
    IsDistBounded (d := d) (fun x => ‖x‖⁻¹)
```

**`Space.IsDistBounded.norm`**, a lemma, [line 766](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L766).

```lean
lemma norm {d : ℕ} : IsDistBounded (d := d) (fun x => ‖x‖)
```

**`Space.IsDistBounded.log_norm`**, a lemma, [line 770](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L770).

```lean
lemma log_norm {d : ℕ} (hd : 2 ≤ d := by omega) :
    IsDistBounded (d := d) (fun x => Real.log ‖x‖)
```

**`Space.IsDistBounded.zpow_smul_self`**, a lemma, [line 783](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L783).

```lean
lemma zpow_smul_self {d : ℕ} (n : ℤ) (hn : - (d - 1 : ℕ) - 1 ≤ n) :
    IsDistBounded (d := d) (fun x => ‖x‖ ^ n • x)
```

**`Space.IsDistBounded.zpow_smul_repr_self`**, a lemma, [line 796](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L796).

```lean
lemma zpow_smul_repr_self {d : ℕ} (n : ℤ) (hn : - (d - 1 : ℕ) - 1 ≤ n) :
    IsDistBounded (d := d) (fun x => ‖x‖ ^ n • basis.repr x)
```

**`Space.IsDistBounded.zpow_smul_repr_self_sub`**, a lemma, [line 801](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L801).

```lean
lemma zpow_smul_repr_self_sub {d : ℕ} (n : ℤ) (hn : - (d - 1 : ℕ) - 1 ≤ n)
    (y : Space d) :
    IsDistBounded (d := d) (fun x => ‖x - y‖ ^ n • basis.repr (x - y))
```

**`Space.IsDistBounded.inv_pow_smul_self`**, a lemma, [line 806](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L806).

```lean
lemma inv_pow_smul_self {d : ℕ} (n : ℕ) (hn : - (d - 1 : ℕ) - 1 ≤ (- n : ℤ)) :
    IsDistBounded (d := d) (fun x => ‖x‖⁻¹ ^ n • x)
```

**`Space.IsDistBounded.inv_pow_smul_repr_self`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L810).

```lean
lemma inv_pow_smul_repr_self {d : ℕ} (n : ℕ) (hn : - (d - 1 : ℕ) - 1 ≤ (- n : ℤ)) :
    IsDistBounded (d := d) (fun x => ‖x‖⁻¹ ^ n • basis.repr x)
```

## F. Multiplication by norms and components

**`Space.IsDistBounded.norm_smul_nat_pow`**, a lemma, [line 820](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L820).

```lean
lemma norm_smul_nat_pow {d} (p : ℕ) (c : Space d) :
    IsDistBounded (fun x => ‖x‖ * ‖x + c‖ ^ p)
```

**`Space.IsDistBounded.norm_smul_zpow`**, a lemma, [line 832](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L832).

```lean
lemma norm_smul_zpow {d} (p : ℤ) (c : Space d) (hn : - (d - 1 : ℕ) ≤ p) :
    IsDistBounded (fun x => ‖x‖ * ‖x + c‖ ^ p)
```

**`Space.IsDistBounded.norm_smul_isDistBounded`**, a lemma, [line 865](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L865).

```lean
lemma norm_smul_isDistBounded {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) :
    IsDistBounded (fun x => ‖x‖ • f x)
```

**`Space.IsDistBounded.norm_mul_isDistBounded`**, a lemma, [line 882](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L882).

```lean
lemma norm_mul_isDistBounded {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) :
    IsDistBounded (fun x => ‖x‖ * f x)
```

**`Space.IsDistBounded.component_smul_isDistBounded`**, a lemma, [line 887](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L887).

```lean
lemma component_smul_isDistBounded {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) (i : Fin d) :
    IsDistBounded (fun x => x i • f x)
```

**`Space.IsDistBounded.component_mul_isDistBounded`**, a lemma, [line 898](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L898).

```lean
lemma component_mul_isDistBounded {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) (i : Fin d) :
    IsDistBounded (fun x => x i * f x)
```

**`Space.IsDistBounded.isDistBounded_smul_self`**, a lemma, [line 903](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L903).

```lean
lemma isDistBounded_smul_self {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) : IsDistBounded (fun x => f x • x)
```

**`Space.IsDistBounded.isDistBounded_smul_self_repr`**, a lemma, [line 910](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L910).

```lean
lemma isDistBounded_smul_self_repr {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) : IsDistBounded (fun x => f x • basis.repr x)
```

**`Space.IsDistBounded.isDistBounded_smul_inner`**, a lemma, [line 918](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L918).

```lean
lemma isDistBounded_smul_inner {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded f) (y : Space d) : IsDistBounded (fun x => ⟪y, x⟫_ℝ • f x)
```

**`Space.IsDistBounded.isDistBounded_smul_inner_of_smul_norm`**, a lemma, [line 925](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L925).

```lean
lemma isDistBounded_smul_inner_of_smul_norm {d : ℕ} [NormedSpace ℝ F] {f : Space d → F}
    (hf : IsDistBounded (fun x => ‖x‖ • f x)) (hae : AEStronglyMeasurable f) (y : Space d) :
    IsDistBounded (fun x => ⟪y, x⟫_ℝ • f x)
```

**`Space.IsDistBounded.isDistBounded_mul_inner`**, a lemma, [line 936](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L936).

```lean
lemma isDistBounded_mul_inner {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) (y : Space d) : IsDistBounded (fun x => ⟪y, x⟫_ℝ * f x)
```

**`Space.IsDistBounded.isDistBounded_mul_inner'`**, a lemma, [line 940](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L940).

```lean
lemma isDistBounded_mul_inner' {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded f) (y : Space d) : IsDistBounded (fun x => ⟪x, y⟫_ℝ * f x)
```

**`Space.IsDistBounded.isDistBounded_mul_inner_of_smul_norm`**, a lemma, [line 944](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L944).

```lean
lemma isDistBounded_mul_inner_of_smul_norm {d : ℕ} {f : Space d → ℝ}
    (hf : IsDistBounded (fun x => ‖x‖ * f x)) (hae : AEStronglyMeasurable f) (y : Space d) :
    IsDistBounded (fun x => ⟪y, x⟫_ℝ * f x)
```

**`Space.IsDistBounded.mul_inner_pow_neg_two`**, a lemma, [line 949](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean#L949).

```lean
lemma mul_inner_pow_neg_two {d : ℕ} (y : Space d) (hd : 2 ≤ d := by omega) :
    IsDistBounded (fun x => ⟪y, x⟫_ℝ * ‖x‖ ^ (- 2 : ℤ))
```

## Depends on

- [Lorentz Vectors](../../../relativity/tensors/part-03/realtensor-vector-basic.md)
- [The structure of a module on Space](module.md)
- [Time as an inner product space](../../time/innerproductspace.md)

## Proof depends on

- [The radial angular measure on Space](../part-02/integrals-radialangularmeasure.md)

## Sources

- [Physlib/SpaceAndTime/Space/IsDistBounded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/IsDistBounded.lean)
