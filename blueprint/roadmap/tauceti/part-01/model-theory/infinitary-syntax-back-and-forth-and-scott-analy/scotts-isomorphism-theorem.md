---
declaration: theorem
origin: cited
lean: TauCeti.scott_isomorphism
statement: formalized
proof: formalized
---

# Scott's isomorphism theorem

In a countable language, every countable structure `M` has
an `Lω₁ω` sentence that `M` satisfies and that holds in a countable structure, in any universe,
exactly when that structure is isomorphic to `M`.

Function symbols are allowed: the sentence is the back-translation of the Scott sentence of the
graph expansion of `M`.

```lean
TauCeti.scott_isomorphism.{u, v, w, w'} {L : FirstOrder.Language}
  [Countable ((k : ℕ) × L.Functions k)] [Countable ((k : ℕ) × L.Relations k)] (M : Type w)
  [L.Structure M] [Countable M] :
  ∃ σ,
    FirstOrder.Language.SentenceInf.Realize σ M ∧
      ∀ (N : Type w') [inst : L.Structure N] [Countable N],
        FirstOrder.Language.SentenceInf.Realize σ N ↔ Nonempty (L.Equiv M N)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Proof depends on

- [FirstOrder.Language.nonempty_equiv_graphExpansion_iff](firstorder-language-nonempty-equiv-graphexpansio.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)
- [TauCeti.PotentialIso.nonempty_equiv_of_cg](tauceti-potentialiso-nonempty-equiv-of-cg.md)
- [TauCeti.realize_scottFormula_iff_bfEquiv](tauceti-realize-scottformula-iff-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.scott_isomorphism`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Isomorphism.html#TauCeti.scott_isomorphism).

## Sources

- [Tau Ceti documentation: `TauCeti.scott_isomorphism`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Isomorphism.html#TauCeti.scott_isomorphism)
- [Source of `TauCeti.scott_isomorphism` in TauCeti/ModelTheory/Scott/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Scott/Isomorphism.lean#L86)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
