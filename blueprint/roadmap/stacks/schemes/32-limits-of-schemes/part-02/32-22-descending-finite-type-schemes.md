---
declaration: section
origin: cited
lean: AlgebraicGeometry.LimitNoetherianSituation, AlgebraicGeometry.LimitNoetherianSituation.nonempty_goodDiagram, AlgebraicGeometry.LimitNoetherianSituation.GoodDiagram.isLimit_imageCone, AlgebraicGeometry.LimitNoetherianSituation.exists_morphismAt_of_dominant, AlgebraicGeometry.LimitNoetherianSituation.exists_morphismAt, AlgebraicGeometry.LimitNoetherianSituation.eventually_eq_morphismAt, AlgebraicGeometry.LimitNoetherianSituation.MorphismAt.eventually_eq_morphismAt_of_dominant, AlgebraicGeometry.LimitNoetherianSituation.exists_eventual_iso_imageSystem
statement: formalized
proof: formalized
---

# 32.22 Descending finite type schemes

Section 32.22 of the Stacks Project, [Tag 0CNL](https://stacks.math.columbia.edu/tag/0CNL). 9 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CNM, a situation

[Tag 0CNM](https://stacks.math.columbia.edu/tag/0CNM) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/NoetherianSystem.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/NoetherianSystem.lean#L45).

> **Stacks Project, Tag 0CNM.** A directed inverse system of Noetherian schemes with affine
> transition morphisms, equipped with a chosen limiting cone.

```lean
structure LimitNoetherianSituation (I : Type v) [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)]
```

## Tag 0CNN, a lemma

[Tag 0CNN](https://stacks.math.columbia.edu/tag/0CNN) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.nonempty_goodDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/GoodDiagramExistence.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/GoodDiagramExistence.lean#L99).

> **Stacks Project, Tag 0CNN.** In the limit situation `S = lim S_i` of a directed inverse
> system of Noetherian schemes with affine transition morphisms, a quasi-separated morphism
> `X ⟶ S` of finite type fits into a diagram over some stage `S_i` with a model `W` of finite type
> over `S_i` whose base change receives `X` as a closed subscheme.

```lean
theorem nonempty_goodDiagram {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : LimitNoetherianSituation.{u, u} I) {X : Scheme.{u}} (f : X ⟶ D.limitScheme)
    [QuasiSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    Nonempty (GoodDiagram D f)
```

## Tag 0CNQ, a lemma

[Tag 0CNQ](https://stacks.math.columbia.edu/tag/0CNQ) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.GoodDiagram.isLimit_imageCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ImageSystemLimit.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ImageSystemLimit.lean#L184).

> **Stacks Project, Tag 0CNQ.** The scheme-theoretic images of a good diagram at
> all later stages form an inverse system with canonical limit `X`.

```lean
noncomputable def isLimit_imageCone {I : Type v} [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)] (D : LimitNoetherianSituation.{v, u} I)
    {X : Scheme.{u}} (f : X ⟶ D.limitScheme) [QuasiSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] (G : GoodDiagram D f) :
    IsLimit (imageCone G)
```

## Tag 0CNR, a lemma

[Tag 0CNR](https://stacks.math.columbia.edu/tag/0CNR) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.exists_morphismAt_of_dominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Existence/Basic.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Existence/Basic.lean#L302). The attribute's comment: “existence”.

> **Stacks Project, Tag 0CNR, existence.** A morphism of schemes over the limit is realized by
> a morphism of the systems of scheme-theoretic images on a sufficiently late common tail.
>
> No hypothesis beyond the source's: in particular no smallness of the index type, and none of the
> quasi-separatedness, finite-type or quasi-compactness hypotheses the source carries, all three
> of which are consequences of the good diagrams.

```lean
public theorem exists_morphismAt_of_dominant (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY) :
    ∃ (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀),
      Nonempty (MorphismAt D f GX GY i₀ hX hY)
```

**`AlgebraicGeometry.LimitNoetherianSituation.exists_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeSystemMorphism.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeSystemMorphism.lean#L63). The attribute's comment: “existence”.

> **Stacks Project, Tag 0CNR, existence.** A morphism of schemes over the limit is
> realized by a morphism of the systems of images on a sufficiently late common tail.

```lean
theorem exists_morphismAt (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY]
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY) :
    ∃ (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀),
      Nonempty (MorphismAt D f GX GY i₀ hX hY)
```

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_eq_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeSystemMorphism.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeSystemMorphism.lean#L76). The attribute's comment: “eventual uniqueness”.

> **Stacks Project, Tag 0CNR, eventual uniqueness.** Two system morphisms inducing the same
> limit morphism agree at every sufficiently late stage.

```lean
theorem eventually_eq_morphismAt (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F G : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_hi : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)) (_hj : i₃ ≤ unop j.left),
        F.maps.app j = G.maps.app j
```

**`AlgebraicGeometry.LimitNoetherianSituation.MorphismAt.eventually_eq_morphismAt_of_dominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitSmallDominantIndex/Uniqueness.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitSmallDominantIndex/Uniqueness.lean#L235). The attribute's comment: “eventual uniqueness”.

> Two morphisms of the image systems inducing the same morphism on the limits agree at every
> sufficiently late stage.

```lean
public theorem eventually_eq_morphismAt_of_dominant (F G : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)), i₃ ≤ unop j.left → F.maps.app j = G.maps.app j
```

## Tag 0CNS, a remark

[Tag 0CNS](https://stacks.math.columbia.edu/tag/0CNS) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.exists_eventual_iso_imageSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ImageSystemComparison.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ImageSystemComparison.lean#L199). The attribute's comment: “eventual isomorphism”.

> **Stacks Project, Tag 0CNS.** The systems associated to two good diagrams for the same
> scheme over the limit become isomorphic on a common tail, by an isomorphism of systems inducing
> the identity of `X` and lying over the base system.

```lean
theorem exists_eventual_iso_imageSystem [FinallySmall.{u} I]
    (D : LimitNoetherianSituation.{v, u} I)
    {X : Scheme.{u}} (p : X ⟶ D.limitScheme)
    [QuasiSeparated p] [LocallyOfFiniteType p] [QuasiCompact p]
    (G₁ G₂ : GoodDiagram D p) :
    ∃ (i₀ : I) (h₁ : G₁.index ≤ i₀) (h₂ : G₂.index ≤ i₀)
      (F : MorphismAt D (𝟙 X) G₁ G₂ i₀ h₁ h₂)
      (G : MorphismAt D (𝟙 X) G₂ G₁ i₀ h₂ h₁),
      ∀ j : Over (op i₀),
        (F.maps.app j ≫ G.maps.app j = 𝟙 _) ∧
        (G.maps.app j ≫ F.maps.app j = 𝟙 _)
```

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_natural_imageSystem_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ImageSystemComparison.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ImageSystemComparison.lean#L257). The attribute's comment: “naturality”.

> **Stacks Project, Tag 0CNS, naturality.** The comparison between the systems of two choices
> of good diagrams commutes, eventually, with any morphism of schemes over the limit.

```lean
theorem eventually_natural_imageSystem_comparison [FinallySmall.{u} I]
    (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme}
    {pY : Y ⟶ D.limitScheme} (f : X ⟶ Y)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    (GX₁ GX₂ : GoodDiagram D pX) (GY₁ GY₂ : GoodDiagram D pY)
    (i₀ : I) (hX₁ : GX₁.index ≤ i₀) (hX₂ : GX₂.index ≤ i₀)
    (hY₁ : GY₁.index ≤ i₀) (hY₂ : GY₂.index ≤ i₀)
    (FX : MorphismAt D (𝟙 X) GX₁ GX₂ i₀ hX₁ hX₂)
    (FY : MorphismAt D (𝟙 Y) GY₁ GY₂ i₀ hY₁ hY₂)
    (H₁ : MorphismAt D f GX₁ GY₁ i₀ hX₁ hY₁)
    (H₂ : MorphismAt D f GX₂ GY₂ i₀ hX₂ hY₂) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)) (_ : i₃ ≤ unop j.left),
        H₁.maps.app j ≫ FY.maps.app j =
          FX.maps.app j ≫ H₂.maps.app j
```

## Tag 0CNT, a lemma

[Tag 0CNT](https://stacks.math.columbia.edu/tag/0CNT) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_flat_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean#L56). The attribute's comment: “eventual flatness”.

> **Stacks Project, Tag 0CNT, eventual flatness.**
>
> The morphisms of the image systems of a flat morphism of finite presentation are flat at every
> sufficiently late stage.

```lean
public theorem eventually_flat_morphismAt
    (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY]
    [Flat f] (hfp : FinitePresentation f)
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)), i₃ ≤ unop j.left → Flat (F.maps.app j)
```

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_isPullback_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean#L76). The attribute's comment: “cartesian transition squares”.

> **Stacks Project, Tag 0CNT, cartesian transition squares.**
>
> On a sufficiently late tail every transition square of the morphism of image systems of a flat
> morphism of finite presentation is cartesian.

```lean
public theorem eventually_isPullback_morphismAt
    (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY]
    [Flat f] (hfp : FinitePresentation f)
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ {j k : Over (op i₀)} (a : j ⟶ k),
        i₃ ≤ unop j.left → i₃ ≤ unop k.left →
          IsPullback (F.maps.app j)
            ((Over.map ((homOfLE hX).op) ⋙ GoodDiagram.imageSystem GX).map a)
            ((Over.map ((homOfLE hY).op) ⋙ GoodDiagram.imageSystem GY).map a)
            (F.maps.app k)
```

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_isPullback_limit_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FlatImageSystemModels.lean#L101). The attribute's comment: “cartesian limit square”.

> **Stacks Project, Tag 0CNT, cartesian limit square.**
>
> The square relating a flat morphism of finite presentation to each sufficiently late morphism of
> the image systems is cartesian.

```lean
public theorem eventually_isPullback_limit_morphismAt
    (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY]
    [Flat f] (hfp : FinitePresentation f)
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)), i₃ ≤ unop j.left →
        IsPullback f
          ((GoodDiagram.imageCone GX).π.app ((Over.map ((homOfLE hX).op)).obj j))
          ((GoodDiagram.imageCone GY).π.app ((Over.map ((homOfLE hY).op)).obj j))
          (F.maps.app j)
```

## Tag 0CNU, a lemma

[Tag 0CNU](https://stacks.math.columbia.edu/tag/0CNU) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_smooth_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/SmoothImageSystem.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/SmoothImageSystem.lean#L267).

> The morphisms on the image systems of a smooth map become smooth at every
> sufficiently late stage.
>
> `Nonempty I` is not a weakening. The conclusion names a specific cofinal stage `i₃ ≥ i₀`,
> which is exactly how Stacks 0CNU states it ("there exists an `i₃ ≥ i₀` such that for `i ≥ i₃`"),
> and that phrasing presupposes the index `i₀`. The hypothesis is the source's own.

```lean
theorem eventually_smooth_morphismAt {I : Type v} [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)] [Small.{u} I] [FinallySmall.{u} I]
    (D : LimitNoetherianSituation.{v, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY]
    [Smooth f]
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)), i₃ ≤ unop j.left → Smooth (F.maps.app j)
```

## Tag 0CNV, a lemma

[Tag 0CNV](https://stacks.math.columbia.edu/tag/0CNV) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_isProper_morphismAt'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperLimitOfFiniteTypeOverZ.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ProperLimitOfFiniteTypeOverZ.lean#L196).

> **[Stacks, Tag 0CNV].** In Situation [Stacks, Tag 0CNM], the components of a morphism of the
> image systems of two good diagrams which induces a proper morphism on the limits are proper from
> some stage onwards.
>
> The limit of the system is quasi-compact and quasi-separated because its stages are Noetherian
> and its transition morphisms affine, so no hypothesis on its underlying space is needed.

```lean
theorem eventually_isProper_morphismAt' {I : Type u} [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)] (D : LimitNoetherianSituation.{u, u} I)
    {X Y : Scheme.{u}} {pX : X ⟶ D.limitScheme} {pY : Y ⟶ D.limitScheme}
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    [QuasiSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    [QuasiSeparated pY] [LocallyOfFiniteType pY] [QuasiCompact pY] [IsProper f]
    (GX : GoodDiagram D pX) (GY : GoodDiagram D pY)
    (i₀ : I) (hX : GX.index ≤ i₀) (hY : GY.index ≤ i₀)
    (F : MorphismAt D f GX GY i₀ hX hY) :
    ∃ (i₃ : I) (_ : i₀ ≤ i₃),
      ∀ (j : Over (op i₀)), i₃ ≤ unop j.left → IsProper (F.maps.app j)
```

## Tag 0CNW, a lemma

[Tag 0CNW](https://stacks.math.columbia.edu/tag/0CNW) in the Stacks Project.

**`AlgebraicGeometry.LimitNoetherianSituation.eventually_comp_eq_comp_morphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitMorphismAt/CartesianSquare.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitMorphismAt/CartesianSquare.lean#L111). The attribute's comment: “eventual commutation of the two composites of systems”.

> **Stacks Project, Tag 0CNW, the eventual commutation.** Given a commuting square of schemes
> quasi-separated and of finite type over the limit `S`, good diagrams for its four corners and
> morphisms `p_i`, `q_i`, `a_i`, `b_i` of the resulting image systems realizing the four morphisms
> of the square on a common tail, the two composites `a_i ∘ p_i` and `b_i ∘ q_i` agree at every
> sufficiently late stage.

```lean
theorem eventually_comp_eq_comp_morphismAt (D : LimitNoetherianSituation.{v, u} I)
    {X₁ X₂ X₃ X₄ : Scheme.{u}} {s₁ : X₁ ⟶ D.limitScheme} {s₂ : X₂ ⟶ D.limitScheme}
    {s₃ : X₃ ⟶ D.limitScheme} {s₄ : X₄ ⟶ D.limitScheme}
    {p : X₁ ⟶ X₃} {q : X₁ ⟶ X₂} {a : X₃ ⟶ X₄} {b : X₂ ⟶ X₄} (hsq : p ≫ a = q ≫ b)
    {G₁ : GoodDiagram D s₁} {G₂ : GoodDiagram D s₂} {G₃ : GoodDiagram D s₃}
    {G₄ : GoodDiagram D s₄} {i₀ : I} {h₁ : G₁.index ≤ i₀} {h₂ : G₂.index ≤ i₀}
    {h₃ : G₃.index ≤ i₀} {h₄ : G₄.index ≤ i₀}
    (P : MorphismAt D p G₁ G₃ i₀ h₁ h₃) (Q : MorphismAt D q G₁ G₂ i₀ h₁ h₂)
    (A : MorphismAt D a G₃ G₄ i₀ h₃ h₄) (B : MorphismAt D b G₂ G₄ i₀ h₂ h₄) :
    ∃ (i₉ : I) (_ : i₀ ≤ i₉), ∀ j : Over (op i₀), i₉ ≤ unop j.left →
      P.maps.app j ≫ A.maps.app j = Q.maps.app j ≫ B.maps.app j
```

**`AlgebraicGeometry.LimitNoetherianSituation.isClosedImmersion_fibreProductComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductClosedImmersion.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductClosedImmersion.lean#L216). The attribute's comment: “closed immersion of the comparison, for the model `W² ×_{W⁴} W³` of the first corner”.

> For the model `W² ×_{W⁴} W³` of the first corner of a cartesian square, the comparison
> `(q_j, p_j) : X¹_j ⟶ X²_j ×_{X⁴_j} X³_j` is a closed immersion at every stage.

```lean
theorem isClosedImmersion_fibreProductComparison (j : Over (op i₀)) :
    IsClosedImmersion (MorphismAt.fibreComparisonApp
      (fibreProductProjTrd G₄ M₂ M₃ hsq hq hb ha i₀ h)
      (fibreProductProjSnd G₄ M₂ M₃ hsq hq hb ha i₀ h)
      (fibreProductBaseTrd G₄ M₃ ha i₀ h) (fibreProductBaseSnd G₄ M₂ hb i₀ h) j
      (fibreProduct_comp_eq_comp G₄ M₂ M₃ hsq hq hb ha i₀ h j))
```

**`AlgebraicGeometry.LimitNoetherianSituation.exists_eventually_isClosedImmersion_fibreComparison_of_goodDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductComparison.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductComparison.lean#L363). The attribute's comment: “closed immersion of the comparison, for four independently chosen good diagrams”.

> **Stacks Project, Tag 0CNW, the closed immersion, for four independently chosen good
> diagrams.** Given a cartesian square of schemes over `S`, a good diagram for each of its four
> corners chosen separately, and morphisms `p_i`, `q_i`, `a_i`, `b_i` of the resulting image
> systems realizing the four morphisms of the square over a common index `i₀`, the comparison
> `(q_i, p_i) : X¹_i ⟶ X²_i ×_{X⁴_i} X³_i` is a closed immersion at every sufficiently late stage.
>
> The compatible models the restricted statement needs are *produced* from the data: replacing
> `G₂`, `G₃` and `G₄` by the good diagrams whose models are their own scheme-theoretic images at
> the stage `i₀`, the components of `B` and of `A` at that stage are morphisms of models over one
> stage, by `AlgebraicGeometry.LimitNoetherianSituation.MorphismAt.stageModelOver`.

```lean
theorem exists_eventually_isClosedImmersion_fibreComparison_of_goodDiagram
    (D : LimitNoetherianSituation.{v, u} I)
    {X₁ X₂ X₃ X₄ : Scheme.{u}} {s₁ : X₁ ⟶ D.limitScheme} {s₂ : X₂ ⟶ D.limitScheme}
    {s₃ : X₃ ⟶ D.limitScheme} {s₄ : X₄ ⟶ D.limitScheme}
    [QuasiSeparated s₂] [LocallyOfFiniteType s₂] [QuasiCompact s₂]
    [QuasiSeparated s₃] [LocallyOfFiniteType s₃] [QuasiCompact s₃]
    [QuasiSeparated s₄] [LocallyOfFiniteType s₄] [QuasiCompact s₄]
    {p : X₁ ⟶ X₃} {q : X₁ ⟶ X₂} {a : X₃ ⟶ X₄} {b : X₂ ⟶ X₄}
    (hsq : IsPullback q p b a) (hq : q ≫ s₂ = s₁) (hb : b ≫ s₄ = s₂) (ha : a ≫ s₄ = s₃)
    (G₁ : GoodDiagram D s₁) (G₂ : GoodDiagram D s₂) (G₃ : GoodDiagram D s₃)
    (G₄ : GoodDiagram D s₄) (i₀ : I) (h₁ : G₁.index ≤ i₀) (h₂ : G₂.index ≤ i₀)
    (h₃ : G₃.index ≤ i₀) (h₄ : G₄.index ≤ i₀)
    (P : MorphismAt D p G₁ G₃ i₀ h₁ h₃) (Q : MorphismAt D q G₁ G₂ i₀ h₁ h₂)
    (A : MorphismAt D a G₃ G₄ i₀ h₃ h₄) (B : MorphismAt D b G₂ G₄ i₀ h₂ h₄) :
    ∃ (i₇ : I) (_ : i₀ ≤ i₇), ∀ (j : Over (op i₀)) (_ : i₇ ≤ unop j.left)
      (hj : P.maps.app j ≫ A.maps.app j = Q.maps.app j ≫ B.maps.app j),
      IsClosedImmersion (MorphismAt.fibreComparisonApp P Q A B j hj)
```

**`AlgebraicGeometry.LimitNoetherianSituation.exists_eventually_isClosedImmersion_and_isIso_fibreComparison_of_fourIndices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductComparison.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitMorphismAt/FibreProductComparison.lean#L509).

> **Stacks Project, Tag 0CNW.** In the limit situation `S = lim S_i` of a directed inverse
> system of Noetherian schemes with affine transition morphisms, let
>
> ```
> X¹ ⟶ X³
> ↓     ↓
> X² ⟶ X⁴
> ```
>
> be a cartesian square of schemes quasi-separated and of finite type over `S`. For each corner
> choose, independently of the others, a good diagram, take the resulting limit descriptions
> `X^n = lim X^n_i` of their systems of scheme-theoretic images, and morphisms of those systems
> `(a_i)_{i ≥ i₅}`, `(b_i)_{i ≥ i₆}`, `(p_i)_{i ≥ i₇}` and `(q_i)_{i ≥ i₈}` realizing the four
> morphisms of the square, each starting at its own index. Then there exists
> `i₉ ≥ max(i₅, i₆, i₇, i₈)` such that at every stage `i ≥ i₉` the square of systems commutes,
> `a_i ∘ p_i = b_i ∘ q_i`, and the induced morphism
>
> ```
> (q_i, p_i) : X¹_i ⟶ X²_i ×_{b_i, X⁴_i, a_i} X³_i
> ```
>
> is a closed immersion; and if moreover `a` and `b` are flat and of finite presentation, there
> exists `i₁₀ ≥ i₉` such that at every stage above `i₁₀` that same morphism is an isomorphism.
>
> The four morphisms of systems are read on the stages above `i₉` by restriction,
> `AlgebraicGeometry.LimitNoetherianSituation.MorphismAt.restrict'`.

```lean
theorem exists_eventually_isClosedImmersion_and_isIso_fibreComparison_of_fourIndices
    (D : LimitNoetherianSituation.{v, u} I)
    {X₁ X₂ X₃ X₄ : Scheme.{u}} {s₁ : X₁ ⟶ D.limitScheme} {s₂ : X₂ ⟶ D.limitScheme}
    {s₃ : X₃ ⟶ D.limitScheme} {s₄ : X₄ ⟶ D.limitScheme}
    [QuasiSeparated s₂] [LocallyOfFiniteType s₂] [QuasiCompact s₂]
    [QuasiSeparated s₃] [LocallyOfFiniteType s₃] [QuasiCompact s₃]
    [QuasiSeparated s₄] [LocallyOfFiniteType s₄] [QuasiCompact s₄]
    {p : X₁ ⟶ X₃} {q : X₁ ⟶ X₂} {a : X₃ ⟶ X₄} {b : X₂ ⟶ X₄}
    (hsq : IsPullback q p b a) (hq : q ≫ s₂ = s₁) (hb : b ≫ s₄ = s₂) (ha : a ≫ s₄ = s₃)
    (G₁ : GoodDiagram D s₁) (G₂ : GoodDiagram D s₂) (G₃ : GoodDiagram D s₃)
    (G₄ : GoodDiagram D s₄) (i₅ i₆ i₇ i₈ : I)
    (h₃₅ : G₃.index ≤ i₅) (h₄₅ : G₄.index ≤ i₅) (h₂₆ : G₂.index ≤ i₆) (h₄₆ : G₄.index ≤ i₆)
    (h₁₇ : G₁.index ≤ i₇) (h₃₇ : G₃.index ≤ i₇) (h₁₈ : G₁.index ≤ i₈) (h₂₈ : G₂.index ≤ i₈)
    (A : MorphismAt D a G₃ G₄ i₅ h₃₅ h₄₅) (B : MorphismAt D b G₂ G₄ i₆ h₂₆ h₄₆)
    (P : MorphismAt D p G₁ G₃ i₇ h₁₇ h₃₇) (Q : MorphismAt D q G₁ G₂ i₈ h₁₈ h₂₈) :
    ∃ (i₉ : I) (k₅ : i₅ ≤ i₉) (k₆ : i₆ ≤ i₉) (k₇ : i₇ ≤ i₉) (k₈ : i₈ ≤ i₉)
      (hcomm : ∀ j : Over (op i₉),
        (P.restrict' k₇).maps.app j ≫ (A.restrict' k₅).maps.app j =
          (Q.restrict' k₈).maps.app j ≫ (B.restrict' k₆).maps.app j),
      (∀ j : Over (op i₉), IsClosedImmersion (MorphismAt.fibreComparisonApp
          (P.restrict' k₇) (Q.restrict' k₈) (A.restrict' k₅) (B.restrict' k₆) j (hcomm j))) ∧
        (Flat a → Flat b → FinitePresentation a → FinitePresentation b →
          ∃ (i₁₀ : I) (_ : i₉ ≤ i₁₀), ∀ j : Over (op i₉), i₁₀ ≤ unop j.left →
            IsIso (MorphismAt.fibreComparisonApp
              (P.restrict' k₇) (Q.restrict' k₈) (A.restrict' k₅) (B.restrict' k₆) j
              (hcomm j)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.22, Tag 0CNL](https://stacks.math.columbia.edu/tag/0CNL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
