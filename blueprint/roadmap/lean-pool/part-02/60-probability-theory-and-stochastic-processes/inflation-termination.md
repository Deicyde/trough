---
declaration: theorem
origin: cited
lean: TriangleInflation.Graph.classification_NW
statement: formalized
proof: formalized
---

# Inflation termination for classical pair-source networks

> For finite binary pair-source networks without isolated vertices, classifies when the inflation hierarchy characterizes compatibility with finite latent alphabets: precisely forests of double stars, where order two suffices. Also proves triangle nontermination for arbitrary measurable latent probability spaces, quantitative obstructions, finite and measurable Finner inequalities, and graph witnesses.

*Quoted from the card [LeanPool/projects/inflation-termination.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/inflation-termination.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`TriangleInflation.Graph.classification_NW`](https://leanpool.github.io/lean-pool/LeanPool/InflationTermination/PalomarSolutions/TriangleInflationClassification.html#TriangleInflation.Graph.classification_NW) (theorem; a main declaration), declared in [LeanPool/InflationTermination/PalomarSolutions/TriangleInflationClassification.lean, line 45](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/InflationTermination/PalomarSolutions/TriangleInflationClassification.lean#L45): “For finite binary pair-source graphs without isolated vertices, some finite order of the Navascués–Wolfe hierarchy characterizes compatibility with finite latent alphabets exactly for double-star forests; order two suffices there.”
- [`TriangleInflation.no_finite_characterizing_orderM`](https://leanpool.github.io/lean-pool/LeanPool/InflationTermination/TriangleInflation/FinnerMeasure.html#TriangleInflation.no_finite_characterizing_orderM) (theorem), declared in [LeanPool/InflationTermination/TriangleInflation/FinnerMeasure.lean, line 635](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/InflationTermination/TriangleInflation/FinnerMeasure.lean#L635): “At every positive inflation order, a triangle law passes both the AI and NW tests but has no compatible model over any measurable latent probability spaces.”

## Project

- Authors: William Blair.
- Project repository: [williamjblair/inflation-termination](https://github.com/williamjblair/inflation-termination), at commit [2aa1f05c](https://github.com/williamjblair/inflation-termination/tree/2aa1f05ce932fdeef3896c83d287abd77cd8befb).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 60A05, 05C05.
- In Lean Pool: [LeanPool/InflationTermination](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/InflationTermination), from the card [LeanPool/projects/inflation-termination.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/inflation-termination.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/inflation-termination.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/inflation-termination.yaml)
- [Lean Pool at 701389c0: LeanPool/InflationTermination](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/InflationTermination)
