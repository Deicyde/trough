---
declaration: section
origin: cited
lean: DirectedColimitOfSheaves.canonicalMap, DirectedColimitOfSheaves.injective_canonicalMap_of_hasInjectiveTransitions, DirectedColimitOfSheaves.injective_canonicalMap_of_isCompact, DirectedColimitOfSheaves.bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions, DirectedColimitOfSheaves.bijective_canonicalMap_of_hasFiniteCompactCofinalCovers, DirectedColimitOfSheaves.exists_system_canonicalMap_not_bijective, SpectralDiagram.canonicalMap, SpectralDiagram.bijective_canonicalMap
statement: formalized
proof: formalized
---

# 6.29 Limits and colimits of sheaves

Section 6.29 of the Stacks Project, [Tag 009E](https://stacks.math.columbia.edu/tag/009E). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 009F, a lemma

[Tag 009F](https://stacks.math.columbia.edu/tag/009F) in the Stacks Project.

**`DirectedColimitOfSheaves.canonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L139).

> The canonical map `Ψ : colimᵢ ℱᵢ(U) ⟶ (colimᵢ ℱᵢ)(U)`, namely the component at `U` of the
> unit `ℱ' ⟶ (ℱ')^#` of sheafification.

```lean
noncomputable def canonicalMap (U : Opens X) :
    (colimitPresheaf F).obj (op U) ⟶ (colimitSheaf F).obj.obj (op U)
```

**`DirectedColimitOfSheaves.injective_canonicalMap_of_hasInjectiveTransitions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L417).

> If all the transition maps are injective, then `Ψ` is injective for any open `U`.

```lean
theorem injective_canonicalMap_of_hasInjectiveTransitions
    (hInj : HasInjectiveTransitions F) (U : Opens X) :
    Function.Injective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.injective_canonicalMap_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L438).

> If `U` is quasi-compact, then `Ψ` is injective, with no hypothesis on the transition
> maps.

```lean
theorem injective_canonicalMap_of_isCompact (U : Opens X)
    (hU : IsCompact (U : Set X)) :
    Function.Injective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L452).

> If `U` is quasi-compact and all the transition maps are injective, then `Ψ` is
> bijective.

```lean
theorem bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions
    (hInj : HasInjectiveTransitions F) (U : Opens X)
    (hU : IsCompact (U : Set X)) :
    Function.Bijective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.bijective_canonicalMap_of_hasFiniteCompactCofinalCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L466). References: SGA 4 VI (1.23), “topological space case”.

> If `U` has a cofinal system of finite open coverings whose pairwise intersections are
> quasi-compact, then `Ψ` is bijective, with no hypothesis on the transition maps.

```lean
theorem bijective_canonicalMap_of_hasFiniteCompactCofinalCovers (U : Opens X)
    (hU : HasFiniteCompactCofinalCovers (X := X) U) :
    Function.Bijective (canonicalMap F U)
```

## Tag 009G, an example

[Tag 009G](https://stacks.math.columbia.edu/tag/009G) in the Stacks Project.

**`DirectedColimitOfSheaves.exists_system_canonicalMap_not_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/ColimitSectionsCounterexample.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/ColimitSectionsCounterexample.lean#L162).

> **Stacks 009G.**  Some hypothesis is necessary in part (4) of 009F: there are a space `X`
> and a system of sheaves of sets `ℱ : ℕ ⥤ TopCat.Sheaf (Type) X` indexed by the directed set
> `ℕ` for which the canonical map `Ψ : colimₙ ℱₙ(X) → (colimₙ ℱₙ)(X)` is not bijective.
>
> The witness is `SectionsCounterexample.sheafSystem`, the pushforwards `jₙ,*𝐙` of the constant
> sheaf along the inclusions of the cofinal subsets `{m : n ≤ m}` of the discrete space `ℕ`.  All
> its stalks die in the colimit while its global sections do not, so `Ψ` is not injective; and
> `SectionsCounterexample.not_hasFiniteCompactCofinalCovers_top` checks that the hypothesis of
> 009F (4) really fails here.

```lean
theorem exists_system_canonicalMap_not_bijective :
    ∃ (X : TopCat) (F : ℕ ⥤ TopCat.Sheaf (Type) X),
      ¬ Function.Bijective (canonicalMap F ⊤)
```

## Tag 0A32, a lemma

[Tag 0A32](https://stacks.math.columbia.edu/tag/0A32) in the Stacks Project.

**`SpectralDiagram.canonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean#L199). The attribute's comment: “the canonical map”.

> The canonical map `colim_{a : j → i} (f_a⁻¹𝒢)(f_a⁻¹ U) → (p_i⁻¹𝒢)(p_i⁻¹ U)`, induced by pulling
> sections back to the limit along the projections.

```lean
def canonicalMap [UnivLE.{max v v', max v u}] :
    colimit (D.sliceFunctor U 𝒢) ⟶ (D.sliceCocone U 𝒢).pt
```

**`SpectralDiagram.bijective_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean#L749). The attribute's comment: “bijectivity of the canonical map”.

> For `i` an object of the cofiltered index category, `𝒢` a sheaf of sets on `X_i` and `U ⊆ X_i`
> a quasi-compact open, the canonical map `colim_{a : j → i} (f_a⁻¹𝒢)(f_a⁻¹ U) → (p_i⁻¹𝒢)(p_i⁻¹ U)`
> is bijective.

```lean
theorem bijective_canonicalMap [UnivLE.{max v v', max v u}] (hU : IsCompact (U : Set (D.F.obj i))) :
    Function.Bijective (D.canonicalMap U 𝒢)
```

## Tag 0A33, a lemma

[Tag 0A33](https://stacks.math.columbia.edu/tag/0A33) in the Stacks Project.

**`SpectralSheafSystem.stageColimitMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean#L680). The attribute's comment: “the canonical map”.

> **The canonical map of Stacks 0A33**, `colim_{a : j → i} F_j(f_a⁻¹U) → F(p_i⁻¹U)`.

```lean
def stageColimitMap [UnivLE.{max v v', max v u}] : colimit (S.stageFunctor U) ⟶
    (S.colimitPullback).obj.obj (op (S.diagram.comapProj i U))
```

**`SpectralSheafSystem.bijective_stageColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean#L1012).

> **Stacks 0A33.**  Let `J` be a cofiltered index category, `j ↦ X_j` a diagram of spectral
> spaces with spectral transition maps, `F_j` a sheaf of sets on `X_j` for each `j` together with a
> compatible system of `f_a`-maps, and `F = colim_j p_j⁻¹F_j` on the limit `X = lim_j X_j`.  Then for
> every `i` and every quasi-compact open `U ⊆ X_i` the canonical map
> `colim_{a : j → i} F_j(f_a⁻¹U) → F(p_i⁻¹U)`
> is bijective.

```lean
theorem bijective_stageColimitMap [UnivLE.{max v v', max v u}]
    (hU : IsCompact (U : Set (S.diagram.F.obj i))) :
    Function.Bijective (S.stageColimitMap U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.29, Tag 009E](https://stacks.math.columbia.edu/tag/009E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
