---
declaration: theorem
origin: cited
lean: main3, FluteBounded, glideSymm, translationInvariance
statement: formalized
proof: formalized
---

# Maxima of Coxeter frieze patterns are Fibonacci numbers

> Formalizes the claim that the sequence of maxima of values of (Coxeter) arithmetic frieze patterns is the Fibonacci sequence, using a correspondence between arithmetic frieze patterns and n-flutes.

*Quoted from the card [LeanPool/projects/frieze-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frieze-patterns.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`main3`](https://leanpool.github.io/lean-pool/LeanPool/FriezePatterns/Chapter3.html#main3) (theorem; a main declaration), declared in [LeanPool/FriezePatterns/Chapter3.lean, line 536](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns/Chapter3.lean#L536): “Proves that the maximum value of an arithmetic frieze pattern of width n is exactly the n-th Fibonacci number, and that this bound is attained.”
- [`FluteBounded`](https://leanpool.github.io/lean-pool/LeanPool/FriezePatterns/Chapter2.html#FluteBounded) (theorem; a main declaration), declared in [LeanPool/FriezePatterns/Chapter2.lean, line 679](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns/Chapter2.lean#L679): “Proves that every entry of an n-flute is bounded above by the n-th Fibonacci number.”
- [`glideSymm`](https://leanpool.github.io/lean-pool/LeanPool/FriezePatterns/Chapter1.html#glideSymm) (theorem; a main declaration), declared in [LeanPool/FriezePatterns/Chapter1.lean, line 145](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns/Chapter1.lean#L145): “Proves the glide-reflection symmetry of Coxeter frieze patterns.”
- [`translationInvariance`](https://leanpool.github.io/lean-pool/LeanPool/FriezePatterns/Chapter1.html#translationInvariance) (theorem; a main declaration), declared in [LeanPool/FriezePatterns/Chapter1.lean, line 188](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns/Chapter1.lean#L188): “Proves the (n+1)-periodicity (horizontal translation invariance) of Coxeter frieze patterns.”

## Project

- Authors: Antoine de Saint-Germain, Akselai, Jon Cheah, Bockman Cheung, Eaton Liu.
- Source: *On upper bounds in frieze patterns* by Antoine de Saint-Germain, [doi:10.1080/00150517.2024.2430958](https://doi.org/10.1080/00150517.2024.2430958), [arXiv:2407.16717](https://arxiv.org/abs/2407.16717).
- Project repository: [Antoine-dSG/frieze_patterns](https://github.com/Antoine-dSG/frieze_patterns).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 05E15, 11B39, 13F60.
- In Lean Pool: [LeanPool/FriezePatterns](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns), from the card [LeanPool/projects/frieze-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frieze-patterns.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/frieze-patterns.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frieze-patterns.yaml)
- [Lean Pool at 701389c0: LeanPool/FriezePatterns](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FriezePatterns)
