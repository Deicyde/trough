# Supernatural numbers

> Prime-exponent supernatural arithmetic, finite-quotient profinite orders and indices of closed subgroups, a closed-subgroup tower law, and the torsion-order comparison with profinite rational-circle character groups.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/formalization.yaml) of [FormalFrontier/supernatural-numbers](https://github.com/FormalFrontier/supernatural-numbers) at commit [cb444a40](https://github.com/FormalFrontier/supernatural-numbers/tree/cb444a4051e593328d3e99ad5ae5c8c56ca48099), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 3 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/supernatural-numbers](https://github.com/FormalFrontier/supernatural-numbers), read at commit [cb444a40](https://github.com/FormalFrontier/supernatural-numbers/tree/cb444a4051e593328d3e99ad5ae5c8c56ca48099) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “self-assessed”
- Review notes: “Compilation checks, including warning-fatal builds, are distinct from complete transitive standard-axiom verification, including private and generated declarations. Neither schema validation nor this self-assessment constitutes independent mathematical review, rights assessment or certification of a particular revision or its publication status.”
- Automation: agent; framework “Codex CLI (Formal Frontier Hive), Lean 4 and mathlib”; tool setup “AI agents using Codex CLI, Lean 4 and mathlib developed the mathematical library, checked clients, metadata, bottom/simplification work and the doc-gen4 Markdown adapter. Beacon assembled the original modules, notices and corrections; Folio contributed headline exposition. Exact model versions and total costs were not recorded here.”
- Automation notes: “Formal Frontier Agents is the collective formalization credit. Beacon is an AI-agent contributor, not a separately identified human author. Beacon's original modules, other AI-agent client/metadata/bottom and documentation contributions, Folio's headline exposition and the adapter's Root Stability/Anchor Ideal recipe lineage are credited in README.md and docs/README.md. Apache notices, collective credit and genuine third-party attribution are preserved; the collective author credit does not identify a copyright holder. The generated API includes displayed Lean signatures and project docstrings, not external book text.”

## Scope

Reusable supernatural-number arithmetic, finite-quotient profinite order and closed-subgroup index, their tower law, and torsion-character comparison under the hypotheses declared in Lean. This metadata does not assert complete source coverage or certify any particular release snapshot.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/formalization.yaml) of [FormalFrontier/supernatural-numbers](https://github.com/FormalFrontier/supernatural-numbers) at commit [cb444a40](https://github.com/FormalFrontier/supernatural-numbers/tree/cb444a4051e593328d3e99ad5ae5c8c56ca48099), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Cohomology of Number Fields*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Corrected second edition, version 2.3 (May 2020), Definitions (1.1.5)--(1.1.6) and the following consequences (book; adapts).

## Builds on

- [Group theory](../group-theory/README.md) (a Lake dependency, pinned at 3e8a081e)


## Headline results

**Arithmetic with arbitrary prime exponents.** A supernatural number has an
`ℕ∞` exponent at every prime, without a finite-support restriction.
Multiplication adds exponents and divisibility is pointwise order; the
complete-lattice bottom is one. Infinite `iProd` uses suprema of exponent
sums over finite subfamilies of a `Type`-indexed family, whereas `iSup` and
`iInf` accept arbitrary `Sort` indices. The positive-natural `ofPNat` and
explicit all-natural `ofNat` preserve multiplication and reflect
divisibility; `ofNat 0 = ⊤` and neither map installs a numeral coercion.
[`iSup_ofNat_dvd_iff`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/NatEmbedding.lean#L129)
characterizes the supernatural least common multiple of a `Sort`-indexed
natural-number family, including empty-family and zero cases. See
[Basic](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Basic.lean) and
[NatEmbedding](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/NatEmbedding.lean).

**The closed-subgroup index tower law.** The supernatural
[`profiniteOrder`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Order.lean#L34) and
[`profiniteIndex`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Order.lean#L43) use finite quotients
of a profinite group. For closed subgroups `N ≤ H` of the **same** ambient
profinite group,
[`profiniteIndex_tower`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Tower.lean#L306) proves
`[G : N] = [G : H] * [H : N]`, taking the relative index in `H` via
`closedSubgroupWithin H N hNH`. Normality is not required, but closedness
and the common profinite ambient group are.

**Torsion and character orders.** For an additive abelian group `A` with
`IsAddTorsion A`,
[`characterEquivProfiniteCharacter`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Characters.lean#L355)
identifies its rational-circle-valued characters with the additive group
underlying its profinite character group; the
[`torsionOrder_eq_profiniteOrder_character`](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbers/Characters.lean#L404)
theorem equates their supernatural orders. The topology-free wrapper gives
`A` the discrete topology; the lower-level Pontryagin interface requires
explicit topological assumptions. These noncomputable constructions make
no nontorsion or general Pontryagin-duality claim.

Mathlib supplies prime-factorization, finite/profinite-group and Pontryagin
infrastructure; this library supplies the supernatural arithmetic and bridges.
The released `groupTheory` library supplies the canonical rational-circle
inclusions and finite-order preimages through
`GroupTheory.Topology.RationalCircle`, following their original formalization
in this library. Publicly importing `SupernaturalNumbers` also exposes these
declarations. Use `AddCircle.rationalToReal`, `AddCircle.rationalToCircle`,
`AddCircle.exists_rational_preimage_of_isOfFinAddOrder` and
`Circle.exists_rational_preimage_of_isOfFinOrder` in new code. The seven former
`Supernatural` names in `Characters` remain deprecated aliases from
October 7, 2026, retained for at least three months. Group Theory's
open-kernel comparison for compact groups is distinct from this library's
discrete torsion-group character equivalence.
See the [API reference](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/docs/API.md) and
[checked finite and infinite examples](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbersTests/ReleaseClients.lean),
as well as [rational-circle clients](https://github.com/FormalFrontier/supernatural-numbers/blob/cb444a4051e593328d3e99ad5ae5c8c56ca48099/SupernaturalNumbersTests/RationalCircle.lean).
