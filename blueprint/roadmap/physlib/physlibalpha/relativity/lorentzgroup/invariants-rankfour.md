---
declaration: module
origin: cited
lean: Lorentz.RankFour.contractionCoeff, Lorentz.RankFour.contractionTensor, Lorentz.RankFour.ofComponents_contractionTensor, Lorentz.RankFour.sum_pi_four, Lorentz.RankFour.act_outerPair, Lorentz.RankFour.act_outerPair_comp, Lorentz.RankFour.act_leviCivitaSymbol, Lorentz.RankFour.isInvariantCoeff_contractionCoeff
statement: formalized
proof: formalized
---

# Lorentz invariants of a rank-four tensor

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.RankFour`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean): 46 declarations (1 instance with no name), 45 with a docstring; 2 private, not shown.

## i. Overview

> A rank-four tensor `T^{μνρσ}` has `4 ^ 4 = 256` components, and four invariant tensors can be
> contracted with it:
>
> * `η_{μν} η_{ρσ}`, `η_{μρ} η_{νσ}` and `η_{μσ} η_{νρ}`, the three pairings of the metric,
> * `ε_{μνρσ}`, the Levi-Civita symbol.
>
> These are the tensors `contractionTensor i`. There are no others: for an equivariant map
> `f : ℂT(fun _ : Fin 4 => .up) →ₗ[ℂ] B`, `IsLorentzCovariant 4`, a vector of `LinearMap.range f ⊔ S`,
> for `S` a Lorentz-stable submodule, is invariant exactly when it is a combination of the four
> images `f (contractionTensor i)` plus an invariant of `S`, `mem_range_sup_invariant_iff` (H), and
> `reducesInvariantsTo_span_contractionTensor` reads the left-to-right direction as a reduction.
> The fourth tensor is a pseudoscalar, so it would drop out if reflections were allowed;
> independence is not proved, and for a given `f` the four images may be dependent or zero.
> When `f` is antisymmetric under exchanging its last two slots, two images already span: that
> of `η_{μρ} η_{νσ}` and that of `ε_{μνρσ}` (B.4). When `f` is moreover symmetric under exchanging
> its first two slots, both of those vanish too (B.5).
>
> The four tensors are invariant, by `Λ η Λᵀ = η` and `det Λ = 1` (B); an invariant of the range of
> `f` is the image of an invariant tensor, whose coefficient tensor is invariant (C); and such a
> coefficient tensor is a combination of the four, two rotations cutting `256` coefficients to `22`
> (D), a boost keeping only what it does not rescale (E), and the `22 × 22` integer equation left
> being solved by one checked matrix identity (F, G).

## ii. Key results

> - `Lorentz.RankFour.contractionTensor` : the four invariant tensors.
> - `Lorentz.RankFour.exists_eq_sum` : an invariant coefficient tensor is a combination of them.
> - `Lorentz.RankFour.mem_range_sup_invariant_iff` : the classification of the invariants.
> - `Lorentz.RankFour.reducesInvariantsTo_span_contractionTensor` : the same as a reduction.
> - `Lorentz.RankFour.span_range_contractionTensor_of_antisymm` : for a map antisymmetric in its
>   last two slots, two of the four images span.
> - `Lorentz.RankFour.apply_contractionTensor_one_of_symm_of_antisymm`,
>   `Lorentz.RankFour.apply_contractionTensor_three_of_symm` : symmetry in the first two slots
>   kills those two images.

## iv. References

> * None.

## A. Coefficient tensors

> A direction is an element of `Fin 1 ⊕ Fin 3`, time or one of the three axes; an index vector
> `d : Fin 4 → Fin 1 ⊕ Fin 3` puts one in each slot, and a coefficient tensor `c` assigns a
> number to each. The components of a tensor, relabelled this way, are its coefficient tensor,
> `coeffEquiv 4`, on which `g` acts by
>
> `(act Λ c) a = ∑_d c_d Λ_{a₀ d₀} ⋯ Λ_{a₃ d₃}`,
>
> with `a` free and `d` summed (`coeffEquiv_smul`), and a tensor is invariant exactly when its
> coefficient tensor is `IsInvariantCoeff` (`invariant_iff_isInvariantCoeff`). Everything in this
> paragraph is stated for any number of slots in `Invariants.Basic` and
> `Invariants.LorentzCovariance` and used here at four.

## B. The four invariant tensors

## C. The metric, the Levi-Civita symbol and the invariant tensors

> The metric is `minkowskiMatrixZ`, the integer form of `minkowskiMatrix`, and the symbol is
> `leviCivitaSymbol`, read on an index vector through `finSumFinEquiv`. Both are integer valued
> because sections F and G evaluate them in the kernel, which cannot compute with real numbers.
> The metric pairings use the slots `(0,1)(2,3)`, `(0,2)(1,3)` and `(0,3)(1,2)`;
> `contractionCoeff` holds the four coefficient tensors and `contractionTensor` the four tensors
> with those coefficients, in that order.

**`Lorentz.RankFour.contractionCoeff`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L119).

> The four coefficient tensors: the three metric pairings, then the Levi-Civita symbol.

```lean
def contractionCoeff : Fin 4 → (Fin 4 → Fin 1 ⊕ Fin 3) → ℤ
```

**`Lorentz.RankFour.contractionTensor`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L127).

> The four invariant tensors with four contravariant indices: `η_{μν} η_{ρσ}`,
> `η_{μρ} η_{νσ}`, `η_{μσ} η_{νρ}` and `ε_{μνρσ}`.

```lean
noncomputable def contractionTensor (i : Fin 4) : ℂT(fun _ : Fin 4 => Color.up)
```

**`Lorentz.RankFour.ofComponents_contractionTensor`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L132).

> `ofComponents T` sends each invariant tensor to the contraction of `T` with its
> coefficients.

```lean
lemma ofComponents_contractionTensor (T : (Fin 4 → Fin 1 ⊕ Fin 3) → B) (i : Fin 4) :
    ofComponents T (contractionTensor i) = ∑ d, ((contractionCoeff i d : ℤ) : ℂ) • T d
