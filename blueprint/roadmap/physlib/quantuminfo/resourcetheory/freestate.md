---
declaration: module
origin: cited
lean: ResourcePretheory.prodRelabel_relabel_cast_prod, FreeStateTheory.IsCompact_IsFree, UnitalFreeStateTheory.RelativeEntResource.tendsto, UnitalFreeStateTheory.RelativeEntResource.tendsto_ennreal, ResourcePretheory, ResourcePretheory.prodRelabel, ResourcePretheory.prodRelabel_assoc, ResourcePretheory.prodCPTPMap
statement: formalized
proof: formalized
---

# QuantumInfo.ResourceTheory.FreeState

The module `QuantumInfo.ResourceTheory.FreeState`, [QuantumInfo/ResourceTheory/FreeState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean): 47 declarations (1 instance with no name), 13 with a docstring, 4 listed as significant.

**`ResourcePretheory`**, a class, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L25).

> A `ResourcePretheory` is a family of Hilbert spaces closed under tensor products, with an
>   instance of `Fintype` and `DecidableEq` for each. It forms a pre-structure then on which to
>   discuss resource theories. For instance, to talk about "two-party scenarios", we could write
>   `ResourcePretheory (ℕ × ℕ)`, with `H (a,b) := (Fin a) × (Fin b)`.
>
> The `Semigroup ι` structure means we have a way to take products of our labels of Hilbert spaces
> in a way that is associative (with actual equality). The `prodEquiv` lets us reinterpret between
> a product-labelled Hilbert spaces, and an actual pair of Hilbert spaces.

```lean
class ResourcePretheory (ι : Type*) extends Semigroup ι where
  /-- The indexing of each Hilbert space -/
  H : ι → Type*
  /-- Each space is finite -/
  [FinH : ∀ i, Fintype (H i)]
  /-- Each object has decidable equality -/
  [DecEqH : ∀ i, DecidableEq (H i)]
  /-- Each space is nonempty (dimension at least 1) -/
  [NonemptyH : ∀ i, Nonempty (H i)]
  /-- The product structure induces an isomorphism of Hilbert spaces -/
  prodEquiv i j : H (i * j) ≃ (H i) × (H j)
  --Possible we want some fact like the associativity of `prod` or the existence of an identity space,
  -- which would then imply MonoidalCategory structure later (instead of just Category). For now we
  -- take the (logically equivalent, in the appropriate model) assumption that the associator is
  -- actually an equality. This is captured in the `Semigroup ι` assumption. If we wanted to turn
  -- this into something more flexible, we would replace that with `Mul ι` (dropping `mul_assoc`)
  -- and get an appropriate associator `Equiv` here.
  hAssoc i j k :
    ((prodEquiv (i * j) k).trans <|
      ((prodEquiv i j).prodCongr (Equiv.refl (H k))).trans <|
      (Equiv.prodAssoc _ _ _).trans <|
      ((Equiv.refl (H i)).prodCongr ((prodEquiv j k).symm)).trans
      (prodEquiv i (j * k)).symm
    )
     = Equiv.cast (congrArg H <| mul_assoc i j k)
```

**`ResourcePretheory.prodRelabel`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L63).

> The `prod` operation of `ResourcePretheory` gives the natural product operation on `MState`s
> that puts us in a new Hilbert space of the category. Accessible by the notation `ρ₁ ⊗ᵣ ρ₂`.

```lean
noncomputable def prodRelabel (ρ₁ : MState (H i)) (ρ₂ : MState (H j)) : MState (H (i * j))
```

**`ResourcePretheory.prodRelabel_assoc`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L69).

```lean
lemma prodRelabel_assoc (ρ₁ : MState (H i)) (ρ₂ : MState (H j)) (ρ₃ : MState (H k)) :
    ρ₁ ⊗ᵣ ρ₂ ⊗ᵣ ρ₃ ≍ ρ₁ ⊗ᵣ (ρ₂ ⊗ᵣ ρ₃)
```

