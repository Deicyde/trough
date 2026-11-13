---
declaration: section
origin: cited
lean: SSet.modelCategoryQuillen.fibration_iff, SSet.modelCategoryQuillen.J, SSet.KanComplex, SSet.modelCategoryQuillen.isStableUnderBaseChange_fibrations, SSet.hasLiftingProperty_horn_ι_comp, SSet.fibration_limit_π_zero, SSet.modelCategoryQuillen.isStableUnderProductsOfShape_fibrations, CategoryTheory.SimplicialObject.kanComplex_forget
statement: formalized
proof: formalized
---

# 14.31 Kan fibrations

Section 14.31 of the Stacks Project, [Tag 08NT](https://stacks.math.columbia.edu/tag/08NT). 9 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08NU, a definition

[Tag 08NU](https://stacks.math.columbia.edu/tag/08NU) in the Stacks Project.

Declarations registered for the tag:

- [`SSet.modelCategoryQuillen.fibration_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SSet.modelCategoryQuillen.fibration_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L131) (StacksFrontier): “Kan fibration: right lifting property against the horn inclusions `J`”.
- [`SSet.modelCategoryQuillen.J`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SSet.modelCategoryQuillen.J#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L133) (StacksFrontier): “Kan fibration: `J`, the horn inclusions `Λ[n+1, i] ⟶ Δ[n+1]`”.
- [`SSet.KanComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SSet.KanComplex#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L135) (StacksFrontier): “Kan complex: `S ⟶ ⊤_ SSet` is a Kan fibration”.

## Tag 08NV, a lemma

[Tag 08NV](https://stacks.math.columbia.edu/tag/08NV) in the Stacks Project.

**`SSet.modelCategoryQuillen.isStableUnderBaseChange_fibrations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean#L94).

> **Stacks 08NV**.
> Kan fibrations of simplicial sets are stable under arbitrary base change. Under
> `fibrations_eq`, they are a right lifting class, and every right lifting class has this closure
> property.

```lean
public theorem isStableUnderBaseChange_fibrations :
    (fibrations SSet.{u}).IsStableUnderBaseChange
```

## Tag 08NW, a lemma

[Tag 08NW](https://stacks.math.columbia.edu/tag/08NW) in the Stacks Project.

**`SSet.hasLiftingProperty_horn_ι_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean#L79). The attribute's comment: “the source's lifting condition, one horn inclusion `Λ[n + 1, i].ι` of Tag 08NU at a time; the same statement for the bundled predicate `HomotopicalAlgebra.Fibration` of the Quillen model structure on `SSet` is upstream's multiplicativity of `fibrations SSet`”.

> **Stacks 08NW**.
> The composition of two Kan fibrations is a Kan fibration: if `f : X ⟶ Y` and `g : Y ⟶ Z` are
> morphisms of simplicial sets each having the right lifting property with respect to all horn
> inclusions, then so does `f ≫ g`.

```lean
public theorem hasLiftingProperty_horn_ι_comp {X Y Z : SSet.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : ∀ (n : ℕ) (i : Fin (n + 2)), HasLiftingProperty Λ[n + 1, i].ι f)
    (hg : ∀ (n : ℕ) (i : Fin (n + 2)), HasLiftingProperty Λ[n + 1, i].ι g) :
    ∀ (n : ℕ) (i : Fin (n + 2)), HasLiftingProperty Λ[n + 1, i].ι (f ≫ g)
```

## Tag 08NX, a lemma

[Tag 08NX](https://stacks.math.columbia.edu/tag/08NX) in the Stacks Project.

**`SSet.fibration_limit_π_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean#L513). The attribute's comment: “Kan fibrations are Mathlib's fibrations for the Quillen model structure on `SSet`, whose generating family `J` is the horn inclusions of Tag 08NU”.

> **Stacks 08NX**.
> Let `F : ℕᵒᵖ ⥤ SSet` be a tower `⋯ → U² → U¹ → U⁰` of simplicial sets each of whose transition
> morphisms `Uᵗ⁺¹ ⟶ Uᵗ` is a Kan fibration. Then the canonical projection
> `limit F ⟶ U⁰ = F.obj (op 0)` from the inverse limit to the bottom term is a Kan fibration.

```lean
theorem fibration_limit_π_zero (F : ℕᵒᵖ ⥤ SSet)
    (hF : ∀ t : ℕ, Fibration (F.map (homOfLE (Nat.le_succ t)).op)) :
    Fibration (limit.π F (Opposite.op 0))
```

## Tag 08NY, a lemma

[Tag 08NY](https://stacks.math.columbia.edu/tag/08NY) in the Stacks Project.

**`SSet.modelCategoryQuillen.isStableUnderProductsOfShape_fibrations`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean#L107). The attribute's comment: “Kan fibrations are Mathlib's fibrations for the Quillen model structure on `SSet`, whose generating family `J` is the horn inclusions of Tag 08NU; stability under products is stated for arbitrary product cones, the source's `∏ X_i → ∏ Y_i` being the case of `Limits.Pi.map`”.

> **Stacks 08NY**.
> A product of Kan fibrations is a Kan fibration: if `f i : X i ⟶ Y i` is a family of morphisms of
> simplicial sets each having the right lifting property with respect to all horn inclusions, then so
> does the induced morphism `∏ X i ⟶ ∏ Y i` between any products of the `X i` and the `Y i`.

```lean
public instance isStableUnderProductsOfShape_fibrations (J : Type w) :
    (fibrations SSet.{u}).IsStableUnderProductsOfShape J
```

## Tag 08NZ, a lemma

[Tag 08NZ](https://stacks.math.columbia.edu/tag/08NZ) in the Stacks Project.

**`CategoryTheory.SimplicialObject.kanComplex_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanComplex/SimplicialGroup.lean#L64). The attribute's comment: “a simplicial group is Mathlib's `SimplicialObject GrpCat`, and its underlying simplicial set is `X ⋙ forget GrpCat`”.

> **Stacks 08NZ**.
> Let `X` be a simplicial group. Then the underlying simplicial set of `X` is a Kan complex.

```lean
theorem kanComplex_forget (X : SimplicialObject GrpCat.{u}) :
    KanComplex (X ⋙ forget GrpCat)
```

## Tag 08P0, a lemma

[Tag 08P0](https://stacks.math.columbia.edu/tag/08P0) in the Stacks Project.

**`CategoryTheory.SimplicialObject.fibration_whiskerRight_forget_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/KanFibration.lean#L424). The attribute's comment: “stated for simplicial groups written additively, commutativity being unused by the source's argument (which reduces to Tag 08NZ, a statement about simplicial groups); the source's simplicial abelian groups are the case of `Functor.whiskerRight f (forget₂ AddCommGrpCat AddGrpCat)`, whose conclusion is the same term by `rfl`. Kan fibrations are Mathlib's fibrations for the Quillen model structure on `SSet`, whose generating family `J` is the horn inclusions of Tag 08NU”.

> **Stacks 08P0**.
> A termwise surjective homomorphism of simplicial groups is a Kan fibration: if `f : X ⟶ Y` is a
> morphism of simplicial groups such that `X_n → Y_n` is surjective for every `n`, then the induced
> morphism of underlying simplicial sets has the right lifting property with respect to all horn
> inclusions.

```lean
public theorem fibration_whiskerRight_forget_of_surjective
    {X Y : SimplicialObject AddGrpCat.{u}} (f : X ⟶ Y)
    (hf : ∀ n : SimplexCategoryᵒᵖ, Function.Surjective (f.app n).hom) :
    Fibration (Functor.whiskerRight f (forget AddGrpCat.{u}))
```

## Tag 08P1, a lemma

[Tag 08P1](https://stacks.math.columbia.edu/tag/08P1) in the Stacks Project.

**`CategoryTheory.SimplicialObject.trivialKanFibrations_whiskerRight_forget_of_surjective_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/SimplicialAbelianGroup.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/SimplicialAbelianGroup.lean#L863). The attribute's comment: “trivial Kan fibrations are the class `SSet.trivialKanFibrations` of Tag 08NL, the right lifting class of the boundary inclusions, the source's surjectivity of `X₀ → Y₀` being its case `n = 0`; the associated chain complex is `s`, Mathlib's `alternatingFaceMapComplex`, the hypothesis being equivalent to the one for the normalized complex `N` by Tag 019C”.

> **Stacks 08P1**.
> If `f : X ⟶ Y` is a
> morphism of simplicial abelian groups such that `X_n → Y_n` is surjective for every `n` and such
> that `s(X) → s(Y)` is a quasi-isomorphism of associated chain complexes, then the induced
> morphism of underlying simplicial sets has the right lifting property with respect to all boundary
> inclusions `∂Δ[n].ι : ∂Δ[n] ⟶ Δ[n]`.

```lean
public theorem trivialKanFibrations_whiskerRight_forget_of_surjective_of_quasiIso
    {X Y : SimplicialObject AddCommGrpCat.{u}} (f : X ⟶ Y)
    (hf : ∀ n : SimplexCategoryᵒᵖ, Function.Surjective (f.app n).hom)
    [QuasiIso ((alternatingFaceMapComplex AddCommGrpCat.{u}).map f)] :
    SSet.trivialKanFibrations (Functor.whiskerRight f (forget AddCommGrpCat.{u}))
```

## Tag 08P2, a lemma

[Tag 08P2](https://stacks.math.columbia.edu/tag/08P2) in the Stacks Project.

**`AlgebraicTopology.quasiIso_alternatingFaceMapComplex_map_of_homotopyEquivalences_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/SimplicialAbelianGroup.lean, line 910](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/SimplicialAbelianGroup.lean#L910). The attribute's comment: “the homotopy equivalence is asked of the underlying simplicial sets, `SimplicialObject.homotopyEquivalences (Type u)` (Tag 019N at `C = Type u`) applied to `Functor.whiskerRight f (forget AddCommGrpCat)`; the associated chain complex is `s`, Mathlib's `alternatingFaceMapComplex`, so that the conclusion is verbatim the hypothesis of 08P1, the version for the normalized complex `N` being equivalent to it by Tag 019C”.

> **Stacks 08P2**.
> Let `f : X ⟶ Y` be a morphism of simplicial
> abelian groups whose underlying morphism of simplicial sets `X ⋙ forget ⟶ Y ⋙ forget` is a
> homotopy equivalence, i.e. admits a morphism of simplicial sets back whose two composites with
> it are homotopic to the identities ([Stacks, Tag 019N]). Then the induced morphism
> `s(X) ⟶ s(Y)` of Moore complexes is a quasi-isomorphism.

```lean
public theorem quasiIso_alternatingFaceMapComplex_map_of_homotopyEquivalences_forget
    {X Y : SimplicialObject AddCommGrpCat.{u}} (f : X ⟶ Y)
    (hf : SimplicialObject.homotopyEquivalences (Type u)
      (Functor.whiskerRight f (forget AddCommGrpCat.{u}))) :
    QuasiIso ((alternatingFaceMapComplex AddCommGrpCat.{u}).map f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.31, Tag 08NT](https://stacks.math.columbia.edu/tag/08NT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
