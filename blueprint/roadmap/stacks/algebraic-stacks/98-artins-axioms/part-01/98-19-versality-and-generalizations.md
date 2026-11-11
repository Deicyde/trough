---
declaration: section
origin: cited
lean: Deformation.Artin.exists_firstOrderThickening_without_localRetraction, Deformation.Artin.isVersalAt_of_specializes
statement: formalized
proof: formalized
---

# 98.19 Versality and generalizations

Section 98.19 of the Stacks Project, [Tag 0G2I](https://stacks.math.columbia.edu/tag/0G2I). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G2J, a lemma

[Tag 0G2J](https://stacks.math.columbia.edu/tag/0G2J) in the Stacks Project.

**`Deformation.Artin.exists_firstOrderThickening_without_localRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/NonversalThickening/ThickeningWithoutRetraction.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/NonversalThickening/ThickeningWithoutRetraction.lean#L618).

> **Stacks 0G2J.** If an object `x` of a category fibred in groupoids with (RS*) over the big
> fppf site of a locally Noetherian scheme is not versal at a finite type point `u` of an affine
> scheme `U` of finite type, then `x` extends to an object `y` over a first order thickening
> `U ⟶ T` with ideal `κ(u)` which has no retraction to `x` over any open neighbourhood of `u`.

```lean
public theorem exists_firstOrderThickening_without_localRetraction
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : Type v} [Category.{w} F]
    (p : F ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (hRS : Deformation.Artin.SatisfiesRSStar B S hS p hp)
    (U : AlgebraicGeometry.BigFppfOver B S hS) (x : F)
    (hx : p.obj x = U)
    [IsAffine ((AlgebraicGeometry.BigFppfOver.toScheme B S hS).obj U)]
    [IsLocallyNoetherian S]
    [LocallyOfFiniteType ((Over.post B.inclusion).obj U).hom]
    (u₀ : ((Over.post B.inclusion).obj U).left)
    (_hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀)
    (hnot : ¬ Deformation.Artin.IsVersalAt
      ((Over.post B.inclusion).obj U) (p ⋙ Over.post B.inclusion)
      u₀ x (congrArg (Over.post B.inclusion).obj hx)) :
    ∃ (T : AlgebraicGeometry.BigFppfOver B S hS) (i : U ⟶ T)
      (y : F) (hy : p.obj y = T) (r : x ⟶ y),
      let V := AlgebraicGeometry.BigFppfOver.toScheme B S hS
      let iS := V.map i
      (p.map r = eqToHom hx ≫ i ≫ eqToHom hy.symm) ∧
      Stacks.Thickenings.IsFirstOrderThickening iS ∧
      Epi (SheafOfModules.unitToPushforwardObjUnit iS.toRingCatSheafHom) ∧
      Nonempty (kernel (SheafOfModules.unitToPushforwardObjUnit
        iS.toRingCatSheafHom) ≅
        (Scheme.Modules.pushforward ((V.obj T).fromSpecResidueField (iS u₀))).obj
          (SheafOfModules.unit
            (Spec ((V.obj T).residueField (iS u₀))).ringCatSheaf)) ∧
      (∀ (W : AlgebraicGeometry.BigFppfOver B S hS) (j : W ⟶ T)
          (w₀ : V.obj W) (_ : V.map j w₀ = iS u₀)
          (_ : IsOpenImmersion (V.map j))
          (z : F) (hz : p.obj z = W) (s : z ⟶ y)
          (_ : p.map s = eqToHom hz ≫ j ≫ eqToHom hy.symm)
          (_ : p.IsCartesian (p.map s) s),
        ¬ ∃ (β : z ⟶ x) (x' : F) (a : x' ⟶ x) (b : x' ⟶ z),
          p.IsCartesian (p.map a) a ∧
          p.IsCartesian (p.map b) b ∧
          IsPullback
            (V.map (p.map a ≫ eqToHom hx))
            (V.map (p.map b ≫ eqToHom hz)) iS (V.map j) ∧
          a ≫ r = b ≫ s ∧ b ≫ β = a)
```

## Tag 0G2K, a lemma

[Tag 0G2K](https://stacks.math.columbia.edu/tag/0G2K) in the Stacks Project.

**`Deformation.Artin.isVersalAt_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessAtGeneralization.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessAtGeneralization.lean#L736).

> **Stacks 0G2K.** Let `S` be a locally Noetherian scheme and `𝒳` a category fibred in
> groupoids over the big fppf site of `S` whose diagonal is representable by algebraic spaces,
> which satisfies (RS*) and which is limit preserving. Let `x` be an object of `𝒳` over a scheme
> `U` locally of finite type over `S`, and let `u ⤳ u₀` be a specialization of points of `U` with
> `u₀` of finite type. If `x` is versal at `u₀`, then `x` is versal at `u`.
>
> The source asks `U` to be of finite type over `S` and `u` to be a finite type point; neither is
> used.

```lean
public theorem isVersalAt_of_specializes [IsLocallyNoetherian S]
    (hΔ : AlgebraicGeometry.Stack.HasRepresentableDiagonal B S hS 𝒳)
    (hRS : SatisfiesRSStar B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (hlim : IsLimitPreserving.{u, u, u, w, v} B S hS 𝒳)
    (x : 𝒳.val.obj) [LocallyOfFiniteType ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).hom]
    (u u₀ : ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).left)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀) (hspec : u ⤳ u₀)
    (hversal : IsVersalAt ((𝒳.val.p ⋙ Over.post B.inclusion).obj x)
      (𝒳.val.p ⋙ Over.post B.inclusion) u₀ x rfl) :
    IsVersalAt ((𝒳.val.p ⋙ Over.post B.inclusion).obj x)
      (𝒳.val.p ⋙ Over.post B.inclusion) u x rfl
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.19, Tag 0G2I](https://stacks.math.columbia.edu/tag/0G2I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
