---
declaration: theorem
origin: cited
lean: RunsOfMultiples.main_theorem, RunsOfMultiples.main_theorem_alt
statement: formalized
proof: formalized
---

# Sharp asymptotic bounds for runs of multiples in finite sets

> For a finite set S of n positive integers, let k(S,a) be the least positive integer k for which k\*a is outside S. Proves an upper bound for every such S and a matching positive lower bound attained by some set of every sufficiently large cardinality n, establishing the extremal order n log n log log n. Contains entropy and chain-compression upper bounds and two lower-bound constructions, sharing definitions, prime estimates and padding. Preserves prime-weighted entropy estimates, smooth-number constructions and abstract cardinality-preserving compression lemmas.

*Quoted from the card [LeanPool/projects/runs-of-multiples.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/runs-of-multiples.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RunsOfMultiples.main_theorem`](https://leanpool.github.io/lean-pool/LeanPool/RunsOfMultiples/Main.html#RunsOfMultiples.main_theorem) (theorem; a main declaration), declared in [LeanPool/RunsOfMultiples/Main.lean, line 32](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RunsOfMultiples/Main.lean#L32): “Every sufficiently large finite set S of positive integers has sum of its first missing multiple indices at most C\*n\*log(n)\*log(log(n)); for every sufficiently large n, a set of exactly n positive integers attains at least c\*n\*log(n)\*log(log(n)), for a fixed c>0. This proof uses entropy and smooth numbers.”
- [`RunsOfMultiples.main_theorem_alt`](https://leanpool.github.io/lean-pool/LeanPool/RunsOfMultiples/Alt/Main.html#RunsOfMultiples.main_theorem_alt) (theorem; a main declaration), declared in [LeanPool/RunsOfMultiples/Alt/Main.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RunsOfMultiples/Alt/Main.lean#L27): “The identical sharp asymptotic statement, proved using compression to divisor-closed, prime-shift-closed sets and a box-times-simplex construction.”

## Project

- Authors: Jason Hoelscher-Obermaier, Claude Opus 5.5 (Lean proofs).
- Source: *Runs of multiples in a finite set of integers* by Claude Opus 5.5 (AI; published by Jason Hoelscher-Obermaier), [https://github.com/jas-ho/runs-of-multiples-lean/blob/8b7e5f23534c321722725f78b6e64981557f0ef5/docs/runs-of-multiples.pdf](https://github.com/jas-ho/runs-of-multiples-lean/blob/8b7e5f23534c321722725f78b6e64981557f0ef5/docs/runs-of-multiples.pdf).
- Project repository: [jas-ho/runs-of-multiples-lean](https://github.com/jas-ho/runs-of-multiples-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11N25, 11B75, 05D05.
- In Lean Pool: [LeanPool/RunsOfMultiples](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RunsOfMultiples), from the card [LeanPool/projects/runs-of-multiples.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/runs-of-multiples.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/runs-of-multiples.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/runs-of-multiples.yaml)
- [Lean Pool at 701389c0: LeanPool/RunsOfMultiples](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RunsOfMultiples)
