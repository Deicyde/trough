---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FiniteOpenSubspace, AlgebraicGeometry.Space.finiteOpenSubspacePresheaf, AlgebraicGeometry.Space.isSheaf_finiteOpenSubspacePresheaf, AlgebraicGeometry.Space.finiteOpenSubspaceEquiv, AlgebraicGeometry.Space.finiteOpenSubspaceMap, AlgebraicGeometry.Space.isIso_finiteOpenSubspaceMap_locallyQuasiFinitePart, AlgebraicGeometry.Space.FiniteOpenSubspace.isClosedSubspace, AlgebraicGeometry.Space.FinitePartFibre.zeroFibre
statement: formalized
proof: formalized
---

# 79.12 The finite part of a morphism

Section 79.12 of the Stacks Project, [Tag 04PB](https://stacks.math.columbia.edu/tag/04PB). 16 tags here are carried by 90 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04PC, an equation

[Tag 04PC](https://stacks.math.columbia.edu/tag/04PC) in the Stacks Project.

**`AlgebraicGeometry.Space.FiniteOpenSubspace`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Basic.lean#L55).

> **Stacks 04PC.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and an algebraic
> space `T`, a morphism `T ⟶ Y` together with an open subspace of `T ×_Y X` which is finite
> over `T`.

```lean
structure FiniteOpenSubspace (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (T : AlgebraicSpaces B S hS)
```

## Tag 04PD, an equation

[Tag 04PD](https://stacks.math.columbia.edu/tag/04PD) in the Stacks Project.

**`AlgebraicGeometry.Space.finiteOpenSubspacePresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Presheaf.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Presheaf.lean#L101).

> **Stacks 04PD.** The finite part `(X/Y)_fin` of a morphism `f : X ⟶ Y` of algebraic spaces
> over `S`: the presheaf whose sections over a scheme `T` are the pairs consisting of a morphism
> `T ⟶ Y` and an open subspace of `T ×_Y X` finite over `T`, with restriction given by base
> change.

```lean
noncomputable def finiteOpenSubspacePresheaf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    FinitePartPresheaf B S hS f
```

## Tag 04PE, a lemma

[Tag 04PE](https://stacks.math.columbia.edu/tag/04PE) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheaf_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/FppfSheaf.lean, line 809](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/FppfSheaf.lean#L809). The attribute's comment: “part (1)”.

> **Stacks 04PE, part (1).** For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme
> `S`, the finite part `(X/Y)_fin` of `f` satisfies the sheaf condition for the fppf topology of
> the big fppf site of `S`.

```lean
public theorem isSheaf_finiteOpenSubspacePresheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (finiteOpenSubspacePresheaf B S hS f).toFunctor
```

**`AlgebraicGeometry.Space.finiteOpenSubspaceEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/FppfSheaf.lean, line 1023](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/FppfSheaf.lean#L1023). The attribute's comment: “part (2)”.

> **Stacks 04PE, part (2).** For an algebraic space `T` over `S`, the morphisms of sheaves
> from `T` to the finite part `(X/Y)_fin` of `f : X ⟶ Y` are in canonical bijection with the
> pairs `(a, Z)` of Stacks 04PC over `T`: the pair attached to a morphism restricts, along every
> morphism from a scheme of the site, to the pair that the morphism names there.

```lean
public noncomputable def finiteOpenSubspaceEquiv
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (T : AlgebraicSpaces B S hS) :
    { e : (T.obj ⟶ (finiteOpenSubspacePresheaf B S hS f).toFunctor) ≃
        FiniteOpenSubspace B S hS f T //
      ∀ (v : T.obj ⟶ (finiteOpenSubspacePresheaf B S hS f).toFunctor)
        (U : BigFppfOver B S hS)
        (g : yoneda.obj U ⟶ T.obj),
        let p := e v
        let q := (finiteOpenSubspacePresheaf B S hS f).sections U
          (v.app (op U) (yonedaEquiv g))
        (q.toBase.hom = g ≫ p.toBase.hom) ∧
          ∃ j : q.subspace.toFunctor ⟶ p.subspace.toFunctor,
            (IsPullback
              (q.subspace.ι ≫ pullback.fst q.toBase.hom f.hom)
              j g
              (p.subspace.ι ≫ pullback.fst p.toBase.hom f.hom)) ∧
            (j ≫ p.subspace.ι ≫ pullback.snd p.toBase.hom f.hom =
              q.subspace.ι ≫ pullback.snd q.toBase.hom f.hom) }
```

## Tag 04PF, a lemma

[Tag 04PF](https://stacks.math.columbia.edu/tag/04PF) in the Stacks Project.

**`AlgebraicGeometry.Space.finiteOpenSubspaceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/OpenImmersionMap.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/OpenImmersionMap.lean#L409).

> The canonical injective map `(X'/Y)₍fin₎ ⟶ (X/Y)₍fin₎` induced by an
> open immersion `X' ⟶ X` over `Y`. Its specification identifies each image
> finite open pair over a test scheme.

```lean
public noncomputable def finiteOpenSubspaceMap
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X' X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (j : X' ⟶ X) (f' : X' ⟶ Y) (f : X ⟶ Y)
    (hj : j ≫ f = f') (hjOpen : AlgebraicGeometry.Space.IsOpenImmersion B S hS j.hom) :
    { m : (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf B S hS f').toFunctor ⟶
        (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf B S hS f).toFunctor //
      Mono m ∧
        ∀ (T : AlgebraicGeometry.BigFppfOver B S hS)
          (s : (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf B S hS f').toFunctor.obj (op T)),
          let p := (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf B S hS f').sections T s
          let q := (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf B S hS f).sections T
            (m.app (op T) s)
          (p.toBase = q.toBase) ∧
            ∃ k : p.subspace.toFunctor ⟶ q.subspace.toFunctor,
              IsIso k ∧
                (k ≫ q.subspace.ι ≫ pullback.fst q.toBase.hom f.hom =
                  p.subspace.ι ≫ pullback.fst p.toBase.hom f'.hom) ∧
                (k ≫ q.subspace.ι ≫ pullback.snd q.toBase.hom f.hom =
                  p.subspace.ι ≫ pullback.snd p.toBase.hom f'.hom ≫ j.hom) }
```

## Tag 04PG, a lemma

[Tag 04PG](https://stacks.math.columbia.edu/tag/04PG) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_finiteOpenSubspaceMap_locallyQuasiFinitePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/LocallyQuasiFinitePart.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/LocallyQuasiFinitePart.lean#L336).

> **Stacks 04PG.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S` which
> is locally of finite type and let `X' ⊆ X` be the maximal open subspace over which `f` is
> locally quasi-finite, Stacks 04NW. Then `(X/Y)_fin = (X'/Y)_fin`, in the sense that the
> canonical injection `(X'/Y)_fin ⟶ (X/Y)_fin` of Stacks 04PF is an isomorphism.

```lean
theorem isIso_finiteOpenSubspaceMap_locallyQuasiFinitePart {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    IsIso (finiteOpenSubspaceMap B S hS (locallyQuasiFinitePartInclusion B S hS f hf)
      (locallyQuasiFinitePartInclusion B S hS f hf ≫ f) f rfl
      (isOpenImmersion_locallyQuasiFinitePartInclusion B S hS f hf)).1
```

## Tag 04PH, a lemma

[Tag 04PH](https://stacks.math.columbia.edu/tag/04PH) in the Stacks Project.

**`AlgebraicGeometry.Space.FiniteOpenSubspace.isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedClosed.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedClosed.lean#L66).

> **Stacks 04PH.** An open subspace of `T ×_Y X` which is finite over `T` is a closed
> subspace of `T ×_Y X`, provided `f : X ⟶ Y` is separated.

```lean
theorem FiniteOpenSubspace.isClosedSubspace (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (T : AlgebraicSpaces B S hS) (Z : FiniteOpenSubspace B S hS f T)
    (hf : IsSeparated B S hS f.hom) :
    IsClosedSubspace B S hS Z.subspace
```

## Tag 04PI, a remark

[Tag 04PI](https://stacks.math.columbia.edu/tag/04PI) in the Stacks Project.

**`AlgebraicGeometry.Space.FinitePartFibre.zeroFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L151). The attribute's comment: “zero\_as\_a\_section\_over\_any\_base”.

> **Stacks 04PI, the zero of the `F₂`-algebra.** The section `0 = (a, ∅)` cut out by no
> point at all, whose projection to `T` is finite because the empty open subspace is the
> coproduct of the empty family.

```lean
def zeroFibre (a : T ⟶ Y) : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.zeroSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L231). The attribute's comment: “zero\_section\_over\_the\_base”.

> **Stacks 04PI.** The zero section `0 = (1_Y, ∅)` of the `F₂`-algebra, as a section of the
> finite part over `Y`.

```lean
def zeroSection : Y.obj ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L237). The attribute's comment: “zero\_section\_is\_the\_empty\_subspace”.

> **Stacks 04PI.** On sections, the zero is the empty open subspace.

```lean
theorem sections_zeroSection (T : BigFppfOver B S hS) (y : Y.obj.obj (op T)) :
    P.sections T ((zeroSection P).app (op T) y) =
      (FinitePartFibre.zeroFibre
        (ObjectProperty.homMk (yonedaEquiv.symm y) : schemeSpace T ⟶ Y)).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.zeroSection_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L245). The attribute's comment: “zero\_section\_lies\_over\_the\_base”.

> **Stacks 04PI.** The zero is a section of the projection to `Y`.

```lean
theorem zeroSection_comp_baseMap : zeroSection P ≫ P.baseMap = 𝟙 Y.obj
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.oneSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L251). The attribute's comment: “unit\_section\_over\_the\_base”.

> **Stacks 04PI, the finite case.** The unit `1 = (1_Y, X)` of the `F₂`-algebra, as a section
> of the finite part over `Y`.

```lean
def oneSection (hfin : IsFinite B S hS f.hom) : Y.obj ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_oneSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L257). The attribute's comment: “unit\_section\_is\_the\_whole\_fibre\_product”.

> **Stacks 04PI, the finite case.** On sections, the unit is the whole fibre product.

```lean
theorem sections_oneSection (hfin : IsFinite B S hS f.hom) (T : BigFppfOver B S hS)
    (y : Y.obj.obj (op T)) :
    P.sections T ((oneSection P hfin).app (op T) y) =
      (FinitePartFibre.one (a := (ObjectProperty.homMk (yonedaEquiv.symm y) :
        schemeSpace T ⟶ Y)) hfin).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.oneSection_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L266). The attribute's comment: “unit\_section\_lies\_over\_the\_base”.

> **Stacks 04PI, the finite case.** The unit is a section of the projection to `Y`.

```lean
theorem oneSection_comp_baseMap (hfin : IsFinite B S hS f.hom) :
    oneSection P hfin ≫ P.baseMap = 𝟙 Y.obj
```

**`AlgebraicGeometry.Space.FinitePartFibre.nonUnitalCommRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L280). The attribute's comment: “f2\_algebra\_without\_unit”.

> **Stacks 04PI.** The sections of the finite part over `T` lying over a fixed `a : T ⟶ Y`
> form a commutative ring without unit: the multiplication is the intersection `⋆₂`, the addition
> is the symmetric difference `⋆₁(⋆₃(s, s'), ⋆₄(s, s'))` and the zero is `(a, ∅)`.

```lean
noncomputable def nonUnitalCommRing (hf : IsSeparated B S hS f.hom) (a : T ⟶ Y) :
    NonUnitalCommRing (FinitePartFibre B S hS f a)
```

**`AlgebraicGeometry.Space.FinitePartFibre.zmodModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L323). The attribute's comment: “f2\_algebra\_scalars”.

> **Stacks 04PI.** Every section is its own additive inverse, so the ring of sections over a
> fixed `a : T ⟶ Y` is an algebra over `F₂`.

```lean
noncomputable def zmodModule (hf : IsSeparated B S hS f.hom) (a : T ⟶ Y) :
    letI := nonUnitalCommRing hf a
    Module (ZMod 2) (FinitePartFibre B S hS f a)
```

**`AlgebraicGeometry.Space.FinitePartFibre.commRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L336). The attribute's comment: “f2\_algebra\_with\_its\_unit\_in\_the\_finite\_case”.

> **Stacks 04PI, the finite case.** When `f` is finite the sections of the finite part over a
> fixed `a : T ⟶ Y` form a commutative ring, the unit being the section `(a, T ×_Y X)` and the
> remaining structure that of the `F₂`-algebra.

```lean
noncomputable def commRing (hf : IsSeparated B S hS f.hom) (hfin : IsFinite B S hS f.hom)
    (a : T ⟶ Y) : CommRing (FinitePartFibre B S hS f a)
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₃_eq_mul_one_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L349). The attribute's comment: “star\_3\_is\_s\_times\_one\_plus\_s\_prime”.

> **Stacks 04PI, the finite case.** `⋆₃(s, s') = s (1 + s')`.

```lean
theorem star₃_eq_mul_one_add (hf : IsSeparated B S hS f.hom) (hfin : IsFinite B S hS f.hom)
    {a : T ⟶ Y} (Z₁ Z₂ : FinitePartFibre B S hS f a) :
    letI := commRing hf hfin a
    star₃ hf Z₁ Z₂ = Z₁ * (1 + Z₂)
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₄_eq_one_add_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/F2Algebra.lean#L357). The attribute's comment: “star\_4\_is\_one\_plus\_s\_times\_s\_prime”.

> **Stacks 04PI, the finite case.** `⋆₄(s, s') = (1 + s) s'`.

```lean
theorem star₄_eq_one_add_mul (hf : IsSeparated B S hS f.hom) (hfin : IsFinite B S hS f.hom)
    {a : T ⟶ Y} (Z₁ Z₂ : FinitePartFibre B S hS f a) :
    letI := commRing hf hfin a
    star₄ hf Z₁ Z₂ = (1 + Z₁) * Z₂
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L302). The attribute's comment: “star\_2\_on\_sections”.

> **Stacks 04PI, the operation `⋆₂`.** The intersection `(a, Z₁ ∩ Z₂)` of two sections of
> the finite part lying over the same morphism to `Y`.

```lean
def star₂ : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₃`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L311). The attribute's comment: “star\_3\_on\_sections”.

> **Stacks 04PI, the operation `⋆₃`.** The difference `(a, Z₁ ∖ Z₂)` of two sections of the
> finite part lying over the same morphism to `Y`.

```lean
def star₃ : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₄`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L320). The attribute's comment: “star\_4\_on\_sections”.

