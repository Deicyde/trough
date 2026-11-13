---
declaration: theorem
origin: cited
lean: FourAP.exists_fourAPFree_positive_permutation
statement: formalized
proof: formalized
---

# A 4AP-free permutation of the positive integers

> Formalizes Boon Suan Ho's construction of a permutation of the positive integers with no four-term arithmetic progression as a subsequence, proving the binary-order lemmas, extension lemma, and computable limit.

*Quoted from the card [LeanPool/projects/four-ap-free-permutation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/four-ap-free-permutation.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FourAP.exists_fourAPFree_positive_permutation`](https://leanpool.github.io/lean-pool/LeanPool/FourAP/Main.html#FourAP.exists_fourAPFree_positive_permutation) (theorem; a main declaration), declared in [LeanPool/FourAP/Main.lean, line 44](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FourAP/Main.lean#L44): “There exists a bijection of the positive integers such that no four increasing positions map to a nonconstant four-term arithmetic progression, including negative common differences.”
- [`FourAP.explicitPositivePermutation_apFree`](https://leanpool.github.io/lean-pool/LeanPool/FourAP/Construction.html#FourAP.explicitPositivePermutation_apFree) (theorem), declared in [LeanPool/FourAP/Construction.lean, line 141](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FourAP/Construction.lean#L141): “The explicit computable positive-integer permutation constructed in the development has the stated four-term progression avoidance property.”

## Project

- Authors: Boon Suan Ho.
- Source: *A 4AP-free permutation of the positive integers* by Boon Suan Ho, [arXiv:2609.12780](https://arxiv.org/abs/2609.12780).
- Project repository: [boonsuan/4ap](https://github.com/boonsuan/4ap), at commit [4630aefb](https://github.com/boonsuan/4ap/tree/4630aefbbcb7f6537aceaeb1afac8dd3af455871).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 11B25, 05D10.
- In Lean Pool: [LeanPool/FourAP](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FourAP), from the card [LeanPool/projects/four-ap-free-permutation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/four-ap-free-permutation.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/four-ap-free-permutation.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/four-ap-free-permutation.yaml)
- [Lean Pool at 701389c0: LeanPool/FourAP](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FourAP)
