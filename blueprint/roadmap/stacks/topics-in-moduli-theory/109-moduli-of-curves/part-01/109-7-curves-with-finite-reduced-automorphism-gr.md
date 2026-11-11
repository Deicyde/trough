---
declaration: section
origin: cited
lean: AlgebraicGeometry.isClosedImmersion_doublePointsToProjectiveLine, AlgebraicGeometry.isPushout_gluingScheme, AlgebraicGeometry.gluedCurve, AlgebraicGeometry.isPushout_gluedCurve, AlgebraicGeometry.epsTranslate, AlgebraicGeometry.epsTranslate_ne_one, AlgebraicGeometry.map_fst_epsTranslate, AlgebraicGeometry.isAffineOpen_gluedCurveAffinePart
statement: formalized
proof: formalized
---

# 109.7 Curves with finite reduced automorphism groups

Section 109.7 of the Stacks Project, [Tag 0DST](https://stacks.math.columbia.edu/tag/0DST). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DSU, an example

[Tag 0DSU](https://stacks.math.columbia.edu/tag/0DSU) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_doublePointsToProjectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L238). The attribute's comment: “the three double points form a closed subscheme of the projective line”.

> **Stacks 0DSU.** For three pairwise distinct points of the affine line, the three double
> points `Spec(k[t]/(t - aᵢ)²)` form a closed subscheme of `P¹_k`.

```lean
theorem isClosedImmersion_doublePointsToProjectiveLine (hpts : Function.Injective pts) :
    IsClosedImmersion (doublePointsToProjectiveLine k pts)
```

**`AlgebraicGeometry.isPushout_gluingScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L256). The attribute's comment: “the two affine lines glue to the spectrum of the equalizer of the two reductions”.

> **Stacks 0DSU.** Gluing two copies of `A¹_k` along the three double points gives the
> spectrum of the equalizer of the two reduction maps `k[t] × k[t] ⇉ ∏ᵢ k[t]/(t - aᵢ)²`: the
> functions on the affine part of the glued curve are the pairs of polynomials agreeing to first
> order at the three points.

```lean
theorem isPushout_gluingScheme (hpts : Function.Injective pts) :
    IsPushout (doublePointsToAffineLine k pts) (doublePointsToAffineLine k pts)
      (Spec.map (CommRingCat.ofHom (gluingSubringSnd pts)))
      (Spec.map (CommRingCat.ofHom (gluingSubringFst pts)))
```

**`AlgebraicGeometry.gluedCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L270). The attribute's comment: “the curve obtained by gluing two projective lines along three double points”.

> **Stacks 0DSU.** The curve `X` of the example: two copies of `P¹_k` glued along the closed
> subscheme of the three double points `Spec(k[t]/(t - aᵢ)²)`, that is, the pushout of
> `T ⟶ P¹_k` with itself.

```lean
def gluedCurve : Scheme.{u}
```

**`AlgebraicGeometry.isPushout_gluedCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L287). The attribute's comment: “the glued curve is the pushout of the two projective lines”.

> **Stacks 0DSU.** The glued curve is the pushout of the two copies of `P¹_k` along the
> three double points.

```lean
theorem isPushout_gluedCurve :
    IsPushout (doublePointsToProjectiveLine k pts) (doublePointsToProjectiveLine k pts)
      (gluedCurveInl k pts hpts) (gluedCurveInr k pts hpts)
```

**`AlgebraicGeometry.epsTranslate`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L451). The attribute's comment: “the automorphism of the equalizer diagram sending t to t + epsilon”.

> **Stacks 0DSU.** The automorphism of the equalizer diagram
> `k[ε][t] × k[ε][t] ⇉ ∏ᵢ k[ε][t]/(t - aᵢ)²` over the dual numbers of a field of characteristic
> `2` given by the substitution `t ↦ t + ε` on both coordinates.

```lean
def epsTranslate : gluingSubring pts ≃+* gluingSubring pts
```

**`AlgebraicGeometry.epsTranslate_ne_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L457). The attribute's comment: “non-triviality of the automorphism sending t to t + epsilon”.

> **Stacks 0DSU.** The substitution `t ↦ t + ε` on the equalizer diagram is not the
> identity.

