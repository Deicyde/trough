---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.quasiCoherentDerived, AlgebraicGeometry.Stack.isQuasicoherentOnSite_affineHomologySheaf, AlgebraicGeometry.Stack.isLocallyKFlatAcyclic_affineEtale, AlgebraicGeometry.Stack.affineEtaleQuasiCoherentEquivalence, AlgebraicGeometry.Stack.representableQuasiCoherentDerivedEquivalence, AlgebraicGeometry.FormalSpace.quasiCoherentDerivedEquivalenceDerivedComplete, AlgebraicGeometry.Stack.isLocallyKFlatAcyclic_affineFppf, AlgebraicGeometry.Stack.affineFppfQuasiCoherentEquivalence
statement: formalized
proof: formalized
---

# 96.26 Quasi-coherent objects in the derived category

Section 96.26 of the Stacks Project, [Tag 0H0G](https://stacks.math.columbia.edu/tag/0H0G). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H0H, a definition

[Tag 0H0H](https://stacks.math.columbia.edu/tag/0H0H) in the Stacks Project.

**`AlgebraicGeometry.Stack.quasiCoherentDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedCategory.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedCategory.lean#L159).

> The *triangulated category of quasi-coherent objects in the derived category* of a category
> `p : 𝒳 ⥤ (Sch/S)_{fppf}` over the big fppf category of `S`:
>
>   `QC(𝒳) = QC(𝒳_{affine}, O)`,
>
> the full subcategory of `D(𝒳_{affine}, O)` of the objects `K` such that for every arrow `U → V`
> of `𝒳_{affine}` the canonical map `RΓ(V, K) ⊗^L_{O(V)} O(U) ⟶ RΓ(U, K)` is an isomorphism, where
> `𝒳_{affine}` is the associated affine site of Stacks 0H09 with its chaotic topology and `O` is
> the structure sheaf of `𝒳` restricted to it.

```lean
abbrev quasiCoherentDerived : Type _
```

## Tag 0H0I, a lemma

[Tag 0H0I](https://stacks.math.columbia.edu/tag/0H0I) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasicoherentOnSite_affineHomologySheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedTopCohomology.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedTopCohomology.lean#L166).

> **Stacks 0H0I.** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids, let `M` be
> an object of the triangulated category `QC(𝒳)` of Stacks 0H0H, and let `b ∈ ℤ` be such that
> `H^i(M) = 0` for all `i > b`. Then `H^b(M)` is a quasi-coherent module on the ringed site
> `(𝒳_{affine}, O)`, in the sense of Stacks 0H0E.

```lean
theorem isQuasicoherentOnSite_affineHomologySheaf
    (M : quasiCoherentDerived.{u, v, w, t} B S hS p) (b : ℤ)
    (hvan : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor
      (PresheafOfModules.{max v w u t} (affineStructurePresheaf B S hS p)) i).obj M.obj)) :
    (affineHomologySheaf.{u, v, w, t} B S hS p M.obj b).IsQuasicoherentOnSite
```

## Tag 0H0J, a lemma

[Tag 0H0J](https://stacks.math.columbia.edu/tag/0H0J) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyKFlatAcyclic_affineEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean#L151). The attribute's comment: “ε : 𝒳\_\{affine,étale} ⟶ 𝒳\_\{affine} satisfies the assumptions of Stacks 0GZS: hypothesis (2), the target being the chaotic site by construction”.

> **Stacks 0H0J, hypothesis (2) of Stacks 0GZS.** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category
> fibred in groupoids and `ε : (𝒳_{affine, étale}, O) ⟶ (𝒳_{affine}, O)` the comparison morphism to
> the associated affine site with its chaotic topology.  For every object `x` of `𝒳_{affine}` and
> every K-flat complex `M^•` of `O(x)`-modules the canonical map
> `M^• ⟶ RΓ((𝒳_{affine, étale}/x), (M^• ⊗_{O(x)} O_x)^#)` is a quasi-isomorphism.  (Hypothesis
> (1) of Stacks 0GZS, that the target topology is chaotic, is the construction of `ε`: modules on
> the chaotic site are presheaves of modules.)

```lean
theorem isLocallyKFlatAcyclic_affineEtale :
    IsLocallyKFlatAcyclic.{t}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (AffineCategory.siteKindRingedSite B S hS p hp .etale).O)
      (affineStructurePresheaf_comm B S hS p)
```

