---
declaration: module
origin: cited
lean: StandardModel.lorentzMixStep, StandardModel.lorentzMix, StandardModel.lorentzMix_zero, StandardModel.lorentzMix_cons_apply, StandardModel.lorentzMix_apply_add, StandardModel.lorentzMix_cons_zero, StandardModel.lorentzMix_map, StandardModel.lorentzMix_smul_fam
statement: formalized
proof: formalized
---

# The covariant derivatives of a Standard Model

The module `PhyslibAlpha.Particles.StandardModel.Realization.CovariantDeriv`, [PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean): 111 declarations (1 instance with no name), 110 with a docstring.

## i. Overview

> The fields of a Standard Model are the bare derivative symbols `[∂_s A_μ^a]`, `[∂_s H^i]`
> and `[∂_s ψ^α]` of [`Basic.lean`](realization-basic.md), with the statistics proved in
> [`Commutations.lean`](realization-commutations.md). The whole jet gauge group acts on those — a gauge
> transformation together with all of its derivatives at the base point — and the
> transformation of a matter symbol carries an inhomogeneous term built from the gauge field.
> This file replaces them by the covariant towers `∇_l H`, `∇_l ψ` and `∇_l F_{μν}`, on which
> a gauge jet acts through its base point alone, and shows that nothing is lost in the
> exchange: the two sets of generators generate the same algebra.
>
> Sections A to E are the Lorentz machinery the towers need, stated for an arbitrary
> `GaugeAlgebraRealization`. A Lorentz transformation mixes each derivative slot of a symbol through a
> column of the Lorentz matrix; the bare symbols are indexed by multisets of directions, so
> that mixing is written as an operator `lorentzMix` on multiset-indexed families, a morphism
> for the Leibniz convolution out of which the correction terms of a covariant derivative are
> built. The Lorentz law of a covariant tower is then a single induction, `repLorentz_tower`,
> instantiated for the matter towers, where the value index carries the contragredient action
> and the gauge action has to commute with the Lorentz action, and for the field-strength
> tower, where the adjoint index carries no Lorentz weight.
>
> Sections F onwards work inside a Standard Model: the field algebra is the algebra generated
> by every symbol of the theory, the covariant towers are the iterated covariant derivatives
> of the twelve matter families and of the field strength, and `fieldAlgebra_eq_covDeriv` says
> that swapping the bare matter symbols for their towers, the gauge-field symbols being kept
> in both, does not change the algebra generated. The towers transform through the base point
> of a gauge jet alone and are fixed by a pure gauge jet — the facts
> `AlgebraRealization.CovFieldAlgebra.Basic` combines into the classification of jet-gauge
> invariants — and the last section records their Lorentz laws, which the covariant form of
> the theory consumes.

## ii. Key results

> - `StandardModel.lorentzMix` : the Lorentz mixing operator on multiset-indexed families of
>   derivative symbols, a morphism for the Leibniz convolution (`lorentzMix_derivConv`).
> - `StandardModel.repLorentz_tower` : the Lorentz law of an abstract covariant tower.
> - `GaugeAlgebraRealization.isLorentzCovDerivTransforms_covDerivIter` and
>   `GaugeAlgebraRealization.repLorentz_iteratedCovDerivAdjoint_fieldStrength` : the Lorentz
>   laws of the covariant matter towers and of the covariant field-strength tower.
> - `AlgebraRealization.fieldAlgebra` : the algebra the fields generate.
> - `AlgebraRealization.covDerivH`, `AlgebraRealization.covDerivFieldStrength` and their
>   companions : the covariant derivative towers.
> - `AlgebraRealization.fieldAlgebra_eq_covDeriv` : the covariant towers generate the field
>   algebra.
> - `AlgebraRealization.repLorentz_covDerivH` and its companions : the Lorentz laws of the
>   covariant matter towers.

## iv. References

> * None.

## A. The Lorentz mixing of derivative slots

> A Lorentz transformation mixes every derivative slot of a symbol through a column
> `L[Λ] · a` of the Lorentz matrix. For symbols indexed by an ordered tuple the mixing is a
> sum over tuples; the covariant derivative symbols carry multisets of directions, so the
> mixing is an operator on multiset-indexed families: peel one direction `a`, replace it by
> every direction `b` weighted by `L[Λ] b a`, and mix what is left. Peeling two directions
> commutes, so the recursion descends to multisets; `lorentzMix_ofFn` identifies the operator
> with the tuple form, and the remaining lemmas record that it is linear in the family.

**`StandardModel.lorentzMixStep`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L112).

> One peeling step of the Lorentz mixing: the direction `a` is removed from the multiset
> index of the family and put back as every direction `b`, weighted by `L[Λ] b a`.

```lean
noncomputable def lorentzMixStep (Λ : SL(2,ℂ)) (a : Fin 1 ⊕ Fin 3)
    (G : Multiset (Fin 1 ⊕ Fin 3) → M) : Multiset (Fin 1 ⊕ Fin 3) → M
```

**An instance with no name**, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L117).

> Peeling two directions commutes, so the mixing is well defined on a multiset.

```lean
instance (Λ : SL(2,ℂ)) : LeftCommutative (lorentzMixStep (M := M) Λ)
```

**`StandardModel.lorentzMix`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L128).

> The Lorentz mixing of a multiset-indexed family along a multiset `s` of directions:
> every direction of `s` is peeled and replaced by all directions, weighted by the
> corresponding column of the Lorentz matrix.

```lean
noncomputable def lorentzMix (Λ : SL(2,ℂ)) (G : Multiset (Fin 1 ⊕ Fin 3) → M)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Multiset (Fin 1 ⊕ Fin 3) → M
```

**`StandardModel.lorentzMix_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L135).

```lean
lemma lorentzMix_zero : lorentzMix Λ G 0 = G
```

**`StandardModel.lorentzMix_cons_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L138).

> Mixing along `a ::ₘ s` peels `a` after mixing along `s`.

```lean
lemma lorentzMix_cons_apply (a : Fin 1 ⊕ Fin 3) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (a ::ₘ s) t = ∑ b, L[Λ] b a • lorentzMix Λ G s (b ::ₘ t)
```

**`StandardModel.lorentzMix_apply_add`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L144).

> Evaluating a mixed family away from the empty multiset is mixing the translated
> family at the empty multiset.

```lean
lemma lorentzMix_apply_add (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∀ (G : Multiset (Fin 1 ⊕ Fin 3) → M) (t : Multiset (Fin 1 ⊕ Fin 3)),
      lorentzMix Λ G s t = lorentzMix Λ (fun r => G (r + t)) s 0
```

**`StandardModel.lorentzMix_cons_zero`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L155).

> Peeling at the empty multiset: the peeled direction is pushed into the family.

