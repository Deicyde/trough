---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.IsHomFromSSet, CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable, CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable_of_finite, CategoryTheory.SimplicialObject.exists_representableBy_sHom, CategoryTheory.SimplicialObject.isPullback_homFromSSet_of_isPushout
statement: formalized
proof: formalized
---

# 14.17 Hom from simplicial sets into simplicial objects

Section 14.17 of the Stacks Project, [Tag 017H](https://stacks.math.columbia.edu/tag/017H). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 017I, a definition

[Tag 017I](https://stacks.math.columbia.edu/tag/017I) in the Stacks Project.

**`CategoryTheory.SimplicialObject.IsHomFromSSet`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L70).

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

**`CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L291).

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

**`CategoryTheory.SimplicialObject.simpHomFromSSet_isRepresentable_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L592). The attribute's comment: “C with binary coproducts and finite limits; U\_n finite nonempty, U with finitely many nondegenerate simplices; the functor X ↦ Mor(X × U, V) is representable”.

> **Stacks 017K**. Let `C` be a category with coproducts of any two objects and with finite
> limits, let `U` be a simplicial set with `U_n` finite and nonempty for all `n ≥ 0` and with all
> `n`-simplices of `U` degenerate for `n ≫ 0` (`[U.Finite]`: finitely many nondegenerate
> simplices), and let `V` be a simplicial object of `C`. Then the functor `Cᵒᵖ ⥤ Sets`,
> `X ↦ Mor_{Simp(C)}(X × U, V)`, is representable. It is represented by the limit of
> `simpHomDiagram U V` over the simplices of `U`, which exists by
> `SSet.hasLimitsOfShape_elements`.

```lean
public theorem simpHomFromSSet_isRepresentable_of_finite
    [HasBinaryCoproducts C] [HasFiniteLimits C]
    (U : SSet.{0}) [∀ n, Finite (U.obj n)] [∀ n, Nonempty (U.obj n)] [U.Finite]
    (V : SimplicialObject C) :
    (simpHomFromSSet U V).IsRepresentable
```

## Tag 017L, a lemma

[Tag 017L](https://stacks.math.columbia.edu/tag/017L) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_representableBy_sHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 987](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L987). References: SGA 4 V (7.3.6.0), “U finite, C fin. limits”.

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

**`CategoryTheory.SimplicialObject.isPullback_homFromSSet_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean, line 1256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/SSetHom.lean#L1256). The attribute's comment: “both the existence of the four `Hom` objects (via 017L) and the identification of `Hom(V ⨿_U W, T)` with the fibre product, as simplicial objects; the source's binary coproducts and nonemptiness of `U_n`, `V_n`, `W_n` are not needed”.

> **Stacks 017N**.
> Let `C` be a category with finite limits, let `a : U ⟶ V` and `b : U ⟶ W` be morphisms of
> simplicial sets with `U_n`, `V_n`, `W_n` finite for all `n ≥ 0` and all `n`-simplices of `U`,
> `V`, `W` degenerate for `n ≫ 0`, let `P = V ⨿_U W` be their pushout, with structure morphisms
> `f : V ⟶ P` and `g : W ⟶ P`, and let `T` be a simplicial object of `C`. Then
> 1. the simplicial objects `Hom(U, T)`, `Hom(V, T)`, `Hom(W, T)` and `Hom(V ⨿_U W, T)` of
>    [Stacks, Tag 017I] exist (`IsHomFromSSet K T H`: `H` represents `X ↦ Mor(X × K, T)` on
>    `Simp(C)`), and
> 2. for any choice of them,
>    `Hom(V, T) ×_{Hom(U, T)} Hom(W, T) = Hom(V ⨿_U W, T)`: the square of simplicial objects formed
>    by the morphisms induced by `f`, `g`, `a` and `b` is a pullback square in `Simp(C)`, i.e. the
>    fibre product on the left is represented by the `Hom` object on the right.
>
> The source also assumes that `C` has coproducts of any two objects and that the `U_n`, `V_n`,
> `W_n` are nonempty, so that the products `X × K` of [Stacks, Tag 017C] are defined; here
> `Mor(X × K, T)` is expressed as `K ⟶ sHom X T` (see `IsHomFromSSet`), which needs neither, so
> those hypotheses are not needed. The degree-`0` form of part 2, for objects of `C`
> representing `X ↦ Mor(X × K, T)`, is `isPullback_hom_of_isPushout`.

```lean
public theorem isPullback_homFromSSet_of_isPushout {C : Type u} [Category.{v} C]
    [HasFiniteLimits C] (T : SimplicialObject C) {U V W P : SSet.{v}}
    [∀ n : ℕ, Finite (U _⦋n⦌)] [∀ n : ℕ, Finite (V _⦋n⦌)] [∀ n : ℕ, Finite (W _⦋n⦌)]
    (hUdeg : ∃ d : ℕ, ∀ n : ℕ, d ≤ n → ∀ x : U _⦋n⦌, x ∈ U.degenerate n)
    (hVdeg : ∃ d : ℕ, ∀ n : ℕ, d ≤ n → ∀ x : V _⦋n⦌, x ∈ V.degenerate n)
    (hWdeg : ∃ d : ℕ, ∀ n : ℕ, d ≤ n → ∀ x : W _⦋n⦌, x ∈ W.degenerate n)
    {a : U ⟶ V} {b : U ⟶ W} {f : V ⟶ P} {g : W ⟶ P} (h : IsPushout a b f g) :
    ((∃ H, Nonempty (IsHomFromSSet U T H)) ∧ (∃ H, Nonempty (IsHomFromSSet V T H)) ∧
      (∃ H, Nonempty (IsHomFromSSet W T H)) ∧ (∃ H, Nonempty (IsHomFromSSet P T H))) ∧
    ∀ {HU HV HW HP : SimplicialObject C} (hU : IsHomFromSSet U T HU)
      (hV : IsHomFromSSet V T HV) (hW : IsHomFromSSet W T HW) (hP : IsHomFromSSet P T HP),
      IsPullback (hV.homEquiv.symm (f ≫ hP.homEquiv (𝟙 HP)))
        (hW.homEquiv.symm (g ≫ hP.homEquiv (𝟙 HP)))
        (hU.homEquiv.symm (a ≫ hV.homEquiv (𝟙 HV)))
        (hU.homEquiv.symm (b ≫ hW.homEquiv (𝟙 HW)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.17, Tag 017H](https://stacks.math.columbia.edu/tag/017H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
