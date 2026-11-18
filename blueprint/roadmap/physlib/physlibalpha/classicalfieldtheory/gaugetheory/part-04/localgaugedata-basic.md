---
declaration: module
origin: cited
lean: LocalGaugeData.maurerCartan_one, LocalGaugeData.maurerCartan_inv, LocalGaugeData.evalLie_adjointJ_ofConstantLie, LocalGaugeData.maurerCartan_eq_of_deriv_adjointJ, LocalGaugeData.evalLie_iteratedDeriv_bracket_congr, LocalGaugeData.Faithful, LocalGaugeData.ext_of_evalLie_iteratedDeriv
statement: formalized
proof: formalized
---

# Local gauge data: further consequences of the laws

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean): 7 declarations, 7 with a docstring.

## i. Overview

> The structure `LocalGaugeData G₀ 𝔤 GJ 𝔤J`, its iterated derivative and its morphisms are
> defined in `Physlib.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Basic`. This file adds the
> consequences of its laws used by the rest of the gauge theory in `PhyslibAlpha`:
>
> * the values of the Maurer–Cartan form on the identity and on inverses, from the cocycle law;
> * the fact that the Maurer–Cartan form is determined by the Leibniz rule `deriv_adjointJ` up
>   to the centre of `𝔤J`, which is why it is a field of the structure;
> * the base-point Taylor data of a bracket, as a function of that of its arguments;
> * the mixin `Faithful`. The transformation laws never ask that the jets be *honest* jets, and
>   `Faithful` records two properties which are true of any honest jet group but are not
>   consequences of the laws: an element of `𝔤J` is determined by its base-point Taylor data,
>   and a jet with vanishing Maurer–Cartan form is constant. The stronger mixin `Free`, in
>   `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Truncation`, adds that every
>   Taylor family is realised.

## ii. Key results

> - `LocalGaugeData.maurerCartan_one`, `LocalGaugeData.maurerCartan_inv` : the values of the
>   Maurer–Cartan form on the identity and on inverses.
> - `LocalGaugeData.maurerCartan_eq_of_deriv_adjointJ` : the Maurer–Cartan form is determined
>   by the Leibniz rule `deriv_adjointJ` up to the centre of `𝔤J`.
> - `LocalGaugeData.evalLie_iteratedDeriv_bracket_congr` : the base-point Taylor data of a bracket
>   is determined by that of its arguments.
> - `LocalGaugeData.Faithful` : the jets are determined by their base-point Taylor data.

## iv. References

> * None.

## A. First consequences of the laws

**`LocalGaugeData.maurerCartan_one`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L68).

> The Maurer–Cartan form of the identity vanishes: the cocycle law at `1 * 1 = 1`.

```lean
lemma maurerCartan_one (μ : Fin 1 ⊕ Fin 3) : jets.maurerCartan 1 μ = 0
```

**`LocalGaugeData.maurerCartan_inv`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L75).

> The Maurer–Cartan form of an inverse: `ω_μ(U⁻¹) = − Ad_{U⁻¹} ω_μ(U)`, the cocycle
> law applied to `U⁻¹ U = 1`.

```lean
lemma maurerCartan_inv (U : GJ) (μ : Fin 1 ⊕ Fin 3) :
    jets.maurerCartan U⁻¹ μ = - jets.adjointJ U⁻¹ (jets.maurerCartan U μ)
```

**`LocalGaugeData.evalLie_adjointJ_ofConstantLie`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L83).

> At the base point, the adjoint action of a jet on a constant is the adjoint action of
> its value.

```lean
lemma evalLie_adjointJ_ofConstantLie (U : GJ) (a : 𝔤) :
    jets.evalLie (jets.adjointJ U (jets.ofConstantLie a)) = jets.adjoint (jets.eval U) a
```

**`LocalGaugeData.maurerCartan_eq_of_deriv_adjointJ`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L95).

