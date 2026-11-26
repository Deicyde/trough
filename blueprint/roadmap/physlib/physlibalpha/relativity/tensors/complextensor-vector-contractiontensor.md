---
declaration: module
origin: cited
lean: Lorentz.RankFour.contractionCoeff, Lorentz.RankFour.contractionTensor, Lorentz.RankFour.liftComponents_contractionTensor, Lorentz.RankFour.sum_pi_four, Lorentz.RankFour.act_outerPair, Lorentz.RankFour.act_outerPair_comp, Lorentz.RankFour.act_leviCivitaSymbol, Lorentz.RankFour.isInvariantCoeff_contractionCoeff
statement: formalized
proof: formalized
---

# The contraction tensors of four four-vector indices

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.ContractionTensor`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean): 24 declarations, 24 with a docstring.

> The Lorentz invariants of four four-vector indices are spanned by the three pairings of the
> metric and the Levi-Civita symbol.

## i. Overview

> A rank-four tensor `T^{μνρσ}` has `4 ^ 4 = 256` components, and four invariant tensors can be
> contracted with it:
>
> * `η_{μν} η_{ρσ}`, `η_{μρ} η_{νσ}` and `η_{μσ} η_{νρ}`, the three pairings of the metric,
> * `ε_{μνρσ}`, the Levi-Civita symbol.
>
> These are the tensors `contractionTensor i`. There are no others: the invariant tensors are the
> span of the four,
> `complexLorentzTensor.invariants_up_pow_four_eq_span_range_contractionTensor` (I). For an
> equivariant map `f : ℂT(fun _ : Fin 4 => .up) →ₗ[ℂ] B`, the invariants of
> `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, therefore reduce to the span of the
> four images `f (contractionTensor i)`, `ComplexVector.reducesInvariantsTo_span_contractionTensor`.
> The fourth tensor is a pseudoscalar, so it would drop out if reflections were allowed. For a
> given `f` the four images may be dependent or zero. When `f` is antisymmetric under exchanging
> its last two slots, two images already span: that of `η_{μρ} η_{νσ}` and that of `ε_{μνρσ}` (F).
> When `f` is moreover symmetric under exchanging its first two slots, both of those vanish too (G).
>
> The four tensors are invariant, by `Λ η Λᵀ = η` and `det Λ = 1` (D, E), and linearly
> independent (H). That they span every invariant is seen through Weyl spinors (I). The Pauli
> matrices change each four-vector index into a bispinor index, a left-handed and a right-handed
> Weyl index, injectively and equivariantly (`complexLorentzTensor.pauliTensorMap`). On the Weyl
> side the invariants are products of those of the four left-handed and of the four right-handed
> indices, two pairings `ε ε` for each chirality, so they span a space of dimension at most four
> (`complexLorentzTensor.invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing`).
> The four tensors are independent, so they span every invariant.

## ii. Key results

> - `Lorentz.RankFour.contractionTensor` : the four invariant tensors.
> - `Lorentz.RankFour.linearIndependent_contractionTensor` : they are linearly independent.
> - `complexLorentzTensor.invariants_up_pow_four_eq_span_range_contractionTensor` : the invariant
>   tensors are their span.
> - `Lorentz.ComplexVector.reducesInvariantsTo_span_contractionTensor` : the invariants of the
>   range of `f` reduce to the span of their images.
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
> paragraph is stated for any number of slots in
> `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.InvariantCoeff`, and used here at four.

## B. The four invariant tensors

## C. The metric, the Levi-Civita symbol and the invariant tensors

> The metric is `minkowskiMatrixZ`, the integer form of `minkowskiMatrix`, and the symbol is
> `leviCivitaSymbol`, read on an index vector through `finSumFinEquiv`. Both are integer valued.
> The metric pairings use the slots `(0,1)(2,3)`, `(0,2)(1,3)` and `(0,3)(1,2)`;
> `contractionCoeff` holds the four coefficient tensors and `contractionTensor` the four tensors
> with those coefficients, in that order.