**`AlgebraicGeometry.Stack.affineEtaleQuasiCoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean#L167). The attribute's comment: “ε : 𝒳\_\{affine,étale} ⟶ 𝒳\_\{affine} satisfies the conclusions of Stacks 0GZS: ε^* and Rε\_* are mutually quasi-inverse equivalences between QC(𝒳) and the objects K of D(𝒳\_\{affine,étale}, O) with Rε\_*K in QC(𝒳)”.

> **Stacks 0H0J, the conclusion of Stacks 0GZS.** For a category fibred in groupoids
> `p : 𝒳 ⥤ (Sch/S)_{fppf}` and the comparison `ε : (𝒳_{affine, étale}, O) ⟶ (𝒳_{affine}, O)`,
> `ε^*` and `Rε_*` are mutually quasi-inverse equivalences between `QC(𝒳)` (Stacks 0H0H) and the
> full subcategory of `D(𝒳_{affine, étale}, O)` of the objects `K` with `Rε_*K` in `QC(𝒳)`.  The
> functor of the equivalence is `ε^*` and its inverse is `Rε_*`, both on the nose
> (`AlgebraicGeometry.Stack.affineQuasiCoherentEquivalence_functor` and `_inverse`).

```lean
def affineEtaleQuasiCoherentEquivalence :
    quasiCoherentDerived.{u, v, w, t} B S hS p ≌
      (pushforwardProperty.{t}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (AffineCategory.siteKindRingedSite B S hS p hp .etale).O)
        (IsQuasiCoherentObject.{u, v, w, t} B S hS p)).FullSubcategory
```

## Tag 0H0K, a proposition

[Tag 0H0K](https://stacks.math.columbia.edu/tag/0H0K) in the Stacks Project.

**`AlgebraicGeometry.Stack.representableQuasiCoherentDerivedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/Equivalence.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/Equivalence.lean#L112). The attribute's comment: “QC(𝒳) is canonically equivalent to D\_QCoh(O\_X) for 𝒳 represented by an algebraic space X”.

> **Stacks 0H0K.** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids, represented
> by the algebraic space `F` through the equivalence `e` over the site between `𝒳` and the
> category of elements of `F` (Stacks 04SV). Then `QC(𝒳)` (Stacks 0H0H) is canonically equivalent
> to `D_QCoh(O_F)` (Stacks 071X), with modules in the universe `max v w u t`.
>
> The equivalence is the composite of the three equivalences of the source's proof, on the
> single-universe lifts `X↑` of `𝒳_{affine, étale}` and `Y↑` of `F_{affine, étale}`: `ε^*` from
> `QC(𝒳)` onto the objects `K` of `D(X↑)` with `Rε_*K` cartesian (Stacks 0H0J, 0GZS); the direct
> image `f_*` along the morphism of ringed sites `f : X↑ ⟶ Y↑` given by the affine étale charts of
> `F` (Stacks 073M), inverse to the derived pullback `Lf^*` on the 0GZS subcategories (the
> argument of Stacks 09J1); and the identification of the 0GZS subcategory of `D(Y↑)` with
> `D_QCoh(O_F)` (Stacks 0H0J, 0H06, 03DX).

```lean
def representableQuasiCoherentDerivedEquivalence :
    quasiCoherentDerived.{u, v, w, t} B S hS p ≌
      Space.QuasicoherentDerivedCategory.{u, max v w u t} B S hS F hF
```

## Tag 0H0L, a proposition