> **Stacks 04PI, the operation `⋆₄`.** The difference `(a, Z₂ ∖ Z₁)` of two sections of the
> finite part lying over the same morphism to `Y`.

```lean
def star₄ : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.pointSet_star₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L329). The attribute's comment: “star\_2\_on\_points”.

> **Stacks 04PI, the operation `⋆₂`.** On points, `⋆₂(s, s')` is the intersection
> `Z₁ ∩ Z₂`.

```lean
theorem pointSet_star₂ : (star₂ hf Z₁ Z₂).pointSet = Z₁.pointSet ∩ Z₂.pointSet
```

**`AlgebraicGeometry.Space.FinitePartFibre.pointSet_star₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L335). The attribute's comment: “star\_3\_on\_points”.

> **Stacks 04PI, the operation `⋆₃`.** On points, `⋆₃(s, s')` is the difference
> `Z₁ ∖ Z₂`.

```lean
theorem pointSet_star₃ : (star₃ hf Z₁ Z₂).pointSet = Z₁.pointSet \ Z₂.pointSet
```

**`AlgebraicGeometry.Space.FinitePartFibre.pointSet_star₄`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L341). The attribute's comment: “star\_4\_on\_points”.

> **Stacks 04PI, the operation `⋆₄`.** On points, `⋆₄(s, s')` is the difference
> `Z₂ ∖ Z₁`.

```lean
theorem pointSet_star₄ : (star₄ hf Z₁ Z₂).pointSet = Z₂.pointSet \ Z₁.pointSet
```

**`AlgebraicGeometry.Space.FinitePartFibre.isOpenImmersion_star₂_le_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L354). The attribute's comment: “intersection\_open\_in\_left”.

> **Stacks 04PI.** `Z₁ ∩ Z₂` is open inside `Z₁`.

```lean
theorem isOpenImmersion_star₂_le_left :
    IsOpenImmersion B S hS (Subfunctor.homOfLe (star₂_le_left hf Z₁ Z₂))
```

**`AlgebraicGeometry.Space.FinitePartFibre.isClosedImmersion_star₂_le_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L360). The attribute's comment: “intersection\_closed\_in\_left”.

