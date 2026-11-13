---
declaration: module
origin: cited
lean: ProbabilisticTheory.AlgState, ProbabilisticTheory.AlgState.map_one, ProbabilisticTheory.AlgState.map_star, ProbabilisticTheory.AlgState.nonneg, ProbabilisticTheory.AlgState.map_add, ProbabilisticTheory.AlgState.map_smul, ProbabilisticTheory.AlgState.PreGNS, ProbabilisticTheory.AlgState.toPre
statement: formalized
proof: formalized
---

# The GNS representation of a state on a unital `*`-algebra

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.GNS`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean): 35 declarations (5 instances with no name), 15 with a docstring.

> A state on a unital complex `*`-algebra defines a Hilbert space, the completion of the algebra for
> the inner product `⟨a, b⟩ = ω(a* b)`, on which a group of state preserving `*`-automorphisms acts
> unitarily.

## i. Overview

> A *state* on a unital complex `*`-algebra `A` is a linear functional `ω` with `ω(1) = 1`,
> `ω(a*) = conj ω(a)`, and `ω(a* a) ≥ 0` for every `a`. The form `⟨a, b⟩ = ω(a* b)` is a positive
> semidefinite inner product on `A`, and the quotient by its null vectors, completed, is the
> *GNS Hilbert space*. No norm on `A` is needed, so the construction applies to algebras that are
> not complete, such as the quasi-local algebra of an infinite lattice before completion.
>
> A `*`-automorphism `σ` of `A` that preserves `ω` preserves the inner product, so it defines an
> isometry on the pre-Hilbert space, and a unitary operator on the GNS space. A group of such
> automorphisms is represented unitarily, and each unitary fixes the class of the unit, the
> cyclic vector.

## ii. Key results

> - `AlgState` : a state on a unital `*`-algebra.
> - `AlgState.GNS` : the Hilbert space of a state.
> - `AlgState.gnsAut` : the unitary implementing a state preserving automorphism.
> - `AlgState.gnsRep` : the unitary representation of a group of state preserving automorphisms.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 2.3.

## A. States and the pre-Hilbert space

**`ProbabilisticTheory.AlgState`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L65).

> A state on a unital complex `*`-algebra: a normalized, Hermitian, positive linear
> functional.

```lean
structure AlgState (A : Type*) [Ring A] [Algebra ℂ A] [StarRing A] [StarModule ℂ A] where
  /-- The linear functional. -/
  toLinearMap : A →ₗ[ℂ] ℂ
  /-- The state is normalized. -/
  map_one' : toLinearMap 1 = 1
  /-- The state is Hermitian. -/
  map_star' : ∀ a, toLinearMap (star a) = star (toLinearMap a)
  /-- The state is positive. -/
  nonneg' : ∀ a, 0 ≤ toLinearMap (star a * a)
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L79).

```lean
instance : FunLike (AlgState A) A ℂ
```

**`ProbabilisticTheory.AlgState.map_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L89).

```lean
lemma map_one : ω 1 = 1
```

**`ProbabilisticTheory.AlgState.map_star`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L91).

```lean
lemma map_star (a : A) : ω (star a) = star (ω a)
```

**`ProbabilisticTheory.AlgState.nonneg`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L93).

```lean
lemma nonneg (a : A) : 0 ≤ ω (star a * a)
```

**`ProbabilisticTheory.AlgState.map_add`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L95).

```lean
lemma map_add (a b : A) : ω (a + b) = ω a + ω b
```

**`ProbabilisticTheory.AlgState.map_smul`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L97).

```lean
lemma map_smul (c : ℂ) (a : A) : ω (c • a) = c * ω a
```

**`ProbabilisticTheory.AlgState.PreGNS`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L101).

> The algebra with the inner product induced by a state, before completion.

```lean
def PreGNS (_ω : AlgState A)
```

**An instance with no name**, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L103).

```lean
instance : AddCommGroup ω.PreGNS
```

**An instance with no name**, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L104).

```lean
instance : Module ℂ ω.PreGNS
```

**`ProbabilisticTheory.AlgState.toPre`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L107).

> The identification of the algebra with its pre-Hilbert space.

```lean
def toPre : A ≃ₗ[ℂ] ω.PreGNS
```

**`ProbabilisticTheory.AlgState.ofPre`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L110).

> The identification of the pre-Hilbert space with the algebra.

```lean
def ofPre : ω.PreGNS ≃ₗ[ℂ] A
```

**`ProbabilisticTheory.AlgState.core`**, an abbrev, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L113).

> The inner product `⟨a, b⟩ = ω (a* b)`.

```lean
noncomputable abbrev core : PreInnerProductSpace.Core ℂ ω.PreGNS
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L127).

```lean
noncomputable instance : SeminormedAddCommGroup ω.PreGNS
```

**An instance with no name**, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L130).

```lean
noncomputable instance : InnerProductSpace ℂ ω.PreGNS
```

**`ProbabilisticTheory.AlgState.inner_pre`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L132).

```lean
lemma inner_pre (a b : ω.PreGNS) : ⟪a, b⟫_ℂ = ω (star (ω.ofPre a) * ω.ofPre b)
```

**`ProbabilisticTheory.AlgState.GNS`**, an abbrev, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L136).

> The **GNS Hilbert space** of a state: the completion of the algebra for the inner product
> `⟨a, b⟩ = ω (a* b)`.

