---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsBounded, ProbabilisticTheory.AlgState.norm_sq_le_of_isBounded, ProbabilisticTheory.sumSq_map, ProbabilisticTheory.IsBounded.map, ProbabilisticTheory.exists_tendsto_state, ProbabilisticTheory.AlgState.limit, ProbabilisticTheory.AlgState.tendsto_limit, ProbabilisticTheory.starAlgEquiv_smul
statement: formalized
proof: formalized
---

# Invariant states by Følner averaging

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Invariant`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean): 24 declarations, 18 with a docstring.

> A state of a `*`-algebra with a group of automorphisms has invariant limit points, obtained by
> averaging over larger and larger finite subsets of the group.

## i. Overview

> A system in thermal equilibrium on an infinite crystal need not be translation invariant, because
> the Gibbs states of finite boxes see the boundary of the box. Averaging a state `φ` over the
> translates `α_g` with `g` in a finite set `F` gives the state `φ_F = |F|⁻¹ ∑_{g ∈ F} φ ∘ α_g`.
> When the sets `F` become invariant under right translation, `|F h Δ F| / |F| → 0` for every `h`
> (a Følner condition), the averaged states become invariant: `φ_F ∘ α_h - φ_F → 0`. If the values
> of the averaged states on each observable are bounded, they have limit points along an
> ultrafilter, and every limit point is an invariant state.
>
> Nothing is assumed about the algebra beyond a bound `a* a + p = c · 1` with `p` a sum of squares
> for each observable `a`. The statement therefore holds for the quasi-local algebra of any net,
> quantum or classical, and for every state, in particular for the thermodynamic limit states of a
> Gibbs ensemble.

## ii. Key results

> - `IsBounded` : an observable is bounded by a multiple of the identity up to a sum of squares.
> - `AlgState.limit` : the ultrafilter limit of a bounded net of states.
> - `AlgState.average` : the average of a state over a finite set of automorphisms.
> - `AlgState.invariantLimit` : the limit of Følner averages.
> - `AlgState.invariantLimit_invariant` : the limit state is invariant under the group.

## iv. References

> * F. Greenleaf, Invariant Means on Topological Groups.
> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 4.3.

## A. Bounded observables

**`ProbabilisticTheory.IsBounded`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L71).

> An observable `a` is **bounded** if some multiple `c · 1` of the identity exceeds `a* a` by a
> sum of squares.

```lean
def IsBounded (a : A) : Prop
```

**`ProbabilisticTheory.AlgState.norm_sq_le_of_isBounded`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L75).

> **Every state is bounded on a bounded observable**, by the same constant.

```lean
lemma AlgState.norm_sq_le_of_isBounded {a : A} {c : ℝ} {p : A} (hp : p ∈ sumSq A)
    (h : star a * a + p = (c : ℂ) • (1 : A)) (ω : AlgState A) : ‖ω a‖ ^ 2 ≤ c
```

**`ProbabilisticTheory.sumSq_map`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L91).

> A star-algebra equivalence maps sums of squares to sums of squares.

```lean
lemma sumSq_map {B : Type*} [Ring B] [Algebra ℂ B] [StarRing B]
    (σ : A ≃⋆ₐ[ℂ] B) {p : A} (hp : p ∈ sumSq A) : σ p ∈ sumSq B
```

**`ProbabilisticTheory.IsBounded.map`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L102).

> A star-algebra automorphism preserves boundedness.

```lean
lemma IsBounded.map {a : A} (ha : IsBounded a) (σ : A ≃⋆ₐ[ℂ] A) : IsBounded (σ a)
```

## B. Limits of states

**`ProbabilisticTheory.exists_tendsto_state`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L115).

> The values of a bounded net of states on an observable have a limit along an ultrafilter.

```lean
lemma exists_tendsto_state (ψ : ι → AlgState A) (𝒰 : Ultrafilter ι)
    (hb : ∀ a : A, ∃ c : ℝ, ∀ i, ‖ψ i a‖ ≤ c) (a : A) :
    ∃ z, Tendsto (fun i => ψ i a) 𝒰 (𝓝 z)
```

**`ProbabilisticTheory.AlgState.limit`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L126).

> **The limit of a bounded net of states along an ultrafilter** is a state.

```lean
def AlgState.limit (ψ : ι → AlgState A) (𝒰 : Ultrafilter ι)
    (hb : ∀ a : A, ∃ c : ℝ, ∀ i, ‖ψ i a‖ ≤ c) : AlgState A
```

**`ProbabilisticTheory.AlgState.tendsto_limit`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L160).

```lean
lemma AlgState.tendsto_limit (ψ : ι → AlgState A) (𝒰 : Ultrafilter ι)
    (hb : ∀ a : A, ∃ c : ℝ, ∀ i, ‖ψ i a‖ ≤ c) (a : A) :
    Tendsto (fun i => ψ i a) 𝒰 (𝓝 (AlgState.limit ψ 𝒰 hb a))
```

## C. Averages over a finite set of automorphisms

**`ProbabilisticTheory.starAlgEquiv_smul`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L174).

```lean
lemma starAlgEquiv_smul (σ : A ≃⋆ₐ[ℂ] A) (c : ℂ) (a : A) : σ (c • a) = c • σ a
```

**`ProbabilisticTheory.averageMap`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L178).

> The linear functional `a ↦ |F|⁻¹ ∑_{g ∈ F} φ (α g a)`.

```lean
def averageMap (φ : AlgState A) (α : Γ → (A ≃⋆ₐ[ℂ] A)) (F : Finset Γ) : A →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.averageMap_apply`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L186).

```lean
lemma averageMap_apply (φ : AlgState A) (α : Γ → (A ≃⋆ₐ[ℂ] A)) (F : Finset Γ) (a : A) :
    averageMap φ α F a = ((F.card : ℂ))⁻¹ * ∑ g ∈ F, φ (α g a)
