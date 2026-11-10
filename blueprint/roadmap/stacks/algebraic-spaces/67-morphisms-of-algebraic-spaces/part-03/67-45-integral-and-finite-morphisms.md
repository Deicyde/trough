---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIntegralHom_iff_representable, AlgebraicGeometry.Space.isFinite_iff_representable, AlgebraicGeometry.Space.IsFinite, AlgebraicGeometry.Space.IsIntegralHom, AlgebraicGeometry.Space.isIntegralHom_of_surjectiveEtaleChart, AlgebraicGeometry.Space.isFinite_of_surjectiveEtaleChart, AlgebraicGeometry.Space.isIntegralHom_iff_etaleLocal, AlgebraicGeometry.Space.isFinite_iff_etaleLocal
statement: formalized
proof: formalized
---

# 67.45 Integral and finite morphisms

Section 67.45 of the Stacks Project, [Tag 03ZN](https://stacks.math.columbia.edu/tag/03ZN). 12 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03ZO, a lemma

[Tag 03ZO](https://stacks.math.columbia.edu/tag/03ZO) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L213). The attribute's comment: “integral case: the affine test criterion for a representable morphism”.

> A morphism of algebraic spaces over `S` is integral in the sense of Stacks 03ZP exactly when it
> is relatively representable and all of its represented base changes are integral morphisms of
> schemes.

```lean
theorem isIntegralHom_iff_representable {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsIntegralHom B S hS f ↔
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsIntegralHom.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f)
```

**`AlgebraicGeometry.Space.isFinite_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L229). The attribute's comment: “finite case: the affine test criterion for a representable morphism”.

> A morphism of algebraic spaces over `S` is finite in the sense of Stacks 03ZP exactly when it
> is relatively representable and all of its represented base changes are finite morphisms of
> schemes.

```lean
theorem isFinite_iff_representable {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsFinite B S hS f ↔
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsFinite.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f)
```

## Tag 03ZP, a definition

[Tag 03ZP](https://stacks.math.columbia.edu/tag/03ZP) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean#L49). The attribute's comment: “finite\_morphism”.

> A morphism of algebraic spaces over `S` is *finite* when, for every object `U` of the big fppf
> site with affine underlying scheme and every morphism `ξ` from `yoneda.obj U` to the target, the
> base change of `f` along `ξ` is represented by an object `V` of the site with affine underlying
> scheme whose projection to `U` is a finite morphism of schemes.

```lean
abbrev IsFinite (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsIntegralHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean#L65). The attribute's comment: “integral\_morphism”.

> A morphism of algebraic spaces over `S` is *integral* when, for every object `Z` of the big
> fppf site with affine underlying scheme and every morphism `g` from `yoneda.obj Z` to the target,
> the base change of `f` along `g` is represented by an object `W` of the site with affine underlying
> scheme whose projection to `Z` is an integral morphism of schemes.

```lean
abbrev IsIntegralHom (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

## Tag 03ZQ, a lemma

[Tag 03ZQ](https://stacks.math.columbia.edu/tag/03ZQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_of_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean#L102). The attribute's comment: “integral: condition (3)”.

> **Stacks 03ZQ for integral morphisms, condition (3) implies condition (2).** A morphism of
> algebraic spaces over `S` whose base change along some surjective étale morphism from a scheme
> is integral is itself integral.

```lean
theorem isIntegralHom_of_surjectiveEtaleChart (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) {U : BigFppfOver B S hS}
    {q : yoneda.obj U ⟶ Y} (hqs : IsSurjective B S hS q) (hqe : IsEtale B S hS q)
    (hbase : IsIntegralHom B S hS (pullback.snd f q)) :
    IsIntegralHom B S hS f
```

**`AlgebraicGeometry.Space.isFinite_of_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean#L120). The attribute's comment: “finite: condition (3)”.

> **Stacks 03ZQ for finite morphisms, condition (3) implies condition (2).** A morphism of
> algebraic spaces over `S` whose base change along some surjective étale morphism from a scheme
> is finite is itself finite.

```lean
theorem isFinite_of_surjectiveEtaleChart (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) {U : BigFppfOver B S hS}
    {q : yoneda.obj U ⟶ Y} (hqs : IsSurjective B S hS q) (hqe : IsEtale B S hS q)
    (hbase : IsFinite B S hS (pullback.snd f q)) :
    IsFinite B S hS f
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_etaleLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean#L174). The attribute's comment: “integral: conditions (2) and (3)”.

> **Stacks 03ZQ for integral morphisms, conditions (2) and (3).** A morphism of algebraic
> spaces over `S` is integral in the sense of Stacks 03ZP exactly when there is one surjective
> étale morphism from a representable presheaf onto its target along which its base change is
> integral.

```lean
theorem isIntegralHom_iff_etaleLocal (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsIntegralHom B S hS f ↔
      ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y),
        (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsIntegralHom B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isFinite_iff_etaleLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteEtaleLocal.lean#L196). The attribute's comment: “finite: conditions (2) and (3)”.

> **Stacks 03ZQ for finite morphisms, conditions (2) and (3).** A morphism of algebraic
> spaces over `S` is finite in the sense of Stacks 03ZP exactly when there is one surjective
> étale morphism from a representable presheaf onto its target along which its base change is
> finite.

```lean
theorem isFinite_iff_etaleLocal (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsFinite B S hS f ↔
      ∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ Y),
        (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsFinite B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L213). The attribute's comment: “integral: conditions (1) and (2)”.

> A morphism of algebraic spaces over `S` is integral in the sense of Stacks 03ZP exactly when it
> is relatively representable and all of its represented base changes are integral morphisms of
> schemes.

```lean
theorem isIntegralHom_iff_representable {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsIntegralHom B S hS f ↔
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsIntegralHom.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f)
```

**`AlgebraicGeometry.Space.isFinite_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L229). The attribute's comment: “finite: conditions (1) and (2)”.

> A morphism of algebraic spaces over `S` is finite in the sense of Stacks 03ZP exactly when it
> is relatively representable and all of its represented base changes are finite morphisms of
> schemes.

```lean
theorem isFinite_iff_representable {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsFinite B S hS f ↔
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsFinite.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f)
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_zariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L243). The attribute's comment: “integral: conditions (2) and (4)”.

> A morphism of algebraic spaces over `S` is integral in the sense of Stacks 03ZP exactly when
> there is a Zariski covering of its target over whose members its base changes are integral.

```lean
theorem isIntegralHom_iff_zariskiCover {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsIntegralHom B S hS f ↔
      ∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
          ∀ i, IsIntegralHom B S hS (Limits.pullback.snd f (U i).ι)
```

**`AlgebraicGeometry.Space.isFinite_iff_zariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralFiniteTfae.lean#L256). The attribute's comment: “finite: conditions (2) and (4)”.

> A morphism of algebraic spaces over `S` is finite in the sense of Stacks 03ZP exactly when
> there is a Zariski covering of its target over whose members its base changes are finite.

```lean
theorem isFinite_iff_zariskiCover {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsFinite B S hS f ↔
      ∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
          ∀ i, IsFinite B S hS (Limits.pullback.snd f (U i).ι)
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L512). The attribute's comment: “integral: conditions (2) and (3)”.

> A morphism of algebraic spaces over `S` is integral exactly when its base change along some
> surjective étale morphism from a representable presheaf onto its target is integral.

```lean
theorem isIntegralHom_iff_etaleChart {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsIntegralHom B S hS f ↔
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
          IsIntegralHom B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isFinite_iff_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L534). The attribute's comment: “finite: conditions (2) and (3)”.

> A morphism of algebraic spaces over `S` is finite exactly when its base change along some
> surjective étale morphism from a representable presheaf onto its target is finite.

```lean
theorem isFinite_iff_etaleChart {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    IsFinite B S hS f ↔
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
          IsFinite B S hS (pullback.snd f g)
```

## Tag 03ZR, a lemma

[Tag 03ZR](https://stacks.math.columbia.edu/tag/03ZR) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean#L130). The attribute's comment: “integral”. References: EGA II (6.1.5), “(ii) integral”.

> The composite of two integral morphisms of algebraic spaces over `S` is integral.

```lean
theorem isIntegralHom_comp {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsIntegralHom B S hS f) (hg : IsIntegralHom B S hS g) :
    IsIntegralHom B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Finite.lean#L142). The attribute's comment: “finite”. References: EGA II (6.1.5), “(ii) finite”.

> The composite of two finite morphisms of algebraic spaces over `S` is finite.

```lean
theorem isFinite_comp {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsFinite B S hS f) (hg : IsFinite B S hS g) :
    IsFinite B S hS (f ≫ g)
```

## Tag 03ZS, a lemma

[Tag 03ZS](https://stacks.math.columbia.edu/tag/03ZS) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L86). The attribute's comment: “integral”.

> A base change of an integral morphism of algebraic spaces over `S` is integral: if `f'` sits
> in a Cartesian square over `f`, then `f'` is integral as soon as `f` is.

```lean
theorem isIntegralHom_of_isPullback {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    {g : Y' ⟶ Y} {k : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback k f' f g)
    (hf : IsIntegralHom B S hS f) : IsIntegralHom B S hS f'
```

**`AlgebraicGeometry.Space.isFinite_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L93). The attribute's comment: “finite”.

> A base change of a finite morphism of algebraic spaces over `S` is finite.

```lean
theorem isFinite_of_isPullback {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    {g : Y' ⟶ Y} {k : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback k f' f g)
    (hf : IsFinite B S hS f) : IsFinite B S hS f'
```

## Tag 0414, a lemma

[Tag 0414](https://stacks.math.columbia.edu/tag/0414) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFinite.isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean#L94). The attribute's comment: “first assertion: a finite morphism is integral”.

> A finite morphism of algebraic spaces is integral.

```lean
theorem IsFinite.isIntegralHom {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsFinite B S hS f) : IsIntegralHom B S hS f
```

**`AlgebraicGeometry.Space.isFinite_of_isIntegralHom_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean#L102). The attribute's comment: “second assertion: an integral morphism locally of finite type is finite”.

> An integral morphism of algebraic spaces which is locally of finite type is finite.

```lean
theorem isFinite_of_isIntegralHom_of_isLocallyOfFiniteType
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsIntegralHom B S hS f) (hft : IsLocallyOfFiniteType B S hS f) :
    IsFinite B S hS f
```

## Tag 0415, a lemma

[Tag 0415](https://stacks.math.columbia.edu/tag/0415) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_iff_isAffineHom_and_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyClosed.lean#L153). References: EGA IV (18.12.8), “more general”; EGA II (6.1.10).

> A morphism of algebraic spaces over `S` is integral if and only if it is affine and
> universally closed.

```lean
theorem isIntegralHom_iff_isAffineHom_and_universallyClosed
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsIntegralHom B S hS f ↔
      IsAffineHom B S hS f ∧ UniversallyClosed B S hS f
```

## Tag 04NY, a lemma

[Tag 04NY](https://stacks.math.columbia.edu/tag/04NY) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiFinite_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L139).

> A finite morphism of algebraic spaces over `S` is quasi-finite.

```lean
theorem isQuasiFinite_of_isFinite (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsFinite B S hS f) :
    IsQuasiFinite B S hS f
```

## Tag 04NZ, a lemma

[Tag 04NZ](https://stacks.math.columbia.edu/tag/04NZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_iff_isAffineHom_and_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteAffineProper.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteAffineProper.lean#L130). References: EGA III (4.4.2), “a) <=> b)”.

> A morphism of algebraic spaces over `S` is finite exactly when it is affine and proper.

```lean
theorem isFinite_iff_isAffineHom_and_isProper {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsFinite B S hS f ↔ IsAffineHom B S hS f ∧ IsProper B S hS f
```

## Tag 081Y, a lemma

[Tag 081Y](https://stacks.math.columbia.edu/tag/081Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L103). The attribute's comment: “finite”. References: EGA II (6.1.5), “(i) finite”.

> A closed immersion of algebraic spaces is finite.

```lean
theorem isFinite_of_isClosedImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f) :
    IsFinite B S hS f
```

**`AlgebraicGeometry.Space.isIntegralHom_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L114). The attribute's comment: “integral”. References: EGA II (6.1.5), “(i) integral”.

> A closed immersion of algebraic spaces is integral.

```lean
theorem isIntegralHom_of_isClosedImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f) :
    IsIntegralHom B S hS f
```

## Tag 0CZ2, a lemma

[Tag 0CZ2](https://stacks.math.columbia.edu/tag/0CZ2) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L173).

> Let `F i ⟶ Y`, for `i` in a finite index type, be finite morphisms of algebraic spaces over
> `S`, and let `G` be their coproduct as a sheaf of sets on the big fppf site of `S`, given by a
> colimit cofan. Then the induced morphism `G ⟶ Y` is finite.

```lean
theorem isFinite_coproduct {I : Type v} [Finite I]
    (F : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : ∀ i, IsAlgebraicSpace B S hS (F i)) (hY : IsAlgebraicSpace B S hS Y)
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨F i, (hF i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hG : IsColimit (Cofan.mk G ι))
    (fᵢ : ∀ i, F i ⟶ Y) (f : G.obj ⟶ Y) (hf : ∀ i, (ι i).hom ≫ f = fᵢ i)
    (hfin : ∀ i, IsFinite B S hS (fᵢ i)) :
    IsFinite B S hS f
```

## Tag 081Z, a lemma

[Tag 081Z](https://stacks.math.columbia.edu/tag/081Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralHom_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L116). The attribute's comment: “part (2): integral”. References: EGA II (6.1.5), “(v) integral”.

> If a composite of morphisms of algebraic spaces over `S` is integral and its second leg is
> separated, then its first leg is integral.

```lean
theorem isIntegralHom_of_comp_of_isSeparated (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsIntegralHom B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    IsIntegralHom B S hS f
```

**`AlgebraicGeometry.Space.isFinite_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IntegralFinite.lean#L127). The attribute's comment: “part (1): finite”. References: EGA II (6.1.5), “(v) finite”.

> If a composite of morphisms of algebraic spaces over `S` is finite and its second leg is
> separated, then its first leg is finite.

```lean
theorem isFinite_of_comp_of_isSeparated (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsFinite B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    IsFinite B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.45, Tag 03ZN](https://stacks.math.columbia.edu/tag/03ZN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