**`ResourcePretheory.prodRelabel_relabel_cast_prod`**, a theorem, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L86). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A `MState.relabel` can be distributed across a `prodRelabel`, if you have proofs that the factors
> correspond correctly.

```lean
theorem prodRelabel_relabel_cast_prod
    (ρ₁ : MState (H i)) (ρ₂ : MState (H j))
    (h : H (k * l) = H (i * j)) (hik : k = i) (hlj : l = j) :
    (ρ₁ ⊗ᵣ ρ₂).relabel (Equiv.cast h) =
    (ρ₁.relabel (Equiv.cast (congrArg H hik))) ⊗ᵣ (ρ₂.relabel (Equiv.cast (congrArg H hlj)))
```

**`ResourcePretheory.prodCPTPMap`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L97).

> The `prod` operation of `ResourcePretheory` gives the natural product operation on `CPTPMap`s. Accessible
> by the notation `M₁ ⊗ᶜᵖᵣ M₂`.

```lean
noncomputable def prodCPTPMap (M₁ : CPTPMap (H i) (H j)) (M₂ : CPTPMap (H k) (H l)) :
    CPTPMap (H (i * k)) (H (j * l))
```

**`ResourcePretheory.PosDef.prod`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L105).

```lean
lemma PosDef.prod {ρ : MState (H i)} {σ : MState (H j)} (hρ : ρ.m.PosDef) (hσ : σ.m.PosDef)
    : (ρ ⊗ᵣ σ).m.PosDef
```

**`ResourcePretheory.qRelEntropy_prodRelabel`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L143).

```lean
lemma qRelEntropy_prodRelabel (ρ₁ ρ₂ : MState (H i)) (σ₁ σ₂ : MState (H j)):
    𝐃(ρ₁ ⊗ᵣ σ₁‖ρ₂ ⊗ᵣ σ₂) = 𝐃(ρ₁‖ρ₂) + 𝐃(σ₁‖σ₂)
```

**`ResourcePretheory.sandwichedRelRentropy_prodRelabel`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L148).

```lean
lemma sandwichedRelRentropy_prodRelabel {α : ℝ} (ρ₁ ρ₂ : MState (H i)) (σ₁ σ₂ : MState (H j)):
    D̃_ α(ρ₁ ⊗ᵣ σ₁‖ρ₂ ⊗ᵣ σ₂) = D̃_ α(ρ₁‖ρ₂) + D̃_ α(σ₁‖σ₂)
```

**`UnitalPretheory`**, a class, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L157).

> A ResourcePretheory is `Unital` if it has a Hilbert space of size 1, i.e. `ℂ`.

```lean
class UnitalPretheory (ι : Type*) extends ResourcePretheory ι, MulOneClass ι, Unique (H 1) where
  prod_default {i} (ρ : MState (H i)) :
    (toResourcePretheory.prodRelabel ρ (Inhabited.default : MState (H 1))) ≍ ρ
  default_prod {i} (ρ : MState (H i)) :
    (toResourcePretheory.prodRelabel (Inhabited.default : MState (H 1)) ρ) ≍ ρ
```

**An instance with no name**, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L167).

```lean
instance : Monoid ι
```

**`UnitalPretheory.spacePow`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L176).

> Powers of spaces.
>
> We define it for `Nat` in a `UnitalPretheory`. In principal this could be done for any
> `ResourcePretheory` and be defined for `PNat` so that we don't have zeroth powers. In
> anticipation that we might some day want that, and that we might do everything with a
> non-equality associator, we keep this as its own definition and keep our own names for
> rewriting theorems where possible.

```lean
noncomputable def spacePow (i : ι) (n : ℕ) : ι
```

**`UnitalPretheory.spacePow_zero`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L184).

```lean
lemma spacePow_zero (i : ι) : i ^ 0 = 1
```

**`UnitalPretheory.spacePow_one`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L188).

```lean
lemma spacePow_one (i : ι) : i ^ 1 = i
```

