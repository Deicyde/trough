---
declaration: section
origin: cited
lean: Deformation.Artin.locallyOfFiniteType_and_quasiCompact_of_isPullback_appTop, Deformation.Artin.isPushout_of_isPullback_appTop, Deformation.Artin.satisfiesRS_of_satisfiesRSStar, Deformation.Artin.isDeformationCategory_predeformationCategory_of_satisfiesRSStar, Deformation.Artin.SatisfiesRSStar, Deformation.Artin.satisfiesRSStar_of_isAlgebraicStack, Deformation.Artin.twoFibreProductOver_satisfiesRSStar
statement: formalized
proof: formalized
---

# 98.18 Strong Rim-Schlessinger

Section 98.18 of the Stacks Project, [Tag 0CXN](https://stacks.math.columbia.edu/tag/0CXN). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CXN, the section

[Tag 0CXN](https://stacks.math.columbia.edu/tag/0CXN) in the Stacks Project.

**`Deformation.Artin.locallyOfFiniteType_and_quasiCompact_of_isPullback_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/FiniteTypeCorner.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/FiniteTypeCorner.lean#L67). The attribute's comment: “observation (3): if S is locally Noetherian, A, B, B' are of finite type over S and B is finite over A, then A' = A ×_B B' is of finite type over S”.

> **Observation (3) of the section on condition (RS\*).** Let `S` be locally Noetherian, and
> let `U = Spec B`, `V = Spec A`, `W = Spec B'`, `Z = Spec A'` be affine schemes with morphisms
> `f : U ⟶ V`, `g : U ⟶ W`, `i : V ⟶ Z`, `j : W ⟶ Z` whose square of global sections exhibits
> `A' = A ×_B B'`, with `B' → B` surjective, and let `t : Z ⟶ S` give the `S`-algebra structures.
> If `A` and `B'` are of finite type over `S` and `B` is finite over `A`, then `A'` is of finite
> type over `S`.

```lean
public theorem locallyOfFiniteType_and_quasiCompact_of_isPullback_appTop
    {S U V W Z : Scheme.{u}} [IsLocallyNoetherian S]
    [IsAffine U] [IsAffine V] [IsAffine W] [IsAffine Z]
    (f : U ⟶ V) (g : U ⟶ W) (i : V ⟶ Z) (j : W ⟶ Z) (t : Z ⟶ S)
    (hsq : IsPullback i.appTop j.appTop f.appTop g.appTop)
    (hsurj : Function.Surjective g.appTop.hom) (hfin : f.appTop.hom.Finite)
    [LocallyOfFiniteType (i ≫ t)] [LocallyOfFiniteType (j ≫ t)] :
    LocallyOfFiniteType t ∧ QuasiCompact t
```

**`Deformation.Artin.isPushout_of_isPullback_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/FromThickeningPushouts.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/FromThickeningPushouts.lean#L125). The attribute's comment: “observation (1): Spec(A') = Spec(A) ⨿_{Spec(B)} Spec(B') in the category of schemes, for A' = A ×_B B' with B' → B surjective (the square-zero kernel is not needed)”.

> A cartesian square of global sections of four affine schemes, one of whose maps is surjective
> on global sections, is a cocartesian square of schemes. This is [Stacks Project, Tag 0ET0]
> transported along `AlgebraicGeometry.Scheme.isoSpec`.

```lean
public theorem isPushout_of_isPullback_appTop {U V W Z : Scheme.{u}}
    [IsAffine U] [IsAffine V] [IsAffine W] [IsAffine Z]
    (f : U ⟶ V) (g : U ⟶ W) (i : V ⟶ Z) (j : W ⟶ Z)
    (hsq : IsPullback i.appTop j.appTop f.appTop g.appTop)
    (hsurj : Function.Surjective g.appTop.hom) : IsPushout f g i j
```

**`Deformation.Artin.satisfiesRS_of_satisfiesRSStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/RSStarImpliesRS.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/RSStarImpliesRS.lean#L685). The attribute's comment: “observation (4): if 𝒳 satisfies (RS*), then 𝒳 satisfies (RS); the base need not be locally Noetherian”.

> **The remark following Stacks 07Y8: condition (RS\*) implies condition (RS).**
>
> Given a pushout square of finite-type local Artinian objects of the site along a closed
> immersion, the closed immersion is a surjection of Artinian local rings, so its kernel is
> nilpotent; the surjection therefore factors as a tower of square-zero surjections, each of
> which (RS\*) covers, and the resulting squares of fibres paste to the given one.

```lean
public theorem satisfiesRS_of_satisfiesRSStar
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒵 : Type u₁} [Category.{v₁} 𝒵] (p : 𝒵 ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hRS : SatisfiesRSStar B S hS p hp) :
    SatisfiesRS B S hS p hp
```

## Tag 07Y8, a definition

[Tag 07Y8](https://stacks.math.columbia.edu/tag/07Y8) in the Stacks Project.

**`Deformation.Artin.isDeformationCategory_predeformationCategory_of_satisfiesRSStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/DeformationCategory.lean, line 1221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/DeformationCategory.lean#L1221). The attribute's comment: “condition (RS*) gives a deformation category”.

> **Stacks Project, Tag 07Y8.** The predeformation category of a finite-type field-valued
> point in a fibred category satisfying (RS*) is a deformation category; only the square-zero
> squares that (RS*) quantifies over are needed.

```lean
public theorem isDeformationCategory_predeformationCategory_of_satisfiesRSStar
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type u₁} [Category.{v₁} 𝒳]
    (p : 𝒳 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRSStar B S hS p hp)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ S)
    (x₀ : 𝒳)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let D := predeformationCategory iΛ
      (p ⋙ Over.post B.inclusion) x₀ hx₀
    letI := D.category
    Deformation.IsDeformationCategory D.projection
```

**`Deformation.Artin.SatisfiesRSStar`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/Strong.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/Strong.lean#L75).

> Condition (RS*): for every fibre-product square of `S`-algebras in the big affine fppf
> site, with one map surjective with square-zero kernel, the canonical functor from the fibre
> over the pullback algebra to the two-fibre product of the other three fibres is an
> equivalence.

```lean
public abbrev SatisfiesRSStar
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type w} [Category X]
    (p : X ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) : Prop
