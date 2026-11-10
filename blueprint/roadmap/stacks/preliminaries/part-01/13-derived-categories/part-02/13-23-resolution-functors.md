---
declaration: section
origin: cited
lean: qhPlus_isTriangulated, qhPlus_isEquivalence, HomotopyCategory.Plus.ResolutionFunctor, HomotopyCategory.Plus.existsUnique_functor_of_resolutionFunctor, HomotopyCategory.Plus.nonempty_resolutionFunctor, HomotopyCategory.Plus.nonempty_isTerminal_rightResolution, HomotopyCategory.Plus.commShiftOfQuasiIso, HomotopyCategory.Plus.commShiftOfQuasiIso_compatibility
statement: formalized
proof: formalized
---

# 13.23 Resolution functors

Section 13.23 of the Stacks Project, [Tag 013U](https://stacks.math.columbia.edu/tag/013U). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 013V, a proposition

[Tag 013V](https://stacks.math.columbia.edu/tag/013V) in the Stacks Project.

**`qhPlus_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 1031](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L1031). The attribute's comment: “(exactness)”.

> **(Claim 1: Exactness.)** The functor of Definition 6 is exact, i.e. it is a triangulated
> functor: it commutes with the shift (the `CommShift ℤ` structure on `QhPlus A`) and sends
> distinguished triangles of `K^+(I)` to distinguished triangles of `D^+(A)`.

```lean
theorem qhPlus_isTriangulated [HasDerivedCategory A] :
    (QhPlus A).IsTriangulated
```

**`qhPlus_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 1195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L1195). References: SGA 4½ Etat 0 (3.1.4), “the equivalence”.

> **(Main theorem, Stacks 013V.)** The canonical functor `K^+(I) → D^+(A)` of Definition 6
> is an equivalence of categories.  Combined with exactness (`qhPlus_isTriangulated`) this
> exhibits it as an equivalence of triangulated categories.

```lean
theorem qhPlus_isEquivalence [EnoughInjectives A] [HasDerivedCategory A] :
    (QhPlus A).IsEquivalence
```

## Tag 013W, a definition

[Tag 013W](https://stacks.math.columbia.edu/tag/013W) in the Stacks Project.

**`HomotopyCategory.Plus.ResolutionFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L187).

> A *resolution functor* for an abelian category `C` is the data of a bounded below
> complex of injectives `(j K).X₁`, i.e. an object of `K⁺(ℐ)`, for every object `K` of
> `K⁺(C)`, together with a quasi-isomorphism `(j K).w : K ⟶ (j K).X₁` in `K⁺(C)`: that is,
> of a right resolution of every `K` for the inclusion `K⁺(ℐ) ⥤ K⁺(C)`. (Functoriality of
> `K ↦ (j K).X₁` is automatic, see [Stacks, Tag 05TJ].)

```lean
public abbrev ResolutionFunctor
```

## Tag 05TJ, a lemma

[Tag 05TJ](https://stacks.math.columbia.edu/tag/05TJ) in the Stacks Project.

**`HomotopyCategory.Plus.existsUnique_functor_of_resolutionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L395).

> Let `C` be an abelian category, `ℐ ⊆ C` its full additive subcategory of injective
> objects, and let `j` be a resolution functor for `C`, i.e. a right resolution
> `(j K).w : K ⟶ (j K).X₁` in `K⁺(ℐ)` of every object `K` of `K⁺(C)`. Then there is a unique
> way to make `K ↦ (j K).X₁` into a functor `F : K⁺(C) ⥤ K⁺(ℐ)` for which the comparison
> maps `(j K).w` form a natural transformation `𝟭 K⁺(C) ⟶ F ⋙ (K⁺(ℐ) ⥤ K⁺(C))`; the latter
> is then a `2`-isomorphism over `D⁺(C)`, since its components are quasi-isomorphisms.

```lean
public theorem existsUnique_functor_of_resolutionFunctor (j : ResolutionFunctor C) :
    ∃! F : HomotopyCategory.Plus C ⥤ HomotopyCategory.Plus (InjectiveObject C),
      ∃ (α : 𝟭 (HomotopyCategory.Plus C) ⟶ F ⋙ (localizerMorphism C).functor)
        (hα : ∀ K, quasiIso C (α.app K)),
        ∀ K, LocalizerMorphism.RightResolution.mk (α.app K) (hα K) = j K
```

## Tag 013X, a lemma

[Tag 013X](https://stacks.math.columbia.edu/tag/013X) in the Stacks Project.

**`HomotopyCategory.Plus.nonempty_resolutionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L306). The attribute's comment: “T\_013X, existence: a resolution functor exists when `C` has enough injectives”. References: SGA 4½ Etat 0 (3.2.3), “(4) existence”.

> Let `C` be an abelian category with enough injectives. Then a resolution functor for `C`
> exists ([Stacks, Tag 013W]): every object `K` of `K⁺(C)` admits a bounded below complex of
> injectives `(j K).X₁` together with a quasi-isomorphism `(j K).w : K ⟶ (j K).X₁` in `K⁺(C)`.

```lean
public theorem nonempty_resolutionFunctor (C : Type*) [Category C] [Abelian C]
    [EnoughInjectives C] :
    Nonempty (HomotopyCategory.Plus.ResolutionFunctor C)
```

**`HomotopyCategory.Plus.nonempty_isTerminal_rightResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L334). The attribute's comment: “T\_013X, uniqueness up to unique isomorphism; no hypothesis on `C`”. References: SGA 4½ Etat 0 (3.2.3), “(4) uniqueness”.

> Let `C` be an abelian category. A right resolution of an object `K` of `K⁺(C)` is unique up
> to unique isomorphism: every right resolution `R` of `K` is a terminal object of the category
> `(localizerMorphism C).RightResolution K` of right resolutions of `K`, in which a morphism
> `R' ⟶ R` is a morphism `f : R'.X₁ ⟶ R.X₁` of `K⁺(ℐ)` with `R'.w ≫ f = R.w` in `K⁺(C)`. So any
> two right resolutions of `K` are related by exactly one morphism compatible with their
> comparison maps, and every such morphism is an isomorphism; applied to two resolution functors
> this is the uniqueness up to unique isomorphism of [Stacks, Tag 013X], and it needs no hypothesis
> on `C` beyond `Abelian C`.

```lean
public theorem nonempty_isTerminal_rightResolution (C : Type*) [Category C] [Abelian C]
    {K : HomotopyCategory.Plus C} (R : (localizerMorphism C).RightResolution K) :
    Nonempty (IsTerminal R)
```

## Tag 014W, a lemma

[Tag 014W](https://stacks.math.columbia.edu/tag/014W) in the Stacks Project.

**`HomotopyCategory.Plus.commShiftOfQuasiIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L542). The attribute's comment: “the commutation with the shift itself; `commShiftOfQuasiIso_compatibility` is its compatibility with the comparison maps and `eq_commShiftOfQuasiIso` its uniqueness”.

> **The commutation of a resolution functor with the shift**, the source's `ξ`: its component
> at `a` and `K` is the unique `ξ_K : F(K⟦a⟧) ⟶ (F K)⟦a⟧` with `α_{K⟦a⟧} ≫ ι ξ_K = (α_K)⟦a⟧`. It
> is the only commutation compatible with `α` (`commShiftOfQuasiIso_compatibility`,
> `eq_commShiftOfQuasiIso`), and `F` is exact for it (`isTriangulated_of_quasiIso`).

```lean
noncomputable def commShiftOfQuasiIso : F.CommShift ℤ
```

**`HomotopyCategory.Plus.commShiftOfQuasiIso_compatibility`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L572). The attribute's comment: “the commutation is compatible with the comparison maps”.

> `commShiftOfQuasiIso` is compatible with the comparison maps `α`: each of its components
> satisfies `α_{K⟦a⟧} ≫ ι ξ_K = (α_K)⟦a⟧`.

```lean
lemma commShiftOfQuasiIso_compatibility :
    letI := commShiftOfQuasiIso F α hα
    NatTrans.CommShift α ℤ
```

**`HomotopyCategory.Plus.eq_commShiftOfQuasiIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L582). The attribute's comment: “uniqueness of the commutation compatible with the comparison maps”.

> Uniqueness of the source's `ξ`: a commutation of `F` with the shift which is compatible with
> the comparison maps `α` has `ξ` for each of its components, hence is `commShiftOfQuasiIso`.

```lean
lemma eq_commShiftOfQuasiIso :
    ∀ h : F.CommShift ℤ, (letI := h; NatTrans.CommShift α ℤ) →
      h = commShiftOfQuasiIso F α hα
```

**`HomotopyCategory.Plus.isTriangulated_of_quasiIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L594). The attribute's comment: “a resolution functor is exact”.

> A resolution functor is exact: it carries distinguished triangles of `K⁺(C)` to
> distinguished triangles of `K⁺(ℐ)`, for its commutation with the shift.

```lean
lemma isTriangulated_of_quasiIso :
    letI := commShiftOfQuasiIso F α hα
    F.IsTriangulated
```

## Tag 05TK, a lemma

[Tag 05TK](https://stacks.math.columbia.edu/tag/05TK) in the Stacks Project.

**`HomotopyCategory.Plus.exists_equivalence_and_existsUnique_lift_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L729).

