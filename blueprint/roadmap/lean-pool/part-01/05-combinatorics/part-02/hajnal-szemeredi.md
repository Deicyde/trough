---
declaration: theorem
origin: cited
lean: HajnalSzemeredi.hajnalSzemeredi, HajnalSzemeredi.hajnalSzemeredi_exact
statement: formalized
proof: formalized
---

# The Hajnal–Szemerédi theorem on equitable vertex colourings

> Every finite simple graph of maximum degree at most r admits a proper colouring with r + 1 colours whose class sizes differ by at most one. When the vertex count is s(r + 1), every class can have exactly s vertices. The proof follows the Kierstead–Kostochka argument, preserving finite-subgraph and arbitrary-palette recolouring, reachability, terminal-class and discharging infrastructure. The polynomial-time algorithm from Section 3 is outside the imported scope.

*Quoted from the card [LeanPool/projects/hajnal-szemeredi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hajnal-szemeredi.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`HajnalSzemeredi.hajnalSzemeredi`](https://leanpool.github.io/lean-pool/LeanPool/HajnalSzemeredi/Final.html#HajnalSzemeredi.hajnalSzemeredi) (theorem; a main declaration), declared in [LeanPool/HajnalSzemeredi/Final.lean, line 88](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HajnalSzemeredi/Final.lean#L88): “Every finite simple graph whose vertex degrees are at most r has a proper colouring by Fin (r + 1) such that the size of any colour class is at most the size of any other colour class plus one.”
- [`HajnalSzemeredi.hajnalSzemeredi_exact`](https://leanpool.github.io/lean-pool/LeanPool/HajnalSzemeredi/Final.html#HajnalSzemeredi.hajnalSzemeredi_exact) (theorem; a main declaration), declared in [LeanPool/HajnalSzemeredi/Final.lean, line 49](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HajnalSzemeredi/Final.lean#L49): “If a finite simple graph has s(r + 1) vertices and every vertex degree is at most r, it has a proper colouring by Fin (r + 1) with every class of size s.”
- [`HajnalSzemeredi.core`](https://leanpool.github.io/lean-pool/LeanPool/HajnalSzemeredi/Main.html#HajnalSzemeredi.core) (theorem), declared in [LeanPool/HajnalSzemeredi/Main.lean, line 168](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HajnalSzemeredi/Main.lean#L168): “For any finite vertex subset S and finite natural-number palette P of size r + 1, if S has s(r + 1) vertices and every vertex has at most r neighbours within S, there is a proper colouring of S in P with all classes of size s.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *A short proof of the Hajnal–Szemerédi theorem on equitable colouring* by H. A. Kierstead, A. V. Kostochka, [doi:10.1017/S0963548307008619](https://doi.org/10.1017/S0963548307008619).
- Project repository: [jtraverso/hajnal-szemeredi](https://github.com/jtraverso/hajnal-szemeredi), at commit [ba34061e](https://github.com/jtraverso/hajnal-szemeredi/tree/ba34061e3cf12dfc8297610d5d7b3f0afac7ec54).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15, 05C35.
- In Lean Pool: [LeanPool/HajnalSzemeredi](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HajnalSzemeredi), from the card [LeanPool/projects/hajnal-szemeredi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hajnal-szemeredi.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/hajnal-szemeredi.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hajnal-szemeredi.yaml)
- [Lean Pool at 701389c0: LeanPool/HajnalSzemeredi](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HajnalSzemeredi)
