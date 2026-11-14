---
declaration: module
origin: cited
lean: Time.natCast_val, Time.natCast_zero, Time.natCast_one, Time.ofNat_val, Time.one_ne_zero, Time.zero_val, Time.eq_zero_iff, Time.one_val
statement: formalized
proof: formalized
---

# Time as an inner product space

The module `Physlib.SpaceAndTime.Time.InnerProductSpace`, [Physlib/SpaceAndTime/Time/InnerProductSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean): 60 declarations (24 instances with no name), 6 with a docstring.

## i. Overview

> In this module we equip the affine type `Time` with a real inner product space structure,
> choosing the implicit origin represented by `Time.mk 0`. The units and orientation agree with the
> real-valued displacements defined in `Physlib.SpaceAndTime.Time.Basic`.
>
> We note that this is the version of time most often used in undergraduate and
> non-mathematical physics.
>
> The choice of units or origin can be made on a case-by-case basis, as
> long as they are done consistently. However, since the choice of units and origin is
> left implicit, Lean will not catch inconsistencies in the choice of units or origin when
> working with `Time`.
>
> For example, for the classical mechanics system corresponding to the harmonic oscillator,
> one can take the origin of time to be the time at which the initial conditions are specified,
> and the units can be taken as anything as long as the units chosen for time `t` and
> the angular frequency `ω` are consistent.
>
> With this choice, `Time` becomes a 1d vector space over `ℝ` with an inner product.

## ii. Key results

> - `toRealCLE` : The continuous linear equivalence from `Time` to `ℝ`.

## iv. References

> * None.

## A. Instances on Time

### A.1. Natural numbers as elements of `Time`

**An instance with no name**, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L78).

```lean
instance : NatCast Time
```

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L83).

> The casting of a natural number to an element of `Time`. This corresponds to a choice of
> (1) zero point in time, and (2) a choice of metric on time (defining `1`).

```lean
instance {n : ℕ} : OfNat Time n
```

**`Time.natCast_val`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L87).

```lean
lemma natCast_val {n : ℕ} : val n = n
```

**`Time.natCast_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L90).

```lean
lemma natCast_zero : ((0 : ℕ) : Time) = 0
```

**`Time.natCast_one`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L93).

```lean
lemma natCast_one : ((1 : ℕ) : Time) = 1
```

**`Time.ofNat_val`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L96).

```lean
lemma ofNat_val {n : ℕ} : val (OfNat.ofNat n : Time) = n
```

**`Time.one_ne_zero`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L98).

```lean
lemma one_ne_zero : (1 : Time) ≠ (0 : Time)
```

**`Time.zero_val`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L102).

```lean
lemma zero_val : val 0 = 0
```

**`Time.eq_zero_iff`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L105).

```lean
lemma eq_zero_iff (t : Time) : t = 0 ↔ t.val = 0
```

**`Time.one_val`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L108).

```lean
lemma one_val : val 1 = 1
```

**`Time.eq_one_iff`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L111).

```lean
lemma eq_one_iff (t : Time) : t = 1 ↔ t.val = 1
```

### A.2. Real numbers as elements of `Time`

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L119).

```lean
instance : Coe ℝ Time
```

**An instance with no name**, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L122).

```lean
instance : Coe Time ℝ
```

**`Time.realCast_val`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L125).

```lean
lemma realCast_val {r : ℝ} : (r : Time).val = r
```

**`Time.realCast_of_natCast`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L128).

```lean
lemma realCast_of_natCast {n : ℕ} : ((n : ℝ) : Time) = n
```

### A.3. Time is inhabited

**An instance with no name**, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L136).

```lean
instance : Inhabited Time
```

**`Time.default_eq_zero`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L140).

```lean
lemma default_eq_zero : default = 0
```

### A.4. The order on `Time`

**An instance with no name**, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L149).

> The choice of an orientation on `Time`.

```lean
instance : LE Time
```

**`Time.le_def`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L152).

```lean
lemma le_def (t1 t2 : Time) :
    t1 ≤ t2 ↔ t1.val ≤ t2.val
```

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L155).

```lean
instance : PartialOrder Time
```

**`Time.lt_def`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L160).

```lean
lemma lt_def (t1 t2 : Time) :
    t1 < t2 ↔ t1.val < t2.val
```

### A.5. Addition of times

**An instance with no name**, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L169).

```lean
instance : Add Time
```

**`Time.add_val`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L173).

```lean
lemma add_val (t1 t2 : Time) :
    (t1 + t2).val = t1.val + t2.val
```

### A.6. Negation of times

**An instance with no name**, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L182).

```lean
instance : Neg Time
```

**`Time.neg_val`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L186).

```lean
lemma neg_val (t : Time) :
    (-t).val = -t.val
