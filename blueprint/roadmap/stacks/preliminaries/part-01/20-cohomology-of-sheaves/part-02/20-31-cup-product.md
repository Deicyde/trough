---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedGlobalCupProduct.globalCupProduct, Stacks.Cohomology.DerivedGlobalCupProduct.cupPairing, Stacks.Cohomology.DerivedGlobalCupProduct.section_cupProduct, Stacks.Cohomology.DerivedRelativeCupProduct.homEquiv_symm_relativeCupProduct, Stacks.Cohomology.DerivedRelativeCupProduct.homEquiv_symm_comp_relativeCupProduct, Stacks.Cohomology.DerivedGlobalCupProduct.cupWithClassCanonical, Stacks.Cohomology.DerivedGlobalCupProduct.homologyFromSingle_cupWithClassCanonical, Stacks.Cohomology.DerivedGlobalCupProduct.homologyFromSingle_cupWithClassCanonical_cupPairing
statement: formalized
proof: formalized
---

# 20.31 Cup product

Section 20.31 of the Stacks Project, [Tag 0FKU](https://stacks.math.columbia.edu/tag/0FKU). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FKU, the section

[Tag 0FKU](https://stacks.math.columbia.edu/tag/0FKU) in the Stacks Project.

**`Stacks.Cohomology.DerivedGlobalCupProduct.globalCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProduct.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProduct.lean#L216). The attribute's comment: “the global cup product μ : RΓ(X, K) ⊗^L\_A RΓ(X, M) ⟶ RΓ(X, K ⊗^L M) in D(A), the first display of the section, built as the relative cup product of Tag 0B68 for the morphism to the one-point space with ring A; the one-point comparison itself (a left adjoint of RΓ(X, -) together with its tensor comparison) is the parameter `OnePointComparison`”.

> The global cup product `μ : RΓ(S, K) ⊗^𝐋_A RΓ(S, M) ⟶ RΓ(S, K ⊗^𝐋_{𝒪_S} M)` in `D(A)` for
> `A = Γ(S, 𝒪_S)`, as a morphism of bifunctors on `D(𝒪_S) × D(𝒪_S)`: the relative cup product
> construction for the adjunction `L ⊣ RΓ(S, -)` and the tensor comparison of `c`.

```lean
def globalCupProduct (c : OnePointComparison S) : GlobalCupProduct S
```

**`Stacks.Cohomology.DerivedGlobalCupProduct.cupPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProduct.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProduct.lean#L275). The attribute's comment: “the induced pairings ∪ : H^i(X, K) × H^j(X, M) ⟶ H^\{i+j}(X, K ⊗^L M), the second display of the section: the tensoring of classes of More on Algebra, Section 15.64 followed by H^\{i+j}(μ); the global cup product μ is the parameter κ, which `globalCupProduct` produces from an `OnePointComparison`”.

> The pairings `∪ : Hⁱ(S, K) ⊗_A Hʲ(S, M) ⟶ Hⁱ⁺ʲ(S, K ⊗^𝐋_{𝒪_S} M)` induced by a global cup
> product `κ`: a class `ξ ∈ Hⁱ(S, K)` and a class `η ∈ Hʲ(S, M)` are tensored to a class `ξ ⊗ η` in
> `Hⁱ⁺ʲ(RΓ(S, K) ⊗^𝐋_A RΓ(S, M))`, and `ξ ∪ η = κ(ξ ⊗ η)`.

```lean
def cupPairing (κ : GlobalCupProduct S)
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing S))) (i j : ℤ) :
    cohomologyModule K i ⊗ cohomologyModule M j ⟶
      cohomologyModule (((derivedTensorProductFunctor S.sheaf).obj K).obj M) (i + j)
```

**`Stacks.Cohomology.DerivedGlobalCupProduct.section_cupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductSection.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductSection.lean#L86). The attribute's comment: “Section 20.31 IN FULL, both displays: the global cup product μ : RΓ(X, K) ⊗^L\_A RΓ(X, M) ⟶ RΓ(X, K ⊗^L M) in D(A), CONSTRUCTED as the relative cup product of Tag 0B68 for the morphism to the one-point space with ring A (first conjunct), natural in both complexes jointly (second conjunct), and the pairings it induces, ∪ : H^i(X, K) × H^j(X, M) ⟶ H^\{i+j}(X, K ⊗^L M), given by the source's two-step recipe ξ ∪ η = μ(ξ ⊗ η) with the tensoring step the pairing of classes of More on Algebra, Section 15.64 (third conjunct). The numbered items of the section are excluded, each having its own tag: 0FP2, 0G6W, 0FP3, 0FKV, 0FP4, 0FP5, 0FP6, 0H99. The one parameter is `OnePointComparison`, the identification D(pt, A) = D(A) that the source has and this repository does not”.

> **Cohomology, Section 0FKU in full: both displays of the section, for the global cup product
> built from a one-point comparison.**
>
> The conjuncts are, in the order the source states them:
>
> * the first display, `μ : RΓ(S, K) ⊗^𝐋_A RΓ(S, M) ⟶ RΓ(S, K ⊗^𝐋_{𝒪_S} M)`, together with the
>   source's *definition* of it — it is the relative cup product of Tag 0B68, namely the adjoint
>   transpose of the tensor comparison followed by the counit of `L ⊣ RΓ(S, -)` in both tensor
>   factors, which is what "we define it as the relative cup product for the morphism of ringed
>   spaces `f : (S, 𝒪_S) ⟶ (pt, A)` via `D(pt, A) = D(A)`" says once `Rf_*` is read as `RΓ(S, -)`;
> * that `μ` is natural in the two complexes jointly, so that it is a morphism of bifunctors on
>   `D(𝒪_S) × D(𝒪_S)` and not a separate map for each pair;
> * the second display, the induced pairings
>   `∪ : Hⁱ(S, K) ⊗_A Hʲ(S, M) ⟶ Hⁱ⁺ʲ(S, K ⊗^𝐋_{𝒪_S} M)`, together with the source's two-step
>   recipe `ξ ∪ η = μ(ξ ⊗ η)`: the tensoring step is a
>   `RingTheory.TorProducts.CohomologyTensorProduct`, i.e. a pairing sending the tensor of the
>   classes of two cocycles to the class of their tensor, which is Equation 15.64.0.1 of Tag 068H
>   and is the source's "we can first tensor them, see More on Algebra, Section 15.64"; the second
>   step is `Hⁱ⁺ʲ(μ)`.
>
> The one-point comparison `c` is the parameter discussed in the module docstring: it stands for the
> identification `D(pt, A) = D(A)`, which the source has and this repository does not. It is a
> hypothesis of the two definitions this theorem is about, so this statement is exactly as
> conditional as they are and no more.
>
> The remaining numbered items of Section 20.31 are not conjoined here because each carries its own
> tag: Lemma 20.31.1 is Tag 0FP2, Remark 20.31.2 is Tag 0G6W, Lemma 20.31.3 is Tag 0FP3, Lemma
> 20.31.4 is Tag 0FKV, and Lemmas 20.31.5 to 20.31.8 are Tags 0FP4, 0FP5, 0FP6 and 0H99. What is
> left to Tag 0FKU itself is the construction of the two displays, which is what this states.

```lean
theorem section_cupProduct (c : OnePointComparison S) :
    (∀ K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing S)),
      (globalCupProduct c).app (K, M) =
        adjunctionBitensorMap c.adjunction (Functor.uncurry.obj (tensorBase S))
          (Functor.uncurry.obj (derivedTensorProductFunctor S.sheaf)) c.tensorComparison K M) ∧
    (∀ K K' M M' : DerivedCategory (SheafOfModules.{u} (structureSheafRing S)),
      ∀ (k : K ⟶ K') (m : M ⟶ M'),
      (Functor.uncurry.obj (tensorBase S)).map
            ((baseSections S).map k ×ₘ (baseSections S).map m) ≫
          (globalCupProduct c).app (K', M') =
        (globalCupProduct c).app (K, M) ≫
          (baseSections S).map
            ((Functor.uncurry.obj (derivedTensorProductFunctor S.sheaf)).map (k ×ₘ m))) ∧
    (∀ (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing S))) (i j : ℤ),
      ∃ p : RingTheory.TorProducts.CohomologyTensorProduct ((baseSections S).obj K)
          ((baseSections S).obj M) i j,
        cupPairing (globalCupProduct c) K M i j =
          p.map ≫ (DerivedCategory.homologyFunctor (ModuleCat.{u} (baseRing S)) (i + j)).map
            ((globalCupProduct c).app (K, M)))