```lean
lemma lorentzMix_cons_zero (a : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (a ::ₘ s) 0 = ∑ b, L[Λ] b a • lorentzMix Λ (fun t => G (b ::ₘ t)) s 0
```

**`StandardModel.lorentzMix_map`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L160).

> The mixing operator commutes with any linear map applied to the values.

```lean
lemma lorentzMix_map (Φ : M →ₗ[ℂ] N) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    Φ (lorentzMix Λ G s t) = lorentzMix Λ (fun r => Φ (G r)) s t
```

**`StandardModel.lorentzMix_smul_fam`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L167).

> The mixing operator is homogeneous in the family.

```lean
lemma lorentzMix_smul_fam (c : ℂ) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => c • G r) s t = c • lorentzMix Λ G s t
```

**`StandardModel.lorentzMix_add_fam`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L172).

> The mixing operator is additive in the family.

```lean
lemma lorentzMix_add_fam (G₁ G₂ : Multiset (Fin 1 ⊕ Fin 3) → M) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => G₁ r + G₂ r) s t = lorentzMix Λ G₁ s t + lorentzMix Λ G₂ s t
```

**`StandardModel.lorentzMix_sum_fam`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L180).

> The mixing operator commutes with finite sums of families.

```lean
lemma lorentzMix_sum_fam {ι : Type*} [Fintype ι] (H : ι → Multiset (Fin 1 ⊕ Fin 3) → M)
    (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => ∑ i, H i r) s t = ∑ i, lorentzMix Λ (H i) s t
```

**`StandardModel.sum_fin_succ_prod_smul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L191).

> A sum over tuples of directions, with one Lorentz matrix factor per slot, split into
> its first slot and the remaining ones.

```lean
lemma sum_fin_succ_prod_smul {n : ℕ} (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3))
    (X : (Fin (n + 1) → (Fin 1 ⊕ Fin 3)) → M) :
    ∑ q : Fin (n + 1) → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (q i) (l i)) • X q =
      ∑ b, ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (L[Λ] b (l 0) * ∏ i, L[Λ] (p i) (l i.succ)) • X (Fin.cons b p)
```

**`StandardModel.lorentzMix_ofFn`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L201).

> The mixing operator agrees with the tuple form of the Lorentz law: along an ordered
> tuple of directions it is the sum over all tuples with one Lorentz matrix factor per
> slot.

```lean
lemma lorentzMix_ofFn {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ G (List.ofFn l) t =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, L[Λ] (p i) (l i)) • G ((List.ofFn p : List (Fin 1 ⊕ Fin 3)) + t)
```

**`StandardModel.lorentzMix_neg_fam`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L222).

> The mixing operator commutes with negation of the family.

```lean
lemma lorentzMix_neg_fam (G : Multiset (Fin 1 ⊕ Fin 3) → M) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => -G r) s t = -lorentzMix Λ G s t
```

**`StandardModel.lorentzMix_sub_fam`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L227).

> The mixing operator is additive in the family, in subtracted form.

```lean
lemma lorentzMix_sub_fam (G₁ G₂ : Multiset (Fin 1 ⊕ Fin 3) → M) (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    lorentzMix Λ (fun r => G₁ r - G₂ r) s t = lorentzMix Λ G₁ s t - lorentzMix Λ G₂ s t
```

## B. The Leibniz convolution

> The correction terms of a covariant derivative are Leibniz convolutions over the multiset
> antidiagonal: a gauge-field symbol carrying `x` derivatives against a matter symbol
> carrying `y`, summed over all splittings `s = x + y`. Expanded in bases, both correction
> terms of this file are scalar combinations of such convolutions of plain products in `B`,
> which is why `lorentzMix_derivConv` — the mixing operator is a morphism for the
> convolution — is what carries a Lorentz law through a covariant derivative.

**`StandardModel.multiset_sum_map_sum`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L252).

> A finite sum inside a multiset sum may be taken outside.

```lean
lemma multiset_sum_map_sum {α ι : Type*} [Fintype ι] (m : Multiset α) (F : ι → α → B) :
    (m.map fun x => ∑ i, F i x).sum = ∑ i, (m.map (F i)).sum
```

**`StandardModel.derivConv`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L260).

> The Leibniz convolution of two families of derivative symbols: the sum over the
> splittings of the multiset of the products of the two symbols.

```lean
noncomputable def derivConv (f g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : B
```

**`StandardModel.derivConv_cons`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L266).

> One derivative peeled off a convolution lands on one factor or the other.

```lean
lemma derivConv_cons (f g : Multiset (Fin 1 ⊕ Fin 3) → B) (a : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv f g (a ::ₘ s) =
      derivConv f (fun r => g (a ::ₘ r)) s + derivConv (fun r => f (a ::ₘ r)) g s
```

**`StandardModel.derivConv_sum_right`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L275).

> The convolution is linear in its right-hand family.

```lean
lemma derivConv_sum_right {ι : Type*} [Fintype ι] (f : Multiset (Fin 1 ⊕ Fin 3) → B)
    (c : ι → ℂ) (g : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv f (fun r => ∑ i, c i • g i r) s = ∑ i, c i • derivConv f (g i) s
```

**`StandardModel.derivConv_sum_left`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L282).

> The convolution is linear in its left-hand family.

```lean
lemma derivConv_sum_left {ι : Type*} [Fintype ι] (g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (c : ι → ℂ) (f : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivConv (fun r => ∑ i, c i • f i r) g s = ∑ i, c i • derivConv (f i) g s
```

**`StandardModel.lorentzMix_derivConv`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L290).

> The Lorentz mixing operator is a morphism for the Leibniz convolution: mixing the two
> factors separately and convolving is the same as convolving and then mixing.

```lean
lemma lorentzMix_derivConv (Λ : SL(2,ℂ)) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∀ (f g : Multiset (Fin 1 ⊕ Fin 3) → B),
      derivConv (fun x => lorentzMix Λ f x 0) (fun y => lorentzMix Λ g y 0) s =
        lorentzMix Λ (derivConv f g) s 0
```

## C. The Lorentz law of a covariant tower

> A covariant tower is built one slot at a time: the tower along `l 0 :: l'` is the tower
> along `l'` with one more plain derivative, plus a correction term `C (l 0)` applied to the
> tower along `l'`. Both towers of this file have that shape, with the derived action of the
> gauge field or the derived bracket as correction, and both corrections are Lorentz
> covariant, linear in the family they correct, and compatible with a twist of the value
> index. That is all the induction uses, so it is run once, for an abstract tower `T`
> transforming into a possibly different tower `T'`: the covariant slots mix by their own
> columns of the Lorentz matrix, the plain slots by `lorentzMix`, and the value index by `τ`.

**`StandardModel.repLorentz_derivConv`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L325).

> The Lorentz law of a Leibniz convolution: the mixing operator is a morphism for the
> convolution, so a convolution of two families with Lorentz laws has one too.

```lean
lemma repLorentz_derivConv
    (hmul : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B), repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂)
    (Λ : SL(2,ℂ)) (f f' g g' : Multiset (Fin 1 ⊕ Fin 3) → B)
    (hf : ∀ x, repLorentz Λ (f x) = lorentzMix Λ f' x 0)
    (hg : ∀ y, repLorentz Λ (g y) = lorentzMix Λ g' y 0) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repLorentz Λ (derivConv f g s) = lorentzMix Λ (derivConv f' g') s 0
```

**`StandardModel.repLorentz_tower`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L341).

> The Lorentz law of a covariant tower. The tower `T` is built by the step `hstep` out of
> a correction `C`, and so is the tower `T'` it transforms into; the seed of `T` transforms
> into the seed of `T'` with the value index twisted by `τ` (`hzero`); and the correction is
> Lorentz covariant (`hC`), linear in the family it corrects (`hClin`), and lets the twist
> through (`hCτ`). Then the covariant slots mix by their own columns, the plain slots by
> `lorentzMix`, and the value index by `τ`.

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

## D. The covariant tower of a matter family

> The covariant derivative of a matter family adds one ordered derivative slot and a Leibniz
> correction `A_ρ · F`, the derived action of the gauge field on the value index through the
> infinitesimal action `act`. Expanded in bases, the correction is a scalar combination of
> Leibniz convolutions of gauge-field symbols against matter symbols, which gives its Lorentz
> law and its linearity in the matter family. The twist of the value index is the
> contragredient action `rep.dual Λ`, and it passes through the correction because the gauge
> action commutes with the Lorentz action on the value space: that is the one hypothesis
> about the species that the Lorentz law needs, and conjugation transports it to the
> conjugate families.

**`StandardModel.GaugeAlgebraRealization.sum_comm₃`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L426).

> Rotating a triple sum so that the innermost index comes first.

```lean
lemma sum_comm₃ {α β γ M : Type*} [Fintype α] [Fintype β] [Fintype γ] [AddCommMonoid M]
    (X : α → β → γ → M) : (∑ a, ∑ b, ∑ c, X a b c) = ∑ c, ∑ a, ∑ b, X a b c
```

**`StandardModel.GaugeAlgebraRealization.sum_derivConv_sum_fam`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L432).

> A scalar combination of convolutions against the gauge field is linear in the
> right-hand families.

```lean
lemma sum_derivConv_sum_fam {ι κ ι' : Type} [Fintype ι] [Fintype κ] [Fintype ι']
    (f : ι → Multiset (Fin 1 ⊕ Fin 3) → B) (coef : ι → κ → ℂ) (c : ι' → ℂ)
    (g : ι' → κ → Multiset (Fin 1 ⊕ Fin 3) → B) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∑ j, ∑ k, coef j k • derivConv (f j) (fun y => ∑ i, c i • g i k y) s =
      ∑ i, c i • ∑ j, ∑ k, coef j k • derivConv (f j) (g i k) s
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_eq_lorentzMix`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L442).

> A Lorentz law in the tuple form, read on the underlying multisets: the transformed
> family mixes by `lorentzMix`.

```lean
lemma repLorentz_eq_lorentzMix (Λ : SL(2,ℂ)) (f g : Multiset (Fin 1 ⊕ Fin 3) → B)
    (hfg : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)), repLorentz Λ (f (List.ofFn l)) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) • g (List.ofFn p))
    (x : Multiset (Fin 1 ⊕ Fin 3)) : repLorentz Λ (f x) = lorentzMix Λ g x 0
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_apply_mix`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L452).

