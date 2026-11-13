---
declaration: module
origin: cited
lean: QuantumMechanics.FiniteHilbertSpace, QuantumMechanics.FiniteHilbertSpace.equivEuclidean, QuantumMechanics.FiniteHilbertSpace.val_add, QuantumMechanics.FiniteHilbertSpace.val_smul, QuantumMechanics.FiniteHilbertSpace.val_zero, QuantumMechanics.FiniteHilbertSpace.linearEquivEuclidean, QuantumMechanics.FiniteHilbertSpace.norm_eq_val, QuantumMechanics.FiniteHilbertSpace.inner_eq_val
statement: formalized
proof: formalized
---

# The Hilbert space of a finite target quantum mechanical system

The module `Physlib.QuantumMechanics.HilbertSpaces.FiniteTarget.Basic`, [Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean): 17 declarations (6 instances with no name), 5 with a docstring.

> A finite target quantum mechanical system is one whose states live in a finite
> dimensional Hilbert space, with the basis states labelled by a finite type `d`
> (for example the sites of a finite lattice, or the levels of a qudit).
>
> This file contains
> - the definition of `FiniteHilbertSpace d`, the Hilbert space of such a system,
>   as a structure wrapping `EuclideanSpace ℂ d`, together with the notation `𝓗[d]`;
> - its vector space structure (`AddCommGroup` and `Module ℂ`), transferred from
>   `EuclideanSpace ℂ d` along the equivalence `equivEuclidean`;
> - its Hilbert space structure (`NormedAddCommGroup`, `InnerProductSpace ℂ`,
>   `FiniteDimensional ℂ` and `CompleteSpace`), induced along `linearEquivEuclidean`;
> - the standard orthonormal basis `basisFun`, whose elements are the states
>   localized at the points of `d`.

**`QuantumMechanics.FiniteHilbertSpace`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L62).

> The Hilbert space of a finite target quantum mechanical system whose target is
> a finite type `d` with decidable equality.
>
> It is defined as a structure with a single field `val`, wrapping an element of
> `EuclideanSpace ℂ d` — the space of functions `d → ℂ` carrying the `L²` inner
> product `⟪ψ, φ⟫ = ∑ i, conj (ψ i) * φ i`. Using a structure in preference to
> `EuclideanSpace ℂ d` itself makes the Hilbert space of states a type of its own,
> with its own API and the notation `𝓗[d]`.
>
> Being finite dimensional, it is automatically a complete inner product space,
> that is, a genuine Hilbert space.

```lean
structure FiniteHilbertSpace (d : Type*) [Fintype d] [DecidableEq d] where
  /-- The underlying element of `EuclideanSpace ℂ d`. -/
  val : EuclideanSpace ℂ d
```

**`QuantumMechanics.FiniteHilbertSpace.equivEuclidean`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L75).

> The equivalence between `FiniteHilbertSpace d` and `EuclideanSpace ℂ d`
> given by `val`.

```lean
def equivEuclidean : FiniteHilbertSpace d ≃ EuclideanSpace ℂ d
```

## The vector space structure on `FiniteHilbertSpace d`

> The vector space structure is transferred from `EuclideanSpace ℂ d`
> along the equivalence `equivEuclidean`.

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L90).

```lean
noncomputable instance : AddCommGroup (FiniteHilbertSpace d)
```

**An instance with no name**, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L92).

```lean
noncomputable instance : Module ℂ (FiniteHilbertSpace d)
```

**`QuantumMechanics.FiniteHilbertSpace.val_add`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L96).

```lean
lemma val_add (ψ φ : FiniteHilbertSpace d) : (ψ + φ).val = ψ.val + φ.val
```

**`QuantumMechanics.FiniteHilbertSpace.val_smul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L99).

```lean
lemma val_smul (c : ℂ) (ψ : FiniteHilbertSpace d) : (c • ψ).val = c • ψ.val
```

**`QuantumMechanics.FiniteHilbertSpace.val_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L102).

```lean
lemma val_zero : (0 : FiniteHilbertSpace d).val = 0
```

**`QuantumMechanics.FiniteHilbertSpace.linearEquivEuclidean`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L106).

> The equivalence between `FiniteHilbertSpace d` and `EuclideanSpace ℂ d`
> as a `ℂ`-linear equivalence, upgrading `equivEuclidean`.

```lean
noncomputable def linearEquivEuclidean : FiniteHilbertSpace d ≃ₗ[ℂ] EuclideanSpace ℂ d
```

## The Hilbert space structure on `FiniteHilbertSpace d`

> The norm and inner product are induced from `EuclideanSpace ℂ d` along
> `linearEquivEuclidean`, making `FiniteHilbertSpace d` a finite dimensional
> (and hence complete) inner product space, that is, a Hilbert space.

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L121).

```lean
noncomputable instance : NormedAddCommGroup (FiniteHilbertSpace d)
```

**`QuantumMechanics.FiniteHilbertSpace.norm_eq_val`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L125).

```lean
lemma norm_eq_val (ψ : FiniteHilbertSpace d) : ‖ψ‖ = ‖ψ.val‖
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L127).

```lean
noncomputable instance : InnerProductSpace ℂ (FiniteHilbertSpace d)
```

**`QuantumMechanics.FiniteHilbertSpace.inner_eq_val`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L131).

```lean
lemma inner_eq_val (ψ φ : FiniteHilbertSpace d) : inner ℂ ψ φ = inner ℂ ψ.val φ.val
```

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L133).

```lean
instance : FiniteDimensional ℂ (FiniteHilbertSpace d)
```

**An instance with no name**, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L136).

```lean
instance : CompleteSpace (FiniteHilbertSpace d)
```

**`QuantumMechanics.FiniteHilbertSpace.isometryEquivEuclidean`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L140).

> The equivalence between `FiniteHilbertSpace d` and `EuclideanSpace ℂ d`
> as a linear isometry equivalence, upgrading `linearEquivEuclidean`.

```lean
noncomputable def isometryEquivEuclidean : FiniteHilbertSpace d ≃ₗᵢ[ℂ] EuclideanSpace ℂ d
```

## The standard orthonormal basis of `FiniteHilbertSpace d`

**`QuantumMechanics.FiniteHilbertSpace.basisFun`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L151).

> The standard orthonormal basis of `FiniteHilbertSpace d`, indexed by `d`.

```lean
noncomputable def basisFun (d : Type*) [Fintype d] [DecidableEq d] :
    OrthonormalBasis d ℂ (FiniteHilbertSpace d)
```

**`QuantumMechanics.FiniteHilbertSpace.basisFun_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean#L155).

```lean
lemma basisFun_apply (i : d) : basisFun d i = ⟨EuclideanSpace.single i 1⟩
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/FiniteTarget/Basic.lean)
