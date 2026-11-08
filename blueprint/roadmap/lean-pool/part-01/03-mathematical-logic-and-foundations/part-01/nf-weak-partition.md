---
declaration: theorem
origin: cited
lean: NFChoice.Foundation.NFStandard.NF_proves_not_WPP
statement: formalized
proof: formalized
---

# New Foundations refutes the Weak Partition Principle

> Constructs a formal first-order derivation of the negation of the Weak Partition Principle from New Foundations, with extensionality and the full integer-stratified comprehension schema. Proves full deductive equivalence with Metamath's Hailperin-derived finite presentation, including its added singleton axiom. Replays the source proof through nominal syntax, explicit freshness certificates, and a de Bruijn calculus. Includes reusable first-order soundness and completeness, stratification, lowering, and proof-translation infrastructure. This is a derivability theorem; it does not assert the consistency of New Foundations.

*Quoted from the card [LeanPool/projects/nf-weak-partition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nf-weak-partition.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`NFChoice.Foundation.NFStandard.NF_proves_not_WPP`](https://leanpool.github.io/lean-pool/LeanPool/NFWeakPartition/NFStandard/NotWPP.html#NFChoice.Foundation.NFStandard.NF_proves_not_WPP) (theorem; a main declaration), declared in [LeanPool/NFWeakPartition/NFStandard/NotWPP.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NFWeakPartition/NFStandard/NotWPP.lean#L27): “Standard New Foundations formally derives the negation of WPP. WPP says that, for all sets x and y, if a function maps y onto x and an injective function maps y into x, then an injective function maps x into y.” Its source, as the card gives it: “Upstream Proof/NFStandard/NotWPP.lean and the exact source formulation documented in README.md at the pinned commit. Standard-NF completion: commit a9f9867ee379835f91a4f05f9c4a352d44ca1775, 2026-08-25 00:16:27 UTC. Palomar registration PALOMAR-2026-08-27-000005 is dated 2026-08-27, without a verified time of day. The responsible public maintainer is Elliot Glazer. Upstream Flypitch4 credits Ian Klatzco and Claude for its Lean 4 port; this import also includes AI-assisted porting and proof repairs, hence mixed provenance. The deterministic Metamath replay is not by itself evidence of AI mathematical authorship. Independent novelty is not claimed by this card.”
- [`NFChoice.Foundation.NFStandard.nf_hailperin_deductivelyEquivalent`](https://leanpool.github.io/lean-pool/LeanPool/NFWeakPartition/NFStandard/Equivalence.html#NFChoice.Foundation.NFStandard.nf_hailperin_deductivelyEquivalent) (theorem), declared in [LeanPool/NFWeakPartition/NFStandard/Equivalence.lean, line 68](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NFWeakPartition/NFStandard/Equivalence.lean#L68): “Extensionality together with every integer-stratified comprehension instance and Metamath's Hailperin-derived finite first-order presentation, including its added singleton axiom, derive exactly the same sentences.” Its source, as the card gives it: “Upstream Proof/NFStandard/Equivalence.lean at the pinned commit. Metamath's ax-sn entry credits the singleton addition to SF on 2015-01-12 and distinguishes it from Hailperin's original presentation: https://us.metamath.org/nfeuni/ax-sn.html.”

## Project

- Authors: Elliot Glazer, NFNotWPP contributors, Jesse Michael Han, Floris van Doorn, Ian Klatzco.
- Source: *NF proves not-WPP, source-complete Lean formalization*, [https://github.com/elliotglazer/nf-not-wpp/tree/fa58a7a895a73422042e167391c78e9149979913](https://github.com/elliotglazer/nf-not-wpp/tree/fa58a7a895a73422042e167391c78e9149979913).
- Project repository: [elliotglazer/nf-not-wpp](https://github.com/elliotglazer/nf-not-wpp), at commit [fa58a7a8](https://github.com/elliotglazer/nf-not-wpp/tree/fa58a7a895a73422042e167391c78e9149979913).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03E70, 03B35.
- In Lean Pool: [LeanPool/NFWeakPartition](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NFWeakPartition), from the card [LeanPool/projects/nf-weak-partition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nf-weak-partition.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nf-weak-partition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nf-weak-partition.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NFWeakPartition](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NFWeakPartition)