> The Lorentz law of the gauge-field symbols, in the multiset form.

```lean
lemma repLorentz_apply_mix (Λ : SL(2,ℂ))
    (x : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (χ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (h.A x μ χ) = lorentzMix Λ (fun t => ∑ a, L[Λ] a μ • h.A t a χ) x 0
```

**`StandardModel.GaugeAlgebraRealization.isLorentzDerivTransforms_mix`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L460).

> The Lorentz law of a family of derivative symbols, in the multiset form.

```lean
lemma isLorentzDerivTransforms_mix {rep : Representation ℂ SL(2,ℂ) V}
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : IsLorentzDerivTransforms repLorentz rep F) (Λ : SL(2,ℂ))
    (x : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V) :
    repLorentz Λ (F x χ) = lorentzMix Λ (fun t => F t (rep.dual Λ χ)) x 0
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_sum_derivConv`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L471).

> The Lorentz law of a scalar combination of convolutions against the gauge field: the
> direction of the gauge field mixes by its own column, the derivative slots by
> `lorentzMix`, and the right-hand families are replaced by their transforms.

```lean
lemma repLorentz_sum_derivConv (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    {ι κ : Type} [Fintype ι] [Fintype κ] (bg : Module.Basis ι ℝ GaugeAlgebra) (coef : ι → κ → ℂ)
    (g g' : κ → Multiset (Fin 1 ⊕ Fin 3) → B)
    (hg : ∀ k y, repLorentz Λ (g k y) = lorentzMix Λ (g' k) y 0) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repLorentz Λ (∑ j, ∑ k, coef j k • derivConv (fun x => h.A x ρ (bg.coord j)) (g k) s) =
      ∑ a, L[Λ] a ρ • lorentzMix Λ
        (fun t => ∑ j, ∑ k, coef j k • derivConv (fun x => h.A x a (bg.coord j)) (g' k) t) s 0
```

**`StandardModel.GaugeAlgebraRealization.actionFam_apply_eq_sum`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L491).

> The action of families expanded in bases of the gauge algebra and the value space.

```lean
lemma actionFam_apply_eq_sum {ι κ : Type} [Fintype ι] [Fintype κ]
    (bg : Module.Basis ι ℝ GaugeAlgebra) (bv : Module.Basis κ ℂ V)
    (f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B)
    (φ : Module.Dual ℂ V) :
    actionFam act f g φ =
      ∑ j, ∑ k, φ (act (bg j) (bv k)) • (f (bg.coord j) * g (bv.coord k))
```

**`StandardModel.GaugeAlgebraRealization.actionFamConv_eq_sum`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L502).

> The derived action family expanded in bases.

```lean
lemma actionFamConv_eq_sum {ι κ : Type} [Fintype ι] [Fintype κ]
    (bg : Module.Basis ι ℝ GaugeAlgebra) (bv : Module.Basis κ ℂ V)
    (ρ : Fin 1 ⊕ Fin 3) (G : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ G s φ = ∑ j, ∑ k, φ (act (bg j) (bv k)) •
      derivConv (fun x => A x ρ (bg.coord j)) (fun y => G y (bv.coord k)) s
```

