---
declaration: theorem
origin: cited
lean: TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap
statement: formalized
proof: formalized
---

# A finite module over a complete noetherian Tate ring has a strict finite presentation

This is the sentence Wedhorn's Remark 8.29 opens with: "we find a presentation
`Aⁿ →[u] Aᵐ →[p] M → 0` (because `A` is noetherian). Proposition 6.18(2) shows that `u` and `p`
are continuous and open onto its image."

`M` carries its canonical topology, which is Mathlib's module topology: every complete
first-countable module topology on a finite module is the module topology
(`TauCeti.Huber.IsTateRing.isModuleTopology`), so `IsModuleTopology A M` is the topology
Proposition 6.18(1) speaks of, and nothing else is asked of `M`. The presentation is Mathlib's
`Module.FinitePresentation.exists_fin'`, available because a finite module over a noetherian ring
is finitely presented. Both maps are continuous by `IsModuleTopology.continuous_of_linearMap`,
`p` is open by `IsModuleTopology.isOpenMap_of_surjective` — the module topology on `M` is the
quotient topology along any linear surjection from `Aᵐ` — and `u` is strict by
`LinearMap.isStrictMap_of_isClosed_range_of_isTateRing`, its range being closed in `Aᵐ` by
`TauCeti.Huber.isClosed_of_isNoetherian`. That closedness is the one place, beyond the existence
of the presentation, where `A` being noetherian enters, and the open mapping theorem is spent on
the free module `Aᵐ`, not on `M`.

```lean
TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap.{u_3, u_4} {A : Type u_3}
  [CommRing A] [UniformSpace A] [IsUniformAddGroup A] [CompleteSpace A] [T0Space A]
  [NonarchimedeanRing A] [TauCeti.Huber.IsTateRing A] [IsNoetherianRing A] {M : Type u_4}
  [AddCommGroup M] [_root_.Module A M] [Module.Finite A M] [TopologicalSpace M]
  [IsModuleTopology A M] :
  ∃ n m u p,
    Continuous ⇑u ∧
      Continuous ⇑p ∧
        Function.Surjective ⇑p ∧ Function.Exact ⇑u ⇑p ∧ Topology.IsStrictMap ⇑u ∧ IsOpenMap ⇑p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Henkel's open mapping theorem](../../topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ClosedSubmodule.html#TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/ClosedSubmodule.html#TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap)
- [Source of `TauCeti.Huber.IsTateRing.exists_presentation_isStrictMap_isOpenMap` in TauCeti/RingTheory/Huber/ClosedSubmodule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/ClosedSubmodule.lean#L160)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
