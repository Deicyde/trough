---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_arrow, SimpleGraph.lt_ramseyNumber_of_choose_lt
statement: formalized
proof: formalized
---

# Finite-colour Ramsey theory

> Finite-colour graph Ramsey theory on Mathlib edge labelings, with a common arrow relation and least-host numbers. Proves finite graph and infinite uniform existence, binomial upper and counting lower bounds, and transitive tournament bounds. Derives Schur triples as an application. Supplies colour-class induced-copy, ordered and hypergraph interfaces; the colour-class and hypergraph specifications retain explicit existence hypotheses.

*Quoted from the card [LeanPool/projects/finite-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-ramsey.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SimpleGraph.exists_arrow`](https://leanpool.github.io/lean-pool/LeanPool/FiniteRamsey/RamseyNumber.html#SimpleGraph.exists_arrow) (theorem; a main declaration), declared in [LeanPool/FiniteRamsey/RamseyNumber.lean, line 62](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FiniteRamsey/RamseyNumber.lean#L62): “Every family of finite target graphs indexed by a finite colour type is arrowed by some finite complete host.” Its source, as the card gives it: “Upstream lean-ramsey at ae8c9d97bae6d963a925754f8e2374f1c1b14587; proposed in \#721 on 2026-10-27T10:39:24Z.”
- [`SimpleGraph.lt_ramseyNumber_of_choose_lt`](https://leanpool.github.io/lean-pool/LeanPool/FiniteRamsey/RamseyLowerBound.html#SimpleGraph.lt_ramseyNumber_of_choose_lt) (theorem; a main declaration), declared in [LeanPool/FiniteRamsey/RamseyLowerBound.lean, line 208](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FiniteRamsey/RamseyLowerBound.lean#L208): “The first-moment counting inequality gives a strict lower bound for the diagonal Ramsey number.” Its source, as the card gives it: “Upstream lean-ramsey at ae8c9d97bae6d963a925754f8e2374f1c1b14587; proposed in \#721 on 2026-10-27T10:39:24Z.”

## Project

- Authors: Brian Sanders.
- Source: *Finite-colour Ramsey theory* by Brian Sanders.
- Project repository: [Egly443/lean-ramsey](https://github.com/Egly443/lean-ramsey), at commit [ae8c9d97](https://github.com/Egly443/lean-ramsey/tree/ae8c9d97bae6d963a925754f8e2374f1c1b14587).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C55, 05D10.
- In Lean Pool: [LeanPool/FiniteRamsey](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FiniteRamsey), from the card [LeanPool/projects/finite-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-ramsey.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/finite-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/finite-ramsey.yaml)
- [Lean Pool at 307e3125: LeanPool/FiniteRamsey](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FiniteRamsey)
