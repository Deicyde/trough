---
declaration: module
origin: cited
lean: Lorentz.lorentzMixStep, Lorentz.lorentzMix, Lorentz.lorentzMix_zero, Lorentz.lorentzMix_cons_apply, Lorentz.lorentzMix_apply_add, Lorentz.lorentzMix_cons_zero, Lorentz.lorentzMix_map, Lorentz.lorentzMix_smul_fam
statement: formalized
proof: formalized
---

# The Lorentz mixing of derivative slots

The module `PhyslibAlpha.Relativity.LorentzMix`, [PhyslibAlpha/Relativity/LorentzMix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean): 19 declarations (1 instance with no name), 18 with a docstring.

## i. Overview

> A Lorentz transformation mixes each derivative slot of a symbol through a column `Λ_{b a}`
> of the Lorentz matrix. On families indexed by multisets of directions this is the operator
> `lorentzMix`: peel one direction `a`, put it back as every direction `b` weighted by
> `Λ_{b a}`, and mix what is left; peeling commutes, so the operator descends to multisets,
> and `lorentzMix_ofFn` is its tuple form. The correction terms of a covariant derivative are
> Leibniz convolutions `derivConv` over the multiset antidiagonal, and `lorentzMix` is a
> morphism for the convolution. The Lorentz law of any covariant tower built one slot at a
> time from a covariant correction is then one induction, `repLorentz_tower`. Nothing here
> depends on a gauge group.

## ii. Key results

> - `Lorentz.lorentzMix`, `Lorentz.lorentzMix_ofFn` : the mixing operator and its tuple form.
> - `Lorentz.derivConv`, `Lorentz.lorentzMix_derivConv` : the Leibniz convolution, and the
>   mixing operator as a morphism for it.
> - `Lorentz.repLorentz_tower` : the Lorentz law of an abstract covariant tower.

## iv. References

> * None.

## A. The Lorentz mixing of derivative slots

**`Lorentz.lorentzMixStep`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L67).

> One peeling step of the Lorentz mixing: the direction `a` is removed from the multiset
> index of the family and put back as every direction `b`, weighted by `Λ_{b a}`.

```lean
noncomputable def lorentzMixStep (Λ : SL(2,ℂ)) (a : Fin 1 ⊕ Fin 3)
    (G : Multiset (Fin 1 ⊕ Fin 3) → M) : Multiset (Fin 1 ⊕ Fin 3) → M
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L72).

> Peeling two directions commutes, so the mixing is well defined on a multiset.

```lean
instance (Λ : SL(2,ℂ)) : LeftCommutative (lorentzMixStep (M := M) Λ)
```

**`Lorentz.lorentzMix`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L83).

> The Lorentz mixing of a multiset-indexed family along a multiset `s` of directions:
> every direction of `s` is peeled and replaced by all directions, weighted by the
> corresponding column of the Lorentz matrix.

```lean
noncomputable def lorentzMix (Λ : SL(2,ℂ)) (G : Multiset (Fin 1 ⊕ Fin 3) → M)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Multiset (Fin 1 ⊕ Fin 3) → M
```

**`Lorentz.lorentzMix_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L90).

```lean
lemma lorentzMix_zero : lorentzMix Λ G 0 = G
```