**`UnitalPretheory.spacePow_succ`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L191).

```lean
lemma spacePow_succ (i : ι) (n : ℕ) : i ^ (n + 1) = (i ^ n) * i
```

**`UnitalPretheory.spacePow_add`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L194).

```lean
lemma spacePow_add (m n : ℕ) :
    i ^ (m + n) = (i ^ m) * (i ^ n)
```

**`UnitalPretheory.spacePow_mul`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L201).

```lean
lemma spacePow_mul (m n : ℕ) :
    i ^ (m * n) = (i ^ m) ^ n
```

**`UnitalPretheory.statePow`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L207).

> Powers of states, using the resource theory's notion of product. Accessible via the notation
> `ρ ⊗ᵣ^[n]`.

```lean
noncomputable def statePow (ρ : MState (H i)) (n : ℕ) : MState (H (i ^ n))
```

**`UnitalPretheory.statePow_zero`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L214).

```lean
lemma statePow_zero (ρ : MState (H i)) : ρ ⊗ᵣ^[0] = default
```

**`UnitalPretheory.statePow_one`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L218).

```lean
lemma statePow_one (ρ : MState (H i)) : ρ ⊗ᵣ^[1] ≍ ρ
```

**`UnitalPretheory.statePow_succ`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L224).

```lean
lemma statePow_succ (ρ : MState (H i)) (n : ℕ) : ρ ⊗ᵣ^[n + 1] = ρ ⊗ᵣ^[n] ⊗ᵣ ρ
```

**`UnitalPretheory.statePow_add`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L227).

```lean
lemma statePow_add (ρ : MState (H i)) (m n : ℕ) : ρ ⊗ᵣ^[m + n] ≍ ρ ⊗ᵣ^[m] ⊗ᵣ ρ ⊗ᵣ^[n]
```

**`UnitalPretheory.statePow_add_relabel`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L240).

```lean
lemma statePow_add_relabel (ρ : MState (H i)) (m n : ℕ) :
    ρ ⊗ᵣ^[m + n] = (ρ ⊗ᵣ^[m] ⊗ᵣ ρ ⊗ᵣ^[n]).relabel (Equiv.cast (by congr; exact pow_add i m n))
```

**`UnitalPretheory.statePow_mul`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L248).

```lean
lemma statePow_mul (ρ : MState (H i)) (m n : ℕ) : ρ ⊗ᵣ^[m * n] ≍ (ρ ⊗ᵣ^[m]) ⊗ᵣ^[n]
```

**`UnitalPretheory.statePow_mul_relabel`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L273).

```lean
lemma statePow_mul_relabel {i : ι} (ρ : MState (H i)) (m n : ℕ) :
   ρ ⊗ᵣ^[m * n] = (ρ ⊗ᵣ^[m]) ⊗ᵣ^[n].relabel (Equiv.cast (congrArg H (pow_mul i m n)))
```

**`UnitalPretheory.PosDef.npow`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L281).

```lean
lemma PosDef.npow {ρ : MState (H i)} (hρ : ρ.m.PosDef) (n : ℕ)
    : (ρ ⊗ᵣ^[n]).m.PosDef
```

**`UnitalPretheory.statePow_rw`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L288).

```lean
lemma statePow_rw {n m : ℕ} (h : n = m) (ρ : MState (H i)) :
    ρ ⊗ᵣ^[n] = (ρ ⊗ᵣ^[m]).relabel (Equiv.cast (by congr))
```

**`UnitalPretheory.qRelEntropy_statePow`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L295).

```lean
lemma qRelEntropy_statePow (ρ σ : MState (H i)) (n : ℕ) :
    𝐃(ρ ⊗ᵣ^[n] ‖ σ  ⊗ᵣ^[n]) = n * 𝐃(ρ‖σ)
```

**`UnitalPretheory.sInf_spectrum_rprod`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L303).

