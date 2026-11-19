---
declaration: theorem
origin: cited
lean: FirstOrder.Language.nonempty_equiv_graphExpansion_iff
statement: formalized
proof: formalized
---

# FirstOrder.Language.nonempty_equiv_graphExpansion_iff

Two structures are isomorphic exactly when their graph expansions are: an `L`-isomorphism
preserves the graph of every function symbol, and a bijection preserving these graphs commutes
with the function symbols.

```lean
FirstOrder.Language.nonempty_equiv_graphExpansion_iff.{u, v, w, w'} {L : FirstOrder.Language}
  {M : Type w} [L.Structure M] {N : Type w'} [L.Structure N] :
  Nonempty (L.graphLanguage.Equiv M N) ↔ Nonempty (L.Equiv M N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.nonempty_equiv_graphExpansion_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/GraphTranslation/Language.html#FirstOrder.Language.nonempty_equiv_graphExpansion_iff).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.nonempty_equiv_graphExpansion_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/GraphTranslation/Language.html#FirstOrder.Language.nonempty_equiv_graphExpansion_iff)
- [Source of `FirstOrder.Language.nonempty_equiv_graphExpansion_iff` in TauCeti/ModelTheory/Infinitary/GraphTranslation/Language.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Infinitary/GraphTranslation/Language.lean#L251)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
