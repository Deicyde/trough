---
declaration: def
origin: cited
lean: TauCeti.peterWeylBasis, TauCeti.dense_representativeSubmodule
statement: formalized
---

# The Peter-Weyl theorem

For a skeleton of the unitary dual of a compact group,
the normalized matrix coefficients `√(dim V_i) · (models i)_{ab}` are a Hilbert basis of `L²(G)`,
indexed by `Σ i, Fin (models i).dim × Fin (models i).dim`.

Algebraic closedness of the scalars is Schur's lemma, and enters through the orthonormality half.

```lean
TauCeti.peterWeylBasis.{u_1, u_2, u_3} {𝕜 : Type u_1} {G : Type u_2} {ι : Type u_3} [RCLike 𝕜]
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [MeasurableSpace G]
  [BorelSpace G] [IsAlgClosed 𝕜] {models : ι → TauCeti.IrrepModel 𝕜 G}
  (h : TauCeti.IsIrrepSkeleton models) :
  HilbertBasis ((i : ι) × Fin (models i).dim × Fin (models i).dim) 𝕜
    ↥(MeasureTheory.Lp 𝕜 2 (TauCeti.haarProb G))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, scalar half](../../representation-theory/other-results/schurs-lemma-scalar-half.md)
- [The spectral theorem for a symmetric convolution operator](../../representation-theory/compact/the-spectral-theorem-for-a-symmetric-convolution.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.peterWeylBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/PeterWeyl.html#TauCeti.peterWeylBasis).

## Other forms

**The Peter-Weyl density theorem.** Formalized in Tau Ceti as [`TauCeti.dense_representativeSubmodule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/RepresentativeDensity.html#TauCeti.dense_representativeSubmodule).

```lean
TauCeti.dense_representativeSubmodule.{u_1, u_2} (𝕜 : Type u_1) (G : Type u_2) [RCLike 𝕜] [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] :
  Dense ↑(TauCeti.representativeSubmodule 𝕜 G)
```

## Sources

- [Tau Ceti documentation: `TauCeti.peterWeylBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/PeterWeyl.html#TauCeti.peterWeylBasis)
- [Source of `TauCeti.peterWeylBasis` in TauCeti/RepresentationTheory/Compact/PeterWeyl.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Compact/PeterWeyl.lean#L509)
