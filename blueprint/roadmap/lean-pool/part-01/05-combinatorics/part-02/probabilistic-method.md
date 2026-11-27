---
declaration: theorem
origin: cited
lean: Finset.prod_one_sub_le_weightProb_forall_not, Finset.exists_forall_not_of_symmetric_lll, SimpleGraph.exists_dependentRandomChoice, SimpleGraph.exists_dependentRandomChoice_of_card_edgeFinset, SimpleGraph.exists_large_cliqueFree_of_deletion
statement: formalized
proof: formalized
---

# The finite probabilistic method for graphs

> Finite, counting-based tools of the probabilistic method. Proves a quantitative asymmetric Lovász Local Lemma under lopsided dependence for arbitrary nonnegative weights of total one on a finite sample set, its p-biased-cube and symmetric corollaries for events determined by coordinate sets, dependent random choice in degree-moment and Fox–Sudakov average-degree forms, and first-moment and deletion bounds for cliques and independent sets of G(n, p). For a finite coordinate set in a countable type, and for a finite vertex type, it identifies the counting probability with Mathlib's setBer(U, p) and binomial random graph G(V, p).

*Quoted from the card [LeanPool/projects/probabilistic-method.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/probabilistic-method.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Finset.prod_one_sub_le_weightProb_forall_not`](https://leanpool.github.io/lean-pool/LeanPool/ProbabilisticMethod/LocalLemma.html#Finset.prod_one_sub_le_weightProb_forall_not) (theorem; a main declaration), declared in [LeanPool/ProbabilisticMethod/LocalLemma.lean, line 262](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod/LocalLemma.lean#L262): “Let w be nonnegative weights of total one on a finite set Ω, and let events E i, i ∈ I, satisfy the lopsided hypothesis that P(E i and no E j, j ∈ S) ≤ P(E i) P(no E j, j ∈ S) for every S ⊆ I avoiding i and Γ i. If 0 ≤ x ≤ 1 and P(E i) ≤ x i ∏ j ∈ Γ i, (1 - x j) for i ∈ I, then the probability that no E i occurs is at least ∏ i ∈ I, (1 - x i).” Its source, as the card gives it: “Upstream LocalLemma.lean at 841e3042ef057564ae3cbd2322e0f369bbf64d34. A finite-weight, lopsided variant of the quantitative asymmetric Local Lemma (Alon–Spencer, The probabilistic method, Lemma 5.1.1, which states the product lower bound); the lopsided dependence condition is that of Erdős–Spencer (1991), who state a symmetric positive-probability form.”
- [`Finset.exists_forall_not_of_symmetric_lll`](https://leanpool.github.io/lean-pool/LeanPool/ProbabilisticMethod/LocalLemma.html#Finset.exists_forall_not_of_symmetric_lll) (theorem; a main declaration), declared in [LeanPool/ProbabilisticMethod/LocalLemma.lean, line 342](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod/LocalLemma.lean#L342): “On the p-biased cube of a finite subset U of a type α, with 0 ≤ p ≤ 1, let each event E i be determined by coordinates T i ⊆ U, meaning E i A ↔ E i B whenever A ∩ T i = B ∩ T i for all finite subsets A, B of α (not only subsets of U). If each P(E i) ≤ q, each T i meets T j for at most d other indices j ∈ I, and e q (d + 1) ≤ 1, some subset of U avoids every E i.” Its source, as the card gives it: “Upstream LocalLemma.lean at 841e3042ef057564ae3cbd2322e0f369bbf64d34; symmetric Local Lemma with the e p (d + 1) ≤ 1 criterion as in Alon–Spencer, The probabilistic method, Corollary 5.1.2, for events on independent biased coordinates.”
- [`SimpleGraph.exists_dependentRandomChoice`](https://leanpool.github.io/lean-pool/LeanPool/ProbabilisticMethod/DependentRandomChoice.html#SimpleGraph.exists_dependentRandomChoice) (theorem; a main declaration), declared in [LeanPool/ProbabilisticMethod/DependentRandomChoice.lean, line 141](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod/DependentRandomChoice.lean#L141): “For a graph on a finite nonempty vertex set of size n and r ≥ 1, if a n ^ t + C(n, r) m ^ t ≤ ∑ v, deg v ^ t, there is a vertex set W with at least a elements in which every r-element subset has at least m common neighbours.” Its source, as the card gives it: “Upstream DependentRandomChoice.lean at 841e3042ef057564ae3cbd2322e0f369bbf64d34. A degree-moment refinement: the hypothesis keeps the moment ∑ v, deg v ^ t computed in the proof of Fox–Sudakov, Dependent random choice (2011), Lemma 2.1, before Jensen's inequality.”
- [`SimpleGraph.exists_dependentRandomChoice_of_card_edgeFinset`](https://leanpool.github.io/lean-pool/LeanPool/ProbabilisticMethod/DependentRandomChoice.html#SimpleGraph.exists_dependentRandomChoice_of_card_edgeFinset) (theorem; a main declaration), declared in [LeanPool/ProbabilisticMethod/DependentRandomChoice.lean, line 178](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod/DependentRandomChoice.lean#L178): “For a graph on a finite nonempty vertex set of size n with e edges, average degree d = 2e / n and r ≥ 1, if a + C(n, r) (m / n) ^ t ≤ n (d / n) ^ t, there is a vertex set W with at least a elements in which every r-element subset has at least m common neighbours.” Its source, as the card gives it: “Upstream DependentRandomChoice.lean at 841e3042ef057564ae3cbd2322e0f369bbf64d34; Fox–Sudakov, Dependent random choice (2011), Lemma 2.1, whose condition n ^ (1 - t) d ^ t - C(n, r) (m / n) ^ t ≥ a is the same inequality.”
- [`SimpleGraph.exists_large_cliqueFree_of_deletion`](https://leanpool.github.io/lean-pool/LeanPool/ProbabilisticMethod/RandomGraph.html#SimpleGraph.exists_large_cliqueFree_of_deletion) (theorem; a main declaration), declared in [LeanPool/ProbabilisticMethod/RandomGraph.lean, line 185](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod/RandomGraph.lean#L185): “For 0 ≤ p ≤ 1 and k, l ≥ 1, some graph G on n vertices has a vertex set t of size at least n - C(n, k) p ^ C(k, 2) - C(n, l) (1 - p) ^ C(l, 2) such that no k-clique of G and no l-clique of its complement lies inside t.” Its source, as the card gives it: “Upstream RandomGraph.lean at 841e3042ef057564ae3cbd2322e0f369bbf64d34; deletion method for off-diagonal Ramsey numbers as in Alon–Spencer, The probabilistic method, Section 3.1.”

## Project

- Authors: Brian Sanders.
- Source: *The finite probabilistic method for graphs* by Brian Sanders.
- Project repository: [Egly443/lean-probabilistic-method](https://github.com/Egly443/lean-probabilistic-method), at commit [841e3042](https://github.com/Egly443/lean-probabilistic-method/tree/841e3042ef057564ae3cbd2322e0f369bbf64d34).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D40, 05C80, 60C05.
- In Lean Pool: [LeanPool/ProbabilisticMethod](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod), from the card [LeanPool/projects/probabilistic-method.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/probabilistic-method.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/probabilistic-method.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/probabilistic-method.yaml)
- [Lean Pool at bb99e52c: LeanPool/ProbabilisticMethod](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ProbabilisticMethod)
