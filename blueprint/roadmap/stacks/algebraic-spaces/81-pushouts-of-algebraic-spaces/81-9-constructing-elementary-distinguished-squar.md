---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPushout_elementaryDistinguishedSquare, AlgebraicGeometry.Space.exists_pushout_isElementaryDistinguishedSquare
statement: formalized
proof: formalized
---

# 81.9 Constructing elementary distinguished squares

Section 81.9 of the Stacks Project, [Tag 0DVH](https://stacks.math.columbia.edu/tag/0DVH). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DVI, a lemma

[Tag 0DVI](https://stacks.math.columbia.edu/tag/0DVI) in the Stacks Project.

**`AlgebraicGeometry.Space.isPushout_elementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ElementaryDistinguishedSquarePushout.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ElementaryDistinguishedSquarePushout.lean#L340).

> **Stacks 0DVI.** An elementary distinguished square is a pushout square in the category
> of algebraic spaces over the base scheme: the target is glued from the open subspace and the
> étale morphism along their fibre product.

```lean
theorem isPushout_elementaryDistinguishedSquare
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {W V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hW : IsAlgebraicSpace B S hS W) (U : Subfunctor W) (f : V ⟶ W)
    (h : IsElementaryDistinguishedSquare B S hS hW U f) :
    IsPushout
      (ObjectProperty.homMk (pullback.snd U.ι f) :
        AlgebraicSpaces.fiberProduct B S hS
            (ObjectProperty.homMk U.ι :
              (⟨U.toFunctor, h.isOpenSubspace.1⟩ : AlgebraicSpaces B S hS) ⟶ ⟨W, hW⟩)
            (ObjectProperty.homMk f :
              (⟨V, h.isAlgebraicSpace⟩ : AlgebraicSpaces B S hS) ⟶ ⟨W, hW⟩) ⟶
          ⟨V, h.isAlgebraicSpace⟩)
      (ObjectProperty.homMk (pullback.fst U.ι f) :
        _ ⟶ (⟨U.toFunctor, h.isOpenSubspace.1⟩ : AlgebraicSpaces B S hS))
      (ObjectProperty.homMk f :
        (⟨V, h.isAlgebraicSpace⟩ : AlgebraicSpaces B S hS) ⟶ ⟨W, hW⟩)
      (ObjectProperty.homMk U.ι :
        (⟨U.toFunctor, h.isOpenSubspace.1⟩ : AlgebraicSpaces B S hS) ⟶ ⟨W, hW⟩)
```

## Tag 0DVJ, a lemma

[Tag 0DVJ](https://stacks.math.columbia.edu/tag/0DVJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_pushout_isElementaryDistinguishedSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ElementaryDistinguishedSquareGluing.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ElementaryDistinguishedSquareGluing.lean#L1158).

> **Stacks 0DVJ.** Let `V` and `U` be algebraic spaces over `S`, let `V'` be an open
> subspace of `V` and let `f' : V' ⟶ U` be a separated étale morphism. Then there is an algebraic
> space `W` over `S` together with an open subspace of `W` isomorphic to `U` and a morphism
> `V ⟶ W` forming an elementary distinguished square, and the resulting square is a pushout of
> `V ← V' → U` in the category of algebraic spaces over `S`.

```lean
theorem exists_pushout_isElementaryDistinguishedSquare
    (U V : AlgebraicSpaces B S hS) (V' : Subfunctor V.obj)
    (hV' : IsOpenSubspace B S hS V') (f' : V'.toFunctor ⟶ U.obj)
    (hf' : IsEtale B S hS f') (hf'sep : IsSeparated B S hS f') :
    ∃ (W : AlgebraicSpaces B S hS) (Uw : Subfunctor W.obj) (e : U.obj ≅ Uw.toFunctor)
      (f : V ⟶ W),
      IsElementaryDistinguishedSquare B S hS W.property Uw f.hom ∧
        IsPushout
          (ObjectProperty.homMk V'.ι :
            (⟨V'.toFunctor, hV'.1⟩ : AlgebraicSpaces B S hS) ⟶ V)
          (ObjectProperty.homMk f' :
            (⟨V'.toFunctor, hV'.1⟩ : AlgebraicSpaces B S hS) ⟶ U)
          f (ObjectProperty.homMk (e.hom ≫ Uw.ι) : U ⟶ W)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.9, Tag 0DVH](https://stacks.math.columbia.edu/tag/0DVH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
