---
declaration: theorem
origin: cited
lean: SimpleGraph.goodman_within, SimpleGraph.goodman_bound, SimpleGraph.IsRegularOfDegree.goodman_eq, SimpleGraph.supersaturation, SimpleGraph.choose_le_card_cliqueFinset_add_mul_choose_ramseyNumber
statement: formalized
proof: formalized
---

# Goodman's formula and clique supersaturation for two-colourings

> Counts monochromatic structures in a red/blue colouring of a complete graph, given as a `SimpleGraph` and its complement. Proves Goodman's formula for monochromatic triangles, inside any finite vertex set and globally, with its degree-imbalance form, the bound n(n-1)(n-5)/24, equality for graphs regular of degree k on 2k+1 vertices, and the stronger bound n(n-2)(n-4)/24 for even n. Also proves monochromatic books, an edge-balance inequality, supersaturation of monochromatic cliques by averaging (made unconditional at the diagonal Ramsey number of the pool's FiniteRamsey project), and a counted Erdős–Szekeres recursion giving explicit lower bounds on the number of red k-cliques or blue l-cliques.

*Quoted from the card [LeanPool/projects/goodman-supersaturation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/goodman-supersaturation.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SimpleGraph.goodman_within`](https://leanpool.github.io/lean-pool/LeanPool/GoodmanSupersaturation/Goodman.html#SimpleGraph.goodman_within) (theorem; a main declaration), declared in [LeanPool/GoodmanSupersaturation/Goodman.lean, line 272](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation/Goodman.lean#L272): “Goodman's formula inside any finite vertex set S. Twice the number of triangles of G and of its complement inside S, plus the number of mixed wedges (the sum over v in S of the red degree times the blue degree of v within S), equals 2 C(|S|, 3).”
- [`SimpleGraph.goodman_bound`](https://leanpool.github.io/lean-pool/LeanPool/GoodmanSupersaturation/Goodman.html#SimpleGraph.goodman_bound) (theorem; a main declaration), declared in [LeanPool/GoodmanSupersaturation/Goodman.lean, line 406](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation/Goodman.lean#L406): “Goodman's bound. For a finite vertex type of size n, n(n-1)(n-5) is at most 24 times the number of triangles of G plus the number of triangles of its complement (natural-number subtraction, so the statement is trivial for n < 5).”
- [`SimpleGraph.IsRegularOfDegree.goodman_eq`](https://leanpool.github.io/lean-pool/LeanPool/GoodmanSupersaturation/Goodman.html#SimpleGraph.IsRegularOfDegree.goodman_eq) (theorem; a main declaration), declared in [LeanPool/GoodmanSupersaturation/Goodman.lean, line 435](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation/Goodman.lean#L435): “Sharpness. If G is regular of degree k on 2k+1 vertices, then 24 times the number of monochromatic triangles equals n(n-1)(n-5) exactly (over the integers).”
- [`SimpleGraph.supersaturation`](https://leanpool.github.io/lean-pool/LeanPool/GoodmanSupersaturation/Supersaturation.html#SimpleGraph.supersaturation) (theorem; a main declaration), declared in [LeanPool/GoodmanSupersaturation/Supersaturation.lean, line 396](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation/Supersaturation.lean#L396): “Counted Erdős–Szekeres recursion. For k, l at least 1 with k + l at least 3 and a finite vertex set S with x = |S| + 1 - 2^(k+l-3) > 0, either G has at least supersaturationBound k l x k-cliques inside S or its complement has at least supersaturationBound l k x l-cliques inside S, where supersaturationBound k l x = x^k 2^(2k+1) / (k! 2^(kl + C(k+1, 2))).”
- [`SimpleGraph.choose_le_card_cliqueFinset_add_mul_choose_ramseyNumber`](https://leanpool.github.io/lean-pool/LeanPool/GoodmanSupersaturation/RamseyNumber.html#SimpleGraph.choose_le_card_cliqueFinset_add_mul_choose_ramseyNumber) (theorem; a main declaration), declared in [LeanPool/GoodmanSupersaturation/RamseyNumber.lean, line 45](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation/RamseyNumber.lean#L45): “Supersaturation by averaging at the diagonal Ramsey number. If R(t, t) is at most n, then C(n, t) is at most C(R(t, t), t) times the number of t-cliques of G plus those of its complement. R(t, t) is the pool's FiniteRamsey ramseyNumber ![t, t]; this bridge was added in the port.”

## Project

- Authors: Brian Sanders.
- Source: *Goodman's formula and supersaturation for two-colourings* by Brian Sanders.
- Project repository: [Egly443/lean-goodman-supersaturation](https://github.com/Egly443/lean-goodman-supersaturation), at commit [6c32aa44](https://github.com/Egly443/lean-goodman-supersaturation/tree/6c32aa44315c4627ceff231bd15c8d48fa4bf2e7).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C55, 05C35, 05D10.
- In Lean Pool: [LeanPool/GoodmanSupersaturation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation), from the card [LeanPool/projects/goodman-supersaturation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/goodman-supersaturation.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/goodman-supersaturation.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/goodman-supersaturation.yaml)
- [Lean Pool at bb99e52c: LeanPool/GoodmanSupersaturation](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GoodmanSupersaturation)