```lean
theorem epsTranslate_ne_one : epsTranslate k pts ≠ RingEquiv.refl _
```

**`AlgebraicGeometry.map_fst_epsTranslate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePoints.lean#L465). The attribute's comment: “the automorphism sending t to t + epsilon is the identity modulo epsilon”.

> **Stacks 0DSU.** The substitution `t ↦ t + ε` becomes the identity modulo `ε`.

```lean
theorem map_fst_epsTranslate (x : gluingSubring pts) :
    ((Polynomial.mapRingHom (TrivSqZeroExt.fstHom k k k).toRingHom) (epsTranslate k pts x).1.1,
        (Polynomial.mapRingHom (TrivSqZeroExt.fstHom k k k).toRingHom)
          (epsTranslate k pts x).1.2) =
      ((Polynomial.mapRingHom (TrivSqZeroExt.fstHom k k k).toRingHom) x.1.1,
        (Polynomial.mapRingHom (TrivSqZeroExt.fstHom k k k).toRingHom) x.1.2)
```

**`AlgebraicGeometry.isAffineOpen_gluedCurveAffinePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsAffinePart.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsAffinePart.lean#L250). The attribute's comment: “the affine open part U of X, the image of the two affine lines”.

> **`U` is an affine open of the glued curve.**

```lean
theorem isAffineOpen_gluedCurveAffinePart : IsAffineOpen (gluedCurveAffinePart k pts hpts)
```

**`AlgebraicGeometry.gluedCurveAffinePartSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsAffinePart.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsAffinePart.lean#L257). The attribute's comment: “O\_X(U) is the equalizer of k[t] × k[t] ⇉ ∏ k[t]/(t - a\_i)²”.

> **The functions on `U` are the equalizer** `O_X(U) ⟶ k[t] × k[t] ⇉ ∏ᵢ k[t]/(t - aᵢ)²`: the
> ring of sections of `X` over the affine part is the ring of pairs of polynomials agreeing to first
> order at the three points.

```lean
def gluedCurveAffinePartSectionsEquiv :
    Γ(gluedCurve k pts hpts, gluedCurveAffinePart k pts hpts) ≃+* gluingSubring pts
```

**`AlgebraicGeometry.gluedCurveDualNumbersAut`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean#L398). The attribute's comment: “the automorphism t ↦ t + ε extends to an automorphism of X over A = k[ε]”.

> **The automorphism `t ↦ t + ε` of the equalizer diagram extends to an automorphism of `X`
> over `A = k[ε]`.** For `k` of characteristic `2`, the automorphism of
> `X_A = X ×_{Spec k} Spec k[ε]` over `Spec k[ε]` which is the translation `t ↦ t + ε` on both
> copies of `ℙ¹_{k[ε]}`.

```lean
def gluedCurveDualNumbersAut :
    Aut (Over.mk (pullback.snd (gluedCurveToBase k pts hpts) (dualNumbersToBase k)))
```

**`AlgebraicGeometry.projectiveLineXChart_comp_gluedCurveDualNumbersAut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean#L415). The attribute's comment: “the automorphism of X\_A is the substitution t ↦ t + ε on the two affine lines”.

> **The automorphism of `X_A` restricts on the two affine lines `Spec k[ε][t]` to the
> substitution `t ↦ t + ε`** of the equalizer diagram
> `O(U_A) ⟶ k[ε][t] × k[ε][t] ⇉ ∏ᵢ k[ε][t]/(t - aᵢ)²`; on the equalizer itself this substitution is
> `AlgebraicGeometry.epsTranslate`.

```lean
theorem projectiveLineXChart_comp_gluedCurveDualNumbersAut (b : Bool) :
    projectiveLineXChart (DualNumber k) ≫ gluedCurveDualNumbersComponent k pts hpts b ≫
        (gluedCurveDualNumbersAut k pts hpts).asIso.hom.left =
      Spec.map (CommRingCat.ofHom (translate (DualNumber.eps : DualNumber k)).toRingHom) ≫
        projectiveLineXChart (DualNumber k) ≫ gluedCurveDualNumbersComponent k pts hpts b
```

