---
declaration: module
origin: cited
lean: Module.End.apply_eq_zero_of_sl2_relations, Module.End.toContinuousLinearMap_symm_apply, Matrix.sl2E, Matrix.sl2F, Matrix.sl2H, Matrix.lie_sl2H_sl2E, Matrix.lie_sl2H_sl2F, Matrix.lie_sl2E_sl2F
statement: formalized
proof: formalized
---

# The standard sl₂ triple

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Triple`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean): 15 declarations, 15 with a docstring.

> The matrices `e`, `f`, `h` of `sl(2, ℂ)`, and the vanishing of their images on the generalized
> kernel of the Casimir.

## i. Overview

> Three operators `H`, `E`, `F` satisfying the `sl₂` relations `[H, E] = 2E`, `[H, F] = -2F` and
> `[E, F] = H` all vanish on the generalized kernel of their Casimir `H² + 2H + 4FE` (A). This is
> the operator form of `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Casimir`.
>
> The standard triple `sl2E`, `sl2F`, `sl2H` of `2 × 2` matrices spans the traceless matrices (B).
> For a map `φ` out of the `2 × 2` matrices preserving brackets, its Casimir `sl2Casimir φ` is the
> Casimir of the images of the triple, and on its generalized kernel `φ` vanishes on every
> traceless matrix (C).

## ii. Key results

> - `Module.End.apply_eq_zero_of_sl2_relations` : operators with the `sl₂` relations vanish on the
>   generalized kernel of their Casimir.
> - `Matrix.sl2E`, `Matrix.sl2F`, `Matrix.sl2H` : the standard `sl₂` triple.
> - `Matrix.eq_sl2_of_trace_eq_zero` : a traceless matrix is a combination of the triple.
> - `Matrix.sl2Casimir` : the Casimir of the images of the triple.
> - `Matrix.apply_eq_zero_of_mem_maxGenEigenspace_sl2Casimir` : on the generalized kernel of the
>   Casimir a bracket-preserving map vanishes on traceless matrices.

## iv. References

> - J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*.

## A. Operators satisfying the sl₂ relations

**`Module.End.apply_eq_zero_of_sl2_relations`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L67).

> Three endomorphisms `H`, `E`, `F` satisfying the `sl₂` relations all vanish on the generalized
> kernel of their Casimir `H² + 2H + 4FE`.

```lean
lemma apply_eq_zero_of_sl2_relations {H E F : Module.End ℂ V} (hHE : H * E - E * H = 2 • E)
    (hHF : H * F - F * H = -(2 • F)) (hEF : E * F - F * E = H) {v : V}
    (hv : v ∈ (H * H + 2 • H + 4 • (F * E)).maxGenEigenspace 0) :
    E v = 0 ∧ F v = 0 ∧ H v = 0
```

**`Module.End.toContinuousLinearMap_symm_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L86).

> The linear map underlying a continuous linear map on a finite-dimensional space acts as it
> does.

```lean
lemma toContinuousLinearMap_symm_apply {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    [FiniteDimensional ℂ E] (A : E →L[ℂ] E) (w : E) :
    (Module.End.toContinuousLinearMap E).symm A w = A w
```

## B. The standard sl₂ triple

**`Matrix.sl2E`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L102).

> The raising element `e` of the standard `sl₂` triple of `2 × 2` matrices.

```lean
def sl2E : Matrix (Fin 2) (Fin 2) ℂ
```

**`Matrix.sl2F`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L105).

> The lowering element `f` of the standard `sl₂` triple of `2 × 2` matrices.

```lean
def sl2F : Matrix (Fin 2) (Fin 2) ℂ
```

**`Matrix.sl2H`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L108).

> The Cartan element `h` of the standard `sl₂` triple of `2 × 2` matrices.

```lean
def sl2H : Matrix (Fin 2) (Fin 2) ℂ
```

**`Matrix.lie_sl2H_sl2E`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L111).

> The bracket `[h, e] = 2 e`.

```lean
lemma lie_sl2H_sl2E : ⁅sl2H, sl2E⁆ = ((2 : ℝ) : ℂ) • sl2E
```

**`Matrix.lie_sl2H_sl2F`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L117).

> The bracket `[h, f] = -2 f`.

```lean
lemma lie_sl2H_sl2F : ⁅sl2H, sl2F⁆ = ((-2 : ℝ) : ℂ) • sl2F
```

**`Matrix.lie_sl2E_sl2F`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L123).

> The bracket `[e, f] = h`.

