---
declaration: module
origin: cited
lean: CompleteTensorProduct, TensorProduct.instNontrivial, CompleteTensorProduct.instNontrivial, CompleteTensorProduct.coe', CompleteTensorProduct.denseRange_coe, CompleteTensorProduct.coe_zero, CompleteTensorProduct.coe_eq_zero_iff, CompleteTensorProduct.coe_neg
statement: formalized
proof: formalized
---

# Complete tensor product

The module `Physlib.QuantumMechanics.HilbertSpaces.TensorProducts.CompleteTensorProduct`, [Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean): 33 declarations (1 instance with no name), 17 with a docstring.

## i. Overview

> Given two inner product spaces `E` and `F` over `𝕜`, their tensor product `E ⊗[𝕜] F` consists
> of finite sums of simple (a.k.a. pure) tensors `m ⊗ₜ[𝕜] n`. This tensor product is again an inner
> product space with inner product defined by `⟪m ⊗ₜ n, m' ⊗ₜ n'⟫_𝕜 = ⟪m, m'⟫_𝕜 * ⟪n, n'⟫_𝕜`
> on simple tensors and then extended by linearity (c.f. `TensorProduct.instInnerProductSpace`).
>
> However, in general this procedure does not result in a Hilbert space: Cauchy sequences need not
> converge because the tensor product does not contain any \_infinite\_ sums of simple tensors.
> In order to obtain a Hilbert space for use in quantum mechanics, we must \_add in\_ the limits
> of Cauchy sequences by taking the completion.
>
> In this module we define the complete tensor product,
> `CompleteTensorProduct 𝕜 E F := Completion (E ⊗[𝕜] F)` with notation `E ⊗ₕ[𝕜] F` and `E ⊗ₕ F`,
> provide some basic properties for the maps which embed `E ⊗[𝕜] F` into `E ⊗ₕ[𝕜] F`
> and prove that `⊗ₕ` is commutative and associative (up to linear isometric equivalence).

## ii. Key results

> - `CompleteTensorProduct 𝕜 E F` (notation `E ⊗ₕ[𝕜] F` and `E ⊗ₕ F`) :
>     The \_completion\_ of the tensor product of a pair of inner product spaces `E` and `F` over `𝕜`.
> - `CompleteTensorProduct.comm 𝕜 E F` : The linear isometric equivalence between
>     `E ⊗ₕ[𝕜] F` and `F ⊗ₕ[𝕜] E`.
> - `CompleteTensorProduct.assoc 𝕜 E F G` : The linear isometric equivalence between
>     `E ⊗ₕ[𝕜] F ⊗ₕ[𝕜] G` and `E ⊗ₕ[𝕜] (F ⊗ₕ[𝕜] G)`.
> - `CompleteTensorProduct.assoc_tIncl₃ₗᵢ` : On the algebraic threefold tensor product,
>     `CompleteTensorProduct.assoc` reduces to `TensorProduct.assoc`.

## iv. References

> * None.

## A. Definition

**`CompleteTensorProduct`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L73).

> The \_completion\_ of the tensor product of two inner product spaces `E` and `F` over `𝕜`.
> By construction this produces a Hilbert space. The localized notations are `E ⊗ₕ F`
> and `E ⊗ₕ[𝕜] F`, accessed by `open scoped CompleteTensorProduct`.

```lean
def CompleteTensorProduct (𝕜 : Type*) [RCLike 𝕜]
    (E : Type*) [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
    (F : Type*) [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] : Type _
```

## B. Nontrivial

**`TensorProduct.instNontrivial`**, an instance, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L99).

```lean
instance _root_.TensorProduct.instNontrivial : Nontrivial (E ⊗[𝕜] F)
```

**`CompleteTensorProduct.instNontrivial`**, an instance, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L105).

```lean
instance instNontrivial : Nontrivial (E ⊗ₕ[𝕜] F)
```

## C. Coercions

**`CompleteTensorProduct.coe'`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L122).

> The canonical embedding of the tensor product into its completion.

```lean
def coe' : E ⊗[𝕜] F → E ⊗ₕ[𝕜] F
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L125).

> Coercion from `E ⊗[𝕜] F` to its completion.

```lean
instance : Coe (E ⊗[𝕜] F) (E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.denseRange_coe`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L127).

```lean
lemma denseRange_coe : DenseRange (coe' : E ⊗[𝕜] F → E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.coe_zero`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L130).

```lean
lemma coe_zero : (0 : E ⊗[𝕜] F) = (0 : E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.coe_eq_zero_iff`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L134).

```lean
lemma coe_eq_zero_iff : (x : E ⊗ₕ[𝕜] F) = 0 ↔ x = 0
```

**`CompleteTensorProduct.coe_neg`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L137).

```lean
lemma coe_neg : (-x : E ⊗[𝕜] F) = (-x : E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.coe_sub`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L140).

