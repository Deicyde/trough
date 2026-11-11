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
- [Source of `TauCeti.Compactification.exists_forall_nonempty_hom` in TauCeti/AlgebraicGeometry/Compactification/Refinement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Compactification/Refinement.lean#L185)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
