---
declaration: section
origin: cited
lean: SSet.existsUnique_hom_app_eq, CategoryTheory.Functor.copower, CategoryTheory.Functor.exists_corepresentableBy_copower, CategoryTheory.Functor.copowerProj, CategoryTheory.SimplicialObject.prodFunctor, CategoryTheory.SimplicialObject.constProdStd.phi_bijective, CategoryTheory.SimplicialObject.constProdStd.phi_trunc_bijective
statement: formalized
proof: formalized
---

# 14.13 Products with simplicial sets

Section 14.13 of the Stacks Project, [Tag 017A](https://stacks.math.columbia.edu/tag/017A). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 017B, an equation

[Tag 017B](https://stacks.math.columbia.edu/tag/017B) in the Stacks Project.

**`SSet.existsUnique_hom_app_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L115). The attribute's comment: “the displayed set is the hom-set `π U ⋙ V ⟶ π U ⋙ W` over the category of elements of `U`; here its elements are described by the faces and the degeneracies”.

> **Stacks 017B**.
> Let `U` be a simplicial set, let `V`, `W` be simplicial objects of a category `C`, and let
> `d n u : V_n ⟶ W_n` be a family of morphisms, indexed by `n : ℕ` and by the `n`-simplices `u` of
> `U`, which commutes with the face maps and with the degeneracy maps. Then `d` is the family of
> components of a unique element of the displayed set of families
> `(f_{n, u} : V_n ⟶ W_n)_{n ≥ 0, u ∈ U_n}` satisfying `f_{m, U(φ)(u)} ∘ V(φ) = W(φ) ∘ f_{n, u}` for
> every `φ : [m] → [n]`, that set being the hom-set `π U ⋙ V ⟶ π U ⋙ W` of functors on the category
> of elements of `U`.

```lean
public theorem existsUnique_hom_app_eq (U : SSet.{w}) {V W : SimplicialObject C}
    (d : ∀ n : ℕ, U.obj (op ⦋n⦌) → (V.obj (op ⦋n⦌) ⟶ W.obj (op ⦋n⦌)))
    (hδ : ∀ (n : ℕ) (i : Fin (n + 2)) (u : U.obj (op ⦋n + 1⦌)),
      V.δ i ≫ d n (U.δ i u) = d (n + 1) u ≫ W.δ i)
    (hσ : ∀ (n : ℕ) (i : Fin (n + 1)) (u : U.obj (op ⦋n⦌)),
      V.σ i ≫ d (n + 1) (U.σ i u) = d n u ≫ W.σ i) :
    ∃! f : Functor.Elements.π U ⋙ V ⟶ Functor.Elements.π U ⋙ W,
      ∀ (n : ℕ) (u : U.obj (op ⦋n⦌)), f.app ⟨u⟩ = d n u
```

## Tag 017C, a definition

[Tag 017C](https://stacks.math.columbia.edu/tag/017C) in the Stacks Project.

**`CategoryTheory.Functor.copower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L189). The attribute's comment: “stated for an arbitrary index category `J` in place of `SimplexCategoryᵒᵖ`, and under the source's looser hypothesis that the coproducts exist”. References: SGA 4 IV (4.3), “more general”.

> **Stacks 017C**.
> The copower of `V : J ⥤ C` by `U : J ⥤ Type w`, defined whenever the coproduct of `U j`-many copies
> of `V j` exists for every `j`: the functor `j ↦ ∐_{u ∈ U j} V j` whose value on `f : i ⟶ j` sends
> the component indexed by `u ∈ U i` into the component indexed by `U f u ∈ U j` by `V f`.
>
> For `J = SimplexCategoryᵒᵖ`, a simplicial set `U` and a simplicial object `V` of `C` this is the
> product `U × V` of [Stacks, Tag 017C]: `(U × V)_n = ∐_{u ∈ U_n} V_n`, and for `φ : [m] → [n]` the
> component `V_n` indexed by `u ∈ U_n` maps to the component `V_m` indexed by `U(φ)(u) ∈ U_m` via
> `V(φ)`. It exists in particular when `C` has the coproduct of any two objects and every `U_n` is
> finite nonempty.

```lean
public noncomputable def copower (V : J ⥤ C) (U : J ⥤ Type w)
    [∀ j, HasCoproduct fun _ : U.obj j => V.obj j] : J ⥤ C
```

## Tag 017D, a lemma

[Tag 017D](https://stacks.math.columbia.edu/tag/017D) in the Stacks Project.

**`CategoryTheory.Functor.exists_corepresentableBy_copower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L311). The attribute's comment: “stated for an arbitrary index category `J` in place of `SimplexCategoryᵒᵖ`, under the source's looser hypothesis that the coproducts exist, and with the canonical isomorphism pinned by its components; the set of Equation 017B is the hom-set `π U ⋙ V ⟶ π U ⋙ W` over the category of elements of `U`”. References: SGA 3 I (1.8), “(1.8.2)”; SGA 4 IV (4.3), “For each set I”.

> **Stacks 017D**.
> Let `V : J ⥤ C` and `U : J ⥤ Type w` be such that the coproducts defining the copower
> `V.copower U` exist. Then the covariant functor sending `W : J ⥤ C` to the hom-set
> `π U ⋙ V ⟶ π U ⋙ W` of functors on the category of elements of `U` is corepresented by
> `V.copower U`, by the bijection which sends `g : V.copower U ⟶ W` to the family of its
> restrictions `Sigma.ι _ u ≫ g.app j : V.obj j ⟶ W.obj j` to the components of the coproducts.
>
> For `J = SimplexCategoryᵒᵖ`, a simplicial set `U` and simplicial objects `V`, `W` of `C` this
> says that the functor `W ↦ Mor_{Simp(C)}(U × V, W)` is canonically isomorphic to the functor
> sending `W` to the set of Equation [Stacks, Tag 017B] of families
> `(f_{n, u} : V_n ⟶ W_n)_{n ≥ 0, u ∈ U_n}` with `f_{m, U(φ)(u)} ∘ V(φ) = W(φ) ∘ f_{n, u}`, the
> isomorphism sending `g : U × V ⟶ W` to `f_{n, u} = Sigma.ι _ u ≫ g_n`.

```lean
public theorem exists_corepresentableBy_copower (V : J ⥤ C) (U : J ⥤ Type w)
    [∀ j, HasCoproduct fun _ : U.obj j => V.obj j] :
    ∃ h : ((whiskeringLeft U.Elements J C).obj (Functor.Elements.π U) ⋙
        coyoneda.obj (op (Functor.Elements.π U ⋙ V))).CorepresentableBy (V.copower U),
      ∀ (W : J ⥤ C) (g : V.copower U ⟶ W) (j : J) (u : U.obj j),
        (h.homEquiv g).app ⟨u⟩ =
          Sigma.ι (fun _ : U.obj j => V.obj j) u ≫ g.app j
```

## Tag 017E, a lemma

[Tag 017E](https://stacks.math.columbia.edu/tag/017E) in the Stacks Project.

**`CategoryTheory.Functor.copowerProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L497). The attribute's comment: “(2); stated for an arbitrary index category `J` in place of `SimplexCategoryᵒᵖ`, and under the looser hypothesis that the coproducts exist”.

> **Stacks 017E** (2).
> The canonical projection `V.copower U ⟶ V`, whose component at `j` is the identity of `V j` on
> each summand of `(V.copower U) j = ∐_{u ∈ U j} V j`. For `J = SimplexCategoryᵒᵖ`, a simplicial
> set `U` and a simplicial object `V` this is the projection `U × V ⟶ V`.

```lean
noncomputable def copowerProj (V : J ⥤ C) (U : J ⥤ Type w)
    [∀ j, HasCoproduct fun _ : U.obj j => V.obj j] : V.copower U ⟶ V
```

**`CategoryTheory.SimplicialObject.prodFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L525). The attribute's comment: “(1)”.

> **Stacks 017E** (1).
> The functor `FSSets × SimplicialObject C ⥤ SimplicialObject C` sending a pair `(U, V)` to the
> product `U × V = V.copower U` and a pair of morphisms `(a, b)` to `Functor.copowerMap b a`.

```lean
noncomputable def prodFunctor : SSet.FSSets.{w} × SimplicialObject C ⥤ SimplicialObject C
```

## Tag 017F, a lemma

[Tag 017F](https://stacks.math.columbia.edu/tag/017F) in the Stacks Project.

**`CategoryTheory.SimplicialObject.constProdStd.phi_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L674). The attribute's comment: “(1)”.

> **Stacks 017F** (part 1).
> For any simplicial object `V` of `C`, the map
> `Φ : Mor_{Simp(C)}(X × Δ[k], V) → Mor_C(X, V_k)`, `Φ(γ) = γ_k ∘ ι_{id_[k]}`, is a bijection.

```lean
theorem phi_bijective (V : SimplicialObject C) :
    Function.Bijective (phi X k V)
```

**`CategoryTheory.SimplicialObject.constProdStd.phi_trunc_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Copower.lean#L749). The attribute's comment: “(2)”.

> **Stacks 017F** (part 2).
> Let `n ≥ k` and let `W` be an `n`-truncated simplicial object of `C`. Then the map
> `Φ_n : Mor_{Simp_n(C)}(sk_n (X × Δ[k]), W) → Mor_C(X, W_k)`, `Φ_n(γ) = γ_k ∘ ι_{id_[k]}`, is a
> bijection.

```lean
theorem phi_trunc_bijective (n : ℕ) (hkn : k ≤ n) (W : SimplicialObject.Truncated C n) :
    Function.Bijective (phiTrunc X k n hkn W)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.13, Tag 017A](https://stacks.math.columbia.edu/tag/017A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
