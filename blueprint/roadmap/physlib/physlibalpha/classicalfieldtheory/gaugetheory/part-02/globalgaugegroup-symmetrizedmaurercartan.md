---
declaration: module
origin: cited
lean: GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_structure, GlobalGaugeGroup.symmetrizedMaurerCartanForm, GlobalGaugeGroup.symmetrizedMaurerCartanForm_zero, GlobalGaugeGroup.symmetrizedMaurerCartanForm_singleton, GlobalGaugeGroup.symmetrizedMaurerCartanForm_cons, GlobalGaugeGroup.iteratedDerivJ_maurerCartan_eq_symmetrized_add, GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_zero_of_symmetrized_eq_zero, GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq
statement: formalized
proof: formalized
---

# The symmetrized Maurer–Cartan form of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SymmetrizedMaurerCartan`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean): 10 declarations, 8 with a docstring; 1 private, not shown.

> The average of the derivatives of the Maurer–Cartan form over its directions.

## i. Overview

> The Maurer–Cartan form `ω_μ(U) = (∂_μ U) U⁻¹` of a gauge jet `U` of a global gauge group `G` is
> `G.maurerCartan`, subject to the cocycle law `maurerCartan_cocycle`, its value
> `maurerCartan_gaugeJetOfConstant` on constants, and the flatness (structure) equation
> `maurerCartan_structure`. This file develops what follows from those laws alone, for any global
> gauge group. The statements are about the form `−ω_μ(U) = −(∂_μ U) U⁻¹`, the sign in which the
> transformation laws of gauge fields use it.
>
> The main construction is the *symmetrized* Maurer–Cartan form
>
>   `ω̄_r(U) = (1 / |r|) ∑_{μ ∈ r} ∂_{r − {μ}} ω_μ(U)`,
>
> the average over which direction of the multiset `r` is carried by the form itself rather than by a
> derivative. Its point is `iteratedDerivJ_maurerCartan_eq_symmetrized_add`: an iterated
> derivative `∂_s ω_μ(U)` is the symmetrized form at `μ ::ₘ s` plus an average of iterated derivatives
> of *brackets* of Maurer–Cartan forms in strictly fewer directions. This is the structural
> equation used to trade an antisymmetric part for lower-order data. It gives the inductive step
> `evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq`, and iterating it,
> `evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq_all`, the base-point Taylor
> data of `ω` are determined by the base-point symmetrized data. How this determines a pure jet, and
> the truncation filtration it defines, is the subject of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Truncation`.

## ii. Key results

> - `GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_structure` : the structural
>   equation at the base point, to all orders.
> - `GlobalGaugeGroup.symmetrizedMaurerCartanForm` : the symmetrized Maurer–Cartan form, with
>   `symmetrizedMaurerCartanForm_singleton` and the recursion
>   `symmetrizedMaurerCartanForm_cons`.
> - `GlobalGaugeGroup.iteratedDerivJ_maurerCartan_eq_symmetrized_add` : the
>   symmetrization defect is an average of brackets in fewer directions.
> - `GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq_all` :
>   the base-point symmetrized data determine the base-point Taylor data of `ω`, with the inductive
>   step `evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq`.
> - `GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_zero_of_symmetrized_eq_zero` : the
>   base-point half of Maurer–Cartan triangularity.
> - `GlobalGaugeGroup.maurerCartan_eq_zero_iff` : the Maurer–Cartan form vanishes
>   exactly on the constant jets.

## iv. References

> * None.

## A. The structural equation at the base point

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_structure`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L90).

> The all-orders structural equation of the Maurer–Cartan form `−ω`, at the base point.
> It is the `s`-th derivative of `∂_μ (−ω_ν) − ∂_ν (−ω_μ) + ⁅−ω_μ, −ω_ν⁆ = 0`, with the bracket
> expanded by the iterated Leibniz rule.

```lean
lemma evalLie_iteratedDerivJ_maurerCartan_structure
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    G.evalLie (G.iteratedDerivJ (μ ::ₘ s) (-G.maurerCartan U ν)) =
      G.evalLie (G.iteratedDerivJ (ν ::ₘ s) (-G.maurerCartan U μ))
      - (s.antidiagonal.map fun p =>
          ⁅G.evalLie (G.iteratedDerivJ p.1 (-G.maurerCartan U μ)),
            G.evalLie (G.iteratedDerivJ p.2 (-G.maurerCartan U ν))⁆).sum
```

## B. The symmetrized Maurer–Cartan form

**`GlobalGaugeGroup.symmetrizedMaurerCartanForm`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L115).

> The symmetrized Maurer–Cartan form `ω̄_r(U) = (1/|r|) ∑_{μ ∈ r} ∂_{r − {μ}} ω_μ(U)`,
> the average, over the directions of `r`, of the Maurer–Cartan form in one direction
> differentiated along the remaining ones.

```lean
noncomputable def symmetrizedMaurerCartanForm (U : G.gaugeJetGroup) (r : Multiset (Fin 1 ⊕ Fin 3)) :
    G.jetLieSubalgebra
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanForm_zero`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L121).

```lean
lemma symmetrizedMaurerCartanForm_zero (U : G.gaugeJetGroup) :
    G.symmetrizedMaurerCartanForm U 0 = 0
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanForm_singleton`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L126).