```lean
lemma sInf_spectrum_rprod {j : ι} (ρ : MState (H i)) (σ : MState (H j)) :
    sInf (spectrum ℝ (ρ ⊗ᵣ σ).m) = sInf (spectrum ℝ ρ.m) * sInf (spectrum ℝ σ.m)
```

**`UnitalPretheory.sInf_spectrum_spacePow`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L308).

```lean
lemma sInf_spectrum_spacePow (σ : MState (H i)) (n : ℕ) :
    sInf (spectrum ℝ (σ ⊗ᵣ^[n]).m) = sInf (spectrum ℝ σ.m) ^ n
```

**`UnitalPretheory.sandwichedRelRentropy_statePow`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L323).

```lean
lemma sandwichedRelRentropy_statePow {α : ℝ} (ρ σ : MState (H i)) (n : ℕ) :
    D̃_ α(ρ ⊗ᵣ^[n] ‖ σ ⊗ᵣ^[n]) = n * D̃_ α(ρ‖σ)
```

**`FreeStateTheory`**, a class, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L342).

> A `FreeStateTheory` is a collection of mixed states (`MState`s) in a `ResourcePretheory` that obeys
> some necessary axioms:
>  * For each Hilbert space `H i`, the free states are a closed, convex set
>  * For each Hilbert space `H i`, there is a free state of full rank
>  * If `ρᵢ ∈ H i` and `ρⱼ ∈ H j` are free, then `ρᵢ ⊗ ρⱼ` is free in `H (prod i j)`.

```lean
class FreeStateTheory (ι : Type*) extends ResourcePretheory ι where
  /-- The set of states we're calling "free" -/
  IsFree : Set (MState (toResourcePretheory.H i))
  /-- The set F(H) of free states is closed -/
  free_closed : IsClosed (@IsFree i)
  /-- The set F(H) of free states is convex (more precisely, their matrices are) -/
  free_convex : Convex ℝ (MState.M '' (@IsFree i))
  /-- The set of free states is closed under tensor product -/
  free_prod {ρ₁ : MState (H i)} {ρ₂ : MState (H j)} (h₁ : ρ₁ ∈ IsFree) (h₂ : ρ₂ ∈ IsFree) : (ρ₁ ⊗ᵣ ρ₂) ∈ IsFree
  /-- The set F(H) of free states contains a full-rank state `ρfull`, equivalently `ρfull` is positive definite. -/
  free_fullRank (i : ι) : open ComplexOrder in ∃ (ρ : MState (H i)), ρ.m.PosDef ∧ ρ ∈ IsFree
```

**`FreeStateTheory.Inhabited_IsFree`**, an instance, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L358).

```lean
noncomputable instance Inhabited_IsFree : Inhabited (IsFree (i := i))
```

**`FreeStateTheory.IsFree.of_unique`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L361).

```lean
lemma IsFree.of_unique [Unique (H i)] (ρ : MState (H i)) : ρ ∈ IsFree
```

**`FreeStateTheory.IsCompact_IsFree`**, a theorem, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L367). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The set of free states is compact because it's a closed subset of a compact space.

```lean
theorem IsCompact_IsFree : IsCompact (IsFree (i := i))
```

**`FreeStateTheory.IsFree.mix`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L373).

```lean
lemma IsFree.mix {ι : Type*} [FreeStateTheory ι] {i : ι} {σ₁ σ₂ : MState (H i)}
    (hσ₁ : σ₁ ∈ IsFree) (hσ₂ : σ₂ ∈ IsFree) (p : Prob) : (p [σ₁ ↔ σ₂]) ∈ IsFree
```

**`UnitalFreeStateTheory`**, a class, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L385).

```lean
class UnitalFreeStateTheory (ι : Type*) extends FreeStateTheory ι, UnitalPretheory ι
```

**`FreeStateTheory.IsFree.npow`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L394).

```lean
lemma _root_.FreeStateTheory.IsFree.npow {i : ι} {ρ : MState (H i)}
    (hρ : ρ ∈ IsFree) (n : ℕ) : (ρ ⊗ᵣ^[n]) ∈ IsFree
```

