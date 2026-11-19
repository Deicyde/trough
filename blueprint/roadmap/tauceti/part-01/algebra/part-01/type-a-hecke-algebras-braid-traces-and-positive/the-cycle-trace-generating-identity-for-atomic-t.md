---
declaration: theorem
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function
statement: formalized
proof: formalized
---

# The cycle-trace generating identity for atomic traces

With `Q = q ^ 2`, the generating
series `1 + (Q - 1) * ∑ (m ≥ 1), tr (ζₘ) * X ^ m` of the atomic traces of the cycle words, times
the factor `1 - Q * p a * X` of each positive letter and `1 + p a * X` of each negative letter,
is the product of the factors `1 - p a * X` of the positive letters and `1 + Q * p a * X` of the
negative letters.

```lean
TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function.{u_1, u_2} {R : Type u_1}
  [CommRing R] {ι : Type u_2} [LinearOrder ι] (pos : ι → Prop) [DecidablePred pos] (q : Rˣ)
  [Fintype ι] (p : ι → R) :
  ((PowerSeries.mk fun m =>
        if m = 0 then 1
        else
          (↑q ^ 2 - 1) *
            (TauCeti.TypeAHeckeAlgebra.atomicTrace pos q p m)
              (TauCeti.TypeAHeckeAlgebra.cycleWord q m)) *
      ∏ a,
        if pos a then 1 - PowerSeries.C (↑q ^ 2 * p a) * PowerSeries.X
        else 1 + PowerSeries.C (p a) * PowerSeries.X) =
    ∏ a,
      if pos a then 1 - PowerSeries.C (p a) * PowerSeries.X
      else 1 + PowerSeries.C (↑q ^ 2 * p a) * PowerSeries.X
```

## Depends on

- [TauCeti.TypeAHeckeAlgebra.atomicTrace](tauceti-typeaheckealgebra-atomictrace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/CycleWord.html#TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/CycleWord.html#TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function)
- [Source of `TauCeti.TypeAHeckeAlgebra.atomicTrace_cycleWord_generating_function` in TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/CycleWord.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/CycleWord.lean#L210)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
