---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.mem_center_iff_forall_commute
statement: formalized
proof: formalized
---

# Centrality in the completed enveloping algebra is detected on the current generators

an
element of `Û` is central exactly when it commutes with the images of all currents.

```lean
TauCeti.CurrentAlgebra.mem_center_iff_forall_commute.{u_1, u_2} {R : Type u_1} {L : Type u_2}
  [CommRing R] [LieRing L] [LieAlgebra R L] {Φ : LinearMap.BilinForm R L}
  {hΦ : LinearMap.BilinForm.lieInvariant L Φ} {hΦs : Φ.IsSymm} {a : R}
  {z : TauCeti.CurrentAlgebra.CompletedEnveloping Φ hΦ hΦs a} :
  z ∈ Subalgebra.center R (TauCeti.CurrentAlgebra.CompletedEnveloping Φ hΦ hΦs a) ↔
    ∀ (u : TauCeti.currentAlgebra R L),
      Commute
        ((TauCeti.CurrentAlgebra.toCompletedEnveloping Φ hΦ hΦs a)
          ((LieAlgebra.ofTwoCocycle.envelopingι
              (TauCeti.CurrentAlgebra.twoCocycleOfBilinear R L Φ hΦ hΦs) a)
            u))
        z
```

## Depends on

- [The completed enveloping algebra](the-completed-enveloping-algebra.md)
- [The completed enveloping algebra is a ring](the-completed-enveloping-algebra-is-a-ring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.mem_center_iff_forall_commute`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Center.html#TauCeti.CurrentAlgebra.mem_center_iff_forall_commute).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.mem_center_iff_forall_commute`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Center.html#TauCeti.CurrentAlgebra.mem_center_iff_forall_commute)
- [Source of `TauCeti.CurrentAlgebra.mem_center_iff_forall_commute` in TauCeti/Algebra/Lie/Current/Center.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Current/Center.lean#L130)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
