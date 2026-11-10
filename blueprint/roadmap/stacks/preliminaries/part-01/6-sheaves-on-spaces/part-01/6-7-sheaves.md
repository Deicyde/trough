---
declaration: section
origin: cited
lean: TopCat.Presheaf.IsSheafUniqueGluing, TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types, TopCat.Sheaf.existsUnique_gluing, TopCat.Sheaf.forget, TopCat.Sheaf, TopCat.instCategorySheaf, TopCat.Sheaf.isTerminalOfEmpty, TopCat.Sheaf.isProductOfDisjoint
statement: formalized
proof: formalized
---

# 6.7 Sheaves

Section 6.7 of the Stacks Project, [Tag 006S](https://stacks.math.columbia.edu/tag/006S). 6 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 006T, a definition

[Tag 006T](https://stacks.math.columbia.edu/tag/006T) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.IsSheafUniqueGluing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsSheafUniqueGluing#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L29) (StacksFrontier): “the unique-gluing sheaf condition for a presheaf of sets”. References: EGA 0 (3.1.2), “concrete category C”; SGA 4½ Arcata (1.2.3); SGA 4½ Arcata (1.6.3), “topological site”; SGA 4 II (2.1), “opens of a space”.
- [`TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L35) (StacksFrontier): “agreement of the unique-gluing condition with the categorical one”. References: EGA 0 (3.1.2), “C = Set”; SGA 3 IV (4.3.5), “special case”; SGA 4½ Arcata (1.6.3), “topological site”.
- [`TopCat.Sheaf.existsUnique_gluing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf.existsUnique_gluing#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L40) (StacksFrontier): “a compatible family over an open covering glues to a unique section”. References: EGA 0 (3.1.2), “concrete category C”; SGA 4½ Arcata (1.6.3), “topological site”.
- [`TopCat.Sheaf.forget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf.forget#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L44) (StacksFrontier): “a morphism of sheaves of sets is a morphism of the underlying presheaves: the forgetful functor to presheaves is fully faithful”. References: SGA 3 IV (4.3.13), “special case”.
- [`TopCat.Sheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L47) (StacksFrontier): “sheaves of sets on `X`, the objects of `Sh(X)`”. References: EGA 0 (3.1.4); EGA 0 (3.1.2); SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.18), “special case”; SGA 4 II (6.1), “special case”; SGA 4 IV (0.1), “special case”; SGA 4 IV (2.1); SGA 4 VI (1.22.1); SGA 4 Vbis (4.2.0), “Fiber of E over a scheme”; SGA 4½ Arcata (1.2.3), “more general”; SGA 4½ Arcata (1.6.3), “topological site”; SGA 4 II (2.1), “opens of a space”.
- [`TopCat.instCategorySheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.instCategorySheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Basic.lean#L51) (StacksFrontier): “the category `Sh(X)`”. References: SGA 3 IV (4.3.1), “special case”; SGA 4 II (6.1), “special case”; SGA 4 IV (0.1), “special case”; SGA 4 IV (2.1), “partial”; SGA 4 II (2.1), “opens of a space”.

## Tag 006U, a remark

[Tag 006U](https://stacks.math.columbia.edu/tag/006U) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Sheaf.isTerminalOfEmpty`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf.isTerminalOfEmpty#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch06.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch06.lean#L15) (StacksFrontier): “F(∅) is a final object”. References: SGA 4 IV (2.2), “Necessity”.
- [`TopCat.Sheaf.isProductOfDisjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf.isProductOfDisjoint#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch06.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch06.lean#L16) (StacksFrontier): “disjoint opens: F(U ∪ V) = F(U) × F(V)”.

## Tag 006V, an example

[Tag 006V](https://stacks.math.columbia.edu/tag/006V) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.presheafToTop`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.presheafToTop#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean#L23) (StacksFrontier): “the presheaf `U ↦ {f : U → Y | f continuous}` on `X`”. References: SGA 6 II (AppII.3.0.1), “presheaf U ↦ C(U,Y)”.
- [`TopCat.sheafToTop`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.sheafToTop#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean#L25) (StacksFrontier): “that presheaf is a sheaf”. References: SGA 4½ Arcata (1.2.3), “more general”; SGA 5 VII (3.8), “partial”; SGA 6 II (AppII.3.0.1).
- [`ContinuousMap.liftCover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ContinuousMap.liftCover#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/OfContinuousMaps.lean#L29) (StacksFrontier): “the gluing of a compatible family of continuous maps over an open covering”. References: SGA 4½ Arcata (1.2.3), “partial”.

## Tag 006W, a definition

[Tag 006W](https://stacks.math.columbia.edu/tag/006W) in the Stacks Project.

**`constantSheafOnSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/Constant.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/Constant.lean#L79). References: EGA 0 (3.6.1), “simple sheaf”; SGA 4 IV (4.3.4), “sheaves on a space”; SGA 4 IV (11.1.5), “special case”; SGA 4 IV (2.7.5), “special case”; SGA 4 IX (2.0), “special case”; SGA 4 Vbis (4.1.0), “partial”.

> The constant sheaf on a topological space `X` with value `A : C`,
> defined as the sheafification of the constant presheaf with value `A`.
> This is Stacks Tag 006W.

```lean
noncomputable def constantSheafOnSpace (X : TopCat) (C : Type*) [Category C]
    [HasWeakSheafify (Opens.grothendieckTopology X) C] (A : C) :
    Sheaf (Opens.grothendieckTopology X) C
```

## Tag 006X, an example

[Tag 006X](https://stacks.math.columbia.edu/tag/006X) in the Stacks Project.

**`presheafToTypes_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PointwiseProduct.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PointwiseProduct.lean#L58).

> Let `X` be a topological space and `A : X → Type u` a family of sets indexed by the points of
> `X`. The pointwise product presheaf `Π`, given on an open `U` by `Π(U) = ∏_{x ∈ U} A x` (encoded as
> the dependent product `∀ x : U, A x`, i.e. Mathlib's `TopCat.presheafToTypes X A`), with
> restriction sending `(a_x)_{x ∈ U}` to `(a_x)_{x ∈ V}` for `V ⊆ U`, is a sheaf of sets.

```lean
theorem presheafToTypes_isSheaf {X : TopCat.{u}} (A : X → Type u) :
    (X.presheafToTypes A).IsSheaf
```

## Tag 006Y, an example

[Tag 006Y](https://stacks.math.columbia.edu/tag/006Y) in the Stacks Project.

**`directSumOverPointsPresheaf_not_isSheaf_in_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/DirectSumOverPoints.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/DirectSumOverPoints.lean#L158).

> **Stacks Tag 006Y.** Let `X` be a topological space and `M : X → Type u`
> be a family of abelian groups indexed by the points of `X`. The presheaf
> `U ↦ ⨁_{x ∈ U} M x` is **not** a sheaf in general: there exists a
> topological space `X` and a family `M` for which the presheaf fails to be
> a sheaf.
>
> The witness is `X = ULift ℕ` with the discrete topology and the constant
> family `M_x = ULift ℤ`. The singleton sets `{n}` form an open cover of `X`,
> and the family of sections `s_n = (n ↦ 1)` is compatible (pairwise
> intersections are empty). However, any gluing would have to take value
> `1 ≠ 0` at every point of `X`, contradicting the finite-support property
> of the direct sum.

```lean
theorem directSumOverPointsPresheaf_not_isSheaf_in_general :
    ∃ (X : TopCat.{u}) (M : X → Type u) (_ : ∀ x, AddCommGroup (M x)),
      ¬ (directSumOverPointsPresheaf (X := X) M).IsSheaf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.7, Tag 006S](https://stacks.math.columbia.edu/tag/006S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