**`StandardModel.GaugeAlgebraRealization.actionFamConv_sum_fam`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L512).

> The derived action family is linear in the matter family.

```lean
lemma actionFamConv_sum_fam {ι : Type} [Fintype ι] (ρ : Fin 1 ⊕ Fin 3) (c : ι → ℂ)
    (H : ι → Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ (fun t => ∑ i, c i • H i t) s φ =
      ∑ i, c i • actionFamConv A act ρ (H i) s φ
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_actionFamConv`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L525).

> The Lorentz law of the derived action family: the derivative slots mix, the direction
> of the gauge field mixes by its own column, and the value index is carried by the
> transformed matter family.

```lean
lemma repLorentz_actionFamConv (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (G G' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hG : ∀ y χ, repLorentz Λ (G y χ) = lorentzMix Λ (fun t => G' t χ) y 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    repLorentz Λ (actionFamConv h.A act ρ G s φ) =
      ∑ a, L[Λ] a ρ • lorentzMix Λ (fun t => actionFamConv h.A act a G' t φ) s 0
```

**`StandardModel.GaugeAlgebraRealization.dual_twist`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L541).

> The twist of the value index past the gauge action: an endomorphism commuting with
> the gauge action may be moved from the dual basis onto the dual vector.

```lean
lemma dual_twist {κ : Type} [Fintype κ] (bv : Module.Basis κ ℂ V) (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : GaugeAlgebra) (v : V), act c (T v) = T (act c v))
    (ψ : Module.Dual ℂ V →ₗ[ℂ] B) (c : GaugeAlgebra) (φ : Module.Dual ℂ V) :
    ∑ k, φ (act c (bv k)) • ψ (T.dualMap (bv.coord k)) =
      ∑ k, (T.dualMap φ) (act c (bv k)) • ψ (bv.coord k)
```

**`StandardModel.GaugeAlgebraRealization.actionFam_comp_dual`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L555).

> The contragredient action may be pulled out of an action of families, provided the
> gauge action commutes with it on the value space.

```lean
lemma actionFam_comp_dual (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : GaugeAlgebra) (v : V), act c (T v) = T (act c v))
    (f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B)
    (φ : Module.Dual ℂ V) :
    actionFam act f (g ∘ₗ T.dualMap) φ = actionFam act f g (T.dualMap φ)
```

**`StandardModel.GaugeAlgebraRealization.actionFamConv_comp_dual`**, a lemma, [line 565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L565).

> The contragredient action may be pulled out of a derived action family.

```lean
lemma actionFamConv_comp_dual (T : V →ₗ[ℂ] V)
    (hT : ∀ (c : GaugeAlgebra) (v : V), act c (T v) = T (act c v)) (ρ : Fin 1 ⊕ Fin 3)
    (K : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    actionFamConv A act ρ (fun t => K t ∘ₗ T.dualMap) s φ =
      actionFamConv A act ρ K s (T.dualMap φ)
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_covDerivIter`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L577).

> The Lorentz law of the iterated covariant derivative of a matter family: the ordered
> covariant slots mix by their own columns and the multiset of plain derivative slots
> mixes by `lorentzMix`, while the value index transforms contragrediently.

```lean
lemma repLorentz_covDerivIter {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep F) (Λ : SL(2,ℂ))
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    repLorentz Λ (covDerivIter h.A act F n l s φ) = ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
      (∏ i, L[Λ] (p i) (l i)) •
        lorentzMix Λ (fun t => covDerivIter h.A act F n p t (rep.dual Λ φ)) s 0
```

**`StandardModel.GaugeAlgebraRealization.isLorentzCovDerivTransforms_covDerivIter`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L597).

> The iterated covariant derivative of a matter family transforms as the covariant
> derivatives of a Lorentz-covariant field, given the Lorentz law of the bare symbols,
> the Lorentz law of the gauge field, and the commutation of the infinitesimal gauge
> action with the Lorentz action on the value space.

```lean
lemma isLorentzCovDerivTransforms_covDerivIter {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep F) :
    IsLorentzCovDerivTransforms repLorentz rep (fun {n} l => covDerivIter h.A act F n l 0)
```

**`StandardModel.GaugeAlgebraRealization.actionConj_comm_repConj`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L609).

> Conjugation preserves the commutation of the gauge action with the Lorentz action:
> both are read on the conjugate module through the same underlying maps.

```lean
lemma actionConj_comm_repConj (rep : Representation ℂ SL(2,ℂ) V)
    (hcomm : ∀ (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : ConjModule V) :
    LocalGaugeData.actionConj act c (rep.conj Λ v) =
      rep.conj Λ (LocalGaugeData.actionConj act c v)
```

**`StandardModel.GaugeAlgebraRealization.isLorentzCovDerivTransforms_covDerivIter_conj`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L618).

> The Lorentz law of the covariant tower of a conjugate family, from the commutation of
> the gauge action with the Lorentz action of the unconjugated species.

```lean
lemma isLorentzCovDerivTransforms_covDerivIter_conj {rep : Representation ℂ SL(2,ℂ) V}
    (hcomm : ∀ (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : V), act c (rep Λ v) = rep Λ (act c v))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ (ConjModule V) →ₗ[ℂ] B)
    (hF : IsLorentzDerivTransforms repLorentz rep.conj F) :
    IsLorentzCovDerivTransforms repLorentz rep.conj
      (fun {n} l => covDerivIter h.A (LocalGaugeData.actionConj act) F n l 0)
```

## E. The covariant tower of the field strength

> The covariant derivative of an adjoint family has the shape of that of a matter family,
> with the bracket `⁅A_ρ, ·⁆` in place of the action on the value index; the gauge index
> carries no Lorentz weight, so the twist is the identity, and the induction of section C
> applies with `bracketFamConv` in place of `actionFamConv`. What is new is the seed: the
> field strength carries two covector indices, and its Lorentz law
> (`repLorentz_fieldStrength_mix`) mixes both. The tower is linear in its seed, so it
> inherits the antisymmetry of the field strength.

**`StandardModel.GaugeAlgebraRealization.bracketFamConv_eq_sum`**, a lemma, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L641).

> The derived bracket family expanded in a basis of the gauge algebra.

```lean
lemma bracketFamConv_eq_sum (ρ : Fin 1 ⊕ Fin 3)
    (G : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    bracketFamConv A ρ G s φ =
      ∑ j, ∑ k, ((φ ⁅Module.Free.chooseBasis ℝ GaugeAlgebra j,
            Module.Free.chooseBasis ℝ GaugeAlgebra k⁆ : ℝ) : ℂ) •
        derivConv (fun x => A x ρ ((Module.Free.chooseBasis ℝ GaugeAlgebra).coord j))
          (fun y => G y ((Module.Free.chooseBasis ℝ GaugeAlgebra).coord k)) s
```

