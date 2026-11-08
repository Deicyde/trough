---
declaration: def
origin: cited
lean: TauCeti.stdPeterWeylBasis
statement: formalized
---

# The Peter-Weyl theorem, unconditionally

The normalized matrix coefficients of the models
chosen in the unitary equivalence classes are a Hilbert basis of `L²(G)`, indexed by
`Σ i, Fin (IrrepClass.model i).dim × Fin (IrrepClass.model i).dim`. No skeleton is assumed:
`isIrrepSkeleton_model` supplies one.

`TauCeti.coe_stdPeterWeylBasis` identifies the elements of this basis with
`TauCeti.peterWeylFamily IrrepClass.model`.

```lean
TauCeti.stdPeterWeylBasis.{u_1, u_2} (𝕜 : Type u_1) (G : Type u_2) [RCLike 𝕜] [IsAlgClosed 𝕜]
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [MeasurableSpace G]
  [BorelSpace G] :
  HilbertBasis ((i : TauCeti.IrrepClass 𝕜 G) × Fin i.model.dim × Fin i.model.dim) 𝕜
    ↥(MeasureTheory.Lp 𝕜 2 (TauCeti.haarProb G))
```

## Depends on

- [The Peter-Weyl theorem](../part-02/the-peter-weyl-theorem.md)

## Proof depends on

- [Schur's lemma, scalar half](../../../representation-theory/other-results/schurs-lemma-scalar-half.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.stdPeterWeylBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/PeterWeyl.html#TauCeti.stdPeterWeylBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.stdPeterWeylBasis`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/PeterWeyl.html#TauCeti.stdPeterWeylBasis)
- [Source of `TauCeti.stdPeterWeylBasis` in TauCeti/RepresentationTheory/Compact/PeterWeyl.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Compact/PeterWeyl.lean#L706)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