```

## Tag 0CXP, a lemma

[Tag 0CXP](https://stacks.math.columbia.edu/tag/0CXP) in the Stacks Project.

**`Deformation.Artin.satisfiesRSStar_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/AlgebraicStackRSStar.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/RimSchlessinger/AlgebraicStackRSStar.lean#L51).

> **Stacks 0CXP.** Every algebraic stack over `S` satisfies condition (RS*) of
> [Stacks Project, Tag 07Y8].
>
> The atlas of the stack is representable by algebraic spaces, surjective and smooth; smooth
> morphisms of algebraic spaces are formally smooth
> (`AlgebraicGeometry.Space.formallySmooth_of_isSmooth_unconditional`, the implication (1) ⟹ (2) of
> [Stacks Project, Tag 04AM]), so the atlas is formally smooth on objects
> ([Stacks Project, Tag 06D3]), and `Deformation.Artin.satisfiesRSStar_of_atlas` applies.

```lean
theorem satisfiesRSStar_of_isAlgebraicStack
    (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (h𝒳 : Stack.IsAlgebraicStack.{u, w} B S hS 𝒳) :
    ∀ hp : 𝒳.p.IsFiberedInGroupoids, SatisfiesRSStar B S hS 𝒳.p hp
```

## Tag 0CXQ, a lemma

[Tag 0CXQ](https://stacks.math.columbia.edu/tag/0CXQ) in the Stacks Project.

**`Deformation.Artin.twoFibreProductOver_satisfiesRSStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/RimSchlessinger.lean, line 1216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ArtinCriteria/RimSchlessinger.lean#L1216).

> The two-fibre product of categories fibred in groupoids satisfying condition (RS*) again
> satisfies (RS*).

```lean
public theorem twoFibreProductOver_satisfiesRSStar
    {X : Type uX} [Category X]
    {Y : Type uY} [Category Y]
    {Z : Type uZ} [Category Z]
    (pX : X ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (pY : Y ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (pZ : Z ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (F : X ⥤ Y) (G : Z ⥤ Y)
    (hX : pX.IsFiberedInGroupoids) (hY : pY.IsFiberedInGroupoids)
    (hZ : pZ.IsFiberedInGroupoids)
    (hF : F ⋙ pY = pX) (hG : G ⋙ pY = pZ)
    (rsX : Deformation.Artin.SatisfiesRSStar B S hS pX hX)
    (rsY : Deformation.Artin.SatisfiesRSStar B S hS pY hY)
    (rsZ : Deformation.Artin.SatisfiesRSStar B S hS pZ hZ) :
    Deformation.Artin.SatisfiesRSStar B S hS
      (TwoFibreProductOver.structureFunctor pX pZ pY F G)
      (TwoFibreProductOver.isFiberedInGroupoids pX pZ pY F G
        hX hZ hY hF hG)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.18, Tag 0CXN](https://stacks.math.columbia.edu/tag/0CXN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