```lean
lemma coe_sub : (x - y : E ⊗[𝕜] F) = (x - y : E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.coe_add`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L143).

```lean
lemma coe_add : (x + y : E ⊗[𝕜] F) = (x + y : E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.coe_smul`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L146).

```lean
lemma coe_smul : (c • x : E ⊗[𝕜] F) = (c • x : E ⊗ₕ[𝕜] F)
```

**`CompleteTensorProduct.inner_coe`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L149).

```lean
lemma inner_coe : ⟪(x : E ⊗ₕ[𝕜] F), (y : E ⊗ₕ[𝕜] F)⟫_𝕜 = ⟪x, y⟫_𝕜
```

**`CompleteTensorProduct.norm_coe`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L152).

```lean
lemma norm_coe : ‖(x : E ⊗ₕ[𝕜] F)‖ = ‖x‖
```

**`CompleteTensorProduct.tInclₗᵢ`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L155).

> The canonical embedding of the tensor product into its completion as a linear isometry.

```lean
def tInclₗᵢ : E ⊗[𝕜] F →ₗᵢ[𝕜] E ⊗ₕ[𝕜] F
```

**`CompleteTensorProduct.coe_tInclₗᵢ`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L158).

```lean
lemma coe_tInclₗᵢ : ⇑(tInclₗᵢ : E ⊗ F →ₗᵢ[𝕜] E ⊗ₕ F) = coe'
```

**`CompleteTensorProduct.tInclL`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L161).

> The canonical embedding of the tensor product into its completion as a continuous linear map.

```lean
def tInclL : E ⊗[𝕜] F →L[𝕜] E ⊗ₕ[𝕜] F
```

**`CompleteTensorProduct.coe_tInclL`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L164).

```lean
lemma coe_tInclL : ⇑(tInclL : E ⊗ F →L[𝕜] E ⊗ₕ F) = coe'
```

**`CompleteTensorProduct.norm_tInclL`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L167).

```lean
lemma norm_tInclL [Nontrivial E] [Nontrivial F] : ‖(tInclL : E ⊗ F →L[𝕜] E ⊗ₕ F)‖ = 1
```

## D. Induction principle

**`CompleteTensorProduct.induction_on`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L183).

> An induction principle for `CompleteTensorProduct` combining those of `Completion`
> and `TensorProduct`.

```lean
lemma induction_on {motive : E ⊗ₕ[𝕜] F → Prop} (z : E ⊗ₕ[𝕜] F)
    (tmul : ∀ (x : E) (y : F), motive (x ⊗ₜ[𝕜] y))
    (add : ∀ x y : E ⊗[𝕜] F, motive x → motive y → motive ↑(x + y))
    (closed : IsClosed {x | motive x}) : motive z
```

## E. Commutative

**`CompleteTensorProduct.comm`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L199).

> The complete tensor product of inner product spaces is commutative,
> up to linear isometric equivalence.

```lean
def comm : E ⊗ₕ[𝕜] F ≃ₗᵢ[𝕜] F ⊗ₕ[𝕜] E
```

**`CompleteTensorProduct.comm_symm`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L204).

```lean
lemma comm_symm : (comm 𝕜 E F).symm = comm 𝕜 F E
```

**`CompleteTensorProduct.comm_coe`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L208).

```lean
lemma comm_coe (x : E ⊗[𝕜] F) : comm 𝕜 E F x = TensorProduct.comm 𝕜 E F x
```

## F. Associative

**`TensorProduct.denseRange_map`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L220).

> The tensor product of a pair of linear maps with dense range also has dense range.

```lean
lemma _root_.TensorProduct.denseRange_map
    {R 𝕜 : Type*} [CommSemiring R] [RCLike 𝕜] {σ : R →+* 𝕜} [RingHomSurjective σ]
    {M : Type*} [AddCommMonoid M] [Module R M] {N : Type*} [AddCommMonoid N] [Module R N]
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
    {F : Type*} [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
    {f : M →ₛₗ[σ] E} (hf : DenseRange f) {g : N →ₛₗ[σ] F} (hg : DenseRange g) :
    DenseRange (TensorProduct.map f g)
```

**`CompleteTensorProduct.assoc`**, a def, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L247).

> The compete tensor product of inner product spaces is associative,
> up to linear isometric equivalence.

```lean
def assoc : E ⊗ₕ[𝕜] F ⊗ₕ[𝕜] G ≃ₗᵢ[𝕜] E ⊗ₕ[𝕜] (F ⊗ₕ[𝕜] G)
```

### F.1. Associativity on the algebraic tensor product

**`CompleteTensorProduct.tIncl₃ₗᵢ`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L271).

> The embedding of the algebraic threefold tensor product `E ⊗[𝕜] F ⊗[𝕜] G` into the complete
> tensor product `E ⊗ₕ[𝕜] F ⊗ₕ[𝕜] G` as a linear isometry: `E ⊗[𝕜] F` is first embedded into
> `E ⊗ₕ[𝕜] F`, then `(E ⊗ₕ[𝕜] F) ⊗[𝕜] G` is embedded into its completion.

