---
declaration: section
origin: cited
lean: comparisonMap_not_injective, comparisonMap_not_surjective, Module.Finite.tfae_piRightHom_surjective, Module.FinitePresentation.tfae_piRightHom_bijective, LinearMap.exists_finitePresentation_factorization_of_rTensor_apply_eq_zero, Module.mittagLeffler_iff_piRightHom_injective, Submodule.exists_fg_isLeast_mem_range_rTensor_subtype_of_mittagLeffler, Function.Exact.mittagLeffler_M₁_and_mittagLeffler_M₂_of_forall_rTensor_injective
statement: formalized
proof: formalized
---

# 10.89 Interchanging direct products with tensor

Section 10.89 of the Stacks Project, [Tag 059H](https://stacks.math.columbia.edu/tag/059H). 11 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 059I, an example

[Tag 059I](https://stacks.math.columbia.edu/tag/059I) in the Stacks Project.

**`comparisonMap_not_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Basic.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Basic.lean#L519). The attribute's comment: “(1)”.

> **Statement 1 (the comparison map need not be injective).**
> With `Q_n = Z/(n+1)Z`, the canonical map
> `c : Q ⊗_Z (∏_n Z/(n+1)Z) → ∏_n (Q ⊗_Z Z/(n+1)Z)` is not injective.

```lean
theorem comparisonMap_not_injective :
    ¬ Function.Injective (tensorPiComparison (fun n : ℕ => ZMod (n + 1)))
```

**`comparisonMap_not_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Basic.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Basic.lean#L598). The attribute's comment: “(2)”.

> **Statement 2 (the comparison map need not be surjective).**
> With `Q_n = Z` and the identification `Q ⊗_Z Z ≅ Q`, the canonical map
> `c : Q ⊗_Z (∏_n Z) → ∏_n Q` is not surjective.

```lean
theorem comparisonMap_not_surjective :
    ¬ Function.Surjective comparisonMapQ
```

## Tag 059J, a proposition

[Tag 059J](https://stacks.math.columbia.edu/tag/059J) in the Stacks Project.

**`Module.Finite.tfae_piRightHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Finiteness/TensorProductPi.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Finiteness/TensorProductPi.lean#L330).

> **Stacks 059J.** Let `R` be a commutative ring and `M` an `R`-module. The following are
> equivalent: (1) `M` is finitely generated; (2) for every family `Q` of `R`-modules the canonical
> map `M ⊗[R] (∀ α, Q α) → ∀ α, M ⊗[R] Q α` is surjective; (3) for every `R`-module `Q` and every
> set `A` the canonical map `M ⊗[R] Q^A → (M ⊗[R] Q)^A` is surjective; (4) for every set `A` the
> canonical map `M ⊗[R] R^A → M^A` is surjective.

```lean
public theorem Module.Finite.tfae_piRightHom_surjective (R : Type u) [CommRing R] (M : Type v)
    [AddCommGroup M] [Module R M] :
    List.TFAE
      [Module.Finite R M,
        ∀ (A : Type v) (Q : A → Type v) [∀ α, AddCommGroup (Q α)] [∀ α, Module R (Q α)],
          Function.Surjective (TensorProduct.piRightHom R R M Q),
        ∀ (A : Type v) (Q : Type v) [AddCommGroup Q] [Module R Q],
          Function.Surjective (TensorProduct.piRightHom R R M fun _ : A ↦ Q),
        ∀ A : Type v, Function.Surjective (TensorProduct.piScalarRightHom R R M A)]
```

## Tag 059K, a proposition

[Tag 059K](https://stacks.math.columbia.edu/tag/059K) in the Stacks Project.

**`Module.FinitePresentation.tfae_piRightHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/TensorProductPi.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/FinitePresentation/TensorProductPi.lean#L444). The attribute's comment: “Test data in the universe of `M`, as in 059J; hence `Small.{v} R`. See the module docstring.”.

> **Stacks 059K.** Let `R` be a commutative ring and `M` an `R`-module. The following are
> equivalent: (1) `M` is finitely presented; (2) for every family `Q` of `R`-modules the canonical
> map `M ⊗[R] (∀ α, Q α) → ∀ α, M ⊗[R] Q α` is bijective; (3) for every `R`-module `Q` and every
> set `A` the canonical map `M ⊗[R] Q^A → (M ⊗[R] Q)^A` is bijective; (4) for every set `A` the
> canonical map `M ⊗[R] R^A → M^A` is bijective.

```lean
public theorem Module.FinitePresentation.tfae_piRightHom_bijective (R : Type u) [CommRing R]
    [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] :
    List.TFAE
      [Module.FinitePresentation R M,
        ∀ (A : Type v) (Q : A → Type v) [∀ α, AddCommGroup (Q α)] [∀ α, Module R (Q α)],
          Function.Bijective (TensorProduct.piRightHom R R M Q),
        ∀ (A : Type v) (Q : Type v) [AddCommGroup Q] [Module R Q],
          Function.Bijective (TensorProduct.piRightHom R R M fun _ : A ↦ Q),
        ∀ A : Type v, Function.Bijective (TensorProduct.piScalarRightHom R R M A)]
```

## Tag 059L, a lemma

[Tag 059L](https://stacks.math.columbia.edu/tag/059L) in the Stacks Project.

**`LinearMap.exists_finitePresentation_factorization_of_rTensor_apply_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/Factorization.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/FinitePresentation/Factorization.lean#L336). The attribute's comment: “The kernel conditions are elementwise, `x` being a single element; `f` factors through `f'` by the pinned equation `f = g ∘ₗ f'`.”.

> **Stacks 059L.** Let `R` be a commutative ring, `P` a finitely presented `R`-module,
> `f : P → M` a map of `R`-modules and `Q` an `R`-module, and let `x ∈ P ⊗ Q` be killed by
> `f ⊗ id_Q`. Then there are a finitely presented `R`-module `P'` and maps `f' : P → P'`,
> `g : P' → M` with `f = g ∘ f'` such that `x` is killed by `f' ⊗ id_Q`.

```lean
public theorem LinearMap.exists_finitePresentation_factorization_of_rTensor_apply_eq_zero
    {R : Type u} [CommRing R] [Small.{v} R] {P M : Type v} {Q : Type w} [AddCommGroup P]
    [Module R P] [AddCommGroup M] [Module R M] [AddCommGroup Q] [Module R Q]
    [Module.FinitePresentation R P] (f : P →ₗ[R] M) {x : P ⊗[R] Q}
    (hx : f.rTensor Q x = 0) :
    ∃ (P' : Type v) (_ : AddCommGroup P') (_ : Module R P')
      (_ : Module.FinitePresentation R P') (f' : P →ₗ[R] P') (g : P' →ₗ[R] M),
      f = g ∘ₗ f' ∧ f'.rTensor Q x = 0
```

## Tag 059M, a proposition

[Tag 059M](https://stacks.math.columbia.edu/tag/059M) in the Stacks Project.

**`Module.mittagLeffler_iff_piRightHom_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/TensorProductPi.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/TensorProductPi.lean#L336). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E; test data in the universe of `M`, as in 059J and 059K, whence `Small.{v} R`. See the module docstring.”.

> **Stacks 059M.** Let `R` be a commutative ring and `M` an `R`-module. Then `M` is
> Mittag-Leffler — every map `f : P → M` from a finitely presented `R`-module dominates and is
> dominated by a map `g : P → Q` into a finitely presented `R`-module, that is
> `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`, which is condition (1) of
> Proposition 059E — if and only if for every family `(Q α)` of `R`-modules the canonical map
> `M ⊗[R] (∀ α, Q α) → ∀ α, M ⊗[R] Q α` is injective.

```lean
public theorem Module.mittagLeffler_iff_piRightHom_injective (R : Type u) [CommRing R]
    [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      ∀ (A : Type v) (Q : A → Type v) [∀ α, AddCommGroup (Q α)] [∀ α, Module R (Q α)],
        Function.Injective (TensorProduct.piRightHom R R M Q)
```

## Tag 0AS6, a lemma

[Tag 0AS6](https://stacks.math.columbia.edu/tag/0AS6) in the Stacks Project.

**`Submodule.exists_fg_isLeast_mem_range_rTensor_subtype_of_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Flat.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Flat.lean#L283). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M and 05CQ; `x ∈ N ⊗_R M` is membership in the range of `N.subtype.rTensor M`, and `smallest` is `IsLeast`. Test data in the universe of `M` and `F`, whence `Small.{v} R`. See the module docstring.”.

> Let `R` be a commutative ring, let `M` be a flat Mittag-Leffler `R`-module, let `F` be an
> `R`-module and let `x ∈ F ⊗[R] M`. Then among the submodules `N ⊆ F` with `x ∈ N ⊗[R] M` — that is,
> with `x` in the range of `N ⊗[R] M → F ⊗[R] M` — there is a smallest one, and it is a finite
> `R`-module.
>
> Being Mittag-Leffler is spelled out inline as condition (1) of Proposition 059E: every map
> `f : P → M` from a finitely presented `R`-module dominates and is dominated by a map `g : P → Q`
> into a finitely presented `R`-module, that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every
> `R`-module `N`.

```lean
public theorem Submodule.exists_fg_isLeast_mem_range_rTensor_subtype_of_mittagLeffler
    {R : Type u} [CommRing R] [Small.{v} R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.Flat R M]
    (hML : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
    {F : Type v} [AddCommGroup F] [Module R F] (x : F ⊗[R] M) :
    ∃ F' : Submodule R F, F'.FG ∧
      IsLeast {N : Submodule R F | x ∈ LinearMap.range (N.subtype.rTensor M)} F'
```

## Tag 059N, a lemma

[Tag 059N](https://stacks.math.columbia.edu/tag/059N) in the Stacks Project.

**`Function.Exact.mittagLeffler_M₁_and_mittagLeffler_M₂_of_forall_rTensor_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/ShortExact.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/ShortExact.lean#L311). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M and 05CQ; universal exactness is `h`, `h₂` and injectivity of `f₁ ⊗ id_T` for every `T`, as in 058K (1). The two items are the two conjuncts.”.

> Let `0 → M₁ →[f₁] M₂ →[f₂] M₃ → 0` be a universally exact sequence of `R`-modules, that is, a
> short exact sequence for which `f₁ ⊗ id_T : M₁ ⊗ T → M₂ ⊗ T` is injective for every `R`-module `T`.
> Then (1) if `M₂` is Mittag-Leffler, so is `M₁`, and (2) if `M₁` and `M₃` are Mittag-Leffler, so is
> `M₂`. Being Mittag-Leffler is spelled out in the intrinsic form 059E (1): every map `f : P → M`
> from a finitely presented module dominates and is dominated by a map `g : P → Q` into a finitely
> presented module, domination meaning `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.

```lean
public theorem Function.Exact.mittagLeffler_M₁_and_mittagLeffler_M₂_of_forall_rTensor_injective
    {R : Type u} [CommRing R] [Small.{v} R] {M₁ M₂ M₃ : Type v} [AddCommGroup M₁] [Module R M₁]
    [AddCommGroup M₂] [Module R M₂] [AddCommGroup M₃] [Module R M₃] {f₁ : M₁ →ₗ[R] M₂}
    {f₂ : M₂ →ₗ[R] M₃} (h : Function.Exact f₁ f₂) (h₂ : Function.Surjective f₂)
    (hf₁ : ∀ (T : Type v) [AddCommGroup T] [Module R T], Function.Injective (f₁.rTensor T)) :
    ((∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
          (f : P →ₗ[R] M₂), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
            (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
              [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) →
        ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
          (f : P →ₗ[R] M₁), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
            (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
              [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ∧
      ((∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
            (f : P →ₗ[R] M₁), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
              (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
                [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) →
        (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
            (f : P →ₗ[R] M₃), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
              (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
                [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) →
        ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
          (f : P →ₗ[R] M₂), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
            (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
              [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
```

## Tag 0EGI, a lemma

[Tag 0EGI](https://stacks.math.columbia.edu/tag/0EGI) in the Stacks Project.

**`Module.mittagLeffler_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/ShortExact.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/ShortExact.lean#L552). The attribute's comment: “The exact sequence `M₁ → M₂ → M₃ → 0` with `M₁` finitely generated is stated as a surjection with finitely generated kernel, as in `Module.finitePresentation_of_surjective`; Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 05CQ and 0AS6, with test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> Let `R` be a commutative ring, let `M` be a Mittag-Leffler `R`-module — every map `f : P → M`
> from a finitely presented `R`-module dominates and is dominated by a map `g : P → Q` into a
> finitely presented `R`-module, that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`,
> which is condition (1) of Proposition 059E — and let `l : M → M'` be a surjective `R`-linear map
> whose kernel is finitely generated. Then `M'` is Mittag-Leffler.

```lean
public theorem Module.mittagLeffler_of_surjective {R : Type u} [CommRing R] [Small.{v} R]
    {M : Type v} [AddCommGroup M] [Module R M] {M' : Type v} [AddCommGroup M'] [Module R M']
    (hML : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
    (l : M →ₗ[R] M') (hl : Function.Surjective l) (hl' : (LinearMap.ker l).FG) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M'), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 0AS7, a lemma

[Tag 0AS7](https://stacks.math.columbia.edu/tag/0AS7) in the Stacks Project.

**`ModuleCat.mittagLeffler_pt_of_forall_mittagLeffler_of_forall_rTensor_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Colimit.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Colimit.lean#L393). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M and 059N; the directed system is a functor with a colimit cocone, as in 059E and 059W; universal injectivity of `f i j` is injectivity of `(F.map u).hom.rTensor T` for every `T`, as in 058K (1). See the module docstring.”.

> **Stacks 0AS7.** Let `R` be a commutative ring, let `F : J ⥤ ModuleCat R` be a directed system
> `(M i, f i j)` of `R`-modules over a nonempty directed preorder `J`, and let `c` be a colimit
> cocone on `F`, so that `M = c.pt` is `colim_{i ∈ J} M i`. Assume every transition map is
> universally injective, that is `f i j ⊗ id_T` is injective for every `R`-module `T`, and that every
> `M i` is Mittag-Leffler. Then `M` is Mittag-Leffler. Being Mittag-Leffler is spelled out in the
> intrinsic form 059E (1): every map `f : P → M` from a finitely presented module dominates and is
> dominated by a map `g : P → Q` into a finitely presented module, domination meaning
> `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.

```lean
public theorem ModuleCat.mittagLeffler_pt_of_forall_mittagLeffler_of_forall_rTensor_injective
    {R : Type u} [CommRing R] [Small.{v} R] {J : Type w} [Preorder J] [IsDirectedOrder J]
    [Nonempty J] {F : J ⥤ ModuleCat.{v} R}
    (hinj : ∀ ⦃i j : J⦄ (u : i ⟶ j) (T : Type v) [AddCommGroup T] [Module R T],
      Function.Injective ((F.map u).hom.rTensor T))
    (hML : ∀ i : J, ∀ (P : Type v) [AddCommGroup P] [Module R P]
        [Module.FinitePresentation R P] (f : P →ₗ[R] F.obj i),
      ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q) (_ : Module.FinitePresentation R Q)
        (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N] [Module R N],
          LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
    {c : Cocone F} (hc : IsColimit c) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] c.pt),
      ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q) (_ : Module.FinitePresentation R Q)
        (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N] [Module R N],
          LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 059P, a lemma

[Tag 059P](https://stacks.math.columbia.edu/tag/059P) in the Stacks Project.

**`Module.mittagLeffler_directSum_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/DirectSum.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/DirectSum.lean#L338). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N and 05CQ; the module is `Mathlib`'s `DirectSum`, as in `Module.Flat.directSum_iff`. No smallness of `R` is assumed, neither direction using it. See the module docstring.”.

> **Stacks 059P.** Let `R` be a commutative ring and `(M i)` a family of `R`-modules indexed by a
> type `ι`. Then the direct sum `⨁ i, M i` is Mittag-Leffler if and only if each `M i` is. Being
> Mittag-Leffler is spelled out in the intrinsic form 059E (1): every map `f : P → M` from a finitely
> presented module dominates and is dominated by a map `g : P → Q` into a finitely presented module,
> domination meaning `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`.

```lean
public theorem Module.mittagLeffler_directSum_iff (R : Type u) [CommRing R] {ι : Type v}
    (M : ι → Type v) [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)] :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] (⨁ i, M i)), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      ∀ i, ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M i), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 05CT, a lemma

[Tag 05CT](https://stacks.math.columbia.edu/tag/05CT) in the Stacks Project.

**`Module.mittagLeffler_trans_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/RestrictScalars.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/RestrictScalars.lean#L506). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N, 059P and 05CQ; flatness is `Module.Flat S M`. `S` and `M` share the universe of the test data, whence the single `Small.{v} R`. See the module docstring.”.

> **Stacks 05CT.** Let `R → S` be a ring map and let `M` be an `S`-module. If `S` is
> Mittag-Leffler as an `R`-module, and `M` is flat and Mittag-Leffler as an `S`-module, then `M` is
> Mittag-Leffler as an `R`-module. Being Mittag-Leffler is spelled out in the intrinsic form
> 059E (1): every map `f : P → M` from a finitely presented module dominates and is dominated by a
> map `g : P → Q` into a finitely presented module, domination meaning
> `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every test module `N`.

```lean
public theorem Module.mittagLeffler_trans_of_flat {R : Type u} {S M : Type v} [CommRing R]
    [CommRing S] [Algebra R S] [Small.{v} R] [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M] [Module.Flat S M]
    (hS : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] S), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N))
    (hM : ∀ (P : Type v) [AddCommGroup P] [Module S P] [Module.FinitePresentation S P]
      (f : P →ₗ[S] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module S Q)
        (_ : Module.FinitePresentation S Q) (g : P →ₗ[S] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module S N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.89, Tag 059H](https://stacks.math.columbia.edu/tag/059H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
