---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigHOver.essImage_singleFunctor_perfectionModule, AlgebraicGeometry.BigHOver.hCohomologyIsoColimitFrobenius
statement: formalized
proof: formalized
---

# 59.107 Cohomology of the structure sheaf in the h topology

Section 59.107 of the Stacks Project, [Tag 0EWS](https://stacks.math.columbia.edu/tag/0EWS). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EWT, a lemma

[Tag 0EWT](https://stacks.math.columbia.edu/tag/0EWT) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.essImage_singleFunctor_perfectionModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HStructureSheaf/EssentialImage.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HStructureSheaf/EssentialImage.lean#L119).

> **Stacks 0EWT.** Let `p` be a prime number and let `S` be a scheme over `𝔽_p`. Consider the
> sheaf `𝒪^{perf} = colim_F 𝒪` on `(Sch/S)_{fppf}`. Then `𝒪^{perf}` is in the essential image of
> `Rε_* : D((Sch/S)_h) ⟶ D((Sch/S)_{fppf})`.
>
> Here `(Sch/S)_h` is a big h site over `S` and `(Sch/S)_{fppf}` its underlying category with the
> fppf topology. `𝒪^{perf}` is the colimit of the Frobenius system of fppf sheaves of rings
> (`AlgebraicGeometry.BigHOver.isColimitPerfectionCocone`); it is an h sheaf, so the identity is a
> comparison of ringed sites `ε : ((Sch/S)_h, 𝒪^{perf}) ⟶ ((Sch/S)_{fppf}, 𝒪^{perf})`, and `Rε_*` is
> any right derived functor of its direct image on sheaves of modules, with its unit `η`. The object
> is `𝒪^{perf}` regarded as a module over itself and placed in degree zero.

```lean
theorem essImage_singleFunctor_perfectionModule
    (Rε : DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
        (bigHRingedSite B S hS (awnRingSheaf B S hS)).O)) ⥤
      DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
        ((bigHRingedSite B S hS (awnRingSheaf B S hS)).ofLe
          (BigHOver.fppfTopology_le_topology B S hS)).O)))
    (η : (Stacks.Sites.CoarserTopology.modulePushforward.{u + 1, u + 1, u, u}
          (BigHOver.fppfTopology_le_topology B S hS)
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (bigHRingedSite B S hS (awnRingSheaf B S hS)).O)).mapHomotopyCategory
          (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η (HomotopyCategory.quasiIso
      (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
        (bigHRingedSite B S hS (awnRingSheaf B S hS)).O))
        (ComplexShape.up ℤ))] :
    Rε.essImage ((DerivedCategory.singleFunctor _ 0).obj (perfectionModule B S hS))
```

## Tag 0EWU, a proposition

[Tag 0EWU](https://stacks.math.columbia.edu/tag/0EWU) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.hCohomologyIsoColimitFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HStructureSheaf/StructureSheafCohomology.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HStructureSheaf/StructureSheafCohomology.lean#L116).

> Let `p` be a prime number and let `S` be a quasi-compact and quasi-separated scheme over
> `𝔽_p`. Then
>
> `H^i((Sch/S)_h, 𝒪^h) ≅ colim_F H^i(S, 𝒪)`
>
> for every `i`, where `𝒪^h` is the h sheafification of the structure sheaf of the big h site of
> `S`, and the colimit is over the system `H^i(S, 𝒪) →^F H^i(S, 𝒪) →^F ⋯` induced by the
> Frobenius `F : 𝒪_S ⟶ 𝒪_S`, `f ↦ f^p`.
>
> The left-hand side is cohomology over the final object of the big h category over `S`, and the
> right-hand side is the colimit of the right derived functors of sections over `S` applied to the
> Frobenius system `AlgebraicGeometry.Scheme.abelianFrobeniusSystem`.

```lean
def hCohomologyIsoColimitFrobenius [CompactSpace S] [QuasiSeparatedSpace S]
    (i : ℕ) :
    (((sheafSections (BigHOver.topology B S hS) AddCommGrpCat.{u}).obj
        (op (BigHOver.final B S hS))).rightDerived i).obj (hStructureSheaf B S hS) ≅
      colimit (S.abelianFrobeniusSystem p hSp ⋙
        ((sheafSections (Opens.grothendieckTopology S) AddCommGrpCat.{u}).obj
          (op ⊤)).rightDerived i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.107, Tag 0EWS](https://stacks.math.columbia.edu/tag/0EWS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
