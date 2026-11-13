---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isColimit_algebraicSpaces_of_scheme, AlgebraicGeometry.Space.isColimit_of_fpqc_local, AlgebraicGeometry.Space.isColimit_of_etale_local_affine_descent, AlgebraicGeometry.Space.isColimit_of_separated_etale_descent
statement: formalized
proof: formalized
---

# 81.3 Colimits of algebraic spaces

Section 81.3 of the Stacks Project, [Tag 0GFN](https://stacks.math.columbia.edu/tag/0GFN). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07SX, a lemma

[Tag 07SX](https://stacks.math.columbia.edu/tag/07SX) in the Stacks Project.

**`AlgebraicGeometry.Space.isColimit_algebraicSpaces_of_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Colimits.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Colimits.lean#L415).

> Under descent of separated étale families and preservation of the scheme
> colimit by étale base change, the colimit is also a colimit of algebraic spaces.

```lean
public theorem isColimit_algebraicSpaces_of_scheme
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type u} [Category.{u} I]
    (D : I ⥤ BigFppfOver B S hS) (c : Cocone D)
    (_hColimit : IsColimit ((BigFppfOver.toScheme B S hS).mapCocone c))
    (hCover : ∀ x : (BigFppfOver.toScheme B S hS).obj c.pt,
      ∃ (i : I) (y : (BigFppfOver.toScheme B S hS).obj (D.obj i)),
        (BigFppfOver.toScheme B S hS).map (c.ι.app i) y = x)
    (hEtaleColimit :
      ∀ (U : BigFppfOver B S hS) (v : U ⟶ c.pt),
        Etale ((BigFppfOver.toScheme B S hS).map v) →
        ∀ (E : I ⥤ BigFppfOver B S hS) (p : E ⟶ D)
          (q : E ⟶ (Functor.const I).obj U),
          (∀ i, IsPullback (p.app i) (q.app i) (c.ι.app i) v) →
          IsColimit ((BigFppfOver.toScheme B S hS).mapCocone
            ({ pt := U, ι := q } : Cocone E)))
    (hEtaleDescent :
      ∀ (E : I ⥤ BigFppfOver B S hS) (p : E ⟶ D),
        (∀ i, Etale ((BigFppfOver.toScheme B S hS).map (p.app i))) →
        (∀ i, _root_.AlgebraicGeometry.IsSeparated
          ((BigFppfOver.toScheme B S hS).map (p.app i))) →
        (∀ {i j : I} (f : i ⟶ j),
          IsPullback (E.map f) (p.app i) (p.app j) (D.map f)) →
        ∃ (U : BigFppfOver B S hS) (v : U ⟶ c.pt)
          (q : E ⟶ (Functor.const I).obj U),
          Etale ((BigFppfOver.toScheme B S hS).map v) ∧
          (∀ i, IsPullback (p.app i) (q.app i) (c.ι.app i) v)) :
    ∀ (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u),
      IsAlgebraicSpace B S hS F →
      ∀ (a : ∀ i : I, yoneda.obj (D.obj i) ⟶ F),
        (∀ {i j : I} (f : i ⟶ j), yoneda.map (D.map f) ≫ a j = a i) →
        ∃! b : yoneda.obj c.pt ⟶ F,
          ∀ i, yoneda.map (c.ι.app i) ≫ b = a i
```

## Tag 0GFQ, a lemma

[Tag 0GFQ](https://stacks.math.columbia.edu/tag/0GFQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isColimit_of_fpqc_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ColimitsFpqcLocal.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ColimitsFpqcLocal.lean#L92).

> **[Stacks, Tag 0GFQ].** Let `T` be an algebraic space over a scheme `S` of a big fppf site
> and let `D` be a diagram of algebraic spaces over `T` with a cocone `c`. Suppose given an fpqc
> covering `f a : (d a).pt ⟶ c.pt` of the vertex such that
>
> * every `d a` is a cocone on a diagram `E a` whose squares over `D` are cartesian, and `d a` is
>   a colimit; and
> * every pairwise overlap `d₂ a b` of the covering is likewise a cocone on a cartesian diagram
>   `E₂ a b` over `D` and is a colimit.
>
> Then `c` is a colimit of `D` in the category of algebraic spaces over `T`.
>
> The base algebraic space is the source's `B`; it is called `T` here because `B` names the big
> fppf site throughout this library.

```lean
theorem isColimit_of_fpqc_local
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {T : AlgebraicSpaces B S hS}
    {I : Type v} [Category.{w} I] (D : I ⥤ Over T) (c : Cocone D)
    {A : Type t}
    (E : A → I ⥤ Over T) (d : ∀ a, Cocone (E a))
    (p : ∀ a, E a ⟶ D)
    (f : ∀ a, (d a).pt ⟶ c.pt)
    (hcover : IsFpqcCovering B S hS fun a => ((f a).left).hom)
    (hbase : ∀ (a : A) (i : I),
      IsPullback ((p a).app i).left ((d a).ι.app i).left (c.ι.app i).left (f a).left)
    (hlocal : ∀ a, Nonempty (IsColimit (d a)))
    (E₂ : A → A → I ⥤ Over T)
    (d₂ : ∀ a b, Cocone (E₂ a b))
    (p₂ : ∀ a b, E₂ a b ⟶ D)
    (toFirst : ∀ a b, (d₂ a b).pt ⟶ (d a).pt)
    (toSecond : ∀ a b, (d₂ a b).pt ⟶ (d b).pt)
    (hoverlap : ∀ a b, IsPullback (toFirst a b).left (toSecond a b).left (f a).left (f b).left)
    (hbaseOverlap : ∀ (a b : A) (i : I),
      IsPullback ((p₂ a b).app i).left ((d₂ a b).ι.app i).left
        (c.ι.app i).left (toFirst a b ≫ f a).left)
    (hoverlapColimit : ∀ a b, Nonempty (IsColimit (d₂ a b))) :
    Nonempty (IsColimit c)
```

## Tag 0GHL, a lemma

[Tag 0GHL](https://stacks.math.columbia.edu/tag/0GHL) in the Stacks Project.

**`AlgebraicGeometry.Space.isColimit_of_etale_local_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/EtaleLocalAffineColimit.lean, line 1200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/EtaleLocalAffineColimit.lean#L1200).

> **Stacks 0GHL.** Let `B` be an algebraic space over `S`, let `D` be a diagram of algebraic
> spaces over `B` and let `c` be a cocone on `D`. If base change along the cocone legs is an
> equivalence from the small étale site of the vertex onto the limit of the small étale sites of
> the members, and if every cocone of morphisms from the base changes of an affine étale
> realization to an affine space over an affine étale base descends uniquely, then `c` is a
> colimit of `D` in the category of algebraic spaces over `B`.

```lean
theorem isColimit_of_etale_local_affine_descent
    {I : Type v} [Category.{w} I]
    {B : AlgebraicSpaces site S hS} {D : I ⥤ Over B}
    (c : Cocone D)
    (h₁ : EtaleComparisonIsEquivalence site S hS c)
    (h₂ : ∀ (B' : AlgebraicSpaces site S hS) (b : B' ⟶ B),
      IsAffineSpace site S hS B'.1 →
      IsEtale site S hS b.hom →
      ∀ (Z : AlgebraicSpaces site S hS) (z : Z ⟶ B'),
        IsAffineSpace site S hS Z.1 →
        ∀ (E : CompatibleEtaleDiagram site S hS D)
          (r : EtaleRealization site S hS c E),
          IsAffineSpace site S hS r.U.1 →
          ∀ (u : r.U ⟶ B'),
            r.toX ≫ c.pt.hom = u ≫ b →
            ∀ (fᵢ : E.U ⟶ (Functor.const I).obj Z),
              (∀ i, fᵢ.app i ≫ z = r.baseChange.app i ≫ u) →
              ∃! f : r.U ⟶ Z,
                (f ≫ z = u) ∧
                  (∀ i, r.baseChange.app i ≫ f = fᵢ.app i)) :
    Nonempty (IsColimit c)
```

## Tag 0GFP, a lemma

[Tag 0GFP](https://stacks.math.columbia.edu/tag/0GFP) in the Stacks Project.

**`AlgebraicGeometry.Space.isColimit_of_separated_etale_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/SeparatedColimitCriterion.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/SeparatedColimitCriterion.lean#L500). The attribute's comment: “all five hypotheses; (1) carried by the diagram landing in the separated spaces over B, (2) by IsColimit of the cocone there, (3) stated as joint surjectivity on points, (4) and (5) stated with cartesian comparison squares”.

> **Stacks 0GFP.** Let `B` be an algebraic space over `S` and let `D` be a diagram of
> algebraic spaces separated over `B`, with a colimit `c` in the category of algebraic spaces
> separated over `B`. Assume that the members of the diagram jointly cover the vertex on points,
> that every separated étale algebraic space over the vertex is the colimit of its base changes
> to the members of the diagram, and that every compatible family of separated étale algebraic
> spaces over the members of the diagram arises as the family of base changes of a separated
> étale algebraic space over the vertex. Then `c` is a colimit of the diagram in the category of
> *all* algebraic spaces over `B`.

```lean
theorem isColimit_of_separated_etale_descent
    (D : I ⥤ SeparatedOver site S hS B) (c : Cocone D) (hc : IsColimit c)
    (hcover : ∀ x : points site S hS c.pt.obj.left.obj,
      ∃ i : I, ∃ y : points site S hS (D.obj i).obj.left.obj,
        pointsMap site S hS (D.obj i).obj.left.obj (c.ι.app i).hom.left.hom y = x)
    (hbase : ∀ (E : I ⥤ SeparatedOver site S hS B) (p : E ⟶ D) (d : Cocone E)
      (q : d.pt ⟶ c.pt), IsEtaleSeparated site S hS q →
      (∀ i : I, IsPullback (p.app i).hom.left (d.ι.app i).hom.left
        (c.ι.app i).hom.left q.hom.left) → IsColimit d)
    (hdesc : ∀ (E : I ⥤ SeparatedOver site S hS B) (p : E ⟶ D),
      (∀ i : I, IsEtaleSeparated site S hS (p.app i)) →
      (∀ {i j : I} (f : i ⟶ j), IsPullback (E.map f).hom.left (p.app i).hom.left
        (p.app j).hom.left (D.map f).hom.left) →
      ∃ (d : Cocone E) (q : d.pt ⟶ c.pt), IsEtaleSeparated site S hS q ∧
        ∀ i : I, IsPullback (p.app i).hom.left (d.ι.app i).hom.left
          (c.ι.app i).hom.left q.hom.left) :
    Nonempty (IsColimit ((separatedOverInclusion site S hS B).mapCocone c))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.3, Tag 0GFN](https://stacks.math.columbia.edu/tag/0GFN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
