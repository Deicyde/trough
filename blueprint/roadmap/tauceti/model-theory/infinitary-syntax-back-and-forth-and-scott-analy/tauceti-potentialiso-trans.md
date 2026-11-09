---
declaration: theorem
origin: cited
lean: TauCeti.PotentialIso.trans
statement: formalized
proof: formalized
---

# TauCeti.PotentialIso.trans

Potential isomorphism is transitive.

```lean
TauCeti.PotentialIso.trans.{u, v, w, w', u_1} {L : FirstOrder.Language} {M : Type w} {N : Type w'}
  [L.Structure M] [L.Structure N] {P : Type u_1} [L.Structure P] (h₁ : TauCeti.PotentialIso M N)
  (h₂ : TauCeti.PotentialIso N P) : TauCeti.PotentialIso M P
```

## Depends on

- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PotentialIso.trans`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/PotentialIso.html#TauCeti.PotentialIso.trans).

## Sources

- [Tau Ceti documentation: `TauCeti.PotentialIso.trans`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/PotentialIso.html#TauCeti.PotentialIso.trans)
- [Source of `TauCeti.PotentialIso.trans` in TauCeti/ModelTheory/BackAndForth/PotentialIso.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/PotentialIso.lean#L112)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
