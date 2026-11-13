---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.CurveGlobalSections.isPerfect, Stacks.EtaleCohomology.isPerfect_etaleModuleDerivedGlobalSections_fieldBaseChange_of_isCtf
statement: formalized
proof: formalized
---

# 64.13 Cohomology of nice complexes

Section 64.13 of the Stacks Project, [Tag 0964](https://stacks.math.columbia.edu/tag/0964). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03TV, a proposition

[Tag 03TV](https://stacks.math.columbia.edu/tag/03TV) in the Stacks Project.

**`Stacks.EtaleCohomology.CurveGlobalSections.isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveGlobalSections.lean, line 745](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveGlobalSections.lean#L745). The attribute's comment: “from the hypercohomology spectral sequences `hSS` and `hSSZ`, the finiteness `hFin` of the étale cohomology of a constructible sheaf, the cohomological dimension `hDimZ`, the constructibility `hPullback` of a derived inverse image, and the projection formula with the Tor window `hTwisting`”.

> **Stacks 03TV.** Let `k` be a field, let `X` be a projective curve over `k`, let `Λ` be a
> finite commutative ring and let `K` be an object of `D_ctf(X_étale, Λ)`. Then the derived global
> sections `RΓ(X_k̄, K)` of the restriction of `K` to the geometric fibre
> `X_k̄ = X ×_{Spec k} Spec k̄` form a perfect complex of `Λ`-modules.
>
> The geometric fibre is the object `Y` of the big étale site, pinned down by `_hbase`, and the
> restriction of `K` to it is the bounded below complex `Kbar`, pinned down by `eKbar`. The proof
> is the one of the source: the hypercohomology spectral sequence `hSS` together with the
> finiteness `hFin` of the étale cohomology of a constructible sheaf gives finiteness of the
> cohomology modules, the projection formula contained in `hTwisting` together with the
> hypercohomology spectral sequence `hSSZ` and the cohomological dimension `hDimZ` gives finite
> Tor dimension, and the criterion of Tag 03TO concludes.

```lean
theorem isPerfect (Y : B.Scheme) (f : Y ⟶ X)
    (Dt : StacksDraft.Perfect.BalancedDerivedTensoring.{r, w} Λ)
    (hSS : HasHypercohomologySpectralSequence.{u, w, r} B Λ Y)
    (hSSZ : HasHypercohomologySpectralSequence.{u, w, 0} B ℤ Y)
    (hFin : HasFiniteConstructibleCohomology.{u, w, r} B Λ Y)
    (hDimZ : HasFiniteEtaleCohomologicalDimension.{u, w, 0} B ℤ Y)
    (hPullback : HasConstructibleDerivedPullback.{u, w, r} B Λ)
    (hTwisting : HasGeometricTwisting.{u, w, r, d} B X Λ T Y f Dt)
    {k : Type u} [Field k] (gk : X.obj ⟶ Spec (CommRingCat.of k))
    (_hcurve : IsCurve k gk) (_hprojective : IsProjective gk)
    (_hbase : ∃ e : Y.obj ≅ Stacks.Frobenius.fieldBaseChange (Over.mk gk) (AlgebraicClosure k),
      B.inclusion.map f = e.hom ≫ pullback.fst gk
        (Stacks.Frobenius.specAlgebraMap k (AlgebraicClosure k)))
    (K : ConstructibleFiniteTorDerivedCategory.{u, w, r, d} B X Λ T)
    (Kbar : DerivedCategory.Plus (SmallEtaleModuleSheaf.{u, w, r} B Λ Y))
    (eKbar : Nonempty (DerivedCategory.Plus.ι.obj Kbar ≅
      (smallEtaleModulePullback.{u, w, r} B Λ f).mapDerivedCategory.obj K.obj.obj)) :
    StacksDraft.Perfect.IsPerfect
      (DerivedCategory.Plus.ι.obj
        ((smallEtaleModuleDerivedGlobalSections.{u, w, r} B Λ Y).obj Kbar))
```

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.isPerfect_etaleModuleDerivedGlobalSections_fieldBaseChange_of_isCtf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveGlobalSectionsPerfect.lean#L40), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumberOfCtfTrace.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumberOfCtfTrace.lean#L175) (StacksFrontier): “for a projective curve `X` over a field `k`, a finite ring `Λ` and `K` in `D_ctf(X, Λ)`, `RΓ(X_k̄, K)` is a perfect complex of `Λ`-modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.13, Tag 0964](https://stacks.math.columbia.edu/tag/0964)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
