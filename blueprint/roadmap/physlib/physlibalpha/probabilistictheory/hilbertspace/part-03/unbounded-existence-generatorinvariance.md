---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate_comm, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate_hasDerivAt, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain_translate, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain_translate_mem, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_hasDerivAt
statement: formalized
proof: formalized
---

# The unitary group preserves the domain of its generator (GeneratorInvariance)

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.GeneratorInvariance`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean): 6 declarations, 6 with a docstring.

> A unitary group preserves the domain of its candidate generator and commutes with it.

## i. Overview

> A strongly continuous unitary group preserves the domain of its candidate generator `T` and commutes
> with it there. So the orbit of a vector in the domain is differentiable at every time `s`, with
> derivative `i T (U s ψ)`.

## ii. Key results

> - `stoneCandidateDomain_translate` : the group preserves the domain.
> - `stoneCandidateGenerator_translate` : the generator commutes with the group.
> - `stoneCandidateGenerator_hasDerivAt` : orbits of domain vectors are differentiable at every time.

## iv. References

> * None.

## A. Invariance of the candidate domain

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate_comm`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L63).

> `U t (U s ψ)` and `U s (U t ψ)` agree as functions of `s`, since `s + t = t + s`.

```lean
lemma stoneCandidateGenerator_translate_comm (ψ : H) (t : ℝ) :
    (fun s : ℝ => (U t : H →L[ℂ] H) (U s ψ)) = (fun s : ℝ => (U s : H →L[ℂ] H) (U t ψ))
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate_hasDerivAt`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L77).

> If `ψ`'s orbit is differentiable at `0` with witness `φ`, then `U t ψ`'s orbit is again
> differentiable at `0`, with witness `U t φ` — the group law turns the fixed continuous linear map
> `U t` applied to `ψ`'s derivative witness into a derivative witness for `U t ψ`.

```lean
lemma stoneCandidateGenerator_translate_hasDerivAt {ψ φ : H} (t : ℝ)
    (hφ : HasDerivAt (fun s : ℝ => U s ψ) φ 0) :
    HasDerivAt (fun s : ℝ => U s (U t ψ)) (U t φ) 0
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain_translate`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L91).

> The candidate domain is invariant under every `U t`.

```lean
lemma stoneCandidateDomain_translate {ψ : H} (hψ : stoneCandidateDomainPred (U := U) ψ)
    (t : ℝ) : stoneCandidateDomainPred (U := U) (U t ψ)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain_translate_mem`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L99).

> The candidate domain, packaged as a `Submodule`-invariance statement under every `U t`.

```lean
lemma stoneCandidateDomain_translate_mem (ψ : stoneCandidateDomain (U := U) hUmul) (t : ℝ) :
    (U t (ψ : H)) ∈ stoneCandidateDomain (U := U) hUmul
```

## B. Commutation and differentiability of orbits

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_translate`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L113).

> The candidate generator commutes with the group it was built from: for `ψ` in `T.domain`,
> `U t ψ` is again in `T.domain`, and `T (U t ψ) = U t (T ψ)`.

```lean
lemma stoneCandidateGenerator_translate (ψ : stoneCandidateDomain (U := U) hUmul) (t : ℝ) :
    stoneCandidateGenerator (U := U) hUmul
        ⟨U t (ψ : H), stoneCandidateDomain_translate_mem hUmul ψ t⟩ =
      U t (stoneCandidateGenerator (U := U) hUmul ψ)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_hasDerivAt`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean#L134).

> The orbit of a domain vector is differentiable at every time `s`, with derivative `i T (U s ψ)`.

```lean
lemma stoneCandidateGenerator_hasDerivAt (ψ : stoneCandidateDomain (U := U) hUmul) (s : ℝ) :
    HasDerivAt (fun r : ℝ => U r (ψ : H))
      (Complex.I • U s (stoneCandidateGenerator (U := U) hUmul ψ)) s
```

## Depends on

- [The candidate generator of a unitary group](unbounded-existence-candidategenerator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GeneratorInvariance.lean)
