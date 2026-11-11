---
declaration: section
origin: cited
lean: CategoryTheory.FiniteFilteredObject, CochainComplex.filteredQuasiIso, CochainComplex.filteredAcyclic, CategoryTheory.FiniteFilteredObject.homologyFunctor_gr_isHomological, CategoryTheory.FiniteFilteredObject.homologyFunctor_grP_isHomological, CategoryTheory.FiniteFilteredObject.homologyFunctor_forget_isHomological, CochainComplex.kernel_eq_filteredAcyclic_and_filteredQuasiIso_eq_inverseImage_isomorphisms, CochainComplex.FilteredDerivedCategory
statement: formalized
proof: formalized
---

# 13.13 Filtered derived categories

Section 13.13 of the Stacks Project, [Tag 05RX](https://stacks.math.columbia.edu/tag/05RX). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05RY, a definition

[Tag 05RY](https://stacks.math.columbia.edu/tag/05RY) in the Stacks Project.

**`CategoryTheory.FiniteFilteredObject`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L236). References: EGA 0 (11.1.3).

> The category `Fil^f(C)` of *finite filtered objects* of `C`: the full subcategory of the
> category `Fil(C) = FilteredObject C ℤᵒᵖ` of filtered objects `(X, F)` on those whose filtration
> `F` is finite.

```lean
public abbrev FiniteFilteredObject (C : Type u) [Category.{v} C]
```

## Tag 05RZ, a definition

[Tag 05RZ](https://stacks.math.columbia.edu/tag/05RZ) in the Stacks Project.

**`CochainComplex.filteredQuasiIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L330). The attribute's comment: “part (1)”. References: SGA 4 Vbis (2.5.1), “Σ: Gr\_n quasi-iso”; SGA 4½ Rapport (4.4), “filtered quasi-iso”.

> A morphism `α : K^• ⟶ L^•` of filtered cochain complexes of an abelian category `A` is a
> **filtered quasi-isomorphism** if `gr^p(α) : gr^p K^• ⟶ gr^p L^•` is a quasi-isomorphism for
> every `p : ℤ`, equivalently if `gr(α)` is a quasi-isomorphism.

```lean
public def filteredQuasiIso : MorphismProperty (FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
```

**`CochainComplex.filteredAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L336). The attribute's comment: “part (2)”.

> A filtered cochain complex `K^•` of an abelian category `A` is **filtered acyclic** if the
> complex `gr^p K^•` is acyclic for every `p : ℤ`, equivalently if `gr(K^•)` is acyclic.

```lean
public def filteredAcyclic : ObjectProperty (FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
```

## Tag 05S0, a lemma

[Tag 05S0](https://stacks.math.columbia.edu/tag/05S0) in the Stacks Project.

**`CategoryTheory.FiniteFilteredObject.homologyFunctor_gr_isHomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean#L114). The attribute's comment: “(1)”.

> **Stacks 05S0 (1).** The functor `K(Fil^f(𝒜)) ⥤ Gr(𝒜)`, `K^• ↦ H^0(gr(K^•))`, is
> homological.

```lean
theorem homologyFunctor_gr_isHomological :
    ((gr (𝒜 := 𝒜)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      HomotopyCategory.homologyFunctor (GradedObject ℤ 𝒜) (ComplexShape.up ℤ) 0).IsHomological
```

**`CategoryTheory.FiniteFilteredObject.homologyFunctor_grP_isHomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean#L122). The attribute's comment: “(2)”.

> **Stacks 05S0 (2).** For every `p : ℤ`, the functor `K(Fil^f(𝒜)) ⥤ 𝒜`,
> `K^• ↦ H^0(gr^p(K^•))`, is homological.

```lean
theorem homologyFunctor_grP_isHomological (p : ℤ) :
    ((grP (𝒜 := 𝒜) p).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      HomotopyCategory.homologyFunctor 𝒜 (ComplexShape.up ℤ) 0).IsHomological
```

**`CategoryTheory.FiniteFilteredObject.homologyFunctor_forget_isHomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Homology.lean#L130). The attribute's comment: “(3)”.

> **Stacks 05S0 (3).** The functor `K(Fil^f(𝒜)) ⥤ 𝒜`, `K^• ↦ H^0((forget F)K^•)`, is
> homological.

```lean
theorem homologyFunctor_forget_isHomological :
    ((forget (𝒜 := 𝒜)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      HomotopyCategory.homologyFunctor 𝒜 (ComplexShape.up ℤ) 0).IsHomological
```

## Tag 05S1, a lemma

[Tag 05S1](https://stacks.math.columbia.edu/tag/05S1) in the Stacks Project.

**`CochainComplex.kernel_eq_filteredAcyclic_and_filteredQuasiIso_eq_inverseImage_isomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Localization.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Localization.lean#L260). References: SGA 4 Vbis (2.5.1), “Σ saturated”; SGA 4½ Etat 0 (2.4.1), “filtered complexes”.

> **Stacks 05S1.** Let `𝒜` be an abelian category. The filtered acyclic complexes
> `FAc(𝒜)` form a strictly full saturated (thick) subcategory of the filtered complexes of `𝒜`,
> whose corresponding saturated multiplicative system in the sense of [Stacks, Tag 05RL] is the
> class `FQis(𝒜)` of filtered quasi-isomorphisms: every localisation
> `L : K(Fil(𝒜)) ⥤ DF(𝒜)` at `FQis(𝒜)` has kernel exactly `FAc(𝒜)` and inverts exactly the
> filtered quasi-isomorphisms. Moreover each `H^n ∘ gr^p` inverts `FQis(𝒜)`, i.e. the homological
> functor `H^0 ∘ gr` factors through `L`.

```lean
public theorem kernel_eq_filteredAcyclic_and_filteredQuasiIso_eq_inverseImage_isomorphisms :
    (filteredAcyclic A).IsClosedUnderIsomorphisms ∧
      (filteredAcyclic A).IsStableUnderRetracts ∧
      (∀ (L : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ ⥤ D)
          [L.IsLocalization (filteredQuasiIso A)],
        L.kernel = filteredAcyclic A ∧
          filteredQuasiIso A = (MorphismProperty.isomorphisms D).inverseImage L) ∧
      (∀ p n : ℤ, (filteredQuasiIso A).IsInvertedBy
        (FilteredObject.gr p ⋙
          HomologicalComplex.homologyFunctor A (ComplexShape.up ℤ) n))
```

## Tag 05S2, a definition

[Tag 05S2](https://stacks.math.columbia.edu/tag/05S2) in the Stacks Project.

**`CochainComplex.FilteredDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L348).

> The **filtered derived category** `DF(A)` of an abelian category `A`: the localisation of
> `K(Fil^f(A))` at the class `FQis(A)` of filtered quasi-isomorphisms, equivalently the quotient
> `K(Fil^f(A))/FAc(A)` by the filtered acyclic complexes ([Stacks, Tag 05S1]). Here `K(Fil^f(A))` is
> modelled by the cochain complexes of `A` filtered by subcomplexes whose filtration is finite in
> each degree — for every `n` some `F^p K^n` is all of `K^n` and some `F^q K^n` is zero — and the
> localisation functor `Q : K(Fil^f(A)) ⥤ DF(A)` is `MorphismProperty.Q`, whose kernel is `FAc(A)`
> ([Stacks, Tag 05S1]). It is triangulated, with the structure induced along
> `K(Fil^f(A)) ⥤ DF(A)` (`CochainComplex.FilteredDerivedCategory.Qh`), which is exact.

```lean
public abbrev FilteredDerivedCategory
```

## Tag 05S3, a lemma

[Tag 05S3](https://stacks.math.columbia.edu/tag/05S3) in the Stacks Project.

**`CochainComplex.isIso_Q_map_gradedPiece_and_forget_of_filteredQuasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean#L610). References: SGA 4 Vbis (2.5.2), “more general”.

> **Stacks 05S3.** Let `𝒜` be an abelian category and let `α : K^• ⟶ L^•` be a filtered
> quasi-isomorphism of filtered cochain complexes of `𝒜`. Then, for every `p`, the localisation
> functor `Q : CochainComplex 𝒜 ℤ ⥤ D(𝒜)` inverts `gr^p(α)`; and if moreover the filtrations of
> `K^•` and of `L^•` are finite in each degree — `F^p K^n = K^n` for some `p` and `F^q K^n = 0` for
> some `q`, for each `n`, i.e. `K^•` and `L^•` are complexes of finitely filtered objects — then
> `Q` inverts the underlying morphism of complexes `(forget F)(α)` as well. Equivalently: the
> functors `gr^p ⋙ Q` and, on `K(Fil^f(𝒜))`, `(forget F) ⋙ Q` invert the filtered
> quasi-isomorphisms, so that each factors canonically through the filtered derived category
> `DF(𝒜)`, compatibly with the localisation functors; the statement about `gr` is the conjunction
> over all `p` of the statements about `gr^p`.

```lean
public theorem isIso_Q_map_gradedPiece_and_forget_of_filteredQuasiIso {A : Type u}
    [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    {K L : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ} (α : K ⟶ L)
    (hα : CochainComplex.filteredQuasiIso A α) :
    (∀ p : ℤ, IsIso (DerivedCategory.Q.map
        ((FilteredObject.gr p).map α))) ∧
      ((∀ n : ℤ, ∃ p q : ℤ, IsIso ((K.filtration.ι.app (op p)).f n) ∧
          IsZero ((K.filtration.obj (op q)).X n)) →
        (∀ n : ℤ, ∃ p q : ℤ, IsIso ((L.filtration.ι.app (op p)).f n) ∧
          IsZero ((L.filtration.obj (op q)).X n)) →
        IsIso (DerivedCategory.Q.map (FilteredObject.forget.map α)))
```

**`CochainComplex.quasiIso_hom_of_filteredQuasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean#L639). The attribute's comment: “the underlying morphism of complexes, as a quasi-isomorphism”. References: SGA 4 Vbis (2.5.2), “more general”.

> **A morphism of filtered complexes which is a quasi-isomorphism on every graded piece is a
> quasi-isomorphism**, provided both filtrations are finite in each degree. This is the second
> clause of [Stacks, Tag 05S3] read as a statement about the morphism of complexes rather than
> about its image in the derived category, which is the form the proofs of [Stacks, Tag 07LD] and
> [Stacks, Tag 0FKH] use when they conclude from the graded pieces. Unlike
> `CochainComplex.isIso_Q_map_gradedPiece_and_forget_of_filteredQuasiIso` it asks for no
> `HasDerivedCategory` instance: the mapping cone of `α.hom` is acyclic outright.
>
> Finiteness cannot be dropped: for the constant filtration `F^p K^• = K^•` every graded piece
> vanishes, so `0 ⟶ K^•` is a filtered quasi-isomorphism whose underlying morphism is not a
> quasi-isomorphism unless `K^•` is acyclic.

```lean
public theorem quasiIso_hom_of_filteredQuasiIso
    {K L : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ} (α : K ⟶ L)
    (hα : CochainComplex.filteredQuasiIso 𝒜 α)
    (hK : K.filtration.IsDegreewiseFinite) (hL : L.filtration.IsDegreewiseFinite) :
    QuasiIso α.hom
```

## Tag 05S4, a definition

[Tag 05S4](https://stacks.math.columbia.edu/tag/05S4) in the Stacks Project.

**`CochainComplex.filteredPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L361). The attribute's comment: “DF^+(A), the bounded below filtered derived category”.

> The filtered cochain complexes `X` of an abelian category `A` whose associated graded is
> bounded below, i.e. such that `H^n(gr(X)) = 0` for `n ≪ 0`: there is an `n : ℤ`, independent of
> `p`, with `H^i(gr^p X) = 0` for all `i < n` and all `p`. These are the objects of the **bounded
> below filtered derived category** `DF^{+}(A)`, the full subcategory of `DF(A)` on the objects `X`
> such that `gr(X)` lies in the bounded below derived category (`D^{+}(Gr(A))`, written `D^{+}(A)`
> in the source).

```lean
public def filteredPlus : ObjectProperty (FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
```

**`CochainComplex.filteredMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L371). The attribute's comment: “DF^-(A), the bounded above filtered derived category”.

> The filtered cochain complexes `X` of an abelian category `A` whose associated graded is
> bounded above, i.e. such that `H^n(gr(X)) = 0` for `n ≫ 0`: there is an `n : ℤ`, independent of
> `p`, with `H^i(gr^p X) = 0` for all `n < i` and all `p`. These are the objects of the **bounded
> above filtered derived category** `DF^{-}(A)`, the full subcategory of `DF(A)` on the objects `X`
> such that `gr(X)` lies in the bounded above derived category (`D^{-}(Gr(A))`, written `D^{-}(A)`
> in the source).

```lean
public def filteredMinus : ObjectProperty (FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
```

**`CochainComplex.filteredBounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L381). The attribute's comment: “DF^b(A), the bounded filtered derived category”.

> The filtered cochain complexes `X` of an abelian category `A` whose associated graded is
> bounded, i.e. such that `H^n(gr(X)) = 0` for `|n| ≫ 0`: there are `a b : ℤ`, independent of `p`,
> with `H^i(gr^p X) = 0` for `i < a` and for `b < i`, for every `p`. These are the objects of the
> **bounded filtered derived category** `DF^b(A)`, the full subcategory of `DF(A)` on the objects
> `X` such that `gr(X)` lies in the bounded derived category (`D^b(Gr(A))`, written `D^b(A)` in the
> source).

```lean
public def filteredBounded : ObjectProperty (FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
```

## Tag 05S5, a lemma

[Tag 05S5](https://stacks.math.columbia.edu/tag/05S5) in the Stacks Project.

**`CochainComplex.exists_filteredQuasiIso_bounded_of_isGE_of_isLE_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean, line 1238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Basic.lean#L1238).

> **Stacks 05S5.** Let `𝒜` be an abelian category and let `K^•` be a filtered cochain complex
> of `𝒜` whose filtration is finite in each degree, i.e. an object of `K(Fil^f(𝒜))`. Then, writing
> `gr^p` for the graded pieces of the filtration:
>
> 1. if `H^n(gr(K^•)) = 0` for all `n < a`, i.e. every `gr^p(K^•)` is cohomologically `≥ a`, there
>    is a filtered quasi-isomorphism `K^• ⟶ L^•` with `L^n = 0` for all `n < a`;
> 2. if `H^n(gr(K^•)) = 0` for all `n > b`, i.e. every `gr^p(K^•)` is cohomologically `≤ b`, there
>    is a filtered quasi-isomorphism `M^• ⟶ K^•` with `M^n = 0` for all `n > b`;
> 3. if `H^n(gr(K^•)) = 0` for all `n < a` and for all `n > b`, i.e. `H^n(gr(K^•)) = 0` for
>    `|n| ≫ 0`, there is a commutative square
>
>    ```
>    M^• ⟶ K^•
>     ↓       ↓
>    N^• ⟶ L^•
>    ```
>
>    of morphisms of filtered complexes all four of which are filtered quasi-isomorphisms, with
>    `L^•` bounded below (`L^n = 0` for `n < a`), `M^•` bounded above (`M^n = 0` for `n > b`) and
>    `N^•` bounded (`N^n = 0` for `n < a` and for `n > b`);
>
> and in each case the complexes produced again have finite filtration in each degree, i.e. lie in
> `K(Fil^f(𝒜))`.

```lean
public theorem exists_filteredQuasiIso_bounded_of_isGE_of_isLE_gradedPiece
    (K : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ)
    (hK : ∀ n : ℤ, ∃ p q : ℤ, IsIso ((K.filtration.ι.app (op p)).f n) ∧
      IsZero ((K.filtration.obj (op q)).X n)) :
    (∀ a : ℤ, (∀ p : ℤ, ((FilteredObject.gr p).obj K).IsGE a) →
        ∃ (L : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (α : K ⟶ L)
          (_ : CochainComplex.filteredQuasiIso 𝒜 α) (_ : L.X.IsStrictlyGE a),
          ∀ n : ℤ, ∃ p q : ℤ, IsIso ((L.filtration.ι.app (op p)).f n) ∧
            IsZero ((L.filtration.obj (op q)).X n)) ∧
      (∀ b : ℤ, (∀ p : ℤ, ((FilteredObject.gr p).obj K).IsLE b) →
        ∃ (M : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (α : M ⟶ K)
          (_ : CochainComplex.filteredQuasiIso 𝒜 α) (_ : M.X.IsStrictlyLE b),
          ∀ n : ℤ, ∃ p q : ℤ, IsIso ((M.filtration.ι.app (op p)).f n) ∧
            IsZero ((M.filtration.obj (op q)).X n)) ∧
      (∀ a b : ℤ, (∀ p : ℤ, ((FilteredObject.gr p).obj K).IsGE a) →
        (∀ p : ℤ, ((FilteredObject.gr p).obj K).IsLE b) →
        ∃ (L M N : FilteredObject (CochainComplex 𝒜 ℤ) ℤᵒᵖ) (f : M ⟶ K) (g : M ⟶ N) (h : K ⟶ L)
          (i : N ⟶ L) (_ : CommSq f g h i) (_ : CochainComplex.filteredQuasiIso 𝒜 f)
          (_ : CochainComplex.filteredQuasiIso 𝒜 g) (_ : CochainComplex.filteredQuasiIso 𝒜 h)
          (_ : CochainComplex.filteredQuasiIso 𝒜 i) (_ : L.X.IsStrictlyGE a)
          (_ : M.X.IsStrictlyLE b) (_ : N.X.IsStrictlyGE a) (_ : N.X.IsStrictlyLE b),
          (∀ n : ℤ, ∃ p q : ℤ, IsIso ((L.filtration.ι.app (op p)).f n) ∧
              IsZero ((L.filtration.obj (op q)).X n)) ∧
            (∀ n : ℤ, ∃ p q : ℤ, IsIso ((M.filtration.ι.app (op p)).f n) ∧
              IsZero ((M.filtration.obj (op q)).X n)) ∧
            (∀ n : ℤ, ∃ p q : ℤ, IsIso ((N.filtration.ι.app (op p)).f n) ∧
              IsZero ((N.filtration.obj (op q)).X n)))
```

## Tag 05S6, a lemma

[Tag 05S6](https://stacks.math.columbia.edu/tag/05S6) in the Stacks Project.

**`CochainComplex.FilteredDerivedCategory.isSaturated_filteredAcyclic_and_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/Basic.lean, line 1121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Basic.lean#L1121).

> Let `𝒜` be an abelian category. For every triangulated subcategory `P` of `K(Fil^f(𝒜))` — in
> particular for `K⁺(Fil^f(𝒜))`, `K⁻(Fil^f(𝒜))` and `Kᵇ(Fil^f(𝒜))` — the filtered acyclic objects
> `FAc_P(𝒜)` of `P` form a strictly full saturated triangulated subcategory of `P`, the filtered
> quasi-isomorphisms `FQis_P(𝒜)` of `P` form a saturated multiplicative system compatible with the
> triangulation which is the class `FAc_P(𝒜).trW` corresponding to `FAc_P(𝒜)` under
> [Stacks, Tag 05RL], and the kernel of any localisation of `P` at `FQis_P(𝒜)` is `FAc_P(𝒜)`.
> Moreover:
>
> 1. the functor `K⁺(Fil^f(𝒜)) ⥤ DF⁺(𝒜)` induced by `Qh : K(Fil^f(𝒜)) ⥤ DF(𝒜)` has kernel
>    `FAc⁺(𝒜)` and is a localisation at `FQis⁺(𝒜)`, so that
>    `K⁺(Fil^f(𝒜))/FAc⁺(𝒜) = FQis⁺(𝒜)⁻¹K⁺(Fil^f(𝒜)) ⥤ DF⁺(𝒜)` is an equivalence;
> 2. the functor `K⁻(Fil^f(𝒜)) ⥤ DF⁻(𝒜)` induced by `Qh` has kernel `FAc⁻(𝒜)` and is a
>    localisation at `FQis⁻(𝒜)`;
> 3. the functor `Kᵇ(Fil^f(𝒜)) ⥤ DFᵇ(𝒜)` induced by `Qh` has kernel `FAcᵇ(𝒜)` and is a
>    localisation at `FQisᵇ(𝒜)`.

```lean
public theorem isSaturated_filteredAcyclic_and_isLocalization :
    (∀ (P : ObjectProperty (HomotopyCategory (FiniteFilteredObject 𝒜) (.up ℤ))) [P.IsTriangulated]
        {D : Type*} [Category* D] (L : P.FullSubcategory ⥤ D)
        [L.IsLocalization ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage P.ι)],
      (((HomotopyCategory.filteredAcyclic 𝒜).inverseImage P.ι).IsClosedUnderIsomorphisms ∧
          ((HomotopyCategory.filteredAcyclic 𝒜).inverseImage P.ι).IsTriangulated ∧
          ((HomotopyCategory.filteredAcyclic 𝒜).inverseImage P.ι).IsSaturated) ∧
        (((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage P.ι).IsSaturated ∧
          ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage P.ι).IsCompatibleWithTriangulation ∧
          ((HomotopyCategory.filteredAcyclic 𝒜).inverseImage P.ι).trW =
            (HomotopyCategory.filteredQuasiIso 𝒜).inverseImage P.ι) ∧
        L.kernel = (HomotopyCategory.filteredAcyclic 𝒜).inverseImage P.ι) ∧
    (∃ F : HomotopyCategory.Plus (FiniteFilteredObject 𝒜) ⥤ (plus 𝒜).FullSubcategory,
      Nonempty (F ⋙ (plus 𝒜).ι ≅ HomotopyCategory.Plus.ι _ ⋙ Qh) ∧
        F.IsLocalization ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage
          (HomotopyCategory.Plus.ι _)) ∧
        F.kernel = (HomotopyCategory.filteredAcyclic 𝒜).inverseImage (HomotopyCategory.Plus.ι _)) ∧
    (∃ F : ((CochainComplex.minus _).strictMap
          (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).FullSubcategory ⥤
        (minus 𝒜).FullSubcategory,
      Nonempty (F ⋙ (minus 𝒜).ι ≅ ((CochainComplex.minus _).strictMap
          (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι ⋙ Qh) ∧
        F.IsLocalization ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage
          ((CochainComplex.minus _).strictMap
            (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι) ∧
        F.kernel = (HomotopyCategory.filteredAcyclic 𝒜).inverseImage
          ((CochainComplex.minus _).strictMap
            (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι) ∧
    (∃ F : ((CochainComplex.plus _ ⊓ CochainComplex.minus _).strictMap
          (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).FullSubcategory ⥤
        (bounded 𝒜).FullSubcategory,
      Nonempty (F ⋙ (bounded 𝒜).ι ≅ ((CochainComplex.plus _ ⊓ CochainComplex.minus _).strictMap
          (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι ⋙ Qh) ∧
        F.IsLocalization ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage
          ((CochainComplex.plus _ ⊓ CochainComplex.minus _).strictMap
            (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι) ∧
        F.kernel = (HomotopyCategory.filteredAcyclic 𝒜).inverseImage
          ((CochainComplex.plus _ ⊓ CochainComplex.minus _).strictMap
            (HomotopyCategory.quotient (FiniteFilteredObject 𝒜) (.up ℤ))).ι)
```

**`CochainComplex.FilteredDerivedCategory.isTriangulated_isLocalization_Qplus_Qminus_Qbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean#L281). The attribute's comment: “the equivalences are equivalences of triangulated categories”.

> The functors `K⁺(Fil^f(𝒜)) ⥤ DF⁺(𝒜)`, `K⁻(Fil^f(𝒜)) ⥤ DF⁻(𝒜)`
> and `Kᵇ(Fil^f(𝒜)) ⥤ DFᵇ(𝒜)` induced by `Qh` are exact localisations at `FQis⁺(𝒜)`,
> `FQis⁻(𝒜)`, `FQisᵇ(𝒜)`: so the induced equivalences
> `FQis^*(𝒜)⁻¹K^*(Fil^f(𝒜)) ⥤ DF^*(𝒜)` are equivalences of triangulated categories.

```lean
theorem isTriangulated_isLocalization_Qplus_Qminus_Qbounded :
    ((Qplus (𝒜 := 𝒜)).IsTriangulated ∧ (Qplus (𝒜 := 𝒜)).IsLocalization
        ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage (HomotopyCategory.Plus.ι _))) ∧
      ((Qminus (𝒜 := 𝒜)).IsTriangulated ∧ (Qminus (𝒜 := 𝒜)).IsLocalization
        ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage (Kminus (𝒜 := 𝒜)).ι)) ∧
      ((Qbounded (𝒜 := 𝒜)).IsTriangulated ∧ (Qbounded (𝒜 := 𝒜)).IsLocalization
        ((HomotopyCategory.filteredQuasiIso 𝒜).inverseImage (Kbounded (𝒜 := 𝒜)).ι))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.13, Tag 05RX](https://stacks.math.columbia.edu/tag/05RX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
