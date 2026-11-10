---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupSchemeOverPoints.Action, AlgebraicGeometry.GroupSchemeOverPoints.Action.IsEquivariant, AlgebraicGeometry.GroupSchemeOverPoints.Action.equivModObj, AlgebraicGeometry.GroupSchemeOverPoints.Action.isEquivariant_iff_isModHom, CategoryTheory.ModObj.mul_smul_self, CategoryTheory.ModObj.one_smul_self, AlgebraicGeometry.IsFreeAction, AlgebraicGeometry.isFreeAction_iff_mono_leftSMul
statement: formalized
proof: formalized
---

# 39.10 Actions of group schemes

Section 39.10 of the Stacks Project, [Tag 022Y](https://stacks.math.columbia.edu/tag/022Y). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 022Z, a definition

[Tag 022Z](https://stacks.math.columbia.edu/tag/022Z) in the Stacks Project.

**`AlgebraicGeometry.GroupSchemeOverPoints.Action`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L82). The attribute's comment: “part (1): an action of a group scheme on a scheme over the base”.

> **Stacks Project, Tag 022Z** (1). An action of the group scheme `G` over `S` on the scheme
> `X` over `S`: a morphism `a : G ×_S X ⟶ X` of schemes over `S` such that for every scheme `T`
> over `S` the map `G(T) × X(T) ⟶ X(T)`, `(g, x) ↦ a ∘ (g, x)`, defines the structure of a
> `G(T)`-set on `X(T)`, namely the identity of `G(T)` acts trivially and `(g h) x = g (h x)`.

```lean
structure Action (X : Over S)
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.IsEquivariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L127). The attribute's comment: “part (2): equivariant morphisms”.

> **Stacks Project, Tag 022Z** (2). A morphism `ψ : X ⟶ Y` of schemes over `S`, where `X` and
> `Y` carry actions `A` and `B` of `G`, is `G`-equivariant if for every scheme `T` over `S` the
> map `ψ : X(T) ⟶ Y(T)` is a morphism of `G(T)`-sets.

```lean
def IsEquivariant (A : G.Action X) (B : G.Action Y) (ψ : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.equivModObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L246). The attribute's comment: “part (1): actions are the module objects over the internal group object”.

> **Stacks Project, Tag 022Z** (1), compared with Mathlib. Actions of the group scheme `G`
> on `X` in the functor-of-points sense are the same as module objects `ModObj` over the
> internal group object `G.grpObj` of `Over S`.

```lean
noncomputable def equivModObj (X : Over S) :
    G.Action X ≃ (letI := G.grpObj; ModObj G.obj X)
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Action.isEquivariant_iff_isModHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Action.lean#L257). The attribute's comment: “part (2): equivariant morphisms are the morphisms of module objects”.

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

Declarations registered for the tag:

- [`CategoryTheory.ModObj.mul_smul_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ModObj.mul_smul_self#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L48) (StacksFrontier): “associativity”.
- [`CategoryTheory.ModObj.one_smul_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ModObj.one_smul_self#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L49) (StacksFrontier): “identity”.

## Tag 07S1, a definition

[Tag 07S1](https://stacks.math.columbia.edu/tag/07S1) in the Stacks Project.

**`AlgebraicGeometry.IsFreeAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L57).

> A group object acts freely on `X` if its action on `T`-points is free for every object `T`.

```lean
abbrev IsFreeAction {C : Type u} [Category.{v} C] [CartesianMonoidalCategory C]
    (G X : C) [GrpObj G] [ModObj G X] : Prop
```

## Tag 07S2, a lemma

[Tag 07S2](https://stacks.math.columbia.edu/tag/07S2) in the Stacks Project.

**`AlgebraicGeometry.isFreeAction_iff_mono_leftSMul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Action.lean#L66). References: SGA 3 IV (3.2.1), “(i), special case”; SGA 3 V (10.2.1), “more general”; SGA 4 IV (9.8.2), “Remark after d)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