```lean
def tIncl₃ₗᵢ : E ⊗[𝕜] F ⊗[𝕜] G →ₗᵢ[𝕜] E ⊗ₕ[𝕜] F ⊗ₕ[𝕜] G
```

**`CompleteTensorProduct.tIncl₃'ₗᵢ`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L277).

> The embedding of the algebraic threefold tensor product `E ⊗[𝕜] (F ⊗[𝕜] G)` into the
> complete tensor product `E ⊗ₕ[𝕜] (F ⊗ₕ[𝕜] G)` as a linear isometry: `F ⊗[𝕜] G` is first
> embedded into `F ⊗ₕ[𝕜] G`, then `E ⊗[𝕜] (F ⊗ₕ[𝕜] G)` is embedded into its completion.

```lean
def tIncl₃'ₗᵢ : E ⊗[𝕜] (F ⊗[𝕜] G) →ₗᵢ[𝕜] E ⊗ₕ[𝕜] (F ⊗ₕ[𝕜] G)
```

**`CompleteTensorProduct.tIncl₃ₗᵢ_tmul`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L282).

> On a simple tensor `x ⊗ₜ y ⊗ₜ z`, the embedding `tIncl₃ₗᵢ` is the nested coercion.

```lean
lemma tIncl₃ₗᵢ_tmul (x : E) (y : F) (z : G) :
    tIncl₃ₗᵢ (x ⊗ₜ[𝕜] y ⊗ₜ[𝕜] z) = (x ⊗ₜ[𝕜] y ⊗ₜ[𝕜] z : (E ⊗ₕ[𝕜] F) ⊗[𝕜] G)
```

**`CompleteTensorProduct.tIncl₃'ₗᵢ_tmul`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L288).

> On a simple tensor `x ⊗ₜ (y ⊗ₜ z)`, the embedding `tIncl₃'ₗᵢ` is the nested coercion.

```lean
lemma tIncl₃'ₗᵢ_tmul (x : E) (y : F) (z : G) :
    tIncl₃'ₗᵢ (x ⊗ₜ[𝕜] (y ⊗ₜ[𝕜] z)) = (x ⊗ₜ[𝕜] (y ⊗ₜ[𝕜] z) : E ⊗[𝕜] (F ⊗ₕ[𝕜] G))
```

**`CompleteTensorProduct.assoc_tIncl₃ₗᵢ`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L295).

> `CompleteTensorProduct.assoc` acting on an element of the algebraic threefold tensor product
> reduces to `TensorProduct.assoc`.

```lean
lemma assoc_tIncl₃ₗᵢ (x : E ⊗[𝕜] F ⊗[𝕜] G) :
    assoc 𝕜 E F G (tIncl₃ₗᵢ x) = tIncl₃'ₗᵢ (TensorProduct.assoc 𝕜 E F G x)
```

**`CompleteTensorProduct.assoc_symm_tIncl₃'ₗᵢ`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L302).

> The inverse of `CompleteTensorProduct.assoc` acting on an element of the algebraic threefold
> tensor product reduces to the inverse of `TensorProduct.assoc`.

```lean
lemma assoc_symm_tIncl₃'ₗᵢ (x : E ⊗[𝕜] (F ⊗[𝕜] G)) :
    (assoc 𝕜 E F G).symm (tIncl₃'ₗᵢ x) = tIncl₃ₗᵢ ((TensorProduct.assoc 𝕜 E F G).symm x)
```

**`CompleteTensorProduct.assoc_tmul`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L308).

> `CompleteTensorProduct.assoc` on simple tensors (c.f. `TensorProduct.assoc_tmul`).

```lean
lemma assoc_tmul (x : E) (y : F) (z : G) :
    assoc 𝕜 E F G (x ⊗ₜ[𝕜] y ⊗ₜ[𝕜] z : (E ⊗ₕ[𝕜] F) ⊗[𝕜] G) =
      (x ⊗ₜ[𝕜] (y ⊗ₜ[𝕜] z) : E ⊗[𝕜] (F ⊗ₕ[𝕜] G))
```

**`CompleteTensorProduct.assoc_symm_tmul`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean#L316).

> The inverse of `CompleteTensorProduct.assoc` on simple tensors
> (c.f. `TensorProduct.assoc_symm_tmul`).

```lean
lemma assoc_symm_tmul (x : E) (y : F) (z : G) :
    (assoc 𝕜 E F G).symm (x ⊗ₜ[𝕜] (y ⊗ₜ[𝕜] z) : E ⊗[𝕜] (F ⊗ₕ[𝕜] G)) =
      (x ⊗ₜ[𝕜] y ⊗ₜ[𝕜] z : (E ⊗ₕ[𝕜] F) ⊗[𝕜] G)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/TensorProducts/CompleteTensorProduct.lean)
