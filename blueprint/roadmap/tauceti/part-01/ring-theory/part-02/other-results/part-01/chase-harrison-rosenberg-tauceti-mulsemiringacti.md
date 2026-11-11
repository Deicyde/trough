---
declaration: theorem
origin: cited
lean: TauCeti.MulSemiringAction.tensorToPi_bijective, TauCeti.MulSemiringAction.tensorToPi_surjective_iff
statement: formalized
proof: formalized
---

# Chase–Harrison–Rosenberg (`TauCeti.MulSemiringAction.tensorToPi_bijective`)

For a free action of a finite group with invariant ring `R`,
`tensorToPi : A ⊗[R] A → (G → A)` is bijective.

```lean
TauCeti.MulSemiringAction.tensorToPi_bijective.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {G : Type u_3} [CommSemiring R] [CommRing A] [Algebra R A] [Group G] [MulSemiringAction G A]
  [SMulCommClass G R A] [Algebra.IsInvariant R A G] [Finite G]
  (hG : ∀ (g : G), g ≠ 1 → Ideal.span (Set.range fun a => g • a - a) = ⊤) :
  Function.Bijective ⇑(TauCeti.MulSemiringAction.tensorToPi R A G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MulSemiringAction.tensorToPi_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Invariant/Free.html#TauCeti.MulSemiringAction.tensorToPi_bijective).

## Other forms

**Chase–Harrison–Rosenberg.** Formalized in Tau Ceti as [`TauCeti.MulSemiringAction.tensorToPi_surjective_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Invariant/Free.html#TauCeti.MulSemiringAction.tensorToPi_surjective_iff).

```lean
TauCeti.MulSemiringAction.tensorToPi_surjective_iff.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {G : Type u_3} [CommSemiring R] [CommRing A] [Algebra R A] [Group G] [MulSemiringAction G A]
  [SMulCommClass G R A] [Finite G] :
  Function.Surjective ⇑(TauCeti.MulSemiringAction.tensorToPi R A G) ↔
    ∀ (g : G), g ≠ 1 → Ideal.span (Set.range fun a => g • a - a) = ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.MulSemiringAction.tensorToPi_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Invariant/Free.html#TauCeti.MulSemiringAction.tensorToPi_bijective)
- [Source of `TauCeti.MulSemiringAction.tensorToPi_bijective` in TauCeti/RingTheory/Invariant/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Invariant/Free.lean#L339)