[Tag 0H0L](https://stacks.math.columbia.edu/tag/0H0L) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.quasiCoherentDerivedEquivalenceDerivedComplete`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FormalSpectrumQuasiCoherentDerived.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FormalSpectrumQuasiCoherentDerived.lean#L237). The attribute's comment: “QC(𝒳) ≌ D\_comp(A, I) for 𝒳 the category fibred in sets of Spf(A), A an adic Noetherian topological S-algebra with ideal of definition I”.

> **Stacks 0H0L.** Let `S` be a scheme and `X = Spf(A)`, where `A` is an adic Noetherian
> topological `S`-algebra with ideal of definition `I` (More on Algebra, Definition 07E8; Formal
> Spaces, Definition 0AIF). Let `p : 𝒳 → (Sch/S)_{fppf}` be the category fibred in sets associated
> to the functor `X` (Categories, Example 04TM). Then `QC(𝒳)` (Definition 0H0H) is equivalent to the
> category `D_comp(A, I)` of objects of `D(A)` which are derived complete with respect to `I`.
>
> The equivalence is constructed: if the powers of `I` stabilize, `I^{N+1} = I^{N+2}`, then
> `I^{N+1} = 0`, `Spec(A) = Spec(A/I^{N+1})` is a final object of `𝒳_{affine}` and the equivalence
> is `RΓ(Spec(A), -)` (Stacks 0H0R), every object of `D(A)` being derived complete; otherwise it is
> the composite of the source's proof, `qcEquivalenceOfStrict`. Here `D(A)` is the derived category
> of `A`-modules in the universe `max (u + 1) t` of the modules of `QC(𝒳)`, in any model.

```lean
def quasiCoherentDerivedEquivalenceDerivedComplete :
    Stack.quasiCoherentDerived.{u, u + 1, u, t} B S hS (formalSpectrumProjection D) ≌
      ObjectProperty.FullSubcategory
        (fun K : DerivedCategory (ModuleCat.{max (u + 1) t} A) => IsDerivedComplete I K)
```

## Tag 0H0X, a lemma

[Tag 0H0X](https://stacks.math.columbia.edu/tag/0H0X) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyKFlatAcyclic_affineFppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean#L186). The attribute's comment: “ε : 𝒳\_\{affine,fppf} ⟶ 𝒳\_\{affine} satisfies the assumptions of Stacks 0GZS: hypothesis (2), the target being the chaotic site by construction”.

> **Stacks 0H0X, hypothesis (2) of Stacks 0GZS.** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category
> fibred in groupoids and `ε : (𝒳_{affine, fppf}, O) ⟶ (𝒳_{affine}, O)` the comparison morphism to
> the associated affine site with its chaotic topology.  For every object `x` of `𝒳_{affine}` and
> every K-flat complex `M^•` of `O(x)`-modules the canonical map
> `M^• ⟶ RΓ((𝒳_{affine, fppf}/x), (M^• ⊗_{O(x)} O_x)^#)` is a quasi-isomorphism.  (Hypothesis
> (1) of Stacks 0GZS, that the target topology is chaotic, is the construction of `ε`: modules on
> the chaotic site are presheaves of modules.)

```lean
theorem isLocallyKFlatAcyclic_affineFppf :
    IsLocallyKFlatAcyclic.{t}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (AffineCategory.siteKindRingedSite B S hS p hp .fppf).O)
      (affineStructurePresheaf_comm B S hS p)
```

**`AlgebraicGeometry.Stack.affineFppfQuasiCoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentDerivedComparison.lean#L202). The attribute's comment: “ε : 𝒳\_\{affine,fppf} ⟶ 𝒳\_\{affine} satisfies the conclusions of Stacks 0GZS: ε^* and Rε\_* are mutually quasi-inverse equivalences between QC(𝒳) and the objects K of D(𝒳\_\{affine,fppf}, O) with Rε\_*K in QC(𝒳)”.

> **Stacks 0H0X, the conclusion of Stacks 0GZS.** For a category fibred in groupoids
> `p : 𝒳 ⥤ (Sch/S)_{fppf}` and the comparison `ε : (𝒳_{affine, fppf}, O) ⟶ (𝒳_{affine}, O)`,
> `ε^*` and `Rε_*` are mutually quasi-inverse equivalences between `QC(𝒳)` (Stacks 0H0H) and the
> full subcategory of `D(𝒳_{affine, fppf}, O)` of the objects `K` with `Rε_*K` in `QC(𝒳)`.  The
> functor of the equivalence is `ε^*` and its inverse is `Rε_*`, both on the nose
> (`AlgebraicGeometry.Stack.affineQuasiCoherentEquivalence_functor` and `_inverse`).

```lean
def affineFppfQuasiCoherentEquivalence :
    quasiCoherentDerived.{u, v, w, t} B S hS p ≌
      (pushforwardProperty.{t}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (AffineCategory.siteKindRingedSite B S hS p hp .fppf).O)
        (IsQuasiCoherentObject.{u, v, w, t} B S hS p)).FullSubcategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.26, Tag 0H0G](https://stacks.math.columbia.edu/tag/0H0G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
