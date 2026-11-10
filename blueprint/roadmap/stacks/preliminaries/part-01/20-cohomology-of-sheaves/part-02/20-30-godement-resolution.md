---
declaration: section
origin: cited
lean: AlgebraicGeometry.GodementResolution.isFlasque_iterate_modulePullbackPushforward, AlgebraicGeometry.GodementResolution.exists_functorial_flasque_godementComplex, AlgebraicGeometry.GodementResolution.homotopyEquivalences_stalk_godementAugmentation, AlgebraicGeometry.GodementResolution.quasiIso_godementAugmentation, AlgebraicGeometry.GodementResolution.exists_quasiIso_boundedBelow_isFlasque_isHomotopyEquiv_stalk_godement
statement: formalized
proof: formalized
---

# 20.30 Godement resolution

Section 20.30 of the Stacks Project, [Tag 0FKR](https://stacks.math.columbia.edu/tag/0FKR). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FKS, a lemma

[Tag 0FKS](https://stacks.math.columbia.edu/tag/0FKS) in the Stacks Project.

**`AlgebraicGeometry.GodementResolution.isFlasque_iterate_modulePullbackPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/Basic.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/Basic.lean#L276). The attribute's comment: “each term f_* f^* ⋯ f_* f^* F is a flasque module”. References: SGA 4 XVII (4.2.3), “(i)”; SGA 4 XVII (4.2), “flasqueness of terms”.

> Every positive iterate `(f_* f^*)^(n+1) F` of a morphism out of a discrete space is a flasque
> sheaf of modules: a sheaf on a discrete space is flasque, and pushforward preserves flasqueness.

```lean
theorem isFlasque_iterate_modulePullbackPushforward
    {Xdisc X : RingedSpace.{u, u}} (f : Xdisc ⟶ X) [DiscreteTopology Xdisc]
    (n : ℕ) (F : SheafOfModules.{u} (structureSheafRing X)) :
    TopCat.Sheaf.IsFlasque ((SheafOfModules.toSheaf (structureSheafRing X)).obj
      (((RingedSpaceModuleAdjunction.modulePullback f ⋙
        RingedSpaceModuleAdjunction.modulePushforward f).iterate (n + 1)).obj F))
```

**`AlgebraicGeometry.GodementResolution.exists_functorial_flasque_godementComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/Basic.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/Basic.lean#L518). The attribute's comment: “the functorial complex of flasque terms f_* f^* ⋯ f_* f^* F”. References: SGA 4 XVII (4.2.3), “(i)”; SGA 4 XVII (4.2), “functorial flasque terms”.

> **Stacks 0FKS**, the complex and its flasque terms. For a ringed space `(X, O_X)` there is a
> functor `G` from sheaves of `O_X`-modules to cochain complexes, with an augmentation `η` from the
> complex concentrated in degree `0`, whose term in degree `n` is the iterate
> `(f_* f^*)^(n+1) F` along the morphism `f : X_disc ⟶ X` from the points of `X` with the discrete
> topology, and each of whose terms is a flasque `O_X`-module.

```lean
theorem exists_functorial_flasque_godementComplex (X : RingedSpace.{u, u}) :
    ∃ (G : SheafOfModules.{u} (structureSheafRing X) ⥤
        CochainComplex
          (SheafOfModules.{u} (structureSheafRing X)) ℕ)
      (_η : CochainComplex.single₀
          (SheafOfModules.{u} (structureSheafRing X)) ⟶ G)
      (_termIso : ∀ n,
        G ⋙ HomologicalComplex.eval
            (SheafOfModules.{u} (structureSheafRing X))
            (ComplexShape.up ℕ) n ≅
          (RingedSpaceModuleAdjunction.modulePullback (fromDiscrete X) ⋙
            RingedSpaceModuleAdjunction.modulePushforward (fromDiscrete X)).iterate (n + 1)),
      ∀ F n, TopCat.Sheaf.IsFlasque
        ((SheafOfModules.toSheaf (structureSheafRing X)).obj
          ((G.obj F).X n))
```

**`AlgebraicGeometry.GodementResolution.homotopyEquivalences_stalk_godementAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/StalkHomotopy.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/StalkHomotopy.lean#L520). The attribute's comment: “the stalkwise homotopy equivalence F_x[0] ≃ ((f_* f^* F)_x → ⋯)”. References: SGA 4 XVII (4.2.3), “(ii)”; SGA 4 XVII (4.2), “stalkwise homotopy”; SGA 4 XVII (4.2.9), “special case”.

> **Clause (5) of [Stacks, Tag 0FKS]**, at one sheaf and one point. The augmentation
> `F[0] ⟶ (f_* f^* F → f_* f^* f_* f^* F → ⋯)` of the Godement complex, read on the stalk at `x`,
> is a homotopy equivalence of complexes of `𝒪_{X,x}`-modules.
>
> This is `hasNaturalStalkHomotopy_godementAugmentation` evaluated at `F`: evaluation at `F` is an
> additive functor, so it carries the homotopy equivalence of complexes of functors to one of
> complexes of modules, and the compatibility clause identifies the result with the stalk of the
> augmentation up to the two isomorphisms `i` and `j`.

```lean
theorem homotopyEquivalences_stalk_godementAugmentation (x : X)
    (F : SheafOfModules.{u} (structureSheafRing X)) :
    HomologicalComplex.homotopyEquivalences (StalkModuleCat X x) (ComplexShape.up ℕ)
      (((SheafOfModules.stalkFunctor (structureSheafRing X) x).mapHomologicalComplex
        (ComplexShape.up ℕ)).map ((godementAugmentation X).app F))
```

**`AlgebraicGeometry.GodementResolution.quasiIso_godementAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/StalkHomotopy.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GodementResolution/StalkHomotopy.lean#L558). The attribute's comment: “exactness of the augmented complex 0 → F → f_* f^* F → ⋯”. References: SGA 4 XVII (4.2.3), “(ii)”; SGA 4 XVII (4.2), “augmented exactness”.

> **Clause (3) of [Stacks, Tag 0FKS]: the augmented Godement complex is exact.** The
> augmentation `F[0] ⟶ G(F)` is a quasi-isomorphism, so
> `0 → F → f_* f^* F → f_* f^* f_* f^* F → ⋯` is exact and the Godement complex is a flasque
> resolution of `F`.
>
> Quasi-isomorphy is detected on stalks (`quasiIso_of_forall_stalk_quasiIso_nat`), and on each
> stalk the augmentation is a homotopy equivalence by
> `homotopyEquivalences_stalk_godementAugmentation`, hence a quasi-isomorphism.

```lean
theorem quasiIso_godementAugmentation (F : SheafOfModules.{u} (structureSheafRing X)) :
    QuasiIso ((godementAugmentation X).app F)
```

## Tag 0FKT, a lemma

[Tag 0FKT](https://stacks.math.columbia.edu/tag/0FKT) in the Stacks Project.

**`AlgebraicGeometry.GodementResolution.exists_quasiIso_boundedBelow_isFlasque_isHomotopyEquiv_stalk_godement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/GodementBoundedBelowResolution.lean, line 1223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/GodementBoundedBelowResolution.lean#L1223). The attribute's comment: “Godement resolution; all four clauses, including the stalkwise homotopy equivalence”.

> **[Stacks, Tag 0FKT], all four clauses, for the Godement resolution.** For a bounded below
> complex `F` of `𝒪_X`-modules there is a quasi-isomorphism `F ⟶ G` with `G` bounded below in the
> same degree, every term of `G` flasque, and, for every `x ∈ X`, the stalk map `F_x ⟶ G_x` a
> homotopy equivalence of complexes of `𝒪_{X,x}`-modules. The map is `godementComparisonMap` onto
> the totalisation of the Godement double complex of `F`.

```lean
theorem exists_quasiIso_boundedBelow_isFlasque_isHomotopyEquiv_stalk_godement
    (hF : ∃ n : ℤ, F.IsStrictlyGE n) :
    ∃ (G : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ) (f : F ⟶ G),
      QuasiIso f ∧ (∃ n : ℤ, G.IsStrictlyGE n) ∧
        (∀ i : ℤ, TopCat.Sheaf.IsFlasque
          ((SheafOfModules.toSheaf (structureSheafRing X)).obj (G.X i))) ∧
        (∀ x : X, ∃ e : HomotopyEquiv ((stalkComplexFunctor X x).obj F)
            ((stalkComplexFunctor X x).obj G), e.hom = (stalkComplexFunctor X x).map f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.30, Tag 0FKR](https://stacks.math.columbia.edu/tag/0FKR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
