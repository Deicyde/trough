---
declaration: theorem
origin: cited
lean: TauCeti.karp_theorem
statement: formalized
proof: formalized
---

# Karp's theorem

Structures in a relational language are potentially isomorphic exactly when
they satisfy the same infinitary sentences. The converse uses the carrier `M ⊕ N`.

```lean
TauCeti.karp_theorem.{u, v, w, w'} {L : FirstOrder.Language} {M : Type w} {N : Type w'}
  [L.Structure M] [L.Structure N] [L.IsRelational] :
  TauCeti.PotentialIso M N ↔ TauCeti.InfEquivW M N
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Proof depends on

- [Back-and-forth equivalence at level `α` gives agreement up to quantifier rank `α`](back-and-forth-equivalence-at-level-gives-agreem.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.karp_theorem`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem).

## Sources

- [Tau Ceti documentation: `TauCeti.karp_theorem`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.karp_theorem)
- [Source of `TauCeti.karp_theorem` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/Karp.lean#L309)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
