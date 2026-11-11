---
declaration: section
origin: cited
lean: Stacks.Modules.tilde_isLocallyFree_iff_module, Stacks.Modules.tilde_isFiniteLocallyFree_iff_module, Stacks.Modules.tilde_isFiniteLocallyFreeOfRank_iff_module, tilde_isLocallyFree_iff, tilde_isFiniteLocallyFree_iff, AlgebraicGeometry.Scheme.Modules.flat_finitePresentation_locallyFree_fiberRank_tfae, Stacks.FiniteLocallyFree.ModuleTFAE.finiteLocallyFree_tfae, Stacks.FiniteLocallyFree.Reduced.isFiniteLocallyFree_iff_isFiniteType_and_isLocallyConstant_fiberRank
statement: formalized
proof: formalized
---

# 28.21 Locally free modules

Section 28.21 of the Stacks Project, [Tag 05P1](https://stacks.math.columbia.edu/tag/05P1). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05JM, a lemma

[Tag 05JM](https://stacks.math.columbia.edu/tag/05JM) in the Stacks Project.

**`Stacks.Modules.tilde_isLocallyFree_iff_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean#L243). The attribute's comment: “locally free”.

> The sheaf `M̃` associated to an `R`-module `M` is a locally free `𝒪_X`-module on
> `X = Spec R`, in the sense of Stacks Tag 01C6, if and only if `M` is a locally free
> `R`-module.

```lean
theorem tilde_isLocallyFree_iff_module :
    SheafOfModules.IsLocallyFree.{u, u, u}
        (tilde (R := CommRingCat.of R) (ModuleCat.of R M)) ↔ Module.IsLocallyFree R M
```

**`Stacks.Modules.tilde_isFiniteLocallyFree_iff_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean#L252). The attribute's comment: “finite locally free”.

> The sheaf `M̃` associated to an `R`-module `M` is a finite locally free `𝒪_X`-module on
> `X = Spec R`, in the sense of Stacks Tag 01C6, if and only if `M` is a finite locally free
> `R`-module.

```lean
theorem tilde_isFiniteLocallyFree_iff_module :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (tilde (R := CommRingCat.of R) (ModuleCat.of R M)) ↔ Module.IsFiniteLocallyFree R M
```

**`Stacks.Modules.tilde_isFiniteLocallyFreeOfRank_iff_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LocallyFreeSite.lean#L262). The attribute's comment: “finite locally free of rank r”.

> The sheaf `M̃` associated to an `R`-module `M` is a finite locally free `𝒪_X`-module of rank
> `r` on `X = Spec R`, in the sense of Stacks Tag 01C6, if and only if `M` is a finite locally free
> `R`-module of rank `r`.

```lean
theorem tilde_isFiniteLocallyFreeOfRank_iff_module (r : ℕ) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (tilde (R := CommRingCat.of R) (ModuleCat.of R M)) r ↔
      Module.IsFiniteLocallyFreeOfRank R M r
```

**`tilde_isLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean, line 1645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean#L1645).

> **Statement 1 (locally free case).** `M~` is a locally free `O_X`-module if
> and only if `M` is a locally free `R`-module.
>
> PROOF (complete modulo the two helper lemmas): rewrite the sheaf side via
> `isLocallyFree_iff_basicOpen`, then:
> * (⇒) For each point `x` choose (by `choose`) a standard open `D(g x) ∋ x` on which
>   the sheaf is free; the family `(g x)` covers `Spec R` (each `x ∈ D(g x)`), so
>   `Ideal.span (range g) = ⊤` by `iSup_basicOpen_eq_top_iff`, and by Helper 1 each
>   `M_{g x}` is free — giving `Module.IsLocallyFree R M` with `ι := PrimeSpectrum R`.
> * (⇐) Given a covering family `f : ι → R` with span `⊤` and each `M_{f i}` free:
>   for any `x`, the cover gives `i` with `x ∈ D(f i)`, and Helper 1 makes the sheaf
>   free on `D(f i)`.

```lean
theorem tilde_isLocallyFree_iff (R : Type u) [CommRing R] (M : Type u)
    [AddCommGroup M] [Module R M] :
    (AlgebraicGeometry.tilde (R := CommRingCat.of R) (ModuleCat.of R M)).IsLocallyFree ↔
      Module.IsLocallyFree R M
```

**`tilde_isFiniteLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean, line 1671](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean#L1671). References: EGA III (7.9.1), “M proj f.t. <=> M~ l.f.”.

> **Statement 2 (finite locally free case).** `M~` is a finite locally free
> `O_X`-module if and only if `M` is a finite locally free `R`-module.
>
> PROOF (complete modulo `isFiniteLocallyFree_iff_basicOpen` and
> `tilde_restrict_basicOpen_finiteFree_iff`): same covering combinatorics as
> Statement 1, now carrying the finiteness witness `Finite I` through the helpers.

```lean
theorem tilde_isFiniteLocallyFree_iff (R : Type u) [CommRing R] (M : Type u)
    [AddCommGroup M] [Module R M] :
    (AlgebraicGeometry.tilde (R := CommRingCat.of R) (ModuleCat.of R M)).IsFiniteLocallyFree ↔
      Module.IsFiniteLocallyFree R M
```

## Tag 05P2, a lemma

[Tag 05P2](https://stacks.math.columbia.edu/tag/05P2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.flat_finitePresentation_locallyFree_fiberRank_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiberRank/LocallyFree.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiberRank/LocallyFree.lean#L303). References: EGA III (7.3.4); EGA 0 (5.4.1), “partial, special case”; EGA IV (19.7.4), “more general”; EGA IV (2.1.12), “special case”.

> For a sheaf of modules `F` on a scheme `X` the following are equivalent: `F` is flat and of
> finite presentation; `F` is of finite presentation and all its stalks are free; `F` is locally
> free and of finite type; `F` is finite locally free; `F` is of finite type, all its stalks are
> free, and its fibre rank is locally constant.
>
> Quasi-coherence is not assumed: it is implied by each of the five conditions.

```lean
theorem flat_finitePresentation_locallyFree_fiberRank_tfae {X : Scheme.{u}} (F : X.Modules) :
    List.TFAE [
      AlgebraicGeometry.SheafOfModules.IsFlat
          (C := TopologicalSpace.Opens X.toTopCat)
          (J := Opens.grothendieckTopology X.toTopCat) (O := X.sheaf) F ∧
        F.IsFinitePresentation,
      F.IsFinitePresentation ∧
        (∀ x : X,
          letI : Module (X.presheaf.stalk x) (F.presheaf.stalk x) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := X.presheaf) F.val x
          Module.Free (X.presheaf.stalk x) (F.presheaf.stalk x)),
      _root_.SheafOfModules.IsLocallyFree.{u, u, u} F ∧
        _root_.SheafOfModules.IsFiniteType.{u, u, u} F,
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) F,
      _root_.SheafOfModules.IsFiniteType.{u, u, u} F ∧
        (∀ x : X,
          letI : Module (X.presheaf.stalk x) (F.presheaf.stalk x) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := X.presheaf) F.val x
          Module.Free (X.presheaf.stalk x) (F.presheaf.stalk x)) ∧
        IsLocallyConstant (fiberRank F)]