```

## Tag 0FP2, a lemma

[Tag 0FP2](https://stacks.math.columbia.edu/tag/0FP2) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.homEquiv_symm_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductOfCohomologyClasses.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductOfCohomologyClasses.lean#L159). The attribute's comment: “the identification-free core, at arbitrary objects of `D(𝒪_Y)` in place of the source's shifted structure sheaves, and for an arbitrary morphism of ringed spaces”.

> The two constructions of the cup product agree: the adjunct of the tensor product `ξ ⊗ η` of
> two cohomology classes followed by the relative cup product of Stacks 0B68 is the derived
> pullback-tensor comparison of Stacks 079U followed by the tensor product `ξ̃ ⊗ η̃` of their
> adjuncts.

```lean
theorem homEquiv_symm_relativeCupProduct
    {U V : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))}
    {K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (ξ : U ⟶ (derivedPushforward f).obj K) (η : V ⟶ (derivedPushforward f).obj M) :
    ((derivedAdjunction f).homEquiv _ _).symm
        (((derivedTensorProductFunctor Y.sheaf).map ξ).app V ≫
          ((derivedTensorProductFunctor Y.sheaf).obj
              ((derivedPushforward f).obj K)).map η ≫
            relativeCupProduct f K M) =
      (pullbackTensorComparison f).app (U, V) ≫
        ((derivedTensorProductFunctor X.sheaf).map
              (((derivedAdjunction f).homEquiv U K).symm ξ)).app
            ((derivedPullback f).obj V) ≫
          ((derivedTensorProductFunctor X.sheaf).obj K).map
            (((derivedAdjunction f).homEquiv V M).symm η)
```

**`Stacks.Cohomology.DerivedRelativeCupProduct.homEquiv_symm_comp_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductOfCohomologyClasses.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductOfCohomologyClasses.lean#L183). The attribute's comment: “stated for an arbitrary morphism of ringed spaces, with the source's identification `𝒪_Y[-i-j] = 𝒪_Y[-i] ⊗ᴸ 𝒪_Y[-j]` carried as an arbitrary morphism `χ`”.

> Let `χ : W ⟶ U ⊗^L_{𝒪_Y} V`. The adjunct of `χ` followed by `ξ ⊗ η` and the relative cup
> product of Stacks 0B68 is `Lf^*χ` followed by the derived pullback-tensor comparison of
> Stacks 079U and by the tensor product `ξ̃ ⊗ η̃` of the adjuncts.

```lean
theorem homEquiv_symm_comp_relativeCupProduct
    {W U V : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))}
    {K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (χ : W ⟶ ((derivedTensorProductFunctor Y.sheaf).obj U).obj V)
    (ξ : U ⟶ (derivedPushforward f).obj K) (η : V ⟶ (derivedPushforward f).obj M) :
    ((derivedAdjunction f).homEquiv _ _).symm
        (χ ≫ ((derivedTensorProductFunctor Y.sheaf).map ξ).app V ≫
          ((derivedTensorProductFunctor Y.sheaf).obj
              ((derivedPushforward f).obj K)).map η ≫
            relativeCupProduct f K M) =
      (derivedPullback f).map χ ≫ (pullbackTensorComparison f).app (U, V) ≫
        ((derivedTensorProductFunctor X.sheaf).map
              (((derivedAdjunction f).homEquiv U K).symm ξ)).app
            ((derivedPullback f).obj V) ≫
          ((derivedTensorProductFunctor X.sheaf).obj K).map
            (((derivedAdjunction f).homEquiv V M).symm η)
```

## Tag 0G6W, a remark

[Tag 0G6W](https://stacks.math.columbia.edu/tag/0G6W) in the Stacks Project.

**`Stacks.Cohomology.DerivedGlobalCupProduct.cupWithClassCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L106). The attribute's comment: “the construction of the map ξ ∪ - : RΓ(X, M)[-i] ⟶ RΓ(X, K ⊗^L M) attached to a class ξ ∈ H^i(X, K), the first clause of the remark, at the global cup product μ of Section 0FKU, `globalCupProductCanonical`, on an arbitrary ringed space”.

> **The map `ξ ∪ -` at the canonical global cup product.** For a class `ξ ∈ Hⁱ(X, K)` it is the
> morphism
>
> `ξ ∪ - : RΓ(X, M)[-i] ⟶ RΓ(X, K ⊗^𝐋_{𝒪_X} M)`
>
> in `D(A)` for `A = Γ(X, 𝒪_X)`, namely the composition of the identification
> `RΓ(X, M)[-i] = A[-i] ⊗^𝐋_A RΓ(X, M)`, of `ξ ⊗ 1` for the morphism representing `ξ`, and of the
> global cup product `μ` of Section 0FKU, `globalCupProductCanonical`.

```lean
def cupWithClassCanonical (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (i : ℤ) (ξ : ModuleCat.of (baseRing X) (baseRing X) ⟶ cohomologyModule K i) :
    ((baseSections X).obj M)⟦-i⟧ ⟶
      (baseSections X).obj (((derivedTensorProductFunctor X.sheaf).obj K).obj M)
```

**`Stacks.Cohomology.DerivedGlobalCupProduct.homologyFromSingle_cupWithClassCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L127). The attribute's comment: “the second clause of the remark: on cohomology ξ ∪ - is the cup product with ξ, for the global cup product `globalCupProductCanonical`. The cup product of two classes is in the composition shape of Section 0FKU and Tag 0FP2, A[-i-j] ⟶ A[-i] ⊗ᴸ A[-j] ⟶ RΓ(X, K) ⊗ᴸ RΓ(X, M) ⟶ RΓ(X, K ⊗ᴸ M), for every identification χ of A[-i-j] with A[-i] ⊗ᴸ A[-j]”.

> On cohomology the map `ξ ∪ -` at the canonical global cup product is the cup product with `ξ`:
> for `ξ ∈ Hⁱ(X, K)` and `η ∈ Hʲ(X, M)`, the map `Hⁱ⁺ʲ(ξ ∪ -)` carries the class of `η`, read in
> `Hⁱ⁺ʲ(RΓ(X, M)[-i])` through the identifications `A[-i-j] = A[-i] ⊗^𝐋_A A[-j]` and
> `A[-i] ⊗^𝐋_A RΓ(X, M) = RΓ(X, M)[-i]`, to the class of the cup product `ξ ∪ η` in the composition
> shape of Section 0FKU and Tag 0FP2.

```lean
theorem homologyFromSingle_cupWithClassCanonical
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) (i j : ℤ)
    (ξ : ModuleCat.of (baseRing X) (baseRing X) ⟶ cohomologyModule K i)
    (η : ModuleCat.of (baseRing X) (baseRing X) ⟶ cohomologyModule M j)
    (χ : baseShift X (i + j) ⟶ ((tensorBase X).obj (baseShift X i)).obj (baseShift X j)) :
    DerivedCategory.homologyFromSingleLinearEquiv (ModuleCat.of (baseRing X) (baseRing X))
          (((baseSections X).obj M)⟦-i⟧) (i + j) (baseRing X)
          (χ ≫ ((tensorBase X).obj (baseShift X i)).map (classRepresentative M j η) ≫
            (baseShiftTensorIso X i ((baseSections X).obj M)).hom) ≫
        (DerivedCategory.homologyFunctor (ModuleCat.{u} (baseRing X)) (i + j)).map
          (cupWithClassCanonical X K M i ξ) =
      DerivedCategory.homologyFromSingleLinearEquiv (ModuleCat.of (baseRing X) (baseRing X))
        ((baseSections X).obj (((derivedTensorProductFunctor X.sheaf).obj K).obj M)) (i + j)
        (baseRing X)
        (χ ≫ ((tensorBase X).map (classRepresentative K i ξ)).app (baseShift X j) ≫
          ((tensorBase X).obj ((baseSections X).obj K)).map (classRepresentative M j η) ≫
            (globalCupProductCanonical X).app (K, M))
```

**`Stacks.Cohomology.DerivedGlobalCupProduct.homologyFromSingle_cupWithClassCanonical_cupPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L155). The attribute's comment: “the second clause of the remark, with the cup product of two classes read against the cohomology-level pairing `cupPairing` of Section 0FKU at the global cup product `globalCupProductCanonical`: the tensoring of classes of Tag 068H followed by H^\{i+j}(μ), which is how the source defines ∪. The source's identification A[-i-j] = A[-i] ⊗ᴸ A[-j] is `pinnedSplitting`”.

> On cohomology, `Hⁱ⁺ʲ(ξ ∪ -)` at the canonical global cup product carries the class of `η` to
> `ξ ∪ η` as `Stacks.Cohomology.DerivedGlobalCupProduct.cupPairing` defines it for the canonical
> global cup product, the source's identification `A[-i-j] = A[-i] ⊗^𝐋_A A[-j]` being
> `pinnedSplitting`.

```lean
theorem homologyFromSingle_cupWithClassCanonical_cupPairing
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) (i j : ℤ)
    (ξ : ModuleCat.of (baseRing X) (baseRing X) ⟶ cohomologyModule K i)
    (η : ModuleCat.of (baseRing X) (baseRing X) ⟶ cohomologyModule M j) :
    DerivedCategory.homologyFromSingleLinearEquiv (ModuleCat.of (baseRing X) (baseRing X))
          (((baseSections X).obj M)⟦-i⟧) (i + j) (baseRing X)
          (pinnedSplitting X i j ≫
            ((tensorBase X).obj (baseShift X i)).map (classRepresentative M j η) ≫
              (baseShiftTensorIso X i ((baseSections X).obj M)).hom) ≫
        (DerivedCategory.homologyFunctor (ModuleCat.{u} (baseRing X)) (i + j)).map
          (cupWithClassCanonical X K M i ξ) =
      (λ_ (ModuleCat.of (baseRing X) (baseRing X))).inv ≫ (ξ ⊗ₘ η) ≫
        cupPairing (globalCupProductCanonical X) K M i j
```

## Tag 0FP3, a lemma

[Tag 0FP3](https://stacks.math.columbia.edu/tag/0FP3) in the Stacks Project.

**`Stacks.Cohomology.CupProductAndDerivedPushforwardOnRingedSpaces.naiveCupProduct_relativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductAndDerivedPushforward.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CupProductAndDerivedPushforward.lean#L400).

> **Stacks 0FP3.**  For a morphism of ringed spaces `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and complexes
> `𝒦^•`, `ℳ^•` of `𝒪_X`-modules, the hexagon
>
> ```
> f_*𝒦^• ⊗^L_{𝒪_Y} f_*ℳ^• ─────→ Rf_*𝒦^• ⊗^L_{𝒪_Y} Rf_*ℳ^•
>           │                                │
>           ↓                                ↓
> Tot(f_*𝒦^• ⊗_{𝒪_Y} f_*ℳ^•)        Rf_*(𝒦^• ⊗^L_{𝒪_X} ℳ^•)
>           │                                │
>           ↓                                ↓
> f_*Tot(𝒦^• ⊗_{𝒪_X} ℳ^•) ─────→ Rf_*Tot(𝒦^• ⊗_{𝒪_X} ℳ^•)
> ```
>
> commutes in `D(𝒪_Y)`.  Its horizontal edges and its top right edge are the comparison
> `f_* ⟶ Rf_*`; the top left and bottom right edges are the canonical map from the derived
> tensor product to the ordinary total tensor complex of Stacks 06YU; the middle left edge is
> the naive cup product and the middle right edge is the relative cup product of Stacks 0B68.

```lean
theorem naiveCupProduct_relativeCupProduct :
    (derivedToTensorNatTrans Y).app
          ((pushforwardComplex f).obj K, (pushforwardComplex f).obj M) ≫
        DerivedCategory.Q.map (naiveCupProduct f K M) ≫
        pushforwardComparisonQ f ((totalComplexPair (sheafTensor X.sheaf)).obj (K, M)) =
      (Functor.uncurry.obj (derivedTensorProductFunctor Y.sheaf)).map
          (pushforwardComparisonQ f K ×ₘ pushforwardComparisonQ f M) ≫
        relativeCupProduct f (DerivedCategory.Q.obj K) (DerivedCategory.Q.obj M) ≫
        (derivedPushforward f).map ((derivedToTensorNatTrans X).app (K, M))
```

## Tag 0FKV, a lemma

[Tag 0FKV](https://stacks.math.columbia.edu/tag/0FKV) in the Stacks Project.

**`Stacks.Cech.CupProductSquare.cupProductSquareCommutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/CupProductSquareCommutes.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/CupProductSquareCommutes.lean#L279).

> **[Stacks, Tag 0FKV].**  Let `(X, 𝒪_X)` be a ringed space, `A = Γ(X, 𝒪_X)`, `𝒦^•` and `ℳ^•`
> bounded below complexes of `𝒪_X`-modules and `𝒰 : X = ⋃ Uᵢ` an open covering.  The diagram
>
> ```
> Tot(Č(𝒰,𝒦)) ⊗^𝐋_A Tot(Č(𝒰,ℳ)) ─────────→ RΓ(X,𝒦) ⊗^𝐋_A RΓ(X,ℳ)
>             │                                        │ μ
>             ↓                                        ↓
> Tot(Tot(Č(𝒰,𝒦)) ⊗_A Tot(Č(𝒰,ℳ)))          RΓ(X, 𝒦 ⊗^𝐋_{𝒪_X} ℳ)
>             │                                        │
>             ↓                                        ↓
> Tot(Č(𝒰, Tot(𝒦 ⊗_{𝒪_X} ℳ))) ─────────────→ RΓ(X, Tot(𝒦 ⊗_{𝒪_X} ℳ))
> ```
>
> commutes in `D(A)`: the left-hand leg `cechLeftLeg` (the canonical map to the total tensor
> complex, then the Čech cup product of [Stacks, Tag 07MB], then the comparison of
> [Stacks, Tag 08BN]) equals the right-hand leg `cechRightLeg` (the comparison of Tag 08BN in both
> factors, then the global cup product `μ`, then `RΓ(X, -)` of the canonical map
> `𝒦^• ⊗^𝐋 ℳ^• ⟶ Tot(𝒦^• ⊗ ℳ^•)`).

```lean
theorem cupProductSquareCommutes :
    cechLeftLeg S Ui hU K M = cechRightLeg S Ui hU K M
```

## Tag 0FP4, a lemma

[Tag 0FP4](https://stacks.math.columbia.edu/tag/0FP4) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductAssociativity.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductAssociativity.lean#L343). The attribute's comment: “associativity of the relative cup product, for a morphism of ringed spaces and arbitrary K, L, M in D(O\_X): the associativity constraints are those of Tag 0FPB (derivedAssociator), and their compatibility with the comparison of Tag 079U is pullbackTensorComparisonAssociative”.

> **The relative cup product is associative.**  For a morphism of ringed spaces
> `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and arbitrary `K, L, M ∈ D(𝒪_X)` the square
>
> ```
> (Rf_*K ⊗^L Rf_*L) ⊗^L Rf_*M ⟶ Rf_*(K ⊗^L L) ⊗^L Rf_*M ⟶ Rf_*((K ⊗^L L) ⊗^L M)
>             |                                                      |
>             | a                                                    | Rf_*a
>             v                                                      v
> Rf_*K ⊗^L (Rf_*L ⊗^L Rf_*M) ⟶ Rf_*K ⊗^L Rf_*(L ⊗^L M) ⟶ Rf_*(K ⊗^L (L ⊗^L M))
> ```
>
> commutes in `D(𝒪_Y)`, where the four unlabelled arrows are relative cup products of Stacks 0B68
> in one or the other tensor factor and `a` is the associativity constraint of Stacks 0FPB.  The
> compatibility of the comparison of Stacks 079U with those constraints is
> `pullbackTensorComparisonAssociative`.

```lean
theorem relativeCupProduct_assoc
    (K L M : DerivedCategory (Mod X.sheaf)) :
    (Functor.uncurry.obj
            (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf)).map
        (relativeCupProduct f K L ×ₘ 𝟙 ((derivedPushforward f).obj M)) ≫
        relativeCupProduct f
            ((Functor.uncurry.obj
              (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf)).obj (K, L))
            M ≫
          (derivedPushforward f).map (derivedAssociator X K L M) =
      derivedAssociator Y ((derivedPushforward f).obj K) ((derivedPushforward f).obj L)
          ((derivedPushforward f).obj M) ≫
        (Functor.uncurry.obj
              (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf)).map
            (𝟙 ((derivedPushforward f).obj K) ×ₘ relativeCupProduct f L M) ≫
          relativeCupProduct f K
            ((Functor.uncurry.obj
              (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf)).obj (L, M))
```

## Tag 0FP5, a lemma

[Tag 0FP5](https://stacks.math.columbia.edu/tag/0FP5) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_braiding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductCommutativity.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductCommutativity.lean#L242). The attribute's comment: “the whole tag: for a morphism of ringed spaces and arbitrary K, L in D(𝒪\_X), the commutativity square of the relative cup product commutes. The commutativity constraints are derivedBraiding of Stacks 0FPB, and their compatibility with the Stacks 079U comparison is pullbackTensorComparisonBraided”.

> **The relative cup product is commutative.**  For a morphism of ringed spaces
> `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and arbitrary `K, L ∈ D(𝒪_X)` the square
>
> ```
> Rf_*K ⊗^L Rf_*L ⟶ Rf_*(K ⊗^L L)
>       |                  |
>       ψ                 Rf_*ψ
>       v                  v
> Rf_*L ⊗^L Rf_*K ⟶ Rf_*(L ⊗^L K)
> ```
>
> commutes in `D(𝒪_Y)`, where the horizontal arrows are the relative cup product of Stacks 0B68
> and `ψ` is the commutativity constraint of Stacks 0FPB.  The compatibility of the comparison of
> Stacks 079U with those constraints is `pullbackTensorComparisonBraided`.

```lean
theorem relativeCupProduct_braiding (K L : DerivedCategory (Mod X.sheaf)) :
    derivedBraiding Y ((derivedPushforward f).obj K) ((derivedPushforward f).obj L) ≫
        relativeCupProduct f L K =
      relativeCupProduct f K L ≫ (derivedPushforward f).map (derivedBraiding X K L)
```

## Tag 0FP6, a lemma

[Tag 0FP6](https://stacks.math.columbia.edu/tag/0FP6) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductComposition.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductComposition.lean#L228). The attribute's comment: “for the composite adjunction and the composite pullback-tensor comparison”.

> **The relative cup product is compatible with composition.**  For the composite adjunction
> `Lg^*Lf^* ⊣ Rf_*Rg_*` and the composite derived pullback-tensor comparison, the relative cup
> product of Stacks 0B68 is the relative cup product for `g` at the pair `(Rf_*K, Rf_*L)` followed
> by `Rg_*` of the relative cup product for `f`.

```lean
theorem relativeCupProduct_comp
    (K L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    adjunctionBitensorMap
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction g).comp
          (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction f))
        (Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Z.sheaf))
        (Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf))
        (pullbackTensorComparisonComp f g) K L =
      relativeCupProduct g
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K)
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj L) ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward g).map
          (relativeCupProduct f K L)
```

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_comp'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductComposition.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductComposition.lean#L275).

> **Stacks 0FP6: the relative cup product is compatible with composition.**  For composable
> morphisms of ringed spaces `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and `g : (Y, 𝒪_Y) ⟶ (Z, 𝒪_Z)` and
> arbitrary `K, L ∈ D(𝒪_X)` the square
>
> ```
> Rg_*Rf_*K ⊗^L Rg_*Rf_*L ⟶ R(g ∘ f)_*K ⊗^L R(g ∘ f)_*L
>           |                            |
>           |                            | relative cup product for f ≫ g
>           v                            v
>    Rg_*Rf_*(K ⊗^L L)     ⟶      R(g ∘ f)_*(K ⊗^L L)
> ```
>
> commutes in `D(𝒪_Z)`, where the horizontal arrows are the composition isomorphism
> `Rf_* ⋙ Rg_* ≅ R(g ∘ f)_*` of Stacks 0D5T — in each tensor factor on top and at the tensor
> product on the bottom — and the left vertical arrow is the relative cup product for `g` at
> `(Rf_*K, Rf_*L)` followed by `Rg_*` of the relative cup product for `f`.
>
> This is the statement of the source, the two identifications being the composition isomorphism.
> It is
> `relativeCupProduct_comp` transported by `adjunctionBitensorMap_transport`, whose two inputs are
> `Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_comp` and
> `Stacks.Cohomology.DerivedPullbackTensor.derivedPullbackTensorIso_comp`.

```lean
theorem relativeCupProduct_comp'
    (K L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (Functor.uncurry.obj
            (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Z.sheaf)).map
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforwardCompIso f
              g).hom.app K ×ₘ
            (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforwardCompIso f
              g).hom.app L) ≫
        relativeCupProduct (f ≫ g) K L =
      relativeCupProduct g
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K)
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj L) ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward g).map
            (relativeCupProduct f K L) ≫
          (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforwardCompIso f
              g).hom.app
            (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj K).obj
              L)
