---
declaration: def
origin: cited
lean: LinearMap.hattoriStallingsTrace
statement: formalized
---

# LinearMap.hattoriStallingsTrace

The Hattori–Stallings trace of an endomorphism of a finite projective left module.
It is characterized by `hattoriStallingsTrace_eq_of_retract`, so does not depend on the
finite free retract chosen in its construction.

```lean
LinearMap.hattoriStallingsTrace.{u_1, u_2} (R : Type u_1) [Ring R] (M : Type u_2) [AddCommGroup M]
  [_root_.Module R M] [Module.Finite R M] [Module.Projective R M] :
  Module.End R M →+ TauCeti.cyclicQuotient ℤ R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.hattoriStallingsTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/HattoriStallings.html#LinearMap.hattoriStallingsTrace).

## Sources

- [Tau Ceti documentation: `LinearMap.hattoriStallingsTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/HattoriStallings.html#LinearMap.hattoriStallingsTrace)
- [Source of `LinearMap.hattoriStallingsTrace` in TauCeti/LinearAlgebra/Trace/HattoriStallings.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Trace/HattoriStallings.lean#L113)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