```

**`ProbabilisticTheory.AlgState.average`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L190).

> **The average of a state over a finite set of automorphisms** is a state.

```lean
def AlgState.average (φ : AlgState A) (α : Γ → (A ≃⋆ₐ[ℂ] A)) (F : Finset Γ)
    (hF : F.Nonempty) : AlgState A
```

**`ProbabilisticTheory.AlgState.average_apply`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L212).

```lean
lemma AlgState.average_apply (φ : AlgState A) (α : Γ → (A ≃⋆ₐ[ℂ] A)) (F : Finset Γ)
    (hF : F.Nonempty) (a : A) :
    φ.average α F hF a = ((F.card : ℂ))⁻¹ * ∑ g ∈ F, φ (α g a)
```

## D. Invariance of Følner limits

**`ProbabilisticTheory.compMap`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L225).

> The linear functional `a ↦ φ (σ a)`.

```lean
def compMap (φ : AlgState A) (σ : A ≃⋆ₐ[ℂ] A) : A →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.compMap_apply`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L230).

```lean
lemma compMap_apply (φ : AlgState A) (σ : A ≃⋆ₐ[ℂ] A) (a : A) : compMap φ σ a = φ (σ a)
```

**`ProbabilisticTheory.AlgState.comp`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L233).

> **The composition of a state with an automorphism** is a state.

```lean
def AlgState.comp (φ : AlgState A) (σ : A ≃⋆ₐ[ℂ] A) : AlgState A
```

**`ProbabilisticTheory.AlgState.comp_apply`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L242).

```lean
lemma AlgState.comp_apply (φ : AlgState A) (σ : A ≃⋆ₐ[ℂ] A) (a : A) : φ.comp σ a = φ (σ a)
```

**`ProbabilisticTheory.AlgState.norm_le_of_isBounded`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L246).

> The bound on a state on a bounded observable, as a norm bound.

```lean
lemma AlgState.norm_le_of_isBounded {a : A} {c : ℝ} {p : A} (hp : p ∈ sumSq A)
    (h : star a * a + p = (c : ℂ) • (1 : A)) (ω : AlgState A) : ‖ω a‖ ≤ c + 1
```

**`ProbabilisticTheory.norm_sum_sub_le`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L254).

> A difference of two sums of a bounded function is bounded by the size of the symmetric
> difference of the index sets.

```lean
lemma norm_sum_sub_le (f : Γ → ℂ) (C : ℝ) (hf : ∀ k, ‖f k‖ ≤ C) (S T : Finset Γ) :
    ‖∑ k ∈ S, f k - ∑ k ∈ T, f k‖ ≤ ((S \ T).card + (T \ S).card) * C
```

**`ProbabilisticTheory.IsRightFolner`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L271).

> The finite sets `F i` are **asymptotically invariant under right translation** along an
> ultrafilter (a Følner condition): `|F h Δ F| / |F| → 0` for every `h`.

```lean
def IsRightFolner (F : ι → Finset Γ) (𝒰 : Ultrafilter ι) : Prop
```

**`ProbabilisticTheory.average_bounded`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L279).

> The averaged states of a state over the sets `F i` are bounded on every observable.

```lean
lemma average_bounded (φ : AlgState A) (hb : ∀ a : A, IsBounded a) (a : A) :
    ∃ c : ℝ, ∀ i, ‖(φ.average (fun g => α g) (F i) (hne i)) a‖ ≤ c
```

**`ProbabilisticTheory.AlgState.invariantLimit`**, a def, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L300).

> **The Følner limit of a state**: the ultrafilter limit of its averages over the sets `F i`.

```lean
def AlgState.invariantLimit (φ : AlgState A) (hb : ∀ a : A, IsBounded a) (𝒰 : Ultrafilter ι) :
    AlgState A
```

**`ProbabilisticTheory.AlgState.invariantLimit_invariant`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L308).

> **The Følner limit of a state is invariant.** When the sets `F i` are asymptotically invariant
> under right translation along `𝒰`, every limit of the averages of a state over them is invariant
> under the group.

```lean
lemma AlgState.invariantLimit_invariant (φ : AlgState A) (hb : ∀ a : A, IsBounded a)
    (𝒰 : Ultrafilter ι) (hF : IsRightFolner F 𝒰) (h : Γ) (a : A) :
    AlgState.invariantLimit α F hne φ hb 𝒰 (α h a) = AlgState.invariantLimit α F hne φ hb 𝒰 a
```

## E. Boundedness in the quasi-local algebra

**`ProbabilisticTheory.sumSq_map_hom`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L353).

> A star-algebra homomorphism maps sums of squares to sums of squares.

```lean
lemma sumSq_map_hom {B : Type*} [Ring B] [Algebra ℂ B] [StarRing B]
    (σ : A →⋆ₐ[ℂ] B) {p : A} (hp : p ∈ sumSq A) : σ p ∈ sumSq B
```

**`ProbabilisticTheory.AlgebraNet.isBounded_of_isLocallyBounded`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean#L364).

> **Every observable of the quasi-local algebra of a locally bounded net is bounded.**

```lean
lemma AlgebraNet.isBounded_of_isLocallyBounded (hb : N.IsLocallyBounded) (x : N.Quasilocal) :
    IsBounded x
```

## Depends on

- [Limit states of the quasi-local algebra](../quasilocal/limit.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Invariant.lean)
