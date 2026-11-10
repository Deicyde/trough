---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.derivedLowerShriek_independent_of_compactification, Stacks.EtaleCohomology.derivedLowerShriekUnbounded_independent_of_compactification, Stacks.EtaleCohomology.derivedLowerShriek_independent_of_compactification_univ, Stacks.EtaleCohomology.derivedLowerShriekUnbounded_independent_of_compactification_univ, Stacks.EtaleCohomology.derivedLowerShriekCompIso, Stacks.EtaleCohomology.derivedLowerShriekCompIsoUniv, Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompIso, Stacks.EtaleCohomology.derivedLowerShriekCompIso_assoc
statement: formalized
proof: formalized
---

# 63.9 Derived lower shriek via compactifications

Section 63.9 of the Stacks Project, [Tag 0F7H](https://stacks.math.columbia.edu/tag/0F7H). 5 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F7I, a lemma

[Tag 0F7I](https://stacks.math.columbia.edu/tag/0F7I) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedLowerShriek_independent_of_compactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/Independence.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/Independence.lean#L129). The attribute's comment: “bounded-below complexes with torsion cohomology sheaves, arbitrary ring Λ”. References: SGA 4½ Arcata (4.5.3), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Stacks Project, Tag 0F7I**, for `Rf_! : D⁺_tors(X_étale, Λ) ⥤ D⁺_tors(Y_étale, Λ)` and an
> arbitrary ring `Λ`. Let `f : X ⟶ Y` be a finite type separated morphism of quasi-compact and
> quasi-separated schemes. Then `X` has a compactification over `Y`, and the functors `Rf_!`
> built from the compactifications are, up to canonical isomorphism, independent of the
> compactification: the isomorphisms `derivedLowerShriekCompactificationIso f j k Λ` between them
> compose, and along every morphism `g : j ⟶ k` of compactifications they are the isomorphism
> built from the map of [Stacks, Tag 0F7G] and the composition of derived direct images.

```lean
theorem derivedLowerShriek_independent_of_compactification :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      (∀ j k l : CompactificationOf (Over.mk f),
        derivedLowerShriekCompactificationIso f j k Λ ≪≫
            derivedLowerShriekCompactificationIso f k l Λ =
          derivedLowerShriekCompactificationIso f j l Λ) ∧
      ∀ {j k : CompactificationOf (Over.mk f)} (g : j ⟶ k),
        derivedLowerShriekCompactificationIso f k j Λ = derivedLowerShriekHomIso Λ g
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnbounded_independent_of_compactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/Independence.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/Independence.lean#L186). The attribute's comment: “unbounded derived category D(X\_étale, Λ), Λ a torsion ring”. References: SGA 4 XVII (5.2.2), “special case”; SGA 4½ Arcata (4.5.3), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Stacks Project, Tag 0F7I**, for `Rf_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` and a torsion ring
> `Λ`. Let `f : X ⟶ Y` be a finite type separated morphism of quasi-compact and quasi-separated
> schemes. Then `X` has a compactification over `Y`, and the functors `Rf_!` built from the
> compactifications are, up to canonical isomorphism, independent of the compactification: the
> isomorphisms `derivedLowerShriekUnboundedCompactificationIso f j k Λ hΛ` between them compose,
> and along every morphism `g : j ⟶ k` of compactifications they are the isomorphism built from
> the map of [Stacks, Tag 0F7G] and the composition of derived direct images.

```lean
theorem derivedLowerShriekUnbounded_independent_of_compactification :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      (∀ j k l : CompactificationOf (Over.mk f),
        derivedLowerShriekUnboundedCompactificationIso f j k Λ hΛ ≪≫
            derivedLowerShriekUnboundedCompactificationIso f k l Λ hΛ =
          derivedLowerShriekUnboundedCompactificationIso f j l Λ hΛ) ∧
      ∀ {j k : CompactificationOf (Over.mk f)} (g : j ⟶ k),
        derivedLowerShriekUnboundedCompactificationIso f k j Λ hΛ =
          derivedLowerShriekUnboundedHomIso Λ g hΛ
```

**`Stacks.EtaleCohomology.derivedLowerShriek_independent_of_compactification_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/IndependenceCoefficientUniverse.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/IndependenceCoefficientUniverse.lean#L129). The attribute's comment: “bounded-below torsion complexes, arbitrary ring Λ in any universe”. References: SGA 4½ Arcata (4.5.3), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Stacks Project, Tag 0F7I**, for `Rf_! : D⁺_tors(X_étale, Λ) ⥤ D⁺_tors(Y_étale, Λ)` and an
> arbitrary ring `Λ`. Let `f : X ⟶ Y` be a finite type separated morphism of quasi-compact and
> quasi-separated schemes. Then `X` has a compactification over `Y`, and the functors `Rf_!`
> built from the compactifications are, up to canonical isomorphism, independent of the
> compactification: the isomorphisms `derivedLowerShriekCompactificationIsoUniv f j k Λ` between them
> compose, and along every morphism `g : j ⟶ k` of compactifications they are the isomorphism
> built from the map of [Stacks, Tag 0F7G] and the composition of derived direct images.

```lean
theorem derivedLowerShriek_independent_of_compactification_univ :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      (∀ j k l : CompactificationOf (Over.mk f),
        derivedLowerShriekCompactificationIsoUniv f j k Λ ≪≫
            derivedLowerShriekCompactificationIsoUniv f k l Λ =
          derivedLowerShriekCompactificationIsoUniv f j l Λ) ∧
      ∀ {j k : CompactificationOf (Over.mk f)} (g : j ⟶ k),
        derivedLowerShriekCompactificationIsoUniv f k j Λ = derivedLowerShriekHomIsoUniv Λ g
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnbounded_independent_of_compactification_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/IndependenceCoefficientUniverse.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactificationIndependence/IndependenceCoefficientUniverse.lean#L186). The attribute's comment: “unbounded derived category D(X\_étale, Λ), Λ a torsion ring in any universe”. References: SGA 4 XVII (5.2.2), “special case”; SGA 4½ Arcata (4.5.3), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Stacks Project, Tag 0F7I**, for `Rf_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` and a torsion ring
> `Λ`. Let `f : X ⟶ Y` be a finite type separated morphism of quasi-compact and quasi-separated
> schemes. Then `X` has a compactification over `Y`, and the functors `Rf_!` built from the
> compactifications are, up to canonical isomorphism, independent of the compactification: the
> isomorphisms `derivedLowerShriekUnboundedCompactificationIsoUniv f j k Λ hΛ` between them compose,
> and along every morphism `g : j ⟶ k` of compactifications they are the isomorphism built from
> the map of [Stacks, Tag 0F7G] and the composition of derived direct images.

```lean
theorem derivedLowerShriekUnbounded_independent_of_compactification_univ :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      (∀ j k l : CompactificationOf (Over.mk f),
        derivedLowerShriekUnboundedCompactificationIsoUniv f j k Λ hΛ ≪≫
            derivedLowerShriekUnboundedCompactificationIsoUniv f k l Λ hΛ =
          derivedLowerShriekUnboundedCompactificationIsoUniv f j l Λ hΛ) ∧
      ∀ {j k : CompactificationOf (Over.mk f)} (g : j ⟶ k),
        derivedLowerShriekUnboundedCompactificationIsoUniv f k j Λ hΛ =
          derivedLowerShriekUnboundedHomIsoUniv Λ g hΛ
```

## Tag 0F7J, a lemma

[Tag 0F7J](https://stacks.math.columbia.edu/tag/0F7J) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedLowerShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIso.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIso.lean#L410).

> **Stacks Project, Tag 0F7J.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be separated morphisms of
> finite type of quasi-compact and quasi-separated schemes, and let `Λ` be a ring. Then
> `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!` as functors on `D⁺_tors(X_étale, Λ)`, where `Rf_!`, `Rg_!` and
> `R(g ∘ f)_!` are computed through arbitrary compactifications `jf`, `jg` and `j`.
>
> The isomorphism is that of the source: through a compactification `X ⟶ X̄` of `X` over `Ȳ`
> (Nagata's theorem, [Stacks, Tag 0F41]) it is
> `R(ḡ ∘ f̄)_* (j' ∘ j)_! ≅ Rḡ_* Rf̄_* j'_! j_! ≅ Rḡ_* i_! Rf'_* j_!`
> (`Stacks.EtaleCohomology.derivedLowerShriekCompOverIso`, which uses [Stacks, Tag 0F7B] for the
> open immersion `i`), and it is transported to the given compactifications by
> [Stacks, Tag 0F7I] (`Stacks.EtaleCohomology.derivedLowerShriekCompactificationIso`), which is the
> independence of the choices made. `Rf_!` carries `D⁺_tors` into `D⁺_tors` by
> `Stacks.EtaleCohomology.isTorsionPlus_derivedLowerShriek_obj`.

```lean
def derivedLowerShriekCompIso [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y]
    [QuasiSeparatedSpace Y] [CompactSpace Z] [QuasiSeparatedSpace Z] [IsSeparated f]
    [LocallyOfFiniteType f] [IsSeparated g] [LocallyOfFiniteType g]
    (jf : CompactificationOf (Over.mk f)) (jg : CompactificationOf (Over.mk g))
    (j : CompactificationOf (Over.mk (f ≫ g))) :
    (isTorsionPlus.{u, 0} Λ X).ι ⋙ derivedLowerShriek.{u, 0} (f ≫ g) j Λ ≅
      (isTorsionPlus.{u, 0} Λ X).ι ⋙ derivedLowerShriek.{u, 0} f jf Λ ⋙
        derivedLowerShriek.{u, 0} g jg Λ
```

**`Stacks.EtaleCohomology.derivedLowerShriekCompIsoUniv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoCoefficientUniverse.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoCoefficientUniverse.lean#L202). The attribute's comment: “D⁺\_tors(X\_étale, Λ), Λ a ring in any universe”.

> **Stacks Project, Tag 0F7J**, for a coefficient ring `Λ` in any universe. Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be separated morphisms of finite type of quasi-compact and quasi-separated schemes,
> and let `Λ` be a ring. Then `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!` as functors on `D⁺_tors(X_étale, Λ)`,
> where `Rf_!`, `Rg_!` and `R(g ∘ f)_!` are computed through arbitrary compactifications `jf`, `jg`
> and `j`.
>
> Through a compactification `X ⟶ X̄` of `X` over `Ȳ` (Nagata's theorem, [Stacks, Tag 0F41]) the
> isomorphism is `Stacks.EtaleCohomology.derivedLowerShriekCompOverIsoUniv`, which uses
> [Stacks, Tag 0F7B] for the open immersion `Y ⟶ Ȳ`; it is transported to the given
> compactifications by [Stacks, Tag 0F7I]
> (`Stacks.EtaleCohomology.derivedLowerShriekCompactificationIsoUniv`).

```lean
def derivedLowerShriekCompIsoUniv [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y]
    [QuasiSeparatedSpace Y] [CompactSpace Z] [QuasiSeparatedSpace Z] [IsSeparated f]
    [LocallyOfFiniteType f] [IsSeparated g] [LocallyOfFiniteType g]
    (jf : CompactificationOf (Over.mk f)) (jg : CompactificationOf (Over.mk g))
    (j : CompactificationOf (Over.mk (f ≫ g))) :
    (isTorsionPlus.{u, w} Λ X).ι ⋙ derivedLowerShriek.{u, w} (f ≫ g) j Λ ≅
      (isTorsionPlus.{u, w} Λ X).ι ⋙ derivedLowerShriek.{u, w} f jf Λ ⋙
        derivedLowerShriek.{u, w} g jg Λ
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoUnbounded.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoUnbounded.lean#L429). The attribute's comment: “unbounded derived categories D(X\_étale, Λ), Λ a torsion ring”.

> **Stacks Project, Tag 0F7J**, on unbounded derived categories. Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be separated morphisms of finite type of quasi-compact and quasi-separated schemes, and
> let `Λ` be a torsion ring, in any universe. Then `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!` as functors
> `D(X_étale, Λ) ⥤ D(Z_étale, Λ)`, where `Rf_!`, `Rg_!` and `R(g ∘ f)_!` are computed through
> arbitrary compactifications `jf`, `jg` and `j`.
>
> The isomorphism is that of the source: through a compactification `X ⟶ X̄` of `X` over `Ȳ`
> (Nagata's theorem, [Stacks, Tag 0F41]) it is
> `R(ḡ ∘ f̄)_* (j' ∘ j)_! ≅ Rḡ_* Rf̄_* j'_! j_! ≅ Rḡ_* i_! Rf'_* j_!`
> (`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompOverIso`, which uses
> [Stacks, Tag 0F7B] for the open immersion `i`), and it is transported to the given
> compactifications by [Stacks, Tag 0F7I]
> (`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompactificationIsoUniv`). The case of
> `D⁺_tors(X_étale, Λ)` for an arbitrary ring is
> `Stacks.EtaleCohomology.derivedLowerShriekCompIsoUniv`.

```lean
def derivedLowerShriekUnboundedCompIso [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y]
    [QuasiSeparatedSpace Y] [CompactSpace Z] [QuasiSeparatedSpace Z] [IsSeparated f]
    [LocallyOfFiniteType f] [IsSeparated g] [LocallyOfFiniteType g]
    (jf : CompactificationOf (Over.mk f)) (jg : CompactificationOf (Over.mk g))
    (j : CompactificationOf (Over.mk (f ≫ g))) :
    derivedLowerShriekUnbounded.{u, w} (f ≫ g) j Λ ≅
      derivedLowerShriekUnbounded.{u, w} f jf Λ ⋙ derivedLowerShriekUnbounded.{u, w} g jg Λ
```

## Tag 0F7K, a lemma

[Tag 0F7K](https://stacks.math.columbia.edu/tag/0F7K) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedLowerShriekCompIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoIndependence.lean, line 921](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/CompositionIsoIndependence.lean#L921).

> **Stacks Project, Tag 0F7K.** Let `f : X ⟶ Y`, `g : Y ⟶ Z` and `h : Z ⟶ T` be separated
> morphisms of finite type of quasi-compact and quasi-separated schemes, and let `Λ` be a ring. Then
> the two isomorphisms `R(h ∘ g ∘ f)_! ≅ Rh_! ∘ Rg_! ∘ Rf_!` on `D⁺_tors(X_étale, Λ)` built from the
> isomorphisms of [Stacks, Tag 0F7J] (`Stacks.EtaleCohomology.derivedLowerShriekCompIso`) agree:
> through `R(h ∘ g)_! ∘ Rf_!` and through `Rh_! ∘ R(g ∘ f)_!`. Each of `Rf_!`, `Rg_!`, `Rh_!`,
> `R(g ∘ f)_!`, `R(h ∘ g)_!` and `R(h ∘ g ∘ f)_!` is computed through an arbitrary compactification.
>
> The proof follows [Stacks, Tag 0F7K]: choosing a compactification `Ȳ` of `Y` over the
> compactification `Z̄` of `Z` (and of `X` over `Ȳ`) the statement is
> `Stacks.EtaleCohomology.derivedLowerShriekCompIso_assoc_of_tower`, and the isomorphisms of
> [Stacks, Tag 0F7J] do not depend on the compactifications
> (`Stacks.EtaleCohomology.derivedLowerShriekCompIso_hom_app_second` and its first and third slot
> companions).

```lean
theorem derivedLowerShriekCompIso_assoc (jf : CompactificationOf (Over.mk f))
    (jg : CompactificationOf (Over.mk g)) (jh : CompactificationOf (Over.mk h))
    (jfg : CompactificationOf (Over.mk (f ≫ g))) (jgh : CompactificationOf (Over.mk (g ≫ h)))
    (jfgh : CompactificationOf (Over.mk (f ≫ g ≫ h)))
    (K : (isTorsionPlus.{u, 0} Λ X).FullSubcategory) :
    (derivedLowerShriekCompIso Λ f (g ≫ h) jf jgh jfgh).hom.app K ≫
        (derivedLowerShriekCompIso Λ g h jg jh jgh).hom.app
          ⟨(derivedLowerShriek.{u, 0} f jf Λ).obj K.obj,
            isTorsionPlus_derivedLowerShriek_obj Λ f jf K.obj K.property⟩ =
      (derivedLowerShriekCompIso Λ (f ≫ g) h jfg jh jfgh).hom.app K ≫
        (derivedLowerShriek.{u, 0} h jh Λ).map
          ((derivedLowerShriekCompIso Λ f g jf jg jfg).hom.app K)
```

## Tag 0F7L, a lemma

[Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChange.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChange.lean#L132). The attribute's comment: “the isomorphism g⁻¹ ∘ Rf\_! ≅ Rf'\_! ∘ (g')⁻¹ on D⁺\_tors”.

> **Stacks Project, Tag 0F7L.** For a cartesian square of schemes `f' ≫ g = g' ≫ f` and a
> compactification `j` of `X` over `Y`, the canonical isomorphism `g⁻¹ ∘ Rf_! ≅ Rf'_! ∘ (g')⁻¹` of
> functors on `D⁺_tors(X_étale, Λ)`, the bounded below complexes with torsion cohomology sheaves,
> `Rf'_!` being computed with the base change of `j`
> (`AlgebraicGeometry.CompactificationOf.baseChange`). Its components are
> `Stacks.EtaleCohomology.derivedLowerShriekBaseChange`.

```lean
def derivedLowerShriekBaseChangeIso :
    (isTorsionPlus.{u, 0} Λ X).ι ⋙ derivedLowerShriek.{u, 0} f j Λ ⋙
        etaleModuleDerivedInverseImagePlus.{u, 0} Λ g ≅
      (isTorsionPlus.{u, 0} Λ X).ι ⋙ etaleModuleDerivedInverseImagePlus.{u, 0} Λ g' ⋙
        derivedLowerShriek.{u, 0} f' (j.baseChange sq) Λ
```

**`Stacks.EtaleCohomology.derivedLowerShriekBaseChange_compIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeComposition.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeComposition.lean#L241). The attribute's comment: “compatibility of the base change isomorphisms with the isomorphisms of Lemma 0F7J”.

> For cartesian squares of quasi-compact and quasi-separated schemes
> ```
> X' --hX--> X
> |f'        |f
> Y' --hY--> Y
> |g'        |g
> Z' --h-->  Z
> ```
> with `f` and `g` separated of finite type, the base change isomorphisms
> `h⁻¹ ∘ R(g ∘ f)_! ≅ R(g' ∘ f')_! ∘ hX⁻¹`, `h⁻¹ ∘ Rg_! ≅ Rg'_! ∘ hY⁻¹` and
> `hY⁻¹ ∘ Rf_! ≅ Rf'_! ∘ hX⁻¹` (`Stacks.EtaleCohomology.derivedLowerShriekBaseChange`) are
> compatible with the isomorphisms `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!`
> (`Stacks.EtaleCohomology.derivedLowerShriekCompIso`) on `D⁺_tors(X_étale, Λ)`, for arbitrary
> compactifications.

```lean
theorem derivedLowerShriekBaseChange_compIso (sqg : IsPullback hY g' g h)
    (sqf : IsPullback hX f' f hY) (jf : CompactificationOf (Over.mk f))
    (jg : CompactificationOf (Over.mk g)) (j : CompactificationOf (Over.mk (f ≫ g)))
    (K : DerivedCategory.Plus (EtaleModules.{u, 0} Λ X)) (hK : isTorsionPlus.{u, 0} Λ X K) :
    haveI : IsSeparated f' := MorphismProperty.of_isPullback sqf inferInstance
    haveI : LocallyOfFiniteType f' := MorphismProperty.of_isPullback sqf inferInstance
    haveI : IsSeparated g' := MorphismProperty.of_isPullback sqg inferInstance
    haveI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback sqg inferInstance
    (etaleModuleDerivedInverseImagePlus.{u, 0} Λ h).map
        ((derivedLowerShriekCompIso Λ f g jf jg j).hom.app ⟨K, hK⟩) ≫
      (derivedLowerShriekBaseChange.{u, 0} Λ sqg jg).app
        ((derivedLowerShriek.{u, 0} f jf Λ).obj K) ≫
      (derivedLowerShriek.{u, 0} g' (jg.baseChange sqg) Λ).map
        ((derivedLowerShriekBaseChange.{u, 0} Λ sqf jf).app K) =
    (derivedLowerShriekBaseChange.{u, 0} Λ (sqf.paste_vert sqg) j).app K ≫
      (derivedLowerShriekCompIso Λ f' g' (jf.baseChange sqf) (jg.baseChange sqg)
        (j.baseChange (sqf.paste_vert sqg))).hom.app
          ⟨(etaleModuleDerivedInverseImagePlus.{u, 0} Λ hX).obj K,
            isTorsionPlus_etaleModuleDerivedInverseImagePlus_obj Λ hX K hK⟩
```

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.derivedLowerShriekUnboundedBaseChangeIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeUnbounded.lean#L152), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeUnboundedRegistration.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedLowerShriek/ProperBaseChangeUnboundedRegistration.lean#L23) (StacksFrontier): “the isomorphism g⁻¹ ∘ Rf\_! ≅ Rf'\_! ∘ (g')⁻¹ on unbounded D(X\_étale, Λ), Λ a torsion ring”.

## Tag 0H6X, a remark

[Tag 0H6X](https://stacks.math.columbia.edu/tag/0H6X) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedLowerShriekBaseChangeIso_hom_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowBaseChangeToDirectImage.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowBaseChangeToDirectImage.lean#L121). The attribute's comment: “(2), on D⁺\_tors”.

> **[Stacks, Tag 0H6X], compatibility (2), on `D⁺_tors(X_étale, Λ)`**: the map `Rf_! ⟶ Rf_*`
> is compatible with the isomorphism `g⁻¹ ∘ Rf_! ≅ Rf'_! ∘ (g')⁻¹` of [Stacks, Tag 0F7L]
> (`Stacks.EtaleCohomology.derivedLowerShriekBaseChangeIso`) and the base change map
> `g⁻¹ ∘ Rf_* ⟶ Rf'_* ∘ (g')⁻¹` of Cohomology on Sites, Remark 07A7
> (`Stacks.EtaleCohomology.etaleModuleDerivedBaseChange`): for a cartesian square
> `g' ≫ f = f' ≫ g`, a compactification `j` of `f` and `K` in `D⁺_tors(X_étale, Λ)`,
> `g⁻¹ Rf_! K ≅ Rf'_! (g')⁻¹ K ⟶ Rf'_* (g')⁻¹ K` is `g⁻¹ Rf_! K ⟶ g⁻¹ Rf_* K ⟶ Rf'_* (g')⁻¹ K`,
> `Rf'_!` being computed with the base change of `j`.

```lean
theorem derivedLowerShriekBaseChangeIso_hom_comp_toDirectImage (sq : IsPullback g' f' f g)
    (j : CompactificationOf (Over.mk f)) (K : (isTorsionPlus.{u, 0} Λ X).FullSubcategory) :
    (derivedLowerShriekBaseChangeIso Λ sq j).hom.app K ≫
        (derivedLowerShriekToDirectImage.{u, 0} Λ f' (j.baseChange sq)).app
          ((etaleModuleDerivedInverseImagePlus.{u, 0} Λ g').obj K.obj) =
      (etaleModuleDerivedInverseImagePlus.{u, 0} Λ g).map
          ((derivedLowerShriekToDirectImage.{u, 0} Λ f j).app K.obj) ≫
        (etaleModuleDerivedBaseChange.{u, 0} Λ f f' g g' sq.w.symm).app K.obj
```

**`Stacks.EtaleCohomology.derivedLowerShriekCompIso_hom_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowCompositionToDirectImage.lean, line 879](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowCompositionToDirectImage.lean#L879). The attribute's comment: “(1), on D⁺\_tors”.

> **[Stacks, Tag 0H6X], compatibility (1), on `D⁺_tors(X_étale, Λ)`**: the map `Rf_! ⟶ Rf_*`
> is compatible with the isomorphism `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!` of [Stacks, Tag 0F7J]
> (`Stacks.EtaleCohomology.derivedLowerShriekCompIso`) and the composition isomorphism
> `R(g ∘ f)_* ≅ Rg_* ∘ Rf_*` of Cohomology on Sites, Tag 0D6E, for arbitrary compactifications
> `jf`, `jg`, `j` of `f`, `g` and `g ∘ f`: for `K` in `D⁺_tors(X_étale, Λ)`,
> `R(g ∘ f)_! K ≅ Rg_! Rf_! K ⟶ Rg_! Rf_* K ⟶ Rg_* Rf_* K ≅ R(g ∘ f)_* K` is the map
> `R(g ∘ f)_! K ⟶ R(g ∘ f)_* K`.

```lean
theorem derivedLowerShriekCompIso_hom_comp_toDirectImage (jf : CompactificationOf (Over.mk f))
    (jg : CompactificationOf (Over.mk g)) (j : CompactificationOf (Over.mk (f ≫ g)))
    (K : (isTorsionPlus.{u, 0} Λ X).FullSubcategory) :
    (derivedLowerShriekCompIso Λ f g jf jg j).hom.app K ≫
        (derivedLowerShriek.{u, 0} g jg Λ).map
          ((derivedLowerShriekToDirectImage.{u, 0} Λ f jf).app K.obj) ≫
        (derivedLowerShriekToDirectImage.{u, 0} Λ g jg).app
          ((etaleModuleDerivedDirectImage.{u, 0} Λ f).obj K.obj) ≫
        (etaleModuleDerivedDirectImageComp.{u, 0} Λ f g (f ≫ g) rfl).inv.app K.obj =
      (derivedLowerShriekToDirectImage.{u, 0} Λ (f ≫ g) j).app K.obj
```

**`Stacks.EtaleCohomology.derivedLowerShriekToDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowToDirectImage.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowToDirectImage.lean#L242). The attribute's comment: “the map Rf\_! ⟶ Rf\_*, functorial in K, on D⁺\_tors”.

> **The map `Rf_! ⟶ Rf_*` of [Stacks, Tag 0H6X]** on `D⁺(X_étale, Λ)`. For a finite type
> separated morphism `f : X ⟶ Y` and a compactification `j : X ⟶ X̄`, `f̄ : X̄ ⟶ Y` of `X` over `Y`
> it is
> ```
> Rf_! = Rf̄_* ∘ Rj_! ⟶ Rf̄_* ∘ Rj_* ≅ R(j ≫ f̄)_* = Rf_*,
> ```
> `Rf̄_*` of the map `Rj_! ⟶ Rj_*` induced by the canonical transformation `j_! ⟶ j_*` of
> [Stacks, Tag 0F4L], followed by the composition isomorphism of derived direct images
> (Cohomology on Sites, Tag 0D6E). It is natural in `K`, and restricts to `D⁺_tors(X_étale, Λ)`.

```lean
def derivedLowerShriekToDirectImage :
    derivedLowerShriek.{u, w} f j Λ ⟶ etaleModuleDerivedDirectImage.{u, w} Λ f
```

**`Stacks.EtaleCohomology.derivedLowerShriekCompactificationIsoUniv_hom_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowToDirectImage.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/BoundedBelowToDirectImage.lean#L384). The attribute's comment: “independence of the compactification, on D⁺\_tors”.

> **[Stacks, Tag 0H6X]: the map `Rf_! ⟶ Rf_*` does not depend on the compactification**, on
> `D⁺_tors(X_étale, Λ)`: for any two compactifications `j₁`, `j₂` of `X` over `Y`, the canonical
> isomorphism `Rf_!^{j₁} ≅ Rf_!^{j₂}` of [Stacks, Tag 0F7I], computed through a compactification
> dominating both, followed by the map `Rf_!^{j₂} ⟶ Rf_*` is the map `Rf_!^{j₁} ⟶ Rf_*`.

```lean
theorem derivedLowerShriekCompactificationIsoUniv_hom_comp_toDirectImage [CompactSpace Y]
    [QuasiSeparatedSpace Y] [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (j₁ j₂ : CompactificationOf (Over.mk f)) :
    (derivedLowerShriekCompactificationIsoUniv f j₁ j₂ Λ).hom ≫
        Functor.whiskerLeft (isTorsionPlus.{u, w} Λ X).ι
          (derivedLowerShriekToDirectImage.{u, w} Λ f j₂) =
      Functor.whiskerLeft (isTorsionPlus.{u, w} Λ X).ι
        (derivedLowerShriekToDirectImage.{u, w} Λ f j₁)
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedBaseChange_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedBaseChangeToDirectImage.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedBaseChangeToDirectImage.lean#L577). The attribute's comment: “(2), on D(X\_étale, Λ), Λ torsion”.

> **[Stacks, Tag 0H6X], compatibility (2), on `D(X_étale, Λ)`**: the map `Rf_! ⟶ Rf_*` is
> compatible with the base change map `g⁻¹ ∘ Rf_! ⟶ Rf'_! ∘ (g')⁻¹` of [Stacks, Tag 0F7L]
> (`Stacks.EtaleCohomology.derivedLowerShriekUnboundedBaseChange`, whose components are those of the
> isomorphism `Stacks.EtaleCohomology.derivedLowerShriekUnboundedBaseChangeIso` when `Λ` is torsion)
> and the base change map `g⁻¹ ∘ Rf_* ⟶ Rf'_* ∘ (g')⁻¹` of Cohomology on Sites, Remark 07A7
> (`Stacks.EtaleCohomology.etaleModuleDerivedBaseChangeUnbounded`): for a cartesian square
> `g' ≫ f = f' ≫ g` and a compactification `j` of `f`, the composite
> `g⁻¹ ∘ Rf_! ⟶ Rf'_! ∘ (g')⁻¹ ⟶ Rf'_* ∘ (g')⁻¹` is `g⁻¹ ∘ Rf_! ⟶ g⁻¹ ∘ Rf_* ⟶ Rf'_* ∘ (g')⁻¹`,
> as transformations of functors on `D(X_étale, Λ)`, `Rf'_!` being computed with the base change of
> `j`.

```lean
theorem derivedLowerShriekUnboundedBaseChange_comp_toDirectImage (sq : IsPullback g' f' f g)
    (j : CompactificationOf (Over.mk f)) :
    derivedLowerShriekUnboundedBaseChange.{u, r} Λ sq j ≫
        Functor.whiskerLeft (etaleModuleDerivedInverseImage.{u, r} Λ g')
          (derivedLowerShriekUnboundedToDirectImage.{u, r} Λ f' (j.baseChange sq)) =
      Functor.whiskerRight (derivedLowerShriekUnboundedToDirectImage.{u, r} Λ f j)
          (etaleModuleDerivedInverseImage.{u, r} Λ g) ≫
        etaleModuleDerivedBaseChangeUnbounded.{u, r} Λ f g g' f' sq.w
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompIso_hom_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedCompositionIsoToDirectImage.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedCompositionIsoToDirectImage.lean#L520). The attribute's comment: “(1), on D(X\_étale, Λ), Λ torsion”.

> **[Stacks, Tag 0H6X], compatibility (1), on `D(X_étale, Λ)`** for a torsion ring `Λ`: the map
> `Rf_! ⟶ Rf_*` is compatible with the isomorphism `R(g ∘ f)_! ≅ Rg_! ∘ Rf_!` of [Stacks, Tag 0F7J]
> (`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompIso`) and the composition isomorphism
> `R(g ∘ f)_* ≅ Rg_* ∘ Rf_*` of Cohomology on Sites, Tag 0D6E, for arbitrary compactifications
> `jf`, `jg`, `j` of `f`, `g` and `g ∘ f`: for `K` in `D(X_étale, Λ)`,
> `R(g ∘ f)_! K ≅ Rg_! Rf_! K ⟶ Rg_! Rf_* K ⟶ Rg_* Rf_* K ≅ R(g ∘ f)_* K` is the map
> `R(g ∘ f)_! K ⟶ R(g ∘ f)_* K`.

```lean
theorem derivedLowerShriekUnboundedCompIso_hom_comp_toDirectImage
    (jf : CompactificationOf (Over.mk f)) (jg : CompactificationOf (Over.mk g))
    (j : CompactificationOf (Over.mk (f ≫ g))) (K : DerivedCategory (EtaleModules.{u, 0} Λ X)) :
    (derivedLowerShriekUnboundedCompIso Λ hΛ f g jf jg j).hom.app K ≫
        (derivedLowerShriekUnbounded.{u, 0} g jg Λ).map
          ((derivedLowerShriekUnboundedToDirectImage.{u, 0} Λ f jf).app K) ≫
        (derivedLowerShriekUnboundedToDirectImage.{u, 0} Λ g jg).app
          ((etaleModuleDerivedDirectImageUnbounded.{u, 0} Λ f).obj K) ≫
        (etaleModuleDerivedDirectImageUnboundedLerayIso.{u, 0} Λ f g (f ≫ g) rfl).inv.app K =
      (derivedLowerShriekUnboundedToDirectImage.{u, 0} Λ (f ≫ g) j).app K
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedToDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedToDirectImage.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedToDirectImage.lean#L108). The attribute's comment: “the map Rf\_! ⟶ Rf\_*, functorial in K, on D(X\_étale, Λ)”.

> **The map `Rf_! ⟶ Rf_*` of [Stacks, Tag 0H6X]** on `D(X_étale, Λ)`. For a finite type
> separated morphism `f : X ⟶ Y` and a compactification `j : X ⟶ X̄`, `f̄ : X̄ ⟶ Y` of `X` over `Y`
> it is
> ```
> Rf_! = Rf̄_* ∘ Rj_! ⟶ Rf̄_* ∘ Rj_* ≅ R(j ≫ f̄)_* = Rf_*,
> ```
> `Rf̄_*` of the map `Rj_! ⟶ Rj_*` induced by the canonical transformation `j_! ⟶ j_*` of
> [Stacks, Tag 0F4L], followed by the inverse of the Leray isomorphism of unbounded derived direct
> images. It is natural in `K`.

```lean
def derivedLowerShriekUnboundedToDirectImage {X Y : Scheme.{u}} (f : X ⟶ Y)
    (j : CompactificationOf (Over.mk f)) :
    derivedLowerShriekUnbounded.{u, r} f j Λ ⟶ etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f
```

**`Stacks.EtaleCohomology.derivedLowerShriekUnboundedCompactificationIsoUniv_hom_comp_toDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedToDirectImage.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CompactSupportFunctoriality/UnboundedToDirectImage.lean#L310). The attribute's comment: “independence of the compactification, on D(X\_étale, Λ), Λ torsion”.

> **[Stacks, Tag 0H6X]: the map `Rf_! ⟶ Rf_*` does not depend on the compactification**, on
> `D(X_étale, Λ)` for a torsion ring `Λ`: for any two compactifications `j₁`, `j₂` of `X` over
> `Y`, the canonical isomorphism `Rf_!^{j₁} ≅ Rf_!^{j₂}` of [Stacks, Tag 0F7I], computed through a
> compactification dominating both, followed by the map `Rf_!^{j₂} ⟶ Rf_*` is the map
> `Rf_!^{j₁} ⟶ Rf_*`.

```lean
theorem derivedLowerShriekUnboundedCompactificationIsoUniv_hom_comp_toDirectImage
    {X Y : Scheme.{u}} (f : X ⟶ Y) [CompactSpace Y] [QuasiSeparatedSpace Y] [IsSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] (j₁ j₂ : CompactificationOf (Over.mk f))
    (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) :
    (derivedLowerShriekUnboundedCompactificationIsoUniv f j₁ j₂ Λ hΛ).hom ≫
        derivedLowerShriekUnboundedToDirectImage.{u, r} Λ f j₂ =
      derivedLowerShriekUnboundedToDirectImage.{u, r} Λ f j₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.9, Tag 0F7H](https://stacks.math.columbia.edu/tag/0F7H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
