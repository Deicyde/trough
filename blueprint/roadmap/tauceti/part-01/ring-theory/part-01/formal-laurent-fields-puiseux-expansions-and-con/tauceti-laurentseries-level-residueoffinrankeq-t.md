---
declaration: theorem
origin: cited
lean: TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace
statement: formalized
proof: formalized
---

# TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace

Trace preserves residues in any tower of finite extensions of `K⸨t⸩`, with every
form expressed as a multiple of the same base differential `dt`.

```lean
TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace.{u_1, u_2, u_3} {K : Type u_1} [Field K]
  [IsAlgClosed K] [CharZero K] {L : Type u_2} [Field L] [Algebra (LaurentSeries K) L] {e : ℕ+}
  {M : Type u_3} [Field M] [Algebra (LaurentSeries K) M] [Algebra M L]
  [IsScalarTower (LaurentSeries K) M L] {d : ℕ+} (hM : Module.finrank (LaurentSeries K) M = ↑d)
  (hL : Module.finrank (LaurentSeries K) L = ↑e) (x : L) :
  (TauCeti.LaurentSeries.Level.residueOfFinrankEq hM) ((Algebra.trace M L) x) =
    (TauCeti.LaurentSeries.Level.residueOfFinrankEq hL) x
```

## Depends on

- [Finite extensions of `K⸨X⸩`](finite-extensions-of-kx.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/Residue.html#TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/Residue.html#TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace)
- [Source of `TauCeti.LaurentSeries.Level.residueOfFinrankEq_trace` in TauCeti/RingTheory/LaurentSeries/Level/Residue.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Level/Residue.lean#L191)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
