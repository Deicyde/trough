---
declaration: theorem
origin: cited
lean: Corless.corless_conjecture, Corless.card_nilpotent
statement: formalized
proof: formalized
---

# Corless's nilpotent Bohemian matrix conjecture

> Classifies the nilpotent complex skew-symmetric tridiagonal matrices with superdiagonal entries in {1, i} and counts them in each admissible dimension. The proof relates characteristic polynomials to weighted path matching polynomials, then uses the mod-2 dimension restriction and a mod-4 folding argument to recover the recursive superdiagonal vectors.

*Quoted from the card [LeanPool/projects/corless-nilpotent.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/corless-nilpotent.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Corless.corless_conjecture`](https://leanpool.github.io/lean-pool/LeanPool/CorlessNilpotent/Vectors.html#Corless.corless_conjecture) (theorem; a main declaration), declared in [LeanPool/CorlessNilpotent/Vectors.lean, line 226](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CorlessNilpotent/Vectors.lean#L226): “For a superdiagonal vector with entries 1 or i, the associated skew-symmetric tridiagonal matrix is nilpotent exactly when the vector belongs to Corless's recursively folded family.”
- [`Corless.card_nilpotent`](https://leanpool.github.io/lean-pool/LeanPool/CorlessNilpotent/Vectors.html#Corless.card_nilpotent) (theorem; a main declaration), declared in [LeanPool/CorlessNilpotent/Vectors.lean, line 290](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CorlessNilpotent/Vectors.lean#L290): “For each nonnegative k, exactly 2^k superdiagonal vectors yield nilpotent matrices of dimension 2^(k+1) - 1.”

## Project

- Authors: Marcel Blattner.
- Source: [doi:10.5206/mt.v1i2.14360](https://doi.org/10.5206/mt.v1i2.14360).
- Project repository: [marcelbtec/corless-nilpotent](https://github.com/marcelbtec/corless-nilpotent), at commit [1f4fa000](https://github.com/marcelbtec/corless-nilpotent/tree/1f4fa000540c5f8ab3f657fa436adb45a1404ade).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 15A18, 05C31.
- In Lean Pool: [LeanPool/CorlessNilpotent](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CorlessNilpotent), from the card [LeanPool/projects/corless-nilpotent.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/corless-nilpotent.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/corless-nilpotent.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/corless-nilpotent.yaml)
- [Lean Pool at 307e3125: LeanPool/CorlessNilpotent](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CorlessNilpotent)
