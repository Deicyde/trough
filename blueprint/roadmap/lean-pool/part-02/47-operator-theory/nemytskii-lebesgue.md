---
declaration: theorem
origin: cited
lean: NemytskiiLebesgue.IsCaratheodory.memLp_nemytskii_volume_iff_growth
statement: formalized
proof: formalized
---

# Nemytskii operators on Lebesgue spaces

> Develops superposition operators induced by Caratheodory functions: measurability, Lp-to-Lq growth bounds and sequential continuity, Lipschitz estimates, monotonicity and coercivity, and Frechet remainder estimates. For Lebesgue measure on the real line and finite-dimensional real fibers, characterizes when every Lp input has an Lq output by the standard integrable-envelope growth condition, for 1 <= p,q < infinity. First-order remainder estimates on arbitrary measure spaces assume a Caratheodory derivative with the stated Holder-compatible growth. The integral-functional result bounds the integrated remainder and proves integrability of the linearized integrand; it does not assert integrability of the original integrand without its separate growth hypotheses. Caratheodory here requires strongly measurable sections and almost-everywhere continuity in the fiber variable.

*Quoted from the card [LeanPool/projects/nemytskii-lebesgue.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nemytskii-lebesgue.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NemytskiiLebesgue.IsCaratheodory.memLp_nemytskii_volume_iff_growth`](https://leanpool.github.io/lean-pool/LeanPool/NemytskiiLebesgue/ConverseImplication.html#NemytskiiLebesgue.IsCaratheodory.memLp_nemytskii_volume_iff_growth) (theorem; a main declaration), declared in [LeanPool/NemytskiiLebesgue/ConverseImplication.lean, line 1052](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue/ConverseImplication.lean#L1052): “For f from R times R^m to R^k with strongly measurable sections and almost-everywhere continuous fibers, and 1 <= p,q < infinity, every Lp input gives an Lq output if and only if there exist an Lq real envelope a and a nonnegative constant C such that almost everywhere, simultaneously for every fiber vector xi, norm(f(x,xi)) <= abs(a(x)) + C \* norm(xi)^(p/q).” Its source, as the card gives it: “Upstream NemytskiiLebesgue/ConverseImplication.lean.”
- [`NemytskiiLebesgue.IsCaratheodory.nemytskii_seqContinuous_of_memLp_of_growth_real`](https://leanpool.github.io/lean-pool/LeanPool/NemytskiiLebesgue/Continuity.html#NemytskiiLebesgue.IsCaratheodory.nemytskii_seqContinuous_of_memLp_of_growth_real) (theorem), declared in [LeanPool/NemytskiiLebesgue/Continuity.lean, line 433](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue/Continuity.lean#L433): “On any measure space, the same Caratheodory and growth assumptions imply that a sequence of Lp functions converging in Lp to an Lp function has superposition images converging in Lq, for finite exponents p,q at least one and finite-dimensional real fibers.” Its source, as the card gives it: “Upstream NemytskiiLebesgue/Continuity.lean.”
- [`NemytskiiLebesgue.IsCaratheodory.eLpNorm_frechet_remainder_le_ofReal_mul_eLpNorm`](https://leanpool.github.io/lean-pool/LeanPool/NemytskiiLebesgue/Frechet.html#NemytskiiLebesgue.IsCaratheodory.eLpNorm_frechet_remainder_le_ofReal_mul_eLpNorm) (theorem), declared in [LeanPool/NemytskiiLebesgue/Frechet.lean, line 430](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue/Frechet.lean#L430): “On a measure space, suppose f and its fiber derivative f' are Caratheodory, f' is the Frechet derivative at every fiber point almost everywhere, p,r >= 1 satisfy 1/q = 1/r + 1/p, and f' is bounded by b + C \* norm(xi)^(p/r) with nonnegative b in Lr and C > 0. At each Lp function u, the Lq integral quantity (a quasi-norm when q < 1) of the first-order remainder is at most epsilon times the Lp norm of l whenever l is in Lp and its Lp norm is sufficiently small.” Its source, as the card gives it: “Upstream NemytskiiLebesgue/Frechet.lean; generalized in this port by removing an unused finite-measure assumption.”
- [`NemytskiiLebesgue.IsCaratheodory.integralFunctional_frechet_deriv`](https://leanpool.github.io/lean-pool/LeanPool/NemytskiiLebesgue/IntegralFunctional.html#NemytskiiLebesgue.IsCaratheodory.integralFunctional_frechet_deriv) (theorem), declared in [LeanPool/NemytskiiLebesgue/IntegralFunctional.lean, line 193](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue/IntegralFunctional.lean#L193): “On a measure space with finite-dimensional real inputs, under Caratheodory assumptions on f and its fiber derivative f', conjugate exponents p,q, and derivative growth b + C\*norm(xi)^(p-1) with nonnegative b in Lq and C > 0, the linearized integrand is integrable for every Lp perturbation. The norm of the integral of the first-order remainder is at most epsilon times the Lp norm of the perturbation when that norm is sufficiently small.” Its source, as the card gives it: “Upstream NemytskiiLebesgue/IntegralFunctional.lean; generalized in this port by removing an unused finite-measure assumption.”

## Project

- Authors: Petr Girg, Petr Nečesal, Martin Dvořák, Jakub Psutka.
- Source: *Nemytskii operators on Lebesgue spaces*.
- Project repository: [madvorak/nemytskii-lebesgue](https://github.com/madvorak/nemytskii-lebesgue), at commit [d276c27a](https://github.com/madvorak/nemytskii-lebesgue/tree/d276c27a1e3ebbd9eb09f25243b5e9808ca168d7).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs. The card's note: “Upstream credits the four listed authors. Its README and available commit history contain no AI disclosure; this is evidence under the repository's human-provenance rubric, not proof of tool non-use. The imported version includes substantial AI-assisted Mathlib porting and proof refactoring by OpenAI Codex, so it is recorded as mixed.”
- License: Apache-2.0.
- MSC2020: 47H30, 46E30, 47J05.
- In Lean Pool: [LeanPool/NemytskiiLebesgue](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue), from the card [LeanPool/projects/nemytskii-lebesgue.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nemytskii-lebesgue.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nemytskii-lebesgue.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nemytskii-lebesgue.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NemytskiiLebesgue](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NemytskiiLebesgue)
