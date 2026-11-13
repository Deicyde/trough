---
declaration: section
origin: cited
lean: IsAbsolutelyFlat, flat_of_flat_of_mul_flat, HasWeakDimensionLE, hasWeakDimensionLE_of_weaklyEtale, absolutelyFlat_tfae, product_of_fields_absolutely_flat, mulFlat_baseChange, weaklyEtale_baseChange
statement: formalized
proof: formalized
---

# 15.106 Weakly étale ring maps

Section 15.106 of the Stacks Project, [Tag 092A](https://stacks.math.columbia.edu/tag/092A). 24 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 092B, a definition

[Tag 092B](https://stacks.math.columbia.edu/tag/092B) in the Stacks Project.

**`IsAbsolutelyFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean#L85).

> **Stacks 092B.** A commutative ring is absolutely flat if every module over it is flat.

```lean
abbrev IsAbsolutelyFlat (A : Type u) [CommRing A] : Prop
```

## Tag 092C, a lemma

[Tag 092C](https://stacks.math.columbia.edu/tag/092C) in the Stacks Project.

**`flat_of_flat_of_mul_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Flat.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Flat.lean#L431).

> **Stacks Tag 092C.** Let `A → B` be a ring map such that the multiplication
> map `μ : B ⊗_A B → B` makes `B` a flat `(B ⊗_A B)`-module. Let `N` be a
> `B`-module. If `N` is flat as an `A`-module, then `N` is flat as a
> `B`-module.

```lean
theorem flat_of_flat_of_mul_flat
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B]
    (hB : Algebra.MulFlat A B)
    (N : Type*) [AddCommGroup N] [Module B N]
    [Module A N] [IsScalarTower A B N]
    (hN : Module.Flat A N) :
    Module.Flat B N
```

## Tag 092D, a definition

[Tag 092D](https://stacks.math.columbia.edu/tag/092D) in the Stacks Project.

**`HasWeakDimensionLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Defs.lean#L53).

> A commutative ring has weak dimension at most `d` if every module over it has Tor
> dimension at most `d`.

```lean
def HasWeakDimensionLE {A : Type u} [CommRing A]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        ((tensoringRight (ModuleCat.{u} A)).obj N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ)))
    (d : ℕ) : Prop
```

## Tag 092E, a lemma

[Tag 092E](https://stacks.math.columbia.edu/tag/092E) in the Stacks Project.

**`hasWeakDimensionLE_of_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeakDimension/WeaklyEtale.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeakDimension/WeaklyEtale.lean#L455).

> **Stacks Tag 092E.** A weakly étale algebra over a commutative ring of weak dimension at most
> `d` also has weak dimension at most `d`.

```lean
theorem hasWeakDimensionLE_of_weaklyEtale
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    (derivedTensorA :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparisonA : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensorA.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        ((tensoringRight (ModuleCat.{u} A)).obj N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedA : ∀ N : ModuleCat.{u} A,
      (derivedTensorA.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparisonA N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ)))
    (d : ℕ) (hAB : Algebra.WeaklyEtale A B)
    (hA : HasWeakDimensionLE derivedTensorA comparisonA isLeftDerivedA d) :
    ∃ (derivedTensorB :
        DerivedCategory (ModuleCat.{v} B) ⥤
          DerivedCategory (ModuleCat.{v} B) ⥤ DerivedCategory (ModuleCat.{v} B))
      (comparisonB : ∀ N : ModuleCat.{v} B,
        DerivedCategory.Q ⋙
            derivedTensorB.flip.obj
              ((DerivedCategory.singleFunctor (ModuleCat.{v} B) 0).obj N) ⟶
          ((tensoringRight (ModuleCat.{v} B)).obj N).mapHomologicalComplex
              (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      (isLeftDerivedB : ∀ N : ModuleCat.{v} B,
        (derivedTensorB.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{v} B) 0).obj N)).IsLeftDerivedFunctor
          (comparisonB N)
          (HomologicalComplex.quasiIso (ModuleCat.{v} B) (ComplexShape.up ℤ))),
      HasWeakDimensionLE derivedTensorB comparisonB isLeftDerivedB d
```

## Tag 092F, a lemma

[Tag 092F](https://stacks.math.columbia.edu/tag/092F) in the Stacks Project.

**`absolutelyFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean#L205).

> For a commutative ring `A`, the following are equivalent: `A` has weak dimension at most
> zero; `A` is absolutely flat; `A` is reduced and every prime ideal is maximal; and the
> localization of `A` at every prime ideal is a field.
>
> Weak dimension is `HasWeakDimensionLE`, which carries the derived tensor product, its comparison
> with termwise tensor product, and the universal property certifying that the comparison exhibits
> the derived tensor product as a total left derived functor. Those data are part of the statement,
> exactly as in the source and as in `weakDimensionLE_one_tfae` (Stacks 092S).

```lean
theorem absolutelyFlat_tfae (A : Type u) [CommRing A]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        ((tensoringRight (ModuleCat.{u} A)).obj N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    [ HasWeakDimensionLE derivedTensor comparison isLeftDerived 0,
      (∀ (M : Type u) [AddCommGroup M] [Module A M], Module.Flat A M),
      IsReduced A ∧ ∀ p : Ideal A, p.IsPrime → p.IsMaximal,
      ∀ (p : Ideal A) [p.IsPrime], IsField (Localization.AtPrime p) ].TFAE
```

## Tag 092G, a lemma

[Tag 092G](https://stacks.math.columbia.edu/tag/092G) in the Stacks Project.

**`product_of_fields_absolutely_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyFlat/ProductOfFields.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AbsolutelyFlat/ProductOfFields.lean#L162).

> **Stacks Tag 092G.** A product of fields is an absolutely flat ring: every module
> over `∏ i, K i` is flat.

```lean
theorem product_of_fields_absolutely_flat {I : Type*} (K : I → Type*) [∀ i, Field (K i)]
    (M : Type*) [AddCommGroup M] [Module (∀ i, K i) M] : Module.Flat (∀ i, K i) M
```

## Tag 092H, a lemma

[Tag 092H](https://stacks.math.columbia.edu/tag/092H) in the Stacks Project.

**`mulFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Basic.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Basic.lean#L113). The attribute's comment: “(1)”.

> If the multiplication map `μ_{B/A} : B ⊗[A] B → B` is flat, then the multiplication map
> `μ_{B'/A'} : B' ⊗[A'] B' → B'` of the base change `B' = A' ⊗[A] B` is flat.
>
> Under the canonical `A'`-algebra isomorphism
> `e : (A' ⊗[A] B) ⊗[A'] (A' ⊗[A] B) ≃ₐ[A'] A' ⊗[A] (B ⊗[A] B)` one has
> `μ_{B'/A'} = (id_{A'} ⊗ μ_{B/A}) ∘ e`, and `id_{A'} ⊗ μ_{B/A}` is flat by
> `RingHom.Flat.tensorProductMap`.

```lean
theorem mulFlat_baseChange (A : Type u₁) (B : Type u₂) (A' : Type u₃)
    [CommRing A] [CommRing B] [CommRing A']
    [Algebra A B] [Algebra A A']
    (h : Algebra.MulFlat A B) :
    Algebra.MulFlat A' (A' ⊗[A] B)
```

**`weaklyEtale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Basic.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Basic.lean#L123). The attribute's comment: “(2)”.

> If `A → B` is weakly étale, then `A' → B'` is weakly étale, where `B' = A' ⊗[A] B` is the
> base change. This is Mathlib's base-change instance for `Algebra.WeaklyEtale`.

```lean
theorem weaklyEtale_baseChange (A : Type u₁) (B : Type u₂) (A' : Type u₃)
    [CommRing A] [CommRing B] [CommRing A']
    [Algebra A B] [Algebra A A']
    (h : Algebra.WeaklyEtale A B) :
    Algebra.WeaklyEtale A' (A' ⊗[A] B)
```

## Tag 092I, a lemma

[Tag 092I](https://stacks.math.columbia.edu/tag/092I) in the Stacks Project.

**`absolutelyFlat_and_isReduced_of_flat_lmul'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AbsolutelyFlat/Basic.lean#L247).

> If the multiplication map `B ⊗[A] B → B` is flat, then an absolutely flat base
> ring makes `B` absolutely flat. Under the same hypothesis, if `A` is reduced and
> `A → B` is weakly étale, then `B` is reduced.

```lean
theorem absolutelyFlat_and_isReduced_of_flat_lmul'
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    (hμ : (Algebra.TensorProduct.lmul' A (S := B)).Flat) :
    ((∀ (M : Type u) [AddCommGroup M] [Module A M], Module.Flat A M) →
      ∀ (N : Type v) [AddCommGroup N] [Module B N], Module.Flat B N) ∧
    (IsReduced A → Algebra.WeaklyEtale A B → IsReduced B)
```

## Tag 092J, a lemma

[Tag 092J](https://stacks.math.columbia.edu/tag/092J) in the Stacks Project.

**`mulFlat_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Basic.lean#L138). The attribute's comment: “(1)”.

> If the multiplication maps `μ_{B/A}` and `μ_{C/B}` are both flat, then the multiplication
> map `μ_{C/A}` is flat.
>
> After reducing to a single universe with `Algebra.MulFlat.ulift_iff`, this is the
> factorisation `μ_{C/A} = μ_{C/B} ∘ (C ⊗_A C → C ⊗_B C)` together with
> `RingHom.Flat.mapOfCompatibleSMul` and `RingHom.Flat.comp`.

```lean
theorem mulFlat_comp (A : Type u₁) (B : Type u₂) (C : Type u₃) [CommRing A] [CommRing B]
    [CommRing C] [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.MulFlat A B) (hBC : Algebra.MulFlat B C) : Algebra.MulFlat A C
```

**`weaklyEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Basic.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Basic.lean#L146). The attribute's comment: “(2)”.

> If `A → B` and `B → C` are both weakly étale, then the composite `A → C` is weakly étale.
> This is Mathlib's `Algebra.WeaklyEtale.trans`.

```lean
theorem weaklyEtale_comp (A B C : Type*) [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.WeaklyEtale A B) (hBC : Algebra.WeaklyEtale B C) :
    Algebra.WeaklyEtale A C
```

## Tag 092K, a lemma

[Tag 092K](https://stacks.math.columbia.edu/tag/092K) in the Stacks Project.

**`flat_lmul'_and_weaklyEtale_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Descent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Descent.lean#L98).

> Let `A → B → C` be compatible maps of commutative rings and suppose that `C` is
> faithfully flat over `B`. Then flatness of the multiplication map `C ⊗[A] C → C` descends
> to the multiplication map `B ⊗[A] B → B`; consequently, if `A → C` is weakly étale, then
> `A → B` is weakly étale.

```lean
theorem flat_lmul'_and_weaklyEtale_of_faithfullyFlat
    (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [Module.FaithfullyFlat B C] :
    ((Algebra.TensorProduct.lmul' A (S := C)).Flat →
      (Algebra.TensorProduct.lmul' A (S := B)).Flat) ∧
    (Algebra.WeaklyEtale A C → Algebra.WeaklyEtale A B)
```

## Tag 092L, a lemma

[Tag 092L](https://stacks.math.columbia.edu/tag/092L) in the Stacks Project.

**`weaklyEtale_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Descent.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Descent.lean#L145).

> If `A → B` and `A → C` are weakly étale, then a compatible algebra map `B → C`
> is weakly étale.

```lean
theorem weaklyEtale_of_comp (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.WeaklyEtale A B) (hAC : Algebra.WeaklyEtale A C) :
    Algebra.WeaklyEtale B C
```

## Tag 092M, a lemma

[Tag 092M](https://stacks.math.columbia.edu/tag/092M) in the Stacks Project.

**`formallyUnramified_of_flat_lmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/FormallyUnramified.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/FormallyUnramified.lean#L49).

> If the multiplication map `B ⊗[A] B → B` is flat, then `B` is formally unramified
> over `A`.

```lean
theorem formallyUnramified_of_flat_lmul (A : Type u) (B : Type v)
    [CommRing A] [CommRing B] [Algebra A B]
    (h : (Algebra.TensorProduct.lmul' A (S := B)).Flat) :
    Algebra.FormallyUnramified A B
```

## Tag 0CKP, a lemma

[Tag 0CKP](https://stacks.math.columbia.edu/tag/0CKP) in the Stacks Project.

**`unramified_of_finiteType_and_etale_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/FormallyUnramified.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/FormallyUnramified.lean#L66).

> If the multiplication map `B ⊗[A] B → B` is flat, finite type implies unramified and
> finite presentation together with flatness implies étale. In particular, every weakly étale
> algebra of finite presentation is étale.

```lean
theorem unramified_of_finiteType_and_etale_of_finitePresentation
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B] :
    ((Algebra.TensorProduct.lmul' A (S := B)).Flat →
      (Algebra.FiniteType A B → Algebra.Unramified A B) ∧
      (Algebra.FinitePresentation A B → Module.Flat A B → Algebra.Etale A B)) ∧
    (Algebra.WeaklyEtale A B →
      Algebra.FinitePresentation A B → Algebra.Etale A B)
```

## Tag 092N, a lemma

[Tag 092N](https://stacks.math.columbia.edu/tag/092N) in the Stacks Project.

**`weaklyEtale_of_isLocalization_etale_filteredColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Descent.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Descent.lean#L408).

> A localization and an étale algebra over a commutative ring are weakly étale, and an
> arbitrary filtered colimit of weakly étale algebras is weakly étale.

```lean
theorem weaklyEtale_of_isLocalization_etale_filteredColimit
    (A : Type u) [CommRing A] :
    (∀ (B : Type v) [CommRing B] [Algebra A B] (M : Submonoid A)
      [IsLocalization M B], Algebra.WeaklyEtale A B) ∧
    (∀ (B : Type v) [CommRing B] [Algebra A B] [Algebra.Etale A B],
      Algebra.WeaklyEtale A B) ∧
    (∀ (J : Type w) [SmallCategory J] [IsFiltered J] [Small.{max u (w + 1)} J]
      (F : J ⥤ CommAlgCat.{w} A) (c : Cocone F), IsColimit c →
      (∀ j, Algebra.WeaklyEtale A (F.obj j)) → Algebra.WeaklyEtale A c.pt)
```

## Tag 092P, a lemma

[Tag 092P](https://stacks.math.columbia.edu/tag/092P) in the Stacks Project.

**`isSeparable_of_flat_lmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Field.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Field.lean#L88).

> Let `L/K` be a field extension. If the multiplication map `L ⊗[K] L → L` is flat,
> then `L/K` is algebraic and separable.

```lean
theorem isSeparable_of_flat_lmul (K : Type u) (L : Type v)
    [Field K] [Field L] [Algebra K L]
    (h : (Algebra.TensorProduct.lmul' K (S := L)).Flat) :
    Algebra.IsSeparable K L
```

## Tag 092Q, a lemma

[Tag 092Q](https://stacks.math.columbia.edu/tag/092Q) in the Stacks Project.

**`flat_lmul_weaklyEtale_filteredColimitEtale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Field.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Field.lean#L362).

> Let `B` be an algebra over a field `K`. The following are equivalent: the multiplication
> map `B ⊗[K] B → B` is flat; `B` is weakly étale over `K`; and `B` is a filtered colimit of
> étale `K`-algebras. Under these equivalent conditions, every finitely generated
> `K`-subalgebra of `B` is étale over `K`.

```lean
theorem flat_lmul_weaklyEtale_filteredColimitEtale_tfae
    (K : Type u) (B : Type v) [Field K] [CommRing B] [Algebra K B] :
    [ (Algebra.TensorProduct.lmul' K (S := B)).Flat,
      Algebra.WeaklyEtale K B,
      ∃ (J : Type v) (_ : SmallCategory J) (_ : IsFiltered J)
        (F : J ⥤ CommAlgCat.{v} K) (c : Cocone F) (_ : IsColimit c),
        Nonempty (c.pt ≅ CommAlgCat.of K B) ∧ ∀ j, Algebra.Etale K (F.obj j) ].TFAE ∧
      ((Algebra.TensorProduct.lmul' K (S := B)).Flat →
        ∀ A : Subalgebra K B, A.FG → Algebra.Etale K A)
```

## Tag 092R, a lemma

[Tag 092R](https://stacks.math.columbia.edu/tag/092R) in the Stacks Project.

**`isSeparable_and_isAlgebraic_residueField_of_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/ResidueField.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/ResidueField.lean#L86).

> If `A → B` is weakly étale and a prime `q` of `B` lies over a prime `p` of `A`, then the
> canonical residue field extension `κ(p) → κ(q)` is separable algebraic.

```lean
theorem isSeparable_and_isAlgebraic_residueField_of_weaklyEtale
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    (h : Algebra.WeaklyEtale A B) (p : Ideal A) [p.IsPrime]
    (q : Ideal B) [q.IsPrime] (hpq : p = q.comap (algebraMap A B)) :
    letI := (Ideal.ResidueField.map p q (algebraMap A B) hpq).toAlgebra
    Algebra.IsSeparable p.ResidueField q.ResidueField ∧
      Algebra.IsAlgebraic p.ResidueField q.ResidueField
```

## Tag 092S, a lemma

[Tag 092S](https://stacks.math.columbia.edu/tag/092S) in the Stacks Project.

**`weakDimensionLE_one_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeakDimension/DimensionOne.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeakDimension/DimensionOne.lean#L377).

> **Stacks Tag 092S.** For a commutative ring, weak dimension at most one, flatness of all
> ideals, flatness of all finitely generated ideals, flatness of submodules of flat modules, and
> the valuation-ring property for all localizations at prime ideals are equivalent.

```lean
theorem weakDimensionLE_one_tfae
    (A : Type u) [CommRing A]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        ((tensoringRight (ModuleCat.{u} A)).obj N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    List.TFAE
      [ HasWeakDimensionLE derivedTensor comparison isLeftDerived 1,
        ∀ I : Ideal A, Module.Flat A I,
        ∀ I : Ideal A, I.FG → Module.Flat A I,
        ∀ (M : Type u) [AddCommGroup M] [Module A M],
          Module.Flat A M → ∀ N : Submodule A M, Module.Flat A N,
        ∀ (p : Ideal A) [p.IsPrime],
          ∃ _ : IsDomain (Localization.AtPrime p),
            ValuationRing (Localization.AtPrime p) ]
```

## Tag 092T, a lemma

[Tag 092T](https://stacks.math.columbia.edu/tag/092T) in the Stacks Project.

**`weakDimensionLE_one_and_isLocalization_pi_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean#L208).

> A product of valuation rings has weak dimension at most one, and the product of their
> fraction fields is the localization at the componentwise non-zero-divisors.

```lean
theorem weakDimensionLE_one_and_isLocalization_pi_fractionRing
    (J : Type v) (A : J → Type u) (K : J → Type w)
    [∀ j, CommRing (A j)] [∀ j, IsDomain (A j)] [∀ j, ValuationRing (A j)]
    [∀ j, Field (K j)] [∀ j, Algebra (A j) (K j)] [∀ j, IsFractionRing (A j) (K j)] :
    HasWeakDimensionLEOne (∀ j, A j) ∧
      IsLocalization
        (.pi Set.univ (fun j ↦ nonZeroDivisors (A j)))
        (∀ j, K j)
```

## Tag 092U, a lemma

[Tag 092U](https://stacks.math.columbia.edu/tag/092U) in the Stacks Project.

**`exists_isPullback_with_weakDimensionLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean#L276).

> A normal domain and its fraction field fit into a cartesian square whose lower-left ring has
> weak dimension at most one and whose lower map is flat, injective, and a ring epimorphism.

```lean
theorem exists_isPullback_with_weakDimensionLE_one
    (A : Type u) [CommRing A] [IsDomain A] [IsIntegrallyClosed A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K] :
    ∃ (V L : Type (max u v)) (_ : CommRing V) (_ : CommRing L)
      (_ : Algebra A V) (_ : Algebra K L) (_ : Algebra V L)
      (_ : Module.Flat V L) (_ : Algebra.IsEpi V L),
      HasWeakDimensionLEOne V ∧
        Function.Injective (algebraMap V L) ∧
        IsPullback
          (CommRingCat.ofHom (algebraMap A K).ulift)
          (CommRingCat.ofHom
            ((algebraMap A V).comp ULift.ringEquiv.toRingHom))
          (CommRingCat.ofHom
            ((algebraMap K L).comp ULift.ringEquiv.toRingHom))
          (CommRingCat.ofHom (algebraMap V L))
```

## Tag 092V, a lemma

[Tag 092V](https://stacks.math.columbia.edu/tag/092V) in the Stacks Project.

**`isIntegrallyClosedIn_of_isEpi_of_flat_of_weakDimensionLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean#L242).

> A flat injective epimorphism of commutative rings whose source has weak dimension at most one
> makes the source integrally closed in the target.

```lean
theorem isIntegrallyClosedIn_of_isEpi_of_flat_of_weakDimensionLE_one
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [Module.Flat A B] [Algebra.IsEpi A B]
    (hA : HasWeakDimensionLEOne A)
    (hinjective : Function.Injective (algebraMap A B)) :
    IsIntegrallyClosedIn A B
```

## Tag 092W, a lemma

[Tag 092W](https://stacks.math.columbia.edu/tag/092W) in the Stacks Project.

**`isIntegrallyClosedIn_tensorProduct_fractionField_of_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean, line 740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/WeakDimension.lean#L740).

> A weakly étale algebra over a normal domain is integrally closed in its scalar extension
> to any fraction field of the domain.

```lean
theorem isIntegrallyClosedIn_tensorProduct_fractionField_of_weaklyEtale
    (A : Type u) (B : Type v) (K : Type w)
    [CommRing A] [CommRing B] [Field K] [Algebra A B] [Algebra A K]
    [IsDomain A] [IsIntegrallyClosed A] [IsFractionRing A K]
    (hAB : Algebra.WeaklyEtale A B) :
    IsIntegrallyClosedIn B (B ⊗[A] K)
```

## Tag 092X, a lemma

[Tag 092X](https://stacks.math.columbia.edu/tag/092X) in the Stacks Project.

**`RingHom.exists_henselianLocalRing_of_isIntegral_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/IntegralDomain.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/IntegralDomain.lean#L262).

> An integral homomorphism from a henselian local ring to a domain makes the target a
> henselian local ring and is a local homomorphism. If the source residue field is separably
> closed, then the target residue field is separably closed and its extension along the induced
> residue-field homomorphism is purely inseparable.

```lean
theorem RingHom.exists_henselianLocalRing_of_isIntegral_of_isDomain
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [HenselianLocalRing A] [IsDomain B] (f : A →+* B) (hf : f.IsIntegral) :
    ∃ (hB : HenselianLocalRing B) (hlocal : IsLocalHom f),
      letI : IsLocalRing B := hB.toIsLocalRing
      letI : IsLocalHom f := hlocal
      IsSepClosed (ResidueField A) →
        IsSepClosed (ResidueField B) ∧ (ResidueField.map f).IsPurelyInseparable
```

## Tag 092Z, a theorem

[Tag 092Z](https://stacks.math.columbia.edu/tag/092Z) in the Stacks Project.

**`bijective_algebraMap_of_weaklyEtale_of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/StrictlyHenselian.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/StrictlyHenselian.lean#L325).

> A local weakly étale algebra over a strictly henselian local ring has bijective structure
> homomorphism.

```lean
theorem bijective_algebraMap_of_weaklyEtale_of_isLocalHom
    (A : Type u) (B : Type v) [CommRing A] [HenselianLocalRing A]
    [IsSepClosed (ResidueField A)] [CommRing B] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)] (hAB : Algebra.WeaklyEtale A B) :
    Function.Bijective (algebraMap A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.106, Tag 092A](https://stacks.math.columbia.edu/tag/092A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
