---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.relativelyRepresentable_of_isFlat_of_mono, AlgebraicGeometry.Space.isIso_of_mono_of_forall_baseChange_mono_fSharp, AlgebraicGeometry.Space.isIso_of_mono_of_isQuasiCompact_of_isFlat_of_isSurjective
statement: formalized
proof: formalized
---

# 76.4 Monomorphisms

Section 76.4 of the Stacks Project, [Tag 0B89](https://stacks.math.columbia.edu/tag/0B89). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B8A, a lemma

[Tag 0B8A](https://stacks.math.columbia.edu/tag/0B8A) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_of_isFlat_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatMonomorphismRepresentable.lean, line 712](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatMonomorphismRepresentable.lean#L712).

> **Stacks 0B8A** (David Rydh). A flat monomorphism of algebraic spaces is representable by
> schemes.

```lean
theorem relativelyRepresentable_of_isFlat_of_mono {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) [Mono f]
    (hf : IsFlat B S hS f) : yoneda.relativelyRepresentable f
```

## Tag 0B8B, a lemma

[Tag 0B8B](https://stacks.math.columbia.edu/tag/0B8B) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_mono_of_forall_baseChange_mono_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonomorphismInjectiveStructureMap.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MonomorphismInjectiveStructureMap.lean#L699).

> **Stacks 0B8B.** A quasi-compact monomorphism of algebraic spaces over `S` whose structure
> homomorphism `𝒪_T ⟶ f_{T,*}𝒪_{X ×_Y T}` is a monomorphism for every `T ⟶ Y` is an
> isomorphism.

```lean
public theorem isIso_of_mono_of_forall_baseChange_mono_fSharp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hqc : Space.IsQuasiCompact B S hS f.hom) [Mono f]
    (hinj : ∀ (T : AlgebraicSpaces B S hS) (g : T ⟶ Y),
      Mono (Space.smallEtaleRingedToposHom B S hS
        (ObjectProperty.homMk (pullback.fst g.hom f.hom) :
          AlgebraicSpaces.fiberProduct B S hS g f ⟶ T)).fSharp) :
    IsIso f
```

## Tag 0B8C, a lemma

[Tag 0B8C](https://stacks.math.columbia.edu/tag/0B8C) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_mono_of_isQuasiCompact_of_isFlat_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatSurjectiveMonomorphism.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatSurjectiveMonomorphism.lean#L138).

> **Stacks 0B8C.** A quasi-compact, flat and surjective monomorphism of algebraic spaces
> over `S` is an isomorphism.

```lean
theorem isIso_of_mono_of_isQuasiCompact_of_isFlat_of_isSurjective
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) [Mono f]
    (hqc : IsQuasiCompact B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (hsurj : IsSurjective B S hS f.hom) :
    IsIso f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.4, Tag 0B89](https://stacks.math.columbia.edu/tag/0B89)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
