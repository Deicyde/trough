---
declaration: theorem
origin: cited
lean: NLSCritical.NLS_apriori
statement: formalized
---

# Energy-critical NLS in three dimensions.

> This file states an a priori estimate for the energy-critical nonlinear Schrödinger equation on $ℝ^3$.
> By 'soft' arguments, this bound implies global well-posedness in the energy space, scattering,
> asymptotic completeness, and uniform regularity (all of which are less elementary to state).
> This is remarked on p. 770 and p. 793 in the referenced article which first proved the a priori bound.
>
> The main theorem is:
> - `NLS_apriori`: a bound on the space-time $L^10$ norm in terms of the initial energy for local
>   smooth solutions to the NLS equation.
>
> ## References
> * [Colliander, Keel, Staffilani, Takaoka, Tao](https://doi.org/10.4007/annals.2008.167.767),
>   Annals of Mathematics 167 (2008) proves the a priori estimate, and thereby, global well-posedness.

*Quoted from [FormalConjectures/Paper/NLSCritical.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/NLSCritical.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `NLSCritical.NLS_apriori`

Solved: stated here without proof.

> The $L^10_{t,x}$ a priori estimate for local schwartz solutions.

```lean
theorem NLS_apriori :
    ∃ f : ℝ → ℝ, ∀ l > 0, ∀ s : LocalSchwartzSolution l,
    L10_local l s.u ≤ f (energy (s.u 0))
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/NLSCritical.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/NLSCritical.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/NLSCritical.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/NLSCritical.lean)
- [Colliander, Keel, Staffilani, Takaoka, Tao](https://doi.org/10.4007/annals.2008.167.767)
