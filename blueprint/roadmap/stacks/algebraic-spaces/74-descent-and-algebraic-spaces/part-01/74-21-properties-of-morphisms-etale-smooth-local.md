---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsEtaleSmoothLocalOnSourceAndTarget, AlgebraicGeometry.Space.postcomp_of_etale, AlgebraicGeometry.Space.of_comp_etale, AlgebraicGeometry.Space.isLocalAtSource_etale, AlgebraicGeometry.Space.isLocalAtTarget_smooth, AlgebraicGeometry.Space.etaleSmoothLocalOnSourceAndTarget_tfae, AlgebraicGeometry.Space.isEtaleSmoothLocalOnSourceAndTarget_of_local, AlgebraicGeometry.Space.isEtale_isEtaleSmoothLocalOnSourceAndTarget
statement: formalized
proof: formalized
---

# 74.21 Properties of morphisms étale-smooth local on source-and-target

Section 74.21 of the Stacks Project, [Tag 0CFY](https://stacks.math.columbia.edu/tag/0CFY). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CFZ, a definition

[Tag 0CFZ](https://stacks.math.columbia.edu/tag/0CFZ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsEtaleSmoothLocalOnSourceAndTarget`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSmoothLocalOnSourceAndTarget.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSmoothLocalOnSourceAndTarget.lean#L59).

> **Stacks 0CFZ.** A property of morphisms of algebraic spaces over `S` is *étale-smooth local
> on the source-and-target* when it is stable under étale precomposition and under smooth base
> change, and holds exactly when it holds on an étale neighbourhood over a smooth target
> neighbourhood of every point of the source.

```lean
structure IsEtaleSmoothLocalOnSourceAndTarget
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS)) : Prop
```

## Tag 0CG0, a lemma

[Tag 0CG0](https://stacks.math.columbia.edu/tag/0CG0) in the Stacks Project.

**`AlgebraicGeometry.Space.postcomp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean#L111). The attribute's comment: “etale\_postcomposition”.

> **Stacks 0CG0**, étale postcomposition. A property of morphisms of algebraic spaces over `S`
> which is étale-smooth local on the source-and-target is preserved by postcomposition with an
> étale morphism.

```lean
theorem postcomp_of_etale
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : P f) (g : Y ⟶ Z)
    (hg : IsEtale B S hS g.hom) : P (f ≫ g)
```

**`AlgebraicGeometry.Space.of_comp_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean#L142). The attribute's comment: “etale\_postcomposition\_permanence”.

> **Stacks 0CG0**, cancelling an étale postcomposition. If a property of morphisms of
> algebraic spaces over `S` is étale-smooth local on the source-and-target and holds for `f ≫ g`
> with `g` étale, then it holds for `f`.

```lean
lemma of_comp_etale
    {P : MorphismProperty (AlgebraicSpaces B S hS)}
    (hP : IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : IsEtale B S hS g.hom)
    (hfg : P (f ≫ g)) : P f
```

**`AlgebraicGeometry.Space.isLocalAtSource_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean#L159). The attribute's comment: “etale\_local\_source”.

> **Stacks 0CG0**, étale locality on the source. A property of morphisms of algebraic spaces
> over `S` which is étale-smooth local on the source-and-target is local at the source for the
> étale topology.

```lean
theorem isLocalAtSource_etale
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : IsEtaleSmoothLocalOnSourceAndTarget B S hS P) :
    P.IsLocalAtSource (Topology.precoverage.{u, v} .etale B S hS)
```

**`AlgebraicGeometry.Space.isLocalAtTarget_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothProperties.lean#L207). The attribute's comment: “smooth\_local\_target”.

> **Stacks 0CG0**, smooth locality on the target. A property of morphisms of algebraic spaces
> over `S` which is étale-smooth local on the source-and-target is local at the target for the
> smooth topology.

```lean
theorem isLocalAtTarget_smooth
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : IsEtaleSmoothLocalOnSourceAndTarget B S hS P) :
    P.IsLocalAtTarget (Topology.precoverage.{u, v} .smooth B S hS)
```

## Tag 0CG1, a lemma

[Tag 0CG1](https://stacks.math.columbia.edu/tag/0CG1) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleSmoothLocalOnSourceAndTarget_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothTfae.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothTfae.lean#L114).

> **Stacks 0CG1.** Seven equivalent criteria for a morphism `f : X ⟶ Y` of algebraic spaces
> over `S` to have a property which is étale-smooth local on the source-and-target: the property
> itself; an étale neighbourhood over a smooth target neighbourhood on which it holds above every
> point of the source; one such neighbourhood surjective onto the source; every such
> neighbourhood; a smooth covering of the target whose base changes have it; an étale covering of
> the source whose composites have it; and a smooth covering of the target together with étale
> coverings of the corresponding fibre products.

```lean
theorem etaleSmoothLocalOnSourceAndTarget_tfae
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : IsEtaleSmoothLocalOnSourceAndTarget B S hS P)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    List.TFAE [
      P f,
      (∀ x : points B S hS X.1,
        ∃ (V U : AlgebraicSpaces B S hS)
          (b : V ⟶ Y)
          (e : U ⟶ AlgebraicSpaces.fiberProduct B S hS f b)
          (v : points B S hS U.1),
          IsSmooth B S hS b.hom ∧
          IsEtale B S hS e.hom ∧
          pointsMap B S hS U.1
            (e ≫ (ObjectProperty.homMk (pullback.fst f.hom b.hom) :
              AlgebraicSpaces.fiberProduct B S hS f b ⟶ X)).hom v = x ∧
          P (e ≫ (ObjectProperty.homMk (pullback.snd f.hom b.hom) :
            AlgebraicSpaces.fiberProduct B S hS f b ⟶ V))),
      (∃ (V U : AlgebraicSpaces B S hS)
        (b : V ⟶ Y)
        (e : U ⟶ AlgebraicSpaces.fiberProduct B S hS f b),
        IsSmooth B S hS b.hom ∧
        IsEtale B S hS e.hom ∧
        IsSurjective B S hS
          (e ≫ (ObjectProperty.homMk (pullback.fst f.hom b.hom) :
            AlgebraicSpaces.fiberProduct B S hS f b ⟶ X)).hom ∧
        P (e ≫ (ObjectProperty.homMk (pullback.snd f.hom b.hom) :
          AlgebraicSpaces.fiberProduct B S hS f b ⟶ V))),
      (∀ (V U : AlgebraicSpaces B S hS)
        (b : V ⟶ Y)
        (e : U ⟶ AlgebraicSpaces.fiberProduct B S hS f b),
        IsSmooth B S hS b.hom →
        IsEtale B S hS e.hom →
        P (e ≫ (ObjectProperty.homMk (pullback.snd f.hom b.hom) :
          AlgebraicSpaces.fiberProduct B S hS f b ⟶ V))),
      (∃ (I : Type (u + 1))
        (V : I → AlgebraicSpaces B S hS)
        (b : ∀ i, V i ⟶ Y),
        IsSmoothCovering B S hS (fun i => (V i).1) (fun i => (b i).hom) ∧
        ∀ i, P (ObjectProperty.homMk (pullback.snd f.hom (b i).hom) :
          AlgebraicSpaces.fiberProduct B S hS f (b i) ⟶ V i)),
      (∃ (I : Type (u + 1))
        (U : I → AlgebraicSpaces B S hS)
        (a : ∀ i, U i ⟶ X),
        IsEtaleCovering B S hS (fun i => (U i).1) (fun i => (a i).hom) ∧
        ∀ i, P ((a i) ≫ f)),
      (∃ (I : Type (u + 1))
        (V : I → AlgebraicSpaces B S hS)
        (b : ∀ i, V i ⟶ Y)
        (J : I → Type (u + 1))
        (U : ∀ i, J i → AlgebraicSpaces B S hS)
        (e : ∀ i j, U i j ⟶ AlgebraicSpaces.fiberProduct B S hS f (b i)),
        IsSmoothCovering B S hS (fun i => (V i).1) (fun i => (b i).hom) ∧
        ∀ i, IsEtaleCovering B S hS (fun j => (U i j).1) (fun j => (e i j).hom) ∧
          ∀ j, P (e i j ≫
            (ObjectProperty.homMk (pullback.snd f.hom (b i).hom) :
              AlgebraicSpaces.fiberProduct B S hS f (b i) ⟶ V i)))]
```

## Tag 0CG2, a lemma

[Tag 0CG2](https://stacks.math.columbia.edu/tag/0CG2) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleSmoothLocalOnSourceAndTarget_of_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothFromLocality/SchemeSquareDescent.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothFromLocality/SchemeSquareDescent.lean#L307).

> **Stacks 0CG2.** A property of morphisms of algebraic spaces over `S` which is étale local
> on the source, smooth local on the target and stable under postcomposition with open immersions
> is étale-smooth local on the source-and-target.

```lean
theorem isEtaleSmoothLocalOnSourceAndTarget_of_local
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsLocalAtSource (Space.Topology.precoverage.{u, u + 1} .etale B S hS)]
    [P.IsLocalAtTarget (Space.Topology.precoverage.{u, u + 1} .smooth B S hS)]
    [P.RespectsRight (fun ⦃X Y : AlgebraicSpaces B S hS⦄
      (f : X ⟶ Y) => Space.IsOpenImmersion B S hS f.hom)] :
    Space.IsEtaleSmoothLocalOnSourceAndTarget B S hS P
```

## Tag 0CG3, a remark

[Tag 0CG3](https://stacks.math.columbia.edu/tag/0CG3) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_isEtaleSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean#L69). The attribute's comment: “étale”.

> Étaleness of morphisms of algebraic spaces over `S` is étale-smooth local on the
> source-and-target.

```lean
theorem isEtale_isEtaleSmoothLocalOnSourceAndTarget :
    IsEtaleSmoothLocalOnSourceAndTarget B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsEtale B S hS f.hom)
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_isEtaleSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean#L90). The attribute's comment: “locally quasi-finite”.

> Local quasi-finiteness of morphisms of algebraic spaces over `S` is étale-smooth local on
> the source-and-target.

```lean
theorem isLocallyQuasiFinite_isEtaleSmoothLocalOnSourceAndTarget :
    IsEtaleSmoothLocalOnSourceAndTarget B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsLocallyQuasiFinite B S hS f.hom)
```

**`AlgebraicGeometry.Space.isUnramified_isEtaleSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/EtaleSmoothExamples.lean#L112). The attribute's comment: “unramified”.

> Unramifiedness of morphisms of algebraic spaces over `S` is étale-smooth local on the
> source-and-target.

```lean
theorem isUnramified_isEtaleSmoothLocalOnSourceAndTarget :
    IsEtaleSmoothLocalOnSourceAndTarget B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsUnramified B S hS f.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.21, Tag 0CFY](https://stacks.math.columbia.edu/tag/0CFY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