**`AlgebraicGeometry.gluedCurveDualNumbersAut_ne_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsDualNumbers.lean#L440). The attribute's comment: “the automorphism of X over A is nontrivial”.

> **The automorphism of `X_A` is not the identity**: it moves the `k[ε]`-point
> `t = 0` of the first copy of `ℙ¹_{k[ε]}` to the point `t = ε`.

```lean
theorem gluedCurveDualNumbersAut_ne_one : gluedCurveDualNumbersAut k pts hpts ≠ 1
```

**`AlgebraicGeometry.finite_aut_gluedCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsFiniteAutomorphisms.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsFiniteAutomorphisms.lean#L338). The attribute's comment: “the automorphism group of X over k is finite”.

> **The automorphism group of `X` over `k` is finite.** For `k` algebraically
> closed and three distinct points, the group of automorphisms over `k` of the curve obtained by
> gluing two copies of `ℙ¹_k` along the three double points `Spec(k[t]/(t - aᵢ)²)` is finite.

```lean
theorem finite_aut_gluedCurve :
    Finite (Aut (Over.mk (gluedCurveToBase k pts hpts)))
```

**`AlgebraicGeometry.finite_autFunctor_gluedCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean#L104). The attribute's comment: “the automorphism group of X over k, the k-points of Aut(X), is finite”.

> `Aut(X)(k)` is finite.

```lean
theorem finite_autFunctor_gluedCurve :
    Finite ((Scheme.autFunctor (gluedCurveOver k pts hpts)).obj (op (pointOver k)))
```

**`AlgebraicGeometry.autFunctor_map_gluedCurveDualNumbersAut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean#L210). The attribute's comment: “the automorphism t ↦ t + ε becomes the identity modulo ε”.

> The automorphism `t ↦ t + ε` of `X_{k[ε]}` restricts to the identity over the closed point
> of `Spec k[ε]`: its image under `Aut(X)(k[ε]) ⟶ Aut(X)(k)` is the identity.

```lean
theorem autFunctor_map_gluedCurveDualNumbersAut :
    (Scheme.autFunctor (gluedCurveOver k pts hpts)).map (dualNumbersClosedPoint k).op
      (gluedCurveDualNumbersAut k pts hpts) =
        (1 : Aut ((Over.pullback (pointOver k).hom).obj (gluedCurveOver k pts hpts)))
```

**`AlgebraicGeometry.not_exists_isReduced_represents_autFunctor_gluedCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ProjectiveLinesGluedAtDoublePointsNonreducedAut.lean#L224). The attribute's comment: “Aut(X) is non-reduced”.

> **The automorphism group scheme of `X` is non-reduced.** For `k` algebraically closed of
> characteristic `2` and three distinct points, no reduced scheme locally of finite type over `k`
> represents the automorphism functor `T ↦ Aut_T(X_T)` of the curve `X` obtained by gluing two
> copies of `ℙ¹_k` along the double points at the three points.

```lean
theorem not_exists_isReduced_represents_autFunctor_gluedCurve :
    ¬ ∃ (G : Over (Spec (.of k))) (_ : IsReduced G.left) (_ : LocallyOfFiniteType G.hom),
      Nonempty (yoneda.obj G ≅ Scheme.autFunctor (gluedCurveOver k pts hpts))
```

## Tag 0DSV, an example

[Tag 0DSV](https://stacks.math.columbia.edu/tag/0DSV) in the Stacks Project.

**`AlgebraicGeometry.GenusOne.autScheme_topologicalKrullDim_eq_one_of_genus_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusOne/AutomorphismSchemeDimension.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusOne/AutomorphismSchemeDimension.lean#L271). The attribute's comment: “genus one: the automorphism group scheme of a smooth proper genus one curve over an algebraically closed field exists and has dimension one”.

> **Stacks Project, Tag 0DSV**, genus one. **The automorphism group scheme of a smooth proper
> curve of genus one over an algebraically closed field has dimension one.** The automorphism
> functor `T ↦ Aut_T(X ×_k T)` of `X` over `k` is representable by a scheme over `k`, and every
> scheme representing it has dimension one.

