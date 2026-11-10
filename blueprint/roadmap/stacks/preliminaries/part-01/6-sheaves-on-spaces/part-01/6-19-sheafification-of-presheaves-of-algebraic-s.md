---
declaration: section
origin: cited
lean: AlgebraicStructureType.exists_sheafification
statement: formalized
proof: formalized
---

# 6.19 Sheafification of presheaves of algebraic structures

Section 6.19 of the Stacks Project, [Tag 0086](https://stacks.math.columbia.edu/tag/0086). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0087, a lemma

[Tag 0087](https://stacks.math.columbia.edu/tag/0087) in the Stacks Project.

**`AlgebraicStructureType.exists_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/AlgebraicStructure.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/AlgebraicStructure.lean#L80). References: EGA 0 (3.5.6), “algebraic structures”; SGA 4 II (6.4), “topological space site”.

> **Stacks Tag 0087.**
>
> Let `X` be a topological space, `(C, F)` a type of algebraic structure and `P` a presheaf
> on `X` with values in `C`.  There is a sheaf `P^#` with values in `C` and a morphism
> `η : P ⟶ P^#` of `C`-valued presheaves such that
>
> 1. `η` identifies the underlying presheaf of sets of `P^#` with the sheafification of the
>    underlying presheaf of sets of `P`: there is an isomorphism `e` from
>    `sheafify J (P ⋙ F)` to `P^# ⋙ F` under `P ⋙ F`, i.e. one satisfying
>    `toSheafify J (P ⋙ F) ≫ e.hom = whiskerRight η F`;
> 2. every morphism `ψ : P ⟶ G` into a `C`-valued sheaf `G` factors uniquely as
>    `P ⟶ P^# ⟶ G`.

```lean
theorem exists_sheafification (X : TopCat.{u}) (P : (Opens X)ᵒᵖ ⥤ A.C) :
    ∃ (Psharp : Sheaf (Opens.grothendieckTopology X) A.C) (η : P ⟶ Psharp.obj),
      (∃ e : sheafify (Opens.grothendieckTopology X) (P ⋙ A.F) ≅ Psharp.obj ⋙ A.F,
          toSheafify (Opens.grothendieckTopology X) (P ⋙ A.F) ≫ e.hom =
            Functor.whiskerRight η A.F) ∧
      ∀ (G : Sheaf (Opens.grothendieckTopology X) A.C) (ψ : P ⟶ G.obj),
        ∃! χ : Psharp ⟶ G, η ≫ χ.hom = ψ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.19, Tag 0086](https://stacks.math.columbia.edu/tag/0086)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