> **Stacks 04PI.** `Z₁ ∩ Z₂` is closed inside `Z₁`.

```lean
theorem isClosedImmersion_star₂_le_left :
    IsClosedImmersion B S hS (Subfunctor.homOfLe (star₂_le_left hf Z₁ Z₂))
```

**`AlgebraicGeometry.Space.FinitePartFibre.isOpenImmersion_star₂_le_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L366). The attribute's comment: “intersection\_open\_in\_right”.

> **Stacks 04PI.** `Z₁ ∩ Z₂` is open inside `Z₂`.

```lean
theorem isOpenImmersion_star₂_le_right :
    IsOpenImmersion B S hS (Subfunctor.homOfLe (star₂_le_right hf Z₁ Z₂))
```

**`AlgebraicGeometry.Space.FinitePartFibre.isClosedImmersion_star₂_le_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L372). The attribute's comment: “intersection\_closed\_in\_right”.

> **Stacks 04PI.** `Z₁ ∩ Z₂` is closed inside `Z₂`.

```lean
theorem isClosedImmersion_star₂_le_right :
    IsClosedImmersion B S hS (Subfunctor.homOfLe (star₂_le_right hf Z₁ Z₂))
```

**`AlgebraicGeometry.Space.FinitePartFibre.zero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L379). The attribute's comment: “zero\_of\_the\_f2\_algebra”.

> **Stacks 04PI.** The zero section `0 = (a, ∅)` of the `F₂`-algebra: the empty open
> subspace, which is finite over `T`.

```lean
def zero : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.subspace_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L393). The attribute's comment: “zero\_is\_the\_empty\_subspace”.

> **Stacks 04PI.** The open subspace of the zero section is the empty one, so `0 = (a, ∅)`.
>
> The empty open subspace of an algebraic space is the sheafification of the bottom subfunctor
> and not the bottom subfunctor itself, whose sections over an object of the site with no points
> are not those of a sheaf.

```lean
theorem subspace_zero : (zero Z₁).subspace =
    (⊥ : Subfunctor (pullback a.hom f.hom)).sheafify (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Space.FinitePartFibre.one`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L405). The attribute's comment: “unit\_of\_finite”.

> **Stacks 04PI, the unit of the finite case.** When `f` is finite the section
> `1 = (a, T ×_Y X)` cut out by all of the points of `T ×_Y X`, which is the restriction along
> `a` of the pair `(1_Y, X)`.

```lean
def one (hfin : IsFinite B S hS f.hom) : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.subspace_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L418). The attribute's comment: “unit\_is\_the\_whole\_fibre\_product”.

> **Stacks 04PI, the unit of the finite case.** The open subspace of the unit is the whole
> of `T ×_Y X`, so `1` is the restriction along `a` of the pair `(1_Y, X)`.

```lean
theorem subspace_one (hfin : IsFinite B S hS f.hom) :
    (one (a := a) hfin).subspace = ⊤
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₂_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L424). The attribute's comment: “unit\_of\_finite\_is\_unit”.

> **Stacks 04PI, the unit of the finite case.** `1 s = s`.

```lean
theorem star₂_one (hfin : IsFinite B S hS f.hom) : star₂ hf (one hfin) Z₁ = Z₁
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₂_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L433). The attribute's comment: “multiplication\_is\_commutative”.

> **Stacks 04PI.** The multiplication `s s' = ⋆₂(s, s')` is commutative.

```lean
theorem star₂_comm : star₂ hf Z₁ Z₂ = star₂ hf Z₂ Z₁
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₂_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Operations.lean#L438). The attribute's comment: “multiplication\_is\_associative”.

