---
declaration: section
origin: cited
lean: Stacks.Chow.TotalChowClass.totalChern_sheafTensor
statement: formalized
proof: formalized
---

# 42.39 Polynomial relations among Chern classes

Section 42.39 of the Stacks Project, [Tag 02UB](https://stacks.math.columbia.edu/tag/02UB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02UD, a lemma

[Tag 02UD](https://stacks.math.columbia.edu/tag/02UD) in the Stacks Project.

**`Stacks.Chow.TotalChowClass.totalChern_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TwistFormula.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TwistFormula.lean#L513). The attribute's comment: “Equation (02UE) in A^*(X), as the single identity c(E tensor L) = T\_\{r,c\_1(L)}(c(E)) of total Chow cohomology classes, under the source's hypotheses and no others. It is Equation (02UE) in each degree i by Stacks.Chow.TotalChowClass.totalChern\_sheafTensor\_degree”.

> **Stacks 02UD for total classes**: for `ℰ` finite locally free of rank `r` and `ℒ`
> invertible, `c(ℰ ⊗ ℒ) = T_{r,c₁(ℒ)}(c(ℰ))`, that is,
> `c_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} binom(r - i + j, j) c_{i-j}(ℰ) c₁(ℒ)^j`.
>
> This is the identity of Stacks 02UD in the Chow cohomology of `Y`. It holds in every degree `i`
> separately, as `Stacks.Chow.TotalChowClass.totalChern_sheafTensor_degree` states.

```lean
theorem totalChern_sheafTensor (E : Y.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] :
    -- `totalChern` reads the rank of a `Y.Modules`, so it asks for the twist's rank at
    -- `Y.ringCatSheaf`, while `GenuineChern.isFiniteLocallyFreeOfRank_sheafTensor` states it at
    -- the native `Tensor.ringSheaf Y.sheaf`. The two are the same sheaf of rings, but only
    -- after unfolding the `Tensor.ringSheaf` def, which instance search does not do, so the
    -- twist's rank is handed over by name at the spelling the statement needs.
    letI : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (R := Y.ringCatSheaf)
        (((Stacks.SheafOfModules.Tensor.sheafTensor Y.sheaf).obj E).obj L) r :=
      GenuineChern.isFiniteLocallyFreeOfRank_sheafTensor E r L
    totalChern C sY (((Stacks.SheafOfModules.Tensor.sheafTensor Y.sheaf).obj E).obj L) r =
      twist (r : ℤ) (firstChernTotal C sY L) (totalChern C sY E r)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.39, Tag 02UB](https://stacks.math.columbia.edu/tag/02UB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
