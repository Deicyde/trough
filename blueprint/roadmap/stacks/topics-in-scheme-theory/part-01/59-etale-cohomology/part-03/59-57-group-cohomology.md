---
declaration: section
origin: cited
lean: Stacks.GroupCohomology.ofRepresentation, Stacks.GroupCohomology.homEquiv, Stacks.GroupCohomology.ofDistribMulAction, Stacks.GroupCohomology.gModuleHomEquiv, Stacks.Injectives.ContinuousModule, continuousGroupCohomologyFunctor, continuousGroupCohomology, Stacks.ContinuousCohomology.continuousModuleCohomologyForgetIso
statement: formalized
proof: formalized
---

# 59.57 Group cohomology

Section 59.57 of the Stacks Project, [Tag 0A2H](https://stacks.math.columbia.edu/tag/0A2H). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04JP, a definition

[Tag 04JP](https://stacks.math.columbia.edu/tag/04JP) in the Stacks Project.

**`Stacks.GroupCohomology.ofRepresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean#L100). The attribute's comment: “R-G-modules”.

> **Stacks Project, Tag 04JP.** An `R`-`G`-module: an `R`-module `M` together with a left
> action of `G` on `M` by `R`-linear maps which is continuous when `M` is given the discrete
> topology.

```lean
def ofRepresentation (ρ : Representation R G M)
    (h : (actionOfRepresentation R G M ρ).IsContinuous) :
    Stacks.Injectives.ContinuousModule.{u, v, w} R G
```

**`Stacks.GroupCohomology.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean#L132). The attribute's comment: “morphisms of R-G-modules”.

> **Stacks Project, Tag 04JP.** A morphism of `R`-`G`-modules is a `G`-equivariant `R`-module
> map.

```lean
def homEquiv (X Y : Stacks.Injectives.ContinuousModule.{u, v, w} R G) :
    (X ⟶ Y) ≃ {f : X.obj.obj.V →ₗ[R] Y.obj.obj.V // ∀ (g : G) (x : X.obj.obj.V),
      f ((X.obj.obj.ρ g).asHom.hom x) = (Y.obj.obj.ρ g).asHom.hom (f x)}
```

**`Stacks.GroupCohomology.ofDistribMulAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean#L181). The attribute's comment: “G-modules”.

> **Stacks Project, Tag 04JP.** A `G`-module, or discrete `G`-module: an abelian group `M`
> together with a left action of `G` on `M` by group homomorphisms which is continuous when `M` is
> given the discrete topology.

```lean
def ofDistribMulAction (h : (actionOfDistribMulAction G M).IsContinuous) :
    Stacks.Injectives.ContinuousModule.{0, v, w} ℤ G
```

**`Stacks.GroupCohomology.gModuleHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean#L194). The attribute's comment: “morphisms of G-modules”.

> **Stacks Project, Tag 04JP.** A morphism of `G`-modules is a `G`-equivariant homomorphism of
> abelian groups.

```lean
def gModuleHomEquiv (X Y : Stacks.Injectives.ContinuousModule.{0, v, w} ℤ G) :
    (X ⟶ Y) ≃ {f : X.obj.obj.V →+ Y.obj.obj.V // ∀ (g : G) (x : X.obj.obj.V),
      f ((X.obj.obj.ρ g).asHom.hom x) = (Y.obj.obj.ρ g).asHom.hom (f x)}
```

Declarations registered for the tag:

- [`Stacks.Injectives.ContinuousModule`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/ContinuousGroupModules.lean#L643), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/DiscreteModules.lean#L214) (StacksFrontier): “the categories Mod\_G and Mod\_\{R,G}”.

## Tag 04JR, a definition

[Tag 04JR](https://stacks.math.columbia.edu/tag/04JR) in the Stacks Project.

**`continuousGroupCohomologyFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Continuous.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Continuous.lean#L205). The attribute's comment: “the cohomology functors”.

> The `i`-th continuous group cohomology functor, namely the `i`-th right
> derived functor of taking invariants.

```lean
abbrev continuousGroupCohomologyFunctor [IsTopologicalGroup G]
    (i : ℕ) : ContinuousGModule.{u, max u v} G ⥤ AddCommGrpCat.{max u v}
```

**`continuousGroupCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Continuous.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Continuous.lean#L213). The attribute's comment: “the cohomology groups”.

> The continuous group cohomology group `Hⁱ(G, M)`. For discrete groups this
> is group cohomology, and for Galois groups it is Galois cohomology. When
> `G = Gal(Kˢᵉᵖ/K)`, it is also denoted `Hⁱ(K, M)`.

```lean
abbrev continuousGroupCohomology [IsTopologicalGroup G]
    (i : ℕ) (M : ContinuousGModule.{u, max u v} G) : AddCommGrpCat.{max u v}
```

## Tag 0DVD, a lemma

[Tag 0DVD](https://stacks.math.columbia.edu/tag/0DVD) in the Stacks Project.

**`Stacks.ContinuousCohomology.continuousModuleCohomologyForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ContinuousCohomology/ForgetCoefficients.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ContinuousCohomology/ForgetCoefficients.lean#L688).

> Continuous group cohomology of continuous discrete `R`-`G`-modules commutes, naturally in the
> module, with forgetting the `R`-module structure.

```lean
def continuousModuleCohomologyForgetIso [IsTopologicalGroup G]
    [HasDerivedCategory.{d} (Stacks.Injectives.ContinuousModule.{u, v, max u v w} R G)]
    [HasDerivedCategory.{d} (ModuleCat.{max u v w} R)] (i : ℕ) :
    cohomologyFunctor.{d, u, v, w} R G i ⋙
        forget₂ (ModuleCat.{max u v w} R) AddCommGrpCat.{max u v w} ≅
      continuousModuleForget.{u, v, max u v w} R G ⋙
        continuousGroupCohomologyFunctor.{v, max u v w} G i
```

## Tag 0DVE, a lemma

[Tag 0DVE](https://stacks.math.columbia.edu/tag/0DVE) in the Stacks Project.

**`Stacks.ContinuousCohomology.extIsoCohomologyDualTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ContinuousCohomology/ExtComparison.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ContinuousCohomology/ExtComparison.lean#L425). The attribute's comment: “R-linear, in every degree; the `Ext`-universe smallness (hasExt\_continuousModule) and themodel of the derived category are free instance arguments”.

> Let `G` be a topological group, `R` a commutative ring and `M`, `N` continuous discrete
> `R`-`G`-modules. If `M` is finite projective as an `R`-module, then `Extⁱ(M, N)`, computed in the
> category of continuous discrete `R`-`G`-modules, is the continuous group cohomology
> `Hⁱ(G, Mᵛ ⊗_R N)` of the diagonal action on `Mᵛ ⊗_R N`, `R`-linearly and in every degree.

```lean
def extIsoCohomologyDualTensor
    [HasDerivedCategory.{d} (Stacks.Injectives.ContinuousModule.{u, v, max u v w} R G)]
    [HasDerivedCategory.{d} (ModuleCat.{max u v w} R)]
    (N : Stacks.Injectives.ContinuousModule.{u, v, max u v w} R G) (i : ℕ) :
    Ext.{max u v w} M N i ≃ₗ[R]
      (cohomologyFunctor.{d, u, v, w} R G i).obj
        (dualTensorContinuousModule.{u, v, max u v w} R G M N)
```

## Tag 0DVF, a lemma

[Tag 0DVF](https://stacks.math.columbia.edu/tag/0DVF) in the Stacks Project.

**`Stacks.ContinuousCohomology.finite_cohomologyFunctor_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ContinuousCohomology/FiniteDimensionalDegreeOne.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ContinuousCohomology/FiniteDimensionalDegreeOne.lean#L496).

> Let `G` be a topological group, `k` a field and `V` a `k`-`G`-module, that is a `k`-module with
> a continuous action of `G` for the discrete topology on `V`. If `G` is topologically finitely
> generated, so that some finite subset generates a dense subgroup, and `V` is finite dimensional
> over `k`, then the first continuous cohomology group `H¹(G, V)` is finite dimensional over `k`.

```lean
theorem finite_cohomologyFunctor_one
    (hG : ∃ S : Finset G, Dense ((Subgroup.closure (S : Set G) : Subgroup G) : Set G))
    (V : Stacks.Injectives.ContinuousModule.{u, v, max u v w} k G)
    [Module.Finite k V.obj.obj.V] :
    Module.Finite k ((cohomologyFunctor.{d, u, v, w} k G 1).obj V)
```

## Tag 0DV3, a lemma

[Tag 0DV3](https://stacks.math.columbia.edu/tag/0DV3) in the Stacks Project.

**`continuousGroupCohomology_isTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Profinite.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Profinite.lean#L449). The attribute's comment: “part (1)”.

> Positive-degree continuous cohomology of a profinite group with discrete
> coefficients is a torsion abelian group.

```lean
public theorem continuousGroupCohomology_isTorsion
    (hG : Stacks.Chapter05.Tag_0BR1.IsProfiniteTop G) (i : ℕ) (hi : 0 < i)
    (M : ContinuousGModule.{u, max u v} G) :
    Module.IsTorsion ℤ (continuousGroupCohomology G i M)
```

**`isZero_continuousGroupCohomology_of_module_rat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Profinite.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/Profinite.lean#L458). The attribute's comment: “part (2)”.

> Positive-degree continuous cohomology of a profinite group vanishes when
> the discrete coefficient module is a rational vector space.

```lean
public theorem isZero_continuousGroupCohomology_of_module_rat
    (hG : Stacks.Chapter05.Tag_0BR1.IsProfiniteTop G) (i : ℕ) (hi : 0 < i)
    (M : ContinuousGModule.{u, max u v} G) [Module ℚ M.1.1.V] :
    IsZero (continuousGroupCohomology G i M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.57, Tag 0A2H](https://stacks.math.columbia.edu/tag/0A2H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