```lean
theorem autScheme_topologicalKrullDim_eq_one_of_genus_eq_one
    (hg : genus f = 1) :
    (∃ G : Over (Spec (.of k)), Nonempty ((Scheme.autFunctor (Over.mk f)).RepresentableBy G)) ∧
      ∀ (G : Over (Spec (.of k))), (Scheme.autFunctor (Over.mk f)).RepresentableBy G →
        topologicalKrullDim G.left = 1
```

**`AlgebraicGeometry.GenusZero.autFunctor_projectiveLine_representableBy_projectiveGeneralLinearTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZero/AutomorphismSchemeDimension.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZero/AutomorphismSchemeDimension.lean#L63). The attribute's comment: “genus zero: Aut(P^1\_k) = PGL\_\{2,k} as functors, an invertible matrix acting by its Moebius map, and PGL\_\{2,k} has dimension three”.

> **Stacks Project, Tag 0DSV**, genus zero. **`Aut(ℙ¹_k) = PGL_{2,k}` as functors.** The scheme
> `PGL_{2,k}` represents the automorphism functor of the projective line over `k`, the point of
> `PGL_{2,k}` given by an invertible matrix `M` over a `k`-algebra `A` corresponding to the Möbius
> automorphism of `M`; and `PGL_{2,k}` has dimension three.

```lean
theorem autFunctor_projectiveLine_representableBy_projectiveGeneralLinearTwo :
    (∃ R : (Scheme.autFunctor (projectiveLineOver k)).RepresentableBy
        (projectiveGeneralLinearTwoScheme k),
      ∀ {A : Type u} [CommRing A] (h : Spec (.of A) ⟶ Spec (.of k))
        (M : Matrix (Fin 2) (Fin 2) A) (hM : IsUnit M.det),
        R.homEquiv (evaluationOver h M hM) = mobiusAutFunctor h M hM) ∧
      topologicalKrullDim (projectiveGeneralLinearTwoScheme k).left = 3
```

**`AlgebraicGeometry.GenusZero.autScheme_topologicalKrullDim_eq_three_of_genus_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusZero/AutomorphismSchemeSmoothCurve.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusZero/AutomorphismSchemeSmoothCurve.lean#L90). The attribute's comment: “genus zero: the automorphism functor of a smooth proper genus zero curve over an algebraically closed field is represented by PGL\_\{2,k}, and every representing scheme has dimension three”.

> **Stacks Project, Tag 0DSV**, genus zero. **The automorphism group scheme of a smooth proper
> curve of genus zero over an algebraically closed field is `PGL_{2,k}` and has dimension three.**
> The automorphism functor `T ↦ Aut_T(X ×_k T)` of `X` over `k` is represented by `PGL_{2,k}`, and
> every scheme representing it has dimension three.

```lean
theorem autScheme_topologicalKrullDim_eq_three_of_genus_eq_zero (hg : genus f = 0) :
    Nonempty ((Scheme.autFunctor (Over.mk f)).RepresentableBy
        (projectiveGeneralLinearTwoScheme k)) ∧
      ∀ G : Over (Spec (.of k)), (Scheme.autFunctor (Over.mk f)).RepresentableBy G →
        topologicalKrullDim G.left = 3
```

## Tag 0DSW, a lemma