**`StandardModel.GaugeAlgebraRealization.bracketFamConv_sum_fam`**, a lemma, [line 654](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L654).

> The derived bracket family is linear in the second family.

```lean
lemma bracketFamConv_sum_fam {ι : Type} [Fintype ι] (ρ : Fin 1 ⊕ Fin 3) (c : ι → ℂ)
    (H : ι → Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    bracketFamConv A ρ (fun t => ∑ i, c i • H i t) s φ =
      ∑ i, c i • bracketFamConv A ρ (H i) s φ
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_bracketFamConv`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L663).

> The Lorentz law of the derived bracket family.

```lean
lemma repLorentz_bracketFamConv (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (G G' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (hG : ∀ y χ, repLorentz Λ (G y χ) = lorentzMix Λ (fun t => G' t χ) y 0)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (bracketFamConv h.A ρ G s φ) =
      ∑ a, L[Λ] a ρ • lorentzMix Λ (fun t => bracketFamConv h.A a G' t φ) s 0
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_iteratedCovDerivAdjoint`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L676).

> The Lorentz law of the iterated covariant derivative in the adjoint: the covariant
> slots mix by their own columns and the seed family is replaced by its transform.

```lean
lemma repLorentz_iteratedCovDerivAdjoint (Λ : SL(2,ℂ))
    (F F' : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (hF : ∀ x χ, repLorentz Λ (F x χ) = lorentzMix Λ (fun t => F' t χ) x 0)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (x : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (iteratedCovDerivAdjoint h.A (List.ofFn l) F x φ) = ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
      (∏ i, L[Λ] (p i) (l i)) •
        lorentzMix Λ (fun t => iteratedCovDerivAdjoint h.A (List.ofFn p) F' t φ) x 0
```

**`StandardModel.GaugeAlgebraRealization.iteratedCovDerivAdjoint_sum_fam`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L693).

> The iterated covariant derivative in the adjoint is linear in the seed family.

```lean
lemma iteratedCovDerivAdjoint_sum_fam {ι : Type} [Fintype ι] (c : ι → ℂ)
    (H : ι → Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) :
    ∀ (l : List (Fin 1 ⊕ Fin 3)) (x : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra),
      iteratedCovDerivAdjoint A l (fun t => ∑ i, c i • H i t) x φ =
        ∑ i, c i • iteratedCovDerivAdjoint A l (H i) x φ
```

**`StandardModel.GaugeAlgebraRealization.iteratedCovDerivAdjoint_neg_fam`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L710).

> The iterated covariant derivative is odd in the family it differentiates: the case of
> a one-element index in `iteratedCovDerivAdjoint_sum_fam`.

```lean
lemma iteratedCovDerivAdjoint_neg_fam
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (l : List (Fin 1 ⊕ Fin 3)) (x : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    iteratedCovDerivAdjoint A l (fun t => - F t) x φ = - iteratedCovDerivAdjoint A l F x φ
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_fieldStrength_mix`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L719).

> The Lorentz law of the field strength: both covector indices mix by their columns,
> and the derivative slots mix by `lorentzMix`.

```lean
lemma repLorentz_fieldStrength_mix (Λ : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3)
    (x : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (fieldStrength h.A μ ν x φ) =
      lorentzMix Λ (fun t => ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • fieldStrength h.A a b t φ) x 0
```

**`StandardModel.GaugeAlgebraRealization.repLorentz_iteratedCovDerivAdjoint_fieldStrength`**, a lemma, [line 755](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L755).

> The Lorentz law of the covariant tower of the field strength: the covariant slots
> mix by their own columns and the two covector indices of the field strength mix by
> theirs.

```lean
lemma repLorentz_iteratedCovDerivAdjoint_fieldStrength (Λ : SL(2,ℂ)) (n : ℕ)
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (iteratedCovDerivAdjoint h.A (List.ofFn l) (fieldStrength h.A μ ν) 0 φ) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) • ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν •
        iteratedCovDerivAdjoint h.A (List.ofFn p) (fieldStrength h.A a b) 0 φ
```

## F. What a covariant tower inherits from its family

> Facts about the covariant tower of a single matter family, in the form the field algebra
> consumes. The span lemma
> `GaugeAlgebraRealization.adjoin_symbols_eq_adjoin_covDerivIter` says that the
> bare symbols and the tower generate the same algebra over the gauge-field symbols, so each
> is a polynomial in the other; the tower commutes with the gauge-field symbols as soon as
> the bare symbols do; and a pure gauge jet acts trivially through the dual base-point
> coefficient of a representation whose zeroth Taylor coefficient it fixes.

**`StandardModel.GaugeAlgebraRealization.symbol_mem_adjoin`**, a lemma, [line 795](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L795).

> A bare matter symbol is a polynomial in the gauge-field symbols and the covariant
> tower of its family.

```lean
lemma symbol_mem_adjoin {X : Set B} (hA : ∀ s μ ψ, A s μ ψ ∈ X)
    (hF : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, covDerivIter A act F n l 0 φ ∈ X)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) : F s φ ∈ Algebra.adjoin ℂ X
```

**`StandardModel.GaugeAlgebraRealization.covDerivIter_mem_adjoin`**, a lemma, [line 805](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L805).

> A symbol of a covariant tower is a polynomial in the gauge-field symbols and the bare
> symbols of its family.

```lean
lemma covDerivIter_mem_adjoin {X : Set B} (hA : ∀ s μ ψ, A s μ ψ ∈ X)
    (hF : ∀ s φ, F s φ ∈ X) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l 0 φ ∈ Algebra.adjoin ℂ X
```

**`StandardModel.GaugeAlgebraRealization.commute_covDerivIter`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L814).

> A symbol of a covariant tower commutes with the gauge-field symbols, as soon as the
> bare symbols of its family do.

```lean
lemma commute_covDerivIter
    (hAA : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
      (ψ ψ' : Module.Dual ℝ GaugeAlgebra), Commute (A s μ ψ) (A s' μ' ψ'))
    (hAF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra)
      (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V), Commute (A s μ ψ) (F s' φ))
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra) :
    Commute (covDerivIter A act F n l 0 φ) (A p μ ψ)
```

**`StandardModel.GaugeAlgebraRealization.repDualCoeff_zero_of_mem_truncationKer_zero`**, a lemma, [line 829](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L829).

> A pure gauge jet acts trivially through the dual base-point coefficient of a
> representation whose zeroth Taylor coefficient is the identity on pure jets.

```lean
lemma repDualCoeff_zero_of_mem_truncationKer_zero
    {rep : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    (hrep : ∀ {W : JetGaugeGroupI}, localGaugeData.eval W = 1 → repCoeff rep W 0 = LinearMap.id)
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ V) :
    repDualCoeff rep U.1⁻¹ 0 φ = φ
```

