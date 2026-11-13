---
declaration: section
origin: cited
lean: SheafOfModules.GradedAlgebra.UnitalHom, SheafOfModules.GradedAlgebra.Hom, SheafOfModules.GradedAlgebra, SheafOfModules.reesGradedAlgebra, Stacks.Sheaves.GradedAlgebraEssentiallySmall.gradedAlgebraPullbackPushforwardAdjunction, SheafOfModules.GradedAlgebra.transport, SheafOfModules.GradedAlgebra.transportFunctor, SheafOfModules.GradedAlgebra.transportAdjunction
statement: formalized
proof: formalized
---

# 24.3 Sheaves of graded algebras

Section 24.3 of the Stacks Project, [Tag 0FQV](https://stacks.math.columbia.edu/tag/0FQV). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FQW, a definition

[Tag 0FQW](https://stacks.math.columbia.edu/tag/0FQW) in the Stacks Project.

**`SheafOfModules.GradedAlgebra.UnitalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullback.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullback.lean#L121). The attribute's comment: “unital homomorphisms of sheaves of graded algebras”.

> A unital homomorphism of sheaves of graded algebras.

```lean
structure UnitalHom (A B : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedAlgebra.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraBridge.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraBridge.lean#L118). The attribute's comment: “homomorphisms of sheaves of graded algebras, and the category they form”.

> A homomorphism of sheaves of graded algebras: a morphism of sheaves of modules in each
> degree, preserving products of homogeneous local sections. The distinguished degree-zero unit
> need not be preserved; the homomorphisms that preserve it are `UnitalHom`.

```lean
structure Hom (A B : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedAlgebra`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean#L123). The attribute's comment: “sheaves of graded algebras, over a sheaf of rings on an arbitrary site”.

> A sheaf of `ℤ`-graded algebras over a sheaf of rings.

```lean
structure GradedAlgebra (R : Sheaf J RingCat.{t})
```

**`SheafOfModules.reesGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IdealSheafPowers.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IdealSheafPowers.lean#L513). The attribute's comment: “the graded algebra of the powers of a sheaf of ideals”. References: SGA 2 XII (4.2), “partial”.

> **The sheaf of graded algebras `⨁_{n ≥ 0} 𝓘ⁿ` of a sheaf of ideals.**  Its degree-`n`
> homogeneous piece is the `n`-th power of `𝓘` for `n ≥ 0` and the zero sheaf of ideals otherwise,
> and its multiplication is the multiplication of sections of the structure sheaf.

```lean
noncomputable def reesGradedAlgebra : GradedAlgebra.{t, t} R
```

## Tag 0FQX, a remark

[Tag 0FQX](https://stacks.math.columbia.edu/tag/0FQX) in the Stacks Project.

**`Stacks.Sheaves.GradedAlgebraEssentiallySmall.gradedAlgebraPullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraCounitEssentiallySmall.lean, line 673](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraCounitEssentiallySmall.lean#L673). The attribute's comment: “part (3): adjunction for graded algebras”.

> **Part (3) of Stacks 0FQX**: pullback of sheaves of graded algebras along a morphism of
> ringed topoi is left adjoint to the direct image, and the right adjoint has the direct-image
> graded algebras as its values on objects.
>
> The unit and the counit are `unitApp` and `counitApp`, whose degreewise components are those of
> the Stacks 03D7 adjunction for sheaves of modules; everything else is
> `adjunctionOfGradedUnitCounit`.

```lean
public noncomputable def gradedAlgebraPullbackPushforwardAdjunction :
    Σ G : SheafOfModules.GradedAlgebra.{w, w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) ⥤
        SheafOfModules.GradedAlgebra.{w, w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O),
      { _adj : (gradedAlgebraPullbackSpecification f.toRingedToposModulesHom).1 ⊣ G //
        ∀ A, G.obj A = pushforwardGradedAlgebra f A }
```

**`SheafOfModules.GradedAlgebra.transport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraFunctoriality.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraFunctoriality.lean#L340). The attribute's comment: “graded\_algebra\_pushforward, graded\_algebra\_pullback”.

> **The transport of a sheaf of graded algebras along a lax monoidal functor between
> categories of sheaves of modules**, with homogeneous pieces the images `F(A_n)` of those of
> `A`.

```lean
noncomputable def transport : GradedAlgebra.{w, w} (toRingCat K Psharp)
```

**`SheafOfModules.GradedAlgebra.transportFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraFunctoriality.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraFunctoriality.lean#L425). The attribute's comment: “graded\_algebra\_pushforward, graded\_algebra\_pullback: functoriality”.

> **A lax monoidal functor between categories of sheaves of modules induces a functor between
> the categories of sheaves of graded algebras.**

```lean
noncomputable def transportFunctor :
    GradedAlgebra.{w, w} (toRingCat J Osharp) ⥤ GradedAlgebra.{w, w} (toRingCat K Psharp)
```

**`SheafOfModules.GradedAlgebra.transportAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraMonoidalAdjunction.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraMonoidalAdjunction.lean#L221). The attribute's comment: “part (3): adjunction for graded algebras”.

> **The transport of sheaves of graded algebras along the left adjoint of a monoidal
> adjunction is left adjoint to the transport along the right adjoint.** For a morphism of ringed
> topoi this is part (3) of the functoriality of sheaves of graded algebras: the pullback of
> graded algebras is left adjoint to the pushforward, so homomorphisms `f^*B ⟶ A` correspond to
> homomorphisms `B ⟶ f_*A`, naturally in both arguments.

```lean
noncomputable def transportAdjunction :
    transportFunctor L hP hO ⊣ transportFunctor G hO hP
```

**`Stacks.Sheaves.GradedAlgebraPullback.gradedAlgebraPullbackSpecification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPullback.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPullback.lean#L206). The attribute's comment: “graded\_algebra\_pullback”.

> The degreewise module pullbacks assemble into a functor of sheaves of graded algebras, with
> the induced multiplication and unit.
>
> This is the pullback half of Stacks 0FQX.

```lean
public noncomputable def gradedAlgebraPullbackSpecification :
    GradedAlgebraPullbackSpecification f
```

**`Stacks.Sheaves.GradedAlgebraPullback.nonempty_gradedAlgebraPullbackSpecification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPullback.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPullback.lean#L222). The attribute's comment: “graded\_algebra\_pullback”.

> A pullback of sheaves of graded algebras exists.
>
> This is the pullback half of Stacks 0FQX; see `gradedAlgebraPullbackSpecification`.

```lean
public theorem nonempty_gradedAlgebraPullbackSpecification :
    Nonempty (GradedAlgebraPullbackSpecification f)
```

**`Stacks.Sheaves.GradedAlgebraPushforward.exists_pushforwardGradedAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPushforward/Construction.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPushforward/Construction.lean#L264). The attribute's comment: “graded\_algebra\_pushforward”.

> A graded algebra whose pieces and operations are the canonical direct images
> of those of the source exists.

```lean
public theorem exists_pushforwardGradedAlgebra
    {X : RingedTopos.{u, u, u}}
    {Y : RingedTopos.{u', u', u'}}
    (f : RingedToposHom X Y)
    (A : SheafOfModules.GradedAlgebra
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.ringedSite X).O)) :
    ∃ B : SheafOfModules.GradedAlgebra
        (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.ringedSite Y).O),
      IsPushforwardGradedAlgebra f A B
```

**`Stacks.Sheaves.GradedAlgebraPushforward.pushforwardGradedAlgebraData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPushforward/Construction.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedAlgebraPushforward/Construction.lean#L277). The attribute's comment: “graded\_algebra\_pushforward”.

> A graded algebra together with its direct-image specification.

```lean
public noncomputable def pushforwardGradedAlgebraData
    {X : RingedTopos.{u, u, u}}
    {Y : RingedTopos.{u', u', u'}}
    (f : RingedToposHom X Y)
    (A : SheafOfModules.GradedAlgebra
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.ringedSite X).O)) :
    { B : SheafOfModules.GradedAlgebra
        (Stacks.SheafOfModules.Tensor.ringSheaf (RingedTopos.ringedSite Y).O) //
      IsPushforwardGradedAlgebra f A B }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.3, Tag 0FQV](https://stacks.math.columbia.edu/tag/0FQV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
