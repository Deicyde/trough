---
declaration: section
origin: cited
lean: AlgebraicGeometry.OneStepDevissage, AlgebraicGeometry.OneStepDevissageAt, AlgebraicGeometry.exists_etaleNeighborhood_oneStepDevissageAt, AlgebraicGeometry.exists_etaleNeighborhood_oneStepDevissageAt_iff_mem_fiber_supp, AlgebraicGeometry.OneStepDevissage.baseChange, AlgebraicGeometry.OneStepDevissageAt.exists_baseChange, AlgebraicGeometry.OneStepDevissageAt.exists_baseChange_of_affine, AlgebraicGeometry.OneStepDevissageAt.StandardShrinking
statement: formalized
proof: formalized
---

# 38.4 One step dévissage

Section 38.4 of the Stacks Project, [Tag 05H3](https://stacks.math.columbia.edu/tag/05H3). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05H4, a definition

[Tag 05H4](https://stacks.math.columbia.edu/tag/05H4) in the Stacks Project.

**`AlgebraicGeometry.OneStepDevissage`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean#L77).

> A one-step dévissage of `F/X/S` over `s`.

```lean
structure OneStepDevissage {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (s : S)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
```

## Tag 05H5, a definition

[Tag 05H5](https://stacks.math.columbia.edu/tag/05H5) in the Stacks Project.

**`AlgebraicGeometry.OneStepDevissageAt`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean#L110).

> A one-step dévissage of `F/X/S` at `x`.

```lean
structure OneStepDevissageAt {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
```

## Tag 05H6, a lemma

[Tag 05H6](https://stacks.math.columbia.edu/tag/05H6) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_oneStepDevissageAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/EtaleNeighborhoodOneStep.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/EtaleNeighborhoodOneStep.lean#L267).

> **Stacks Project, Tag 05H6.** A finite-type quasi-coherent module supported at a point of a
> fibre admits a one-step dévissage there after elementary étale neighbourhoods of the point and
> of its image.

```lean
theorem exists_etaleNeighborhood_oneStepDevissageAt {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (x : X)
    (hx : f.asFiber x ∈
      SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι (f x))).obj F)) :
    ∃ (U : EtaleNeighborhood X x) (V : EtaleNeighborhood S (f x)) (h : U.scheme ⟶ V.scheme),
      U.IsElementary ∧ V.IsElementary ∧ (U.toBase ≫ f = h ≫ V.toBase) ∧
        (h U.point = V.point) ∧
        ∃ (hft : LocallyOfFiniteType h)
          (hq : ((Scheme.Modules.pullback U.toBase).obj F).IsQuasicoherent)
          (hf : ((Scheme.Modules.pullback U.toBase).obj F).IsFiniteType),
          letI : LocallyOfFiniteType h := hft
          letI : ((Scheme.Modules.pullback U.toBase).obj F).IsQuasicoherent := hq
          letI : ((Scheme.Modules.pullback U.toBase).obj F).IsFiniteType := hf
          Nonempty (OneStepDevissageAt h
            ((Scheme.Modules.pullback U.toBase).obj F) U.point)
```

**`AlgebraicGeometry.exists_etaleNeighborhood_oneStepDevissageAt_iff_mem_fiber_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/EtaleNeighborhoodOneStep.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/EtaleNeighborhoodOneStep.lean#L558).

> **Stacks Project, Tag 05H6**, in sharp form. The elementary étale neighbourhoods of `(X, x)`
> and of `(S, f x)` over which the pullback of `F` acquires a one-step dévissage at the
> distinguished point exist exactly when `x` lies in the support of the restriction of `F` to the
> fibre of `f` through `x`.
>
> The forward implication is the converse of the source's lemma; it holds because a one-step
> dévissage at a point records that the point lies in the support of the module on its fibre
> (`AlgebraicGeometry.OneStepDevissageAt.mem_supp`), and the support of the pullback of `F` to an
> étale neighbourhood is the inverse image of the support of `F`.

```lean
theorem exists_etaleNeighborhood_oneStepDevissageAt_iff_mem_fiber_supp {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (x : X) :
    (∃ (U : EtaleNeighborhood X x) (V : EtaleNeighborhood S (f x)) (h : U.scheme ⟶ V.scheme),
      U.IsElementary ∧ V.IsElementary ∧ (U.toBase ≫ f = h ≫ V.toBase) ∧
        (h U.point = V.point) ∧
        ∃ (hft : LocallyOfFiniteType h)
          (hq : ((Scheme.Modules.pullback U.toBase).obj F).IsQuasicoherent)
          (hf : ((Scheme.Modules.pullback U.toBase).obj F).IsFiniteType),
          letI : LocallyOfFiniteType h := hft
          letI : ((Scheme.Modules.pullback U.toBase).obj F).IsQuasicoherent := hq
          letI : ((Scheme.Modules.pullback U.toBase).obj F).IsFiniteType := hf
          Nonempty (OneStepDevissageAt h
            ((Scheme.Modules.pullback U.toBase).obj F) U.point)) ↔
      f.asFiber x ∈
        SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι (f x))).obj F)
```

## Tag 05H7, a lemma

[Tag 05H7](https://stacks.math.columbia.edu/tag/05H7) in the Stacks Project.

**`AlgebraicGeometry.OneStepDevissage.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChange.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChange.lean#L245).

> **Stacks Project, Tag 05H7.** A one-step dévissage and all its presenting data persist
> under base change to a pointed affine scheme.

```lean
def baseChange {X S S' : Scheme.{u}} (f : X ⟶ S) (F : X.Modules)
    (s : S) (s' : S') (h : S' ⟶ S) (hs : h s' = s)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType] [IsAffine S']
    (D : OneStepDevissage f F s) :
    BaseChangeData f F s s' h hs D
```

## Tag 05H8, a lemma

[Tag 05H8](https://stacks.math.columbia.edu/tag/05H8) in the Stacks Project.

**`AlgebraicGeometry.OneStepDevissageAt.exists_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChangeAt.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChangeAt.lean#L481).

> **Stacks Project, Tag 05H8.** A one-step dévissage at a point survives an affine pointed
> base change which induces an isomorphism of residue fields: for the unique points `x'`, `z'`,
> `y'` of the base-changed schemes lying over the original distinguished points and over the new
> base point, the base-changed dévissage is a one-step dévissage at `x'` with distinguished
> points `z'` and `y'`.

```lean
theorem exists_baseChange {X S S' : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : OneStepDevissageAt f F x)
    (s' : S') (h : S' ⟶ S) (hs : h s' = f x) [IsAffine S']
    [IsIso ((S.residueFieldCongr hs).inv ≫ h.residueFieldMap s')]
    (B : OneStepDevissage.BaseChangeData f F (f x) s' h hs D.toOneStepDevissage) :
    letI := B.locallyOfFiniteType
    letI := B.quasicoherent
    letI := B.finiteType
    ∀ (x' : ↥(pullback f h)) (_ : pullback.fst f h x' = x)
      (_ : pullback.snd f h x' = s') (z' : B.devissage.Z) (_ : B.pZ z' = D.z)
      (_ : (B.devissage.π ≫ B.devissage.g) z' = s') (y' : B.devissage.Y)
      (_ : B.pY y' = D.y) (_ : B.devissage.g y' = s'),
      ∃ E : OneStepDevissageAt (pullback.snd f h)
          ((Scheme.Modules.pullback (pullback.fst f h)).obj F) x',
        HEq E.toOneStepDevissage B.devissage ∧ HEq E.z z' ∧ HEq E.y y'
```

**`AlgebraicGeometry.OneStepDevissageAt.exists_baseChange_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChangeAtPoints.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/BaseChangeAtPoints.lean#L130).

> **Stacks Project, Tag 05H8.** A one-step dévissage at a point survives an affine pointed
> base change which induces an isomorphism of residue fields: the base change of the dévissage
> constructed in `AlgebraicGeometry.OneStepDevissage.baseChange` is a one-step dévissage at the
> unique point `x'` of the base-changed source lying over `x` and over the new base point, with
> distinguished points the unique points `z'` and `y'` of the base-changed closed subscheme and
> smooth scheme lying over `z` and `y` and over the new base point.

```lean
theorem exists_baseChange_of_affine {X S S' : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : OneStepDevissageAt f F x)
    (s' : S') (h : S' ⟶ S) (hs : h s' = f x) [IsAffine S']
    [IsIso ((S.residueFieldCongr hs).inv ≫ h.residueFieldMap s')] :
    let B := OneStepDevissage.baseChange f F (f x) s' h hs D.toOneStepDevissage
    letI := B.locallyOfFiniteType
    letI := B.quasicoherent
    letI := B.finiteType
    ∃ (x' : ↥(pullback f h)) (z' : B.devissage.Z) (y' : B.devissage.Y)
      (E : OneStepDevissageAt (pullback.snd f h)
        ((Scheme.Modules.pullback (pullback.fst f h)).obj F) x'),
      ((pullback.fst f h x' = x ∧ pullback.snd f h x' = s') ∧
        ∀ w : ↥(pullback f h), pullback.fst f h w = x → pullback.snd f h w = s' → w = x') ∧
      ((B.pZ z' = D.z ∧ (B.devissage.π ≫ B.devissage.g) z' = s') ∧
        ∀ w : B.devissage.Z, B.pZ w = D.z →
          (B.devissage.π ≫ B.devissage.g) w = s' → w = z') ∧
      ((B.pY y' = D.y ∧ B.devissage.g y' = s') ∧
        ∀ w : B.devissage.Y, B.pY w = D.y → B.devissage.g w = s' → w = y') ∧
      HEq E.toOneStepDevissage B.devissage ∧ HEq E.z z' ∧ HEq E.y y'
```

## Tag 05H9, a definition

[Tag 05H9](https://stacks.math.columbia.edu/tag/05H9) in the Stacks Project.

**`AlgebraicGeometry.OneStepDevissageAt.StandardShrinking`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep.lean#L145).

> A standard shrinking of a one-step dévissage at `x`.

```lean
structure StandardShrinking {X S : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) (x : X) [LocallyOfFiniteType f]
    [F.IsQuasicoherent] [F.IsFiniteType]
    (D : OneStepDevissageAt f F x)
```

## Tag 05HA, a lemma

[Tag 05HA](https://stacks.math.columbia.edu/tag/05HA) in the Stacks Project.

**`AlgebraicGeometry.exists_standardShrinking_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean#L470). The attribute's comment: “part (1)”.

> **Stacks Tag 05HA, part (1).** Restricting a one-step dévissage at `x` to a principal open
> neighbourhood `V` of `f x` in the base is a standard shrinking, whose other three opens are the
> inverse images of `V`.

```lean
theorem exists_standardShrinking_base {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType] (D : OneStepDevissageAt f F x)
    (V : S.Opens) (a : Γ(S, ⊤)) (hV : V = S.basicOpen a) (hs : f x ∈ V) :
    ∃ E : D.StandardShrinking, E.S' = V ∧ E.X' = f ⁻¹ᵁ V ∧
      E.Z' = (D.toOneStepDevissage.i ≫ f) ⁻¹ᵁ V ∧ E.Y' = D.toOneStepDevissage.g ⁻¹ᵁ V
```

**`AlgebraicGeometry.exists_standardShrinking_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean#L495). The attribute's comment: “part (2)”.

> **Stacks Tag 05HA, part (2).** Given a principal open neighbourhood `W` of the distinguished
> point `y` of the smooth scheme, there is a standard shrinking whose smooth open is `W` cut down
> to the inverse image of the new base.

```lean
theorem exists_standardShrinking_smooth {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType] (D : OneStepDevissageAt f F x)
    (W : D.toOneStepDevissage.Y.Opens) (a : Γ(D.toOneStepDevissage.Y, ⊤))
    (hW : W = D.toOneStepDevissage.Y.basicOpen a) (hy : D.y ∈ W) :
    ∃ E : D.StandardShrinking, E.Y' = W ⊓ (D.toOneStepDevissage.g ⁻¹ᵁ E.S')
```

**`AlgebraicGeometry.exists_standardShrinking_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/Shrinking.lean#L507). The attribute's comment: “part (3)”.

> **Stacks Tag 05HA, part (3).** Given any open neighbourhood `U` of `x`, there is a standard
> shrinking whose source open lies inside `U`.

```lean
theorem exists_standardShrinking_source {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType] (D : OneStepDevissageAt f F x)
    (U : X.Opens) (hx : x ∈ U) : ∃ E : D.StandardShrinking, E.X' ≤ U
```

## Tag 05HE, a lemma

[Tag 05HE](https://stacks.math.columbia.edu/tag/05HE) in the Stacks Project.

**`AlgebraicGeometry.exists_oneStepDevissageAt_of_etaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Glueing.lean, line 630](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Glueing.lean#L630).

> **Stacks Project, Tag 05HE.** A one-step dévissage at a point can be pulled through a
> compatible pair of elementary étale neighbourhoods of the base and of the smooth scheme, after a
> further elementary étale localization of the base: the new smooth scheme is an open subscheme of
> the base change of the given neighbourhood, the new closed subscheme is the base change of the
> old one, and the new module is the pullback of the old one.

```lean
theorem exists_oneStepDevissageAt_of_etaleNeighborhood
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : OneStepDevissageAt f F x)
    (U : EtaleNeighborhood S (f x)) (hU : U.IsElementary)
    (V : EtaleNeighborhood D.toOneStepDevissage.Y D.y)
    (hV : V.IsElementary) (h : V.scheme ⟶ U.scheme)
    (hcomm : V.toBase ≫ D.toOneStepDevissage.g = h ≫ U.toBase)
    (hpoint : h V.point = U.point) :
    ∃ (W : EtaleNeighborhood U.scheme U.point)
      (_ : W.IsElementary)
      (A : EtaleNeighborhood X x) (_ : A.IsElementary)
      (b : A.scheme ⟶ W.scheme),
      b A.point = W.point ∧
      A.toBase ≫ f = b ≫ W.toBase ≫ U.toBase ∧
      ∃ (hl : LocallyOfFiniteType b)
        (hq : ((Scheme.Modules.pullback A.toBase).obj F).IsQuasicoherent)
        (ht : ((Scheme.Modules.pullback A.toBase).obj F).IsFiniteType),
        letI := hl
        letI := hq
        letI := ht
        ∃ (D' : OneStepDevissageAt b ((Scheme.Modules.pullback A.toBase).obj F) A.point)
          (j : D'.toOneStepDevissage.Y ⟶ pullback h W.toBase)
          (p : D'.toOneStepDevissage.Z ⟶ D.toOneStepDevissage.Z),
          IsOpenImmersion j ∧
          D'.toOneStepDevissage.g = j ≫ pullback.snd h W.toBase ∧
          (j ≫ pullback.fst h W.toBase) D'.y = V.point ∧
          p D'.z = D.z ∧
          D'.toOneStepDevissage.i ≫ A.toBase =
            p ≫ D.toOneStepDevissage.i ∧
          IsPullback p D'.toOneStepDevissage.i D.toOneStepDevissage.i
            A.toBase ∧
          IsPullback p D'.toOneStepDevissage.π D.toOneStepDevissage.π
            (j ≫ pullback.fst h W.toBase ≫ V.toBase) ∧
          Nonempty (D'.toOneStepDevissage.G ≅
            (Scheme.Modules.pullback p).obj D.toOneStepDevissage.G)
```

## Tag 05HF, a lemma

[Tag 05HF](https://stacks.math.columbia.edu/tag/05HF) in the Stacks Project.

**`AlgebraicGeometry.exists_freeMap_isIso_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/FreeMap.lean, line 591](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/FreeMap.lean#L591). The attribute's comment: “existence of the generically invertible map”.

> **Stacks 05HF**, first assertion. For a one-step dévissage, a free `𝒪_Y`-module of positive
> finite rank maps to the direct image `π_* G` by a map that becomes an isomorphism over the
> residue field of the image in `Y` of a point of the fibre of `g` over `s`.

```lean
theorem exists_freeMap_isIso_genericFiber :
    ∃ (r : ℕ) (_ : 0 < r)
      (α : SheafOfModules.free (R := D.Y.ringCatSheaf) (ULift.{u} (Fin r)) ⟶
        (Scheme.Modules.pushforward D.π).obj D.G),
      IsIso ((Scheme.Modules.pullback
        (D.Y.fromSpecResidueField (D.g.fiberι s ξ))).map α)
```

**`AlgebraicGeometry.dim_support_cokernel_fiber_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/FreeMap.lean, line 644](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/OneStep/FreeMap.lean#L644). The attribute's comment: “dimension of the cokernel support”.

> **Stacks 05HF**, second assertion. If a map into the direct image `π_* G` of a one-step
> dévissage becomes an isomorphism over the residue field of the image in `Y` of a point of the
> fibre of `g` over `s`, then the fibre over `s` of the support of its cokernel has strictly
> smaller dimension than the fibre over `s` of the support of `F`.

```lean
theorem dim_support_cokernel_fiber_lt {P : D.Y.Modules}
    (α : P ⟶ (Scheme.Modules.pushforward D.π).obj D.G)
    (hα : IsIso ((Scheme.Modules.pullback
      (D.Y.fromSpecResidueField (D.g.fiberι s ξ))).map α)) :
    topologicalKrullDim
        (SheafOfModules.supp ((Scheme.Modules.pullback (D.g.fiberι s)).obj (cokernel α))) <
      topologicalKrullDim
        (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.4, Tag 05H3](https://stacks.math.columbia.edu/tag/05H3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
