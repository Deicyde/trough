---
declaration: theorem
origin: cited
lean: LeanPool.KrohnRhodes.krohn_rhodes_prime_decomposition
statement: formalized
proof: formalized
---

# Aperiodic and simple-group wreath-division towers

> Constructs a finite recursive wreath-division tower for every finite monoid in universe zero, with finite aperiodic or finite simple-group factors and every simple-group factor a monoid divisor of the original monoid. Implements a variant of the Diekert–Kufleitner–Steinberg local-divisor argument, with reusable monoid and semigroup division, local divisors, action coverings, wreath reassociation, and the Krasner–Kaloujnine group embedding. The endpoint permits arbitrary aperiodic factors and recursive intermediate bases; it does not assert the three-element flip-flop reduction, a single transformation-monoid strong division, or quantitative decomposition bounds.

*Quoted from the card [LeanPool/projects/krohn-rhodes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krohn-rhodes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.KrohnRhodes.krohn_rhodes_prime_decomposition`](https://leanpool.github.io/lean-pool/LeanPool/KrohnRhodes/PrimeDecomposition.html#LeanPool.KrohnRhodes.krohn_rhodes_prime_decomposition) (theorem; a main declaration), declared in [LeanPool/KrohnRhodes/PrimeDecomposition.lean, line 1032](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrohnRhodes/PrimeDecomposition.lean#L1032): “Every finite monoid M in universe zero admits a finite list of finite monoid factors, each witnessed to be aperiodic or a simple group, with DivTowerWreath M factors and every simple-group factor a monoid divisor of M. An empty tower means M divides the trivial monoid. At a nonempty step, M divides F wreath B for a finite action of a finite monoid B that itself has the tail tower.” Its source, as the card gives it: “Upstream PrimeDecomposition.lean, completed September 28, 2026 at 07:36:52 UTC and publicly released at 08:48:24 UTC. Variant of Diekert–Kufleitner–Steinberg, arXiv:1111.1585, Sections 3–4, with left actions, the larger local divisor cM intersect Mc, arbitrary aperiodic factors, and recursive semigroup divisions. The stronger flip-flop and transformation-monoid claims of Theorem 4.1 are not asserted. Upstream CITATION.cff attributes the proofs primarily to Claude Code under Aditya Rao's direction.”
- [`LeanPool.KrohnRhodes.krasnerKaloujnine_injective`](https://leanpool.github.io/lean-pool/LeanPool/KrohnRhodes/Foundations/KrasnerKaloujnine.html#LeanPool.KrohnRhodes.krasnerKaloujnine_injective) (theorem), declared in [LeanPool/KrohnRhodes/Foundations/KrasnerKaloujnine.lean, line 139](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrohnRhodes/Foundations/KrasnerKaloujnine.lean#L139): “For any group G and normal subgroup N, the constructed monoid homomorphism from G to Mathlib's regular wreath product of N and G/N is injective. No finiteness assumption is required.” Its source, as the card gives it: “Upstream Foundations/KrasnerKaloujnine.lean; the classical Krasner–Kaloujnine embedding theorem.”
- [`LeanPool.KrohnRhodes.LocalDivisor.localDivides`](https://leanpool.github.io/lean-pool/LeanPool/KrohnRhodes/Foundations/LocalDivisor.html#LeanPool.KrohnRhodes.LocalDivisor.localDivides) (theorem), declared in [LeanPool/KrohnRhodes/Foundations/LocalDivisor.lean, line 166](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrohnRhodes/Foundations/LocalDivisor.lean#L166): “For any monoid M and c in M, the local divisor on cM intersect Mc, with its twisted multiplication and identity c, is a quotient of a submonoid of M.” Its source, as the card gives it: “Diekert–Kufleitner–Steinberg, arXiv:1111.1585, Section 2.5; uses the full local divisor rather than the smaller cMc union {c}.”

## Project

- Authors: Aditya Rao.
- Source: *Krohn–Rhodes formalization by Aditya Rao*, [arXiv:1111.1585](https://arxiv.org/abs/1111.1585).
- Project repository: [adii800/krohn-rhodes-lean](https://github.com/adii800/krohn-rhodes-lean), at commit [8152fef3](https://github.com/adii800/krohn-rhodes-lean/tree/8152fef3507406d2b4f4ed3760404ea88298e382).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 20M10, 20M35, 20E22.
- In Lean Pool: [LeanPool/KrohnRhodes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrohnRhodes), from the card [LeanPool/projects/krohn-rhodes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krohn-rhodes.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/krohn-rhodes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krohn-rhodes.yaml)
- [Lean Pool at 701389c0: LeanPool/KrohnRhodes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrohnRhodes)