**`UnitalFreeStateTheory.relabel_cast_isFree`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L403).

```lean
lemma relabel_cast_isFree {i j : ι} (ρ : MState (H i)) (h : j = i) {h' : H j = H i}:
    ρ.relabel (Equiv.cast h') ∈ IsFree ↔ ρ ∈ IsFree
```

**`UnitalFreeStateTheory.relativeEntResource_ne_top`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L413).

> In a `FreeStateTheory`, we have free states of full rank, therefore the minimum relative entropy
> of any state `ρ` to a free state is finite.

```lean
lemma relativeEntResource_ne_top (ρ : MState (H i)) : ⨅ σ ∈ IsFree, 𝐃(ρ‖σ) ≠ ⊤
```

**`UnitalFreeStateTheory.RelativeEntResource`**, a def, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L426).

```lean
noncomputable def RelativeEntResource : MState (H i) → ℝ≥0
```

**`UnitalFreeStateTheory.exists_isFree_relativeEntResource`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L432).

```lean
lemma exists_isFree_relativeEntResource (ρ : MState (H i)) :
    ∃ σ ∈ IsFree, 𝐃(ρ‖σ) = 𝑅ᵣ ρ
```

**`UnitalFreeStateTheory.RelativeEntResource.Subadditive`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L441).

```lean
lemma RelativeEntResource.Subadditive (ρ : MState (H i)) :
    Subadditive fun n ↦ (𝑅ᵣ (ρ ⊗ᵣ^[n]) : ℝ)
```

**`UnitalFreeStateTheory.RegularizedRelativeEntResource`**, a def, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L461).

```lean
noncomputable def RegularizedRelativeEntResource (ρ : MState (H i)) : ℝ≥0
```

**`UnitalFreeStateTheory.RelativeEntResource.tendsto`**, a theorem, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L471). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Lemma 5

```lean
theorem RelativeEntResource.tendsto (ρ : MState (H i)) :
    Filter.atTop.Tendsto (fun n ↦ 𝑅ᵣ (ρ ⊗ᵣ^[n]) / n) (𝓝 (𝑅ᵣ∞ ρ))
```

**`UnitalFreeStateTheory.RelativeEntResource.tendsto_ennreal`**, a theorem, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L481). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Alternate version of Lemma 5 which states the convergence with the `ENNReal`
> expression for `RelativeEntResource`, as opposed its `untop`-ped `NNReal` value.

```lean
theorem RelativeEntResource.tendsto_ennreal (ρ : MState (H i)) :
    Filter.atTop.Tendsto (fun n ↦ (⨅ σ ∈ IsFree, 𝐃(ρ ⊗ᵣ^[n]‖σ)) / ↑n) (𝓝 (𝑅ᵣ∞ ρ))
```

**`UnitalFreeStateTheory.GlobalRobustness`**, a def, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L490).

```lean
noncomputable def GlobalRobustness {i : ι} : MState (H i) → ℝ≥0
```

**`UnitalFreeStateTheory.IsAsymptoticallyNongenerating`**, a def, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean#L497).

> A sequence of operations `f_n` is asymptotically nongenerating if `lim_{n→∞} RG(f_n(ρ_n)) = 0`, where
> RG is `GlobalRobustness` and `ρ_n` is any sequence of free states. Equivalently, we can take the `max` (
> over operations and states) on the left-hand side inside the limit.

```lean
def IsAsymptoticallyNongenerating (dI dO : ι) (f : (n : ℕ) → CPTPMap (H (dI⊗^H[n])) (H (dO⊗^H[n]))) : Prop
```

## Depends on

- [QuantumInfo.Entropy.Relative](../entropy/relative.md)

## Proof depends on

- [QuantumInfo.ForMathlib.Minimax](../formathlib/minimax.md)

## Sources

- [QuantumInfo/ResourceTheory/FreeState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ResourceTheory/FreeState.lean)