```

### A.7. Subtraction of times

**An instance with no name**, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L195).

```lean
instance : Sub Time
```

**`Time.sub_val`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L199).

```lean
lemma sub_val (t1 t2 : Time) :
    (t1 - t2).val = t1.val - t2.val
```

### A.8. Scalar multiplication of time

**An instance with no name**, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L208).

```lean
instance : SMul ℝ Time
```

**`Time.smul_real_val`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L212).

```lean
lemma smul_real_val (k : ℝ) (t : Time) :
    (k • t).val = k * t.val
```

### A.9. Module on `Time`

**An instance with no name**, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L221).

```lean
instance : AddGroup Time
```

**An instance with no name**, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L229).

```lean
instance : AddCommGroup Time
```

**An instance with no name**, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L232).

```lean
instance : Module ℝ Time
```

### A.10. Norm of time

**An instance with no name**, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L246).

```lean
instance : Norm Time
```

**`Time.norm_eq_val`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L249).

```lean
lemma norm_eq_val (t : Time) :
    ‖t‖ = ‖t.val‖
```

**`Time.dist_eq_val`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L252).

```lean
lemma dist_eq_val (t1 t2 : Time) :
    dist t1 t2 = ‖t1.val - t2.val‖
```

**`Time.dist_eq_real_dist`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L255).

```lean
lemma dist_eq_real_dist (t1 t2 : Time) :
    dist t1 t2 = dist t1.val t2.val
```

**An instance with no name**, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L258).

```lean
instance : SeminormedAddCommGroup Time
```

**An instance with no name**, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L264).

```lean
instance : NormedAddCommGroup Time
```

**An instance with no name**, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L270).

```lean
instance : NormedSpace ℝ Time
```

### A.11. Inner product on `Time`

**An instance with no name**, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L281).

```lean
instance : Inner ℝ Time
```

**`Time.inner_def`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L285).

```lean
lemma inner_def (t1 t2 : Time) :
    ⟪t1, t2⟫_ℝ = t1.val * t2.val
```

**An instance with no name**, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L288).

```lean
noncomputable instance : InnerProductSpace ℝ Time
```

### A.12. Decidability of `Time`

**An instance with no name**, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L300).

```lean
noncomputable instance : DecidableEq Time
```

### A.13. Measurability of `Time`

**An instance with no name**, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L308).

```lean
instance : MeasurableSpace Time
```

**An instance with no name**, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L310).

```lean
instance : BorelSpace Time
```

## B. Basis of `Time`

**`Time.basis`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L321).

> The orthonomral basis on `Time` defined by `1`.

```lean
noncomputable def basis : OrthonormalBasis (Fin 1) ℝ Time
```

**`Time.basis_apply_eq_one`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L354).

```lean
lemma basis_apply_eq_one (i : Fin 1) :
    basis i = 1
```

**`Time.rank_eq_one`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L361).

```lean
lemma rank_eq_one : Module.rank ℝ Time = 1
```

**`Time.finRank_eq_one`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L365).

```lean
lemma finRank_eq_one : Module.finrank ℝ Time = 1
```

**An instance with no name**, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L368).

```lean
instance : FiniteDimensional ℝ Time
```

**`Time.volume_eq_basis_addHaar`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L370).

```lean
lemma volume_eq_basis_addHaar :
    (volume (α := Time)) = basis.toBasis.addHaar
```

## C. Maps from `Time` to `ℝ`

**`Time.toRealCLM`**, a def, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L380).

> The continuous linear map from `Time` to `ℝ`.

```lean
noncomputable def toRealCLM : Time →L[ℝ] ℝ
```

**`Time.toRealCLE`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L387).

> The continuous linear equivalence from `Time` to `ℝ`.

```lean
noncomputable def toRealCLE : Time ≃L[ℝ] ℝ
```

**`Time.toRealLIE`**, a def, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L398).

> The linear isometry equivalence from `Time` to `ℝ`.

```lean
noncomputable def toRealLIE : Time ≃ₗᵢ[ℝ] ℝ
```

**`Time.eq_one_smul`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L409).

```lean
lemma eq_one_smul (t : Time) :
    t = t.val • 1
```

**`Time.val_measurable`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L413).

```lean
lemma val_measurable : Measurable Time.val
```

**`Time.val_measurableEmbedding`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L415).

```lean
lemma val_measurableEmbedding : MeasurableEmbedding Time.val
```

**`Time.val_measurePreserving`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L418).

```lean
lemma val_measurePreserving : MeasurePreserving Time.val volume volume
```

**`Time.val_differentiable`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L422).

```lean
lemma val_differentiable : Differentiable ℝ Time.val
```

**`Time.fderiv_val`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean#L425).

```lean
lemma fderiv_val (t : Time) : fderiv ℝ Time.val t 1 = 1
```

## Depends on

- [Time](basic.md)

## Sources

- [Physlib/SpaceAndTime/Time/InnerProductSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/InnerProductSpace.lean)
