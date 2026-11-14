---
declaration: module
origin: cited
lean: LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_structure, LocalGaugeData.symmetrizedMaurerCartanForm, LocalGaugeData.symmetrizedMaurerCartanForm_apply_zero, LocalGaugeData.symmetrizedMaurerCartanForm_one, LocalGaugeData.symmetrizedMaurerCartanForm_ofConstant, LocalGaugeData.symmetrizedMaurerCartanForm_singleton, LocalGaugeData.symmetrizedMaurerCartanForm_cons, LocalGaugeData.iteratedDeriv_maurerCartan_eq_symmetrized_add
statement: formalized
proof: formalized
---

# The Maurer–Cartan form of a local gauge data package

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MaurerCartan`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean): 12 declarations, 8 with a docstring.

## i. Overview

> The Maurer–Cartan form `ω_μ(U) = i (∂_μ U) U⁻¹` of a package
> `jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J` is the field `jets.maurerCartan`, subject to the cocycle
> law `maurerCartan_cocycle`, its value `maurerCartan_ofConstant` on constants, and the
> flatness (structural) equation `maurerCartan_structure`. This file develops what follows
> from those laws alone, for any package: nothing here mentions a particular gauge group.
>
> The main construction is the *symmetrized* Maurer–Cartan form
>
>   `ω̄_r(U) = (1 / |r|) ∑_{μ ∈ r} ∂_{r − {μ}} ω_μ(U)`,
>
> the average over which direction of the multiset `r` is carried by the form itself rather
> than by a derivative. Its point is `iteratedDeriv_maurerCartan_eq_symmetrized_add`: an
> iterated derivative `∂_s ω_μ(U)` is the symmetrized form at `μ ::ₘ s` plus an average of
> iterated derivatives of *brackets* of Maurer–Cartan forms in strictly fewer directions —
> the structural equation used to trade an antisymmetric part for lower-order data. This gives
> the inductive step `evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq`, and iterating
> it, `evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq_all`: the base-point Taylor
> data of `ω` is determined by the base-point symmetrized data. How this determines a pure
> jet, and the truncation filtration it defines, is the subject of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Truncation`.

## ii. Key results

> - `LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_structure` : the structural equation
>   at the base point, to all orders.
> - `LocalGaugeData.symmetrizedMaurerCartanForm` : the symmetrized Maurer–Cartan form, with
>   `symmetrizedMaurerCartanForm_singleton` and the recursion
>   `symmetrizedMaurerCartanForm_cons`.
> - `LocalGaugeData.iteratedDeriv_maurerCartan_eq_symmetrized_add` : the symmetrization
>   defect is an average of brackets in fewer directions.
> - `LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq_all` : the
>   base-point symmetrized data determine the base-point Taylor data of `ω`, with the
>   inductive step `evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq`.
> - `LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_eq_zero_of_symmetrized_eq_zero` : the
>   base-point half of Maurer–Cartan triangularity.
> - `LocalGaugeData.maurerCartan_eq_zero_iff` : in a faithful package, the Maurer–Cartan form
>   vanishes exactly on the constant jets.

## iv. References

> * None.

## A. The structural equation at the base point

**`LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_structure`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L82).

> The all-orders structural equation of the Maurer–Cartan form, at the base point:
> the `s`-th derivative of `∂_μ ω_ν − ∂_ν ω_μ + ⁅ω_μ, ω_ν⁆ = 0`, with the bracket
> expanded by the iterated Leibniz rule.

```lean
lemma evalLie_iteratedDeriv_maurerCartan_structure
    (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    jets.evalLie (jets.iteratedDeriv (μ ::ₘ s) (jets.maurerCartan U ν)) =
      jets.evalLie (jets.iteratedDeriv (ν ::ₘ s) (jets.maurerCartan U μ))
      - (s.antidiagonal.map fun p =>
          ⁅jets.evalLie (jets.iteratedDeriv p.1 (jets.maurerCartan U μ)),
            jets.evalLie (jets.iteratedDeriv p.2 (jets.maurerCartan U ν))⁆).sum
```

## B. The symmetrized Maurer–Cartan form

**`LocalGaugeData.symmetrizedMaurerCartanForm`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L107).

> The symmetrized Maurer–Cartan form `ω̄_r(U) = (1/|r|) ∑_{μ ∈ r} ∂_{r − {μ}} ω_μ(U)`:
> the average, over the directions of `r`, of the Maurer–Cartan form in one direction
> differentiated along the remaining ones.

```lean
noncomputable def symmetrizedMaurerCartanForm (U : GJ) (r : Multiset (Fin 1 ⊕ Fin 3)) : 𝔤J
```

**`LocalGaugeData.symmetrizedMaurerCartanForm_apply_zero`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L112).

```lean
lemma symmetrizedMaurerCartanForm_apply_zero (U : GJ) :
    jets.symmetrizedMaurerCartanForm U 0 = 0
```

**`LocalGaugeData.symmetrizedMaurerCartanForm_one`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L117).

```lean
lemma symmetrizedMaurerCartanForm_one : jets.symmetrizedMaurerCartanForm 1 = 0
```

**`LocalGaugeData.symmetrizedMaurerCartanForm_ofConstant`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L122).