**`Lorentz.lorentzMix_cons_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L93).

> Mixing along `a ::ₘ s` peels `a` after mixing along `s`.

```lean
lemma lorentzMix_cons_apply (a : Fin 1 ⊕ Fin 3) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (a ::ₘ s) t = ∑ b, L[Λ] b a • lorentzMix Λ G s (b ::ₘ t)
```

**`Lorentz.lorentzMix_apply_add`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L99).

> Evaluating a mixed family away from the empty multiset is mixing the translated
> family at the empty multiset.

```lean
lemma lorentzMix_apply_add (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∀ (G : Multiset (Fin 1 ⊕ Fin 3) → M) (t : Multiset (Fin 1 ⊕ Fin 3)),
      lorentzMix Λ G s t = lorentzMix Λ (fun r => G (r + t)) s 0
```

**`Lorentz.lorentzMix_cons_zero`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L110).

> Peeling at the empty multiset: the peeled direction is pushed into the family.

```lean
lemma lorentzMix_cons_zero (a : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (a ::ₘ s) 0 = ∑ b, L[Λ] b a • lorentzMix Λ (fun t => G (b ::ₘ t)) s 0
```

**`Lorentz.lorentzMix_map`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L115).

> The mixing operator commutes with any linear map applied to the values.

```lean
lemma lorentzMix_map (Φ : M →ₗ[ℂ] N) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    Φ (lorentzMix Λ G s t) = lorentzMix Λ (fun r => Φ (G r)) s t
```

**`Lorentz.lorentzMix_smul_fam`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L122).

> The mixing operator is homogeneous in the family.

```lean
lemma lorentzMix_smul_fam (c : ℂ) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => c • G r) s t = c • lorentzMix Λ G s t
```

**`Lorentz.lorentzMix_add_fam`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L127).

> The mixing operator is additive in the family.

```lean
lemma lorentzMix_add_fam (G₁ G₂ : Multiset (Fin 1 ⊕ Fin 3) → M)
    (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => G₁ r + G₂ r) s t = lorentzMix Λ G₁ s t + lorentzMix Λ G₂ s t
```

**`Lorentz.lorentzMix_sum_fam`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L136).

> The mixing operator commutes with finite sums of families.

```lean
lemma lorentzMix_sum_fam {ι : Type*} [Fintype ι] (H : ι → Multiset (Fin 1 ⊕ Fin 3) → M)
    (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => ∑ i, H i r) s t = ∑ i, lorentzMix Λ (H i) s t
```

**`Lorentz.lorentzMix_ofFn`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L148).

> The mixing operator agrees with the tuple form of the Lorentz law: along an ordered
> tuple of directions it is the sum over all tuples with one Lorentz matrix factor per
> slot.

```lean
lemma lorentzMix_ofFn {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (List.ofFn l) t =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, L[Λ] (p i) (l i)) • G ((List.ofFn p : List (Fin 1 ⊕ Fin 3)) + t)
```

## B. The Leibniz convolution

**`Lorentz.derivConv`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L177).

> The Leibniz convolution of two families of derivative symbols: the sum over the
> splittings of the multiset of the products of the two symbols.

```lean
noncomputable def derivConv (f g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : B
```

**`Lorentz.derivConv_cons`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L183).

> One derivative peeled off a convolution lands on one factor or the other.

```lean
lemma derivConv_cons (f g : Multiset (Fin 1 ⊕ Fin 3) → B) (a : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv f g (a ::ₘ s) =
      derivConv f (fun r => g (a ::ₘ r)) s + derivConv (fun r => f (a ::ₘ r)) g s
```

**`Lorentz.derivConv_sum_right`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L192).

> The convolution is linear in its right-hand family.

```lean
lemma derivConv_sum_right {ι : Type*} [Fintype ι] (f : Multiset (Fin 1 ⊕ Fin 3) → B)
    (c : ι → ℂ) (g : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv f (fun r => ∑ i, c i • g i r) s = ∑ i, c i • derivConv f (g i) s
```

**`Lorentz.derivConv_sum_left`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L199).

> The convolution is linear in its left-hand family.

```lean
lemma derivConv_sum_left {ι : Type*} [Fintype ι] (g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (c : ι → ℂ) (f : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv (fun r => ∑ i, c i • f i r) g s = ∑ i, c i • derivConv (f i) g s
```

**`Lorentz.lorentzMix_derivConv`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L207).

> The Lorentz mixing operator is a morphism for the Leibniz convolution: mixing the two
> factors separately and convolving is the same as convolving and then mixing.

```lean
lemma lorentzMix_derivConv (Λ : SL(2,ℂ)) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∀ (f g : Multiset (Fin 1 ⊕ Fin 3) → B),
      derivConv (fun x => lorentzMix Λ f x 0) (fun y => lorentzMix Λ g y 0) s =
        lorentzMix Λ (derivConv f g) s 0
```

**`Lorentz.repLorentz_derivConv`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L221).

> The Lorentz law of a Leibniz convolution: the mixing operator is a morphism for the
> convolution, so a convolution of two families with Lorentz laws has one too.

```lean
lemma repLorentz_derivConv {repLorentz : Representation ℂ SL(2,ℂ) B}
    (hmul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂)
    (Λ : SL(2,ℂ)) (f f' g g' : Multiset (Fin 1 ⊕ Fin 3) → B)
    (hf : ∀ x, repLorentz Λ (f x) = lorentzMix Λ f' x 0)
    (hg : ∀ y, repLorentz Λ (g y) = lorentzMix Λ g' y 0) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repLorentz Λ (derivConv f g s) = lorentzMix Λ (derivConv f' g') s 0
```

## C. The Lorentz law of a covariant tower

> A covariant tower is built one slot at a time: the tower along `l 0 :: l'` is the tower
> along `l'` with one more plain derivative, plus a correction `C (l 0)` applied to the tower
> along `l'`. The induction is run once, for an abstract tower with a Lorentz covariant
> correction that is linear in the family it corrects and lets a twist of the value index
> through.

**`Lorentz.repLorentz_tower`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean#L256).

> The Lorentz law of a covariant tower `T` built by the step `hstep` from a correction
> `C`, transforming into a tower `T'` built by the same step: the seed of `T` transforms
> into the seed of `T'` with the value index twisted by `τ` (`hzero`), and the correction is
> Lorentz covariant (`hC`), linear in the family it corrects (`hClin`) and lets the twist
> through (`hCτ`). Then the covariant slots mix by their own columns of the Lorentz matrix,
> the plain slots by `lorentzMix`, and the value index by `τ`.

```lean
lemma repLorentz_tower {K : Type} [Field K] {W : Type} [AddCommGroup W] [Module K W]
    [Module K B] [SMulCommClass K ℂ B] (Λ : SL(2,ℂ))
    (T T' : (n : ℕ) → (Fin n → (Fin 1 ⊕ Fin 3)) → Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B)
    (C : (Fin 1 ⊕ Fin 3) → (Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B) →
      Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B)
    (τ : W →ₗ[K] W)
    (hstep : ∀ (n : ℕ) (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)),
      T (n + 1) l s = T n (fun i => l i.succ) (l 0 ::ₘ s) + C (l 0) (T n fun i => l i.succ) s)
    (hstep' : ∀ (n : ℕ) (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)),
      T' (n + 1) l s = T' n (fun i => l i.succ) (l 0 ::ₘ s) + C (l 0) (T' n fun i => l i.succ) s)
    (hzero : ∀ (l : Fin 0 → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : W),
      repLorentz Λ (T 0 l s φ) = lorentzMix Λ (fun t => T' 0 l t (τ φ)) s 0)
    (hC : ∀ (ρ : Fin 1 ⊕ Fin 3) (G G' : Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B),
      (∀ y χ, repLorentz Λ (G y χ) = lorentzMix Λ (fun t => G' t χ) y 0) →
      ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : W), repLorentz Λ (C ρ G s φ) =
        ∑ a, L[Λ] a ρ • lorentzMix Λ (fun t => C a G' t φ) s 0)
    (hClin : ∀ (ρ : Fin 1 ⊕ Fin 3) {ι : Type} [Fintype ι] (c : ι → ℂ)
      (G : ι → Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B) (s : Multiset (Fin 1 ⊕ Fin 3))
      (φ : W), C ρ (fun t => ∑ i, c i • G i t) s φ = ∑ i, c i • C ρ (G i) s φ)
    (hCτ : ∀ (ρ : Fin 1 ⊕ Fin 3) (G : Multiset (Fin 1 ⊕ Fin 3) → W →ₗ[K] B)
      (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : W),
      C ρ (fun t => G t ∘ₗ τ) s φ = C ρ G s (τ φ)) :
    ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : W),
      repLorentz Λ (T n l s φ) =
        ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
          (∏ i, L[Λ] (p i) (l i)) • lorentzMix Λ (fun t => T' n p t (τ φ)) s 0
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../physlib/relativity/sl2c/basic.md)

## Proof depends on

- [Peeling the first slot off a sum over tuples](../mathematics/part-02/formathlib/fin.md)
- [Sums over the antidiagonal of a multiset](../mathematics/part-01/multisetantidiagonal.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzMix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzMix.lean)
