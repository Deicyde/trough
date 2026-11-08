---
declaration: theorem
origin: cited
lean: TauCeti.realize_scottSentenceAt_iff
statement: formalized
proof: formalized
---

# TauCeti.realize_scottSentenceAt_iff

At a countable internally stabilizing level, the Scott sentence of a countable structure `M`
holds in a countable structure exactly when that structure is isomorphic to `M`.

```lean
TauCeti.realize_scottSentenceAt_iff.{u, v, w, w', o} {L : FirstOrder.Language} [L.IsRelational]
  [Countable ((k : ℕ) × L.Relations k)] (M : Type w) [L.Structure M] [Countable M] {α : Ordinal.{o}}
  (hα : α < Ordinal.omega 1) (hs : TauCeti.SelfStabilizesCompletely M α) (N : Type w')
  [L.Structure N] [Countable N] :
  FirstOrder.Language.SentenceInf.Realize (TauCeti.scottSentenceAt M α) N ↔ Nonempty (L.Equiv M N)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Proof depends on

- [TauCeti.PotentialIso](tauceti-potentialiso.md)
- [TauCeti.realize_scottFormula_iff_bfEquiv](tauceti-realize-scottformula-iff-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.realize_scottSentenceAt_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Isomorphism.html#TauCeti.realize_scottSentenceAt_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.realize_scottSentenceAt_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Isomorphism.html#TauCeti.realize_scottSentenceAt_iff)
- [Source of `TauCeti.realize_scottSentenceAt_iff` in TauCeti/ModelTheory/Scott/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Scott/Isomorphism.lean#L68)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
