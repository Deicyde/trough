---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chernCap_tensorObj_of_isInvertibleModule
statement: formalized
proof: formalized
---

# 82.29 Polynomial relations among Chern classes

Section 82.29 of the Stacks Project, [Tag 0ES3](https://stacks.math.columbia.edu/tag/0ES3). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ES4, a lemma

[Tag 0ES4](https://stacks.math.columbia.edu/tag/0ES4) in the Stacks Project.

**`AlgebraicGeometry.Space.chernCap_tensorObj_of_isInvertibleModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassInvertibleTwist.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassInvertibleTwist.lean#L320).

> **Stacks 0ES4, the Chern classes of a twist by an invertible module.** In Situation 0EDT let
> `X/B` be good, let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` and let `ℒ` be an
> invertible `𝒪_X`-module; `ℰ ⊗ ℒ` is finite locally free of rank `r`. Then for every `i`
>
>   `c_i(ℰ ⊗ ℒ) = ∑_{j=0}^{i} C(r + j - i, j) c_{i-j}(ℰ) c₁(ℒ)^j`.
>
> For `i ≤ r` the binomial coefficient is the source's `C(r - i + j, j)`; for `i > r` both sides
> vanish, which is the convention `c_i = 0` above the rank, the left side by vanishing above the
> rank and the right side termwise (`c_{i-j}(ℰ) = 0` for `i - j > r` and `C(r + j - i, j) = 0`
> otherwise).
>
> The Chern classes are those of Stacks 0ERZ, `c_n(ℰ) ∩ -` on `CH_*(X)` (`chernCap`). An identity in
> `A^*(X)` is an identity of the operations on `CH_*(Y)` for every good `Y ⟶ X`; the operation of
> `c_n(ℰ)` on `CH_*(Y)` is `c_n(f^*ℰ) ∩ -`, and `f^*(ℰ ⊗ ℒ) ≅ f^*ℰ ⊗ f^*ℒ` with `f^*ℰ` of rank `r`
> and `f^*ℒ` invertible, so the statement for all good `X` is the statement in `A^*(X)`.

```lean
theorem chernCap_tensorObj_of_isInvertibleModule {X : D.Ambient} {sX : X ⟶ D.space}
    (hX : D.IsGood sX) {E L : Modules.{u, u} D.site D.base D.base_mem X hX.1} {r : ℕ}
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX E r)
    (hL : IsInvertibleModule (goodSpace hX) L) (i : ℕ) :
    chernCap.{u, u + 1} (E ⊗ L) r (isFiniteLocallyFreeOfRank_tensorObj_of_isInvertibleModule hE hL)
        i =
      ∑ j ∈ Finset.range (i + 1), ((r + j - i).choose j : ℤ) •
        (chernCap.{u, u + 1} E r hE (i - j) *
          chernCap.{u, u + 1} L 1
            (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule (goodSpace hX) hL) 1 ^ j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.29, Tag 0ES3](https://stacks.math.columbia.edu/tag/0ES3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
