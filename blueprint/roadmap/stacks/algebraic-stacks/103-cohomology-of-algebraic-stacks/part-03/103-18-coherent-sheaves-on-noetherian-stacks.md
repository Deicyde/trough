---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.isFiltered_coherentSubobject_and_isColimit
statement: formalized
proof: formalized
---

# 103.18 Coherent sheaves on Noetherian stacks

Section 103.18 of the Stacks Project, [Tag 0GRE](https://stacks.math.columbia.edu/tag/0GRE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GRF, a lemma

[Tag 0GRF](https://stacks.math.columbia.edu/tag/0GRF) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFiltered_coherentSubobject_and_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSubmoduleColimitNoetherian.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSubmoduleColimitNoetherian.lean#L300).

> **Stacks 0GRF.**  Let `𝒳` be a Noetherian algebraic stack.  Every quasi-coherent
> `𝒪_𝒳`-module `ℱ` is the filtered colimit of its coherent submodules: the coherent subobjects of `ℱ`
> in `QCoh(𝒪_𝒳)` form a filtered (nonempty and directed) partially ordered set, and `ℱ` with the
> inclusions is the colimit in `QCoh(𝒪_𝒳)` of the diagram of their underlying modules.
>
> "Submodule" means subobject in `QCoh(𝒪_𝒳)`, the category the source works in.  Read as subsheaves
> of `ℱ` on the big fppf site the statement is false (`k[x, x⁻¹]` on `𝔸¹_k` has no nonzero coherent
> subsheaf: it vanishes over `Spec k[x]/(x)`); see the module docstring.

```lean
theorem isFiltered_coherentSubobject_and_isColimit (h𝒳 : IsNoetherianStack.{u, w, w'} B S hS 𝒳)
    (F : quasicoherentModules B S hS 𝒳) :
    IsFiltered (CoherentSubobject B S hS 𝒳 F) ∧
      Nonempty (IsColimit (coherentSubobjectCocone B S hS 𝒳 F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.18, Tag 0GRE](https://stacks.math.columbia.edu/tag/0GRE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