```

## D. The four coefficient tensors are invariant

> `Λ η Λᵀ = η` defines the Lorentz group; entry by entry it is
> `LorentzGroup.sum_minkowskiMatrixZ_mul`, and a pair of metrics is two copies of it, one per
> pair of slots (`act_outerPair`). The inner and split pairings are the outer one with the slots
> permuted (`act_outerPair_comp`). The symbol against
> four rows of `M` gives `det M` times the symbol of those rows (`sum_leviCivitaSymbol_mul_prod`),
> and `det Λ = 1` here: the only use of the determinant, and the reason there are four invariants
> and not three, a reflection having `det = -1`. `sum_pi_four` is bookkeeping.

**`Lorentz.RankFour.sum_pi_four`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L150).

> Bookkeeping: a sum over index vectors is a fourfold sum over directions.

```lean
lemma sum_pi_four {M : Type*} [AddCommMonoid M] (F : (Fin 4 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 4 → Fin 1 ⊕ Fin 3, F d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, ∑ z : Fin 1 ⊕ Fin 3,
        ∑ w : Fin 1 ⊕ Fin 3, F ![x, y, z, w]
```

**`Lorentz.RankFour.act_outerPair`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L169).

> The pairing of slots `(0,1)` and `(2,3)` is fixed: two copies of
> `LorentzGroup.sum_minkowskiMatrixZ_mul`.

```lean
lemma act_outerPair (Λ : LorentzGroup 3) (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((minkowskiMatrixZ (d 0) (d 1) * minkowskiMatrixZ (d 2) (d 3) : ℤ) : ℂ)) a
      = ((minkowskiMatrixZ (a 0) (a 1) * minkowskiMatrixZ (a 2) (a 3) : ℤ) : ℂ)
```

**`Lorentz.RankFour.act_outerPair_comp`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L191).

> The same for the slots permuted by `σ`, by renaming the summation variable.

```lean
lemma act_outerPair_comp (σ : Equiv.Perm (Fin 4)) (Λ : LorentzGroup 3)
    (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((minkowskiMatrixZ (d (σ 0)) (d (σ 1))
        * minkowskiMatrixZ (d (σ 2)) (d (σ 3)) : ℤ) : ℂ)) a
      = ((minkowskiMatrixZ (a (σ 0)) (a (σ 1))
        * minkowskiMatrixZ (a (σ 2)) (a (σ 3)) : ℤ) : ℂ)
```

**`Lorentz.RankFour.act_leviCivitaSymbol`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L207).

> The symbol is fixed by a Lorentz matrix of determinant `1`; in general it picks up `det Λ`,
> by `sum_leviCivitaSymbol_mul_prod`.

```lean
lemma act_leviCivitaSymbol (Λ : LorentzGroup 3) (hΛ : Λ.1.det = 1) (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((leviCivitaSymbol fun μ => d (finSumFinEquiv μ) : ℤ) : ℂ)) a
      = ((leviCivitaSymbol fun μ => a (finSumFinEquiv μ) : ℤ) : ℂ)
```

**`Lorentz.RankFour.isInvariantCoeff_contractionCoeff`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L223).

> The four coefficient tensors are invariant.

```lean
lemma isInvariantCoeff_contractionCoeff (i : Fin 4) :
    IsInvariantCoeff fun d => ((contractionCoeff i d : ℤ) : ℂ)
```

## E. The four tensors are Lorentz invariant

**`Lorentz.RankFour.contractionTensor_invariant`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L242).

> Each of the four tensors is Lorentz invariant, its coefficient tensor being invariant.

```lean
lemma contractionTensor_invariant (i : Fin 4) (g : SL(2,ℂ)) :
    g • contractionTensor i = contractionTensor i
```

## F. Exchanging the last two slots

> Exchanging the slots `2` and `3`, `permT (Equiv.swap 2 3)`, fixes `η_{μν} η_{ρσ}`, the metric
> being symmetric, and exchanges `η_{μρ} η_{νσ}` with `η_{μσ} η_{νρ}`. So a linear map `f` out of
> the tensors with `f ∘ₗ permT (Equiv.swap 2 3) = -f` sends the first tensor to zero and the
> third to minus the second, and the four images span what the second and the Levi-Civita image
> span. Neither equivariance of `f` nor any structure on `B` beyond a complex module is used; the
> two remaining images may still be dependent or zero.

**`Lorentz.RankFour.isReindexing_swap_two_three`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L265).

> Exchanging the last two of four contravariant slots is a reindexing.

```lean
lemma isReindexing_swap_two_three :
    Tensor.IsReindexing (fun _ : Fin 4 => Color.up) (fun _ => Color.up)
      ⇑(Equiv.swap (2 : Fin 4) 3)
```

**`Lorentz.RankFour.permT_swap_two_three_contractionTensor_zero`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L271).

> `η_{μν} η_{ρσ}` is unchanged by exchanging its last two slots.

```lean
lemma permT_swap_two_three_contractionTensor_zero :
    Tensor.permT _ isReindexing_swap_two_three (contractionTensor 0) = contractionTensor 0
```

**`Lorentz.RankFour.permT_swap_two_three_contractionTensor_one`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L278).

> Exchanging the last two slots of `η_{μρ} η_{νσ}` gives `η_{μσ} η_{νρ}`.

```lean
lemma permT_swap_two_three_contractionTensor_one :
    Tensor.permT _ isReindexing_swap_two_three (contractionTensor 1) = contractionTensor 2
```

**`Lorentz.RankFour.apply_contractionTensor_zero_of_antisymm`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L287).

> A map antisymmetric in the last two slots sends `η_{μν} η_{ρσ}` to zero.

```lean
lemma apply_contractionTensor_zero_of_antisymm
    (hf : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 0) = 0
```

**`Lorentz.RankFour.apply_contractionTensor_two_of_antisymm`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L300).

> A map antisymmetric in the last two slots sends `η_{μσ} η_{νρ}` to minus the image of
> `η_{μρ} η_{νσ}`.

```lean
lemma apply_contractionTensor_two_of_antisymm
    (hf : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 2) = -f (contractionTensor 1)
```

**`Lorentz.RankFour.span_range_contractionTensor_of_antisymm`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L309).

> For a map antisymmetric in the last two slots, the images of the four invariant tensors
> span the same as the images of `η_{μρ} η_{νσ}` and `ε_{μνρσ}`.

```lean
lemma span_range_contractionTensor_of_antisymm
    (hf : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    Submodule.span ℂ (Set.range fun i => f (contractionTensor i))
      = Submodule.span ℂ {f (contractionTensor 1), f (contractionTensor 3)}
```

## G. Exchanging the first two slots

> Exchanging the slots `0` and `1`, `permT (Equiv.swap 0 1)`, exchanges `η_{μρ} η_{νσ}` with
> `η_{μσ} η_{νρ}` and negates `ε_{μνρσ}`. So a linear map `f` out of the tensors with
> `f ∘ₗ permT (Equiv.swap 0 1) = f` sends `ε_{μνρσ}` to zero, and if `f` is also antisymmetric in
> its last two slots it sends `η_{μρ} η_{νσ}` to zero as well: in both a symmetric pair of slots
> is contracted against an antisymmetric one. As in B.4 nothing beyond a complex module is used.

**`Lorentz.RankFour.isReindexing_swap_zero_one`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L342).

> Exchanging the first two of four contravariant slots is a reindexing.

```lean
lemma isReindexing_swap_zero_one :
    Tensor.IsReindexing (fun _ : Fin 4 => Color.up) (fun _ => Color.up)
      ⇑(Equiv.swap (0 : Fin 4) 1)
```

**`Lorentz.RankFour.permT_swap_zero_one_contractionTensor_one`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L348).

> Exchanging the first two slots of `η_{μρ} η_{νσ}` gives `η_{μσ} η_{νρ}`.

```lean
lemma permT_swap_zero_one_contractionTensor_one :
    Tensor.permT _ isReindexing_swap_zero_one (contractionTensor 1) = contractionTensor 2
```

**`Lorentz.RankFour.permT_swap_zero_one_contractionTensor_three`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L355).

> Exchanging the first two slots negates `ε_{μνρσ}`.

```lean
lemma permT_swap_zero_one_contractionTensor_three :
    Tensor.permT _ isReindexing_swap_zero_one (contractionTensor 3) = -contractionTensor 3
```

**`Lorentz.RankFour.apply_contractionTensor_one_of_symm_of_antisymm`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L370).

> A map symmetric in the first two slots and antisymmetric in the last two sends
> `η_{μρ} η_{νσ}` to zero.

```lean
lemma apply_contractionTensor_one_of_symm_of_antisymm
    (hs : f ∘ₗ Tensor.permT _ isReindexing_swap_zero_one = f)
    (ha : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 1) = 0
```

**`Lorentz.RankFour.apply_contractionTensor_three_of_symm`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L383).

> A map symmetric in the first two slots sends `ε_{μνρσ}` to zero.

```lean
lemma apply_contractionTensor_three_of_symm
    (hs : f ∘ₗ Tensor.permT _ isReindexing_swap_zero_one = f) :
    f (contractionTensor 3) = 0
```

## H. Invariants of the range come from invariant coefficient tensors

> An invariant of the range of `f` is the image of an invariant tensor
> (`TensorSpecies.IsEquivariant.exists_invariant_add_of_mem_sup`): the adjoint of the action of
> `g` on the coefficients is the action of `g†`. The coefficient tensor of an invariant tensor is
> invariant, so what remains is to classify the invariant coefficient tensors, sections D to G.

## I. The rotations by `π` about the axes and the rotation `x → y → z → x`

> The rotation by `π` about the `k`-th axis is `SL2C.halfTurn k`, with diagonal Lorentz matrix
> fixing time and that axis and negating the other two, so it multiplies `c d` by `-1` once per
> slot of `d` holding a negated direction (`act_halfTurn`), and where that sign is `-1`
> invariance forces `c d = 0`. Call `d` half-turn fixed when all three signs are `1`
> (`IsHalfTurnFixed`): with `n_t, n_x, n_y, n_z` the counts of each direction that says all four
> have the same parity, so `xxyy` and `txyz` survive, `tttx` does not, and `64` of `256` remain.
>
> The rotation `x → y → z → x` fixes time (`rotationCycle`) and permutes rather than rescales, so
> the new coefficient at `a` is the old one at `cycIdx (cycIdx a)` (`act_rotationCycle`) and
> invariance reads `c (cycIdx d) = c d`: `c` is constant on the orbit
> `{d, cycIdx d, cycIdx (cycIdx d)}`, of three members unless `d` is `tttt`. Both actions are
> stated for any number of slots in `Invariants.Basic`.

**`Lorentz.RankFour.IsHalfTurnFixed`**, a def, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L426).

> All three half turns fix the coefficient at `d`, that is the sign product is `1` for each
> axis. Equivalently, and not used below, all four directions occur an even number of times
> among the slots, or all four an odd number.

```lean
def IsHalfTurnFixed (d : Fin 4 → Fin 1 ⊕ Fin 3) : Prop
```

**An instance with no name**, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L429).

```lean
instance : DecidablePred IsHalfTurnFixed
```

**`Lorentz.RankFour.eq_zero_of_not_isHalfTurnFixed`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L433).

> An invariant coefficient tensor vanishes off the half-turn fixed index vectors.

```lean
lemma eq_zero_of_not_isHalfTurnFixed {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) {d : Fin 4 → Fin 1 ⊕ Fin 3} (hd : ¬IsHalfTurnFixed d) :
    c d = 0
```

## J. The boost along an axis

## K. An invariant tensor has boost weight zero

> The boosts along the axis `i` are `SL2C.boostAxis i t ht`, of rapidity `2 log t` for `t > 0`.
> In each slot replace the coordinate directions by the light-cone directions `D₀ - Dᵢ`,
> `D₀ + Dᵢ` and the two transverse ones: they are eigenvectors of the boost with eigenvalues
> `t²`, `t⁻²`, `1`, `1` (`sum_boostAxis_lightConeCoeff`, imported), so their weights, the
> exponents of `t`, are `2`, `-2`, `0`, `0` (`lightConeWeight`). A multi-index `κ` picks one per
> slot and `lightConeComponent i c κ` contracts `c` against that choice; the boost scales it by
> `t` to the total weight of `κ`, so `t = 2` kills every component of nonzero weight. Only the
> `z`-axis is used below, and nothing claims these elements generate the group: F and G show that
> what they force is enough.

## L. The weight-zero projection

> Writing each coordinate direction in the light-cone basis recovers `c` from its light-cone
> components (`eq_sum_lightConeComponent`), and for an invariant `c` only weight zero survives.
> The projection that keeps total weight `m` is `Invariants.transitionZ`, built a slot at a time
> and stated at any number of slots in `Invariants.LightCone`; each slot carries the factor `2`
> of `lightConeCoeffInvZ`, so at four slots the projection is `2 ^ 4 = 16` times the true one.
> That is the only place the `16` comes from.

**`Lorentz.RankFour.sixteen_mul_eq_sum_transitionZ`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L469).

> An invariant coefficient tensor is its own weight-zero projection.

```lean
lemma sixteen_mul_eq_sum_transitionZ {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) (i : Fin 3) (d : Fin 4 → Fin 1 ⊕ Fin 3) :
    16 * c d = ∑ e, ((transitionZ i d e 0 : ℤ) : ℂ) * c e
```

## M. The `22` orbit coordinates and the orbit matrix

## N. The orbits

> Write an index vector as a word, `tttt` or `txxt`. Cycling the axes carries one to another and
> three cyclings return it, so they fall into orbits of at most three: `txxt`, `tyyt`, `tzzt`
> form one, and `tttt` is alone. By D an invariant tensor vanishes off the `64` half-turn fixed
> vectors and is constant on each orbit, and those `64` make `22` orbits, `21` of size three plus
> `tttt`; `orbitRep` lists one from each, and the two lemmas below check at all `256` index
> vectors that these cover the half-turn fixed ones without overlapping. So an invariant tensor is its
> `22` values at the representatives, its orbit coordinates, which `ofOrbitCoord` inverts.

**`Lorentz.RankFour.orbitRep`**, a def, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L502).

> One index vector from each of the `22` orbits, checked by the two lemmas below.

```lean
def orbitRep : Fin 22 → Fin 4 → Fin 1 ⊕ Fin 3
```

**`Lorentz.RankFour.orbit`**, a def, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L527).

> The `k`-th representative and its two cyclings; for `tttt` the three coincide.

```lean
def orbit (k : Fin 22) : Finset (Fin 4 → Fin 1 ⊕ Fin 3)
```

**`Lorentz.RankFour.isHalfTurnFixed_iff_exists_mem_orbit`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L531).

> The vectors in one of the `22` orbits are exactly the half-turn fixed ones, a finite check.

```lean
lemma isHalfTurnFixed_iff_exists_mem_orbit :
    ∀ d, IsHalfTurnFixed d ↔ ∃ k, d ∈ orbit k
```

**`Lorentz.RankFour.disjoint_orbit`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L536).

> Different orbits share no index vector, a finite check.

```lean
lemma disjoint_orbit : ∀ k l : Fin 22, k ≠ l → Disjoint (orbit k) (orbit l)
```

**`Lorentz.RankFour.eq_of_mem_orbit`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L540).

> An index vector lies in at most one orbit.

```lean
lemma eq_of_mem_orbit {k l : Fin 22} {d : Fin 4 → Fin 1 ⊕ Fin 3}
    (hk : d ∈ orbit k) (hl : d ∈ orbit l) : k = l
```

**`Lorentz.RankFour.eq_orbitRep_of_mem_orbit`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L545).

> A tensor unchanged by cycling takes, on an orbit, its value at the representative.

```lean
lemma eq_orbitRep_of_mem_orbit {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : ∀ d, c (cycIdx d) = c d) {k : Fin 22} {d : Fin 4 → Fin 1 ⊕ Fin 3}
    (h : d ∈ orbit k) : c d = c (orbitRep k)
```

**`Lorentz.RankFour.ofOrbitCoord`**, a def, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L555).

> The coefficient tensor with orbit coordinates `b`, and `0` off the orbits.

```lean
noncomputable def ofOrbitCoord (b : Fin 22 → ℂ) (d : Fin 4 → Fin 1 ⊕ Fin 3) : ℂ
```

**`Lorentz.RankFour.eq_ofOrbitCoord`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L559).

> An invariant coefficient tensor is rebuilt from its `22` orbit coordinates.

```lean
lemma eq_ofOrbitCoord {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c) :
    c = ofOrbitCoord fun k => c (orbitRep k)
```

**`Lorentz.RankFour.sum_mul_ofOrbitCoord`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L573).

> Contracting against such a tensor collects the `256` index vectors into the `22` orbits.

```lean
lemma sum_mul_ofOrbitCoord (f : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ) (b : Fin 22 → ℂ) :
    ∑ e, f e * ofOrbitCoord b e = ∑ l, (∑ e ∈ orbit l, f e) * b l
```

## O. The orbit matrix

> Take `16 c_d = ∑_e transitionZ 2 d e 0 * c_e` at a representative and its two cyclings and add.
> The left gives `48` times one orbit coordinate, the right collects the `256` index vectors into
> the `22` orbits, and what is left is `M b = 48 b` with `M = orbitMatrix` below and
> `48 = 3 * 16`. Entry `M k l` sums the transitions from the three cyclings of the representative
> of orbit `k` into orbit `l` (`orbitMatrix_apply`, checked over `484` entries), so the printed
> integers are not meant to be read; `M` is not symmetric, a row carrying three cyclings and a
> column an orbit.

**`Lorentz.RankFour.orbitMatrix`**, a def, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L596).

> Forty-eight times the weight-zero projection along `z` on the orbit coordinates, the three
> cyclings summed and not averaged, so `48 = 3 * 16`. Meaningful only through
> `orbitMatrix_apply`.

```lean
def orbitMatrix : Matrix (Fin 22) (Fin 22) ℤ
```

**`Lorentz.RankFour.orbitMatrix_apply`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L633).

> Each entry sums the `z`-axis transitions from orbit `k` into orbit `l`, a finite check.

```lean
lemma orbitMatrix_apply : ∀ k l : Fin 22,
    orbitMatrix k l = ∑ e ∈ orbit l, (transitionZ 2 (orbitRep k) e 0
      + transitionZ 2 (cycIdx (orbitRep k)) e 0
      + transitionZ 2 (cycIdx (cycIdx (orbitRep k))) e 0)
```

**`Lorentz.RankFour.orbitMatrix_mulVec`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L640).

> The orbit coordinates of an invariant coefficient tensor satisfy `M b = 48 b`.

```lean
lemma orbitMatrix_mulVec {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) :
    orbitMatrix.map (Int.cast : ℤ → ℂ) *ᵥ (fun k => c (orbitRep k))
      = (48 : ℂ) • fun k => c (orbitRep k)
```

## P. The certificate

> F leaves `M b = 48 b` for the orbit coordinates `b k = c (orbitRep k)`. Four solutions are
> known, the orbit coordinates `v i = contractionOrbit i` of the tensors of B; there are no
> others, by one identity between `22 × 22` integer matrices:
>
> `M (M - 32) (M - 16) (M² - 44 M + 192) = 393216 • projector`,
>
> where `projector = ∑ i, (v i) (w i)ᵀ` is four rank-one matrices built from the columns `v i`
> and rows `w i = contractionWeight i`, so it sends any vector to a combination of the `v i`.
> Lean checks it by computing all `484` entries of each side. On a solution `b` every factor
> turns `M` into `48`, giving `48² - 44 * 48 + 192 = 384`, then `32`, `16`, `48`, so the left
> sends `b` to `48 * 16 * 32 * 384 = 9437184` times `b` and the right to `393216 • (projector b)`.
> As `9437184 = 393216 * 24` this leaves `projector b = 24 b` (`projector_mulVec`), writing `b`,
> and with it `c`, as a combination of the four; the `24` is
> `contractionWeight_mul_contractionOrbit`. The identity is
> `λ (3λ - 2) (3λ - 1) (12λ² - 11λ + 1) / 4` at `λ = M / 48` with denominators cleared, but that
> is only where it came from: the file proves nothing about the spectrum.

**`Lorentz.RankFour.contractionOrbit`**, a def, [line 683](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L683).

> The orbit coordinates of the `i`-th coefficient tensor.

```lean
def contractionOrbit (i : Fin 4) (k : Fin 22) : ℤ
```

**`Lorentz.RankFour.contractionWeight`**, a def, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L688).

> Four rows of `22` integers paired with `contractionOrbit` to build `projector`. Found by
> computation and characterised by `contractionWeight_mul_contractionOrbit`; unrelated to boost
> weight.

```lean
def contractionWeight : Fin 4 → Fin 22 → ℤ
```

**`Lorentz.RankFour.contractionWeight_mul_contractionOrbit`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L695).

> The weight rows and orbit coordinates pair to `24 δᵢⱼ`, a finite check.

```lean
lemma contractionWeight_mul_contractionOrbit : ∀ i j : Fin 4,
    ∑ k, contractionWeight i k * contractionOrbit j k = if i = j then 24 else 0
```

**`Lorentz.RankFour.projector`**, a def, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L700).

> Four rank-one matrices, so it sends any vector to a combination of the `v i`.

```lean
def projector : Matrix (Fin 22) (Fin 22) ℤ
```

**`Lorentz.RankFour.certificate`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L704).

> An identity between `22 × 22` integer matrices, a finite check over `484` entries.

```lean
lemma certificate :
    orbitMatrix * (orbitMatrix - 32 • 1) * (orbitMatrix - 16 • 1)
      * (orbitMatrix * orbitMatrix - 44 • orbitMatrix + 192 • 1) = 393216 • projector
```

**`Lorentz.RankFour.projector_mulVec`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L716).

> The integer projector matrix acts on invariant orbit coordinates by multiplication by `24`.
> The `24` is the normalization of `projector`: each factor of the certificate acts on such a
> vector as a scalar, `M` by `48`, `M - z` by `48 - z` and the quadratic factor by
> `48 ^ 2 - 44 * 48 + 192 = 384`, so the left-hand side scales it by
> `48 * 32 * 16 * 384 = 9437184`, and dividing by the `393216` on the right leaves `24`.

```lean
lemma projector_mulVec {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c) :
    projector.map (Int.cast : ℤ → ℂ) *ᵥ (fun k => c (orbitRep k))
      = (24 : ℂ) • fun k => c (orbitRep k)
```

**`Lorentz.RankFour.orbitCoord_eq`**, a lemma, [line 757](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L757).

> `24` times an orbit coordinate of an invariant tensor, read entry by entry off the previous
> lemma: `projector` is built from the columns `contractionOrbit i` and the rows
> `contractionWeight i`.

```lean
lemma orbitCoord_eq {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    (k : Fin 22) :
    24 * c (orbitRep k)
      = ∑ i, (contractionOrbit i k : ℂ) * ∑ l, (contractionWeight i l : ℂ) * c (orbitRep l)
```

**`Lorentz.RankFour.exists_eq_sum`**, a lemma, [line 771](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L771).

> An invariant coefficient tensor is a combination of the four.

```lean
lemma exists_eq_sum {c : (Fin 4 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c) :
    ∃ a : Fin 4 → ℂ, c = fun d => ∑ i, a i * ((contractionCoeff i d : ℤ) : ℂ)
```

## Q. The classification of the invariants of an equivariant map

> C to G reduce the invariants of `LinearMap.range f ⊔ S` to the span of the four images
> `f (contractionTensor i)`; conversely those images are invariant, so a combination of them plus
> an invariant of `S` is an invariant of `LinearMap.range f ⊔ S`.

**`Lorentz.RankFour.reducesInvariantsTo_span_contractionTensor`**, a lemma, [line 803](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L803).

> The invariants of the range of `f` reduce to the span of the images of the four invariant
> tensors.

```lean
lemma reducesInvariantsTo_span_contractionTensor (hf : IsLorentzCovariant 4 B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
      (Submodule.span ℂ (Set.range fun i => f (contractionTensor i)))
```

**`Lorentz.RankFour.mem_range_sup_invariant_iff`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean#L814).

> A vector of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is invariant exactly
> when it is a combination of the images of the four invariant tensors plus an invariant of
> `S`. `hS` is used only left to right.

```lean
lemma mem_range_sup_invariant_iff (hf : IsLorentzCovariant 4 B repLorentz f) (x : B)
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) :
    (x ∈ LinearMap.range f ⊔ S ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ a : Fin 4 → ℂ, ∃ y ∈ S, x = ∑ i, a i • f (contractionTensor i) + y
        ∧ ∀ g : SL(2,ℂ), repLorentz g y = y
```

## Depends on

- [The light-cone basis of a boost axis over the integers](invariants-lightcone.md)
- [Equivariant maps out of tensors with four-vector indices](invariants-lorentzcovariance.md)
- [The Minkowski matrix over the integers](../minkowskimatrix.md)

## Proof depends on

- [Contracting the Levi-Civita symbol against a matrix](../../mathematics/part-02/levicivita/basic.md)
- [The defining relation of the Lorentz group on its entries](basic.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankFour.lean)
