---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupSchemeOverPoints.Action, AlgebraicGeometry.GroupSchemeOverPoints.Action.IsEquivariant, AlgebraicGeometry.GroupSchemeOverPoints.Action.equivModObj, AlgebraicGeometry.GroupSchemeOverPoints.Action.isEquivariant_iff_isModHom, AlgebraicGeometry.GroupSchemeOverPoints.Action.exists_act_eq_iff, AlgebraicGeometry.IsFreeAction, AlgebraicGeometry.isFreeAction_iff_mono_leftSMul
statement: formalized
proof: formalized
---

# 39.10 Actions of group schemes

Section 39.10 of the Stacks Project, [Tag 022Y](https://stacks.math.columbia.edu/tag/022Y). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 022Z, a definition

[Tag 022Z](https://stacks.math.columbia.edu/tag/022Z) in the Stacks Project.

**`AlgebraicGeometry.GroupSchemeOverPoints.Action`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L85). The attribute's comment: “part (1): an action of a group scheme on a scheme over the base”.

> **Stacks Project, Tag 022Z** (1). An action of the group scheme `G` over `S` on the scheme
> `X` over `S`: a morphism `a : G ×_S X ⟶ X` of schemes over `S` such that for every scheme `T`
> over `S` the map `G(T) × X(T) ⟶ X(T)`, `(g, x) ↦ a ∘ (g, x)`, defines the structure of a
> `G(T)`-set on `X(T)`, namely the identity of `G(T)` acts trivially and `(g h) x = g (h x)`.

```lean
structure Action (X : Over S)
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.IsEquivariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L130). The attribute's comment: “part (2): equivariant morphisms”.

> **Stacks Project, Tag 022Z** (2). A morphism `ψ : X ⟶ Y` of schemes over `S`, where `X` and
> `Y` carry actions `A` and `B` of `G`, is `G`-equivariant if for every scheme `T` over `S` the
> map `ψ : X(T) ⟶ Y(T)` is a morphism of `G(T)`-sets.

```lean
def IsEquivariant (A : G.Action X) (B : G.Action Y) (ψ : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.equivModObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L249). The attribute's comment: “part (1): actions are the module objects over the internal group object”.

> **Stacks Project, Tag 022Z** (1), compared with Mathlib. Actions of the group scheme `G`
> on `X` in the functor-of-points sense are the same as module objects `ModObj` over the
> internal group object `G.grpObj` of `Over S`.

```lean
noncomputable def equivModObj (X : Over S) :
    G.Action X ≃ (letI := G.grpObj; ModObj G.obj X)
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.isEquivariant_iff_isModHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L260). The attribute's comment: “part (2): equivariant morphisms are the morphisms of module objects”.

> **Stacks Project, Tag 022Z** (2), compared with Mathlib. A morphism `ψ : X ⟶ Y` over `S` is
> `G`-equivariant for actions `A` and `B` exactly when it is a morphism `IsModHom` of the
> associated module objects over the internal group object `G.grpObj`.

```lean
theorem isEquivariant_iff_isModHom (A : G.Action X) (B : G.Action Y) (ψ : X ⟶ Y) :
    IsEquivariant A B ψ ↔
      letI := G.grpObj
      letI := A.modObj
      letI := B.modObj
      IsModHom G.obj ψ
```

## Tag 03LD, an equation

[Tag 03LD](https://stacks.math.columbia.edu/tag/03LD) in the Stacks Project.

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.exists_act_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L292). The attribute's comment: “actions in the sense of 022Z are the morphisms making both diagrams commute”.

> **Stacks Project, Tag 03LD**. A morphism `a : G ×_S X ⟶ X` of schemes over `S` is an action
> of `G` on `X/S` in the sense of Tag 022Z (it makes every `X(T)` a `G(T)`-set) exactly when the
> associativity diagram `a ∘ (m × 1_X) = a ∘ (1_G × a)` and the unit diagram
> `a ∘ (e × 1_X) = 1_X` commute.

```lean
theorem exists_act_eq_iff (a : G.obj ⊗ X ⟶ X) :
    (∃ A : G.Action X, A.act = a) ↔
      (G.mul ▷ X) ≫ a = (α_ G.obj G.obj X).hom ≫ (G.obj ◁ a) ≫ a ∧
        lift (toUnit X ≫ (1 : 𝟙_ (Over S) ⟶ G.obj)) (𝟙 X) ≫ a = 𝟙 X
```

## Tag 07S1, a definition

[Tag 07S1](https://stacks.math.columbia.edu/tag/07S1) in the Stacks Project.

**`AlgebraicGeometry.IsFreeAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L53).

> A group object acts freely on `X` if its action on `T`-points is free for every object `T`.

```lean
abbrev IsFreeAction {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] : Prop
```

## Tag 07S2, a lemma

[Tag 07S2](https://stacks.math.columbia.edu/tag/07S2) in the Stacks Project.

**`AlgebraicGeometry.isFreeAction_iff_mono_leftSMul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L62). References: SGA 3 IV (3.2.1), “(i), special case”; SGA 3 V (10.2.1), “more general”; SGA 4 IV (9.8.2), “Remark after d)”.

> A group action is free if and only if `(g, x) ↦ (g • x, x)` is a monomorphism.

```lean
lemma isFreeAction_iff_mono_leftSMul {C : Type u} [Category.{v} C]
    [CartesianMonoidalCategory C] (G X : C) [GrpObj G] [ModObj G X] :
    IsFreeAction G X ↔ Mono (ModObj.leftSMul G X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.10, Tag 022Y](https://stacks.math.columbia.edu/tag/022Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
