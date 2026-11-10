---
declaration: section
origin: cited
lean: CategoryTheory.ShortComplex.exact_iff_exact_map_evaluation, CategoryTheory.SimplicialObject.Truncated.app_top_injective_and_exists_iff, CategoryTheory.SimplicialObject.eilenbergMacLane, CategoryTheory.SimplicialObject.EilenbergMacLane.emSplit, CategoryTheory.SimplicialObject.EilenbergMacLane.emShortComplex_shortExact, CategoryTheory.SimplicialObject.exists_mono_isColimit_sk
statement: formalized
proof: formalized
---

# 14.22 Simplicial objects in abelian categories

Section 14.22 of the Stacks Project, [Tag 018Y](https://stacks.math.columbia.edu/tag/018Y). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 018Z, a lemma

[Tag 018Z](https://stacks.math.columbia.edu/tag/018Z) in the Stacks Project.

**`CategoryTheory.ShortComplex.exact_iff_exact_map_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L83).

> **Stacks 018Z**.
> A short complex `S` of functors `J ⥤ A`, with `A` an abelian category, is exact if and only if
> evaluating it at each object `j` of `J` gives an exact short complex of `A`. For
> `J = SimplexCategoryᵒᵖ` (resp. `J = SimplexCategory`) this says that a sequence of (co)simplicial
> objects of `A` is exact if and only if it is exact in each degree.

```lean
public theorem exact_iff_exact_map_evaluation (S : ShortComplex (J ⥤ A)) :
    S.Exact ↔ ∀ j : J, (S.map ((evaluation J A).obj j)).Exact
```

## Tag 0190, a lemma

[Tag 0190](https://stacks.math.columbia.edu/tag/0190) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.app_top_injective_and_exists_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L269). The attribute's comment: “part (1): both hom-sets, with the vanishing conditions stated over all non-surjective (resp. non-injective) operators instead of the faces (resp. degeneracies)”.

> **Stacks 0190** (part 1).
> Let `U` be a `k`-truncated simplicial object of `C` with `U_i = 0` for `i < k`, and write
> `A = U_k`. Then for every `k`-truncated simplicial object `V`:
>
> * a morphism `U ⟶ V` is determined by its top component `A ⟶ V_k`, and a morphism `f : A ⟶ V_k`
>   is the top component of one if and only if `f ≫ V(φ) = 0` for every non-surjective
>   `φ : ⦋m⦌ ⟶ ⦋k⦌`, i.e. if and only if `d^k_i ∘ f = 0` for `i = 0, …, k`;
> * a morphism `V ⟶ U` is determined by its top component `V_k ⟶ A`, and a morphism `f : V_k ⟶ A`
>   is the top component of one if and only if `V(ψ) ≫ f = 0` for every non-injective
>   `ψ : ⦋k⦌ ⟶ ⦋m⦌`, i.e. if and only if `f ∘ s^{k-1}_i = 0` for `i = 0, …, k - 1`.

```lean
public theorem app_top_injective_and_exists_iff {k : ℕ} {U : SimplicialObject.Truncated C k}
    (hU : ∀ (m : ℕ) (hm : m < k), IsZero (U _⦋m,hm.le⦌ₖ)) (V : SimplicialObject.Truncated C k) :
    (Function.Injective (fun g : U ⟶ V => g.app (op ⦋k⦌ₖ)) ∧
      ∀ f : U _⦋k⦌ₖ ⟶ V _⦋k⦌ₖ, (∃ g : U ⟶ V, g.app (op ⦋k⦌ₖ) = f) ↔
        ∀ (m : SimplexCategory.Truncated k) (φ : m ⟶ ⦋k⦌ₖ),
          ¬ Function.Surjective φ.hom.toOrderHom → f ≫ V.map φ.op = 0) ∧
    (Function.Injective (fun g : V ⟶ U => g.app (op ⦋k⦌ₖ)) ∧
      ∀ f : V _⦋k⦌ₖ ⟶ U _⦋k⦌ₖ, (∃ g : V ⟶ U, g.app (op ⦋k⦌ₖ) = f) ↔
        ∀ (m : SimplexCategory.Truncated k) (ψ : ⦋k⦌ₖ ⟶ m),
          ¬ Function.Injective ψ.hom.toOrderHom → V.map ψ.op ≫ f = 0)
```

## Tag 0191, a definition

[Tag 0191](https://stacks.math.columbia.edu/tag/0191) in the Stacks Project.

**`CategoryTheory.SimplicialObject.eilenbergMacLane`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean#L66).

> **Stacks 0191**.
> For an object `A` of `C` and an integer `k ≥ 0`, the *Eilenberg-MacLane object* `K(A, k)` is
> `K(A, k) = i_{k!}U`, the left Kan extension along the inclusion of the `k`-truncated simplex
> category (equivalently, the image under the left adjoint of `k`-truncation) of the `k`-truncated
> simplicial object `U` of [Stacks, Tag 0190] with `U_i = 0` for `i < k`, `U_k = A` and all
> operators `U(φ)` zero except `U(id_⦋k⦌) = id_A`.

```lean
public noncomputable def eilenbergMacLane (A : C) (k : ℕ)
    [∀ F : (SimplexCategory.Truncated k)ᵒᵖ ⥤ C,
      (SimplexCategory.Truncated.inclusion k).op.HasLeftKanExtension F] :
    SimplicialObject C
```

## Tag 0192, a lemma

[Tag 0192](https://stacks.math.columbia.edu/tag/0192) in the Stacks Project.

**`CategoryTheory.SimplicialObject.EilenbergMacLane.emSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean#L697).

> **Stacks 0192**.
> The sequence `0 → K(A,k) → E → K(A,k+1) → 0` is term by term split exact: for each degree `n`
> the short complex obtained by evaluating it at `[n]` admits a splitting in `𝒜`.

```lean
theorem emSplit (A : 𝒜) (k : ℕ) (n : SimplexCategoryᵒᵖ) :
    Nonempty
      (((emShortComplex A k).map ((CategoryTheory.evaluation _ _).obj n)).Splitting)
```

**`CategoryTheory.SimplicialObject.EilenbergMacLane.emShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean, line 716](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean#L716).

> **Stacks 0192**.
> The sequence `0 → K(A,k) → E → K(A,k+1) → 0` is a short exact sequence of simplicial objects
> of `𝒜`.

```lean
theorem emShortComplex_shortExact (A : 𝒜) (k : ℕ) :
    (emShortComplex A k).ShortExact
```

## Tag 0193, a lemma

[Tag 0193](https://stacks.math.columbia.edu/tag/0193) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_mono_isColimit_sk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L361).

> **Stacks 0193**.
> Let `V` be a simplicial object of an abelian category `A`. Then there are monomorphisms
> `f n : i_{n!} sk_n V ⟶ i_{(n + 1)!} sk_{n + 1} V` between consecutive skeleta of `V` such that `V`,
> equipped with the canonical morphisms `i_{n!} sk_n V ⟶ V` (the counits of `i_{n!} ⊣ sk_n`), is the
> colimit of the resulting sequence: `V = colim_n i_{n!} sk_n V`.

```lean
public theorem exists_mono_isColimit_sk (V : SimplicialObject A) :
    ∃ (f : (n : ℕ) → (sk n).obj V ⟶ (sk (n + 1)).obj V)
      (ι : Functor.ofSequence (X := fun n ↦ (sk n).obj V) f ⟶ (Functor.const ℕ).obj V),
      (∀ n, Mono (f n)) ∧ (∀ n, ι.app n = (skAdj n).counit.app V) ∧
        Nonempty (IsColimit (Cocone.mk V ι))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.22, Tag 018Y](https://stacks.math.columbia.edu/tag/018Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