## G. The field algebra and the covariant towers

> The field algebra is the algebra generated by every derivative symbol of the theory. The
> covariant towers are the iterated covariant derivatives of the twelve matter families along
> ordered tuples of directions, evaluated at the empty multiset, each built with the
> infinitesimal action of its species (`actionConj` of it for a conjugate family), together
> with the iterated covariant derivative of the field strength along a list of directions.
> The set `matterTowers` collects the matter towers, and `matterTowers_induction` is the case
> split over them that the rest of the file runs.

**`StandardModel.AlgebraRealization.symbols`**, a def, [line 869](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L869).

> The generators of the field algebra: every derivative symbol of the gauge field, of
> the Higgs and its conjugate, and of the three generations of each fermion species and
> their conjugates.

```lean
def symbols : Set B
```

**`StandardModel.AlgebraRealization.fieldAlgebra`**, a def, [line 882](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L882).

> The algebra generated by all the fields of the Standard Model and their derivative
> symbols: the gauge field, the Higgs and its conjugate, and the three families of each
> fermion species with their conjugates.

```lean
def fieldAlgebra : Subalgebra ℂ B
```

**`StandardModel.AlgebraRealization.covDerivH`**, a def, [line 885](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L885).

> The iterated covariant derivative of the Higgs field.

```lean
noncomputable def covDerivH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ HiggsVec →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarH`**, a def, [line 890](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L890).

> The iterated covariant derivative of the conjugate Higgs field.

```lean
noncomputable def covDerivBarH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule HiggsVec) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivD`**, a def, [line 895](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L895).

> The iterated covariant derivative of the down-type quarks.

```lean
noncomputable def covDerivD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ DownSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarD`**, a def, [line 900](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L900).

> The iterated covariant derivative of the conjugate down-type quarks.

```lean
noncomputable def covDerivBarD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule DownSinglet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivU`**, a def, [line 905](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L905).

> The iterated covariant derivative of the up-type quarks.

```lean
noncomputable def covDerivU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ UpSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarU`**, a def, [line 910](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L910).

> The iterated covariant derivative of the conjugate up-type quarks.

```lean
noncomputable def covDerivBarU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule UpSinglet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivQ`**, a def, [line 915](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L915).

> The iterated covariant derivative of the quark doublets.

```lean
noncomputable def covDerivQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ QuarkDoublet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarQ`**, a def, [line 920](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L920).

> The iterated covariant derivative of the conjugate quark doublets.

```lean
noncomputable def covDerivBarQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule QuarkDoublet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivL`**, a def, [line 925](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L925).

> The iterated covariant derivative of the lepton doublets.

```lean
noncomputable def covDerivL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonDoubletV →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarL`**, a def, [line 930](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L930).

> The iterated covariant derivative of the conjugate lepton doublets.

```lean
noncomputable def covDerivBarL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonDoubletV) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivE`**, a def, [line 935](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L935).

> The iterated covariant derivative of the lepton singlets.

```lean
noncomputable def covDerivE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ LeptonSinglet →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivBarE`**, a def, [line 940](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L940).

> The iterated covariant derivative of the conjugate lepton singlets.

```lean
noncomputable def covDerivBarE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule LeptonSinglet) →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.covDerivFieldStrength`**, a def, [line 946](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L946).

> The iterated covariant derivative `∇_{l₁} ⋯ ∇_{lₙ} F_{μν}` of the field strength of the
> gauge field, along an ordered list of directions.

```lean
noncomputable def covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B
```

**`StandardModel.AlgebraRealization.matterTowers`**, a def, [line 951](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L951).

> The covariant towers of the twelve matter families: every symbol of every tower.

```lean
def matterTowers : Set B
```

**`StandardModel.AlgebraRealization.matterTowers_induction`**, a lemma, [line 962](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L962).

> A property of every symbol of every matter tower is proved tower by tower.

```lean
lemma matterTowers_induction (P : B → Prop) {b : B} (hb : b ∈ h.matterTowers)
    (hH : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivH l φ))
    (hbarH : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarH l φ))
    (hd : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivD i l φ))
    (hbard : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarD i l φ))
    (hu : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivU i l φ))
    (hbaru : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarU i l φ))
    (hQ : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivQ i l φ))
    (hbarQ : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarQ i l φ))
    (hL : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivL i l φ))
    (hbarL : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarL i l φ))
    (he : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivE i l φ))
    (hbare : ∀ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, P (h.covDerivBarE i l φ)) :
    P b
```

## H. The covariant towers generate the field algebra

> The span lemma of section F, for the twelve families at once: each bare symbol is a
> polynomial in the gauge-field symbols and its own tower, and each tower symbol is a
> polynomial in the gauge-field symbols and its own bare symbols.

**`StandardModel.AlgebraRealization.symbols_subset_adjoin_matterTowers`**, a lemma, [line 998](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L998).

> Every bare symbol is a polynomial in the gauge-field symbols and the matter towers.

```lean
lemma symbols_subset_adjoin_matterTowers :
    h.symbols ⊆ Algebra.adjoin ℂ
      ((⋃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3), Set.range (h.A s μ)) ∪
        h.matterTowers)
```

**`StandardModel.AlgebraRealization.fieldAlgebra_eq_covDeriv`**, a lemma, [line 1053](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1053).

> The covariant towers generate the field algebra: replacing the plain derivative
> symbols of every matter field by their covariant derivative towers does not change the
> generated algebra; only the gauge-field symbols remain plain.

```lean
lemma fieldAlgebra_eq_covDeriv :
    h.fieldAlgebra = Algebra.adjoin ℂ
    ((⋃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3), Set.range (h.A s μ)) ∪
      (⋃ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)),
        Set.range (h.covDerivH l) ∪ Set.range (h.covDerivBarH l)) ∪
      (⋃ (i : Fin 3) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)),
        Set.range (h.covDerivD i l) ∪ Set.range (h.covDerivBarD i l) ∪
        Set.range (h.covDerivU i l) ∪ Set.range (h.covDerivBarU i l) ∪
        Set.range (h.covDerivQ i l) ∪ Set.range (h.covDerivBarQ i l) ∪
        Set.range (h.covDerivL i l) ∪ Set.range (h.covDerivBarL i l) ∪
        Set.range (h.covDerivE i l) ∪ Set.range (h.covDerivBarE i l)))
```

## I. Gauge covariance of the covariant towers

> Each matter tower transforms in the representation of its species, by
> `TransformsIn.covDerivIter`, and the field-strength tower in the adjoint. At the base point
> that is the action of the base-point value of the gauge jet alone (`repJet_covDerivIter`),
> and a pure gauge jet — one with trivial base-point value — fixes every tower. The section
> instantiates this species by species, the conjugate families through the conjugate action
> and representation.

