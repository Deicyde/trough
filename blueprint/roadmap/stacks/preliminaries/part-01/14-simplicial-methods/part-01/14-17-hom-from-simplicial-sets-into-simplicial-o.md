---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.IsHomFromSSet, CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable, SSet.hasLimitsOfShape_elements, CategoryTheory.SimplicialObject.exists_representableBy_sHom, CategoryTheory.SimplicialObject.isPullback_hom_of_isPushout
statement: formalized
proof: formalized
---

# 14.17 Hom from simplicial sets into simplicial objects

Section 14.17 of the Stacks Project, [Tag 017H](https://stacks.math.columbia.edu/tag/017H). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 017I, a definition

[Tag 017I](https://stacks.math.columbia.edu/tag/017I) in the Stacks Project.

**`CategoryTheory.SimplicialObject.IsHomFromSSet`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L69).

> **Stacks 017I**.
> `IsHomFromSSet U V H` is the datum exhibiting a simplicial object `H` of a category `C` as a
> `Hom(U, V)` for a simplicial set `U` and a simplicial object `V` of `C`: a bijection
> `Mor(W, H) ≃ Mor(W × U, V)`, functorial in the simplicial object `W` of `C`. The right-hand side is
> written as `U ⟶ sHom W V`, the morphisms of simplicial sets from `U` into the enriched hom of `W`
> and `V`.

```lean
public abbrev IsHomFromSSet (U : SSet.{v}) (V H : SimplicialObject C)
```

## Tag 017J, a lemma

[Tag 017J](https://stacks.math.columbia.edu/tag/017J) in the Stacks Project.

**`CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L291).

> **Stacks 017J**. Let `C` be a category with coproducts of any two objects and with countable
> limits, let `U` be a simplicial set with `U_n` finite and nonempty for all `n ≥ 0`, and let `V`
> be a simplicial object of `C`. Then the functor `Cᵒᵖ ⥤ Sets`, `X ↦ Mor_{Simp(C)}(X × U, V)`, is
> representable.

```lean
theorem simpHomFromSSet_isRepresentable
    [HasBinaryCoproducts C] [HasCountableLimits C]
    (U : SSet.{0}) [∀ n, Finite (U.obj n)] [∀ n, Nonempty (U.obj n)]
    (V : SimplicialObject C) :
    (simpHomFromSSet U V).IsRepresentable
```

## Tag 017K, a lemma

[Tag 017K](https://stacks.math.columbia.edu/tag/017K) in the Stacks Project.

**`SSet.hasLimitsOfShape_elements`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L526).

> **Stacks 017K**.
> Let `U` be a simplicial set with finitely many nondegenerate simplices, i.e. with `U_n`
> finite for all `n` and with all `n`-simplices degenerate for `n ≫ 0`, and let `C` be a
> category with finite limits. Then every diagram indexed by the category `U.Elements` of
> simplices of `U` has a limit in `C`.

```lean
public instance hasLimitsOfShape_elements (U : SSet.{w}) [U.Finite] (C : Type u)
    [Category.{v} C] [HasFiniteLimits C] : HasLimitsOfShape U.Elements C
```

## Tag 017L, a lemma

[Tag 017L](https://stacks.math.columbia.edu/tag/017L) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_representableBy_sHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 923](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L923). References: SGA 4 V (7.3.6.0), “U finite, C fin. limits”.

> **Stacks 017L**.
> Let `C` be a category with finite limits, let `U` be a finite simplicial set and let `V` be a
> simplicial object of `C`. Then the simplicial object `Hom(U, V)` exists: the functor
> `W ↦ (U ⟶ sHom W V)` on `(SimplicialObject C)ᵒᵖ`, which is `W ↦ Mor(W × U, V)`, is representable
> by a simplicial object `H` of `C`; moreover `H _⦋n⦌` represents `X ↦ Mor(X × U × Δ[n], V)`, the
> functor represented by `Hom(U × Δ[n], V)_0`.

```lean
public theorem exists_representableBy_sHom {C : Type u} [Category.{v} C] [HasFiniteLimits C]
    (U : SSet.{v}) [U.Finite] (V : SimplicialObject C) :
    ∃ H : SimplicialObject C,
      Nonempty ((sHomFunctor (SimplicialObject C) ⋙
        (evaluation (SimplicialObject C) SSet.{v}).obj V ⋙
        coyoneda.obj (op U)).RepresentableBy H) ∧
      ∀ n : ℕ, Nonempty (((SimplicialObject.const C).op ⋙ sHomFunctor (SimplicialObject C) ⋙
        (evaluation (SimplicialObject C) SSet.{v}).obj V ⋙
        coyoneda.obj (op (U ⊗ Δ[n]))).RepresentableBy (H _⦋n⦌))
```

## Tag 017N, a lemma

[Tag 017N](https://stacks.math.columbia.edu/tag/017N) in the Stacks Project.

**`CategoryTheory.SimplicialObject.isPullback_hom_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 1090](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L1090). The attribute's comment: “stated in degree 0, for the representing objects of `X ↦ Mor(X × K, T)`”.

> **Stacks 017N**.
> Let `T` be a simplicial object of a category `C`, let `a : U ⟶ V` and `b : U ⟶ W` be morphisms
> of simplicial sets, and let `P = V ⨿_U W` be their pushout, with structure morphisms
> `f : V ⟶ P`, `g : W ⟶ P`. Assume that for each of the four simplicial sets `K = U, V, W, P` the
> presheaf `X ↦ Mor_{Simp(C)}(X × K, T) = Mor_{SSet}(K, T ⋙ coyoneda.obj (op X))` on `C` is
> represented by an object `Hom(K, T)₀` of `C` — as it is, by [Stacks, Tag 017L], when `C` has
> coproducts of any two objects and finite limits, the `U_n`, `V_n`, `W_n` are finite nonempty and
> all simplices of `U`, `V`, `W` in high enough degree are degenerate. Then
> `Hom(P, T)₀ = Hom(V, T)₀ ×_{Hom(U, T)₀} Hom(W, T)₀`
> via the morphisms induced by `f`, `g`, `a` and `b`.

```lean
public theorem isPullback_hom_of_isPushout {C : Type u} [Category.{v} C]
    (T : SimplicialObject C) {U V W P : SSet.{v}}
    {a : U ⟶ V} {b : U ⟶ W} {f : V ⟶ P} {g : W ⟶ P} (h : IsPushout a b f g)
    {HU HV HW HP : C}
    (hU : (coyoneda ⋙ (Functor.whiskeringLeft SimplexCategoryᵒᵖ C (Type v)).obj T ⋙
        coyoneda.obj (op U)).RepresentableBy HU)
    (hV : (coyoneda ⋙ (Functor.whiskeringLeft SimplexCategoryᵒᵖ C (Type v)).obj T ⋙
        coyoneda.obj (op V)).RepresentableBy HV)
    (hW : (coyoneda ⋙ (Functor.whiskeringLeft SimplexCategoryᵒᵖ C (Type v)).obj T ⋙
        coyoneda.obj (op W)).RepresentableBy HW)
    (hP : (coyoneda ⋙ (Functor.whiskeringLeft SimplexCategoryᵒᵖ C (Type v)).obj T ⋙
        coyoneda.obj (op P)).RepresentableBy HP) :
    IsPullback (hV.homEquiv.symm (f ≫ hP.homEquiv (𝟙 HP)))
      (hW.homEquiv.symm (g ≫ hP.homEquiv (𝟙 HP)))
      (hU.homEquiv.symm (a ≫ hV.homEquiv (𝟙 HV)))
      (hU.homEquiv.symm (b ≫ hW.homEquiv (𝟙 HW)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.17, Tag 017H](https://stacks.math.columbia.edu/tag/017H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