```

## Tag 0H99, a lemma

[Tag 0H99](https://stacks.math.columbia.edu/tag/0H99) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_derivedBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductBaseChange.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProductBaseChange.lean#L473).

> **Stacks 0H99: the relative cup product is compatible with a commutative square of ringed
> spaces.**
>
> For a commutative square `g' ≫ f = f' ≫ g` of ringed spaces and arbitrary `K, L ∈ D(𝒪_X)`, the
> hexagon `RelativeCupProductBaseChangeSquare` commutes at the relative cup product of Stacks 0B68
> for `f` and for `f'` and the derived base change map of Stacks 08HY: the derived pullback along
> `g` of the cup product for `f`, followed by the base change map and by `Rf'_*` of the comparison
> of Stacks 079U for `g'`, equals the comparison of Stacks 079U for `g`, followed by the base
> change map in each tensor factor and by the cup product for `f'`.
>
> There is no boundedness, flatness or quasi-coherence hypothesis on `K` and `L`, and no associator
> or symmetry of `⊗^L` is used: the hexagon has binary tensor products only.

```lean
theorem relativeCupProduct_derivedBaseChangeMap
    (K L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    RelativeCupProductBaseChangeSquare
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f)
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f')
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g)
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g')
      (Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf))
      (Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf))
      (Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y'.sheaf))
      (Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X'.sheaf))
      (Stacks.Cohomology.DerivedProjectionFormula.pullbackTensorComparison g)
      (Stacks.Cohomology.DerivedProjectionFormula.pullbackTensorComparison g') K L
      (relativeCupProduct f K L)
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj K).obj L))
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq K)
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq L)
      (relativeCupProduct f'
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g').obj K)
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g').obj L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.31, Tag 0FKU](https://stacks.math.columbia.edu/tag/0FKU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
