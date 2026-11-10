---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.rot_of_distTriang, CategoryTheory.Pretriangulated.inv_rot_of_distTriang, CategoryTheory.Functor.CommShift, CategoryTheory.Functor.mapTriangle, CategoryTheory.Functor.IsTriangulated, CategoryTheory.Functor.IsPretriangulatedSubcategory, CategoryTheory.Functor.IsHomological, CategoryTheory.Functor.map_distinguished_op_exact
statement: formalized
proof: formalized
---

# 13.3 The definition of a triangulated category

Section 13.3 of the Stacks Project, [Tag 05QK](https://stacks.math.columbia.edu/tag/05QK). 6 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05QL, an equation

[Tag 05QL](https://stacks.math.columbia.edu/tag/05QL) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Pretriangulated.rot_of_distTriang`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.rot_of_distTriang#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L75) (StacksFrontier): “pieces on the right: rotation Y → Z → X[1] → Y[1], last map -f[1]”.
- [`CategoryTheory.Pretriangulated.inv_rot_of_distTriang`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pretriangulated.inv_rot_of_distTriang#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L77) (StacksFrontier): “pieces on the left: inverse rotation Z[-1] → X → Y → Z, first map -h[-1]”.

## Tag 014V, a definition

[Tag 014V](https://stacks.math.columbia.edu/tag/014V) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.CommShift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.CommShift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L68) (StacksFrontier): “the functorial isomorphisms ξ : F(X[1]) ≅ F(X)[1] (for every shift by ℤ)”. References: SGA 4 XVII (0.3), “One variable with ε = +1”; SGA 4½ Etat 0 (1.1.0).
- [`CategoryTheory.Functor.mapTriangle`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapTriangle#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L70) (StacksFrontier): “the image triangle (F X, F Y, F Z, F f, F g, ξ_X ∘ F h)”. References: SGA 6 I (1.1.3), “partial”.
- [`CategoryTheory.Functor.IsTriangulated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsTriangulated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L72) (StacksFrontier): “exact (triangulated) functor: the image triangle of every distinguished triangle is distinguished”. References: SGA 4 XVII (1.1.3); SGA 4 XVII (2.2.13.1); SGA 6 I (1.1.3), “partial”.

## Tag 05QM, a definition

[Tag 05QM](https://stacks.math.columbia.edu/tag/05QM) in the Stacks Project.

**`CategoryTheory.Functor.IsPretriangulatedSubcategory`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L244).

> **Stacks 05QM.** A functor `ι : C ⥤ D` between pre-triangulated categories, equipped
> with a commutation with the shift, *exhibits `C` as a pre-triangulated subcategory of `D`*
> if it is faithful and sends distinguished triangles of `C` to distinguished triangles of
> `D`. The set of triangles `T'` of the source is then `distTriang C`, and `T' ⊆ T` is
> `CategoryTheory.Functor.map_distinguished`. If `D` is triangulated, `C` is a *triangulated
> subcategory* of `D` when moreover `CategoryTheory.IsTriangulated C`.

```lean
public class IsPretriangulatedSubcategory (ι : C ⥤ D) [ι.CommShift ℤ] : Prop
    extends ι.Faithful, ι.IsTriangulated
```

## Tag 0147, a definition

[Tag 0147](https://stacks.math.columbia.edu/tag/0147) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsHomological`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsHomological#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L24) (StacksFrontier): “homological functor: sends every distinguished triangle to a sequence H(X) → H(Y) → H(Z) exact in the abelian category; it extends `PreservesZeroMorphisms` and implies `Additive` (instance), so it is the Stacks notion for an additive functor”. References: SGA 4½ Etat 0 (1.3).
- [`CategoryTheory.Functor.map_distinguished_op_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_distinguished_op_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L28) (StacksFrontier): “cohomological functor: Mathlib's form is a homological functor `H : Dᵒᵖ ⥤ A` for the opposite pretriangulated structure, whose defining exactness is H(Z) → H(Y) → H(X) for each distinguished triangle of `D`”.

## Tag 0148, an equation

[Tag 0148](https://stacks.math.columbia.edu/tag/0148) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.homologySequenceδ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.homologySequenceδ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L32) (StacksFrontier): “the connecting map H(h) : H^n(Z) → H^(n+1)(X), with H^n = `F.shift n`”.
- [`CategoryTheory.Functor.homologySequenceComposableArrows₅_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.homologySequenceComposableArrows₅_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L34) (StacksFrontier): “the exact sequence itself, as a `ComposableArrows A 5` from H^n(X) to H^(n+1)(Z); the long exact sequence is the family of these over all n”.

## Tag 0150, a definition

[Tag 0150](https://stacks.math.columbia.edu/tag/0150) in the Stacks Project.

**`CategoryTheory.Functor.DeltaFunctorStructure`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Functor.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Functor.lean#L172).

> The structure of a **`δ`-functor** from an abelian category `𝒜` to a (pre)triangulated
> category `𝒟` on a functor `G : 𝒜 ⥤ 𝒟`: a rule assigning to every short exact sequence
> `0 ⟶ A ⟶ B ⟶ C ⟶ 0` of `𝒜` a connecting morphism `δ : G(C) ⟶ G(A)⟦1⟧` such that the triangle
> `(G(A), G(B), G(C), G(a), G(b), δ)` — the image of the short exact sequence under the
> `δ`-functor — is distinguished, and such that `δ` is natural in the short exact sequence.

```lean
public structure DeltaFunctorStructure (G : 𝒜 ⥤ 𝒟)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.3, Tag 05QK](https://stacks.math.columbia.edu/tag/05QK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
