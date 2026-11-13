---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.power, CategoryTheory.SimplicialObject.bijective_comp_proj_id_of_prod_coyoneda
statement: formalized
proof: formalized
---

# 14.15 Hom from cosimplicial sets into simplicial objects

Section 14.15 of the Stacks Project, [Tag 0B14](https://stacks.math.columbia.edu/tag/0B14). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B15, a definition

[Tag 0B15](https://stacks.math.columbia.edu/tag/0B15) in the Stacks Project.

**`CategoryTheory.SimplicialObject.power`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean#L100). The attribute's comment: “the finiteness and nonemptiness of the `U_n` are replaced by the existence of the products they index, which is all they are used for; dual to `CosimplicialObject.power` of Tag 019V”.

> **Stacks 0B15.** `Hom(U, V)`, the simplicial object of maps from a cosimplicial set `U` into a
> simplicial object `V` of `C`. Its degree `n` part is the power `Hom(U, V)_n = ∏_{u ∈ U_n} V_n`, the
> object of `C` whose `X`-valued points are the maps `U_n → Mor_C(X, V_n)`, and for `φ : [m] ⟶ [n]`
> in `Δ` the structure map `Hom(U, V)_n ⟶ Hom(U, V)_m` is the morphism whose `u`-th component, for
> `u ∈ U_m`, is the projection to the `U(φ)(u)`-th factor followed by `V(φ)`; on `X`-valued points it
> is `f ↦ V(φ) ∘ f ∘ U(φ)`.

```lean
noncomputable def power (V : SimplicialObject C) (U : CosimplicialObject (Type w))
    [∀ n : SimplexCategoryᵒᵖ, HasProduct fun _ : U.obj n.unop => V.obj n] :
    SimplicialObject C
```

## Tag 017M, a lemma

[Tag 017M](https://stacks.math.columbia.edu/tag/017M) in the Stacks Project.

**`CategoryTheory.SimplicialObject.bijective_comp_proj_id_of_prod_coyoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean#L304). The attribute's comment: “the source's U is characterised rather than constructed: its terms being the self products indexed by C[k]\_n of Tag 0B13, and its structure maps the reindexing, are the hypotheses, which is part (3); the two conjuncts are parts (1) and (2), the latter for an arbitrary truncation level j ≥ k”.

> **`Hom(C[k], X)` represents evaluation in degree `k`.** Let `X` be an object of a category
> `C`, let `k : ℕ`, and let `U` be a simplicial object of `C` with coordinates
> `pr n : C[k]_n → (U_n ⟶ X)` indexed by the terms `C[k]_n = Mor_Δ(⦋k⦌, ⦋n⦌)` of the standard
> cosimplicial set `C[k]` of [Stacks, Tag 0B13], such that the coordinates exhibit `U_n` as the
> self product `∏_{α ∈ C[k]_n} X` — the `T`-valued points of `U_n` are the maps of sets
> `C[k]_n → Mor_C(T, X)`, `f ↦ (f ≫ pr n α)_α` — and such that the structure maps reindex along
> `C[k]`, that is `U(φ) ≫ pr_α = pr_{C[k](φ)(α)} = pr_{φ ∘ α}`; so `U` is an incarnation of
> `Hom(C[k], X)` for `X` read as the constant simplicial object. Then `U` represents evaluation in
> degree `k`: (1) for every simplicial object `V` of `C` the map `γ ↦ γ_k ≫ pr_{id_⦋k⦌}` is a
> bijection `Mor_{Simp(C)}(V, U) → Mor_C(V_k, X)`, and (2) for every `j ≥ k` and every
> `j`-truncated simplicial object `W` of `C` the same formula is a bijection
> `Mor_{Simp_j(C)}(W, sk_j U) → Mor_C(W_k, X)`.

```lean
public theorem bijective_comp_proj_id_of_prod_coyoneda (X : C) (k : ℕ) (U : SimplicialObject C)
    (pr : ∀ n : ℕ, uliftCoyoneda.{w}.obj (op ⦋k⦌) ^⦋n⦌ → (U _⦋n⦌ ⟶ X))
    (hpr : ∀ (n : ℕ) (T : C), Function.Bijective fun (f : T ⟶ U _⦋n⦌)
      (α : uliftCoyoneda.{w}.obj (op ⦋k⦌) ^⦋n⦌) => f ≫ pr n α)
    (hmap : ∀ (n m : ℕ) (φ : ⦋m⦌ ⟶ ⦋n⦌) (α : uliftCoyoneda.{w}.obj (op ⦋k⦌) ^⦋m⦌),
      U.map φ.op ≫ pr m α = pr n ((uliftCoyoneda.{w}.obj (op ⦋k⦌)).map φ α)) :
    (∀ V : SimplicialObject C, Function.Bijective fun γ : V ⟶ U =>
        (γ.app (op ⦋k⦌) ≫ pr k (ULift.up (𝟙 ⦋k⦌)) : V _⦋k⦌ ⟶ X)) ∧
    (∀ (j : ℕ) (hkj : k ≤ j) (W : Truncated C j),
      Function.Bijective fun γ : W ⟶ (truncation j).obj U =>
        (γ.app (op ⟨⦋k⦌, hkj⟩) ≫ pr k (ULift.up (𝟙 ⦋k⦌)) :
          W.obj (op (⟨⦋k⦌, hkj⟩ : SimplexCategory.Truncated j)) ⟶ X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.15, Tag 0B14](https://stacks.math.columbia.edu/tag/0B14)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
