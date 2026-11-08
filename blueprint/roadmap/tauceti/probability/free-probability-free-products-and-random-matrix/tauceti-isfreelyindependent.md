---
declaration: def
origin: cited
lean: TauCeti.IsFreelyIndependent
statement: formalized
---

# TauCeti.IsFreelyIndependent

Subalgebras `B i` of `A` are *freely independent* with respect to a linear functional `φ` if
`φ (a₁ * ⋯ * aₙ) = 0` for every nonempty word `[(i₁, a₁), …, (iₙ, aₙ)]` whose consecutive labels
are distinct and whose letters satisfy `aⱼ ∈ B iⱼ` and `φ aⱼ = 0`. Labels that are not adjacent
may coincide.

```lean
TauCeti.IsFreelyIndependent.{u_1, u_2, u_4} {R : Type u_1} {A : Type u_2} {ι : Type u_4}
  [CommSemiring R] [Semiring A] [Algebra R A] (φ : A →ₗ[R] R) (B : ι → Subalgebra R A) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependent`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Independence.html#TauCeti.IsFreelyIndependent).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFreelyIndependent`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Independence.html#TauCeti.IsFreelyIndependent)
- [Source of `TauCeti.IsFreelyIndependent` in TauCeti/Probability/FreeProbability/Independence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/FreeProbability/Independence.lean#L94)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
