---
declaration: instance
origin: cited
lean: TauCeti.CurrentAlgebra.instRingCompletedEnveloping
statement: formalized
---

# The completed enveloping algebra is a ring

**The completed enveloping algebra is a ring**, with `(x y)_n = x · y_n` for the action of `Û`
on the smooth module `U / I_n` extending that of `U`, and unit the image of `1`.

```lean
TauCeti.CurrentAlgebra.instRingCompletedEnveloping.{u_1, u_2} {R : Type u_1} {L : Type u_2}
  [CommRing R] [LieRing L] [LieAlgebra R L] (Φ : LinearMap.BilinForm R L)
  (hΦ : LinearMap.BilinForm.lieInvariant L Φ) (hΦs : Φ.IsSymm) (a : R) :
  Ring (TauCeti.CurrentAlgebra.CompletedEnveloping Φ hΦ hΦs a)
```

## Depends on

- [The completed enveloping algebra](the-completed-enveloping-algebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.instRingCompletedEnveloping`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Completion.html#TauCeti.CurrentAlgebra.instRingCompletedEnveloping).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.instRingCompletedEnveloping`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Completion.html#TauCeti.CurrentAlgebra.instRingCompletedEnveloping)
- [Source of `TauCeti.CurrentAlgebra.instRingCompletedEnveloping` in TauCeti/Algebra/Lie/Current/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Current/Completion.lean#L163)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