**`Lorentz.RankFour.contractionCoeff`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L118).

> The four coefficient tensors, the three metric pairings, then the Levi-Civita symbol.

```lean
def contractionCoeff : Fin 4 → (Fin 4 → Fin 1 ⊕ Fin 3) → ℤ
```

**`Lorentz.RankFour.contractionTensor`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L126).

> The four invariant tensors with four contravariant indices, `η_{μν} η_{ρσ}`,
> `η_{μρ} η_{νσ}`, `η_{μσ} η_{νρ}` and `ε_{μνρσ}`.

```lean
noncomputable def contractionTensor (i : Fin 4) : ℂT(fun _ : Fin 4 => Color.up)
```

**`Lorentz.RankFour.liftComponents_contractionTensor`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L131).

> `liftComponents T` sends each invariant tensor to the contraction of `T` with its
> coefficients.

```lean
lemma liftComponents_contractionTensor (T : (Fin 4 → Fin 1 ⊕ Fin 3) → B) (i : Fin 4) :
    liftComponents T (contractionTensor i)
      = ∑ d, ((contractionCoeff i d : ℤ) : ℂ) • T d
```

## D. The four coefficient tensors are invariant

> `Λ η Λᵀ = η` defines the Lorentz group; entry by entry it is
> `LorentzGroup.sum_minkowskiMatrixZ_mul`, and a pair of metrics is two copies of it, one per
> pair of slots (`act_outerPair`). The inner and split pairings are the outer one with the slots
> permuted (`act_outerPair_comp`). The symbol against
> four rows of `M` gives `det M` times the symbol of those rows (`sum_leviCivitaSymbol_mul_prod`),
> and `det Λ = 1` here: the only use of the determinant, and the reason there are four invariants
> and not three, a reflection having `det = -1`. `sum_pi_four` is bookkeeping.

**`Lorentz.RankFour.sum_pi_four`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L150).

> A sum over index vectors is a fourfold sum over directions.

```lean
lemma sum_pi_four {M : Type*} [AddCommMonoid M] (F : (Fin 4 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 4 → Fin 1 ⊕ Fin 3, F d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, ∑ z : Fin 1 ⊕ Fin 3,
        ∑ w : Fin 1 ⊕ Fin 3, F ![x, y, z, w]
```

**`Lorentz.RankFour.act_outerPair`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L169).

> The pairing of slots `(0,1)` and `(2,3)` is fixed, by two copies of
> `LorentzGroup.sum_minkowskiMatrixZ_mul`.

```lean
lemma act_outerPair (Λ : LorentzGroup 3) (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((minkowskiMatrixZ (d 0) (d 1) * minkowskiMatrixZ (d 2) (d 3) : ℤ) : ℂ)) a
      = ((minkowskiMatrixZ (a 0) (a 1) * minkowskiMatrixZ (a 2) (a 3) : ℤ) : ℂ)
```

**`Lorentz.RankFour.act_outerPair_comp`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L191).

> The same for the slots permuted by `σ`, by renaming the summation variable.

```lean
lemma act_outerPair_comp (σ : Equiv.Perm (Fin 4)) (Λ : LorentzGroup 3)
    (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((minkowskiMatrixZ (d (σ 0)) (d (σ 1))
        * minkowskiMatrixZ (d (σ 2)) (d (σ 3)) : ℤ) : ℂ)) a
      = ((minkowskiMatrixZ (a (σ 0)) (a (σ 1))
        * minkowskiMatrixZ (a (σ 2)) (a (σ 3)) : ℤ) : ℂ)
```

**`Lorentz.RankFour.act_leviCivitaSymbol`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L207).

> The symbol is fixed by a Lorentz matrix of determinant `1`; in general it picks up `det Λ`,
> by `sum_leviCivitaSymbol_mul_prod`.