> **Stacks 04PI.** The multiplication `s s' = ⋆₂(s, s')` is associative.

```lean
theorem star₂_assoc (Z₃ : FinitePartFibre B S hS f a) :
    star₂ hf (star₂ hf Z₁ Z₂) Z₃ = star₂ hf Z₁ (star₂ hf Z₂ Z₃)
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.existsUnique_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Presheaf.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Presheaf.lean#L86). The attribute's comment: “projection\_to\_base”.

> **Stacks 04PI.** The component rule sending a finite open pair to its morphism to `Y`
> determines a unique morphism of presheaves to `Y`, namely the projection
> `FinitePartPresheaf.baseMap`.

```lean
theorem existsUnique_projection (P : FinitePartPresheaf B S hS f) :
    ∃! π : P.toFunctor ⟶ Y.obj,
      ∀ T (p : P.toFunctor.obj (op T)),
        yonedaEquiv.symm (π.app (op T) p) = (P.sections T p).toBase.hom
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₁Map`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L260). The attribute's comment: “star\_1\_as\_a\_morphism\_of\_sheaves”.

> **Stacks 04PI, the operation `⋆₁`.** The morphism of presheaves
> `⋆₁ : (X/Y)_fin ×_Y (X/Y)_fin ⟶ (X/Y)_fin` sending a pair of sections over a common morphism
> to `Y` to the union `Z₁ ∪ Z₂`.

```lean
def star₁Map : Limits.pullback P.baseMap P.baseMap ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_star₁Map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L266). The attribute's comment: “star\_1\_morphism\_on\_sections”.

> **Stacks 04PI, the operation `⋆₁`.** On sections, `⋆₁` is the union `Z₁ ∪ Z₂`.

```lean
theorem sections_star₁Map (T : BigFppfOver B S hS)
    (z : (Limits.pullback P.baseMap P.baseMap).obj (op T)) :
    P.sections T ((star₁Map P hf).app (op T) z) =
      (FinitePartFibre.star₁ hf (FinitePartFibre.ofPair rfl)
        (FinitePartFibre.ofPair (P.sections_snd_toBase_eq_fst T z))).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₁Map_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L275). The attribute's comment: “star\_1\_is\_a\_morphism\_over\_the\_base”.

> **Stacks 04PI, the operation `⋆₁`.** It is a morphism over `Y`.

```lean
theorem star₁Map_comp_baseMap :
    star₁Map P hf ≫ P.baseMap = Limits.pullback.fst P.baseMap P.baseMap ≫ P.baseMap
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₂Map`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L283). The attribute's comment: “star\_2\_as\_a\_morphism\_of\_sheaves”.

> **Stacks 04PI, the operation `⋆₂`.** The morphism of presheaves
> `⋆₂ : (X/Y)_fin ×_Y (X/Y)_fin ⟶ (X/Y)_fin` sending a pair of sections over a common morphism
> to `Y` to the intersection `Z₁ ∩ Z₂`.

```lean
def star₂Map : Limits.pullback P.baseMap P.baseMap ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_star₂Map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L289). The attribute's comment: “star\_2\_morphism\_on\_sections”.

> **Stacks 04PI, the operation `⋆₂`.** On sections, `⋆₂` is the intersection `Z₁ ∩ Z₂`.

```lean
theorem sections_star₂Map (T : BigFppfOver B S hS)
    (z : (Limits.pullback P.baseMap P.baseMap).obj (op T)) :
    P.sections T ((star₂Map P hf).app (op T) z) =
      (FinitePartFibre.star₂ hf (FinitePartFibre.ofPair rfl)
        (FinitePartFibre.ofPair (P.sections_snd_toBase_eq_fst T z))).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₂Map_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L298). The attribute's comment: “star\_2\_is\_a\_morphism\_over\_the\_base”.

> **Stacks 04PI, the operation `⋆₂`.** It is a morphism over `Y`.

```lean
theorem star₂Map_comp_baseMap :
    star₂Map P hf ≫ P.baseMap = Limits.pullback.fst P.baseMap P.baseMap ≫ P.baseMap
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₃Map`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L306). The attribute's comment: “star\_3\_as\_a\_morphism\_of\_sheaves”.

> **Stacks 04PI, the operation `⋆₃`.** The morphism of presheaves
> `⋆₃ : (X/Y)_fin ×_Y (X/Y)_fin ⟶ (X/Y)_fin` sending a pair of sections over a common morphism
> to `Y` to the difference `Z₁ ∖ Z₂`.

```lean
def star₃Map : Limits.pullback P.baseMap P.baseMap ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_star₃Map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L312). The attribute's comment: “star\_3\_morphism\_on\_sections”.

> **Stacks 04PI, the operation `⋆₃`.** On sections, `⋆₃` is the difference `Z₁ ∖ Z₂`.

```lean
theorem sections_star₃Map (T : BigFppfOver B S hS)
    (z : (Limits.pullback P.baseMap P.baseMap).obj (op T)) :
    P.sections T ((star₃Map P hf).app (op T) z) =
      (FinitePartFibre.star₃ hf (FinitePartFibre.ofPair rfl)
        (FinitePartFibre.ofPair (P.sections_snd_toBase_eq_fst T z))).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₃Map_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L321). The attribute's comment: “star\_3\_is\_a\_morphism\_over\_the\_base”.

> **Stacks 04PI, the operation `⋆₃`.** It is a morphism over `Y`.

```lean
theorem star₃Map_comp_baseMap :
    star₃Map P hf ≫ P.baseMap = Limits.pullback.fst P.baseMap P.baseMap ≫ P.baseMap
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₄Map`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L329). The attribute's comment: “star\_4\_as\_a\_morphism\_of\_sheaves”.

> **Stacks 04PI, the operation `⋆₄`.** The morphism of presheaves
> `⋆₄ : (X/Y)_fin ×_Y (X/Y)_fin ⟶ (X/Y)_fin` sending a pair of sections over a common morphism
> to `Y` to the difference `Z₂ ∖ Z₁`.

```lean
def star₄Map : Limits.pullback P.baseMap P.baseMap ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_star₄Map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L335). The attribute's comment: “star\_4\_morphism\_on\_sections”.

> **Stacks 04PI, the operation `⋆₄`.** On sections, `⋆₄` is the difference `Z₂ ∖ Z₁`.