```lean
lemma symmetrizedMaurerCartanForm_singleton (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    G.symmetrizedMaurerCartanForm U {μ} = (-G.maurerCartan U μ)
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanForm_cons`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L132).

> The recursion for the symmetrized Maurer–Cartan form, peeling one direction off the
> multiset.

```lean
lemma symmetrizedMaurerCartanForm_cons (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (r : Multiset (Fin 1 ⊕ Fin 3)) : G.symmetrizedMaurerCartanForm U (μ ::ₘ r) =
    (1/(r.card + 1 : ℝ) : ℝ) • (G.iteratedDerivJ r (-G.maurerCartan U μ))
    + ((r.card : ℝ)/(r.card + 1 : ℝ)) •
      G.derivJ μ (G.symmetrizedMaurerCartanForm U r)
```

## C. Determination of the Maurer–Cartan form by its symmetrized coefficients

**`GlobalGaugeGroup.iteratedDerivJ_maurerCartan_eq_symmetrized_add`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L169).

> The symmetrization defect of the Maurer–Cartan form. An iterated derivative of
> `ω` is the corresponding symmetrized form plus an average of iterated derivatives
> of brackets of `ω` in strictly fewer directions. This is the structural equation
> `maurerCartan_structure` used to trade the antisymmetric part for lower-order data.

```lean
lemma iteratedDerivJ_maurerCartan_eq_symmetrized_add (U : G.gaugeJetGroup)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    G.iteratedDerivJ s (-G.maurerCartan U μ) =
      G.symmetrizedMaurerCartanForm U (μ ::ₘ s) +
      (1/(s.card + 1 : ℝ)) • (s.map fun ν =>
        G.iteratedDerivJ (s.erase ν)
          ⁅-G.maurerCartan U μ, -G.maurerCartan U ν⁆).sum
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_zero_of_symmetrized_eq_zero`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L212).

> Maurer–Cartan triangularity, base-point half. If the base-point symmetrized
> Maurer–Cartan data of `U` vanish in every nonempty multiset of at most `n` directions,
> then so do all its base-point Maurer–Cartan Taylor coefficients below order `n`. The
> induction is on the order. The symmetrization defect
> `iteratedDerivJ_maurerCartan_eq_symmetrized_add` expresses `∂_s ω_μ` through the
> symmetrized form, which vanishes by hypothesis, and brackets of `ω`s differentiated
> strictly fewer times, which vanish by the inductive hypothesis through
> `evalLie_iteratedDerivJ_bracket_congr`.

```lean
lemma evalLie_iteratedDerivJ_maurerCartan_eq_zero_of_symmetrized_eq_zero
    (U : G.gaugeJetGroup) {n : ℕ}
    (h : ∀ r : Multiset (Fin 1 ⊕ Fin 3), r ≠ 0 → r.card ≤ n →
      G.evalLie (G.symmetrizedMaurerCartanForm U r) = 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (hs : s.card < n) :
    G.evalLie (G.iteratedDerivJ s (-G.maurerCartan U μ))
      = 0
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L256).

> The determination step. If the base-point symmetrized Maurer–Cartan data of `U` and
> `V` agree, and their Maurer–Cartan Taylor data agree in fewer than `n` directions,
> then they agree in `n` directions.

```lean
lemma evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq
    (U V : G.gaugeJetGroup) (n : ℕ)
    (hsym : ∀ r, G.evalLie (G.symmetrizedMaurerCartanForm U r) =
      G.evalLie (G.symmetrizedMaurerCartanForm V r))
    (ih : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3), s.card < n →
      G.evalLie (G.iteratedDerivJ s (-G.maurerCartan U μ)) =
        G.evalLie (G.iteratedDerivJ s
          (-G.maurerCartan V μ)))
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (hs : s.card = n) :
    G.evalLie (G.iteratedDerivJ s (-G.maurerCartan U μ)) =
      G.evalLie (G.iteratedDerivJ s
        (-G.maurerCartan V μ))
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq_all`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L287).

> The symmetrized data determine the Maurer–Cartan Taylor data. If the base-point
> symmetrized Maurer–Cartan data of `U` and `V` agree, so do all base-point Taylor
> coefficients of their Maurer–Cartan forms. Strong induction on the order, with
> `evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq` as the step.

```lean
lemma evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq_all
    (U V : G.gaugeJetGroup)
    (hsym : ∀ r, G.evalLie (G.symmetrizedMaurerCartanForm U r) =
      G.evalLie (G.symmetrizedMaurerCartanForm V r))
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    G.evalLie (G.iteratedDerivJ s (-G.maurerCartan U μ)) =
      G.evalLie (G.iteratedDerivJ s
        (-G.maurerCartan V μ))
```

## D. Vanishing of the Maurer–Cartan form

**`GlobalGaugeGroup.maurerCartan_eq_zero_iff`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean#L314).

> The Maurer–Cartan form of a gauge jet vanishes exactly when the jet is constant.

```lean
lemma maurerCartan_eq_zero_iff (U : G.gaugeJetGroup) :
    G.maurerCartan U = 0 ↔ U = G.gaugeJetOfConstant (G.evalGaugeJet U)
```

## Depends on

- [The jet operations of a global gauge group](globalgaugegroup-jetoperations.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SymmetrizedMaurerCartan.lean)
