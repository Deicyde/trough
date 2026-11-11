---
declaration: def
origin: cited
lean: ContinuousMulEquiv.quotientKerEquivOfSurjective, ContinuousAddEquiv.quotientKerEquivOfSurjective
statement: formalized
---

# The first isomorphism theorem for a surjective strict homomorphism of topological groups

`G ⧸ f.ker ≃ₜ* H`.

```lean
ContinuousMulEquiv.quotientKerEquivOfSurjective.{u_1, u_2} {G : Type u_1} {H : Type u_2} [Group G]
  [Group H] [TopologicalSpace G] [TopologicalSpace H] (f : G →* H) (hf : Topology.IsStrictMap ⇑f)
  (hs : Function.Surjective ⇑f) : G ⧸ f.ker ≃ₜ* H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousMulEquiv.quotientKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/ContinuousMonoidHom/QuotientKerEquiv.html#ContinuousMulEquiv.quotientKerEquivOfSurjective).

## Other forms

**The first isomorphism theorem for a surjective strict homomorphism of topological additive groups.** Formalized in Tau Ceti as [`ContinuousAddEquiv.quotientKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/ContinuousMonoidHom/QuotientKerEquiv.html#ContinuousAddEquiv.quotientKerEquivOfSurjective).

```lean
ContinuousAddEquiv.quotientKerEquivOfSurjective.{u_1, u_2} {G : Type u_1} {H : Type u_2}
  [AddGroup G] [AddGroup H] [TopologicalSpace G] [TopologicalSpace H] (f : G →+ H)
  (hf : Topology.IsStrictMap ⇑f) (hs : Function.Surjective ⇑f) : G ⧸ f.ker ≃ₜ+ H
```

## Sources

- [Tau Ceti documentation: `ContinuousMulEquiv.quotientKerEquivOfSurjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/ContinuousMonoidHom/QuotientKerEquiv.html#ContinuousMulEquiv.quotientKerEquivOfSurjective)
- [Source of `ContinuousMulEquiv.quotientKerEquivOfSurjective` in TauCeti/Topology/Algebra/ContinuousMonoidHom/QuotientKerEquiv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/ContinuousMonoidHom/QuotientKerEquiv.lean#L47)
