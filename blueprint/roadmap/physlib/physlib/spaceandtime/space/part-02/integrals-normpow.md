---
declaration: module
origin: cited
lean: Space.radial_jacobian_zpow_mul_self, Space.radial_norm_power_spherical_integral_eq_space_integral, Space.integrableOn_norm_rpow_ball_iff, Space.integrableOn_norm_rpow_ball_compl_iff, Space.integrableOn_norm_rpow_shell, Space.integrableOn_norm_rpow_iff_of_isBounded_nhds, Space.integrableOn_norm_rpow_of_isBounded_compl_nhds, Space.integrableOn_norm_rpow_of_compl_nhds
statement: formalized
proof: formalized
---

# Integrability of norm powers on subsets of Space

The module `Physlib.SpaceAndTime.Space.Integrals.NormPow`, [Physlib/SpaceAndTime/Space/Integrals/NormPow.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean): 8 declarations, 6 with a docstring; 2 private, not shown.

## i. Overview

> This module contains results on the integrability of `x ↦ ‖x‖ᵖ` for real exponents `p` on subsets of
> `Space d`.
>
> The integrability of `x ↦ ‖x‖ᵖ` on `ball 0 b` and `(ball 0 b)ᶜ` follows from the 1d results
> `integrableOn_Ioo_rpow_iff` and `integrableOn_Ioi_rpow_iff` after changing to spherical coordinates.

## ii. Key results

> - `integrableOn_norm_rpow_iff_of_isBounded_nhds`: Necessary and sufficient condition for
>     integrability on a set `s` which is a bounded neighborhood of the origin.
> - `integrableOn_norm_rpow_of_isBounded_compl_nhds`: Integrability for all bounded sets `s`
>     with `0 ∉ closure s`.
> - `integrableOn_norm_rpow_of_compl_nhds`: A sufficient condition for integrability on `s`
>     with `0 ∉ closure s`.
> - `radial_norm_power_spherical_integral_eq_space_integral`: The spherical-coordinate integral
>     identity for integer powers of the norm against a Schwartz map.

## iv. References

> * None.

**`Space.radial_jacobian_zpow_mul_self`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L52).

```lean
lemma radial_jacobian_zpow_mul_self
    {d p : ℕ} [NeZero d] {q : ℤ} (hp_int : (p : ℤ) = q + (d : ℤ))
    {r : ℝ} (hr : 0 < r) :
    r ^ (d - 1) * (r ^ q * r) = r ^ p
```

**`Space.radial_norm_power_spherical_integral_eq_space_integral`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L82).

```lean
lemma radial_norm_power_spherical_integral_eq_space_integral
    {d p : ℕ} [NeZero d] {q : ℤ} (hp_int : (p : ℤ) = q + (d : ℤ))
    (hp_pos : 0 < p) (η : 𝓢(Space d, ℝ)) :
    ∫ x : Space d, η x * ‖x‖ ^ q =
      ∫ (n : ↑(Metric.sphere (0 : Space d) 1)),
        ∫ (r : Set.Ioi (0 : ℝ)),
          r.1 ^ (p - 1) * η (r.1 • n.1)
          ∂(.comap Subtype.val volume)
        ∂(volume (α := Space d).toSphere)
```

**`Space.integrableOn_norm_rpow_ball_iff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L106).

> The function `x ↦ ‖x‖ᵖ` is integrable on `{x : Space d | 0 ≤ ‖x‖ < b}` iff `0 < d + p`.

```lean
lemma integrableOn_norm_rpow_ball_iff {d : ℕ} [NeZero d] {b : ℝ} (hb : 0 < b) (p : ℝ) :
    IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) (Metric.ball 0 b) ↔ 0 < d + p
```

**`Space.integrableOn_norm_rpow_ball_compl_iff`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L133).

> The function `x ↦ ‖x‖ᵖ` is integrable on `{x : Space d | 0 < a ≤ ‖x‖}` iff `d + p < 0`.

```lean
lemma integrableOn_norm_rpow_ball_compl_iff {d : ℕ} [NeZero d] {a : ℝ} (ha : 0 < a) (p : ℝ) :
    IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) (Metric.ball 0 a)ᶜ ↔ d + p < 0
```

**`Space.integrableOn_norm_rpow_shell`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L154).

> The function `x ↦ ‖x‖ᵖ` is integrable on the shell `{x : Space d | 0 < a ≤ ‖x‖ ∧ ‖x‖ < b}`.

```lean
lemma integrableOn_norm_rpow_shell {d : ℕ} {a : ℝ} (ha : 0 < a) (b p : ℝ) :
    IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) ((Metric.ball 0 b) ∩ (Metric.ball 0 a)ᶜ)
```

**`Space.integrableOn_norm_rpow_iff_of_isBounded_nhds`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L176).

> The function `x ↦ ‖x‖ᵖ` is integrable on a bounded neighborhood of the origin
> iff `0 < d + p`.

```lean
lemma integrableOn_norm_rpow_iff_of_isBounded_nhds {d : ℕ} [NeZero d] {s : Set (Space d)}
    (hs : Bornology.IsBounded s) (hs' : s ∈ nhds 0) (p : ℝ) :
    IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) s ↔ 0 < d + p
```

**`Space.integrableOn_norm_rpow_of_isBounded_compl_nhds`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L186).

> The function `x ↦ ‖x‖ᵖ` is integrable on a bounded subset with the origin in its exterior.

```lean
lemma integrableOn_norm_rpow_of_isBounded_compl_nhds {d : ℕ} {s : Set (Space d)}
    (hs : Bornology.IsBounded s) (hs' : sᶜ ∈ nhds 0) (p : ℝ) :
    IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) s
```

**`Space.integrableOn_norm_rpow_of_compl_nhds`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean#L196).

> The function `x ↦ ‖x‖ᵖ` is integrable on a subset with the origin in its exterior provided
> the decay at infinity is fast enough.

```lean
lemma integrableOn_norm_rpow_of_compl_nhds {d : ℕ} [NeZero d] {s : Set (Space d)}
    (hs : sᶜ ∈ nhds 0) {p : ℝ} (h : d + p < 0) : IntegrableOn (fun x : Space d ↦ ‖x‖ ^ p) s
```

## Depends on

- [The structure of a module on Space](../part-01/module.md)

## Proof depends on

- [Functions on `Space d` which can be made into distributions](../part-01/isdistbounded.md)

## Sources

- [Physlib/SpaceAndTime/Space/Integrals/NormPow.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/NormPow.lean)
