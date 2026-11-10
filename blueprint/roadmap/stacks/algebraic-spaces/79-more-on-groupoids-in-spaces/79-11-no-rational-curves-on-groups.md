---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_factorization_of_dense_open, AlgebraicGeometry.Space.exists_coordinateProjection_isFinite, AlgebraicGeometry.Space.morphism_projectiveLine_constant
statement: formalized
proof: formalized
---

# 79.11 No rational curves on groups

Section 79.11 of the Stacks Project, [Tag 0AEK](https://stacks.math.columbia.edu/tag/0AEK). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AEL, a lemma

[Tag 0AEL](https://stacks.math.columbia.edu/tag/0AEL) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_factorization_of_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FactorizationDenseOpen.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FactorizationDenseOpen.lean#L201).

> **Stacks 0AEL.** Let `f : X ⟶ Y` and `g : X ⟶ Z` be morphisms of algebraic spaces over an
> algebraic space `T` with `Y ⟶ T` separated and `g` surjective, flat and locally of finite
> presentation. If there is a scheme-theoretically dense open subspace `V ⊆ Z` such that the
> restriction of `f` to `g⁻¹(V)` factors through `V` over `T`, then `f` factors through `g`
> over `T`.

```lean
theorem exists_factorization_of_dense_open
    {T X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hT : IsAlgebraicSpace B S hS T) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (pX : X ⟶ T) (pY : Y ⟶ T) (pZ : Z ⟶ T) (f : X ⟶ Y) (g : X ⟶ Z)
    (hf : f ≫ pY = pX) (hg : g ≫ pZ = pX)
    (hsep : IsSeparated B S hS pY)
    (hsurj : IsSurjective B S hS g) (hflat : IsFlat B S hS g)
    (hlfp : IsLocallyOfFinitePresentation B S hS g)
    (V : Subfunctor Z) (hV : IsOpenSubspace B S hS V)
    (hdense : IsSchemeTheoreticallyDense B S hS V)
    (hfactor : ∃ v : V.toFunctor ⟶ Y,
      (v ≫ pY = V.ι ≫ pZ) ∧
      (pullback.fst g V.ι ≫ f = pullback.snd g V.ι ≫ v)) :
    ∃ h : Z ⟶ Y, (g ≫ h = f) ∧ (h ≫ pY = pZ)
```

## Tag 0AEM, a lemma

[Tag 0AEM](https://stacks.math.columbia.edu/tag/0AEM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_coordinateProjection_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ProjectiveLineFactorization.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ProjectiveLineFactorization.lean#L176).

> **Stacks 0AEM.** Let `k` be a field, let `n` be a positive integer, let `Z` be an algebraic
> space over `Spec k` separated and of finite type over `Spec k` and let `w : (ℙ¹_k)^n ⟶ Z`. Then
> `w` factors as the projection onto the coordinates in some subset `I ⊆ Fin n` followed by a
> finite morphism.
>
> The contraction step is
> `AlgebraicGeometry.Space.exists_coordinateProjection_finite_fibres`, and a morphism out of a
> finite power of the projective line all of whose fibres on points are finite is finite by
> `AlgebraicGeometry.Space.isFinite_of_finite_fibres`.

```lean
theorem exists_coordinateProjection_isFinite (n : ℕ) (hn : 0 < n)
    (Z : (BigFppfOver B (Spec (CommRingCat.of k)) hk)ᵒᵖ ⥤ Type u)
    (hZ : IsAlgebraicSpace B (Spec (CommRingCat.of k)) hk Z)
    (z : Z ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hk)) : BigFppfOver B (Spec (CommRingCat.of k)) hk))
    (hsep : IsSeparated B (Spec (CommRingCat.of k)) hk z)
    (hft : IsFiniteType B (Spec (CommRingCat.of k)) hk z)
    (w : projectiveLinePower k B hk (Fin n) ⟶ Z) :
    ∃ (I : Finset (Fin n)) (g : projectiveLinePower k B hk I ⟶ Z),
      w = coordinateProjection k B hk n I ≫ g ∧
        IsFinite B (Spec (CommRingCat.of k)) hk g
```

## Tag 0AEN, a lemma

[Tag 0AEN](https://stacks.math.columbia.edu/tag/0AEN) in the Stacks Project.

**`AlgebraicGeometry.Space.morphism_projectiveLine_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ProjectiveLineFactorization.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ProjectiveLineFactorization.lean#L197).

> **Stacks 0AEN.** Let `k` be a field and let `G` be a separated group algebraic space locally
> of finite type over `k`. Every morphism from the projective line over `k` to `G` over `Spec k`
> is constant: it factors through a section of the structure morphism of `G`.
>
> This is `AlgebraicGeometry.Space.morphism_projectiveLine_eq_constant` with its hypothesis
> `h0AEMfibres` — the contraction step of [Stacks, Tag 0AEM] — supplied by
> `AlgebraicGeometry.Space.exists_coordinateProjection_finite_fibres`.

```lean
theorem morphism_projectiveLine_constant
    (G : GroupAlgebraicSpace B (Spec (CommRingCat.of k)) hk
      (yoneda.obj (Over.mk (𝟙 (B.obj hk))))
      (isAlgebraicSpace_yoneda B (Spec (CommRingCat.of k)) hk _))
    (hsep : IsSeparatedOver B (Spec (CommRingCat.of k)) hk G.obj.X.left)
    (hft : IsLocallyOfFiniteType B (Spec (CommRingCat.of k)) hk G.obj.X.hom)
    (f : projectiveLineOverBase k B hk ⟶ G.obj.X) :
    ∃ c : yoneda.obj (Over.mk (𝟙 (B.obj hk))) ⟶ G.obj.X.left,
      c ≫ G.obj.X.hom = 𝟙 _ ∧
        f.left = (projectiveLineOverBase k B hk).hom ≫ c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.11, Tag 0AEK](https://stacks.math.columbia.edu/tag/0AEK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
