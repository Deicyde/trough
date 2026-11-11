---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_openSubspace_of_fpqcCovering, AlgebraicGeometry.Space.existsUnique_desc_of_fpqcCovering
statement: formalized
proof: formalized
---

# 74.7 Fpqc coverings

Section 74.7 of the Stacks Project, [Tag 04P0](https://stacks.math.columbia.edu/tag/04P0). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04P1, a lemma

[Tag 04P1](https://stacks.math.columbia.edu/tag/04P1) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_openSubspace_of_fpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcOpenSubspaceDescent.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcOpenSubspaceDescent.lean#L420).

> A family of open subspaces `Wᵢ i` of the members of an fpqc covering `f i : Tᵢ i ⟶ T` whose
> two pullbacks to each `Tᵢ i ×_T Tᵢ j` agree is the family of preimages of a unique open subspace
> of `T`.

```lean
public theorem existsUnique_openSubspace_of_fpqcCovering
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {T : AlgebraicSpaces B S hS}
    {Tᵢ : I → AlgebraicSpaces B S hS}
    (f : ∀ i, Tᵢ i ⟶ T)
    (hf : IsFpqcCovering B S hS (fun i => (f i).hom))
    (Wᵢ : ∀ i, {W : Subfunctor (Tᵢ i).1 // IsOpenSubspace B S hS W})
    (hW : ∀ i j,
      (Wᵢ i).1.preimage (pullback.fst (f i).hom (f j).hom) =
        (Wᵢ j).1.preimage (pullback.snd (f i).hom (f j).hom)) :
    ∃! W : {W : Subfunctor T.1 // IsOpenSubspace B S hS W},
      ∀ i, W.1.preimage (f i).hom = (Wᵢ i).1
```

## Tag 04P2, a lemma

[Tag 04P2](https://stacks.math.columbia.edu/tag/04P2) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_desc_of_fpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcMorphismDescent.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcMorphismDescent.lean#L485).

> **Stacks 04P2.** For an fpqc covering `{X i ⟶ Y}` of algebraic spaces over `S` and an
> algebraic space `Z` over `S`, the diagram
> `Mor(Y, Z) ⟶ ∏ i, Mor(X i, Z) ⇉ ∏ (i, j), Mor(X i ×_Y X j, Z)` is an equalizer: a family of
> morphisms `X i ⟶ Z` agreeing on the fibre products `X i ×_Y X j` descends uniquely to `Y ⟶ Z`.
>
> The input is Stacks 0APL, that an algebraic space is a sheaf for the fpqc topology; the rest is
> formal.

```lean
public theorem existsUnique_desc_of_fpqcCovering
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {X : I → AlgebraicSpaces B S hS}
    {Y : AlgebraicSpaces B S hS}
    (f : ∀ i, X i ⟶ Y)
    (hf : IsFpqcCovering B S hS (fun i => (f i).hom))
    (Z : AlgebraicSpaces B S hS)
    (g : ∀ i, X i ⟶ Z)
    (hg : ∀ i j,
      (ObjectProperty.homMk (pullback.fst (f i).hom (f j).hom) :
        AlgebraicSpaces.fiberProduct B S hS (f i) (f j) ⟶ X i) ≫ g i =
      (ObjectProperty.homMk (pullback.snd (f i).hom (f j).hom) :
        AlgebraicSpaces.fiberProduct B S hS (f i) (f j) ⟶ X j) ≫ g j) :
    ∃! h : Y ⟶ Z, ∀ i, f i ≫ h = g i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.7, Tag 04P0](https://stacks.math.columbia.edu/tag/04P0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
