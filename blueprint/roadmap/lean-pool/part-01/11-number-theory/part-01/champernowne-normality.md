---
declaration: theorem
origin: cited
lean: Champernowne.champernowne_normal
statement: formalized
proof: formalized
---

# Champernowne normality in every base

> Proves that concatenating the base-b digits of the positive integers gives a normal digit sequence for every integer base b at least 2: every nonempty length-k word of digits below b has limiting frequency b^(-k). This is a discrete, all-base generalization of D. G. Champernowne's 1933 base-ten result, without a real-number expansion bridge. Includes reusable substring-counting inequalities, a digit-string equivalence, exact cohort counts, and quantitative prefix bounds used to establish the frequency limit.

*Quoted from the card [LeanPool/projects/champernowne-normality.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/champernowne-normality.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Champernowne.champernowne_normal`](https://leanpool.github.io/lean-pool/LeanPool/Champernowne/Main.html#Champernowne.champernowne_normal) (theorem; a main declaration), declared in [LeanPool/Champernowne/Main.lean, line 20](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne/Main.lean#L20): “For every integer base b at least 2, the sequence formed by concatenating the base-b digits of 1, 2, 3, and so on is normal: each nonempty word w of digits below b has limiting occurrence frequency 1 / b^(length w), counting overlapping occurrences.”
- [`Champernowne.champernowne_normal_ten`](https://leanpool.github.io/lean-pool/LeanPool/Champernowne/Main.html#Champernowne.champernowne_normal_ten) (theorem), declared in [LeanPool/Champernowne/Main.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne/Main.lean#L27): “The decimal digit sequence 123456789101112... is normal in base ten.”
- [`Champernowne.sum_countOccurrences_cohort`](https://leanpool.github.io/lean-pool/LeanPool/Champernowne/CountExtras.html#Champernowne.sum_countOccurrences_cohort) (theorem), declared in [LeanPool/Champernowne/CountExtras.lean, line 570](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne/CountExtras.lean#L570): “For a nonempty length-k word of base-b digits with nonzero first digit and k at most m, its total occurrences inside all m-digit positive integers equal b^(m-k) + (m-k)(b-1)b^(m-k-1), with natural subtraction in the exponents.”
- [`Champernowne.sum_countOccurrences_cohort_zero`](https://leanpool.github.io/lean-pool/LeanPool/Champernowne/CountExtras.html#Champernowne.sum_countOccurrences_cohort_zero) (theorem), declared in [LeanPool/Champernowne/CountExtras.lean, line 582](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne/CountExtras.lean#L582): “For a nonempty length-k word of base-b digits starting with zero and k at most m, its total occurrences inside all m-digit positive integers equal (m-k)(b-1)b^(m-k-1), with natural subtraction in the exponent.”

## Project

- Authors: Arthur Champernowne.
- Source: *Champernowne Sequence Normality Proof* by Arthur Champernowne.
- Project repository: [OldMathematician/ChampernowneNormality](https://github.com/OldMathematician/ChampernowneNormality), at commit [31a76dbd](https://github.com/OldMathematician/ChampernowneNormality/tree/31a76dbde2727745beb6fb81af4cab1ce6a15fda).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11K16, 68R15.
- In Lean Pool: [LeanPool/Champernowne](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne), from the card [LeanPool/projects/champernowne-normality.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/champernowne-normality.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/champernowne-normality.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/champernowne-normality.yaml)
- [Lean Pool at 701389c0: LeanPool/Champernowne](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Champernowne)
