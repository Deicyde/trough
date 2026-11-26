---
declaration: module
origin: cited
lean: Lorentz.Invariants.act, Lorentz.Invariants.IsInvariantCoeff, Lorentz.sum_pi_fin_two, Lorentz.sum_pi_fin_zero, Lorentz.sum_pi_fin_one, Lorentz.vecCons_fin_one_eta, Lorentz.sum_pi_fin_three, Lorentz.vectorIdx
statement: formalized
proof: formalized
---

# Invariant coefficient tensors of the complex vector representation

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.InvariantCoeff`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean): 23 declarations, 21 with a docstring.

> Invariant coefficient tensors on spacetime indices, and equivariant maps out of the tensors with
> `n` four-vector indices.

## i. Overview

> The tensors `ℂT(fun _ : Fin n => .up)` with `n` contravariant indices are the `n`-th tensor power
> of the complex vector representation `ComplexVector`. This file holds the machinery that the
> classifications of their invariants use: the odd ranks in
> `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction`, rank two in
> `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Basic` and rank four in
> `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.ContractionTensor`.
>
> A real `4 × 4` matrix acts on coefficient tensors one factor per slot, `Invariants.act`, and an
> invariant coefficient tensor is one fixed by the Lorentz matrix of every element of `SL(2, ℂ)`
> (A). Section B collects sums over index vectors.
>
> The components of a tensor, relabelled by `Fin 1 ⊕ Fin 3` in each slot, are a coefficient tensor,
> `coeffEquiv` (C), on which `SL(2,ℂ)` acts by `Invariants.act`. An invariant tensor therefore has
> an invariant coefficient tensor, `Invariants.IsInvariantCoeff`, and a classification of the
> invariant coefficient tensors is a classification of the invariant tensors (D).
>
> A family `T` of vectors indexed by `n` directions is the map `liftComponents T`, sending each basis
> tensor to the matching vector, and it is equivariant exactly when the vectors obey the
> transformation law of the components of a tensor (E, `isEquivariant_liftComponents_up_iff`),
>
> `repLorentz g (T l) = ∑_a (∏ i, Λ(g)_{a i, l i}) • T a`,
>
> with `l` free and `a` summed, and the summed index first in each factor of the Lorentz matrix
> `Λ(g)` of `g`. Permuting the slots by `permT σ` reads the coefficient tensor and the family at
> permuted index vectors (`permT_coeffEquiv_symm`, `liftComponents_comp_permT`). Products of a family
> with a Lorentz-inert element or with a Lorentz vector are again such families (F).

## ii. Key results

> - `Lorentz.Invariants.IsInvariantCoeff` : invariant coefficient tensors.
> - `Lorentz.coeffEquiv` : the components of a tensor with `n` four-vector indices, as a coefficient
>   tensor.
> - `Lorentz.invariant_iff_isInvariantCoeff` : a tensor is invariant exactly when its coefficient
>   tensor is.
> - `Lorentz.invariants_tensorRep_le_map` : the invariant tensors come from the invariant
>   coefficient tensors.
> - `Lorentz.isEquivariant_liftComponents_up_iff` : the map of a family is equivariant exactly when
>   the family obeys the transformation law.
> - `Lorentz.isEquivariant_liftComponents_up_mul_fixed`,
>   `Lorentz.isEquivariant_liftComponents_up_mul_vector` : products of a family with a Lorentz-inert
>   element or with a Lorentz vector.

## iv. References

> * None.

## A. Coefficient tensors on spacetime indices

**`Lorentz.Invariants.act`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L96).

> The action of a real `4 × 4` matrix on coefficient tensors, one factor per slot:
> `(act Λ c) a = ∑_d c_d Λ_{a₀ d₀} ⋯`, with `a` free and `d` summed.

```lean
def act (Λ : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (a : Fin n → Fin 1 ⊕ Fin 3) : ℂ
```

**`Lorentz.Invariants.IsInvariantCoeff`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L101).

> A coefficient tensor fixed by `act` of the Lorentz matrix of every `g : SL(2,ℂ)`.

```lean
def IsInvariantCoeff (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) : Prop
```

## B. Sums over index vectors

**`Lorentz.sum_pi_fin_two`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L118).

> A sum over families of two four-vector indices is a double sum.

```lean
lemma sum_pi_fin_two {M : Type*} [AddCommMonoid M] (f : (Fin 2 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 2 → Fin 1 ⊕ Fin 3, f d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, f ![x, y]
```

**`Lorentz.sum_pi_fin_zero`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L130).

> A sum over families of no four-vector indices is its single term.

```lean
lemma sum_pi_fin_zero {M : Type*} [AddCommMonoid M] (f : (Fin 0 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 0 → Fin 1 ⊕ Fin 3, f d = f ![]
```

**`Lorentz.sum_pi_fin_one`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L137).

> A sum over families of one four-vector index is a single sum.

```lean
lemma sum_pi_fin_one {M : Type*} [AddCommMonoid M] (f : (Fin 1 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 1 → Fin 1 ⊕ Fin 3, f d = ∑ x : Fin 1 ⊕ Fin 3, f ![x]
```

**`Lorentz.vecCons_fin_one_eta`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L146).

> A family of one four-vector index is the tuple of its own entry.

```lean
lemma vecCons_fin_one_eta (l : Fin 1 → Fin 1 ⊕ Fin 3) : ![l 0] = l
```

**`Lorentz.sum_pi_fin_three`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L152).

> A sum over families of three four-vector indices is a triple sum.

```lean
lemma sum_pi_fin_three {M : Type*} [AddCommMonoid M] (f : (Fin 3 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 3 → Fin 1 ⊕ Fin 3, f d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, ∑ z : Fin 1 ⊕ Fin 3, f ![x, y, z]
```

## C. Coefficient tensors

**`Lorentz.vectorIdx`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L180).

> The component indices of a tensor with `n` contravariant indices, which are labelled by
> `Fin 1 ⊕ Fin 3` in each slot.

```lean
def vectorIdx (n : ℕ) :
    ComponentIdx (S := complexLorentzTensor) (fun _ : Fin n => Color.up)
      ≃ (Fin n → Fin 1 ⊕ Fin 3)
```

**`Lorentz.vectorIdx_symm_apply`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L185).

```lean
lemma vectorIdx_symm_apply (d : Fin n → Fin 1 ⊕ Fin 3) (i : Fin n) :
    (vectorIdx n).symm d i = d i
```

**`Lorentz.coeffEquiv`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L190).

> The components of a tensor with `n` contravariant indices, as a coefficient tensor, the
> component equivalence of the species for the labels `vectorIdx n`.

```lean
noncomputable def coeffEquiv (n : ℕ) :
    ℂT(fun _ : Fin n => Color.up) ≃ₗ[ℂ] ((Fin n → Fin 1 ⊕ Fin 3) → ℂ)
```

**`Lorentz.coeffEquiv_apply`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L194).

```lean
lemma coeffEquiv_apply (t : ℂT(fun _ : Fin n => Color.up)) (d : Fin n → Fin 1 ⊕ Fin 3) :
    coeffEquiv n t d = (Tensor.basis _).repr t ((vectorIdx n).symm d)
```

**`Lorentz.coeffEquiv_symm_apply`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L199).

> The tensor with coefficient tensor `c` is the combination of the basis tensors with those
> coefficients.

```lean
lemma coeffEquiv_symm_apply (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    (coeffEquiv n).symm c = ∑ d, c d • Tensor.basis _ ((vectorIdx n).symm d)
```

**`Lorentz.permT_coeffEquiv_symm`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L210).

> Permuting the slots of a tensor by `σ` permutes its coefficient tensor: slot `i` of
> `permT σ h t` holds slot `σ i` of `t`, so the new coefficient at `d` is the old one at
> `d ∘ σ.symm`.

```lean
lemma permT_coeffEquiv_symm (σ : Equiv.Perm (Fin n))
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    permT σ h ((coeffEquiv n).symm c) = (coeffEquiv n).symm fun d => c (d ∘ σ.symm)
```

**`Lorentz.coeffEquiv_smul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L226).

> The action of `g` on tensors is the action `act` of its Lorentz matrix on coefficient
> tensors.

```lean
lemma coeffEquiv_smul (g : SL(2,ℂ)) (t : ℂT(fun _ : Fin n => Color.up)) :
    coeffEquiv n (g • t) = act (SL2C.toLorentzGroup g).1 (coeffEquiv n t)
```

**`Lorentz.invariant_iff_isInvariantCoeff`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L239).

> A tensor is invariant exactly when its coefficient tensor is an invariant coefficient
> tensor.

```lean
lemma invariant_iff_isInvariantCoeff (t : ℂT(fun _ : Fin n => Color.up)) :
    (∀ g : SL(2,ℂ), g • t = t) ↔ IsInvariantCoeff (coeffEquiv n t)
```

## D. Invariant tensors from invariant coefficient tensors

**`Lorentz.invariants_tensorRep_le_map`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L254).

> The invariant tensors lie in the image of any submodule `K` of coefficient tensors which
> contains every invariant coefficient tensor.

```lean
lemma invariants_tensorRep_le_map {n : ℕ} {K : Submodule ℂ ((Fin n → Fin 1 ⊕ Fin 3) → ℂ)}
    (hK : ∀ c, IsInvariantCoeff c → c ∈ K) :
    (complexLorentzTensor.tensorRep (fun _ : Fin n => Color.up)).invariants ≤
      K.map (coeffEquiv n).symm.toLinearMap
```

## E. Maps from components

**`Lorentz.liftComponents_coeffEquiv_symm`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L272).

> The map of a family contracts the coefficient tensor of its argument with the family.

```lean
lemma liftComponents_coeffEquiv_symm (T : (Fin n → Fin 1 ⊕ Fin 3) → B)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    liftComponents T ((coeffEquiv n).symm c)
      = ∑ d, c d • T d
```

**`Lorentz.liftComponents_comp_permT`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L281).

> Precomposing the map of a family with the slot permutation `permT σ` reads the family at the
> permuted index vectors `d ∘ σ`.

```lean
lemma liftComponents_comp_permT (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) T ∘ₗ permT σ h
      = liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) fun d => T (d ∘ σ)
```

**`Lorentz.liftComponents_comp_permT_eq_neg`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L292).

> A family antisymmetric under reading its index vectors through `σ` gives a map
> antisymmetric under `permT σ`.

```lean
lemma liftComponents_comp_permT_eq_neg (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B} (hT : ∀ d, T (d ∘ σ) = -T d) :
    liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) T ∘ₗ permT σ h
      = -liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) T
```

**`Lorentz.liftComponents_comp_permT_eq_self`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L302).

> A family symmetric under reading its index vectors through `σ` gives a map invariant under
> `permT σ`.

```lean
lemma liftComponents_comp_permT_eq_self (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B} (hT : ∀ d, T (d ∘ σ) = T d) :
    liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) T ∘ₗ permT σ h
      = liftComponents (S := complexLorentzTensor) (c := fun _ : Fin n => .up) T
```

**`Lorentz.isEquivariant_liftComponents_up_iff`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L312).

> The map of a family is equivariant exactly when the family obeys the transformation law of
> the components of a tensor with `n` four-vector indices.

```lean
lemma isEquivariant_liftComponents_up_iff {repLorentz : Representation ℂ SL(2,ℂ) B}
    (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin n => .up) repLorentz (liftComponents T) ↔
      ∀ (g : SL(2,ℂ)) l, repLorentz g (T l) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
        (∏ i, (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • T a
```

## F. Products of families in an algebra

> When the families take values in an algebra on which `SL(2,ℂ)` acts multiplicatively, a family
> times a Lorentz-inert element keeps its rank, and a rank-two family times a Lorentz vector is a
> rank-three family.

**`Lorentz.isEquivariant_liftComponents_up_mul_fixed`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L340).

> Multiplying a Lorentz tensor family by a Lorentz-inert element gives a family of the
> same rank, the element riding through the transformation law untouched.

```lean
lemma isEquivariant_liftComponents_up_mul_fixed {n : ℕ}
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B}
    (hT : complexLorentzTensor.IsEquivariant (fun _ : Fin n => .up) repLorentz (liftComponents T))
    {y : B} (hy : ∀ g : SL(2,ℂ), repLorentz g y = y) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin n => .up) repLorentz
      (liftComponents fun d => T d * y)
```

**`Lorentz.isEquivariant_liftComponents_up_mul_vector`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean#L353).

> A rank-two family against a Lorentz vector is a rank-three family, the two covector
> indices of the first factor and the single index of the second make three.

```lean
lemma isEquivariant_liftComponents_up_mul_vector
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {T : (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hT : complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentz (liftComponents T))
    {U : (Fin 1 ⊕ Fin 3) → B}
    (hU : ∀ (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3), repLorentz g (U μ)
      = ∑ ν : Fin 1 ⊕ Fin 3, (((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ) • U ν) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 3 => .up) repLorentz
      (liftComponents fun d : Fin 3 → Fin 1 ⊕ Fin 3 => T ![d 0, d 1] * U (d 2))
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Equivariant maps out of the tensors of a species](equivariant.md)

## Proof depends on

- [Reynolds elements for complex Lorentz tensors](../lorentzgroup/invariants-reynolds.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/InvariantCoeff.lean)
