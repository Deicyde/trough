---
declaration: section
origin: cited
lean: Stacks.Chow.TotalChowClass.totalChern_sheafTensor, Stacks.Chow.chernCapFamily_tensorObj_eq_binomialTransform
statement: formalized
proof: formalized
---

# 42.39 Polynomial relations among Chern classes

Section 42.39 of the Stacks Project, [Tag 02UB](https://stacks.math.columbia.edu/tag/02UB). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02UD, a lemma

[Tag 02UD](https://stacks.math.columbia.edu/tag/02UD) in the Stacks Project.

**`Stacks.Chow.TotalChowClass.totalChern_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TwistFormula.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDerived/TwistFormula.lean#L513). The attribute's comment: “Equation (02UE) in A^*(X), as the single identity c(E tensor L) = T_{r,c_1(L)}(c(E)) of total Chow cohomology classes, under the source's hypotheses and no others. It is Equation (02UE) in each degree i by Stacks.Chow.TotalChowClass.totalChern_sheafTensor_degree”.

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

**`Stacks.Chow.chernCapFamily_tensorObj_eq_binomialTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassTwist.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassTwist.lean#L487). The attribute's comment: “the two relations of Stacks 02U6 are hypotheses, hrelEL being the one already transported along the comparison of projective bundles of Stacks 02NC, and so is their uniqueness (the injectivity half of Stacks 02TX); the conclusion is the identity capped with an arbitrary cycle, the source's identity in the ring A^*(X) being unstateable here (there is no multiplication on bivariant classes) and the source itself reducing it to this form by Stacks 02UC. Carried besides: hcomm (commutativity of the two first Chern class cap operators on the bundle, Stacks 02UA), hpull (flat pullback carries c_1(L) to c_1(pi^*L), Stacks 02SS and 02RD), h0 (the zeroth cap products of E and of E tensor L both being the class of alpha, Stacks 02U5 (1) at j = 0), the Stacks 02U0 data chernE and chernEL, the rank of E tensor L, and Stacks 02TI for c_1(L) as hfac”.

> **Stacks 02UD.** Let `ℰ` be a finite locally free `𝒪_X`-module of rank `r`, let `ℒ` be
> invertible and let `α` be an `n`-cycle on `X`. Then for every `m ≤ r`
>
>   `c_m(ℰ ⊗ ℒ) ∩ α = ∑_{j=0}^{m} binom(r - m + j, j) c₁(ℒ)^j ∩ (c_{m-j}(ℰ) ∩ α)`
>
> in `A_{n-m}(X)`, the right-hand side being the binomial transform of the Chern class cap products
> of `ℰ` along `c₁(ℒ) ∩ -`.
>
> The relation of Stacks 02U6 on the projective bundle of `ℰ` is carried for `ℰ` and, transported
> along the comparison `𝐏(ℰ) ≅ 𝐏(ℰ ⊗ ℒ)` of Stacks 02NC, for `ℰ ⊗ ℒ`; so is its uniqueness, which
> is the injectivity half of Stacks 02TX. See the module documentation.

```lean
theorem chernCapFamily_tensorObj_eq_binomialTransform (twist twistL : ChernCapOperator C sP)
    (n : ℤ) (E L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (hrankE : PullbackPreservesRank E r)
    (hrankEL : PullbackPreservesRank (Scheme.Modules.tensorObjRingedSpace X E L) r)
    (chernE chernEL : ChernClassCycleRule C r) (hfac : InvertibleChernCapDescends C sX L)
    (α : CycleGroup C sX n)
    (hcomm : ∀ i,
      (ChernCapOperator.towerStep C sP twist (bundleRelationDegree r n) (i + 1)).comp
          (ChernCapOperator.towerStep C sP twistL (bundleRelationDegree r n) i) =
        (ChernCapOperator.towerStep C sP twistL (bundleRelationDegree r n) (i + 1)).comp
          (ChernCapOperator.towerStep C sP twist (bundleRelationDegree r n) i))
    (hpull : ∀ i,
      (projectiveBundleTowerPullback C sX sP π hsP r hπ hfacπ n (i + 1)).comp
          (firstChernCapStep C sX n L hfac i) =
        (ChernCapOperator.towerStep C sP twistL (bundleRelationDegree r n) i).comp
          (projectiveBundleTowerPullback C sX sP π hsP r hπ hfacπ n i))
    (h0 : chernCapFamily C sX n (Scheme.Modules.tensorObjRingedSpace X E L) r hrankEL chernEL α 0 =
      chernCapFamily C sX n E r hrankE chernE α 0)
    (hrelE : alternatingTowerSum
      (ChernCapOperator.towerStep C sP twist (bundleRelationDegree r n)) r
      (towerPullback (projectiveBundleTowerPullback C sX sP π hsP r hπ hfacπ n)
        (chernCapFamily C sX n E r hrankE chernE α)) = 0)
    (hrelEL : alternatingTowerSum
      (fun j => ChernCapOperator.towerStep C sP twist (bundleRelationDegree r n) j +
        ChernCapOperator.towerStep C sP twistL (bundleRelationDegree r n) j) r
      (towerPullback (projectiveBundleTowerPullback C sX sP π hsP r hπ hfacπ n)
        (chernCapFamily C sX n (Scheme.Modules.tensorObjRingedSpace X E L) r hrankEL
          chernEL α)) = 0)
    (huniq : ∀ d : (∀ j : ℕ, chowGroup C sX (n - (j : ℤ))), d 0 = 0 →
      alternatingTowerSum
          (fun j => ChernCapOperator.towerStep C sP twist (bundleRelationDegree r n) j +
            ChernCapOperator.towerStep C sP twistL (bundleRelationDegree r n) j) r
          (towerPullback (projectiveBundleTowerPullback C sX sP π hsP r hπ hfacπ n) d) = 0 →
        ∀ m ≤ r, d m = 0)
    {m : ℕ} (hm : m ≤ r) :
    chernCapFamily C sX n (Scheme.Modules.tensorObjRingedSpace X E L) r hrankEL chernEL α m =
      binomialTransform (firstChernCapStep C sX n L hfac) r
        (chernCapFamily C sX n E r hrankE chernE α) m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.39, Tag 02UB](https://stacks.math.columbia.edu/tag/02UB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
