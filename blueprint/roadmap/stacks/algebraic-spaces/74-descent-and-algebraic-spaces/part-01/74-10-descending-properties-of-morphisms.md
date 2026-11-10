---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.Topology, AlgebraicGeometry.Space.Topology.IsCovering, AlgebraicGeometry.Space.Topology.precoverage, CategoryTheory.MorphismProperty.IsLocalAtTarget, AlgebraicGeometry.Space.prop_fiberProduct_fst_of_isLocalAtTarget, AlgebraicGeometry.Space.largestOpenSubspace, AlgebraicGeometry.Space.factorsThrough_largestOpenSubspace, AlgebraicGeometry.Space.largestOpenSubspace_baseChange
statement: formalized
proof: formalized
---

# 74.10 Descending properties of morphisms

Section 74.10 of the Stacks Project, [Tag 03YG](https://stacks.math.columbia.edu/tag/03YG). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03YH, a definition

[Tag 03YH](https://stacks.math.columbia.edu/tag/03YH) in the Stacks Project.

**`AlgebraicGeometry.Space.Topology`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L375). The attribute's comment: “the five topologies”.

> **Stacks 03YH.** The topologies for which locality on the base of a property of morphisms
> of algebraic spaces is considered.

```lean
inductive Topology
```

**`AlgebraicGeometry.Space.Topology.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L392). The attribute's comment: “covering families”.

> **Stacks 03YH.** A family of morphisms of algebraic spaces over `S` with common target is
> a covering family for the topology `τ` when its source and target presheaves are algebraic
> spaces and it satisfies the covering condition of `τ`.

```lean
abbrev Topology.IsCovering (τ : Topology)
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Yi : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : ∀ i, Yi i ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.Topology.precoverage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L410). The attribute's comment: “the precoverage”.

> **Stacks 03YH.** The precoverage on the category of algebraic spaces over `S` presented by
> the `τ`-covering families. A property `P` of morphisms of algebraic spaces is local on the
> base for `τ` exactly when
> `CategoryTheory.MorphismProperty.IsLocalAtTarget P (τ.precoverage B S hS)`.

```lean
def Topology.precoverage (τ : Topology)
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    Precoverage (AlgebraicSpaces B S hS)
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsLocalAtTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsLocalAtTarget#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L418) (StacksFrontier): “locality on the base”. References: SGA 3 IV (4.6.3), “(e_T)”; SGA 3 VIB (2.0), “b)”.

## Tag 06EM, a lemma

[Tag 06EM](https://stacks.math.columbia.edu/tag/06EM) in the Stacks Project.

**`AlgebraicGeometry.Space.prop_fiberProduct_fst_of_isLocalAtTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/LocalAtTarget.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/LocalAtTarget.lean#L121).

> A property of morphisms of algebraic spaces over `S` which is local on the base for `τ` is
> inherited by the base change along any morphism of the kind belonging to `τ`.

```lean
theorem prop_fiberProduct_fst_of_isLocalAtTarget
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (τ : Topology) (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtTarget (τ.precoverage.{u, v} B S hS)]
    {X Y Y' : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f)
    (hg : match τ with
      | .fpqc => IsFlat B S hS g.hom
      | .fppf => IsFlat B S hS g.hom ∧ IsLocallyOfFinitePresentation B S hS g.hom
      | .syntomic => IsSyntomic B S hS g.hom
      | .smooth => IsSmooth B S hS g.hom
      | .etale => IsEtale B S hS g.hom) :
    P (ObjectProperty.homMk (pullback.fst g.hom f.hom) :
      AlgebraicSpaces.fiberProduct B S hS g f ⟶ Y')
```

## Tag 06R2, a lemma

