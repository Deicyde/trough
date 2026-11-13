---
declaration: section
origin: cited
lean: CategoryTheory.ShortComplex.exact_iff_exact_map_evaluation, CategoryTheory.SimplicialObject.mono_iff_mono_app, CategoryTheory.SimplicialObject.epi_iff_epi_app, CategoryTheory.CosimplicialObject.mono_iff_mono_app, CategoryTheory.CosimplicialObject.epi_iff_epi_app, CategoryTheory.Abelian.functorCategoryAbelian, CategoryTheory.SimplicialObject.EilenbergMacLane.eilenbergMacLaneIsoEmKAk, CategoryTheory.SimplicialObject.Truncated.app_top_injective_and_exists_iff_faces
statement: formalized
proof: formalized
---

# 14.22 Simplicial objects in abelian categories

Section 14.22 of the Stacks Project, [Tag 018Y](https://stacks.math.columbia.edu/tag/018Y). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 018Z, a lemma

[Tag 018Z](https://stacks.math.columbia.edu/tag/018Z) in the Stacks Project.

**`CategoryTheory.ShortComplex.exact_iff_exact_map_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L96). The attribute's comment: “(4): a sequence of (co)simplicial objects of an abelian category is exact if and only if it is exact in each degree, stated for functors `J ⥤ A` from any category `J`”.

> **Stacks 018Z (4)**.
> A short complex `S` of functors `J ⥤ A`, with `A` an abelian category, is exact if and only if
> evaluating it at each object `j` of `J` gives an exact short complex of `A`. For
> `J = SimplexCategoryᵒᵖ` (resp. `J = SimplexCategory`) this says that a sequence of (co)simplicial
> objects of `A` is exact if and only if it is exact in each degree.

```lean
public theorem exact_iff_exact_map_evaluation (S : ShortComplex (J ⥤ A)) :
    S.Exact ↔ ∀ j : J, (S.map ((evaluation J A).obj j)).Exact
```

**`CategoryTheory.SimplicialObject.mono_iff_mono_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L116). The attribute's comment: “(2) for simplicial objects: a morphism is a monomorphism if and only if it is a monomorphism in each degree”.

> **Stacks 018Z (2)**, simplicial objects.
> A morphism `f : X ⟶ Y` of simplicial objects of an abelian category is a monomorphism if and only
> if each component `f_n : X_n ⟶ Y_n` is a monomorphism.

```lean
public theorem mono_iff_mono_app {X Y : SimplicialObject A} (f : X ⟶ Y) :
    Mono f ↔ ∀ n : ℕ, Mono (f.app (Opposite.op (SimplexCategory.mk n)))
```

**`CategoryTheory.SimplicialObject.epi_iff_epi_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L125). The attribute's comment: “(3) for simplicial objects: a morphism is an epimorphism if and only if it is an epimorphism in each degree”.

> **Stacks 018Z (3)**, simplicial objects.
> A morphism `f : X ⟶ Y` of simplicial objects of an abelian category is an epimorphism if and only
> if each component `f_n : X_n ⟶ Y_n` is an epimorphism.

```lean
public theorem epi_iff_epi_app {X Y : SimplicialObject A} (f : X ⟶ Y) :
    Epi f ↔ ∀ n : ℕ, Epi (f.app (Opposite.op (SimplexCategory.mk n)))
```

**`CategoryTheory.CosimplicialObject.mono_iff_mono_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L138). The attribute's comment: “(2) for cosimplicial objects: a morphism is a monomorphism if and only if it is a monomorphism in each degree”.

> **Stacks 018Z (2)**, cosimplicial objects.
> A morphism `f : X ⟶ Y` of cosimplicial objects of an abelian category is a monomorphism if and
> only if each component `f_n : X_n ⟶ Y_n` is a monomorphism.

```lean
public theorem mono_iff_mono_app {X Y : CosimplicialObject A} (f : X ⟶ Y) :
    Mono f ↔ ∀ n : ℕ, Mono (f.app (SimplexCategory.mk n))
```

