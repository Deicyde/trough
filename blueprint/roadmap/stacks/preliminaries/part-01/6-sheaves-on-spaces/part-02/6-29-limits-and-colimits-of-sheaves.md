---
declaration: section
origin: cited
lean: DirectedColimitOfSheaves.canonicalMap, DirectedColimitOfSheaves.injective_canonicalMap_of_hasInjectiveTransitions, DirectedColimitOfSheaves.injective_canonicalMap_of_isCompact, DirectedColimitOfSheaves.bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions, DirectedColimitOfSheaves.bijective_canonicalMap_of_hasFiniteCompactCofinalCovers, DirectedColimitOfSheaves.QuasiCompactCounterexample.compactSpace_and_canonicalMap_top_injective_not_surjective, SpectralDiagram.canonicalMap, SpectralDiagram.bijective_canonicalMap
statement: formalized
proof: formalized
---

# 6.29 Limits and colimits of sheaves

Section 6.29 of the Stacks Project, [Tag 009E](https://stacks.math.columbia.edu/tag/009E). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 009F, a lemma

[Tag 009F](https://stacks.math.columbia.edu/tag/009F) in the Stacks Project.

**`DirectedColimitOfSheaves.canonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L139).

> The canonical map `Ψ : colimᵢ ℱᵢ(U) ⟶ (colimᵢ ℱᵢ)(U)`, namely the component at `U` of the
> unit `ℱ' ⟶ (ℱ')^#` of sheafification.

```lean
noncomputable def canonicalMap (U : Opens X) :
    (colimitPresheaf F).obj (op U) ⟶ (colimitSheaf F).obj.obj (op U)
```

**`DirectedColimitOfSheaves.injective_canonicalMap_of_hasInjectiveTransitions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L417).

> If all the transition maps are injective, then `Ψ` is injective for any open `U`.

```lean
theorem injective_canonicalMap_of_hasInjectiveTransitions
    (hInj : HasInjectiveTransitions F) (U : Opens X) :
    Function.Injective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.injective_canonicalMap_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L438).

> If `U` is quasi-compact, then `Ψ` is injective, with no hypothesis on the transition
> maps.

```lean
theorem injective_canonicalMap_of_isCompact (U : Opens X)
    (hU : IsCompact (U : Set X)) :
    Function.Injective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L452).

> If `U` is quasi-compact and all the transition maps are injective, then `Ψ` is
> bijective.

```lean
theorem bijective_canonicalMap_of_isCompact_of_hasInjectiveTransitions
    (hInj : HasInjectiveTransitions F) (U : Opens X)
    (hU : IsCompact (U : Set X)) :
    Function.Bijective (canonicalMap F U)
```

**`DirectedColimitOfSheaves.bijective_canonicalMap_of_hasFiniteCompactCofinalCovers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/FilteredColimitSections.lean#L466). References: SGA 4 VI (1.23), “topological space case”.

> If `U` has a cofinal system of finite open coverings whose pairwise intersections are
> quasi-compact, then `Ψ` is bijective, with no hypothesis on the transition maps.

```lean
theorem bijective_canonicalMap_of_hasFiniteCompactCofinalCovers (U : Opens X)
    (hU : HasFiniteCompactCofinalCovers (X := X) U) :
    Function.Bijective (canonicalMap F U)
```

## Tag 009G, an example

