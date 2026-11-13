---
declaration: theorem
origin: cited
lean: Undecidability.exists_small_undecidable_presentations
statement: formalized
proof: formalized
---

# Small undecidable groups and effective Adian–Rabin families

> Proves the existence of a finitely presented group with three generator slots and nine relator slots whose word problem is undecidable, and effective families with undecidable triviality having respectively four generators and eleven relators, and two generators and ten relators. The dependency closure includes computable machine-to-Thue reductions, synchronized rewriting, Borisov’s group simulator, injective HNN and Tietze compression, and general Miller–Tancer and Gordon constructions. Formalizes the algebraic results of the cited paper; its four-manifold consequences are outside this project.

*Quoted from the card [LeanPool/projects/small-undecidable-groups.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/small-undecidable-groups.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Undecidability.exists_three_generator_nine_relator_group_with_unsolvable_word_problem`](https://leanpool.github.io/lean-pool/LeanPool/SmallUndecidableGroups.html#Undecidability.exists_three_generator_nine_relator_group_with_unsolvable_word_problem) (theorem), declared in [LeanPool/SmallUndecidableGroups.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups.lean#L27): “There is a finite presentation with three generator slots and nine relator slots whose word problem is not a computable predicate.” Its source, as the card gives it: “arXiv:2609.10461v1, Theorem 1.1.”
- [`Undecidability.exists_four_generator_eleven_relator_adian_rabin_family`](https://leanpool.github.io/lean-pool/LeanPool/SmallUndecidableGroups.html#Undecidability.exists_four_generator_eleven_relator_adian_rabin_family) (theorem), declared in [LeanPool/SmallUndecidableGroups.lean, line 37](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups.lean#L37): “There is a uniformly computable family of finite presentations with four generator slots and eleven relator slots for which the set of indices presenting the trivial group is not computable.” Its source, as the card gives it: “arXiv:2609.10461v1, Theorem 1.3.”
- [`Undecidability.exists_two_generator_ten_relator_adian_rabin_family`](https://leanpool.github.io/lean-pool/LeanPool/SmallUndecidableGroups.html#Undecidability.exists_two_generator_ten_relator_adian_rabin_family) (theorem), declared in [LeanPool/SmallUndecidableGroups.lean, line 50](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups.lean#L50): “There is a uniformly computable family of finite presentations with two generator slots and ten relator slots for which the set of indices presenting the trivial group is not computable.” Its source, as the card gives it: “arXiv:2609.10461v1, Theorem 1.4.”
- [`Undecidability.exists_small_undecidable_presentations`](https://leanpool.github.io/lean-pool/LeanPool/SmallUndecidableGroups.html#Undecidability.exists_small_undecidable_presentations) (theorem; a main declaration), declared in [LeanPool/SmallUndecidableGroups.lean, line 60](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups.lean#L60): “The three small-presentation bounds hold together: an undecidable word problem with three generators and nine relators, and effective families with undecidable triviality with four generators and eleven relators and with two generators and ten relators.” Its source, as the card gives it: “arXiv:2609.10461v1, Theorems 1.1, 1.3, and 1.4.”

## Project

- Authors: Marc Kegel, Shana Yunsheng Li, Qiuyu Ren.
- Source: *Small undecidable groups and unrecognizable 4-manifolds*, [arXiv:2609.10461](https://arxiv.org/abs/2609.10461).
- Project repository: [32805433/Adian-Rabin](https://github.com/32805433/Adian-Rabin), at commit [fb4a401e](https://github.com/32805433/Adian-Rabin/tree/fb4a401e8fbdba36e7b35c11fde2baa15592e185).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 20F10, 03D35.
- In Lean Pool: [LeanPool/SmallUndecidableGroups](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups), from the card [LeanPool/projects/small-undecidable-groups.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/small-undecidable-groups.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/small-undecidable-groups.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/small-undecidable-groups.yaml)
- [Lean Pool at 701389c0: LeanPool/SmallUndecidableGroups](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SmallUndecidableGroups)