```lean
theorem sections_star₄Map (T : BigFppfOver B S hS)
    (z : (Limits.pullback P.baseMap P.baseMap).obj (op T)) :
    P.sections T ((star₄Map P hf).app (op T) z) =
      (FinitePartFibre.star₄ hf (FinitePartFibre.ofPair rfl)
        (FinitePartFibre.ofPair (P.sections_snd_toBase_eq_fst T z))).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.star₄Map_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L344). The attribute's comment: “star\_4\_is\_a\_morphism\_over\_the\_base”.

> **Stacks 04PI, the operation `⋆₄`.** It is a morphism over `Y`.

```lean
theorem star₄Map_comp_baseMap :
    star₄Map P hf ≫ P.baseMap = Limits.pullback.fst P.baseMap P.baseMap ≫ P.baseMap
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.addMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L351). The attribute's comment: “addition\_as\_a\_morphism\_of\_sheaves”.

> **Stacks 04PI.** The addition of the `F₂`-algebra as a morphism of presheaves
> `(X/Y)_fin ×_Y (X/Y)_fin ⟶ (X/Y)_fin`.

```lean
def addMap : Limits.pullback P.baseMap P.baseMap ⟶ P.toFunctor
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.sections_addMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L357). The attribute's comment: “addition\_morphism\_on\_sections”.

> **Stacks 04PI.** On sections, the addition is `⋆₁(⋆₃(s, s'), ⋆₄(s, s'))`.

```lean
theorem sections_addMap (T : BigFppfOver B S hS)
    (z : (Limits.pullback P.baseMap P.baseMap).obj (op T)) :
    P.sections T ((addMap P hf).app (op T) z) =
      (FinitePartFibre.add hf (FinitePartFibre.ofPair rfl)
        (FinitePartFibre.ofPair (P.sections_snd_toBase_eq_fst T z))).toPair
```

**`AlgebraicGeometry.Space.FinitePartPresheaf.addMap_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/PresheafOperations.lean#L366). The attribute's comment: “addition\_is\_a\_morphism\_over\_the\_base”.

> **Stacks 04PI.** The addition of the `F₂`-algebra is a morphism over `Y`.

```lean
theorem addMap_comp_baseMap :
    addMap P hf ≫ P.baseMap = Limits.pullback.fst P.baseMap P.baseMap ≫ P.baseMap
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_star₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L98). The attribute's comment: “star\_1\_commutes\_with\_restriction”.

> The operation `⋆₁`, the union of two sections, commutes with restriction along
> `T' ⟶ T`.

```lean
theorem restrict_star₁ : (star₁ hf Z₁ Z₂).restrict h = star₁ hf (Z₁.restrict h) (Z₂.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_star₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L104). The attribute's comment: “star\_2\_commutes\_with\_restriction”.

> The operation `⋆₂`, the intersection of two sections, commutes with restriction along
> `T' ⟶ T`.

```lean
theorem restrict_star₂ : (star₂ hf Z₁ Z₂).restrict h = star₂ hf (Z₁.restrict h) (Z₂.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_star₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L110). The attribute's comment: “star\_3\_commutes\_with\_restriction”.

> The operation `⋆₃`, the difference `Z₁ ∖ Z₂`, commutes with restriction along
> `T' ⟶ T`.

```lean
theorem restrict_star₃ : (star₃ hf Z₁ Z₂).restrict h = star₃ hf (Z₁.restrict h) (Z₂.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_star₄`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L116). The attribute's comment: “star\_4\_commutes\_with\_restriction”.

> The operation `⋆₄`, the difference `Z₂ ∖ Z₁`, commutes with restriction along
> `T' ⟶ T`.

```lean
theorem restrict_star₄ : (star₄ hf Z₁ Z₂).restrict h = star₄ hf (Z₁.restrict h) (Z₂.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L122). The attribute's comment: “addition\_commutes\_with\_restriction”.

> The addition of the `F₂`-algebra, the symmetric difference of two sections, commutes with
> restriction along `T' ⟶ T`.

```lean
theorem restrict_add : (add hf Z₁ Z₂).restrict h = add hf (Z₁.restrict h) (Z₂.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L127). The attribute's comment: “zero\_commutes\_with\_restriction”.

> The zero section restricts to the zero section.

```lean
theorem restrict_zero : (zero Z₁).restrict h = zero (Z₁.restrict h)
```

**`AlgebraicGeometry.Space.FinitePartFibre.restrict_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Restriction.lean#L132). The attribute's comment: “unit\_commutes\_with\_restriction”.

> For `f` finite, the unit section restricts to the unit section.

```lean
theorem restrict_one (hfin : IsFinite B S hS f.hom) :
    (one (a := a) hfin).restrict h = one (a := h ≫ a) hfin
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L284). The attribute's comment: “star\_1\_on\_sections”.

> **Stacks 04PI, the operation `⋆₁`.** The union `(a, Z₁ ∪ Z₂)` of two sections of the finite
> part lying over the same morphism to `Y`.
>
> Its projection to `T` is finite because `Z₁ ∪ Z₂` is the disjoint union of the open and closed
> pieces `Z₁` and `Z₂ ∖ Z₁`, hence their coproduct as a sheaf, and a morphism out of a finite
> coproduct whose restriction to each summand is finite is finite.

```lean
def star₁ : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.pointSet_star₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L315). The attribute's comment: “star\_1\_on\_points”.

> **Stacks 04PI, the operation `⋆₁`.** On points, `⋆₁(s, s')` is the union `Z₁ ∪ Z₂`.

```lean
theorem pointSet_star₁ : (star₁ hf Z₁ Z₂).pointSet = Z₁.pointSet ∪ Z₂.pointSet
```

**`AlgebraicGeometry.Space.FinitePartFibre.add`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L326). The attribute's comment: “addition\_of\_the\_f2\_algebra”.

> **Stacks 04PI, the addition of the `F₂`-algebra.** `s + s' = ⋆₁(⋆₃(s, s'), ⋆₄(s, s'))`.

```lean
def add : FinitePartFibre B S hS f a
```

**`AlgebraicGeometry.Space.FinitePartFibre.pointSet_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L331). The attribute's comment: “addition\_is\_the\_symmetric\_difference”.

> **Stacks 04PI.** The addition `s + s' = ⋆₁(⋆₃(s, s'), ⋆₄(s, s'))` of the `F₂`-algebra is
> the symmetric difference.

```lean
theorem pointSet_add : (add hf Z₁ Z₂).pointSet = Z₁.pointSet ∆ Z₂.pointSet
```

**`AlgebraicGeometry.Space.FinitePartFibre.add_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L337). The attribute's comment: “addition\_is\_commutative”.

> **Stacks 04PI.** The addition of the `F₂`-algebra is commutative.

```lean
theorem add_comm : add hf Z₁ Z₂ = add hf Z₂ Z₁
```

**`AlgebraicGeometry.Space.FinitePartFibre.add_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L342). The attribute's comment: “addition\_is\_associative”.

> **Stacks 04PI.** The addition of the `F₂`-algebra is associative.

