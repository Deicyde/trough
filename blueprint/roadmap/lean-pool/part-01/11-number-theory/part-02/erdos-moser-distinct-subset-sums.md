---
declaration: theorem
origin: cited
lean: LeanPool.ErdosMoser.leoMoserVarianceBound
statement: formalized
proof: formalized
---

# Leo Moser's finite distinct-subset-sums inequality

> Formalizes the exact finite sum-of-squares inequality that Guy's 1982 account states as Theorem 2 and attributes to Leo Moser: a finite set A of natural numbers with distinct subset sums satisfies 4^|A| - 1 <= 3 \* sum(a^2). It then derives direct and square-root lower bounds for the largest element of A. This does not claim the stronger historical asymptotic bound attributed jointly to Erdős and Moser, and Erdős Problem 1 remains open.

*Quoted from the card [LeanPool/projects/erdos-moser-distinct-subset-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos-moser-distinct-subset-sums.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.ErdosMoser.leoMoserVarianceBound`](https://leanpool.github.io/lean-pool/LeanPool/ErdosMoser/SubsetSums.html#LeanPool.ErdosMoser.leoMoserVarianceBound) (theorem; a main declaration), declared in [LeanPool/ErdosMoser/SubsetSums.lean, line 129](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosMoser/SubsetSums.lean#L129): “If a finite set A of natural numbers has distinct subset sums, then 4^|A| - 1 is at most three times the sum of the squares of the elements of A.” Its source, as the card gives it: “Richard K. Guy, "Sets of Integers Whose Subsets Have Distinct Sums," Theorem 2 (credited there to Leo Moser), Annals of Discrete Mathematics 12 (1982), 141-154, doi:10.1016/S0304-0208(08)73500-X.”
- [`LeanPool.ErdosMoser.erdosMoserMaxBound`](https://leanpool.github.io/lean-pool/LeanPool/ErdosMoser/Bounds.html#LeanPool.ErdosMoser.erdosMoserMaxBound) (theorem), declared in [LeanPool/ErdosMoser/Bounds.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosMoser/Bounds.lean#L28): “For a nonempty finite set A of natural numbers with distinct subset sums, 4^|A| - 1 is at most 3|A| times the square of its largest element.”
- [`LeanPool.ErdosMoser.erdosMoserMaxSqrt`](https://leanpool.github.io/lean-pool/LeanPool/ErdosMoser/Bounds.html#LeanPool.ErdosMoser.erdosMoserMaxSqrt) (theorem), declared in [LeanPool/ErdosMoser/Bounds.lean, line 47](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosMoser/Bounds.lean#L47): “The equivalent square-root lower bound on the largest element: sqrt((4^|A| - 1)/(3|A|)) is at most max(A).”

## Project

- Authors: Egor Lyfar.
- Source: *Sets of Integers Whose Subsets Have Distinct Sums* by Richard K. Guy, [doi:10.1016/S0304-0208(08)73500-X](https://doi.org/10.1016/S0304-0208%2808%2973500-X), [https://www.erdosproblems.com/1](https://www.erdosproblems.com/1).
- Project repository: [lyfar/erdos-moser-distinct-subset-sums-lean](https://github.com/lyfar/erdos-moser-distinct-subset-sums-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11B13, 11B75.
- In Lean Pool: [LeanPool/ErdosMoser](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosMoser), from the card [LeanPool/projects/erdos-moser-distinct-subset-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos-moser-distinct-subset-sums.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos-moser-distinct-subset-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos-moser-distinct-subset-sums.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ErdosMoser](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosMoser)
