---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_eventually_constant_quasicoherentSubobjects, AlgebraicGeometry.Space.exists_idealPowSmul_eq_bot_iff_supportOfSheaf_subset_idealZeroLocus, AlgebraicGeometry.Space.exists_idealPowSmul_inf_eq, AlgebraicGeometry.Space.canonicalMapToHomRestrict_bijective, AlgebraicGeometry.Space.canonicalMapToSections_bijective, AlgebraicGeometry.Space.idealPowHomRestrict
statement: formalized
proof: formalized
---

# 69.13 Coherent sheaves on Noetherian spaces

Section 69.13 of the Stacks Project, [Tag 07UI](https://stacks.math.columbia.edu/tag/07UI). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07UJ, a lemma

[Tag 07UJ](https://stacks.math.columbia.edu/tag/07UJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_eventually_constant_quasicoherentSubobjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAscendingChain.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAscendingChain.lean#L311).

> **Stacks 07UJ.** The ascending chain condition holds for the quasi-coherent submodules of a
> coherent module on a Noetherian algebraic space: an ascending sequence of quasi-coherent subobjects
> of a coherent `𝒪_F`-module is eventually constant.

```lean
theorem exists_eventually_constant_quasicoherentSubobjects
    (hZ : B.Contains (⊤_ Scheme.{u})) (hN : IsNoetherian B S hS hZ F)
    (M : Modules.{u, u} B S hS F hF) (hM : IsCoherent B S hS F hF M)
    (G : ℕ → Subobject M)
    (hG : ∀ n, SheafOfModules.IsQuasicoherentOnSite (G n : Modules.{u, u} B S hS F hF))
    (hmono : Monotone G) :
    ∃ n, ∀ k, n ≤ k → G k = G n
```

## Tag 07UK, a lemma

[Tag 07UK](https://stacks.math.columbia.edu/tag/07UK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_idealPowSmul_eq_bot_iff_supportOfSheaf_subset_idealZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealPowerSupport.lean, line 811](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealPowerSupport.lean#L811). References: EGA I (9.3.4), “more general”.

> **Stacks 07UK.** Let `X` be a Noetherian algebraic space over a scheme `S`, let `F` be a
> coherent `𝒪_X`-module and let `ℐ ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals, cutting out the
> closed subspace `Z ⊆ X`.  Then `ℐⁿ F = 0` for some `n ≥ 0` if and only if the support of `F` is
> contained in `Z`, set theoretically.
>
> The closed subspace enters only through its point set `|V(ℐ)|`, which is what the set-theoretic
> containment refers to.  For the forward implication no finiteness is needed: over a chart on
> which `ℐ` is the whole structure sheaf, and over every chart below it, `F` has no sections at
> all, so the support misses the image of that chart.  The converse is the substantial half: on a
> surjective affine chart with Noetherian ring of sections, which a Noetherian algebraic space has,
> the sections of `F` form a finite module annihilated by a power of each section of `ℐ`, hence by
> a power of `ℐ(U)` because the ring is Noetherian; and quasi-coherence carries that single
> annihilation to every chart.

```lean
theorem exists_idealPowSmul_eq_bot_iff_supportOfSheaf_subset_idealZeroLocus
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hN : IsNoetherian B S hS hZ X.1)
    (M : Modules.{u, u} B S hS X.1 X.2) (hM : IsCoherent B S hS X.1 X.2 M)
    (I : (SheafOfModules.unit (structureRingSheaf B S hS X)).Submodule)
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite) :
    (∃ n : ℕ, Stacks.Sites.idealSmul (M := M)
        (Stacks.Sites.idealPow (O := (smallEtaleRingedSite B S hS X.1 X.2).O) I n) ⊤ = ⊥) ↔
      supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj M) ⊆
        idealZeroLocus B S hS X I
```

## Tag 07UL, a lemma

[Tag 07UL](https://stacks.math.columbia.edu/tag/07UL) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_idealPowSmul_inf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentArtinRees.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentArtinRees.lean#L510).

> Artin-Rees for a quasi-coherent submodule `G` of a coherent module `M` and a quasi-coherent
> sheaf of ideals `I` on a Noetherian algebraic space: there is a `c ≥ 0` with
> `I ⁿ⁻ᶜ (I ᶜ M ⊓ G) = I ⁿ M ⊓ G` for every `n ≥ c`.

```lean
theorem exists_idealPowSmul_inf_eq (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ F) (M : Modules.{u, u} B S hS F hF)
    (hM : IsCoherent B S hS F hF M) (G : M.Submodule)
    (hG : G.toSheafOfModules.IsQuasicoherentOnSite) (I : IdealSheaves B S hS F hF)
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite) :
    ∃ c : ℕ, ∀ n : ℕ, c ≤ n →
      Stacks.Sites.idealPowSmul I (n - c) (idealPowSubmodule I c M ⊓ G)
        = idealPowSubmodule I n M ⊓ G
```

## Tag 07UM, a lemma

[Tag 07UM](https://stacks.math.columbia.edu/tag/07UM) in the Stacks Project.

**`AlgebraicGeometry.Space.canonicalMapToHomRestrict_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentHomColimitBijective.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentHomColimitBijective.lean#L84). The attribute's comment: “first display”.