[Tag 06R2](https://stacks.math.columbia.edu/tag/06R2) in the Stacks Project.

**`AlgebraicGeometry.Space.largestOpenSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean#L471). The attribute's comment: “existence and maximality”.

> **Stacks 06R2**, existence and maximality. For a property `P` of morphisms of algebraic
> spaces over `S` which is local on the target for a topology `τ` other than the fpqc topology,
> every morphism `f : X ⟶ Y` has a largest open subspace of `Y` over which its restriction has
> `P`.

```lean
noncomputable def largestOpenSubspace (τ : Topology) (hτ : τ ≠ .fpqc)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtTarget (Topology.precoverage.{u, u + 1} τ B S hS)]
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    {W : {W : Subfunctor Y.obj // IsOpenSubspace B S hS W} //
      HasPropertyOnOpen B S hS P f W ∧
        ∀ V : {V : Subfunctor Y.obj // IsOpenSubspace B S hS V},
          HasPropertyOnOpen B S hS P f V → V.1 ≤ W.1}
```

**`AlgebraicGeometry.Space.factorsThrough_largestOpenSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean#L499). The attribute's comment: “part (1)”.

> **Stacks 06R2**, part (1). A morphism `g : Y' ⟶ Y` which `τ` admits as a member of a
> covering family and along which the base change of `f` has `P` factors through the largest open
> locus of `f`.

```lean
theorem factorsThrough_largestOpenSubspace (τ : Topology) (hτ : τ ≠ .fpqc)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtTarget (Topology.precoverage.{u, u + 1} τ B S hS)]
    {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hg : τ.IsMember B S hS g.hom) (hP : P (pullback.snd f g)) :
    ∃ h : Y' ⟶ openObject B S hS (largestOpenSubspace B S hS τ hτ P f).1,
      h ≫ openInclusion B S hS (largestOpenSubspace B S hS τ hτ P f).1 = g
```

**`AlgebraicGeometry.Space.largestOpenSubspace_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean#L519). The attribute's comment: “part (2)”.

> **Stacks 06R2**, part (2). The largest open locus of a base change of `f` along a morphism
> `g` which `τ` admits as a member of a covering family is the inverse image of the largest open
> locus of `f`.

```lean
theorem largestOpenSubspace_baseChange (τ : Topology) (hτ : τ ≠ .fpqc)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtTarget (Topology.precoverage.{u, u + 1} τ B S hS)]
    {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hg : τ.IsMember B S hS g.hom) :
    (largestOpenSubspace B S hS τ hτ P (pullback.snd f g)).1.1 =
      ((largestOpenSubspace B S hS τ hτ P f).1.1).preimage g.hom
```

**`AlgebraicGeometry.Space.largestOpenSubspace_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargestOpenLocus.lean#L568). The attribute's comment: “part (3)”.

> **Stacks 06R2**, part (3). The largest open locus of the base change of `f` along a member
> of a `τ`-covering of its target is the inverse image of the largest open locus of `f`.

```lean
theorem largestOpenSubspace_covering (τ : Topology) (hτ : τ ≠ .fpqc)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtTarget (Topology.precoverage.{u, u + 1} τ B S hS)]
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) {I : Type v}
    (Yi : I → AlgebraicSpaces B S hS) (g : ∀ i, Yi i ⟶ Y)
    (hg : τ.IsCovering B S hS (fun i ↦ (Yi i).obj) (fun i ↦ (g i).hom)) (i : I) :
    (largestOpenSubspace B S hS τ hτ P (pullback.snd f (g i))).1.1 =
      ((largestOpenSubspace B S hS τ hτ P f).1.1).preimage (g i).hom
```

## Tag 041J, a lemma

[Tag 041J](https://stacks.math.columbia.edu/tag/041J) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalAtTarget_fpqc_of_affineDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FpqcLocalAtTarget.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FpqcLocalAtTarget.lean#L641).

> An affine-local morphism property which descends along surjective flat
> maps of affine schemes and respects finite coproducts is fpqc local on the
> target.

```lean
public theorem isLocalAtTarget_fpqc_of_affineDescent
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hcoprod : ∀ (n : ℕ)
      (X Y : Fin n → AlgebraicSpaces B S hS)
      (f : ∀ i, X i ⟶ Y i)
      (X₀ Y₀ : AlgebraicSpaces B S hS)
      (ιX : ∀ i, X i ⟶ X₀) (ιY : ∀ i, Y i ⟶ Y₀)
      (g : X₀ ⟶ Y₀),
      IsColimit (Cofan.mk X₀ ιX) →
      IsColimit (Cofan.mk Y₀ ιY) →
      (∀ i, f i ≫ ιY i = ιX i ≫ g) →
      (∀ i, P (f i)) → P g)
    (haffine : ∀ {X Y : AlgebraicSpaces B S hS}
      (f : X ⟶ Y),
      P f ↔ ∀ (T : BigAffineFppf B S hS)
        (g : schemeSpace
          ((BigAffineFppf.inclusion B S hS).obj T) ⟶ Y),
        P (pullback.snd f g))
    (hdescent : ∀ (T T' : BigAffineFppf B S hS)
      (g : T' ⟶ T),
      Flat ((BigAffineFppf.toScheme B S hS).map g) →
      Surjective ((BigAffineFppf.toScheme B S hS).map g) →
      ∀ (X : AlgebraicSpaces B S hS)
        (f : X ⟶ schemeSpace
          ((BigAffineFppf.inclusion B S hS).obj T)),
        P (pullback.snd f
          (schemeSpaceMap
            ((BigAffineFppf.inclusion B S hS).map g))) → P f) :
    P.IsLocalAtTarget (Space.Topology.precoverage.{u, v}
      .fpqc B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.10, Tag 03YG](https://stacks.math.columbia.edu/tag/03YG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
