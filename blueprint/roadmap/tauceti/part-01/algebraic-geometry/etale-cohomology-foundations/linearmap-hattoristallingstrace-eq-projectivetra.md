---
declaration: theorem
origin: cited
lean: LinearMap.hattoriStallingsTrace_eq_projectiveTrace
statement: formalized
proof: formalized
---

# LinearMap.hattoriStallingsTrace_eq_projectiveTrace

Over a commutative ring the Hattori–Stallings trace is the cyclic class of the
finite-projective contraction trace, including on projective modules of varying local rank.

```lean
LinearMap.hattoriStallingsTrace_eq_projectiveTrace.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [Module.Finite R M] [Module.Projective R M]
  (f : Module.End R M) :
  (LinearMap.hattoriStallingsTrace R M) f =
    (TauCeti.commutatorSubmodule ℤ R).mkQ ((LinearMap.projectiveTrace R M) f)
```

## Depends on

- [LinearMap.hattoriStallingsTrace](linearmap-hattoristallingstrace.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.hattoriStallingsTrace_eq_projectiveTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/HattoriStallings.html#LinearMap.hattoriStallingsTrace_eq_projectiveTrace).

## Sources

- [Tau Ceti documentation: `LinearMap.hattoriStallingsTrace_eq_projectiveTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/HattoriStallings.html#LinearMap.hattoriStallingsTrace_eq_projectiveTrace)
- [Source of `LinearMap.hattoriStallingsTrace_eq_projectiveTrace` in TauCeti/LinearAlgebra/Trace/HattoriStallings.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Trace/HattoriStallings.lean#L237)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
