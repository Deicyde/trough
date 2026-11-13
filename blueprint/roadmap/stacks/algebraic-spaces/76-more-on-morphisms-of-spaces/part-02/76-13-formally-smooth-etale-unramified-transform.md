---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FormallySmooth, AlgebraicGeometry.Space.FormallyEtale, AlgebraicGeometry.Space.FormallyUnramified, AlgebraicGeometry.Space.formallyEtale_iff_formallySmooth_and_formallyUnramified, AlgebraicGeometry.Space.FormallySmooth.comp, AlgebraicGeometry.Space.formallyEtale_comp, AlgebraicGeometry.Space.formallyUnramified_comp, AlgebraicGeometry.Space.FormallySmooth.baseChange
statement: formalized
proof: formalized
---

# 76.13 Formally smooth, étale, unramified transformations

Section 76.13 of the Stacks Project, [Tag 04G3](https://stacks.math.columbia.edu/tag/04G3). 7 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 049S, a definition

[Tag 049S](https://stacks.math.columbia.edu/tag/049S) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallySmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L68). The attribute's comment: “part (1)”. References: SGA 3 XI (1.6), “formally smooth”.

> **Stacks 049S, part (1).** Every commutative affine square against a
> square-zero closed immersion admits a lift.

```lean
public abbrev FormallySmooth {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.FormallyEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L79). The attribute's comment: “part (2)”. References: SGA 3 XI (1.6), “formally étale”.

> **Stacks 049S, part (2).** Every commutative affine square against a
> square-zero closed immersion admits exactly one lift.

```lean
public abbrev FormallyEtale {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.FormallyUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L90). The attribute's comment: “part (3)”. References: SGA 3 XI (1.6), “formally unramified”.

> **Stacks 049S, part (3).** Every commutative affine square against a
> square-zero closed immersion admits at most one lift.

```lean
public abbrev FormallyUnramified {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) :
    Prop
```

## Tag 04G4, a lemma

[Tag 04G4](https://stacks.math.columbia.edu/tag/04G4) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_iff_formallySmooth_and_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleIffSmoothUnramified.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleIffSmoothUnramified.lean#L49). References: EGA IV (17.1.1), “étale ⟺ smooth+unram”.

> **Stacks 04G4.** A transformation of set-valued functors on the big fppf site is
> formally étale if and only if it is both formally smooth and formally unramified.

```lean
public theorem formallyEtale_iff_formallySmooth_and_formallyUnramified (a : F ⟶ G) :
    FormallyEtale a ↔ (FormallySmooth a ∧ FormallyUnramified a)
```

## Tag 049T, a lemma

[Tag 049T](https://stacks.math.columbia.edu/tag/049T) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallySmooth.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L48). The attribute's comment: “formally\_smooth\_comp”. References: EGA IV (17.1.3), “(ii) smooth”; EGA IV (17.1.5), “sufficiency, smooth”.

> **Stacks 049T, formal smoothness under composition.**

```lean
public theorem FormallySmooth.comp (a : F ⟶ G) (b : G ⟶ H)
    (ha : FormallySmooth a) (hb : FormallySmooth b) :
    FormallySmooth (a ≫ b)
```

**`AlgebraicGeometry.Space.formallyEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L60). The attribute's comment: “formally\_etale\_comp”. References: EGA IV (17.1.3), “(ii) étale”; EGA IV (17.1.5), “sufficiency, étale”.

> The composite of two formally étale transformations is formally étale.

```lean
public theorem formallyEtale_comp {a : F ⟶ G} {b : G ⟶ H}
    (ha : FormallyEtale a) (hb : FormallyEtale b) :
    FormallyEtale (a ≫ b)
```

**`AlgebraicGeometry.Space.formallyUnramified_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L74). The attribute's comment: “formally\_unramified\_comp”. References: EGA IV (17.1.3), “(ii) unramified”; EGA IV (17.1.5), “sufficiency, unramified”.

> **Stacks 049T, composition part.** A composite of formally unramified
> transformations is formally unramified.

```lean
public theorem formallyUnramified_comp (a : F ⟶ G) (b : G ⟶ H)
    (ha : FormallyUnramified a) (hb : FormallyUnramified b) :
    FormallyUnramified (a ≫ b)
```

## Tag 049U, a lemma

[Tag 049U](https://stacks.math.columbia.edu/tag/049U) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallySmooth.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean#L227). The attribute's comment: “formally\_smooth\_base\_change”. References: EGA IV (17.1.3), “(iii) smooth”.

> **Stacks 049U, formal smoothness under base change.**

```lean
public theorem FormallySmooth.baseChange
    (D : FppfFunctorPullbackSituation.{u, v})
    (ha : FormallySmooth D.a) :
    FormallySmooth D.toH
```

**`AlgebraicGeometry.Space.formallyEtale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean#L240). The attribute's comment: “formally\_etale\_base\_change”. References: EGA IV (17.1.3), “(iii) étale”.

> A base change of a formally étale transformation is formally étale.

```lean
public theorem formallyEtale_baseChange
    (D : FppfFunctorPullbackSituation.{u, v})
    (ha : FormallyEtale D.a) :
    FormallyEtale D.toH
```

**`AlgebraicGeometry.Space.formallyUnramified_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean#L252). The attribute's comment: “formally\_unramified\_base\_change”. References: EGA IV (17.1.3), “(iii) unramified”.

> The base change of a formally unramified transformation is formally
> unramified.

```lean
public theorem formallyUnramified_baseChange
    (D : FppfFunctorPullbackSituation.{u, v})
    (ha : FormallyUnramified D.a) :
    FormallyUnramified D.toH
```

## Tag 04AL, a lemma

[Tag 04AL](https://stacks.math.columbia.edu/tag/04AL) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean#L46). The attribute's comment: “etale\_implies\_formally\_etale”. References: EGA IV (17.1.3), “(i) open immersion”.

> An étale representable transformation on the big fppf site is formally étale.

```lean
public theorem formallyEtale_of_etale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G)
    (ha : (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a) :
    FormallyEtale a
```

**`AlgebraicGeometry.Space.formallySmooth_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean#L121). The attribute's comment: “etale\_implies\_formally\_smooth”. References: EGA IV (17.1.3), “(i) open immersion”.

> An étale representable transformation on the big fppf site is formally smooth.

```lean
public theorem formallySmooth_of_etale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G)
    (ha : (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a) :
    FormallySmooth a
```

**`AlgebraicGeometry.Space.formallySmooth_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Smooth.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Smooth.lean#L70). The attribute's comment: “part (1)”.

> **Stacks 04AL, part (1).** A smooth representable transformation on the big fppf site is
> formally smooth.

```lean
public theorem formallySmooth_of_smooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G)
    (ha : (MorphismProperty.inverseImage
      (@Smooth.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a) :
    FormallySmooth a
```

**`AlgebraicGeometry.Space.formallySmooth_formallyEtale_formallyUnramified_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/SmoothEtaleUnramified.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/SmoothEtaleUnramified.lean#L70). References: EGA 0 (19.0.1), “partial”; SGA 3 XI (1.6), “necessity direction”.

> **Stacks 04AL.**  Let `S` be a scheme, let `F` and `G` be set-valued functors on the big
> fppf site over `S`, and let `a : F ⟶ G` be a representable transformation of functors.  Then
>
> 1. if `a` is smooth it is formally smooth;
> 2. if `a` is étale it is formally étale;
> 3. if `a` is unramified it is formally unramified.
>
> Each part is proved by turning the lifting problem into one for the scheme representing the
> base change of `a` along a point of the target, where the corresponding implication for
> morphisms of schemes applies; see
> `AlgebraicGeometry.Space.formallySmooth_of_smooth`,
> `AlgebraicGeometry.Space.formallyEtale_of_etale` and
> `AlgebraicGeometry.Space.formallyUnramified_of_unramified`, which this statement assembles.

```lean
public theorem formallySmooth_formallyEtale_formallyUnramified_of_representable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) :
    ((MorphismProperty.inverseImage (@Smooth.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a → FormallySmooth a) ∧
      ((MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a → FormallyEtale a) ∧
      ((MorphismProperty.inverseImage (@Unramified.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a → FormallyUnramified a)
```

**`AlgebraicGeometry.Space.formallyUnramified_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Unramified.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Unramified.lean#L189). The attribute's comment: “unramified\_implies\_formally\_unramified”.

> **Stacks Project, Tag 04AL.** An unramified representable transformation is
> formally unramified.

```lean
public theorem formallyUnramified_of_unramified
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G)
    (ha : (MorphismProperty.inverseImage
      (@Unramified.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a) :
    FormallyUnramified a
```

## Tag 04CY, a lemma

[Tag 04CY](https://stacks.math.columbia.edu/tag/04CY) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_comp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean#L108). The attribute's comment: “compose\_formally\_etale”.

> An étale transformation followed by a formally étale transformation is formally étale.

```lean
public theorem formallyEtale_comp_of_etale
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {a : F ⟶ G} {b : G ⟶ H}
    (ha : (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a)
    (hb : FormallyEtale b) :
    FormallyEtale (a ≫ b)
```

**`AlgebraicGeometry.Space.formallySmooth_comp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Etale.lean#L133). The attribute's comment: “compose\_formally\_smooth”.

> An étale transformation followed by a formally smooth transformation is formally smooth.

```lean
public theorem formallySmooth_comp_of_etale
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {a : F ⟶ G} {b : G ⟶ H}
    (ha : (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a)
    (hb : FormallySmooth b) :
    FormallySmooth (a ≫ b)
```

**`AlgebraicGeometry.Space.exists_etale_affine_local_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleLocalLift.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleLocalLift.lean#L210). The attribute's comment: “local\_formal\_smooth\_lift”.

> **Stacks 04CY, the local form of the descent half.** In a representable, surjective, étale
> situation `F ⟶ G ⟶ H` over an affine square-zero thickening `i : T ⟶ T'`, a formally smooth
> composite admits, over every point of `T`, an affine étale neighbourhood `U' ⟶ T'` of its
> image and a section of `G` over `U'` which lifts the given section of `H` and agrees with the
> given section of `G` over `T` after restriction to every common refinement.

```lean
public theorem exists_etale_affine_local_lift
    (D : RepresentableSurjectiveEtaleSituation.{u})
    (T T' : BigFppfOver D.B D.S D.hS) (i : T ⟶ T')
    (_hT' : IsAffine ((BigFppfOver.toScheme D.B D.S D.hS).obj T'))
    (hi : IsSquareZeroClosedImmersion D.B D.S D.hS i)
    (x : D.G.obj (op T)) (y : D.H.obj (op T'))
    (hxy : D.b.app (op T) x = D.H.map i.op y)
    (hsmooth : FormallySmooth (D.a ≫ D.b))
    (t : (BigFppfOver.toScheme D.B D.S D.hS).obj T) :
    ∃ (U' : BigFppfOver D.B D.S D.hS) (j : U' ⟶ T') (z : D.G.obj (op U')),
      IsAffine ((BigFppfOver.toScheme D.B D.S D.hS).obj U') ∧
      Etale ((BigFppfOver.toScheme D.B D.S D.hS).map j) ∧
      (∃ u : (BigFppfOver.toScheme D.B D.S D.hS).obj U',
        ((BigFppfOver.toScheme D.B D.S D.hS).map j).base u =
          ((BigFppfOver.toScheme D.B D.S D.hS).map i).base t) ∧
      D.b.app (op U') z = D.H.map j.op y ∧
      ∀ (V : BigFppfOver D.B D.S D.hS) (f : V ⟶ T) (g : V ⟶ U'),
        f ≫ i = g ≫ j → D.G.map f.op x = D.G.map g.op z
```

**`AlgebraicGeometry.Space.formallyUnramified_comp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Unramified.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Unramified.lean#L219). The attribute's comment: “compose\_formally\_unramified”.

> A formally unramified transformation remains formally unramified after
> precomposition with an étale transformation.

```lean
public theorem formallyUnramified_comp_of_etale
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (b : G ⟶ H)
    (ha : (MorphismProperty.inverseImage (@Etale :
      MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a)
    (hb : FormallyUnramified b) :
    FormallyUnramified (a ≫ b)
```

**`AlgebraicGeometry.Space.formallyUnramified_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L181). The attribute's comment: “part (5), corrected form: G separated for the étale topology; false as written, see DoubledSection.Rational.not\_forall\_descend”.

> **Stacks 04CY**, the corrected part (5) of the tag. In a
> representable, surjective, étale situation, a formally unramified composite forces the second
> transformation to be formally unramified as soon as the intermediate presheaf is separated for
> the étale topology.
>
> Separatedness is the whole of what is used, and it is exactly the step the tag's own proof
> takes: having identified two sections of `G` after pullback along an étale covering, that proof
> concludes "hence `f = g` as `W' → T'` is an étale covering".
>
> It cannot be dropped: the tag states this part for arbitrary set-valued functors, and in that
> generality it is false. The counterexample is
> `AlgebraicGeometry.Space.DoubledSection.exists_not_formallyUnramified_of_comp`, which doubles
> the sections of the functor of points of the thickening that factor through neither the étale
> cover nor the thickened object. This is an erratum to the source statement.
>
> An intermediate presheaf which is an algebraic space over `S` is separated for the étale
> topology, so `AlgebraicGeometry.Space.formallyUnramified_of_formallyUnramified_comp` is the
> special case of this result at such a presheaf, as is
> `AlgebraicGeometry.Space.formallyUnramified_of_comp`, which asks the full sheaf condition.

```lean
public theorem formallyUnramified_of_comp_of_isSeparated
    (s : RepresentableSurjectiveEtaleSituation.{u})
    (hG : Presieve.IsSeparated ((etaleTopology s.B).over (s.B.obj s.hS)) s.G)
    (hba : FormallyUnramified (s.a ≫ s.b)) :
    FormallyUnramified s.b
```

**`AlgebraicGeometry.Space.formallyUnramified_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L277). The attribute's comment: “descend\_formally\_unramified”.

> In a representable, surjective, étale situation, a formally unramified composite forces the
> second transformation to be formally unramified as soon as the intermediate presheaf is a sheaf
> for the étale topology.
>
> This is the special case of
> `AlgebraicGeometry.Space.formallyUnramified_of_comp_of_isSeparated` at a presheaf which
> satisfies the full sheaf condition rather than merely separatedness, so it is a weaker statement
> than the corrected part (5) of Stacks 04CY, whose registration as that part sits on that
> result.

```lean
public theorem formallyUnramified_of_comp
    (s : RepresentableSurjectiveEtaleSituation.{u})
    (hG : Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.G)
    (hba : FormallyUnramified (s.a ≫ s.b)) :
    FormallyUnramified s.b
```

**`AlgebraicGeometry.Space.formallyEtale_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L303). The attribute's comment: “part (6), corrected form: G a sheaf and H separated for the étale topology; false as written, see DoubledSection.Rational.not\_forall\_descend”.

> **Stacks 04CY**, the corrected part (6) of the tag. In
> a representable, surjective, étale situation, a formally étale composite forces the second
> transformation to be formally étale as soon as the intermediate presheaf is a sheaf for the
> étale topology and the target presheaf is separated for it.
>
> Separatedness is all that the target presheaf contributes, and it is all the tag's own proof
> asks of it: `H` enters only to compare two sections of `H` that already agree over an étale
> covering. The intermediate presheaf genuinely needs the full sheaf condition, since the proof
> glues the étale-local solutions produced by part (4) — "hence we may glue the local solutions
> to get assertion (6)" in the tag.
>
> The tag states this part for arbitrary set-valued functors, and in that generality it is
> false: the situation of
> `AlgebraicGeometry.Space.DoubledSection.exists_not_formallyUnramified_of_comp` has a formally
> étale composite and a second transformation that is not formally étale. This is an erratum to
> the source statement.

```lean
public theorem formallyEtale_of_comp_of_isSeparated
    (s : RepresentableSurjectiveEtaleSituation.{u})
    (hG : Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.G)
    (hH : Presieve.IsSeparated ((etaleTopology s.B).over (s.B.obj s.hS)) s.H)
    (hba : FormallyEtale (s.a ≫ s.b)) :
    FormallyEtale s.b
```

**`AlgebraicGeometry.Space.formallyEtale_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L450). The attribute's comment: “descend\_formally\_etale”.

> In a representable, surjective, étale situation, a formally étale composite forces the
> second transformation to be formally étale as soon as the intermediate and target presheaves
> are sheaves for the étale topology.
>
> This is the corollary of `AlgebraicGeometry.Space.formallyEtale_of_comp_of_isSeparated`
> obtained by strengthening separatedness of the target presheaf to the full sheaf condition, so
> it states a special case of the corrected part (6) of Stacks 04CY, whose registration as that
> part sits on that result.

```lean
public theorem formallyEtale_of_comp
    (s : RepresentableSurjectiveEtaleSituation.{u})
    (hG : Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.G)
    (hH : Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.H)
    (hba : FormallyEtale (s.a ≫ s.b)) :
    FormallyEtale s.b
```

**`AlgebraicGeometry.Space.formallyUnramified_of_formallyUnramified_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleDescent.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleDescent.lean#L462). The attribute's comment: “part (5), for a middle functor which is an algebraic space”.

> Let `p : F ⟶ G` be a representable, surjective and étale transformation of set-valued
> functors on the big fppf site of `S`, let `q : G ⟶ H` and let `G` be an algebraic space over `S`.
> If `p ≫ q` is formally unramified in the sense of [Stacks Project, Tag 049S], then so is `q`.
>
> The corrected part (5) asks `G` to be separated for the étale topology, and an algebraic space
> is (see the implementation notes of this file), so this is a special case of
> `AlgebraicGeometry.Space.formallyUnramified_of_comp_of_isSeparated`, which carries the
> corrected part (5). This proof uses a hypothesis of a different kind — separatedness for the
> fpqc topology, which follows from the representable diagonal alone. The composition direction
> is `AlgebraicGeometry.Space.formallyUnramified_comp_of_etale`.

```lean
theorem formallyUnramified_of_formallyUnramified_comp (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : F ⟶ G) (q : G ⟶ H)
    (hG : IsAlgebraicSpace B S hS G)
    (hps : (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf p)
    (hpe : (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf p)
    (hpq : FormallyUnramified (p ≫ q)) :
    FormallyUnramified q
```

**`AlgebraicGeometry.Space.DoubledSection.Rational.not_forall_descend_formallyEtale_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DescentFormallyEtaleNeedsSeparatedTarget.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DescentFormallyEtaleNeedsSeparatedTarget.lean#L269). The attribute's comment: “counterexample to part (6) with G an étale sheaf and H arbitrary: the condition on H in the corrected form cannot be dropped”.

> **Part (6) of Stacks 04CY is false when only the intermediate functor is asked to be an
> étale sheaf.** The universal statement "for every representable, surjective, étale `a : F ⟶ G`
> and every `b : G ⟶ H` with `F` and `G` étale sheaves, `b` is formally étale when `b ∘ a` is"
> fails, already over `Spec ℚ`.
>
> So the corrected part (6), `AlgebraicGeometry.Space.formallyEtale_of_comp_of_isSeparated`, needs
> its hypothesis on the target functor `H` as well as its hypothesis on `G`; the latter is shown
> necessary by `AlgebraicGeometry.Space.DoubledSection.Rational.not_forall_descend`.

```lean
public theorem not_forall_descend_formallyEtale_of_isSheaf :
    ¬ (∀ s : RepresentableSurjectiveEtaleSituation.{0},
        Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.F →
        Presheaf.IsSheaf ((etaleTopology s.B).over (s.B.obj s.hS)) s.G →
        FormallyEtale (s.a ≫ s.b) → FormallyEtale s.b)
```

**`AlgebraicGeometry.Space.DoubledSection.Rational.not_forall_descend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DescentFormallyUnramifiedNeedsSeparatedRational.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/DescentFormallyUnramifiedNeedsSeparatedRational.lean#L268). The attribute's comment: “counterexample to parts (5),(6) as written”.

> **Parts (5) and (6) of Stacks 04CY are false as written.** The source states, for an
> arbitrary representable, surjective, étale `a : F ⟶ G` and any `b : G ⟶ H` of set-valued
> functors on a big fppf site, that `b` is formally unramified when `b ∘ a` is (part (5)) and
> formally étale when `b ∘ a` is (part (6)). Both universal statements fail, already over
> `Spec ℚ`.
>
> The corrected forms are `AlgebraicGeometry.Space.formallyUnramified_of_comp_of_isSeparated`
> and `AlgebraicGeometry.Space.formallyEtale_of_comp_of_isSeparated`.

```lean
theorem not_forall_descend :
    ¬ (∀ s : RepresentableSurjectiveEtaleSituation.{0},
        FormallyUnramified (s.a ≫ s.b) → FormallyUnramified s.b) ∧
      ¬ (∀ s : RepresentableSurjectiveEtaleSituation.{0},
        FormallyEtale (s.a ≫ s.b) → FormallyEtale s.b)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.hasPullbacks_bigAffineFppf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L138), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L93) (StacksFrontier): “fibre products in the big affine fppf site”.
- [`AlgebraicGeometry.preservesPullbacks_bigAffineFppfToScheme`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L145), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedEtaleDescent.lean#L96) (StacksFrontier): “preservation by the big affine fppf functor to schemes”.

## Tag 04G5, a lemma

[Tag 04G5](https://stacks.math.columbia.edu/tag/04G5) in the Stacks Project.

**`AlgebraicGeometry.Space.formallySmooth_of_comp_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean#L75). The attribute's comment: “smooth”. References: EGA IV (17.1.4), “formally smooth case”; EGA IV (17.1.5), “necessity, smooth”.

> **Stacks 04G5, smooth.** Formal smoothness of a composite descends to its
> first factor when the second factor is formally unramified.

```lean
public theorem formallySmooth_of_comp_of_formallyUnramified (a : F ⟶ G) (b : G ⟶ H)
    (hb : FormallyUnramified b)
    (hba : FormallySmooth (a ≫ b)) :
    FormallySmooth a
```

**`AlgebraicGeometry.Space.formallyEtale_of_comp_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean#L87). The attribute's comment: “etale”. References: EGA IV (17.1.4), “formally étale case”; EGA IV (17.1.5), “necessity, étale”.

> **Stacks 04G5, étale case.** A first factor of a formally étale
> transformation is formally étale if the second factor is formally unramified.

```lean
public theorem formallyEtale_of_comp_of_formallyUnramified (a : F ⟶ G) (b : G ⟶ H)
    (hb : FormallyUnramified b)
    (hba : FormallyEtale (a ≫ b)) :
    FormallyEtale a
```

**`AlgebraicGeometry.Space.formallyUnramified_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Factor.lean#L101). The attribute's comment: “unramified”. References: EGA IV (17.1.3), “(v), b fmly unramified”; EGA IV (17.1.5), “necessity, unramified”.

> **Stacks Project, Tag 04G5, unramified case.** If a transformation and a
> composite ending in it are formally unramified, so is the first factor.

```lean
public theorem formallyUnramified_left_of_comp (a : F ⟶ G) (b : G ⟶ H)
    (_hb : FormallyUnramified b)
    (hba : FormallyUnramified (a ≫ b)) :
    FormallyUnramified a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.13, Tag 04G3](https://stacks.math.columbia.edu/tag/04G3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
