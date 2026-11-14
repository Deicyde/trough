---
declaration: module
origin: cited
lean: Lorentz.IsBiLeftWeyl, Lorentz.IsBiRightWeyl, Lorentz.IsBiDualLeftWeyl, Lorentz.IsBiDualRightWeyl, Lorentz.basis_repr_smul_pair, Lorentz.basis_repr_pair_eq_neg_swap_of_invariant, Lorentz.exists_eq_smul_metricTensor_of_invariant, Lorentz.invariantReductionToMetricTensor
statement: formalized
proof: formalized
---

# Lorentz invariants of two Weyl indices of the same kind

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.IsBiLeftWeyl`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean): 20 declarations, 20 with a docstring.

## i. Overview

> Let `k` be one of the four Weyl colours and `f : ℂT[k, k] →ₗ[ℂ] B` a Lorentz-equivariant linear
> map. Every Lorentz invariant in the range of `f` is a multiple of `f (metricTensor k)`, the
> image of the `ε` metric of that colour, the shape of a Majorana or Dirac mass term. That is
> `exists_smul_map_metricTensor_add_of_invariant`, stated modulo a
> Lorentz-stable submodule `S`, and packaged for the reductions of the Standard Model as
> `invariantReductionToMetricTensor`. The families with two left-handed,
> two right-handed, two dual left-handed and two dual right-handed indices are `IsBiLeftWeyl`,
> `IsBiRightWeyl`, `IsBiDualLeftWeyl` and `IsBiDualRightWeyl` (A).
>
> By `TensorSpecies.IsEquivariant.invariantReductionToSpan` it is enough to show that the invariant
> tensors of `ℂT[k, k]` are the multiples of `metricTensor k` (B). Two elements of `SL(2,ℂ)` pin
> the components `r` of an invariant tensor down. The first acts on the colour `k` by
> `diag (2, 2⁻¹)`, which scales `r (0, 0)` by `4` and `r (1, 1)` by `4⁻¹`, so these vanish. The
> second acts by an antidiagonal matrix with entries `μ`, `μ² = -1`, which sends `r (0, 1)` to
> `μ² r (1, 0)`, so `r (0, 1) = -r (1, 0)`. For `k = upL` these are the boost along `z` and the
> half turn about `x`; for the other colours they are their images under conjugation and inversion.
> The metric is itself invariant, with a nonzero `(0, 1)` component, so `r` is a multiple of its
> components.

## ii. Key results

> - `IsBiLeftWeyl` : a family with two left-handed Weyl indices `T^{α₁ α₂}`: an equivariant linear map
>   out of `ℂT[.upL, .upL]`
> - `IsBiRightWeyl` : a family with two right-handed Weyl indices `T^{α̇₁ α̇₂}`: an equivariant linear
>   map out of `ℂT[.upR, .upR]`
> - `IsBiDualLeftWeyl` : a family with two dual left-handed Weyl indices `T_{α₁ α₂}`: an equivariant
>   linear map out of `ℂT[.downL, .downL]`
> - `IsBiDualRightWeyl` : a family with two dual right-handed Weyl indices `T_{α̇₁ α̇₂}`: an
>   equivariant linear map out of `ℂT[.downR, .downR]`
> - `invariantReductionToMetricTensor`
> - `exists_smul_map_metricTensor_add_of_invariant` : for a Weyl colour `k` and an equivariant map `f`
>   out of `ℂT[k, k]`, every Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable
>   submodule, is a multiple of the image `f (metricTensor k)` of the metric plus an element of `S`

## iv. References

> * None.

## A. Families with two Weyl indices of the same kind

**`Lorentz.IsBiLeftWeyl`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L75).

> A family with two left-handed Weyl indices `T^{α₁ α₂}`: an equivariant linear map out of
> `ℂT[.upL, .upL]`.

```lean
abbrev IsBiLeftWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.upL, .upL] →ₗ[ℂ] B) : Prop
```

**`Lorentz.IsBiRightWeyl`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L81).

> A family with two right-handed Weyl indices `T^{α̇₁ α̇₂}`: an equivariant linear map out of
> `ℂT[.upR, .upR]`.

```lean
abbrev IsBiRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.upR, .upR] →ₗ[ℂ] B) : Prop
```

**`Lorentz.IsBiDualLeftWeyl`**, an abbrev, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L87).

> A family with two dual left-handed Weyl indices `T_{α₁ α₂}`: an equivariant linear map out
> of `ℂT[.downL, .downL]`.

```lean
abbrev IsBiDualLeftWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.downL, .downL] →ₗ[ℂ] B) : Prop
```

**`Lorentz.IsBiDualRightWeyl`**, an abbrev, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L93).

> A family with two dual right-handed Weyl indices `T_{α̇₁ α̇₂}`: an equivariant linear map
> out of `ℂT[.downR, .downR]`.

```lean
abbrev IsBiDualRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.downR, .downR] →ₗ[ℂ] B) : Prop
```

## B. The invariant tensors with two Weyl indices of the same kind

**`Lorentz.basis_repr_smul_pair`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L109).

> The components of `g • t` for a tensor with two indices: the matrix of `g` in the colour of
> each index acts on that index.

```lean
lemma basis_repr_smul_pair (g : SL(2,ℂ)) (t : ℂT[k, k']) (a : basisIdx k)
    (b : basisIdx k') :
    (Tensor.basis ![k, k']).repr (g • t)
        ((piFinTwoEquiv fun j : Fin 2 => basisIdx (![k, k'] j)).symm (a, b))
      = ∑ x, ∑ y, LinearMap.toMatrix (complexLorentzTensor.basis k)
          (complexLorentzTensor.basis k) (complexLorentzTensor.rep k g) a x *
        LinearMap.toMatrix (complexLorentzTensor.basis k') (complexLorentzTensor.basis k')
          (complexLorentzTensor.rep k' g) b y *
        (Tensor.basis ![k, k']).repr t
          ((piFinTwoEquiv fun j : Fin 2 => basisIdx (![k, k'] j)).symm (x, y))
```

**`Lorentz.basis_repr_pair_eq_neg_swap_of_invariant`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L129).

> The components of an invariant tensor with two Weyl indices of the same colour are
> antisymmetric. The inverse boost along `z` scales the two diagonal components by `4` and `4⁻¹`,
> and the inverse half turn about `x` sends the mixed component `(0, 1)` to minus `(1, 0)`; for
> the dual colours the inverse cancels against the inverse in the matrix of the colour.

```lean
lemma basis_repr_pair_eq_neg_swap_of_invariant
    (hk : k = .upL ∨ k = .downL ∨ k = .upR ∨ k = .downR) {t : ℂT[k, k]}
    (ht : ∀ g : SL(2,ℂ), g • t = t) (a b : basisIdx k) :
    (Tensor.basis ![k, k]).repr t
        ((piFinTwoEquiv fun j : Fin 2 => basisIdx (![k, k] j)).symm (a, b))
      = - (Tensor.basis ![k, k]).repr t
        ((piFinTwoEquiv fun j : Fin 2 => basisIdx (![k, k] j)).symm (b, a))
```

**`Lorentz.exists_eq_smul_metricTensor_of_invariant`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L162).

> The invariant tensors with two Weyl indices of the same colour are the multiples of the
> metric of that colour: both have antisymmetric components, and the `(0, 1)` component of the
> metric does not vanish.

```lean
lemma exists_eq_smul_metricTensor_of_invariant
    (hk : k = .upL ∨ k = .downL ∨ k = .upR ∨ k = .downR) (t : ℂT[k, k])
    (ht : ∀ g : SL(2,ℂ), g • t = t) : ∃ a : ℂ, t = a • metricTensor k
```

## C. The classification of the invariants

**`Lorentz.invariantReductionToMetricTensor`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L217).

> For a Weyl colour `k` and an equivariant map `f` out of `ℂT[k, k]`, the Lorentz invariants
> of the range of `f` reduce to the span of the image `f (metricTensor k)` of the metric.

```lean
noncomputable def invariantReductionToMetricTensor
    (hk : k = .upL ∨ k = .downL ∨ k = .upR ∨ k = .downR)
    (hf : complexLorentzTensor.IsEquivariant ![k, k] repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

**`Lorentz.exists_smul_map_metricTensor_add_of_invariant`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L228).

> For a Weyl colour `k` and an equivariant map `f` out of `ℂT[k, k]`, every Lorentz invariant
> of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is a multiple of the image
> `f (metricTensor k)` of the metric plus an element of `S`.

```lean
lemma exists_smul_map_metricTensor_add_of_invariant
    (hk : k = .upL ∨ k = .downL ∨ k = .upR ∨ k = .downR)
    (hf : complexLorentzTensor.IsEquivariant ![k, k] repLorentz f) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ LinearMap.range f ⊔ S) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ a : ℂ, ∃ y ∈ S, x = a • f (metricTensor k) + y
```

**`Lorentz.IsBiLeftWeyl.invariantReductionToSpan`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L240).

> The Lorentz invariants of the range of a family with two left-handed Weyl indices reduce to
> the span of the image of `εL`.

```lean
noncomputable def IsBiLeftWeyl.invariantReductionToSpan {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[.upL, .upL] →ₗ[ℂ] B}
    (hf : IsBiLeftWeyl B repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

**`Lorentz.IsBiRightWeyl.invariantReductionToSpan`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L248).

> The Lorentz invariants of the range of a family with two right-handed Weyl indices reduce to
> the span of the image of `εR`.

```lean
noncomputable def IsBiRightWeyl.invariantReductionToSpan {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[.upR, .upR] →ₗ[ℂ] B}
    (hf : IsBiRightWeyl B repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

**`Lorentz.IsBiDualLeftWeyl.invariantReductionToSpan`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L256).

> The Lorentz invariants of the range of a family with two dual left-handed Weyl indices
> reduce to the span of the image of `εL'`.

```lean
noncomputable def IsBiDualLeftWeyl.invariantReductionToSpan {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[.downL, .downL] →ₗ[ℂ] B}
    (hf : IsBiDualLeftWeyl B repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

**`Lorentz.IsBiDualRightWeyl.invariantReductionToSpan`**, a def, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L264).

> The Lorentz invariants of the range of a family with two dual right-handed Weyl indices
> reduce to the span of the image of `εR'`.

```lean
noncomputable def IsBiDualRightWeyl.invariantReductionToSpan {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[.downR, .downR] →ₗ[ℂ] B}
    (hf : IsBiDualRightWeyl B repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

## D. Maps from components

> A family of vectors `T a b` indexed by two basis indices is the linear map
> `ofPairComponents T` sending `e_a ⊗ e_b` to `T a b`, and it is equivariant when the vectors are
> moved as the basis tensors are.

**`Lorentz.ofPairComponents`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L285).

> The linear map out of `ℂT[k, k']` sending the basis tensor `e_a ⊗ e_b` to `T a b`.

```lean
noncomputable def ofPairComponents (T : basisIdx k → basisIdx k' → B) :
    ℂT[k, k'] →ₗ[ℂ] B
```

**`Lorentz.range_ofPairComponents`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L290).

> The range of `ofPairComponents T` is the span of the vectors `T a b`.

```lean
lemma range_ofPairComponents (T : basisIdx k → basisIdx k' → B) :
    LinearMap.range (ofPairComponents T)
      = Submodule.span ℂ (Set.range fun m : basisIdx k × basisIdx k' => T m.1 m.2)
```

**`Lorentz.ofPairComponents_mem`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L299).

> The image of `ofPairComponents T` lies in every submodule containing the vectors
> `T a b`.

```lean
lemma ofPairComponents_mem (T : basisIdx k → basisIdx k' → B) {M : Submodule ℂ B}
    (hT : ∀ a b, T a b ∈ M) (t : ℂT[k, k']) : ofPairComponents T t ∈ M
```

**`Lorentz.map_ofPairComponents`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L309).

> A linear map applied after `ofPairComponents T` is `ofPairComponents` of its values on the
> components.

```lean
lemma map_ofPairComponents {B' : Type*} [AddCommGroup B'] [Module ℂ B'] (σ : B →ₗ[ℂ] B')
    (T : basisIdx k → basisIdx k' → B) (t : ℂT[k, k']) :
    σ (ofPairComponents T t) = ofPairComponents (fun a b => σ (T a b)) t
```

**`Lorentz.ofPairComponents_sum`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L317).

> `ofPairComponents` of a sum of families is the sum of the maps.

```lean
lemma ofPairComponents_sum {ι : Type*} (s : Finset ι)
    (T : ι → basisIdx k → basisIdx k' → B) :
    ofPairComponents (fun a b => ∑ i ∈ s, T i a b) = ∑ i ∈ s, ofPairComponents (T i)
```

**`Lorentz.ofPairComponents_sub`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L324).

> `ofPairComponents` of a difference of families is the difference of the maps.

```lean
lemma ofPairComponents_sub (T T' : basisIdx k → basisIdx k' → B) :
    ofPairComponents (fun a b => T a b - T' a b) = ofPairComponents T - ofPairComponents T'
```

**`Lorentz.isEquivariant_ofPairComponents`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean#L330).

> `ofPairComponents T` is equivariant when each index of `T a b` is moved by the matrix of `g`
> in its colour, the summed index first in each factor.

```lean
lemma isEquivariant_ofPairComponents {repLorentz : Representation ℂ SL(2,ℂ) B}
    (T : basisIdx k → basisIdx k' → B)
    (hT : ∀ (g : SL(2,ℂ)) a b, repLorentz g (T a b)
      = ∑ x, ∑ y, (LinearMap.toMatrix (complexLorentzTensor.basis k)
          (complexLorentzTensor.basis k) (complexLorentzTensor.rep k g) x a *
        LinearMap.toMatrix (complexLorentzTensor.basis k') (complexLorentzTensor.basis k')
          (complexLorentzTensor.rep k' g) y b) • T x y) :
    complexLorentzTensor.IsEquivariant ![k, k'] repLorentz (ofPairComponents T)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../../../physlib/relativity/tensors/part-01/complextensor-metrics-basic.md)
- [The colours of complex Lorentz tensors are closed under adjoints](invariants-adjointclosed.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsBiLeftWeyl.lean)