```lean
theorem add_assoc (Z₃ : FinitePartFibre B S hS f a) :
    add hf (add hf Z₁ Z₂) Z₃ = add hf Z₁ (add hf Z₂ Z₃)
```

**`AlgebraicGeometry.Space.FinitePartFibre.add_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L348). The attribute's comment: “zero\_is\_neutral\_for\_addition”.

> **Stacks 04PI.** The zero section `0 = (a, ∅)` is neutral for the addition.

```lean
theorem add_zero : add hf Z₁ (zero Z₁) = Z₁
```

**`AlgebraicGeometry.Space.FinitePartFibre.add_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L363). The attribute's comment: “section\_plus\_itself\_is\_zero”.

> **Stacks 04PI.** `s + s = 0` for every local section: the algebra is an `F₂`-algebra, every
> section being its own additive inverse.

```lean
theorem add_self : add hf Z₁ Z₁ = zero Z₁
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₂_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L370). The attribute's comment: “multiplication\_distributes\_over\_addition”.

> **Stacks 04PI.** The multiplication `s s' = ⋆₂(s, s')` distributes over the addition.

```lean
theorem star₂_add (Z₃ : FinitePartFibre B S hS f a) :
    star₂ hf (add hf Z₁ Z₂) Z₃ = add hf (star₂ hf Z₁ Z₃) (star₂ hf Z₂ Z₃)
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₃_eq_star₂_one_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L386). The attribute's comment: “star\_3\_through\_the\_unit”.

> **Stacks 04PI, the finite case.** `⋆₃(s, s') = s (1 + s')`.

```lean
theorem star₃_eq_star₂_one_add (hfin : IsFinite B S hS f.hom) :
    star₃ hf Z₁ Z₂ = star₂ hf Z₁ (add hf (one hfin) Z₂)
```

