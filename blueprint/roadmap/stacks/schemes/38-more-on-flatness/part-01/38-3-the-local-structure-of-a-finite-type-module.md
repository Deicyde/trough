---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finitePresentation_closedSubscheme_fiber_eq_supp, AlgebraicGeometry.exists_elementaryDevissage, AlgebraicGeometry.ElementaryDevissage.finitePresentation_π, AlgebraicGeometry.ElementaryDevissage.isFinitePresentationNear_iff_closed, AlgebraicGeometry.ElementaryDevissage.isFinitePresentationNear_iff_pushforward, AlgebraicGeometry.ElementaryDevissage.finitePresentation_stalk_iff_closed, AlgebraicGeometry.ElementaryDevissage.finitePresentation_stalk_iff_pushforward, AlgebraicGeometry.ElementaryDevissage.isFlatOverAt_iff_closed
statement: formalized
proof: formalized
---

# 38.3 The local structure of a finite type module

Section 38.3 of the Stacks Project, [Tag 057P](https://stacks.math.columbia.edu/tag/057P). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 057Q, a lemma

[Tag 057Q](https://stacks.math.columbia.edu/tag/057Q) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_closedSubscheme_fiber_eq_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FiniteTypeModuleLocalStructure.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FiniteTypeModuleLocalStructure.lean#L264).

> **[Stacks, Tag 057Q].** Let `f : X ⟶ S` be a finite type morphism of affine schemes and let
> `F` be a quasi-coherent `𝒪_X`-module of finite type. For every point `s` of `S` there is a closed
> immersion `i : Z ⟶ X` of finite presentation and a quasi-coherent finite type `𝒪_Z`-module `G`
> with `i_* G ≅ F` whose fibre over `s` is the support of the restriction of `F` to the fibre of
> `X` over `s`.
>
> The equality of the fibre with the support is an equality of subsets of `X`: the image of the
> fibre of `Z` is the image of the support of the pullback of `F` to the fibre of `X`.

```lean
theorem exists_finitePresentation_closedSubscheme_fiber_eq_supp {S : Scheme.{u}} (f : X ⟶ S)
    [IsAffine X] [IsAffine S] [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (s : S) :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X) (G : Z.Modules)
      (_ : (Scheme.Modules.pushforward i).obj G ≅ F),
      IsClosedImmersion i ∧ FinitePresentation i ∧ G.IsQuasicoherent ∧ G.IsFiniteType ∧
        Set.range (fun z : (i ≫ f).fiber s => i ((i ≫ f).fiberι s z)) =
          f.fiberι s '' SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)
```

## Tag 057S, a lemma

[Tag 057S](https://stacks.math.columbia.edu/tag/057S) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryDevissage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/ElementaryDevissage.lean, line 811](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/ElementaryDevissage.lean#L811).

> **Stacks Project, Tag 057S.** A finite-type quasi-coherent module admits an elementary
> dévissage at any point of the support of its fibre.

```lean
theorem exists_elementaryDevissage {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (x : X)
    (hx : f.asFiber x ∈
      SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι (f x))).obj F)) :
    Nonempty (ElementaryDevissage f F x hx)
```

## Tag 057T, a lemma

[Tag 057T](https://stacks.math.columbia.edu/tag/057T) in the Stacks Project.

**`AlgebraicGeometry.ElementaryDevissage.finitePresentation_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean#L338). The attribute's comment: “finite presentation of π”.

> **Stacks Project, Tag 057T.** The finite morphism `π` of an elementary dévissage of a
> morphism locally of finite presentation is of finite presentation.
>
> The composite `Z ⟶ Y ⟶ V` equals `Z ⟶ U ⟶ X ⟶ S`, which is locally of finite presentation
> because the closed immersion `i` is, `U ⟶ X` is étale and `f` is; the structure morphism
> `V ⟶ S` is locally of finite type, so Stacks 02FV strips it off twice and leaves `π` locally of
> finite presentation. A finite morphism is quasi-compact and quasi-separated, so `π` is of finite
> presentation.

```lean
theorem finitePresentation_π [LocallyOfFinitePresentation f] (D : ElementaryDevissage f F x hx) :
    FinitePresentation D.π
```

**`AlgebraicGeometry.ElementaryDevissage.isFinitePresentationNear_iff_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean#L361). The attribute's comment: “equivalence of (1), (2) and (3)”.

> **Stacks Project, Tag 057T**, the equivalence of conditions (1) and (2). In an elementary
> dévissage, `F` is of finite presentation near `x` exactly when the module `G` on the closed
> subscheme is of finite presentation near `z`.
>
> Finite presentation near `x` passes to the étale neighbourhood `U` and back by Stacks 01BQ and
> Stacks 05B0; on `U` the module is `i_* G` by the dévissage isomorphism, and the closed immersion
> `i` is finite with singleton fibre, so Stacks 05B4 and Stacks 05B8 exchange `i_* G` and `G`.

```lean
theorem isFinitePresentationNear_iff_closed [F.IsQuasicoherent]
    (D : ElementaryDevissage f F x hx) :
    IsFinitePresentationNear F x ↔ IsFinitePresentationNear D.G D.z
```

**`AlgebraicGeometry.ElementaryDevissage.isFinitePresentationNear_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean#L382). The attribute's comment: “equivalence of (1), (2) and (3)”.

> **Stacks Project, Tag 057T**, the equivalence of conditions (2) and (3). In an elementary
> dévissage of a morphism locally of finite presentation, the module `G` is of finite presentation
> near `z` exactly when its direct image `π_* G` is of finite presentation near `π z`.
>
> The morphism `π` is finite, of finite presentation by
> `AlgebraicGeometry.ElementaryDevissage.finitePresentation_π`, and its fibre over `π z` is `{z}`,
> so this is the transfer across a finite morphism with a singleton fibre.

```lean
theorem isFinitePresentationNear_iff_pushforward [LocallyOfFinitePresentation f]
    (D : ElementaryDevissage f F x hx) :
    IsFinitePresentationNear D.G D.z ↔
      IsFinitePresentationNear ((Scheme.Modules.pushforward D.π).obj D.G) (D.π D.z)
```

**`AlgebraicGeometry.ElementaryDevissage.finitePresentation_stalk_iff_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean#L400). The attribute's comment: “equivalence of (a), (b) and (c)”.

> **Stacks Project, Tag 057T**, the equivalence of conditions (a) and (b). In an elementary
> dévissage the stalk `F_x` is a finitely presented `𝒪_{X,x}`-module exactly when the stalk `G_z`
> is a finitely presented `𝒪_{Z,z}`-module.
>
> The étale morphism `U ⟶ X` is flat, so the stalk map `𝒪_{X,x} → 𝒪_{U,i z}` is a flat local
> homomorphism and finite presentation of the stalk is unchanged by the pullback; the pullback of
> `F` to `U` is `i_* G`; and the closed immersion `i` is finite, of finite presentation and has
> singleton fibre, so Stacks 05B8 and Stacks 0564 exchange `(i_* G)_{i z}` and `G_z`.

```lean
theorem finitePresentation_stalk_iff_closed (D : ElementaryDevissage f F x hx) :
    Module.FinitePresentation (ToType (X.presheaf.stalk x))
        (ToType (TopCat.Presheaf.stalk F.val.presheaf x)) ↔
      Module.FinitePresentation (ToType (D.Z.presheaf.stalk D.z))
        (ToType (TopCat.Presheaf.stalk D.G.val.presheaf D.z))
```

**`AlgebraicGeometry.ElementaryDevissage.finitePresentation_stalk_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FinitePresentationTransfer.lean#L425). The attribute's comment: “equivalence of (a), (b) and (c)”.

> **Stacks Project, Tag 057T**, the equivalence of conditions (b) and (c). In an elementary
> dévissage of a morphism locally of finite presentation the stalk `G_z` is a finitely presented
> `𝒪_{Z,z}`-module exactly when the stalk `(π_* G)_{π z}` is a finitely presented
> `𝒪_{Y,π z}`-module.
>
> The morphism `π` is finite, of finite presentation by
> `AlgebraicGeometry.ElementaryDevissage.finitePresentation_π`, and its fibre over `π z` is `{z}`,
> so this is the transfer of finite presentation of a stalk across a finite morphism with a
> singleton fibre.

```lean
theorem finitePresentation_stalk_iff_pushforward [LocallyOfFinitePresentation f]
    (D : ElementaryDevissage f F x hx) :
    Module.FinitePresentation (ToType (D.Z.presheaf.stalk D.z))
        (ToType (TopCat.Presheaf.stalk D.G.val.presheaf D.z)) ↔
      Module.FinitePresentation (ToType (D.Y.presheaf.stalk (D.π D.z)))
        (ToType (TopCat.Presheaf.stalk
          ((Scheme.Modules.pushforward D.π).obj D.G).val.presheaf (D.π D.z)))
```

## Tag 057U, a lemma

[Tag 057U](https://stacks.math.columbia.edu/tag/057U) in the Stacks Project.

**`AlgebraicGeometry.ElementaryDevissage.isFlatOverAt_iff_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean#L252). The attribute's comment: “equivalence of (a), (b) and (c)”.

> **Stacks Project, Tag 057U**, the equivalence of conditions (a) and (b). In an elementary
> dévissage the stalk `F_x` is flat over `𝒪_{S,f x}` exactly when the stalk `G_z` is flat over
> `𝒪_{V,h (π z)}`.
>
> The étale morphism `U ⟶ X` is flat, so Stacks 02JZ replaces `F` at `x` by its pullback to `U` at
> the distinguished point; Stacks 05B9 replaces flatness over `S` by flatness over `V`; the
> pullback of `F` to `U` is `i_* G`; and the closed immersion `i` is finite with singleton fibre,
> so Stacks 05B8 exchanges the stalk of `i_* G` for the stalk of `G`.

```lean
theorem isFlatOverAt_iff_closed [F.IsQuasicoherent] (D : ElementaryDevissage f F x hx) :
    IsFlatOverAt f.toLRSHom.toShHom F x ↔
      IsFlatOverAt (D.π ≫ D.h).toLRSHom.toShHom D.G D.z
```

**`AlgebraicGeometry.ElementaryDevissage.isFlatOverAt_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean#L286). The attribute's comment: “equivalence of (a), (b) and (c)”.

> **Stacks Project, Tag 057U**, the equivalence of conditions (b) and (c). In an elementary
> dévissage the stalk `G_z` is flat over `𝒪_{V,h (π z)}` exactly when the stalk `(π_* G)_{π z}`
> is.
>
> The morphism `π` is finite and its fibre over `π z` is `{z}`, so this is the transfer of
> flatness over the base at a point across a finite morphism with a singleton fibre.

```lean
theorem isFlatOverAt_iff_pushforward (D : ElementaryDevissage f F x hx) :
    IsFlatOverAt (D.π ≫ D.h).toLRSHom.toShHom D.G D.z ↔
      IsFlatOverAt D.h.toLRSHom.toShHom
        ((Scheme.Modules.pushforward D.π).obj D.G) (D.π D.z)
```

**`AlgebraicGeometry.ElementaryDevissage.isFlatOverNear_iff_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean#L302). The attribute's comment: “equivalence of (1), (2) and (3)”.

> **Stacks Project, Tag 057U**, the equivalence of conditions (1) and (2). In an elementary
> dévissage, `F` is flat over `S` near `x` exactly when `G` is flat over `V` near `z`.
>
> The étale morphism `U ⟶ X` is flat and open, so Stacks 02JZ transfers flatness over the base
> near `x` to flatness of the pullback near the distinguished point of `U`; Stacks 05B9 interchanges
> flatness over `S` and over `V`; the pullback is `i_* G`; and the closed immersion `i` is finite
> with singleton fibre, so Stacks 0FLM and Stacks 05B8 exchange `i_* G` and `G`.

```lean
theorem isFlatOverNear_iff_closed [F.IsQuasicoherent] (D : ElementaryDevissage f F x hx) :
    IsFlatOverNear f F x ↔ IsFlatOverNear (D.π ≫ D.h) D.G D.z
```

**`AlgebraicGeometry.ElementaryDevissage.isFlatOverNear_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/FlatnessTransfer.lean#L324). The attribute's comment: “equivalence of (1), (2) and (3)”.

> **Stacks Project, Tag 057U**, the equivalence of conditions (2) and (3). In an elementary
> dévissage, `G` is flat over `V` near `z` exactly when `π_* G` is flat over `V` near `π z`.
>
> The morphism `π` is finite and its fibre over `π z` is `{z}`, so this is the transfer of
> flatness over the base near a point across a finite morphism with a singleton fibre.

```lean
theorem isFlatOverNear_iff_pushforward (D : ElementaryDevissage f F x hx) :
    IsFlatOverNear (D.π ≫ D.h) D.G D.z ↔
      IsFlatOverNear D.h ((Scheme.Modules.pushforward D.π).obj D.G) (D.π D.z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.3, Tag 057P](https://stacks.math.columbia.edu/tag/057P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