> **[Stacks, Tag 07UM], first display.**  For a Noetherian algebraic space `X` over `S`, a
> quasi-coherent sheaf of ideals `ℐ` with open complement `U = X ∖ V(ℐ)`, a coherent `𝒪_X`-module
> `𝒢` and a quasi-coherent `𝒪_X`-module `ℱ`, the canonical map
>
> `colim_n Hom_{𝒪_X}(ℐⁿ 𝒢, ℱ) ⟶ Hom_{𝒪_U}(𝒢|_U, ℱ|_U)`
>
> is bijective.
>
> Injectivity is `AlgebraicGeometry.Space.canonicalMapToHomRestrict_injective`: a morphism
> `φ : ℐⁿ𝒢 ⟶ ℱ` vanishing on `U` has coherent image supported in `V(ℐ)`, so some power of `ℐ`
> annihilates that image and `φ` dies on a deeper step of the filtration.  Surjectivity is
> `AlgebraicGeometry.Space.canonicalMapToHomRestrict_surjective`: a morphism `𝒢|_U ⟶ ℱ|_U` is
> transported to a surjective Noetherian affine chart, extended there by the first display of
> [Stacks, Tag 01YB] on the chart's scheme, made compatible on the kernel pair by raising the
> exponent of the ideal, and glued.

```lean
theorem canonicalMapToHomRestrict_bijective (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ X.1) (hI : I.toSheafOfModules.IsQuasicoherentOnSite)
    (G F : Modules.{u, u} B S hS X.1 X.2) (hG : IsCoherent B S hS X.1 X.2 G)
    [F.IsQuasicoherentOnSite] :
    Function.Bijective (canonicalMapToHomRestrict B S hS X I G F)
```

**`AlgebraicGeometry.Space.canonicalMapToSections_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentHomColimitBijective.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentHomColimitBijective.lean#L109). The attribute's comment: “the in particular display”.

> **[Stacks, Tag 07UM], the "in particular" display.**  For a Noetherian algebraic space `X`
> over `S`, a quasi-coherent sheaf of ideals `ℐ` with open complement `U = X ∖ V(ℐ)` and a
> quasi-coherent `𝒪_X`-module `ℱ`, the canonical map
>
> `colim_n Hom_{𝒪_X}(ℐⁿ, ℱ) ⟶ Γ(U, ℱ|_U)`
>
> is bijective.
>
> This is `AlgebraicGeometry.Space.canonicalMapToHomRestrict_bijective` at `𝒢 = 𝒪_X`, which is
> legitimate because the structure sheaf of a Noetherian algebraic space is coherent
> (`AlgebraicGeometry.Space.isCoherent_structureSheaf`, the structure-sheaf clause of
> [Stacks, Tag 07UB]), composed with the bijection `SheafOfModules.unitHomEquiv` identifying the
> morphisms `𝒪_U ⟶ ℱ|_U` with the sections of `ℱ|_U`.  Noetherian implies the étale-local
> Noetherian property that the coherence of the structure sheaf asks for, which is `hN.2.2`.

```lean
theorem canonicalMapToSections_bijective (hZ : B.Contains (⊤_ Scheme.{u}))
    (hN : IsNoetherian B S hS hZ X.1) (hI : I.toSheafOfModules.IsQuasicoherentOnSite)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] :
    Function.Bijective (canonicalMapToSections B S hS X I F)
```

**`AlgebraicGeometry.Space.idealPowHomRestrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HomOverIdealUnitLocus.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HomOverIdealUnitLocus.lean#L325). The attribute's comment: “the canonical map of the first display, term by term”.

> **The canonical map of the first display of [Stacks, Tag 07UM], term by term.**  A morphism
> `φ : ℐⁿ G ⟶ F` restricts along an étale morphism `j : Y ⟶ X` whose image misses `V(ℐ)` to a
> morphism `G|_Y ⟶ F|_Y`, the source being read through the isomorphism `ℐⁿ G|_Y ≅ G|_Y` of
> `AlgebraicGeometry.Space.isIso_etaleModulePullback_idealPowModuleι`.
>
> These maps agree along the transition maps of the direct system, which is
> `AlgebraicGeometry.Space.idealPowHomRestrict_homOfLE`, so together they are a single map out of
> `colim_n Hom_{𝒪_X}(ℐⁿ G, F)`.  The bijectivity asserted by the tag is not proved; see the
> section "What is not proved" of the module documentation.

```lean
noncomputable def idealPowHomRestrict {Y : AlgebraicSpaces B S hS} (j : Y ⟶ X)
    (hj : IsEtale B S hS j.hom) (I : IdealSheaves B S hS X.1 X.2)
    (hjU : Set.range (pointsMap B S hS Y.1 j.hom) ⊆ idealUnitLocus B S hS X I)
    (n : ℕ) {M N : Modules.{u, u} B S hS X.1 X.2} (φ : idealPowModule I n M ⟶ N) :
    (etaleModulePullback B S hS j hj).obj M ⟶ (etaleModulePullback B S hS j hj).obj N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.13, Tag 07UI](https://stacks.math.columbia.edu/tag/07UI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