**`StandardModel.AlgebraRealization.repJet_covDerivIter`**, a lemma, [line 1097](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1097).

> The covariant tower of a matter family transforms through the base point of a gauge
> jet alone, given the gauge law of the family and the infinitesimal action of its
> species.

```lean
lemma repJet_covDerivIter {V : Type} [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V]
    {rep : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
        {act : GaugeAlgebra →ₗ[ℝ] V →ₗ[ℂ] V}
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B} (hF : TransformsIn repJet rep F)
    (hact : localGaugeData.IsInfinitesimalActionOf act rep) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI) (φ : Module.Dual ℂ V) :
    repJet U (covDerivIter h.A act F n l 0 φ) =
      covDerivIter h.A act F n l 0 (repDualCoeff rep U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivH`**, a lemma, [line 1108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1108).

> The Higgs tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ HiggsVec) : repJet U (h.covDerivH l φ) =
      h.covDerivH l (repDualCoeff HiggsVec.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarH`**, a lemma, [line 1114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1114).

> The conjugate Higgs tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarH {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) : repJet U (h.covDerivBarH l φ) =
      h.covDerivBarH l (repDualCoeff (repConj HiggsVec.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivD`**, a lemma, [line 1120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1120).

> The down-type quark tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ DownSinglet) : repJet U (h.covDerivD i l φ) =
      h.covDerivD i l (repDualCoeff DownSinglet.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarD`**, a lemma, [line 1126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1126).

> The conjugate down-type quark tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarD (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) : repJet U (h.covDerivBarD i l φ) =
      h.covDerivBarD i l (repDualCoeff (repConj DownSinglet.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivU`**, a lemma, [line 1132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1132).

> The up-type quark tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ UpSinglet) : repJet U (h.covDerivU i l φ) =
      h.covDerivU i l (repDualCoeff UpSinglet.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarU`**, a lemma, [line 1138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1138).

> The conjugate up-type quark tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarU (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) : repJet U (h.covDerivBarU i l φ) =
      h.covDerivBarU i l (repDualCoeff (repConj UpSinglet.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivQ`**, a lemma, [line 1144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1144).

> The quark doublet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ QuarkDoublet) : repJet U (h.covDerivQ i l φ) =
      h.covDerivQ i l (repDualCoeff QuarkDoublet.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarQ`**, a lemma, [line 1150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1150).

> The conjugate quark doublet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarQ (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) : repJet U (h.covDerivBarQ i l φ) =
      h.covDerivBarQ i l (repDualCoeff (repConj QuarkDoublet.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivL`**, a lemma, [line 1156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1156).

> The lepton doublet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ LeptonDoubletV) : repJet U (h.covDerivL i l φ) =
      h.covDerivL i l (repDualCoeff LeptonDoubletV.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarL`**, a lemma, [line 1162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1162).

> The conjugate lepton doublet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarL (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) : repJet U (h.covDerivBarL i l φ) =
      h.covDerivBarL i l (repDualCoeff (repConj LeptonDoubletV.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivE`**, a lemma, [line 1168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1168).

> The lepton singlet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ LeptonSinglet) : repJet U (h.covDerivE i l φ) =
      h.covDerivE i l (repDualCoeff LeptonSinglet.repJetGaugeGroupI U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarE`**, a lemma, [line 1174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1174).

> The conjugate lepton singlet tower transforms through the base point of a gauge jet.

```lean
lemma repJet_covDerivBarE (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : JetGaugeGroupI)
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) : repJet U (h.covDerivBarE i l φ) =
      h.covDerivBarE i l (repDualCoeff (repConj LeptonSinglet.repJetGaugeGroupI) U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivH_of_mem_truncationKer_zero`**, a lemma, [line 1180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1180).

> A pure gauge jet fixes the Higgs tower.

```lean
lemma repJet_covDerivH_of_mem_truncationKer_zero {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ HiggsVec) :
    repJet U.1 (h.covDerivH l φ) = h.covDerivH l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarH_of_mem_truncationKer_zero`**, a lemma, [line 1187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1187).

> A pure gauge jet fixes the conjugate Higgs tower.

```lean
lemma repJet_covDerivBarH_of_mem_truncationKer_zero {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    repJet U.1 (h.covDerivBarH l φ) = h.covDerivBarH l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivD_of_mem_truncationKer_zero`**, a lemma, [line 1194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1194).

> A pure gauge jet fixes the down-type quark tower.

```lean
lemma repJet_covDerivD_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ DownSinglet) :
    repJet U.1 (h.covDerivD i l φ) = h.covDerivD i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarD_of_mem_truncationKer_zero`**, a lemma, [line 1201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1201).

> A pure gauge jet fixes the conjugate down-type quark tower.

```lean
lemma repJet_covDerivBarD_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : localGaugeData.truncationKer 0)
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    repJet U.1 (h.covDerivBarD i l φ) = h.covDerivBarD i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivU_of_mem_truncationKer_zero`**, a lemma, [line 1209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1209).

> A pure gauge jet fixes the up-type quark tower.

```lean
lemma repJet_covDerivU_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ UpSinglet) :
    repJet U.1 (h.covDerivU i l φ) = h.covDerivU i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarU_of_mem_truncationKer_zero`**, a lemma, [line 1216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1216).

> A pure gauge jet fixes the conjugate up-type quark tower.

```lean
lemma repJet_covDerivBarU_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : localGaugeData.truncationKer 0)
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    repJet U.1 (h.covDerivBarU i l φ) = h.covDerivBarU i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivQ_of_mem_truncationKer_zero`**, a lemma, [line 1224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1224).

> A pure gauge jet fixes the quark doublet tower.

```lean
lemma repJet_covDerivQ_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ QuarkDoublet) :
    repJet U.1 (h.covDerivQ i l φ) = h.covDerivQ i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarQ_of_mem_truncationKer_zero`**, a lemma, [line 1231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1231).

> A pure gauge jet fixes the conjugate quark doublet tower.

```lean
lemma repJet_covDerivBarQ_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : localGaugeData.truncationKer 0)
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    repJet U.1 (h.covDerivBarQ i l φ) = h.covDerivBarQ i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivL_of_mem_truncationKer_zero`**, a lemma, [line 1239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1239).

> A pure gauge jet fixes the lepton doublet tower.

```lean
lemma repJet_covDerivL_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ LeptonDoubletV) :
    repJet U.1 (h.covDerivL i l φ) = h.covDerivL i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarL_of_mem_truncationKer_zero`**, a lemma, [line 1246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1246).

> A pure gauge jet fixes the conjugate lepton doublet tower.

```lean
lemma repJet_covDerivBarL_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : localGaugeData.truncationKer 0)
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    repJet U.1 (h.covDerivBarL i l φ) = h.covDerivBarL i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivE_of_mem_truncationKer_zero`**, a lemma, [line 1254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1254).

> A pure gauge jet fixes the lepton singlet tower.

```lean
lemma repJet_covDerivE_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (U : localGaugeData.truncationKer 0) (φ : Module.Dual ℂ LeptonSinglet) :
    repJet U.1 (h.covDerivE i l φ) = h.covDerivE i l φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivBarE_of_mem_truncationKer_zero`**, a lemma, [line 1261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1261).

> A pure gauge jet fixes the conjugate lepton singlet tower.

```lean
lemma repJet_covDerivBarE_of_mem_truncationKer_zero (i : Fin 3) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : localGaugeData.truncationKer 0)
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    repJet U.1 (h.covDerivBarE i l φ) = h.covDerivBarE i l φ
```

**`StandardModel.AlgebraRealization.covDerivFieldStrength_swap`**, a lemma, [line 1271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1271).

> The covariant tower of the field strength is antisymmetric in its two covector
> indices: the field strength itself is, the gauge-field symbols commuting, and the
> iterated covariant derivative is odd in the family it differentiates.

```lean
lemma covDerivFieldStrength_swap (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    h.covDerivFieldStrength l ν μ φ = - h.covDerivFieldStrength l μ ν φ
```

**`StandardModel.AlgebraRealization.repJet_covDerivFieldStrength`**, a lemma, [line 1281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1281).

> The covariant tower of the field strength transforms through the base point of a gauge
> jet: no derivative of the gauge transformation enters.

```lean
lemma repJet_covDerivFieldStrength (U : JetGaugeGroupI) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    repJet U (h.covDerivFieldStrength l μ ν φ) =
      h.covDerivFieldStrength l μ ν (localGaugeData.adjointDualCoeff U⁻¹ 0 φ)
```

**`StandardModel.AlgebraRealization.repJet_covDerivFieldStrength_of_mem_truncationKer_zero`**, a lemma, [line 1288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1288).

> A pure gauge jet fixes the covariant tower of the field strength.

```lean
lemma repJet_covDerivFieldStrength_of_mem_truncationKer_zero
    (U : localGaugeData.truncationKer 0) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    repJet U.1 (h.covDerivFieldStrength l μ ν φ) = h.covDerivFieldStrength l μ ν φ
```

## J. The Lorentz laws of the covariant matter towers

> `isLorentzCovDerivTransforms_covDerivIter` and its `_conj` form turn the bare Lorentz law
> of each family, recorded by `AlgebraRealization`, into that of its covariant tower, given
> the commutation of the infinitesimal gauge action of the species with its Lorentz action.
> Each species proves that commutation next to its `gaugeAlgebraAction`
> (`HiggsVec.gaugeAlgebraAction_comm_repLorentz` and, for the fermions,
> `gaugeAlgebraAction_comm_repLorentzGroup` in its own `GaugeAlgebraAction.lean`).

**`StandardModel.AlgebraRealization.repLorentz_covDerivH`**, a lemma, [line 1309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1309).

> The Higgs tower transforms as a Lorentz scalar.

```lean
lemma repLorentz_covDerivH : IsLorentzCovDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec) (fun {_n} l => h.covDerivH l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarH`**, a lemma, [line 1315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1315).

> The conjugate Higgs tower transforms as a Lorentz scalar.

```lean
lemma repLorentz_covDerivBarH : IsLorentzCovDerivTransforms repLorentz
    (Representation.trivial ℂ SL(2,ℂ) HiggsVec).conj (fun {_n} l => h.covDerivBarH l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivD`**, a lemma, [line 1321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1321).

> The down-type quark tower transforms as a right-handed Weyl spinor.

```lean
lemma repLorentz_covDerivD (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    DownSinglet.repLorentzGroup (fun {_n} l => h.covDerivD i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarD`**, a lemma, [line 1327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1327).

> The conjugate down-type quark tower transforms in the conjugate Weyl representation.

```lean
lemma repLorentz_covDerivBarD (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    DownSinglet.repLorentzGroup.conj (fun {_n} l => h.covDerivBarD i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivU`**, a lemma, [line 1333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1333).

> The up-type quark tower transforms as a right-handed Weyl spinor.

```lean
lemma repLorentz_covDerivU (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    UpSinglet.repLorentzGroup (fun {_n} l => h.covDerivU i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarU`**, a lemma, [line 1339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1339).

> The conjugate up-type quark tower transforms in the conjugate Weyl representation.

```lean
lemma repLorentz_covDerivBarU (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    UpSinglet.repLorentzGroup.conj (fun {_n} l => h.covDerivBarU i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivQ`**, a lemma, [line 1345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1345).

> The quark doublet tower transforms as a left-handed Weyl spinor.

```lean
lemma repLorentz_covDerivQ (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    QuarkDoublet.repLorentzGroup (fun {_n} l => h.covDerivQ i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarQ`**, a lemma, [line 1351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1351).

> The conjugate quark doublet tower transforms in the conjugate Weyl representation.

```lean
lemma repLorentz_covDerivBarQ (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    QuarkDoublet.repLorentzGroup.conj (fun {_n} l => h.covDerivBarQ i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivL`**, a lemma, [line 1357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1357).

> The lepton doublet tower transforms as a left-handed Weyl spinor.

```lean
lemma repLorentz_covDerivL (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    LeptonDoubletV.repLorentzGroup (fun {_n} l => h.covDerivL i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarL`**, a lemma, [line 1363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1363).

> The conjugate lepton doublet tower transforms in the conjugate Weyl representation.

```lean
lemma repLorentz_covDerivBarL (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    LeptonDoubletV.repLorentzGroup.conj (fun {_n} l => h.covDerivBarL i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivE`**, a lemma, [line 1369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1369).

> The lepton singlet tower transforms as a right-handed Weyl spinor.

```lean
lemma repLorentz_covDerivE (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    LeptonSinglet.repLorentzGroup (fun {_n} l => h.covDerivE i l)
```

**`StandardModel.AlgebraRealization.repLorentz_covDerivBarE`**, a lemma, [line 1375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean#L1375).

> The conjugate lepton singlet tower transforms in the conjugate Weyl representation.

```lean
lemma repLorentz_covDerivBarE (i : Fin 3) : IsLorentzCovDerivTransforms repLorentz
    LeptonSinglet.repLorentzGroup.conj (fun {_n} l => h.covDerivBarE i l)
```

## Depends on

- [The algebra valued Standard model](realization-basic.md)

## Proof depends on

- [The statistics of the Standard Model fields](realization-commutations.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovariantDeriv.lean)
