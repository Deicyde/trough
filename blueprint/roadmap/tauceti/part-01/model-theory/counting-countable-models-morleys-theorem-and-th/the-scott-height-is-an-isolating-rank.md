---
declaration: theorem
origin: cited
lean: TauCeti.isIsolatingRank_scottHeight
statement: formalized
proof: formalized
---

# The Scott height is an isolating rank

The Scott height of the structure decoded from a
configuration on `ℕ` is invariant under isomorphism and countable, and back-and-forth
equivalence of the empty tuples at the Scott height of `c` decides isomorphism with `c`.

```lean
TauCeti.isIsolatingRank_scottHeight.{u, v} (L : FirstOrder.Language) [L.IsRelational] :
  TauCeti.IsIsolatingRank fun c => TauCeti.scottHeight ℕ
```

## Depends on

- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)
- [TauCeti.IsIsolatingRank](tauceti-isisolatingrank.md)

## Proof depends on

- [TauCeti.PotentialIso](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-potentialiso.md)
- [TauCeti.PotentialIso.nonempty_equiv_of_cg](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-potentialiso-nonempty-equiv-of-cg.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIsolatingRank_scottHeight`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.isIsolatingRank_scottHeight).

## Sources

- [Tau Ceti documentation: `TauCeti.isIsolatingRank_scottHeight`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.isIsolatingRank_scottHeight)
- [Source of `TauCeti.isIsolatingRank_scottHeight` in TauCeti/ModelTheory/Counting/Stratification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/Stratification.lean#L199)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