```lean
abbrev GNS : Type _
```

## B. Implementing automorphisms

**`ProbabilisticTheory.AlgState.preAut`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L144).

> The map `[a] ↦ [σ a]` on the pre-Hilbert space.

```lean
def preAut : ω.PreGNS →ₗ[ℂ] ω.PreGNS
```

**`ProbabilisticTheory.AlgState.ofPre_preAut`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L147).

```lean
lemma ofPre_preAut (x : ω.PreGNS) : ω.ofPre (preAut ω σ x) = σ (ω.ofPre x)
```

**`ProbabilisticTheory.AlgState.inner_preAut`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L149).

```lean
lemma inner_preAut (hσ : ∀ a, ω (σ a) = ω a) (x y : ω.PreGNS) :
    ⟪preAut ω σ x, preAut ω σ y⟫_ℂ = ⟪x, y⟫_ℂ
```

**`ProbabilisticTheory.AlgState.norm_preAut`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L155).

```lean
lemma norm_preAut (hσ : ∀ a, ω (σ a) = ω a) (x : ω.PreGNS) : ‖preAut ω σ x‖ = ‖x‖
```

**`ProbabilisticTheory.AlgState.preAutCLM`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L162).

> The automorphism as a bounded operator on the pre-Hilbert space.

```lean
def preAutCLM (hσ : ∀ a, ω (σ a) = ω a) : ω.PreGNS →L[ℂ] ω.PreGNS
```

**`ProbabilisticTheory.AlgState.gnsAut`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L166).

> **The operator on the GNS space implementing a state preserving automorphism.**

```lean
def gnsAut (hσ : ∀ a, ω (σ a) = ω a) : ω.GNS →L[ℂ] ω.GNS
```

**`ProbabilisticTheory.AlgState.gnsAut_coe`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L168).

```lean
lemma gnsAut_coe (hσ : ∀ a, ω (σ a) = ω a) (x : ω.PreGNS) :
    gnsAut σ hσ (x : ω.GNS) = ((preAut ω σ x : ω.PreGNS) : ω.GNS)
```

**`ProbabilisticTheory.AlgState.inner_gnsAut`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L172).

```lean
lemma inner_gnsAut (hσ : ∀ a, ω (σ a) = ω a) (x y : ω.GNS) :
    ⟪gnsAut σ hσ x, gnsAut σ hσ y⟫_ℂ = ⟪x, y⟫_ℂ
```

## C. Representations of groups

**`ProbabilisticTheory.AlgState.gnsAut_mul`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L190).

```lean
lemma gnsAut_mul (g h : Γ) :
    gnsAut (α (g * h)) (hα (g * h)) = gnsAut (α g) (hα g) * gnsAut (α h) (hα h)
```

**`ProbabilisticTheory.AlgState.gnsAut_one`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L204).

```lean
lemma gnsAut_one : gnsAut (α 1) (hα 1) = 1
```

**`ProbabilisticTheory.AlgState.star_gnsAut_mul_gnsAut`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L216).

```lean
lemma star_gnsAut_mul_gnsAut (g : Γ) :
    star (gnsAut (α g) (hα g)) * gnsAut (α g) (hα g) = 1
```

**`ProbabilisticTheory.AlgState.star_gnsAut`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L222).

```lean
lemma star_gnsAut (g : Γ) : star (gnsAut (α g) (hα g)) = gnsAut (α g⁻¹) (hα g⁻¹)
```

**`ProbabilisticTheory.AlgState.gnsUnitary`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L231).

> **The unitary operator on the GNS space implementing a symmetry** of the state.

```lean
def gnsUnitary (g : Γ) : unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`ProbabilisticTheory.AlgState.gnsRep`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L239).

> **The unitary representation of a group of symmetries on the GNS space of an invariant
> state.**

```lean
def gnsRep : Γ →* unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`ProbabilisticTheory.AlgState.cyclicVector`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L245).

> The cyclic vector: the class of the unit.

```lean
def cyclicVector : ω.GNS
```

## D. Composition and commutation of implementing operators

**`ProbabilisticTheory.AlgState.gnsAut_comp`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L258).

> The operator implementing a composite of automorphisms is the composite of the operators.

```lean
lemma gnsAut_comp :
    gnsAut (σ * τ) (fun a => by rw [StarAlgEquiv.mul_apply, hσ, hτ]) =
      gnsAut σ hσ * gnsAut τ hτ
```

**`ProbabilisticTheory.AlgState.gnsAut_congr`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L272).

> Equal automorphisms are implemented by equal operators.

```lean
lemma gnsAut_congr {σ τ : A ≃⋆ₐ[ℂ] A} (h : σ = τ) (hσ : ∀ a, ω (σ a) = ω a)
    (hτ : ∀ a, ω (τ a) = ω a) : gnsAut σ hσ = gnsAut τ hτ
```

**`ProbabilisticTheory.AlgState.gnsAut_commute`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean#L277).

> Commuting automorphisms are implemented by commuting operators.

```lean
lemma gnsAut_commute {σ τ : A ≃⋆ₐ[ℂ] A} (hσ : ∀ a, ω (σ a) = ω a) (hτ : ∀ a, ω (τ a) = ω a)
    (h : σ * τ = τ * σ) : Commute (gnsAut σ hσ) (gnsAut τ hτ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/GNS.lean)
