---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.Augmented, CategoryTheory.SimplicialObject.existsUnique_hom_const_app_zero_eq_iff, CategoryTheory.Arrow.truncation_bijective_into_cechNerve, CategoryTheory.Arrow.truncated_mor_equiv_setOf, CategoryTheory.Arrow.cechNerve_isCoskeletal, CategoryTheory.SimplicialObject.existsUnique_hom_cechNerve_app_zero_comp_π_eq_id
statement: formalized
proof: formalized
---

# 14.20 Augmentations

Section 14.20 of the Stacks Project, [Tag 018F](https://stacks.math.columbia.edu/tag/018F). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 018G, a definition

[Tag 018G](https://stacks.math.columbia.edu/tag/018G) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SimplicialObject.Augmented`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.Augmented#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L120) (StacksFrontier). References: SGA 4 Vbis (1.2.6).

## Tag 018H, a lemma

[Tag 018H](https://stacks.math.columbia.edu/tag/018H) in the Stacks Project.

**`CategoryTheory.SimplicialObject.existsUnique_hom_const_app_zero_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/CechNerve.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/CechNerve.lean#L106). The attribute's comment: “restriction to degree 0 is a bijection from augmentations of U towards X onto the morphisms ε₀ : U\_0 ⟶ X with ε₀ ∘ d^1\_0 = ε₀ ∘ d^1\_1”.

> Let `U` be a simplicial object of a category `C`, let `X : C` and let `ε₀ : U_0 ⟶ X`. Then `ε₀`
> extends to a unique augmentation of `U` towards `X`, i.e. to a unique morphism
> `U ⟶ (const C).obj X` with `ε₀` as its degree `0` component, precisely when
> `U.δ 0 ≫ ε₀ = U.δ 1 ≫ ε₀`.

```lean
public theorem existsUnique_hom_const_app_zero_eq_iff (U : SimplicialObject C) (X : C)
    (ε₀ : U _⦋0⦌ ⟶ X) :
    (∃! ε : U ⟶ (const C).obj X, ε.app (op ⦋0⦌) = ε₀) ↔ U.δ 0 ≫ ε₀ = U.δ 1 ≫ ε₀
```

## Tag 018I, a lemma

[Tag 018I](https://stacks.math.columbia.edu/tag/018I) in the Stacks Project.

**`CategoryTheory.Arrow.truncation_bijective_into_cechNerve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/CechNerve.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/CechNerve.lean#L417). The attribute's comment: “(1)”.

> For a simplicial object `V` and the Čech nerve `U` of `f : Y ⟶ X`,
> the map `Mor(V, U) → Mor(sk₁ V, sk₁ U)`, `g ↦ sk₁ g`, induced by the `1`-truncation functor, is a
> bijection.

```lean
theorem truncation_bijective_into_cechNerve
    (f : Arrow C) [HasCechPullbacks f] (V : SimplicialObject C) :
    Function.Bijective
      (fun g : V ⟶ cechNerve f => (truncation 1).map g)
```

**`CategoryTheory.Arrow.truncated_mor_equiv_setOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/CechNerve.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/CechNerve.lean#L437). The attribute's comment: “(2)”.

> Morphisms `sk₁ V ⟶ sk₁ U` of `1`-truncated simplicial objects
> correspond bijectively to the morphisms `g₀ : V₀ ⟶ Y` satisfying
> `f ∘ g₀ ∘ d¹₀ = f ∘ g₀ ∘ d¹₁`, the bijection sending `g` to its degree-`0` component
> `deg0Component g`.

```lean
theorem truncated_mor_equiv_setOf
    (f : Arrow C) [HasCechPullbacks f] (V : SimplicialObject C) :
    ∃ e : ((truncation 1).obj V ⟶ (truncation 1).obj (cechNerve f)) ≃
        { g₀ : V.obj (op (SimplexCategory.mk 0)) ⟶ f.left //
            V.δ (0 : Fin 2) ≫ g₀ ≫ f.hom = V.δ (1 : Fin 2) ≫ g₀ ≫ f.hom },
      ∀ g, (e g : V.obj (op (SimplexCategory.mk 0)) ⟶ f.left) = deg0Component g
```

**`CategoryTheory.Arrow.cechNerve_isCoskeletal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/CechNerve.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/CechNerve.lean#L518). The attribute's comment: “(3)”.

> The Čech nerve `U` is `1`-coskeletal: the unit
> `U ⟶ cosk₁ (sk₁ U)` of the `sk₁`/`cosk₁` adjunction is an isomorphism.

```lean
theorem cechNerve_isCoskeletal
    (f : Arrow C) [HasCechPullbacks f] [HasCosk₁ C] :
    IsIso ((coskAdj (C := C) 1).unit.app (cechNerve f))
```

## Tag 018J, a remark

[Tag 018J](https://stacks.math.columbia.edu/tag/018J) in the Stacks Project.

**`CategoryTheory.SimplicialObject.existsUnique_hom_cechNerve_app_zero_comp_π_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/CechNerve.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/CechNerve.lean#L617). The attribute's comment: “the canonical morphism V ⟶ U, pinned as the unique morphism to the Čech nerve of ε₀ which is the identity of V\_0 in degree 0”.

> Let `C` be a category with fibre products, let `V` be a simplicial object of `C` and let
> `ε : V ⟶ (const C).obj X` be an augmentation of `V` towards `X : C`, with degree `0` component
> `ε₀ : V_0 ⟶ X`. Let `U` be the Čech nerve of `ε₀`, whose `n`th term is the `(n + 1)`-fold fibre
> product `V_0 ×_X ⋯ ×_X V_0`. Then there is exactly one morphism `V ⟶ U` whose degree `0` component
> is the canonical isomorphism `V_0 ≅ V_0 ×_X X`.

```lean
public theorem existsUnique_hom_cechNerve_app_zero_comp_π_eq_id [HasFiniteWidePullbacks C]
    (V : SimplicialObject C) (X : C) (ε : V ⟶ (const C).obj X) :
    ∃! g : V ⟶ (Arrow.mk (ε.app (op ⦋0⦌) : V _⦋0⦌ ⟶ X)).cechNerve,
      g.app (op ⦋0⦌) ≫ WidePullback.π _ 0 = 𝟙 (V _⦋0⦌)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.20, Tag 018F](https://stacks.math.columbia.edu/tag/018F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
