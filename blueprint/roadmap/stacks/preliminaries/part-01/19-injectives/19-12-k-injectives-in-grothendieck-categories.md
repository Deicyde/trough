---
declaration: section
origin: cited
lean: Stacks.Injectives.SmallSubobjectEpi.exists_subobject_epi_size_le, Stacks.Injectives.acyclicComplexSizeBound, Stacks.Injectives.exists_small_boundedAbove_acyclic_subcomplex, Stacks.Injectives.exists_epi_coproduct_small_boundedAbove_acyclic, Stacks.Injectives.isKInjective_of_small_boundedAbove_acyclic, Stacks.Injectives.isKInjective_of_injective_of_small_boundedAbove_acyclic, Stacks.Injectives.exists_functorial_termwise_mono_quasiIso_homotopy_zero, Stacks.Injectives.exists_functorialInjectiveResolution
statement: formalized
proof: formalized
---

# 19.12 K-injectives in Grothendieck categories

Section 19.12 of the Stacks Project, [Tag 079I](https://stacks.math.columbia.edu/tag/079I). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 079J, a lemma

[Tag 079J](https://stacks.math.columbia.edu/tag/079J) in the Stacks Project.

**`Stacks.Injectives.SmallSubobjectEpi.exists_subobject_epi_size_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Size/SmallSubobjectEpi.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Size/SmallSubobjectEpi.lean#L259).

> Let `C` be a Grothendieck abelian category with generator `separator C`. For every
> epimorphism `π : M ⟶ N` there is a subobject `M' ⊆ M` such that `M'.arrow ≫ π` is an
> epimorphism and `size M' ≤ cardFn (separator C) (size N)`.

```lean
theorem exists_subobject_epi_size_le
    (M N : C) (π : M ⟶ N) [Epi π] :
    ∃ M' : Subobject M,
      Epi (M'.arrow ≫ π) ∧
      size ((M' : C)) ≤ cardFn (separator C) (size N)
```

## Tag 079K, a lemma

[Tag 079K](https://stacks.math.columbia.edu/tag/079K) in the Stacks Project.

**`Stacks.Injectives.acyclicComplexSizeBound`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean#L62). The attribute's comment: “the cardinal”.

> A cardinal which uniformly bounds the sizes of the terms of the small bounded-above acyclic
> complexes: the supremum over `n` of the `(n + 1)`-st iterate of `κ ↦ #(Subobject (∐_κ U))` at
> `#(Subobject U)`, where `U` is the separator of `C`.

```lean
noncomputable def acyclicComplexSizeBound (C : Type u) [Category.{v} C] [Abelian C]
    [IsGrothendieckAbelian.{w} C] : Cardinal.{w}
```

**`Stacks.Injectives.exists_small_boundedAbove_acyclic_subcomplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean#L447). The attribute's comment: “part (1)”.

> Every nonzero acyclic complex contains a nonzero bounded-above acyclic subcomplex
> whose terms have uniformly bounded size.

```lean
theorem exists_small_boundedAbove_acyclic_subcomplex
    (M : CochainComplex C ℤ) (hM : M.Acyclic) (hM₀ : ¬ IsZero M) :
    ∃ (N : CochainComplex C ℤ) (f : N ⟶ M),
      Mono f ∧
      ¬ IsZero N ∧
      N.Acyclic ∧
      (∃ a : ℤ, ∀ n : ℤ, a < n → IsZero (N.X n)) ∧
      ∀ n : ℤ, Cardinal.mk (Shrink.{w} (Subobject (N.X n))) ≤
        acyclicComplexSizeBound (C := C)
```

**`Stacks.Injectives.exists_epi_coproduct_small_boundedAbove_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/SmallAcyclicComplexes.lean#L475). The attribute's comment: “part (2)”.

> Every acyclic complex is an epimorphic image of a coproduct of bounded-above
> acyclic complexes whose terms have uniformly bounded size.

```lean
theorem exists_epi_coproduct_small_boundedAbove_acyclic
    (M : CochainComplex C ℤ) (hM : M.Acyclic) :
    ∃ (I : Type w) (N : I → CochainComplex C ℤ)
      (f : (∐ fun i ↦ N i) ⟶ M),
      Epi f ∧
      ∀ i : I,
        (N i).Acyclic ∧
        (∃ a : ℤ, ∀ n : ℤ, a < n → IsZero ((N i).X n)) ∧
        ∀ n : ℤ,
          Cardinal.mk (Shrink.{w} (Subobject ((N i).X n))) ≤
            acyclicComplexSizeBound (C := C)
```

## Tag 079L, a lemma

[Tag 079L](https://stacks.math.columbia.edu/tag/079L) in the Stacks Project.

**`Stacks.Injectives.isKInjective_of_small_boundedAbove_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/Criterion.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/Criterion.lean#L686).

> A complex of injective objects is K-injective provided that all maps to it from
> bounded-above acyclic complexes within the uniform size bound are null-homotopic.

```lean
theorem isKInjective_of_small_boundedAbove_acyclic (I : CochainComplex C ℤ)
    (hI : ∀ n : ℤ, Injective (I.X n))
    (hvanish : ∀ (M : CochainComplex C ℤ), M.Acyclic →
      (∃ a : ℤ, ∀ n : ℤ, a < n → IsZero (M.X n)) →
      (∀ n : ℤ, Cardinal.mk (Shrink.{w} (Subobject (M.X n))) ≤
        acyclicComplexSizeBound (C := C)) →
      ∀ f : M ⟶ I, Nonempty (Homotopy f 0)) :
    I.IsKInjective
```

**`Stacks.Injectives.isKInjective_of_injective_of_small_boundedAbove_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/Criterion.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/Criterion.lean#L765).

> A complex of injective objects in a Grothendieck abelian category is K-injective if every
> map to it in the homotopy category from a uniformly small bounded-above acyclic complex is zero.

```lean
theorem isKInjective_of_injective_of_small_boundedAbove_acyclic
    (I : CochainComplex C ℤ) [∀ n : ℤ, Injective (I.X n)]
    (hI : ∀ (M : CochainComplex C ℤ), M.Acyclic →
      (∃ a : ℤ, ∀ n : ℤ, a < n → IsZero (M.X n)) →
      (∀ n : ℤ, Cardinal.mk (Shrink.{w} (Subobject (M.X n))) ≤
        acyclicComplexSizeBound (C := C)) →
      ∀ f : (HomotopyCategory.quotient C (ComplexShape.up ℤ)).obj M ⟶
        (HomotopyCategory.quotient C (ComplexShape.up ℤ)).obj I, f = 0) :
    I.IsKInjective
```

## Tag 079M, a lemma

[Tag 079M](https://stacks.math.columbia.edu/tag/079M) in the Stacks Project.

**`Stacks.Injectives.exists_functorial_termwise_mono_quasiIso_homotopy_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialHomotopies.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialHomotopies.lean#L46).

> **Stacks Project, Tag 079M.** For a set of acyclic cochain complexes, there is a
> functorial termwise monomorphic quasi-isomorphism such that postcomposing any map from one
> of the given complexes makes that map null-homotopic.

```lean
theorem exists_functorial_termwise_mono_quasiIso_homotopy_zero
    {I : Type w} (K : I → CochainComplex C ℤ) (hK : ∀ i, (K i).Acyclic) :
    ∃ (F : CochainComplex C ℤ ⥤ CochainComplex C ℤ)
      (j : Functor.id (CochainComplex C ℤ) ⟶ F),
      (∀ (M : CochainComplex C ℤ) (n : ℤ), Mono ((j.app M).f n)) ∧
      (∀ M : CochainComplex C ℤ, QuasiIso (j.app M)) ∧
      ∀ (M : CochainComplex C ℤ) (i : I) (f : K i ⟶ M),
        homotopic C (ComplexShape.up ℤ) (f ≫ j.app M) 0
```

## Tag 079N, a lemma

[Tag 079N](https://stacks.math.columbia.edu/tag/079N) in the Stacks Project.

**`Stacks.Injectives.exists_functorialInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/Enlargement.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/Enlargement.lean#L681).

> A Grothendieck abelian category admits a functorial termwise monomorphic quasi-isomorphism
> from every cochain complex to one whose map in each degree factors through an injective
> subobject.

```lean
theorem exists_functorialInjectiveResolution [IsGrothendieckAbelian.{w} C] :
    Nonempty (FunctorialInjectiveResolution C)
```

**`Stacks.Injectives.FunctorialEnlargement.exists_functorialInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Spaltenstein/Enlargement.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Spaltenstein/Enlargement.lean#L685).

> **Stacks Project, Tag 079N.**  A Grothendieck abelian category admits a functorial
> injective enlargement of unbounded cochain complexes: a functor on `CochainComplex C ℤ`
> together with a natural inclusion which is a monomorphism in every degree, a
> quasi-isomorphism, and which in each degree factors through an injective subobject of the
> corresponding term of the enlargement.
>
> This discharges the hypothesis of [Stacks, Tag 079P], which the tree states relative to
> exactly this datum.

```lean
theorem exists_functorialInjectiveResolution :
    Nonempty (Stacks.Injectives.KInjectiveResolution.FunctorialInjectiveResolution C)
```

## Tag 079P, a theorem

[Tag 079P](https://stacks.math.columbia.edu/tag/079P) in the Stacks Project.

**`Stacks.Injectives.exists_functorial_quasiIso_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean, line 1198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean#L1198). The attribute's comment: “existence and functoriality”.

> Functorial K-injective resolutions exist in a Grothendieck abelian category.

```lean
theorem exists_functorial_quasiIso_isKInjective :
    Nonempty (FunctorialKInjectiveResolution C)
```

**`Stacks.Injectives.kInjectiveResolutionInclusion_quasiIso`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean, line 1372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean#L1372). The attribute's comment: “quasi-isomorphism”.

> The inclusion into the chosen K-injective resolution is a quasi-isomorphism.

```lean
noncomputable instance kInjectiveResolutionInclusion_quasiIso
    (M : CochainComplex C ℤ) :
    QuasiIso ((kInjectiveResolutionInclusion C).app M)
```

**`Stacks.Injectives.kInjectiveResolutionInclusion_f_mono`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean, line 1379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean#L1379). The attribute's comment: “termwise monomorphism”.

> The inclusion into the chosen K-injective resolution is termwise monic.

```lean
noncomputable instance kInjectiveResolutionInclusion_f_mono
    (M : CochainComplex C ℤ) (n : ℤ) :
    Mono (((kInjectiveResolutionInclusion C).app M).f n)
```

**`Stacks.Injectives.kInjectiveResolutionFunctor_obj_X_injective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean, line 1386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean#L1386). The attribute's comment: “injective terms”.

> Every term of the chosen resolution is an injective object.

```lean
noncomputable instance kInjectiveResolutionFunctor_obj_X_injective
    (M : CochainComplex C ℤ) (n : ℤ) :
    Injective (((kInjectiveResolutionFunctor C).obj M).X n)
```

**`Stacks.Injectives.kInjectiveResolutionFunctor_obj_isKInjective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean, line 1393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/KInjective/FunctorialResolution.lean#L1393). The attribute's comment: “K-injective target”.

> The chosen resolution is K-injective.

```lean
noncomputable instance kInjectiveResolutionFunctor_obj_isKInjective
    (M : CochainComplex C ℤ) :
    ((kInjectiveResolutionFunctor C).obj M).IsKInjective
```

**`Stacks.Injectives.FunctorialEnlargement.exists_functorial_quasiIso_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Spaltenstein/Enlargement.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Spaltenstein/Enlargement.lean#L706). The attribute's comment: “existence and functoriality”. References: SGA 2 VIII (1.4), “more general”.

> **Stacks Project, Tag 079P**, unconditionally.  Functorial K-injective resolutions
> exist in a Grothendieck abelian category: every complex `M` admits, functorially in `M`, a
> termwise monomorphic quasi-isomorphism into a K-injective complex with injective terms.
>
> The tree proves this relative to the Tag 079N datum
> (`exists_functorial_quasiIso_isKInjective_of_functorialInjectiveResolution`);
> `exists_functorialInjectiveResolution` supplies the datum.

```lean
theorem exists_functorial_quasiIso_isKInjective :
    Nonempty (Stacks.Injectives.KInjectiveResolution.FunctorialKInjectiveResolution C)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.12, Tag 079I](https://stacks.math.columbia.edu/tag/079I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
