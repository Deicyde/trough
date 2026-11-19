---
declaration: theorem
origin: cited
lean: TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE
statement: formalized
proof: formalized
---

# Hartogs' local removable singularity theorem

In a finite-dimensional complex normed space
`E` of dimension at least two, any map `f : E → F` into a complete complex normed space that is
complex differentiable on a punctured neighbourhood of `p` agrees on a punctured neighbourhood of
`p` with a function analytic at `p`.

```lean
TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : E → F} {p : E}
  (hf : ∀ᶠ (z : E) in nhdsWithin p {p}ᶜ, DifferentiableAt ℂ f z) :
  ∃ g, AnalyticAt ℂ g p ∧ g =ᶠ[nhdsWithin p {p}ᶜ] f
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Hartogs' extension theorem on product shells](hartogs-extension-theorem-on-product-shells.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE)
- [Source of `TauCeti.exists_analyticAt_and_eventuallyEq_nhdsNE` in TauCeti/Analysis/Complex/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Hartogs.lean#L212)