> The Maurer–Cartan form is determined by the Leibniz rule, up to the centre. Since
> `adjointJ U` is invertible, `deriv_adjointJ` says exactly that the inner derivation
> `⁅maurerCartan U μ, ·⁆` is `adjointJ U ∘ deriv μ ∘ adjointJ U⁻¹ − deriv μ`; so any other
> form obeying the same rule differs from it by something acting trivially in the adjoint
> representation of `𝔤J`. It follows that the Maurer–Cartan form is redundant data exactly
> when that representation is faithful — which it is not for the Standard Model, whose jet
> gauge algebra has a central `u(1)` factor. That is why `maurerCartan` is a field of the
> structure rather than a construction from the rest of it.

```lean
lemma maurerCartan_eq_of_deriv_adjointJ
    (hfaithful : ∀ x y : 𝔤J, (∀ z : 𝔤J, ⁅x, z⁆ = ⁅y, z⁆) → x = y)
    (ω : GJ → (Fin 1 ⊕ Fin 3) → 𝔤J)
    (hω : ∀ (U : GJ) (μ : Fin 1 ⊕ Fin 3) (x : 𝔤J),
      jets.deriv μ (jets.adjointJ U x)
        = jets.adjointJ U (jets.deriv μ x) - ⁅ω U μ, jets.adjointJ U x⁆) :
    ω = jets.maurerCartan
```

## B. The Taylor data of a bracket

**`LocalGaugeData.evalLie_iteratedDeriv_bracket_congr`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L122).

> The base-point Taylor data of a bracket is determined by that of its arguments.
> If the base-point values of the iterated derivatives of `a` and `b` along sub-multisets
> of `w` agree with those of `a'` and `b'`, then so do those of the brackets: the iterated
> Leibniz rule expands the bracket over the antidiagonal of `w`, whose parts are all
> sub-multisets of `w`.

```lean
lemma evalLie_iteratedDeriv_bracket_congr (w : Multiset (Fin 1 ⊕ Fin 3)) (a b a' b' : 𝔤J)
    (ha : ∀ p ≤ w, jets.evalLie (jets.iteratedDeriv p a)
      = jets.evalLie (jets.iteratedDeriv p a'))
    (hb : ∀ p ≤ w, jets.evalLie (jets.iteratedDeriv p b)
      = jets.evalLie (jets.iteratedDeriv p b')) :
    jets.evalLie (jets.iteratedDeriv w ⁅a, b⁆)
      = jets.evalLie (jets.iteratedDeriv w ⁅a', b'⁆)
```

## C. Faithful packages

> The two laws below make a pure jet (`eval U = 1`) recoverable from its Maurer–Cartan form;
> see `LocalGaugeData.maurerCartan_injOn_truncationKer_zero`. They hold for the full jet group of
> any matrix group and for its truncations, but are recorded separately from the structure
> because the covariance theory does not need them.

**`LocalGaugeData.Faithful`**, a class, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L150).

> A package is faithful when an element of `𝔤J` is determined by the base-point values
> of its iterated derivatives (Taylor determinacy) and a jet with vanishing Maurer–Cartan
> form is the constant jet of its value.

```lean
class Faithful (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) : Prop where
  ext_of_evalLie_iteratedDeriv : ∀ {x y : 𝔤J},
    (∀ s : Multiset (Fin 1 ⊕ Fin 3),
      jets.evalLie (jets.iteratedDeriv s x) = jets.evalLie (jets.iteratedDeriv s y)) → x = y
  eq_ofConstant_of_maurerCartan_eq_zero : ∀ {U : GJ},
    jets.maurerCartan U = 0 → U = jets.ofConstant (jets.eval U)
```

**`LocalGaugeData.ext_of_evalLie_iteratedDeriv`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L158).

> Taylor determinacy of a faithful package, in the form of an extensionality lemma.

```lean
lemma ext_of_evalLie_iteratedDeriv [jets.Faithful] {x y : 𝔤J}
    (h : ∀ s : Multiset (Fin 1 ⊕ Fin 3),
      jets.evalLie (jets.iteratedDeriv s x) = jets.evalLie (jets.iteratedDeriv s y)) :
    x = y
```

## Depends on

- [Local gauge data](../../../../physlib/classicalfieldtheory/gaugetheory/localgaugedata-basic.md)

## Proof depends on

- [Sums over the antidiagonal of a multiset](../../../mathematics/part-01/multisetantidiagonal.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean)
