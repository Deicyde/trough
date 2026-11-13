---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chernCapGraded_tensorObj_of_isInvertibleModule
statement: formalized
proof: formalized
---

# 82.29 Polynomial relations among Chern classes

Section 82.29 of the Stacks Project, [Tag 0ES3](https://stacks.math.columbia.edu/tag/0ES3). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ES4, a lemma

[Tag 0ES4](https://stacks.math.columbia.edu/tag/0ES4) in the Stacks Project.

**`AlgebraicGeometry.Space.chernCapGraded_tensorObj_of_isInvertibleModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTensorInvertible.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTensorInvertible.lean#L83). The attribute's comment: “c\_i(E ⊗ L) = sum\_\{j=0}^\{i} binom(r-i+j, j) c\_\{i-j}(E) c\_1(L)^j in A^*(X) for the Chern classes of Definition 0ERZ (chernClass), as the identity of their cap operations of Lemma 0ERY on ⊕\_k CH\_k(X') (chernCapGraded, product = composition) for every good test space X' → X”.

> **Stacks 0ES4, the Chern classes of a twist by an invertible module.** In Situation 0EDT let
> `X/B` be good, let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` and let `ℒ` be an
> invertible `𝒪_X`-module; `ℰ ⊗ ℒ` is finite locally free of rank `r`. Then for every
> `i = 0, …, r` (the range of the Chern classes of Definition 0ERZ)
>
>   `c_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} C(r - i + j, j) c_{i-j}(ℰ) c₁(ℒ)^j`   in `A^*(X)`,
>
> for the Chern classes `c_j ∈ A^j(X)` of Stacks 0ERZ (`AlgebraicGeometry.Space.chernClass`); for
> `j ≤ i ≤ r` the source's `C(r - i + j, j)` is written `C(r + j - i, j)` in natural numbers.
>
> The product of `A^*(X)` is composition (Stacks 0ERK) and a bivariant class is determined by its
> cap operations on the good test spaces `g : X' ⟶ X` (Stacks 0ERJ), the cap operation of
> `c_j(ℰ)` on `X'` being `c_j(ℰ) ∩ -` of Stacks 0ERY (`AlgebraicGeometry.Space.chernClass_cap`).
> The identity is stated as that of the cap operations on `⨁_k CH_k(X')` for every good
> `g : X' ⟶ X`: `c_j(ℰ) ∩ -` is `chernCapGraded`, and the product is composition.

```lean
theorem chernCapGraded_tensorObj_of_isInvertibleModule
    {E L : Modules.{u, u} D.site D.base D.base_mem X hX.1} {r : ℕ}
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX E r)
    (hL : IsInvertibleModule (goodSpace hX) L) (i : Fin (r + 1)) {Y : D.Ambient} (g : Y ⟶ X)
    (hY : D.IsGood (g ≫ sX)) :
    chernCapGraded D sX hX (E ⊗ L) r
        (isFiniteLocallyFreeOfRank_tensorObj_of_isInvertibleModule hE hL) g hY i =
      ∑ j : Fin ((i : ℕ) + 1), ((r + (j : ℕ) - (i : ℕ)).choose (j : ℕ) : ℤ) •
        (chernCapGraded D sX hX E r hE g hY ⟨(i : ℕ) - (j : ℕ), by have := i.isLt; omega⟩ *
          chernCapGraded D sX hX L 1
            (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule (goodSpace hX) hL) g hY 1 ^
            (j : ℕ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.29, Tag 0ES3](https://stacks.math.columbia.edu/tag/0ES3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
