---
declaration: theorem
origin: cited
lean: TauCeti.countable_infEquivAt_nat_iff_iso
statement: formalized
proof: formalized
---

# Karp's theorem for countable structures

Countable structures in a relational language are
isomorphic exactly when they satisfy the same `L_{ω₁ω}` sentences, the infinitary sentences whose
conjunctions and disjunctions are indexed by `ℕ`.

```lean
TauCeti.countable_infEquivAt_nat_iff_iso.{u, v, w, w'} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] [L.IsRelational] [Countable M] [Countable N] :
  TauCeti.InfEquivAt ℕ M N ↔ Nonempty (L.Equiv M N)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Proof depends on

- [Karp's theorem at a common carrier](karps-theorem-at-a-common-carrier.md)
- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.countable_infEquivAt_nat_iff_iso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.countable_infEquivAt_nat_iff_iso).

## Sources

- [Tau Ceti documentation: `TauCeti.countable_infEquivAt_nat_iff_iso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.countable_infEquivAt_nat_iff_iso)
- [Source of `TauCeti.countable_infEquivAt_nat_iff_iso` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/Karp.lean#L326)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