```lean
lemma act_leviCivitaSymbol (Λ : LorentzGroup 3) (hΛ : Λ.1.det = 1) (a : Fin 4 → Fin 1 ⊕ Fin 3) :
    act Λ.1 (fun d => ((leviCivitaSymbol fun μ => d (finSumFinEquiv μ) : ℤ) : ℂ)) a
      = ((leviCivitaSymbol fun μ => a (finSumFinEquiv μ) : ℤ) : ℂ)
```

**`Lorentz.RankFour.isInvariantCoeff_contractionCoeff`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L223).

> The four coefficient tensors are invariant.

```lean
lemma isInvariantCoeff_contractionCoeff (i : Fin 4) :
    IsInvariantCoeff fun d => ((contractionCoeff i d : ℤ) : ℂ)
```

## E. The four tensors are Lorentz invariant

**`Lorentz.RankFour.contractionTensor_invariant`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L242).

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

**`Lorentz.RankFour.isReindexing_swap_two_three`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L265).

> Exchanging the last two of four contravariant slots is a reindexing.

```lean
lemma isReindexing_swap_two_three :
    Tensor.IsReindexing (fun _ : Fin 4 => Color.up) (fun _ => Color.up)
      ⇑(Equiv.swap (2 : Fin 4) 3)
```

**`Lorentz.RankFour.permT_swap_two_three_contractionTensor_zero`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L271).

> `η_{μν} η_{ρσ}` is unchanged by exchanging its last two slots.

```lean
lemma permT_swap_two_three_contractionTensor_zero :
    Tensor.permT _ isReindexing_swap_two_three (contractionTensor 0) = contractionTensor 0
```

**`Lorentz.RankFour.permT_swap_two_three_contractionTensor_one`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L278).

> Exchanging the last two slots of `η_{μρ} η_{νσ}` gives `η_{μσ} η_{νρ}`.

```lean
lemma permT_swap_two_three_contractionTensor_one :
    Tensor.permT _ isReindexing_swap_two_three (contractionTensor 1) = contractionTensor 2
```

**`Lorentz.RankFour.apply_contractionTensor_zero_of_antisymm`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L287).

> A map antisymmetric in the last two slots sends `η_{μν} η_{ρσ}` to zero.

```lean
lemma apply_contractionTensor_zero_of_antisymm
    (hf : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 0) = 0
```

**`Lorentz.RankFour.apply_contractionTensor_two_of_antisymm`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L300).

> A map antisymmetric in the last two slots sends `η_{μσ} η_{νρ}` to minus the image of
> `η_{μρ} η_{νσ}`.

```lean
lemma apply_contractionTensor_two_of_antisymm
    (hf : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 2) = -f (contractionTensor 1)
```

**`Lorentz.RankFour.span_range_contractionTensor_of_antisymm`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L309).

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
> is contracted against an antisymmetric one. As in F nothing beyond a complex module is used.

**`Lorentz.RankFour.isReindexing_swap_zero_one`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L342).

> Exchanging the first two of four contravariant slots is a reindexing.

```lean
lemma isReindexing_swap_zero_one :
    Tensor.IsReindexing (fun _ : Fin 4 => Color.up) (fun _ => Color.up)
      ⇑(Equiv.swap (0 : Fin 4) 1)
```

**`Lorentz.RankFour.permT_swap_zero_one_contractionTensor_one`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L348).

> Exchanging the first two slots of `η_{μρ} η_{νσ}` gives `η_{μσ} η_{νρ}`.

```lean
lemma permT_swap_zero_one_contractionTensor_one :
    Tensor.permT _ isReindexing_swap_zero_one (contractionTensor 1) = contractionTensor 2
```

**`Lorentz.RankFour.permT_swap_zero_one_contractionTensor_three`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L355).

> Exchanging the first two slots negates `ε_{μνρσ}`.

```lean
lemma permT_swap_zero_one_contractionTensor_three :
    Tensor.permT _ isReindexing_swap_zero_one (contractionTensor 3) = -contractionTensor 3
```