```lean
lemma symmetrizedMaurerCartanForm_ofConstant (g : G₀) :
    jets.symmetrizedMaurerCartanForm (jets.ofConstant g) = 0
```

**`LocalGaugeData.symmetrizedMaurerCartanForm_singleton`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L128).

```lean
lemma symmetrizedMaurerCartanForm_singleton (U : GJ) (μ : Fin 1 ⊕ Fin 3) :
    jets.symmetrizedMaurerCartanForm U {μ} = jets.maurerCartan U μ
```

**`LocalGaugeData.symmetrizedMaurerCartanForm_cons`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L134).

> The recursion for the symmetrized Maurer–Cartan form: peeling one direction off the
> multiset.

```lean
lemma symmetrizedMaurerCartanForm_cons (U : GJ) (μ : Fin 1 ⊕ Fin 3)
    (r : Multiset (Fin 1 ⊕ Fin 3)) : jets.symmetrizedMaurerCartanForm U (μ ::ₘ r) =
    (1/(r.card + 1 : ℝ) : ℝ) • (jets.iteratedDeriv r (jets.maurerCartan U μ))
    + ((r.card : ℝ)/(r.card + 1 : ℝ)) •
      jets.deriv μ (jets.symmetrizedMaurerCartanForm U r)
```

## C. Determination of the Maurer–Cartan form by its symmetrized coefficients

**`LocalGaugeData.iteratedDeriv_maurerCartan_eq_symmetrized_add`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L170).

> The symmetrization defect of the Maurer–Cartan form: an iterated derivative of
> `ω` is the corresponding symmetrized form plus an average of iterated derivatives
> of brackets of `ω` in strictly fewer directions. This is the structural equation
> `maurerCartan_structure` used to trade the antisymmetric part for lower-order data.

```lean
lemma iteratedDeriv_maurerCartan_eq_symmetrized_add (U : GJ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    jets.iteratedDeriv s (jets.maurerCartan U μ) =
      jets.symmetrizedMaurerCartanForm U (μ ::ₘ s) +
      (1/(s.card + 1 : ℝ)) • (s.map fun ν =>
        jets.iteratedDeriv (s.erase ν)
          ⁅jets.maurerCartan U μ, jets.maurerCartan U ν⁆).sum
```

**`LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_eq_zero_of_symmetrized_eq_zero`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L211).

> Maurer–Cartan triangularity, base-point half: if the base-point symmetrized
> Maurer–Cartan data of `U` vanish in every nonempty multiset of at most `n` directions,
> then so do all its base-point Maurer–Cartan Taylor coefficients below order `n`. The
> induction is on the order: the symmetrization defect
> `iteratedDeriv_maurerCartan_eq_symmetrized_add` expresses `∂_s ω_μ` through the
> symmetrized form, which vanishes by hypothesis, and brackets of `ω`s differentiated
> strictly fewer times, which vanish by the inductive hypothesis through
> `evalLie_iteratedDeriv_bracket_congr`.

```lean
lemma evalLie_iteratedDeriv_maurerCartan_eq_zero_of_symmetrized_eq_zero (U : GJ) {n : ℕ}
    (h : ∀ r : Multiset (Fin 1 ⊕ Fin 3), r ≠ 0 → r.card ≤ n →
      jets.evalLie (jets.symmetrizedMaurerCartanForm U r) = 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (hs : s.card < n) :
    jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U μ)) = 0
```

**`LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L252).

> Determination step: if the base-point symmetrized Maurer–Cartan data of `U` and
> `V` agree, and their Maurer–Cartan Taylor data agree in fewer than `n` directions,
> then they agree in `n` directions.

```lean
lemma evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq (U V : GJ) (n : ℕ)
    (hsym : ∀ r, jets.evalLie (jets.symmetrizedMaurerCartanForm U r) =
      jets.evalLie (jets.symmetrizedMaurerCartanForm V r))
    (ih : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3), s.card < n →
      jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U μ)) =
        jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan V μ)))
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (hs : s.card = n) :
    jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U μ)) =
      jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan V μ))
```

**`LocalGaugeData.evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq_all`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L280).

> **The symmetrized data determine the Maurer–Cartan Taylor data**: if the base-point
> symmetrized Maurer–Cartan data of `U` and `V` agree, so do all base-point Taylor
> coefficients of their Maurer–Cartan forms. Strong induction on the order, with
> `evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq` as the step.

```lean
lemma evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq_all (U V : GJ)
    (hsym : ∀ r, jets.evalLie (jets.symmetrizedMaurerCartanForm U r) =
      jets.evalLie (jets.symmetrizedMaurerCartanForm V r))
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U μ)) =
      jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan V μ))
```

## D. Faithful packages and the Maurer–Cartan form

**`LocalGaugeData.maurerCartan_eq_zero_iff`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean#L304).

> In a faithful package, the Maurer–Cartan form vanishes exactly on the constant jets.

```lean
lemma maurerCartan_eq_zero_iff [jets.Faithful] (U : GJ) :
    jets.maurerCartan U = 0 ↔ U = jets.ofConstant (jets.eval U)
```

## Depends on

- [Local gauge data: further consequences of the laws](localgaugedata-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MaurerCartan.lean)
