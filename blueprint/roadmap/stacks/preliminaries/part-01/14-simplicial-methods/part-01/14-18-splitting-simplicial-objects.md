---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.SubobjectSplitting, CategoryTheory.SimplicialObject.Truncated.SubobjectSplitting, SSet.Splitting.existsUnique_equiv_nonDegenerate, SSet.injective_of_injective_on_nonDegenerate, SSet.surjective_of_surjective_on_nonDegenerate, SSet.bijective_of_bijective_on_nonDegenerate, SSet.skeleton_obj_eq_top_and_hasDimensionLE, CategoryTheory.SimplicialObject.exists_splitting_range_ι_eq_iInf_ker_δ
statement: formalized
proof: formalized
---

# 14.18 Splitting simplicial objects

Section 14.18 of the Stacks Project, [Tag 017O](https://stacks.math.columbia.edu/tag/017O). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 017P, a definition

[Tag 017P](https://stacks.math.columbia.edu/tag/017P) in the Stacks Project.

**`CategoryTheory.SimplicialObject.SubobjectSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L88). The attribute's comment: “the definition for full simplicial objects; a monomorphism represents each source subobject, and `Splitting.isColimit'` is exactly the displayed coproduct isomorphism”.

> **Stacks 017P**, for full simplicial objects.
> A splitting by subobjects is a Mathlib splitting whose structure maps `N(U_n) ⟶ U_n` are
> monomorphisms, so that they represent the subobjects required by the source definition.

```lean
structure SubobjectSplitting (X : SimplicialObject C) extends X.Splitting
```

**`CategoryTheory.SimplicialObject.Truncated.SubobjectSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L131). The attribute's comment: “the definition for truncated simplicial objects; the index category is the surjections `[n] → [m]`, automatically with `m ≤ n ≤ r`”.

> **Stacks 017P**, for truncated simplicial objects.
> A splitting of an `r`-truncated simplicial object consists of subobjects in every degree at most
> `r` whose images under all surjections form a coproduct decomposition in each truncated degree.

```lean
structure SubobjectSplitting {r : ℕ} (X : SimplicialObject.Truncated C r)
```

## Tag 017R, a lemma

[Tag 017R](https://stacks.math.columbia.edu/tag/017R) in the Stacks Project.

**`SSet.Splitting.existsUnique_equiv_nonDegenerate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L592).

> **Stacks 017R**.
> If `s` is a splitting of a simplicial set `X`, then for every `n` there is a unique bijection
> between `s.N n` and the set of nondegenerate `n`-simplices of `X` compatible with the maps `s.ι n`
> and `Subtype.val` to `X _⦋n⦌`.

```lean
public theorem Splitting.existsUnique_equiv_nonDegenerate (s : X.Splitting) (n : ℕ) :
    ∃! e : s.N n ≃ X.nonDegenerate n, ∀ x, (e x : X _⦋n⦌) = s.ι n x
```

## Tag 017S, a lemma

[Tag 017S](https://stacks.math.columbia.edu/tag/017S) in the Stacks Project.

**`SSet.injective_of_injective_on_nonDegenerate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean#L65). The attribute's comment: “(1)”.

> **Stacks 017S** (part 1).
> Let `f : U ⟶ V` be a morphism of simplicial sets sending nondegenerate simplices to
> nondegenerate simplices, whose induced map on nondegenerate simplices is injective. Then
> `f.app ⦋n⦌` is injective for every `n`.

```lean
theorem injective_of_injective_on_nonDegenerate
    {U V : SSet} (f : U ⟶ V)
    (ha : PreservesNonDegenerate f) (hb : InjectiveOnNonDegenerate f) :
    ∀ (n : ℕ), Function.Injective (f.app (Opposite.op ⦋n⦌))
```

**`SSet.surjective_of_surjective_on_nonDegenerate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean#L98). The attribute's comment: “(2)”.

> **Stacks 017S** (part 2).
> Let `f : U ⟶ V` be a morphism of simplicial sets whose induced map on nondegenerate simplices is
> surjective. Then `f.app ⦋n⦌` is surjective for every `n`.

```lean
theorem surjective_of_surjective_on_nonDegenerate
    {U V : SSet} (f : U ⟶ V)
    (hb : SurjectiveOnNonDegenerate f) :
    ∀ (n : ℕ), Function.Surjective (f.app (Opposite.op ⦋n⦌))
```

**`SSet.bijective_of_bijective_on_nonDegenerate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialSet/NonDegenerateSimplices.lean#L113). The attribute's comment: “(3)”.

> **Stacks 017S** (part 3).
> Let `f : U ⟶ V` be a morphism of simplicial sets sending nondegenerate simplices to
> nondegenerate simplices, whose induced map on nondegenerate simplices is both injective and
> surjective. Then `f.app ⦋n⦌` is bijective for every `n`.

```lean
theorem bijective_of_bijective_on_nonDegenerate
    {U V : SSet} (f : U ⟶ V)
    (ha : PreservesNonDegenerate f)
    (hbinj : InjectiveOnNonDegenerate f) (hbsurj : SurjectiveOnNonDegenerate f) :
    ∀ (n : ℕ), Function.Bijective (f.app (Opposite.op ⦋n⦌))
```

## Tag 017T, a lemma

[Tag 017T](https://stacks.math.columbia.edu/tag/017T) in the Stacks Project.

**`SSet.skeleton_obj_eq_top_and_hasDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 967](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L967).

> **Stacks 017T**.
> The sub-simplicial set generated by the simplices of `X` in degrees at most `n` is
> `X.skeleton (n + 1)`. It agrees with `X` through degree `n`, and every simplex in a higher degree
> is degenerate.

```lean
public theorem skeleton_obj_eq_top_and_hasDimensionLE (X : SSet.{u}) (n : ℕ) :
    (∀ i : ℕ, i ≤ n → (X.skeleton (n + 1)).obj (op (SimplexCategory.mk i)) = ⊤) ∧
      HasDimensionLE (X.skeleton (n + 1) : SSet) n
```

## Tag 017U, a lemma

[Tag 017U](https://stacks.math.columbia.edu/tag/017U) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_splitting_range_ι_eq_iInf_ker_δ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L504).

> **Stacks 017U**.
> Every simplicial abelian group `U` has a splitting whose nondegenerate part is `N(U_0) = U_0` and
> `N(U_m) = ⋂_{i = 0}^{m - 1} Ker(d^m_i)` for `m ≥ 1`, and this splitting is functorial: any morphism
> of simplicial abelian groups carries `N(U_m)` into `N(V_m)`.

```lean
public theorem exists_splitting_range_ι_eq_iInf_ker_δ :
    ∃ s : ∀ U : SimplicialObject AddCommGrpCat.{u}, U.Splitting,
      (∀ (U : SimplicialObject AddCommGrpCat.{u}) (n : ℕ), Mono ((s U).ι n)) ∧
      (∀ U : SimplicialObject AddCommGrpCat.{u}, ((s U).ι 0).hom.range = ⊤) ∧
      (∀ (U : SimplicialObject AddCommGrpCat.{u}) (n : ℕ), ((s U).ι (n + 1)).hom.range =
        ⨅ i : Fin (n + 1), (U.δ i.castSucc).hom.ker) ∧
      (∀ (U V : SimplicialObject AddCommGrpCat.{u}) (f : U ⟶ V) (n : ℕ),
        ∃ g : (s U).N n ⟶ (s V).N n, (s U).ι n ≫ f.app (op ⦋n⦌) = g ≫ (s V).ι n)
```

## Tag 017V, a lemma

[Tag 017V](https://stacks.math.columbia.edu/tag/017V) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_splittingFunctor_mk_ι_eq_inf_kernelSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L433).

> **Stacks 017V**.
> Every simplicial object `U` of an abelian category `A` has a splitting whose nondegenerate parts
> are `N(U₀) = U₀` and `N(U_{n + 1}) = ⋂_{i = 0}^{n} Ker(d^{n + 1}_i)`, and this splitting is
> functorial: the splittings are the values of a functor `SimplicialObject A ⥤ Split A` which is a
> section of the functor forgetting the splitting.

```lean
public theorem exists_splittingFunctor_mk_ι_eq_inf_kernelSubobject :
    ∃ F : SimplicialObject A ⥤ Split A,
      F ⋙ Split.forget A = 𝟭 (SimplicialObject A) ∧
      (∀ U : SimplicialObject A, IsIso ((F.obj U).s.ι 0)) ∧
      ∀ (U : SimplicialObject A) (n : ℕ), ∃ _ : Mono ((F.obj U).s.ι (n + 1)),
        Subobject.mk ((F.obj U).s.ι (n + 1)) =
          Finset.univ.inf
            fun i : Fin (n + 1) => kernelSubobject ((F.obj U).X.δ i.castSucc)
```

## Tag 017W, a lemma

[Tag 017W](https://stacks.math.columbia.edu/tag/017W) in the Stacks Project.

**`AlgebraicTopology.NormalizedMooreComplex.mono_epi_isIso_app_iff_map_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L639).

> **Stacks 017W**.
> The normalized Moore complex functor `N` of an abelian category reflects (and preserves) degreewise
> monomorphisms, epimorphisms and isomorphisms: for a morphism `f : U ⟶ V` of simplicial objects, `f`
> is a monomorphism in each degree if and only if `N(f)_m` is a monomorphism for every `m`, and
> likewise for epimorphisms and for isomorphisms.

```lean
public theorem NormalizedMooreComplex.mono_epi_isIso_app_iff_map_f (f : U ⟶ V) :
    ((∀ Δ : SimplexCategoryᵒᵖ, Mono (f.app Δ)) ↔
        ∀ m : ℕ, Mono (((normalizedMooreComplex A).map f).f m)) ∧
      ((∀ Δ : SimplexCategoryᵒᵖ, Epi (f.app Δ)) ↔
        ∀ m : ℕ, Epi (((normalizedMooreComplex A).map f).f m)) ∧
      ((∀ Δ : SimplexCategoryᵒᵖ, IsIso (f.app Δ)) ↔
        ∀ m : ℕ, IsIso (((normalizedMooreComplex A).map f).f m))
```

## Tag 017X, a lemma

[Tag 017X](https://stacks.math.columbia.edu/tag/017X) in the Stacks Project.

**`CategoryTheory.SimplicialObject.normalizedMoore_factors_arrow_comp_δ_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 849](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L849).

> **Stacks 017X**.
> The last face carries the Stacks-convention normalized Moore subobject in degree `n + 1` into the
> normalized Moore subobject in degree `n`.

```lean
theorem normalizedMoore_factors_arrow_comp_δ_last (U : SimplicialObject C) (n : ℕ) :
    (normalizedMoore U n).Factors
      ((normalizedMoore U (n + 1)).arrow ≫ U.δ (Fin.last (n + 1)))
```

## Tag 017Y, a lemma

[Tag 017Y](https://stacks.math.columbia.edu/tag/017Y) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Usub_isSubSimplicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L751). The attribute's comment: “(1)”.

> **Stacks 017Y** (1).
> `U'` is a sub simplicial object of `U`: for every order-preserving map `ψ : [m'] → [m]` the
> morphism `U(ψ) : U_m → U_{m'}` maps `U'_m` into `U'_{m'}`, that is, the composite
> `(U'_m).arrow ≫ U(ψ)` factors through `U'_{m'}`.

```lean
theorem Usub_isSubSimplicial (U : SimplicialObject C) (n m m' : ℕ)
    (ψ : SimplexCategory.mk m' ⟶ SimplexCategory.mk m) :
    (Usub U n m').Factors ((Usub U n m).arrow ≫ U.map ψ.op)
```

**`CategoryTheory.SimplicialObject.Usub_eq_top_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L770). The attribute's comment: “(2)”.

> **Stacks 017Y** (2).
> For every `i ≤ n` one has `U'_i = U_i`, that is, `U'_i` is the top subobject of `U_i`.

```lean
theorem Usub_eq_top_of_le (U : SimplicialObject C) (n i : ℕ) (h : i ≤ n) :
    Usub U n i = ⊤
```

**`CategoryTheory.SimplicialObject.Usub_inf_moore_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean, line 927](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Split.lean#L927). The attribute's comment: “(3)”.

> **Stacks 017Y** (3).
> For every `m > n` one has `N(U'_m) = 0`. By the splitting of [Stacks, Tag 017V] one has
> `N(U'_m) = U'_m ∩ N(U_m)` as subobjects of `U_m`, so the assertion is that the intersection
> `U'_m ⊓ N(U_m)` is the zero subobject.

```lean
theorem Usub_inf_moore_eq_bot (U : SimplicialObject C) (n m : ℕ) (h : n < m) :
    Usub U n m ⊓ normalizedMoore U m = ⊥
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.18, Tag 017O](https://stacks.math.columbia.edu/tag/017O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
