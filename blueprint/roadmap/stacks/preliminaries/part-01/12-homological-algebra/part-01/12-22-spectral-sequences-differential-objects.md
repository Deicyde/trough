---
declaration: section
origin: cited
lean: CategoryTheory.DifferentialObject, CategoryTheory.DifferentialObject.Hom, stacksDifferentialObject_abelianStructure, stacksDifferentialObject_abelian, StacksDifferentialObject.homology, StacksDifferentialObject.ShortExactSequence.homology_exact_sequence, StacksDifferentialObject.spectralSequenceOfEndo
statement: formalized
proof: formalized
---

# 12.22 Spectral sequences: differential objects

Section 12.22 of the Stacks Project, [Tag 011U](https://stacks.math.columbia.edu/tag/011U). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 011V, a definition

[Tag 011V](https://stacks.math.columbia.edu/tag/011V) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.DifferentialObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.DifferentialObject#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L36) (StacksFrontier): “object”.
- [`CategoryTheory.DifferentialObject.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.DifferentialObject.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L37) (StacksFrontier): “morphism”.

## Tag 011W, a lemma

[Tag 011W](https://stacks.math.columbia.edu/tag/011W) in the Stacks Project.

**`stacksDifferentialObject_abelianStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L235). The attribute's comment: “structure”.

> The abelian structure on the category of differential objects of an abelian category.

```lean
noncomputable def stacksDifferentialObject_abelianStructure
    (C : Type*) [Category C] [Abelian C] :
    Abelian (StacksDifferentialObject C)
```

**`stacksDifferentialObject_abelian`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L241). The attribute's comment: “nonempty”.

```lean
alias stacksDifferentialObject_abelian
```

## Tag 011X, a definition

[Tag 011X](https://stacks.math.columbia.edu/tag/011X) in the Stacks Project.

**`StacksDifferentialObject.homology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L282).

> The homology `H(A, d) = Ker(d)/Im(d)` of a differential object, as the homology of
> `A --d--> A --d--> A`.

```lean
noncomputable abbrev homology (A : StacksDifferentialObject C) : C
```

## Tag 011Y, a lemma

[Tag 011Y](https://stacks.math.columbia.edu/tag/011Y) in the Stacks Project.

**`StacksDifferentialObject.ShortExactSequence.homology_exact_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialObject.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialObject.lean#L390).

> For a short exact sequence `0 → (A, d) → (B, d) → (C, d) → 0` of
> differential objects there is a connecting morphism `δ : H(C, d) ⟶ H(A, d)` making the periodic
> sequence `H(A, d) → H(B, d) → H(C, d) -δ→ H(A, d) → H(B, d) → ⋯` exact at every spot.

```lean
theorem homology_exact_sequence :
    ∃ (δ : S.C.homology ⟶ S.A.homology)
      (h₁ : S.homologyMap₁ ≫ S.homologyMap₂ = 0)
      (h₂ : S.homologyMap₂ ≫ δ = 0)
      (h₃ : δ ≫ S.homologyMap₁ = 0),
      (ShortComplex.mk S.homologyMap₁ S.homologyMap₂ h₁).Exact ∧
      (ShortComplex.mk S.homologyMap₂ δ h₂).Exact ∧
      (ShortComplex.mk δ S.homologyMap₁ h₃).Exact
```

## Tag 011Z, a definition

[Tag 011Z](https://stacks.math.columbia.edu/tag/011Z) in the Stacks Project.

**`StacksDifferentialObject.spectralSequenceOfEndo`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/DifferentialObject.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/DifferentialObject.lean#L137).

> The spectral sequence `(E_r, d_r)_{r ≥ 0}` associated to a differential object `(A, d)`
> and an injective endomorphism `α` commuting with `d`: `(E_0, d_0) = (A/αA, d)`, and for `r ≥ 1`
> it is the spectral sequence of the exact couple `(H(A, d), H(A/αA, d), H(α), δ, H(π))`, so
> `E_1 = H(A/αA, d)`.

```lean
noncomputable abbrev spectralSequenceOfEndo : Ungraded 𝒜 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.22, Tag 011U](https://stacks.math.columbia.edu/tag/011U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
