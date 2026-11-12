---
catalog: module
lean: Cslib.Probability.PMF.uniformOfFinset, Cslib.Probability.PMF.uniformOfFinset_apply, Cslib.Probability.PMF.mem_support_uniformOfFinset_iff, Cslib.Probability.PMF.uniformOfFintype, Cslib.Probability.PMF.uniformOfFintype_apply, Cslib.Probability.PMF.bind_pair_apply, Cslib.Probability.PMF.bind_pair_tsum_fst, Cslib.Probability.PMF.uniformOfFintype_map_equiv, Cslib.Probability.PMF.uniformOfFintype_prod, Cslib.Probability.PMF.posteriorDist, Cslib.Probability.PMF.posteriorDist_apply, Cslib.Probability.PMF.posteriorDist_eq_prior_of_outputIndist
statement: formalized
proof: formalized
---

# PMF Utilities

`Cslib.Probability.PMF`, in [Cslib/Probability/PMF.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean), by Josha Dekker, Devon Tuma, Kexing Ying, Samuel Schlesinger.

> ## NB: This module is temporary
>
> The bind/pure and posterior lemmas here have no dependence on any domain-specific
> structure. They should be upstreamed to Mathlib
> (likely `Mathlib.Probability.ProbabilityMassFunction.Monad` or a new
> `Mathlib.Probability.ProbabilityMassFunction.Prod`). Once accepted upstream,
> these lemmas should be removed and their consumers should import the Mathlib module instead.
>
> The uniform samplers retain the PMF interface removed in
> [mathlib#42909](https://github.com/leanprover-community/mathlib4/pull/42909),
> pending a decision on CSLib's probability API. Their definitions and proofs are adapted from
> `Mathlib.Probability.Distributions.Uniform` before that PR, by Josha Dekker, Devon Tuma,
> and Kexing Ying, under the Apache 2.0 license.
> Original sampler copyright (c) 2024 Josha Dekker. All rights reserved.
>
> ## Main results
>
> - `Cslib.Probability.PMF.bind_pair_apply`: the "pairing" bind at `(a, b)` equals `p a * f a b`
> - `Cslib.Probability.PMF.bind_pair_tsum_fst`: marginalizing over the first component
> - `Cslib.Probability.PMF.uniformOfFintype_map_equiv`:
>   a uniform distribution is invariant under equivalence
> - `Cslib.Probability.PMF.posteriorDist`: the posterior as a `PMF`
> - `Cslib.Probability.PMF.posteriorDist_eq_prior_of_outputIndist`:
>   if the output distribution does not depend on the input, conditioning does
>   not change the prior

`Cslib.Probability.PMF.uniformOfFinset` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L53))

> Uniform probability mass function on a nonempty finite set.

```lean
noncomputable def uniformOfFinset (s : Finset α) (hs : s.Nonempty) : PMF α
```

`Cslib.Probability.PMF.uniformOfFinset_apply` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L65))

```lean
theorem uniformOfFinset_apply (s : Finset α) (hs : s.Nonempty) (a : α) :
    uniformOfFinset s hs a = if a ∈ s then (s.card : ℝ≥0∞)⁻¹ else 0
```

`Cslib.Probability.PMF.mem_support_uniformOfFinset_iff` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L69))

```lean
theorem mem_support_uniformOfFinset_iff {s : Finset α} (hs : s.Nonempty) (a : α) :
    a ∈ (uniformOfFinset s hs).support ↔ a ∈ s
```

`Cslib.Probability.PMF.uniformOfFintype` (definition, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L74))

> Uniform probability mass function on a nonempty finite type.

```lean
noncomputable def uniformOfFintype (α : Type*) [Fintype α] [Nonempty α] : PMF α
```

`Cslib.Probability.PMF.uniformOfFintype_apply` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L78))

```lean
theorem uniformOfFintype_apply [Fintype α] [Nonempty α] (a : α) :
    uniformOfFintype α a = (Fintype.card α : ℝ≥0∞)⁻¹
```

`Cslib.Probability.PMF.bind_pair_apply` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L84))

> Evaluating the "pairing" bind `(do let a ← p; return (a, ← f a))` at `(a, b)`
> gives the product `p a * f a b`.

```lean
theorem bind_pair_apply (p : PMF α) (f : α → PMF β) (a : α) (b : β) :
    (p.bind fun a' => (f a').bind fun b' => PMF.pure (a', b')) (a, b) = p a * f a b
```

`Cslib.Probability.PMF.bind_pair_tsum_fst` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L93))

> Summing the pairing bind over the first component gives the marginal.

```lean
theorem bind_pair_tsum_fst (p : PMF α) (f : α → PMF β) (b : β) :
    ∑' a, (p.bind fun a' => (f a').bind fun b' => PMF.pure (a', b')) (a, b) =
      (p.bind f) b
```

`Cslib.Probability.PMF.uniformOfFintype_map_equiv` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L99))

> A uniform distribution on a finite type is invariant under any equivalence.

```lean
theorem uniformOfFintype_map_equiv {γ : Type v} [Fintype α] [Fintype γ] [Nonempty α] [Nonempty γ]
    (e : α ≃ γ) :
    (uniformOfFintype α).map e = uniformOfFintype γ
```

`Cslib.Probability.PMF.uniformOfFintype_prod` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L108))

> Independent uniform sampling on `α` and `β` equals uniform sampling on `α × β`.

```lean
theorem uniformOfFintype_prod (α β : Type*)
    [Fintype α] [Nonempty α] [Fintype β] [Nonempty β] :
    ((PMF.uniformOfFintype α).bind fun a =>
      (PMF.uniformOfFintype β).map fun b => (a, b)) =
    PMF.uniformOfFintype (α × β)
```

`Cslib.Probability.PMF.posteriorDist` (definition, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L121))

> The posterior distribution `Pr[A = a | B = b]` as a `PMF`,
> given `a ← p`, `b ← f a`, and that `b` has positive marginal probability:
> the joint distribution's slice at `b`, normalized.

```lean
noncomputable def posteriorDist (p : PMF α) (f : α → PMF β) (b : β)
    (hb : b ∈ (p.bind f).support) : PMF α
```

`Cslib.Probability.PMF.posteriorDist_apply` (theorem, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L129))

```lean
theorem posteriorDist_apply (p : PMF α) (f : α → PMF β) (b : β)
    (hb : b ∈ (p.bind f).support) (a : α) :
    posteriorDist p f b hb a =
      (p.bind fun a' => (f a').bind fun b' => PMF.pure (a', b')) (a, b) /
        (p.bind f) b
```

`Cslib.Probability.PMF.posteriorDist_eq_prior_of_outputIndist` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean#L138))

> If the output distribution of a channel does not depend on the input, then
> conditioning on any output with positive probability leaves the prior unchanged.

```lean
theorem posteriorDist_eq_prior_of_outputIndist (p : PMF α) (f : α → PMF β)
    (h : ∀ a₀ a₁ : α, f a₀ = f a₁)
    (b : β) (hb : b ∈ (p.bind f).support) :
    posteriorDist p f b hb = p
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Probability/PMF.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/PMF.lean)
