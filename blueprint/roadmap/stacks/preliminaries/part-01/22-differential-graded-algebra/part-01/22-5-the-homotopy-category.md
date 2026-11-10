---
declaration: section
origin: cited
lean: DifferentialGradedModule.Homotopy, DifferentialGradedModule.Homotopic, DifferentialGradedModule.Homotopy.exists_comp, DifferentialGradedModule.HomotopyCategory, DifferentialGradedModule.preservesCoproducts_toHomotopyCategory, DifferentialGradedModule.hasProducts_homotopyCategory, DifferentialGradedModule.hasCoproducts_homotopyCategory
statement: formalized
proof: formalized
---

# 22.5 The homotopy category

Section 22.5 of the Stacks Project, [Tag 09JM](https://stacks.math.columbia.edu/tag/09JM). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09JN, a definition

[Tag 09JN](https://stacks.math.columbia.edu/tag/09JN) in the Stacks Project.

**`DifferentialGradedModule.Homotopy`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean#L58). The attribute's comment: “homotopy between morphisms”.

> An `A`-linear degree `-1` homotopy between homomorphisms of differential graded
> `A`-modules.

```lean
structure Homotopy (f g : Hom M N)
```

**`DifferentialGradedModule.Homotopic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean#L76). The attribute's comment: “homotopic morphisms”.

> Two homomorphisms of differential graded modules are homotopic if a homotopy between them
> exists.

```lean
abbrev Homotopic (f g : Hom M N) : Prop
```

## Tag 09JP, a lemma

[Tag 09JP](https://stacks.math.columbia.edu/tag/09JP) in the Stacks Project.

**`DifferentialGradedModule.Homotopy.exists_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Homotopy.lean#L81).

> Composing a homotopy with homomorphisms of differential graded modules on either side gives
> a homotopy whose underlying map is the corresponding composite.

```lean
theorem Homotopy.exists_comp {K L : DifferentialGradedModule.{u, v, w} A} (f g : Hom L M)
    (a : Hom K L) (c : Hom M N) (h : Homotopy f g) :
    ∃ k : Homotopy (c.comp (f.comp a)) (c.comp (g.comp a)),
      ∀ x : K.M, k.toLinearMap x = c.toFun (h.toLinearMap (a.toFun x))
```

## Tag 09JQ, a definition

[Tag 09JQ](https://stacks.math.columbia.edu/tag/09JQ) in the Stacks Project.

**`DifferentialGradedModule.HomotopyCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategory.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategory.lean#L119).

> The homotopy category of right differential graded `A`-modules.

```lean
abbrev HomotopyCategory (A : DifferentialGradedAlgebra R) : Type _
```

## Tag 09JR, a lemma

[Tag 09JR](https://stacks.math.columbia.edu/tag/09JR) in the Stacks Project.

**`DifferentialGradedModule.preservesCoproducts_toHomotopyCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryCoproducts.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryCoproducts.lean#L295). The attribute's comment: “homotopy_direct_sums_preserved”.

> The quotient functor preserves direct sums indexed by a type in the ambient universe.

```lean
instance preservesCoproducts_toHomotopyCategory (A : DifferentialGradedAlgebra R)
    (ι : Type u) :
    PreservesColimitsOfShape (Discrete ι) (toHomotopyCategory A)
```

**`DifferentialGradedModule.hasProducts_homotopyCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryLimits.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryLimits.lean#L199). The attribute's comment: “homotopy_products”.

> The homotopy category of differential graded modules over a differential graded algebra has
> all products.

```lean
instance hasProducts_homotopyCategory (A : DifferentialGradedAlgebra.{u, v} R) :
    HasProducts.{w} (HomotopyCategory.{u, v, w} A)
```

**`DifferentialGradedModule.hasCoproducts_homotopyCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryLimits.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyCategoryLimits.lean#L401). The attribute's comment: “homotopy_direct_sums”.

> The homotopy category of differential graded modules has direct sums.

```lean
instance hasCoproducts_homotopyCategory (A : DifferentialGradedAlgebra.{u, v} R) :
    HasCoproducts.{w} (HomotopyCategory.{u, v, w} A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.5, Tag 09JM](https://stacks.math.columbia.edu/tag/09JM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
