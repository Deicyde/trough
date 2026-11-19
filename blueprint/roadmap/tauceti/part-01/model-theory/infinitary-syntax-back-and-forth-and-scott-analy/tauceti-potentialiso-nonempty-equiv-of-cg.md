---
declaration: theorem
origin: cited
lean: TauCeti.PotentialIso.nonempty_equiv_of_cg
statement: formalized
proof: formalized
---

# TauCeti.PotentialIso.nonempty_equiv_of_cg

Potentially isomorphic countably generated structures are isomorphic. Countable generation
suffices even when function symbols generate uncountably many elements.

```lean
TauCeti.PotentialIso.nonempty_equiv_of_cg.{u, v, w, w'} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] (h : TauCeti.PotentialIso M N)
  (hM : FirstOrder.Language.Structure.CG L M) (hN : FirstOrder.Language.Structure.CG L N) :
  Nonempty (L.Equiv M N)
```

## Depends on

- [TauCeti.PotentialIso](tauceti-potentialiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PotentialIso.nonempty_equiv_of_cg`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Countable.html#TauCeti.PotentialIso.nonempty_equiv_of_cg).

## Sources

- [Tau Ceti documentation: `TauCeti.PotentialIso.nonempty_equiv_of_cg`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Countable.html#TauCeti.PotentialIso.nonempty_equiv_of_cg)
- [Source of `TauCeti.PotentialIso.nonempty_equiv_of_cg` in TauCeti/ModelTheory/BackAndForth/Countable.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/BackAndForth/Countable.lean#L90)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
