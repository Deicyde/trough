---
declaration: section
origin: cited
lean: TopCat.Presheaf.IsFlasque, CategoryTheory.epi_iff_surjective, Stacks.Cohomology.isFlasque_of_injective_module, Stacks.Cohomology.FlasqueAcyclic.rightAcyclic_evaluation_of_isFlasque, Stacks.Cohomology.FlasqueCech.isZero_cechComplex_homology_of_isFlasque, Stacks.Cohomology.FlasquePushforward.isZero_rightDerivedPlus_modulePushforward_of_isFlasque, Stacks.Cohomology.RaviCech.isZero_cechCohomology_of_surjective_restrictions
statement: formalized
proof: formalized
---

# 20.12 Flasque sheaves

Section 20.12 of the Stacks Project, [Tag 09SV](https://stacks.math.columbia.edu/tag/09SV). 6 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09SW, a definition

[Tag 09SW](https://stacks.math.columbia.edu/tag/09SW) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.IsFlasque`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsFlasque#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch20.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch20.lean#L45) (StacksFrontier): “flasque presheaf: every restriction map is an epimorphism (for presheaves in any category)”.
- [`CategoryTheory.epi_iff_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.epi_iff_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch20.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch20.lean#L47) (StacksFrontier): “for presheaves of sets, an epimorphism is a surjection”.

## Tag 09SX, a lemma

[Tag 09SX](https://stacks.math.columbia.edu/tag/09SX) in the Stacks Project.

**`Stacks.Cohomology.isFlasque_of_injective_module`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveFlasqueModules.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveFlasqueModules.lean#L158). References: EGA 0 (12.2.1), “partial”; SGA 4 V (4.10), “2), F=A, ringed space”.

> **Stacks Project, Tag 09SX.** An injective sheaf of modules on a ringed space is flasque,
> stated with Mathlib's `TopCat.Presheaf.IsFlasque` for the underlying sheaf of abelian groups.
> This is the reformulation of Tag 01EA.

```lean
instance isFlasque_of_injective_module
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{v})
    (I : SheafOfModules.{w} R) [Injective I] :
    TopCat.Presheaf.IsFlasque (X := TopCat.of X) ((SheafOfModules.toSheaf R).obj I).obj
```

## Tag 09SY, a lemma

[Tag 09SY](https://stacks.math.columbia.edu/tag/09SY) in the Stacks Project.

**`Stacks.Cohomology.FlasqueAcyclic.rightAcyclic_evaluation_of_isFlasque`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasqueModulesAreAcyclic.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasqueModulesAreAcyclic.lean#L76). References: SGA 4 V (4.6), “special case”.

> **Stacks 09SY.** A flasque sheaf of modules is acyclic for the derived sections functor
> on every open subset. Taking `U = ⊤` gives acyclicity for global sections.

```lean
public lemma rightAcyclic_evaluation_of_isFlasque
    (hF : TopCat.Presheaf.IsFlasque (X := TopCat.of X)
      ((SheafOfModules.toSheaf R).obj F).obj) :
    (SheafOfModules.evaluation R (op U)).rightAcyclic F
```

## Tag 09SZ, a lemma

[Tag 09SZ](https://stacks.math.columbia.edu/tag/09SZ) in the Stacks Project.

**`Stacks.Cohomology.FlasqueCech.isZero_cechComplex_homology_of_isFlasque`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasqueCechVanishing.lean, line 776](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasqueCechVanishing.lean#L776).

> **Stacks 09SZ.** A flasque sheaf has zero Čech cohomology in every positive degree.

```lean
public lemma isZero_cechComplex_homology_of_isFlasque
    {X : TopCat.{u}} {ι : Type v} (F : TopCat.Sheaf AddCommGrpCat.{v} X)
    (V : Opens X) (U : ι → Opens X) (hU : V = ⨆ i, U i) [F.IsFlasque]
    (p : ℕ) (hp : 0 < p) :
    IsZero (((cechComplexFunctor U).obj F.obj).homology p)
```

## Tag 09T0, a lemma

[Tag 09T0](https://stacks.math.columbia.edu/tag/09T0) in the Stacks Project.

**`Stacks.Cohomology.FlasquePushforward.isZero_rightDerivedPlus_modulePushforward_of_isFlasque`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasquePushforwardVanishing.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/FlasquePushforwardVanishing.lean#L220). References: SGA 4 V (5.2), “special case”.

> A flasque sheaf of modules has vanishing positive higher direct images under any
> morphism of ringed spaces.

```lean
public lemma isZero_rightDerivedPlus_modulePushforward_of_isFlasque
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (F : SheafOfModules.{u} (structureSheafRing X))
    [TopCat.Sheaf.IsFlasque ((SheafOfModules.toSheaf _).obj F)]
    (p : ℤ) (hp : 0 < p) :
    IsZero (((RingedSpaceModuleAdjunction.modulePushforward f).rightDerivedPlus p).obj F)
```

## Tag 0A36, a lemma

[Tag 0A36](https://stacks.math.columbia.edu/tag/0A36) in the Stacks Project.

**`Stacks.Cohomology.RaviCech.isZero_cechCohomology_of_surjective_restrictions`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/VanishingFromSurjectiveRestrictions.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/VanishingFromSurjectiveRestrictions.lean#L206).

> If restriction from the covered open to every union of nonempty finite intersections of
> members of the cover is surjective, then the positive-degree Čech cohomology of the cover
> vanishes.

```lean
lemma isZero_cechCohomology_of_surjective_restrictions
    (U₀ : Opens X) (hcover : U₀ = ⨆ i, U i)
    (hres : ∀ (V : Opens X) (hVU : V ≤ U₀),
      (∃ S : Set (Finset ι), (∀ s ∈ S, s.Nonempty) ∧
        V = ⨆ s : S, ⨅ i : (s : Finset ι), U i) →
      Function.Surjective (F.obj.map (homOfLE hVU).op))
    (p : ℕ) (hp : 0 < p) :
    IsZero
      (((CategoryTheory.cechComplexFunctor (A := AddCommGrpCat.{v}) U).obj F.obj).homology p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.12, Tag 09SV](https://stacks.math.columbia.edu/tag/09SV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
