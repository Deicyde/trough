---
declaration: section
origin: cited
lean: CommAlgCat.standardResolution, CommAlgCat.cotangentSimplicialModule, CommAlgCat.cotangentComplex, CommAlgCat.existsSliceStandardEndofunctor, CommAlgCat.sliceStandardResolution_iso, CategoryTheory.Over.postAdjunctionRight, CategoryTheory.Over.post_forget_eq_forget_comp, CommAlgCat.isDirectedColimitOfTypes_cotangentComplexAb
statement: formalized
proof: formalized
---

# 92.3 The cotangent complex of a ring map

Section 92.3 of the Stacks Project, [Tag 08PL](https://stacks.math.columbia.edu/tag/08PL). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08PM, a definition

[Tag 08PM](https://stacks.math.columbia.edu/tag/08PM) in the Stacks Project.

**`CommAlgCat.standardResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/StandardResolution.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/StandardResolution.lean#L177).

> **Stacks Project, Tag 08PM.** The standard resolution of the commutative `A`-algebra `B`,
> augmented to `B`. Its degree `n` term is the `(n + 1)`-fold iteration of `C ↦ A[C]`.

```lean
noncomputable def standardResolution (A : Type u) [CommRing A]
    (B : CommAlgCat.{max u v} A) : SimplicialObject.Augmented (CommAlgCat.{max u v} A)
```

## Tag 08PN, a definition

[Tag 08PN](https://stacks.math.columbia.edu/tag/08PN) in the Stacks Project.

**`CommAlgCat.cotangentSimplicialModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Complex.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Complex.lean#L304). The attribute's comment: “the simplicial module”.

> The canonical simplicial `B`-module `Ω[P•⁄A] ⊗[P•] B`.

```lean
noncomputable def cotangentSimplicialModule (A : Type u) [CommRing A]
    (B : CommAlgCat.{max u v} A) : CotangentSimplicialModuleData A B
```

**`CommAlgCat.cotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Complex.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Complex.lean#L335). The attribute's comment: “the associated complex”.

> The cotangent complex `L_{B/A}` associated to the standard resolution.

```lean
noncomputable def cotangentComplex (A : Type u) [CommRing A]
    (B : CommAlgCat.{max u v} A) : CochainComplex (ModuleCat.{max u v} B) ℤ
```

## Tag 08PP, a remark

[Tag 08PP](https://stacks.math.columbia.edu/tag/08PP) in the Stacks Project.

**`CommAlgCat.existsSliceStandardEndofunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SliceStandardResolution.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SliceStandardResolution.lean#L245). The attribute's comment: “the standard endofunctor in the slice”.

> The comonad of the lifted adjunction has a standard augmented simplicial
> endofunctor in the category of algebras over `B`.

```lean
theorem existsSliceStandardEndofunctor :
    ∃ X : SimplicialObject.Augmented (Over B ⥤ Over B),
      IsSliceStandardEndofunctor A B X
```

**`CommAlgCat.sliceStandardResolution_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SliceStandardResolution.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SliceStandardResolution.lean#L320). The attribute's comment: “comparison of standard resolutions”.

> Every standard simplicial endofunctor arising from the slice adjunction, evaluated on
> the identity of `B`, gives the ordinary augmented standard resolution of `B`.

```lean
theorem sliceStandardResolution_iso
    (X : SimplicialObject.Augmented (Over B ⥤ Over B))
    (hX : IsSliceStandardEndofunctor A B X) :
    Nonempty
      (((SimplicialObject.Augmented.whiskeringObj _ _ (Over.forget B)).obj
        ((SimplicialObject.Augmented.whiskeringObj _ _
        ((evaluation (Over B) (Over B)).obj (Over.mk (𝟙 B)))).obj X)) ≅
        standardResolution A B)
```

Declarations registered for the tag:

- [`CategoryTheory.Over.postAdjunctionRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.postAdjunctionRight#doc) registered with `add_to_stacks` in [StacksFrontier/Cotangent/SliceStandardResolution.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SliceStandardResolution.lean#L74) (StacksFrontier): “the adjunction”.
- [`CategoryTheory.Over.post_forget_eq_forget_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.post_forget_eq_forget_comp#doc) registered with `add_to_stacks` in [StacksFrontier/Cotangent/SliceStandardResolution.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SliceStandardResolution.lean#L75) (StacksFrontier): “the commutative square”. References: SGA 3 I (1.6), “more general”.

## Tag 08S9, a lemma

[Tag 08S9](https://stacks.math.columbia.edu/tag/08S9) in the Stacks Project.

**`CommAlgCat.isDirectedColimitOfTypes_cotangentComplexAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/DirectedColimit.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/DirectedColimit.lean#L1057). The attribute's comment: “degreewise”.

> Let `A i → B i` be a system of ring maps over a directed index set `I`, with `Ainf` the
> colimit of the `A i` and `Binf` the colimit of the `B i`. Then in every degree the canonical
> maps induced by the comparison squares exhibit `L_{Binf⁄Ainf}` as the directed colimit of the
> cotangent complexes `L_{B i⁄A i}`, the transition maps of the system being those induced by
> the squares of the system; that is, `colim L_{B i⁄A i} = L_{colim B i⁄colim A i}`.

```lean
theorem CommAlgCat.isDirectedColimitOfTypes_cotangentComplexAb
    (hA : IsDirectedColimitOfTypes (fun _ _ h a => (sq h).base a)
      (fun i a => (cocone i).base a))
    (hB : IsDirectedColimitOfTypes (fun _ _ h b => (sq h).map b)
      (fun i b => (cocone i).map b))
    (n : ℤ) :
    IsDirectedColimitOfTypes
      (fun _ _ h a => (CommAlgCat.cotangentComplexAbMap (sq h)).f n a)
      (fun i a => (CommAlgCat.cotangentComplexAbMap (cocone i)).f n a)
```

**`CommAlgCat.isColimit_cotangentComplexAbCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/DirectedColimit.lean, line 1270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/DirectedColimit.lean#L1270). The attribute's comment: “the colimit of complexes”.

> Cotangent complexes commute with directed colimits of ring maps: the cocone of canonical
> maps `L_{B i⁄A i} → L_{Binf⁄Ainf}` on the system of canonical maps `L_{B i⁄A i} → L_{B j⁄A j}`
> is a colimit cocone.

```lean
noncomputable def CommAlgCat.isColimit_cotangentComplexAbCocone :
    IsColimit (CommAlgCat.cotangentComplexAbCocone sq cocone hA hB)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.3, Tag 08PL](https://stacks.math.columbia.edu/tag/08PL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