**`CategoryTheory.CosimplicialObject.epi_iff_epi_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L147). The attribute's comment: “(3) for cosimplicial objects: a morphism is an epimorphism if and only if it is an epimorphism in each degree”.

> **Stacks 018Z (3)**, cosimplicial objects.
> A morphism `f : X ⟶ Y` of cosimplicial objects of an abelian category is an epimorphism if and
> only if each component `f_n : X_n ⟶ Y_n` is an epimorphism.

```lean
public theorem epi_iff_epi_app {X Y : CosimplicialObject A} (f : X ⟶ Y) :
    Epi f ↔ ∀ n : ℕ, Epi (f.app (SimplexCategory.mk n))
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.functorCategoryAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.functorCategoryAbelian#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L104) (StacksFrontier): “(1): the categories `SimplicialObject A` and `CosimplicialObject A` of simplicial and cosimplicial objects of an abelian category `A` are abelian; they are the functor categories `SimplexCategoryᵒᵖ ⥤ A` and `SimplexCategory ⥤ A`, which this instance makes abelian.”.

## Tag 0190, a lemma

[Tag 0190](https://stacks.math.columbia.edu/tag/0190) in the Stacks Project.

**`CategoryTheory.SimplicialObject.EilenbergMacLane.eilenbergMacLaneIsoEmKAk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLaneExplicit.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/EilenbergMacLaneExplicit.lean#L237). The attribute's comment: “parts (2) and (3): `i_{k!}U` is isomorphic, as a simplicial object, to the simplicial object `emKAk A k` defined by the rules of (2) and (3)”.

> **Stacks 0190** (2)-(3).
> The Eilenberg-MacLane object `K(A, k) = i_{k!}U` of [Stacks, Tag 0191] (the left Kan extension
> `eilenbergMacLane A k`) is isomorphic, as a simplicial object, to the explicit simplicial object
> `emKAk A k`, whose `n`-th term is `⨁_α A` over the surjections `α : ⦋n⦌ → ⦋k⦌` and whose
> operator attached to `φ : ⦋m⦌ → ⦋n⦌` sends the summand `α` by the identity to the summand
> `α ∘ φ` when that is surjective and to zero otherwise.

```lean
noncomputable def eilenbergMacLaneIsoEmKAk (k : ℕ) : eilenbergMacLane A k ≅ emKAk A k
```

**`CategoryTheory.SimplicialObject.Truncated.app_top_injective_and_exists_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/TopDegree.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/TopDegree.lean#L171). The attribute's comment: “(1) for `k ≥ 1`, written `k = j + 1`, with the faces `d^k_i` and degeneracies `s^{k-1}_i`; each hom-set is identified with its set of top components. For `k = 0` (where both conditions are empty) see `exists_iso_sk_surjSum_cosk_injSum`.”.

> **Stacks 0190** (1), in terms of faces and degeneracies.
> Let `k = j + 1 ≥ 1` and let `U` be a `k`-truncated simplicial object of `C` with `U_i = 0` for
> `i < k`; write `A = U_k`. For every `k`-truncated simplicial object `V`:
>
> * a morphism `U ⟶ V` is determined by its top component `A ⟶ V_k`, and
>   `Mor(U, V) = {f : A → V_k | d^k_i ∘ f = 0, i = 0, …, k}`;
> * a morphism `V ⟶ U` is determined by its top component `V_k ⟶ A`, and
>   `Mor(V, U) = {f : V_k → A | f ∘ s^{k - 1}_i = 0, i = 0, …, k - 1}`.
>
> For `k = 0` both conditions are empty, and the statement is the case `k = 0` of
> `exists_iso_sk_surjSum_cosk_injSum` (1).

```lean
theorem app_top_injective_and_exists_iff_faces {j : ℕ}
    {U : SimplicialObject.Truncated C (j + 1)}
    (hU : ∀ (m : ℕ) (hm : m < j + 1), IsZero (U.obj (op ⟨⦋m⦌, hm.le⟩)))
    (V : SimplicialObject.Truncated C (j + 1)) :
    (Function.Injective (fun g : U ⟶ V => g.app (op ⟨⦋j + 1⦌, le_rfl⟩)) ∧
      ∀ f : U.obj (op ⟨⦋j + 1⦌, le_rfl⟩) ⟶ V.obj (op ⟨⦋j + 1⦌, le_rfl⟩),
        (∃ g : U ⟶ V, g.app (op ⟨⦋j + 1⦌, le_rfl⟩) = f) ↔
          ∀ i : Fin (j + 2),
            f ≫ V.map (SimplexCategory.Truncated.Hom.tr (SimplexCategory.δ i)).op = 0) ∧
    (Function.Injective (fun g : V ⟶ U => g.app (op ⟨⦋j + 1⦌, le_rfl⟩)) ∧
      ∀ f : V.obj (op ⟨⦋j + 1⦌, le_rfl⟩) ⟶ U.obj (op ⟨⦋j + 1⦌, le_rfl⟩),
        (∃ g : V ⟶ U, g.app (op ⟨⦋j + 1⦌, le_rfl⟩) = f) ↔
          ∀ i : Fin (j + 1),
            V.map (SimplexCategory.Truncated.Hom.tr (SimplexCategory.σ i)).op ≫ f = 0)
```

**`CategoryTheory.SimplicialObject.Truncated.exists_iso_sk_surjSum_cosk_injSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/TopDegree.lean, line 725](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/TopDegree.lean#L725). The attribute's comment: “(1)–(7). (1) is the first conjunct, with the conditions stated over all non-surjective (resp. non-injective) operators, which also covers `k = 0`; the face and degeneracy form for `k ≥ 1` is `app_top_injective_and_exists_iff_faces`. (2)–(5) are the isomorphisms `e₁`, `e₂` onto `surjSum` and `injSum`, whose terms and operators are by definition the sums and matrices of the statement. (6) is the matrix of `e₁⁻¹ ≫ c ≫ e₂` in each degree, `c = skToCosk U` being the unique morphism restricting to the identity of `U`. (7) is `Mono c`.”.

> **Stacks 0190**.
> Let `𝒜` be an abelian category, let `k : ℕ` and let `U` be a `k`-truncated simplicial object of
> `𝒜` with `U_i = 0` for `i < k`; write `A = U_k`. (All operators `U(φ)` other than
> `U(id_{⦋k⦌}) = id_A` then vanish, so this is the object `U` of the Stacks project.)
>
> 1. For every `k`-truncated simplicial object `V`, a morphism `U ⟶ V` (resp. `V ⟶ U`) is
>    determined by its top component, and the top components are exactly the `f : A ⟶ V_k` with
>    `f ≫ V(φ) = 0` for every non-surjective `φ : ⦋m⦌ ⟶ ⦋k⦌` (resp. the `f : V_k ⟶ A` with
>    `V(ψ) ≫ f = 0` for every non-injective `ψ : ⦋k⦌ ⟶ ⦋m⦌`); these are the conditions
>    `d^k_i ∘ f = 0`, `i = 0, …, k` (resp. `f ∘ s^{k-1}_i = 0`, `i = 0, …, k - 1`), see
>    `app_top_injective_and_exists_iff_faces`.
> 2. and 3. `i_{k!}U` is isomorphic to `surjSum A k`: its `n`-th term is `⨁_α A` over the
>    surjections `α : ⦋n⦌ ⟶ ⦋k⦌`, and `i_{k!}U(φ)` maps the summand `α` by the identity to the
>    summand `α ∘ φ` if `α ∘ φ` is surjective, and to zero otherwise.
> 4. and 5. `cosk_k U` is isomorphic to `injSum A k`: its `n`-th term is `⨁_β A` over the
>    injections `β : ⦋k⦌ ⟶ ⦋n⦌`, and `cosk_k U(φ)` maps the summand `β` to zero if `β` does not
>    factor through `φ`, and by the identity to each summand `β'` with `β = φ ∘ β'` if it does.
> 6. Under these isomorphisms the canonical map `c : i_{k!}U ⟶ cosk_k U` (`skToCosk U`) has, in
>    degree `n`, `(α, β)` coefficient `id_A` if `α ∘ β = id_{⦋k⦌}` and `0` otherwise.
> 7. `c` is injective, i.e. a monomorphism.

```lean
theorem exists_iso_sk_surjSum_cosk_injSum {U : SimplicialObject.Truncated 𝒜 k}
    (hU : ∀ (m : ℕ) (hm : m < k), IsZero (U _⦋m,hm.le⦌ₖ)) :
    (∀ V : SimplicialObject.Truncated 𝒜 k,
      (Function.Injective (fun g : U ⟶ V => g.app (op ⦋k⦌ₖ)) ∧
        ∀ f : U _⦋k⦌ₖ ⟶ V _⦋k⦌ₖ, (∃ g : U ⟶ V, g.app (op ⦋k⦌ₖ) = f) ↔
          ∀ (m : SimplexCategory.Truncated k) (φ : m ⟶ ⦋k⦌ₖ),
            ¬ Function.Surjective φ.hom.toOrderHom → f ≫ V.map φ.op = 0) ∧
      (Function.Injective (fun g : V ⟶ U => g.app (op ⦋k⦌ₖ)) ∧
        ∀ f : V _⦋k⦌ₖ ⟶ U _⦋k⦌ₖ, (∃ g : V ⟶ U, g.app (op ⦋k⦌ₖ) = f) ↔
          ∀ (m : SimplexCategory.Truncated k) (ψ : ⦋k⦌ₖ ⟶ m),
            ¬ Function.Injective ψ.hom.toOrderHom → V.map ψ.op ≫ f = 0)) ∧
    ∃ (e₁ : (Truncated.sk k).obj U ≅ surjSum (U _⦋k⦌ₖ) k)
      (e₂ : (Truncated.cosk k).obj U ≅ injSum (U _⦋k⦌ₖ) k),
      (∀ n : SimplexCategory, (e₁.inv ≫ skToCosk U ≫ e₂.hom).app (op n) =
        biproduct.matrix fun (α : {α : n ⟶ ⦋k⦌ // Function.Surjective α.toOrderHom})
          (β : {β : ⦋k⦌ ⟶ n // Function.Injective β.toOrderHom}) =>
            if β.1 ≫ α.1 = 𝟙 _ then 𝟙 (U _⦋k⦌ₖ) else 0) ∧
      Mono (skToCosk U)
```

## Tag 0191, a definition

[Tag 0191](https://stacks.math.columbia.edu/tag/0191) in the Stacks Project.

**`CategoryTheory.SimplicialObject.eilenbergMacLane`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/EilenbergMacLane.lean#L66).

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

**`CategoryTheory.SimplicialObject.EilenbergMacLane.eilenbergMacLaneShortComplex_shortExact_and_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/EilenbergMacLaneExplicit.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/EilenbergMacLaneExplicit.lean#L279).

> **Stacks 0192**.
> Let `𝒜` be an abelian category, `A` an object of `𝒜` and `k ≥ 0`. Let `E` be the simplicial
> object with `E_n = ⨁_α A` over the monotone `α : ⦋n⦌ → ⦋k + 1⦌` whose image is `⦋k⦌` or
> `⦋k + 1⦌`, the operator attached to `φ : ⦋m⦌ → ⦋n⦌` sending the summand `α` by the identity to
> the summand `α ∘ φ` when its image is `⦋k⦌` or `⦋k + 1⦌` and to zero otherwise (`emEobj A k`).
> Then `0 → K(A, k) → E → K(A, k + 1) → 0`, with `K(A, k)` and `K(A, k + 1)` the Eilenberg-MacLane
> objects `i_{k!}U` of [Stacks, Tag 0191], is a short exact sequence of simplicial objects which is
> term by term split exact: evaluating it in any degree `n` gives a split short exact sequence
> of `𝒜`.

```lean
theorem eilenbergMacLaneShortComplex_shortExact_and_splitting (k : ℕ) :
    (eilenbergMacLaneShortComplex A k).ShortExact ∧
      ∀ n : SimplexCategoryᵒᵖ, Nonempty
        (((eilenbergMacLaneShortComplex A k).map ((evaluation _ _).obj n)).Splitting)
```

## Tag 0193, a lemma

[Tag 0193](https://stacks.math.columbia.edu/tag/0193) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_mono_isColimit_sk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Abelian.lean#L425).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