```

**`Stacks.FiniteLocallyFree.ModuleTFAE.finiteLocallyFree_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/FiniteLocallyFreeTFAE.lean, line 882](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/FiniteLocallyFreeTFAE.lean#L882). References: EGA III (7.3.4).

> A quasi-coherent sheaf of modules on a scheme is finite locally free exactly
> when it satisfies any of the five equivalent flatness, presentation, stalk, or
> rank conditions.
>
> `AlgebraicGeometry.Scheme.Modules.flat_finitePresentation_locallyFree_fiberRank_tfae` in
> `StacksFrontier.AlgebraicGeometry.FiberRank.LocallyFree` carries the tag too, and states the same
> list of five conditions without assuming quasi-coherence, so it implies this statement outright.
> Both carry the tag: a Stacks tag is registered once per clause or part of its statement, and more
> than one carrier is expected rather than a defect.

```lean
theorem finiteLocallyFree_tfae {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] :
    List.TFAE [
      AlgebraicGeometry.SheafOfModules.IsFlat F ∧ F.IsFinitePresentation,
      F.IsFinitePresentation ∧
        (∀ x : X,
          letI : Module (X.presheaf.stalk x) (F.presheaf.stalk x) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := X.presheaf) F.val x
          Module.Free (X.presheaf.stalk x) (F.presheaf.stalk x)),
      SheafOfModules.IsLocallyFree F ∧ F.IsFiniteType,
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree F,
      F.IsFiniteType ∧
        (∀ x : X,
          letI : Module (X.presheaf.stalk x) (F.presheaf.stalk x) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := X.presheaf) F.val x
          Module.Free (X.presheaf.stalk x) (F.presheaf.stalk x)) ∧
        IsLocallyConstant (fiberRank F)]
```

## Tag 0FWH, a lemma

[Tag 0FWH](https://stacks.math.columbia.edu/tag/0FWH) in the Stacks Project.

**`Stacks.FiniteLocallyFree.Reduced.isFiniteLocallyFree_iff_isFiniteType_and_isLocallyConstant_fiberRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/ReducedFiniteLocallyFree.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/ReducedFiniteLocallyFree.lean#L416).

> On a reduced scheme, a quasi-coherent sheaf is finite locally free exactly
> when it is of finite type and has locally constant fibre rank.

```lean
theorem isFiniteLocallyFree_iff_isFiniteType_and_isLocallyConstant_fiberRank
    {X : Scheme.{u}} [IsReduced X] (F : X.Modules) [F.IsQuasicoherent] :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree F ↔
      (F.IsFiniteType ∧ IsLocallyConstant (fiberRank F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.21, Tag 05P1](https://stacks.math.columbia.edu/tag/05P1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