**`Lorentz.RankFour.apply_contractionTensor_one_of_symm_of_antisymm`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L370).

> A map symmetric in the first two slots and antisymmetric in the last two sends
> `η_{μρ} η_{νσ}` to zero.

```lean
lemma apply_contractionTensor_one_of_symm_of_antisymm
    (hs : f ∘ₗ Tensor.permT _ isReindexing_swap_zero_one = f)
    (ha : f ∘ₗ Tensor.permT _ isReindexing_swap_two_three = -f) :
    f (contractionTensor 1) = 0
```

**`Lorentz.RankFour.apply_contractionTensor_three_of_symm`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L383).

> A map symmetric in the first two slots sends `ε_{μνρσ}` to zero.

```lean
lemma apply_contractionTensor_three_of_symm
    (hs : f ∘ₗ Tensor.permT _ isReindexing_swap_zero_one = f) :
    f (contractionTensor 3) = 0
```

## H. The four tensors are independent

> At `t t x x`, `t x t x`, `t x x t` and `t x y z` exactly one of the four coefficient tensors is
> nonzero, so the four coefficient tensors, and with them the four tensors, are linearly
> independent.

**`Lorentz.RankFour.linearIndependent_contractionCoeff`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L405).

> The four coefficient tensors are linearly independent.

```lean
lemma linearIndependent_contractionCoeff :
    LinearIndependent ℂ fun i d => ((contractionCoeff i d : ℤ) : ℂ)
```

**`Lorentz.RankFour.linearIndependent_contractionTensor`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L431).

> The four tensors are linearly independent.

```lean
lemma linearIndependent_contractionTensor : LinearIndependent ℂ contractionTensor
```

## I. The classification of the invariants

> The Pauli matrices change each four-vector index into a bispinor index, a left-handed and a
> right-handed Weyl index, which is an injective equivariant map
> `complexLorentzTensor.pauliTensorMap 4` into the tensors with four left-handed and then four
> right-handed Weyl indices. Its image of the invariant tensors lies in their invariants, the span of
> the four products of pairings `ε ε ⊗ ε̄ ε̄`
> (`complexLorentzTensor.invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing`). So
> the invariant tensors have dimension at most four, and the four linearly independent invariant
> tensors `contractionTensor i` span them. With them comes the reduction of the invariants of
> `LinearMap.range f ⊔ S` to the span of the four images `f (contractionTensor i)`.

**`complexLorentzTensor.invariants_up_pow_four_eq_span_range_contractionTensor`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L452).

> The invariant tensors with four four-vector indices are the span of the four
> `contractionTensor i`.

```lean
lemma _root_.complexLorentzTensor.invariants_up_pow_four_eq_span_range_contractionTensor :
    (complexLorentzTensor.tensorRep (fun _ : Fin 4 => Color.up)).invariants =
      Submodule.span ℂ (Set.range contractionTensor)
```

**`Lorentz.ComplexVector.reducesInvariantsTo_span_contractionTensor`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean#L477).

> The invariants of the range of `f` reduce to the span of the images of the four invariant
> tensors.

```lean
lemma _root_.Lorentz.ComplexVector.reducesInvariantsTo_span_contractionTensor
    (hf : complexLorentzTensor.IsEquivariant (fun _ : Fin 4 => .up) repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
      (Submodule.span ℂ (Set.range fun i => f (contractionTensor i)))
```

## Depends on

- [The Minkowski matrix over the integers](../minkowskimatrix.md)
- [Invariant coefficient tensors of the complex vector representation](complextensor-vector-invariantcoeff.md)

## Proof depends on

- [Contracting the Levi-Civita symbol against a matrix](../../mathematics/part-02/levicivita/basic.md)
- [The metric pairings of bispinor indices](../bispinors/metricpairing.md)
- [The defining relation of the Lorentz group on its entries](../lorentzgroup/basic.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/ContractionTensor.lean)
