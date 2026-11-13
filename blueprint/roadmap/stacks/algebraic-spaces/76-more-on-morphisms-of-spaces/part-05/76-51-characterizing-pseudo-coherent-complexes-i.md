---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.torIndependent_baseChange_product_of_isFlat, AlgebraicGeometry.Space.nonempty_derivedChowDatum, AlgebraicGeometry.Space.DerivedChowDatum.isFinitePresentation_overOpenToOpen, AlgebraicGeometry.Space.DerivedChowDatum.nonempty_restrict_derivedPushforward_tensor_iso, AlgebraicGeometry.Space.isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor, AlgebraicGeometry.Space.isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor_perfect
statement: formalized
proof: formalized
---

# 76.51 Characterizing pseudo-coherent complexes, II

Section 76.51 of the Stacks Project, [Tag 0CTP](https://stacks.math.columbia.edu/tag/0CTP). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CTQ, a lemma

[Tag 0CTQ](https://stacks.math.columbia.edu/tag/0CTQ) in the Stacks Project.

**`AlgebraicGeometry.Space.torIndependent_baseChange_product_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceFlatBaseChange.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/TorIndependenceFlatBaseChange.lean#L512).

> Let `S` be a scheme, let
> ```
> Z' ⟶ Y'
> ↓     ↓
> X' ⟶ B'
> ```
> be a commutative square of algebraic spaces over `S`, let `Bb ⟶ B'` be a morphism and let `Xb`
> and `Yb` be the base changes of `X'` and `Y'` to `Bb`.  If `Y' ⟶ B'` and `Z' ⟶ X'` are flat,
> then `Xb ×_{Bb} Yb` and `Z'` are Tor independent over `X' ×_{B'} Y'`.

```lean
public theorem torIndependent_baseChange_product_of_isFlat
    {Bb B' X' Y' Z' Xb Yb P P' : AlgebraicSpaces B S hS}
    {bb : Bb ⟶ B'} {x : X' ⟶ B'} {y : Y' ⟶ B'} {zx : Z' ⟶ X'} {zy : Z' ⟶ Y'}
    (hz : zx ≫ x = zy ≫ y)
    {xX' : Xb ⟶ X'} {xB : Xb ⟶ Bb} (sqX : IsPullback xX'.hom xB.hom x.hom bb.hom)
    {yY' : Yb ⟶ Y'} {yB : Yb ⟶ Bb} (sqY : IsPullback yY'.hom yB.hom y.hom bb.hom)
    {pXb : P ⟶ Xb} {pYb : P ⟶ Yb} (sqP : IsPullback pXb.hom pYb.hom xB.hom yB.hom)
    {p'X : P' ⟶ X'} {p'Y : P' ⟶ Y'} (sqP' : IsPullback p'X.hom p'Y.hom x.hom y.hom)
    (pp' : P ⟶ P') (hpp'X : pp' ≫ p'X = pXb ≫ xX') (hpp'Y : pp' ≫ p'Y = pYb ≫ yY')
    (zp' : Z' ⟶ P') (hzp'X : zp' ≫ p'X = zx) (hzp'Y : zp' ≫ p'Y = zy)
    (hy : IsFlat B S hS y.hom) (hzx : IsFlat B S hS zx.hom) :
    TorIndependent P.2 Z'.2 P'.2 pp'.hom zp'.hom
```

## Tag 0CTR, a lemma

[Tag 0CTR](https://stacks.math.columbia.edu/tag/0CTR) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_derivedChowDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/General.lean, line 576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/General.lean#L576).

> **Stacks 0CTR (derived Chow lemma).** Let `A` be a ring and `X` an algebraic space separated
> and of finite presentation over `A`. Every point `x ∈ |X|` carries a datum of the derived Chow
> lemma: `n ≥ 0`, a closed subspace `Z ⊂ X ×_A ℙⁿ_A` of finite presentation, an open `V ⊂ ℙⁿ_A`,
> a point of `c⁻¹(V)` over `x` and `E ∈ D(𝒪_{X ×_A ℙⁿ_A})` with properties (1)–(5) of the source
> (`AlgebraicGeometry.Space.DerivedChowDatum`).

```lean
theorem nonempty_derivedChowDatum (X : AlgebraicSpaces B (Spec (.of A)) hA)
    (hsep : IsSeparated B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X).hom)
    (hfp : IsFinitePresentation B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X).hom)
    (x : points B (Spec (.of A)) hA X.1) :
    Nonempty (DerivedChowDatum X x)
```

## Tag 0CTS, a lemma

[Tag 0CTS](https://stacks.math.columbia.edu/tag/0CTS) in the Stacks Project.

**`AlgebraicGeometry.Space.DerivedChowDatum.isFinitePresentation_overOpenToOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/Restriction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/Restriction.lean#L179). The attribute's comment: “the closed immersion c|\_W : W ⟶ V of the statement is of finite presentation”.

> **Stacks 0CTS, first assertion.** For `X` of finite presentation over `S`, the closed
> immersion `c|_W : W ⟶ V` is of finite presentation.

```lean
theorem isFinitePresentation_overOpenToOpen
    (hfp : IsFinitePresentation B S hS (toBase B S hS X).hom) :
    IsFinitePresentation B S hS (overOpenToOpen D.i D.v).hom
```

**`AlgebraicGeometry.Space.DerivedChowDatum.nonempty_restrict_derivedPushforward_tensor_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/Restriction.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/Restriction.lean#L196).

> **Stacks 0CTS.** For a datum `(n, Z, z, V, E)` of the derived Chow lemma on `X` and
> `K ∈ D_QCoh(𝒪_X)`, `Rq_*(Lp^*K ⊗^𝐋 E)|_V ≅ R(c|_W)_* K|_W`, where `p` and `q` are the two
> projections of `X ×_S ℙⁿ_S`, `c|_W : W ⟶ V` is the closed immersion of the datum and `K|_W` is
> the derived pullback along the étale morphism `b : W ⟶ X`.

```lean
theorem nonempty_restrict_derivedPushforward_tensor_iso
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hK : QcohDerived B S hS X K) :
    Nonempty ((smallEtaleDerivedModulePullback B S hS D.v).obj
        ((derivedModulePushforward B S hS (productSnd X D.n D.contains)).obj
          (((smallEtaleDerivedTensor B S hS (product B S hS X D.n D.contains)).obj
            ((smallEtaleDerivedModulePullback B S hS (productFst X D.n D.contains)).obj K)).obj
              D.E)) ≅
      (derivedModulePushforward B S hS (overOpenToOpen D.i D.v)).obj
        ((smallEtaleDerivedModulePullback B S hS
          (overOpenι D.i D.v ≫ D.i ≫ productFst X D.n D.contains)).obj K))
```

## Tag 0CTT, a lemma

[Tag 0CTT](https://stacks.math.columbia.edu/tag/0CTT) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePseudoCoherent.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePseudoCoherent.lean#L73).

> **Stacks 0CTT.** Let `X` be an algebraic space separated and of finite presentation over `A`
> and `K ∈ D_QCoh(𝒪_X)` with `RΓ(X, E ⊗^𝐋 K)` pseudo-coherent over `A` for every pseudo-coherent
> `E`. Then `K` is pseudo-coherent relative to `A`.

```lean
theorem isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor
    {X : AlgebraicSpaces B (Spec (CommRingCat.of A)) hA}
    (hsep : IsSeparated B _ hA (toBase B _ hA X).hom)
    (hfp : IsFinitePresentation B _ hA (toBase B _ hA X).hom)
    (K : DerivedCategory (Modules.{u, u} B _ hA X.1 X.2)) (hK : QcohDerived B _ hA X K)
    (h : ∀ E : DerivedCategory (Modules.{u, u} B _ hA X.1 X.2),
      (smallEtaleRingedSite B _ hA X.1 X.2).IsPseudoCoherent E →
        StacksDraft.PseudoCoherence.IsPseudoCoherent
          ((representedAffineDerivedSections B _ hA (baseSiteObj B _ hA)).obj
            ((derivedModulePushforward B _ hA (toBase B _ hA X)).obj
              (((smallEtaleDerivedTensor B _ hA X).obj E).obj K)))) :
    IsRelativelyPseudoCoherent B _ hA X.1 X.2 (toBase B _ hA X).hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B _ hA hfp.1) ⟨K, hK⟩
```

## Tag 0GFJ, a lemma

[Tag 0GFJ](https://stacks.math.columbia.edu/tag/0GFJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePseudoCoherentPerfect.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePseudoCoherentPerfect.lean#L53).

> Let `X` be an algebraic space separated and of finite presentation over `A` and
> `K ∈ D_QCoh(𝒪_X)` with `RΓ(X, E ⊗^𝐋 K)` pseudo-coherent over `A` for every perfect `E`. Then `K`
> is pseudo-coherent relative to `A`.

```lean
theorem isRelativelyPseudoCoherent_of_isPseudoCoherent_derivedSections_tensor_perfect
    {X : AlgebraicSpaces B (Spec (CommRingCat.of A)) hA}
    (hsep : IsSeparated B _ hA (toBase B _ hA X).hom)
    (hfp : IsFinitePresentation B _ hA (toBase B _ hA X).hom)
    (K : DerivedCategory (Modules.{u, u} B _ hA X.1 X.2)) (hK : QcohDerived B _ hA X K)
    (h : ∀ E : DerivedCategory (Modules.{u, u} B _ hA X.1 X.2),
      (smallEtaleRingedSite B _ hA X.1 X.2).IsPerfect E →
        StacksDraft.PseudoCoherence.IsPseudoCoherent
          ((representedAffineDerivedSections B _ hA (baseSiteObj B _ hA)).obj
            ((derivedModulePushforward B _ hA (toBase B _ hA X)).obj
              (((smallEtaleDerivedTensor B _ hA X).obj E).obj K)))) :
    IsRelativelyPseudoCoherent B _ hA X.1 X.2 (toBase B _ hA X).hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B _ hA hfp.1) ⟨K, hK⟩
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.51, Tag 0CTP](https://stacks.math.columbia.edu/tag/0CTP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