> Let `C` be an abelian category, `ℐ ⊆ C` its full additive subcategory of injective
> objects, and let `F : K⁺(C) ⥤ K⁺(ℐ)` be a functor equipped with comparison maps
> `α.app K : K ⟶ F K` in `K⁺(C)` that are quasi-isomorphisms, i.e. the functorial form of a
> resolution functor ([Stacks, Tags 013W, 05TJ]). Then `F` factors through the localization
> `Q : K⁺(C) ⥤ D⁺(C)` by a functor which is quasi-inverse to the canonical functor
> `K⁺(ℐ) ⥤ D⁺(C)`, and the factorization is unique up to a unique natural transformation
> over `F`.

```lean
public theorem exists_equivalence_and_existsUnique_lift_of_quasiIso
    (F : HomotopyCategory.Plus C ⥤ HomotopyCategory.Plus (InjectiveObject C))
    (α : 𝟭 (HomotopyCategory.Plus C) ⟶ F ⋙ (localizerMorphism C).functor)
    (hα : ∀ K, quasiIso C (α.app K)) :
    (∃ e : DerivedCategory.Plus C ≌ HomotopyCategory.Plus (InjectiveObject C),
      e.inverse = (localizerMorphism C).functor ⋙ DerivedCategory.Plus.Qh ∧
        Nonempty (DerivedCategory.Plus.Qh ⋙ e.functor ≅ F)) ∧
    ∀ (j₁ j₂ : DerivedCategory.Plus C ⥤ HomotopyCategory.Plus (InjectiveObject C))
      (e₁ : DerivedCategory.Plus.Qh ⋙ j₁ ≅ F) (e₂ : DerivedCategory.Plus.Qh ⋙ j₂ ≅ F),
      ∃! τ : j₁ ⟶ j₂,
        Functor.whiskerLeft DerivedCategory.Plus.Qh τ = e₁.hom ≫ e₂.inv
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.23, Tag 013U](https://stacks.math.columbia.edu/tag/013U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
