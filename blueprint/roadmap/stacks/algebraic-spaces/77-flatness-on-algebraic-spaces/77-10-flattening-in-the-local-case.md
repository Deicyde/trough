---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_idealSheafData_isFlatOverAtPoint_iff_factors, AlgebraicGeometry.Space.exists_finitePresentation_idealSheafData_isFlatOverAtPoint_iff_factors
statement: formalized
proof: formalized
---

# 77.10 Flattening in the local case

Section 77.10 of the Stacks Project, [Tag 0CWN](https://stacks.math.columbia.edu/tag/0CWN). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CWP, a lemma

[Tag 0CWP](https://stacks.math.columbia.edu/tag/0CWP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_idealSheafData_isFlatOverAtPoint_iff_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/LocalFlattening.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/LocalFlattening.lean#L406). The attribute's comment: “the closed flattening subscheme, for an arbitrary subset E of the closed fibre: nothing is assumed beyond the source's hypotheses”.

> **Stacks Project, Tag 0CWP.** Let `S = Spec A` be the spectrum of a henselian local ring with
> closed point `s`, let `f : X ⟶ S` be a morphism of algebraic spaces which is locally of finite
> type, let `F` be a quasi-coherent `𝒪_X`-module of finite type and let `E ⊆ |X_s|` be a subset.
> There is a closed subscheme `Z ⊆ S` such that for every morphism of pointed schemes
> `(T, t) ⟶ (S, s)` the following are equivalent:
>
> 1. `F_T` is flat over `T` at all points of `|X_t|` which map to a point of `E ⊆ |X_s|`;
> 2. `Spec 𝒪_{T,t} ⟶ S` factors through `Z`.
>
> Here `X` is an algebraic space over `S`, `f` its structure morphism to the terminal algebraic
> space `S`, and `X_T = X ×_S T` the fibre product of algebraic spaces; the points of `|X_t|` are
> the points of `|X_T|` over `t ∈ |T|`, and the closed fibre `|X_s|` is the set of points of `|X|`
> over `s`, through which a point of `|X_t|` maps to `|X_s|` by its image in `|X|`. Flatness of
> `F_T` over `T` at a point is Stacks 05VV at a point, and `Z` is given by its ideal sheaf.

```lean
theorem exists_idealSheafData_isFlatOverAtPoint_iff_factors [HenselianLocalRing A]
    (X : AlgebraicSpaces B (Spec (.of A)) hA) (f : X ⟶ schemeSpace (Over.mk (𝟙 (B.obj hA))))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f.hom)
    (F : Modules.{u, u} B (Spec (.of A)) hA X.1 X.2) (hFq : F.IsQuasicoherentOnSite)
    (hFt : SheafOfModules.IsFiniteTypeOnSite F)
    (E : Set {x : points B (Spec (.of A)) hA X.1 //
      pointsMap B (Spec (.of A)) hA X.1 f.hom x = closedBasePoint A B hA}) :
    ∃ Z : (Spec (.of A)).IdealSheafData,
      ∀ (T : BigFppfOver B (Spec (.of A)) hA) (g : T ⟶ Over.mk (𝟙 (B.obj hA)))
        (t : (BigFppfOver.toScheme B (Spec (.of A)) hA).obj T),
        (BigFppfOver.toScheme B (Spec (.of A)) hA).map g t = IsLocalRing.closedPoint A →
        ((∀ x' : points B (Spec (.of A)) hA (pullback f (schemeSpaceMap g)).1,
            pointsMap B (Spec (.of A)) hA _ (pullback.snd f (schemeSpaceMap g)).hom x' =
              (pointsEquivScheme B (Spec (.of A)) hA T).symm t →
            ∀ hx : pointsMap B (Spec (.of A)) hA X.1 f.hom
                (pointsMap B (Spec (.of A)) hA _ (pullback.fst f (schemeSpaceMap g)).hom x') =
                closedBasePoint A B hA,
              (⟨_, hx⟩ : {x : points B (Spec (.of A)) hA X.1 //
                pointsMap B (Spec (.of A)) hA X.1 f.hom x = closedBasePoint A B hA}) ∈ E →
              IsFlatOverAtPoint B (Spec (.of A)) hA (pullback f (schemeSpaceMap g)).2
                (pullback.snd f (schemeSpaceMap g)).hom
                ((modulePullback B (Spec (.of A)) hA (pullback.fst f (schemeSpaceMap g))).obj F)
                x') ↔
          ∃ h : Spec (((BigFppfOver.toScheme B (Spec (.of A)) hA).obj T).presheaf.stalk t) ⟶
              Z.subscheme,
            h ≫ Z.subschemeι = ((BigFppfOver.toScheme B (Spec (.of A)) hA).obj T).fromSpecStalk t ≫
              (BigFppfOver.toScheme B (Spec (.of A)) hA).map g)
```

**`AlgebraicGeometry.Space.exists_finitePresentation_idealSheafData_isFlatOverAtPoint_iff_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/LocalFlattening.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/LocalFlattening.lean#L460). The attribute's comment: “the finite-presentation assertion, for E closed and quasi-compact in |X\_s|: nothing is assumed beyond the source's hypotheses”.

> **Stacks Project, Tag 0CWP, the final assertion.** In the situation of
> `AlgebraicGeometry.Space.exists_idealSheafData_isFlatOverAtPoint_iff_factors`, if moreover
> `X ⟶ S` is locally of finite presentation, `F` is of finite presentation and `E ⊆ |X_s|` is
> closed and quasi-compact, then the closed subscheme `Z` may be chosen with `Z ⟶ S` of finite
> presentation. The topology on `|X_s|` is the subspace topology of the closed fibre in `|X|`
> (Stacks 03BY).

```lean
theorem exists_finitePresentation_idealSheafData_isFlatOverAtPoint_iff_factors
    [HenselianLocalRing A]
    (X : AlgebraicSpaces B (Spec (.of A)) hA) (f : X ⟶ schemeSpace (Over.mk (𝟙 (B.obj hA))))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f.hom)
    (hfp : IsLocallyOfFinitePresentation B (Spec (.of A)) hA f.hom)
    (F : Modules.{u, u} B (Spec (.of A)) hA X.1 X.2) (hFq : F.IsQuasicoherentOnSite)
    (hFt : SheafOfModules.IsFiniteTypeOnSite F) (hFp : SheafOfModules.IsFinitePresentationOnSite F)
    (E : Set {x : points B (Spec (.of A)) hA X.1 //
      pointsMap B (Spec (.of A)) hA X.1 f.hom x = closedBasePoint A B hA})
    (hEc : IsClosed E) (hEk : IsCompact E) :
    ∃ Z : (Spec (.of A)).IdealSheafData,
      AlgebraicGeometry.FinitePresentation Z.subschemeι ∧
      ∀ (T : BigFppfOver B (Spec (.of A)) hA) (g : T ⟶ Over.mk (𝟙 (B.obj hA)))
        (t : (BigFppfOver.toScheme B (Spec (.of A)) hA).obj T),
        (BigFppfOver.toScheme B (Spec (.of A)) hA).map g t = IsLocalRing.closedPoint A →
        ((∀ x' : points B (Spec (.of A)) hA (pullback f (schemeSpaceMap g)).1,
            pointsMap B (Spec (.of A)) hA _ (pullback.snd f (schemeSpaceMap g)).hom x' =
              (pointsEquivScheme B (Spec (.of A)) hA T).symm t →
            ∀ hx : pointsMap B (Spec (.of A)) hA X.1 f.hom
                (pointsMap B (Spec (.of A)) hA _ (pullback.fst f (schemeSpaceMap g)).hom x') =
                closedBasePoint A B hA,
              (⟨_, hx⟩ : {x : points B (Spec (.of A)) hA X.1 //
                pointsMap B (Spec (.of A)) hA X.1 f.hom x = closedBasePoint A B hA}) ∈ E →
              IsFlatOverAtPoint B (Spec (.of A)) hA (pullback f (schemeSpaceMap g)).2
                (pullback.snd f (schemeSpaceMap g)).hom
                ((modulePullback B (Spec (.of A)) hA (pullback.fst f (schemeSpaceMap g))).obj F)
                x') ↔
          ∃ h : Spec (((BigFppfOver.toScheme B (Spec (.of A)) hA).obj T).presheaf.stalk t) ⟶
              Z.subscheme,
            h ≫ Z.subschemeι = ((BigFppfOver.toScheme B (Spec (.of A)) hA).obj T).fromSpecStalk t ≫
              (BigFppfOver.toScheme B (Spec (.of A)) hA).map g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.10, Tag 0CWN](https://stacks.math.columbia.edu/tag/0CWN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