[Tag 009G](https://stacks.math.columbia.edu/tag/009G) in the Stacks Project.

**`DirectedColimitOfSheaves.QuasiCompactCounterexample.compactSpace_and_canonicalMap_top_injective_not_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/ColimitSectionsCounterexample.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/ColimitSectionsCounterexample.lean#L721). The attribute's comment: “The example itself: the space `{s₁, s₂, ξ₁, ξ₂, …}`, the system `jₙ,* 𝐙` as sheaves of sets, quasi-compactness of the space, injectivity and non-surjectivity of `Ψ` on global sections, `colimₙ Γ(X, ℱₙ) = M`, `Γ(X, ℱ) = M ⊕ M` with `Ψ` the diagonal, the stalks of `ℱ`, and `ℱ` as the sum of the two skyscraper sheaves.”.

> **Stacks 009G.**  Let `X = {s₁, s₂, ξ₁, ξ₂, …}`, where a subset is open if it contains all
> of the `ξᵢ` as soon as it contains `s₁` or `s₂`; let `Uₙ = {ξₙ, ξₙ₊₁, …}` and `ℱₙ = jₙ,* 𝐙`
> (`sheafSystem`; `sheafSystemObjIso` identifies `ℱₙ` with the pushforward of the constant sheaf),
> with the restriction maps as transition maps, and let `ℱ = colimₙ ℱₙ`.  Then:
>
> * `X` is quasi-compact;
> * the canonical map `Ψ : colimₙ Γ(X, ℱₙ) → Γ(X, ℱ)` of 009F is injective but not surjective;
> * with `M = colimₙ ∏_{m ≥ n} 𝐙` (`tailColimit`), `colimₙ Γ(X, ℱₙ) = M` and `Γ(X, ℱ) = M ⊕ M`,
>   and under these identifications `Ψ` is the diagonal;
> * the stalk of `ℱ` is zero at every `ξₙ` and is `M` at `s₁` and at `s₂`;
> * `ℱ` is the direct sum of the skyscraper sheaves with value `M` at `s₁` and `s₂`: the maps
>   `toSkyscraper i` to Mathlib's `skyscraperPresheaf (s i) M` identify `ℱ(U)` with the product
>   of their sections over `U`, for every open `U`.
>
> So some condition is necessary in 009F (4), even for a quasi-compact open.  The sheaves are
> sheaves of sets, the setting of 009F in this library, so the direct sum `M ⊕ M` is the product
> set `M × M`, and the zero stalk is a one-point set; the points `ξ` are numbered from `0`.

```lean
theorem compactSpace_and_canonicalMap_top_injective_not_surjective :
    CompactSpace space ∧
      Function.Injective (canonicalMap sheafSystem ⊤) ∧
      ¬ Function.Surjective (canonicalMap sheafSystem ⊤) ∧
      (∃ (e : (colimitPresheaf sheafSystem).obj (op ⊤) ≃ tailColimit)
        (e' : (colimitSheaf sheafSystem).obj.obj (op ⊤) ≃ tailColimit × tailColimit),
        ∀ t, e' (canonicalMap sheafSystem ⊤ t) = (e t, e t)) ∧
      (∀ n, Subsingleton ((colimitSheaf sheafSystem).presheaf.stalk (Point.ξ n))) ∧
      (∀ i, Nonempty ((colimitSheaf sheafSystem).presheaf.stalk (Point.s i) ≃ tailColimit)) ∧
      ∀ U : Opens space, Function.Bijective fun σ : (colimitSheaf sheafSystem).obj.obj (op U) =>
        ((toSkyscraper true).app (op U) σ, (toSkyscraper false).app (op U) σ)
```

## Tag 0A32, a lemma

[Tag 0A32](https://stacks.math.columbia.edu/tag/0A32) in the Stacks Project.

**`SpectralDiagram.canonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean#L199). The attribute's comment: “the canonical map”.

> The canonical map `colim_{a : j → i} (f_a⁻¹𝒢)(f_a⁻¹ U) → (p_i⁻¹𝒢)(p_i⁻¹ U)`, induced by pulling
> sections back to the limit along the projections.

```lean
def canonicalMap [UnivLE.{max v v', max v u}] :
    colimit (D.sliceFunctor U 𝒢) ⟶ (D.sliceCocone U 𝒢).pt
```

**`SpectralDiagram.bijective_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/PullbackSections.lean#L749). The attribute's comment: “bijectivity of the canonical map”.

> For `i` an object of the cofiltered index category, `𝒢` a sheaf of sets on `X_i` and `U ⊆ X_i`
> a quasi-compact open, the canonical map `colim_{a : j → i} (f_a⁻¹𝒢)(f_a⁻¹ U) → (p_i⁻¹𝒢)(p_i⁻¹ U)`
> is bijective.

```lean
theorem bijective_canonicalMap [UnivLE.{max v v', max v u}] (hU : IsCompact (U : Set (D.F.obj i))) :
    Function.Bijective (D.canonicalMap U 𝒢)
```

## Tag 0A33, a lemma

[Tag 0A33](https://stacks.math.columbia.edu/tag/0A33) in the Stacks Project.

**`SpectralSheafSystem.stageColimitMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean#L680). The attribute's comment: “the canonical map”.

> **The canonical map of Stacks 0A33**, `colim_{a : j → i} F_j(f_a⁻¹U) → F(p_i⁻¹U)`.

```lean
def stageColimitMap [UnivLE.{max v v', max v u}] : colimit (S.stageFunctor U) ⟶
    (S.colimitPullback).obj.obj (op (S.diagram.comapProj i U))
```

**`SpectralSheafSystem.bijective_stageColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Limits/DescendOpens.lean#L1012).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