**`AlgebraicGeometry.Space.FinitePartFibre.star₄_eq_star₂_one_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Union.lean#L392). The attribute's comment: “star\_4\_through\_the\_unit”.

> **Stacks 04PI, the finite case.** `⋆₄(s, s') = (1 + s) s'`.

```lean
theorem star₄_eq_star₂_one_add (hfin : IsFinite B S hS f.hom) :
    star₄ hf Z₁ Z₂ = star₂ hf (add hf (one hfin) Z₁) Z₂
```

## Tag 04PK, a lemma

[Tag 04PK](https://stacks.math.columbia.edu/tag/04PK) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenImmersion_diagonal_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Diagonal.lean, line 855](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Diagonal.lean#L855). The attribute's comment: “relative diagonal”.

> **Stacks 04PK, the relative diagonal.** For a morphism `f : X ⟶ Y` of algebraic spaces
> over `S`, the diagonal `(X/Y)_fin ⟶ (X/Y)_fin ×_Y (X/Y)_fin` is representable by schemes and
> an open immersion.

```lean
theorem isOpenImmersion_diagonal_finiteOpenSubspacePresheaf
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    IsOpenImmersion B S hS
      (pullback.diagonal (finiteOpenSubspacePresheaf B S hS f).baseMap)
```

**`AlgebraicGeometry.Space.relativelyRepresentable_diag_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Diagonal.lean, line 912](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Diagonal.lean#L912). The attribute's comment: “absolute diagonal”.

> **Stacks 04PK, the absolute diagonal.** For a morphism `f : X ⟶ Y` of algebraic spaces
> over `S`, the absolute diagonal `(X/Y)_fin ⟶ (X/Y)_fin × (X/Y)_fin` is representable by
> schemes: it is the relative diagonal followed by a base change of the diagonal of `Y`.

```lean
theorem relativelyRepresentable_diag_finiteOpenSubspacePresheaf
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    yoneda.relativelyRepresentable
      (diag (finiteOpenSubspacePresheaf B S hS f).toFunctor)
```

## Tag 04QE, a lemma

[Tag 04QE](https://stacks.math.columbia.edu/tag/04QE) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isEtale_comp_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/EtaleChart.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/EtaleChart.lean#L118).

> **Stacks 04QE.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and let `U` be
> a scheme of the big fppf site. A morphism from the presheaf represented by `U` to the finite
> part `(X/Y)_fin` — equivalently, a morphism `U ⟶ Y` together with an open subspace of
> `U ×_Y X` finite over `U` — is representable by schemes and étale as soon as its composite
> with the projection `(X/Y)_fin ⟶ Y` is.

```lean
theorem isEtale_of_isEtale_comp_baseMap
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (U : AlgebraicGeometry.BigFppfOver B S hS)
    (p : yoneda.obj U ⟶
      (finiteOpenSubspacePresheaf B S hS f).toFunctor)
    (hp : (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf
        (p ≫ (finiteOpenSubspacePresheaf B S hS f).baseMap)) :
    (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (AlgebraicGeometry.BigFppfOver.toScheme B S hS)).presheaf p
```

## Tag 04QF, a lemma

[Tag 04QF](https://stacks.math.columbia.edu/tag/04QF) in the Stacks Project.

**`AlgebraicGeometry.Space.FinitePartPresheaf.isPullback_mapOfPullbackSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/BaseChangeSquare.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/BaseChangeSquare.lean#L342).

> **Stacks 04QF.** Let `S` be a scheme and let a square `X' → X`, `X' → Y'`, `X → Y`,
> `Y' → Y` be a fibre product square of algebraic spaces over `S`. Then the square
> `(X'/Y')_fin → (X/Y)_fin`, `(X'/Y')_fin → Y'`, `(X/Y)_fin → Y`, `Y' → Y` is a fibre product
> square of sheaves on the big fppf site of `S`.

```lean
theorem isPullback_mapOfPullbackSquare (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X' X Y' Y : AlgebraicSpaces B S hS} (f' : X' ⟶ X) (g' : X' ⟶ Y')
    (f : X ⟶ Y) (g : Y' ⟶ Y) (h : IsPullback f' g' f g) (P : FinitePartPresheaf B S hS g')
    (Q : FinitePartPresheaf B S hS f) :
    IsPullback (mapOfPullbackSquare B S hS f' g' f g h P Q) P.baseMap Q.baseMap g.hom
```

## Tag 04QG, a lemma

[Tag 04QG](https://stacks.math.columbia.edu/tag/04QG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_surjective_etale_chart_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/EtaleCover/SurjectiveChart.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/EtaleCover/SurjectiveChart.lean#L683).

> The finite-part sheaf of a separated, locally quasi-finite morphism of
> algebraic spaces has a surjective étale scheme cover that is étale over the
> target.

```lean
theorem _root_.AlgebraicGeometry.Space.exists_surjective_etale_chart_finiteOpenSubspacePresheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf_sep : Space.IsSeparated B S hS f.hom)
    (hf_lqf : Space.IsLocallyQuasiFinite B S hS f.hom) :
    ∃ (U : BigFppfOver B S hS)
      (p : yoneda.obj U ⟶
        (Space.finiteOpenSubspacePresheaf B S hS f).toFunctor),
      (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf
          (p ≫ (Space.finiteOpenSubspacePresheaf B S hS f).baseMap) ∧
      (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf p ∧
      (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf p
```

## Tag 04QH, a proposition

[Tag 04QH](https://stacks.math.columbia.edu/tag/04QH) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/AlgebraicSpace.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/AlgebraicSpace.lean#L262). The attribute's comment: “(X/Y)\_fin is an algebraic space”.

> **Stacks 04QH, the first conclusion.** The finite part `(X/Y)_fin` of a separated morphism
> `f : X ⟶ Y` of algebraic spaces over `S` which is locally of finite type is an algebraic space
> over `S`.

```lean
theorem isAlgebraicSpace_finiteOpenSubspacePresheaf
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    IsAlgebraicSpace B S hS (finiteOpenSubspacePresheaf B S hS f).toFunctor
```

**`AlgebraicGeometry.Space.isEtale_baseMap_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/AlgebraicSpace.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/AlgebraicSpace.lean#L274). The attribute's comment: “(X/Y)\_fin → Y is étale”.

> **Stacks 04QH, the second conclusion.** The projection `(X/Y)_fin ⟶ Y` of the finite part
> of a separated morphism `f : X ⟶ Y` of algebraic spaces over `S` which is locally of finite
> type is étale.

```lean
theorem isEtale_baseMap_finiteOpenSubspacePresheaf
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    IsEtale B S hS (finiteOpenSubspacePresheaf B S hS f).baseMap
```

## Tag 04QI, a remark

[Tag 04QI](https://stacks.math.columbia.edu/tag/04QI) in the Stacks Project.

**`AlgebraicGeometry.chartInclusion_origin_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginNotSeparated.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginNotSeparated.lean#L54). The attribute's comment: “the example: the two chart origins are distinct points”.

> The two chart origins of affine space with doubled origin are distinct points of the glued
> scheme.

```lean
theorem chartInclusion_origin_ne (k : Type u) [Field k] (n : ℕ) :
    chartInclusion k n 0 (affineOrigin k n) ≠ chartInclusion k n 1 (affineOrigin k n)
```

**`AlgebraicGeometry.flat_locallyOfFinitePresentation_not_isSeparated_coordinateMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginNotSeparated.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginNotSeparated.lean#L122). The attribute's comment: “the example: flat and locally of finite presentation but not separated”.

> In positive dimension the coordinate morphism of affine space with doubled origin is flat and
> locally of finite presentation but not separated.

```lean
theorem flat_locallyOfFinitePresentation_not_isSeparated_coordinateMorphism
    (k : Type u) [Field k] (n : ℕ) (hn : 0 < n) :
    Flat (coordinateMorphism k n) ∧
      LocallyOfFinitePresentation (coordinateMorphism k n) ∧
      ¬ IsSeparated (coordinateMorphism k n)
```

**`AlgebraicGeometry.Space.doubledOrigin_finitePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/DoubledOriginNotAlgebraic/FourPoints.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/DoubledOriginNotAlgebraic/FourPoints.lean#L457). References: EGA I (5.5.11), “partial”.

> **Stacks Project, Tag 04QI.** The condition that `f` be separated cannot be dropped from
> Stacks 04QH. Let `X` be affine `n`-space over a field `k` with its origin doubled, `n > 0`
> (the remark takes `n = 1`, the affine line with zero doubled), `Y` affine `n`-space, and
> `f : X ⟶ Y` the coordinate morphism, read as a morphism of algebraic spaces over `Spec k` in a
> big fppf site containing `Spec k`. Then:
>
> 1. `f` is locally of finite type but not separated, so it satisfies every hypothesis of Stacks
>    04QH except separatedness;
> 2. over the origin of `Y` there are exactly two points `0₁ ≠ 0₂` of `X`, the chart origins, and
>    `(X/Y)_fin` has exactly four points over the origin, its sections over `Spec k` lying over the
>    origin, which correspond to the four subsets `∅`, `{0₁}`, `{0₂}`, `{0₁, 0₂}` of that fibre
>    (`AlgebraicGeometry.Space.exists_equiv_originPoints`);
> 3. of these, exactly the three subsets `∅`, `{0₁}`, `{0₂}` lift to an open subscheme of
>    `U ×_Y X` finite over `U` for an étale `U ⟶ Y`
>    (`AlgebraicGeometry.Space.IsEtaleLiftablePoint`, chart index `i` standing for the chart
>    origin `0ᵢ`);
> 4. hence `(X/Y)_fin`, if it is an algebraic space, is not étale over `Y`;
> 5. in fact `(X/Y)_fin` is not an algebraic space ("Details omitted" in the source).
>
> The second clause of (1) also follows from (5) and Stacks 04QH, which is how it is proved here;
> (4) is proved by the argument of the remark, independently of (5).

```lean
theorem doubledOrigin_finitePart (hn : 0 < n) :
    (IsLocallyOfFiniteType B (Spec (.of k)) hk (schemeSpaceMap (doubledCoordHom B k hk n)).hom ∧
      ¬ IsSeparated B (Spec (.of k)) hk (schemeSpaceMap (doubledCoordHom B k hk n)).hom) ∧
    ((coordinateMorphism k n).base ⁻¹' {affineOrigin k n} =
        {chartInclusion k n 0 (affineOrigin k n), chartInclusion k n 1 (affineOrigin k n)} ∧
      chartInclusion k n 0 (affineOrigin k n) ≠ chartInclusion k n 1 (affineOrigin k n)) ∧
    (∃ e : originPoints (B := B) (k := k) (hk := hk) (n := n) ≃ Set (Fin 2),
      ∀ ξ, e ξ = chartIndices ((doubledOriginFinitePart B k hk n).sections _ ξ.1)) ∧
    Nat.card (originPoints (B := B) (k := k) (hk := hk) (n := n)) = 4 ∧
    {T : Set (Fin 2) | IsEtaleLiftablePoint B k hk n T} = {∅, {0}, {1}} ∧
    (IsAlgebraicSpace B (Spec (.of k)) hk (doubledOriginFinitePart B k hk n).toFunctor →
      ¬ IsEtale B (Spec (.of k)) hk (doubledOriginFinitePart B k hk n).baseMap) ∧
    ¬ IsAlgebraicSpace B (Spec (.of k)) hk (doubledOriginFinitePart B k hk n).toFunctor
```

## Tag 04RI, a lemma

[Tag 04RI](https://stacks.math.columbia.edu/tag/04RI) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_baseMap_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean#L773). The attribute's comment: “part (1): separatedness”.

> **Stacks 04RI, part (1).** For a separated, flat morphism `f : X ⟶ Y` of algebraic spaces
> over `S` which is locally of finite presentation, the projection `(X/Y)_fin ⟶ Y` from the
> finite part of `f` is separated.

```lean
theorem isSeparated_baseMap_finiteOpenSubspacePresheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom)
    (hflat : IsFlat B S hS f.hom)
    (hfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    IsSeparated B S hS (finiteOpenSubspacePresheaf B S hS f).baseMap
```

**`AlgebraicGeometry.Space.isEtale_baseMap_finiteOpenSubspacePresheaf_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean, line 837](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean#L837). The attribute's comment: “part (1): étaleness”.

> For a separated, flat morphism `f : X ⟶ Y` of algebraic spaces over `S` which is locally of
> finite presentation, the projection `(X/Y)_fin ⟶ Y` from the finite part of `f` is étale: such
> a morphism is in particular locally of finite type.

```lean
theorem isEtale_baseMap_finiteOpenSubspacePresheaf_of_isFlat
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom)
    (_hflat : IsFlat B S hS f.hom)
    (hfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    IsEtale B S hS (finiteOpenSubspacePresheaf B S hS f).baseMap
```

**`AlgebraicGeometry.Space.relativelyRepresentable_baseMap_finiteOpenSubspacePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean, line 853](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean#L853). The attribute's comment: “part (1): representability”.

> **Stacks 04RI, part (1).** For a separated, flat morphism `f : X ⟶ Y` of algebraic spaces
> over `S` which is locally of finite presentation, the projection `(X/Y)_fin ⟶ Y` from the finite
> part of `f` is representable: it is étale, hence locally quasi-finite, and separated.

```lean
theorem relativelyRepresentable_baseMap_finiteOpenSubspacePresheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom)
    (hflat : IsFlat B S hS f.hom)
    (hfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    yoneda.relativelyRepresentable (finiteOpenSubspacePresheaf B S hS f).baseMap
```

**`AlgebraicGeometry.Space.isRepresentable_finiteOpenSubspacePresheaf_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean, line 871](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/SeparatedRepresentable.lean#L871). The attribute's comment: “part (2): the finite part over a scheme is a scheme”.

> **Stacks 04RI, part (2).** If moreover `Y` is a scheme, then the finite part `(X/Y)_fin` of
> a separated, flat morphism locally of finite presentation is a scheme: it is separated and
> locally quasi-finite over the representable `Y`, so Stacks 03XX applies.

```lean
theorem isRepresentable_finiteOpenSubspacePresheaf_of_isRepresentable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsep : IsSeparated B S hS f.hom)
    (hflat : IsFlat B S hS f.hom)
    (hfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (hY : Y.obj.IsRepresentable) :
    (finiteOpenSubspacePresheaf B S hS f).toFunctor.IsRepresentable
```

## Tag 04RQ, an equation

[Tag 04RQ](https://stacks.math.columbia.edu/tag/04RQ) in the Stacks Project.

**`AlgebraicGeometry.Space.FiniteOpenPairWithSection`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Basic.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Basic.lean#L71).

> **Stacks 04RQ.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` with a section
> `σ`, and an algebraic space `T`, a morphism `a : T ⟶ Y` together with an open subspace `Z` of
> `T ×_Y X` which is finite over `T` and contains the section of `T ×_Y X` over `T` induced
> by `σ`.

```lean
structure FiniteOpenPairWithSection (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X Y T : AlgebraicSpaces B S hS) (f : X ⟶ Y) (σ : Y ⟶ X)
    (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj)
```

## Tag 04RR, a lemma

[Tag 04RR](https://stacks.math.columbia.edu/tag/04RR) in the Stacks Project.

**`AlgebraicGeometry.Space.finitePartWithSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean#L220). The attribute's comment: “the transformation”.

> The canonical transformation from finite open pairs containing a section
> to all finite open pairs, with its pointwise characterization.

```lean
public noncomputable def finitePartWithSection
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (σ : Y ⟶ X) (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj) :
    FinitePartWithSection B S hS f σ hσ
```

**`AlgebraicGeometry.Space.isOpenImmersion_finitePartWithSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean#L316). The attribute's comment: “part (1)”.

> The transformation is representable by open immersions.

```lean
public theorem isOpenImmersion_finitePartWithSection
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (σ : Y ⟶ X) (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj) :
    Space.IsOpenImmersion B S hS
      (finitePartWithSection B S hS f σ hσ).toSubfunctor.ι
```

**`AlgebraicGeometry.Space.isClosedImmersion_finitePartWithSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean#L331). The attribute's comment: “part (2)”.

> For separated `f`, the same transformation is representable by closed
> immersions as well as open immersions.

```lean
public theorem isClosedImmersion_finitePartWithSection
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (σ : Y ⟶ X) (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj)
    (hf : Space.IsSeparated B S hS f.hom) :
    Space.IsClosedImmersion B S hS
      (finitePartWithSection B S hS f σ hσ).toSubfunctor.ι
```

**`AlgebraicGeometry.Space.isOpenSubspace_finitePartWithSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean#L351). The attribute's comment: “part (3)”.

> If the finite-part functor is an algebraic space, the section-containing
> subfunctor is an open algebraic subspace of it.

```lean
public theorem isOpenSubspace_finitePartWithSection
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (σ : Y ⟶ X) (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj)
    (hfin : AlgebraicGeometry.IsAlgebraicSpace B S hS
      (Space.finiteOpenSubspacePresheaf B S hS f).toFunctor) :
    Space.IsOpenSubspace B S hS
      (finitePartWithSection B S hS f σ hσ).toSubfunctor
```

**`AlgebraicGeometry.Space.openSubscheme_finitePartWithSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/WithSection.lean#L366). The attribute's comment: “part (4)”.

> A scheme representing the finite-part functor contains the
> section-containing functor as a compatible open subscheme.

```lean
public theorem openSubscheme_finitePartWithSection
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicGeometry.AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (σ : Y ⟶ X) (hσ : σ.hom ≫ f.hom = 𝟙 Y.obj)
    (V : AlgebraicGeometry.BigFppfOver B S hS)
    (e : yoneda.obj V ≅
      (Space.finiteOpenSubspacePresheaf B S hS f).toFunctor) :
    ∃ (U : AlgebraicGeometry.BigFppfOver B S hS) (i : U ⟶ V)
      (e' : yoneda.obj U ≅
        (finitePartWithSection B S hS f σ hσ).toSubfunctor.toFunctor),
      AlgebraicGeometry.IsOpenImmersion
        ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).map i) ∧
      yoneda.map i ≫ e.hom =
        e'.hom ≫ (finitePartWithSection B S hS f σ hσ).toSubfunctor.ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.12, Tag 04PB](https://stacks.math.columbia.edu/tag/04PB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
