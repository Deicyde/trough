---
declaration: theorem
origin: cited
lean: TauCeti.Compactification.exists_forall_nonempty_hom
statement: formalized
proof: formalized
---

# TauCeti.Compactification.exists_forall_nonempty_hom

Every nonempty finite family of compactifications has a dense common refinement.

```lean
TauCeti.Compactification.exists_forall_nonempty_hom.{u, u_1} {X S : AlgebraicGeometry.Scheme}
  {f : X ⟶ S} {ι : Type u_1} [Finite ι] [Nonempty ι] (C : ι → TauCeti.Compactification f) :
  ∃ E, ∀ (i : ι), Nonempty (E.obj ⟶ C i)
```

## Depends on

- [TauCeti.Compactification](tauceti-compactification.md)
- [TauCeti.DenseCompactification](tauceti-densecompactification.md)

## Proof depends on

- [TauCeti.Compactification.commonRefinement](tauceti-compactification-commonrefinement.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Compactification.exists_forall_nonempty_hom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.Compactification.exists_forall_nonempty_hom).

## Sources

- [Tau Ceti documentation: `TauCeti.Compactification.exists_forall_nonempty_hom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.Compactification.exists_forall_nonempty_hom)
- [Source of `TauCeti.Compactification.exists_forall_nonempty_hom` in TauCeti/AlgebraicGeometry/Compactification/Refinement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Compactification/Refinement.lean#L185)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
