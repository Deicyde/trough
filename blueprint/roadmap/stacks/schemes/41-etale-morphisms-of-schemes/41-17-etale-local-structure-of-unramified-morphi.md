---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_etaleNeighborhood_isClosedImmersion_opens_of_unramifiedAt, AlgebraicGeometry.exists_etaleNeighborhood_disjoint_closed_decomposition_of_unramifiedAt, AlgebraicGeometry.exists_etaleNeighborhood_disjoint_closed_decomposition_of_finite_unramified
statement: formalized
proof: formalized
---

# 41.17 Étale local structure of unramified morphisms

Section 41.17 of the Stacks Project, [Tag 04HG](https://stacks.math.columbia.edu/tag/04HG). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04HH, a lemma

[Tag 04HH](https://stacks.math.columbia.edu/tag/04HH) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_isClosedImmersion_opens_of_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/ClosedImmersionOpens.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/ClosedImmersionOpens.lean#L126).

> **Stacks Project, Tag 04HH.** After a single étale base change, finitely many distinct points
> of one fibre at which a morphism of schemes is unramified are covered, in that fibre, by open
> subschemes which are closed immersions over the new base, pass through the distinguished point,
> and pairwise avoid one another there.

```lean
public theorem exists_etaleNeighborhood_isClosedImmersion_opens_of_unramifiedAt
    {X S : Scheme.{u}} (f : X ⟶ S) (n : ℕ) (x : Fin n → X) (s : S)
    (hx : ∀ i, f (x i) = s) (hx_injective : Function.Injective x)
    (hunramified : ∀ i, UnramifiedAt f (x i)) :
    ∃ (U : EtaleNeighborhood S s) (m : Fin n → ℕ)
      (V : (Σ i, Fin (m i)) → (pullback f U.toBase).Opens),
      (∀ a, IsClosedImmersion ((V a).ι ≫ pullback.snd f U.toBase) ∧
        ∃ y : (pullback f U.toBase : Scheme.{u}),
          y ∈ V a ∧ (pullback.snd f U.toBase) y = U.point) ∧
      (∀ a b, a ≠ b → ∀ y : (pullback f U.toBase : Scheme.{u}),
        y ∈ V a → y ∈ V b → (pullback.snd f U.toBase) y ≠ U.point) ∧
      (∀ (i : Fin n) (y : (pullback f U.toBase : Scheme.{u})),
        (pullback.snd f U.toBase) y = U.point →
        (pullback.fst f U.toBase) y = x i →
        ∃ j : Fin (m i), y ∈ V ⟨i, j⟩)
```

## Tag 04HI, a lemma

[Tag 04HI](https://stacks.math.columbia.edu/tag/04HI) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_disjoint_closed_decomposition_of_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/DisjointDecomposition.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/DisjointDecomposition.lean#L66).

> **Stacks Project, Tag 04HI.** A separated morphism of schemes which is unramified at finitely
> many points of one fibre becomes, after a single étale base change around the image point, the
> disjoint union of finitely many closed subschemes of the new base passing through the
> distinguished point and a remainder whose distinguished fibre avoids the chosen points. The
> remainder has empty distinguished fibre when the chosen points exhaust the original fibre.

```lean
public theorem exists_etaleNeighborhood_disjoint_closed_decomposition_of_unramifiedAt
    {X S : Scheme.{u}} (f : X ⟶ S) [IsSeparated f] (n : ℕ) (x : Fin n → X) (s : S)
    (hx : ∀ i, f (x i) = s) (hunramified : ∀ i, UnramifiedAt f (x i)) :
    ∃ (U : EtaleNeighborhood S s)
      (W : (pullback f U.toBase).Opens) (m : Fin n → ℕ)
      (V : (Σ i, Fin (m i)) → (pullback f U.toBase).Opens),
      (sSup (Set.range V) ⊔ W = ⊤) ∧
        (Pairwise (Disjoint on V)) ∧
        (∀ a, Disjoint (V a) W) ∧
        (∀ a, IsClosedImmersion ((V a).ι ≫ pullback.snd f U.toBase)) ∧
        (∀ a, ∃ z : (V a).toScheme,
          ((V a).ι ≫ pullback.snd f U.toBase) z = U.point) ∧
        (∀ (z : (W.ι ≫ pullback.snd f U.toBase).fiber U.point) (i : Fin n),
          ((W.ι ≫ pullback.snd f U.toBase).fiberι U.point ≫ W.ι ≫
            pullback.fst f U.toBase) z ≠ x i) ∧
    ((∀ y : X, f y = s → ∃ i, y = x i) →
          IsEmpty ((W.ι ≫ pullback.snd f U.toBase).fiber U.point))
```

## Tag 04HJ, a lemma

[Tag 04HJ](https://stacks.math.columbia.edu/tag/04HJ) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_disjoint_closed_decomposition_of_finite_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/DisjointDecomposition.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/EtaleLocalStructure/DisjointDecomposition.lean#L271).

> **Stacks Project, Tag 04HJ.** A finite unramified morphism of schemes becomes a finite
> disjoint union of closed immersions after an étale base change around any chosen point of the
> target.

```lean
public theorem exists_etaleNeighborhood_disjoint_closed_decomposition_of_finite_unramified
    {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f] [Unramified f] (s : S) :
    ∃ (U : EtaleNeighborhood S s) (n : ℕ) (V : Fin n → (pullback f U.toBase).Opens),
      (sSup (Set.range V) = ⊤) ∧
        (Pairwise (Disjoint on V)) ∧
        (∀ j, IsClosedImmersion ((V j).ι ≫ pullback.snd f U.toBase))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.17, Tag 04HG](https://stacks.math.columbia.edu/tag/04HG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