[Tag 0DSW](https://stacks.math.columbia.edu/tag/0DSW) in the Stacks Project.

**`AlgebraicGeometry.curvesSmall.exists_deligneMumfordLocus_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesDeligneMumfordLocusUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesDeligneMumfordLocusUnconditional.lean#L60).

> There exists an open substack `Curves^DM ⊂ Curves` of the algebraic stack of curves over
> `Spec ℤ` such that
>
> 1. `Curves^DM` is the maximal open substack of `Curves` which is DM: it is Deligne–Mumford, and
>    every Deligne–Mumford open substack of `Curves` is contained in it;
> 2. for a family of curves `X → S`, the classifying morphism `S → Curves` factors through
>    `Curves^DM` if and only if the group algebraic space `Aut_S(X)` is unramified over `S`;
> 3. for a field-valued point `x : Spec k → Curves`, classifying a proper `X` of dimension `≤ 1`
>    over `k`, the following are equivalent: `x` factors through `Curves^DM`; `Aut(X)` is
>    geometrically reduced over `k` of dimension `0`; `Aut(X) → Spec k` is unramified.

```lean
theorem exists_deligneMumfordLocus_unconditional :
    ∃ W : Stack.OpenSubstack (curvesAlgebraicStack B hZ
        (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)),
      (Stack.AlgebraicStacks.IsAbsolutelyDM B integerBase hZ B.contains_terminal
          W.toAlgebraicStack ∧
        ∀ V : Stack.OpenSubstack (curvesAlgebraicStack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)),
          Stack.AlgebraicStacks.IsAbsolutelyDM B integerBase hZ B.contains_terminal
              V.toAlgebraicStack →
            V.property ≤ W.property) ∧
      (∀ F : CurveFamily B hZ,
        W.property (ShrinkHoms.toShrinkHoms F) ↔
          Space.IsUnramified B integerBase hZ (CurveFamily.autFunctorProjection F)) ∧
      ∀ x : Stack.FieldValuedPoint B integerBase hZ (curvesAlgebraicStack B hZ
          (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)).val.val,
        List.TFAE
          [W.property x.obj,
            Space.IsGeometricallyReduced x.carrier B
                (Stack.contains_spectrum_fieldValuedPoint B integerBase hZ x)
                (Stack.automorphismGroupSpaceOverField B integerBase hZ _ x)
                (Stack.isAlgebraicSpace_automorphismGroupSpaceOverField B integerBase hZ _ x) ∧
              Space.dimension B (Spec (.of x.carrier))
                (Stack.contains_spectrum_fieldValuedPoint B integerBase hZ x)
                (Stack.automorphismGroupSpaceOverField B integerBase hZ _ x)
                (Stack.isAlgebraicSpace_automorphismGroupSpaceOverField B integerBase hZ _ x) = 0,
            Stack.IsUnramifiedAutomorphismGroupSpace B integerBase hZ
              (curvesAlgebraicStack B hZ
                (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)) x]
```

## Tag 0E6G, a lemma

[Tag 0E6G](https://stacks.math.columbia.edu/tag/0E6G) in the Stacks Project.

**`AlgebraicGeometry.curvesSmall.tfae_curvesDMLocus_unramified_derivations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesDMLocusDerivations.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesDMLocusDerivations.lean#L57).

> Let `X` be a proper scheme of dimension at most one over a field `k`, and `x : Spec k → Curves`
> the point of the algebraic stack of curves classifying it. The following are equivalent:
> 1. (Stacks 0DSW (3)(a)) `x` factors through `Curves^DM`, the maximal DM open substack;
> 2. (Stacks 0DSW (3)(b)) `Aut(X)` is geometrically reduced over `k` and has dimension `0`;
> 3. (Stacks 0DSW (3)(c)) `Aut(X) → Spec k` is unramified;
> 4. `Der_k(𝒪_X, 𝒪_X) = 0`, i.e. the type of `k`-derivations of `𝒪_X` into `𝒪_X` is a
>    subsingleton (it has the zero derivation).

```lean
theorem tfae_curvesDMLocus_unramified_derivations :
    List.TFAE
      [Stack.dmLocus B integerBase hZ B.contains_terminal
          (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ))
          (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack B hZ)).obj,
        Space.IsGeometricallyReduced k B hk
            (Stack.automorphismGroupSpaceOverField B integerBase hZ _
              (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)))
            (Stack.isAlgebraicSpace_automorphismGroupSpaceOverField B integerBase hZ _
              (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack B hZ))) ∧
          Space.dimension B (Spec (.of k)) hk
            (Stack.automorphismGroupSpaceOverField B integerBase hZ _
              (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)))
            (Stack.isAlgebraicSpace_automorphismGroupSpaceOverField B integerBase hZ _
              (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack B hZ))) = 0,
        Stack.IsUnramifiedAutomorphismGroupSpace B integerBase hZ
          (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ))
          (curveFieldPoint X hk hdim (curvesFiberedCategory_isAlgebraicStack B hZ)),
        Subsingleton (schemeMorphismDerivations (Λ := k) (k := k) (𝟙 X.left) X.hom)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.7, Tag 0DST](https://stacks.math.columbia.edu/tag/0DST)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
