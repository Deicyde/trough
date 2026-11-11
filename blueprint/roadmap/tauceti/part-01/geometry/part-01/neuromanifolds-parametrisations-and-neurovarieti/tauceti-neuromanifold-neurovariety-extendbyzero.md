---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.neurovariety_extendByZero_comp
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.neurovariety_extendByZero_comp

Zero-padding the coordinates along an injective `s` transports the neurovariety along the
padding. No finiteness of the coordinates is needed.

```lean
TauCeti.Neuromanifold.neurovariety_extendByZero_comp.{u_1, u_2, u_3, u_4} {W : Type u_1}
  {σ : Type u_2} {τ : Type u_3} {K : Type u_4} [Field K] {s : σ → τ} (hs : Function.Injective s)
  (c : W → σ → K) :
  TauCeti.Neuromanifold.neurovariety (⇑(Function.ExtendByZero.linearMap K K s) ∘ c) =
    ⇑(Function.ExtendByZero.linearMap K K s) '' TauCeti.Neuromanifold.neurovariety c
```

## Depends on

- [TauCeti.Neuromanifold.neurovariety](tauceti-neuromanifold-neurovariety.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.neurovariety_extendByZero_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Neurovariety.html#TauCeti.Neuromanifold.neurovariety_extendByZero_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.neurovariety_extendByZero_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Neurovariety.html#TauCeti.Neuromanifold.neurovariety_extendByZero_comp)
- [Source of `TauCeti.Neuromanifold.neurovariety_extendByZero_comp` in TauCeti/Geometry/Neuromanifold/Neurovariety.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/Neurovariety.lean#L232)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
