---
declaration: theorem
origin: cited
lean: RS.regts_sevenster_characterisation
statement: formalized
proof: formalized
---

# A proof of the Regts–Sevenster conjecture, formalized

> A Lean 4 proof of the Regts–Sevenster conjecture. A complex-valued graph parameter, normalized at the empty graph and invariant under isomorphism, has exponentially bounded edge-connection rank if and only if it is a mixed partition function. For a natural rank base R, a representing model can be chosen with k even and 2ℓ odd colours satisfying k + 2ℓ ≤ R. The development also proves the even connection-rank growth limit, minimum total colour dimension, minimal parity formulas and prescribed-dimension criterion. Schrijver's factorial argument supplies nilpotent-trace vanishing; semisimplicity and Deligne's fibre-functor theorem give the model; a polynomial commutant estimate gives the sharp colour budget. Deligne's theorem and the required symmetric-group character theory are proved within the development. The appendix's trace-zeta results give rationality and degree bounds, with an independent proof of nilpotent-trace vanishing. The theorems of record use only propext, Classical.choice and Quot.sound, checked by pinned audits.

*Quoted from the card [LeanPool/projects/regts-sevenster.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/regts-sevenster.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RS.regts_sevenster_characterisation`](https://leanpool.github.io/lean-pool/LeanPool/RegtsSevenster/RS/Summit.html#RS.regts_sevenster_characterisation) (theorem; a main declaration), declared in [LeanPool/RegtsSevenster/RS/Summit.lean, line 86](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RegtsSevenster/RS/Summit.lean#L86): “Normalized isomorphism-invariant complex graph parameters with exponentially bounded edge-connection ranks are precisely mixed partition functions.”
- [`RS.regts_sevenster_total`](https://leanpool.github.io/lean-pool/LeanPool/RegtsSevenster/RS/Summit.html#RS.regts_sevenster_total) (theorem), declared in [LeanPool/RegtsSevenster/RS/Summit.lean, line 53](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RegtsSevenster/RS/Summit.lean#L53): “A natural rank bound R admits a representing mixed model with total color dimension at most R.”
- [`RS.deligne_theorem`](https://leanpool.github.io/lean-pool/LeanPool/RegtsSevenster/RS/Classical/Deligne/DeligneAssembly.html#RS.deligne_theorem) (theorem), declared in [LeanPool/RegtsSevenster/RS/Classical/Deligne/DeligneAssembly.lean, line 324](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RegtsSevenster/RS/Classical/Deligne/DeligneAssembly.lean#L324): “The development proves its stated Deligne fiber-functor theorem for the symmetric tensor categories used in the representation.”

## Project

- Authors: William Whistler.
- Project repository: [willwhistler/regts-sevenster](https://github.com/willwhistler/regts-sevenster), at commit [bb0a6054](https://github.com/willwhistler/regts-sevenster/tree/bb0a60543d48afac3f36938104b5c85c7c0396c7).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C50, 18M20.
- In Lean Pool: [LeanPool/RegtsSevenster](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RegtsSevenster), from the card [LeanPool/projects/regts-sevenster.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/regts-sevenster.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/regts-sevenster.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/regts-sevenster.yaml)
- [Lean Pool at 701389c0: LeanPool/RegtsSevenster](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RegtsSevenster)