```lean
lemma lie_sl2E_sl2F : ⁅sl2E, sl2F⁆ = sl2H
```

**`Matrix.eq_sl2_of_trace_eq_zero`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L128).

> A traceless `2 × 2` matrix is a complex combination of the standard `sl₂` triple.

```lean
lemma eq_sl2_of_trace_eq_zero {X : Matrix (Fin 2) (Fin 2) ℂ} (htr : X.trace = 0) :
    X = X 0 1 • sl2E + X 1 0 • sl2F + X 0 0 • sl2H
```

## C. Images of the triple

**`Matrix.sl2Casimir`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L149).

> The Casimir `H² + 2H + 4FE` of the images `H`, `E`, `F` of the standard `sl₂` triple under a
> map `φ` into an algebra.

```lean
def sl2Casimir (φ : Matrix (Fin 2) (Fin 2) ℂ → B) : B
```

**`Matrix.sl2_relations`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L154).

> The images of the standard `sl₂` triple under a map preserving brackets and real multiples
> satisfy the `sl₂` relations.

```lean
lemma sl2_relations {φ : Matrix (Fin 2) (Fin 2) ℂ → B} (hlie : ∀ X Y, ⁅φ X, φ Y⁆ = φ ⁅X, Y⁆)
    (hsmul : ∀ (r : ℝ) X, φ ((r : ℂ) • X) = (r : ℂ) • φ X) :
    φ sl2H * φ sl2E - φ sl2E * φ sl2H = 2 • φ sl2E ∧
      φ sl2H * φ sl2F - φ sl2F * φ sl2H = -(2 • φ sl2F) ∧
      φ sl2E * φ sl2F - φ sl2F * φ sl2E = φ sl2H
```

**`Matrix.sl2Casimir_mem`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L168).

> The Casimir of a map whose values lie in a subspace closed under multiplication lies in that
> subspace.

```lean
lemma sl2Casimir_mem {φ : Matrix (Fin 2) (Fin 2) ℂ → B} {S : Submodule ℂ B}
    (hS : ∀ a ∈ S, ∀ b ∈ S, a * b ∈ S) (hφ : ∀ X, φ X ∈ S) : sl2Casimir φ ∈ S
```

**`Matrix.commute_sl2Casimir`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L175).

> The Casimirs of two maps with commuting values commute.

```lean
lemma commute_sl2Casimir {φ χ : Matrix (Fin 2) (Fin 2) ℂ → B}
    (h : ∀ X Y, Commute (φ X) (χ Y)) : Commute (sl2Casimir φ) (sl2Casimir χ)
```

**`Matrix.apply_eq_zero_of_sl2`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L185).

> A map from `2 × 2` matrices, additive and scaling each matrix by some complex number, which
> kills a vector on the standard `sl₂` triple, kills it on every traceless matrix.

```lean
lemma apply_eq_zero_of_sl2 {V : Type*} [AddCommGroup V] [Module ℂ V]
    {φ : Matrix (Fin 2) (Fin 2) ℂ → Module.End ℂ V} (hadd : ∀ X Y, φ (X + Y) = φ X + φ Y)
    (hsmul : ∀ (c : ℂ) X, ∃ c' : ℂ, φ (c • X) = c' • φ X) {v : V} (hE : φ sl2E v = 0)
    (hF : φ sl2F v = 0) (hH : φ sl2H v = 0) {X : Matrix (Fin 2) (Fin 2) ℂ} (htr : X.trace = 0) :
    φ X v = 0
```

**`Matrix.apply_eq_zero_of_mem_maxGenEigenspace_sl2Casimir`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean#L198).

> On the generalized kernel of the Casimir of a map preserving brackets and real multiples, the
> images of the standard `sl₂` triple vanish.

```lean
lemma apply_eq_zero_of_mem_maxGenEigenspace_sl2Casimir {V : Type*} [AddCommGroup V] [Module ℂ V]
    [FiniteDimensional ℂ V] {φ : Matrix (Fin 2) (Fin 2) ℂ → Module.End ℂ V}
    (hlie : ∀ X Y, ⁅φ X, φ Y⁆ = φ ⁅X, Y⁆) (hsmul : ∀ (r : ℝ) X, φ ((r : ℂ) • X) = (r : ℂ) • φ X)
    {v : V} (hv : v ∈ (sl2Casimir φ).maxGenEigenspace 0) :
    φ sl2E v = 0 ∧ φ sl2F v = 0 ∧ φ sl2H v = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [The Casimir of an sl₂ triple](sl2-casimir.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Triple.lean)
