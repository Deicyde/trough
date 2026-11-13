---
declaration: theorem
origin: cited
lean: Erdos137.erdos137_finite, Erdos137.erdos137_eventually_not_powerful
statement: formalized
proof: formalized
---

# Erdős Problem \#137: powerful products of consecutive integers

> Formalizes the abc-conditional finiteness results for Erdős Problem \#137 (Erdős–Selfridge): a number N is powerful if every prime dividing N has its square dividing N, and the question is whether the product F(k,n) = n(n+1)⋯(n+k-1) of k ≥ 3 consecutive integers can be powerful for infinitely many n. Each route isolates its abc input (a radical lower bound) as a single explicit hypothesis and proves everything else outright, concluding that, conditionally, F(k,n) is powerful for only finitely many n for each fixed k ≥ 3.

*Quoted from the card [LeanPool/projects/erdos137.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos137.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Erdos137.erdos137_finite`](https://leanpool.github.io/lean-pool/LeanPool/Erdos137/Finiteness.html#Erdos137.erdos137_finite) (theorem; a main declaration), declared in [LeanPool/Erdos137/Finiteness.lean, line 254](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137/Finiteness.lean#L254): “Under the Granville–Langevin radical bound RadLB k (an abc-conditional hypothesis) and k ≥ 3, the set of n ≥ 1 for which F(k,n) is powerful is finite.”
- [`Erdos137.erdos137_eventually_not_powerful`](https://leanpool.github.io/lean-pool/LeanPool/Erdos137/Finiteness.html#Erdos137.erdos137_eventually_not_powerful) (theorem; a main declaration), declared in [LeanPool/Erdos137/Finiteness.lean, line 178](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137/Finiteness.lean#L178): “Under RadLB k and k ≥ 3, there is a threshold beyond which F(k,n) is never powerful.”
- [`Erdos137.lemma_star`](https://leanpool.github.io/lean-pool/LeanPool/Erdos137/Finiteness.html#Erdos137.lemma_star) (theorem), declared in [LeanPool/Erdos137/Finiteness.lean, line 104](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137/Finiteness.lean#L104): “Unconditionally, the radical squared times the powerful part of m is at most m squared (rad m ^ 2 \* B2 m ≤ m ^ 2).”
- [`Erdos137.powerful_rad_sq_le`](https://leanpool.github.io/lean-pool/LeanPool/Erdos137/Finiteness.html#Erdos137.powerful_rad_sq_le) (theorem), declared in [LeanPool/Erdos137/Finiteness.lean, line 169](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137/Finiteness.lean#L169): “A nonzero powerful number N satisfies rad N ^ 2 ≤ N.”

## Project

- Authors: Scott D. Hughes.
- Source: *Erdős Problem \#137: powerful products of consecutive integers* by Scott D. Hughes, [https://www.erdosproblems.com/137](https://www.erdosproblems.com/137).
- Project repository: [scottdhughes/erdos137](https://github.com/scottdhughes/erdos137).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11A51, 11N25.
- In Lean Pool: [LeanPool/Erdos137](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137), from the card [LeanPool/projects/erdos137.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos137.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/erdos137.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos137.yaml)
- [Lean Pool at 701389c0: LeanPool/Erdos137](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos137)
