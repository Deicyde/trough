---
declaration: def
origin: cited
lean: LeanPool.DemazureProduct.AspPerm.star
statement: formalized
---

# Extended Demazure Product on ASP Permutations

> Formalizes the extended Demazure product on almost-sign-preserving integer permutations, including slipface models, residuals, greedy and stingy characterizations, reduction theorems, adjacent-transposition formulas, and 321-avoiding factorization results.

*Quoted from the card [LeanPool/projects/demazure-product.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/demazure-product.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 9 main results, each with its informal statement quoted from the card. The scan finds 9 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.DemazureProduct.AspPerm.star`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Submodular.html#LeanPool.DemazureProduct.AspPerm.star) (def; a main declaration), declared in [LeanPool/DemazureProduct/Submodular.lean, line 1063](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Submodular.lean#L1063): “Defines the extended Demazure product on almost-sign-preserving permutations.”
- [`LeanPool.DemazureProduct.AspPerm.star_assoc`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Submodular.html#LeanPool.DemazureProduct.AspPerm.star_assoc) (lemma), declared in [LeanPool/DemazureProduct/Submodular.lean, line 1115](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Submodular.lean#L1115): “Proves associativity of the extended Demazure product on almost-sign-preserving permutations.”
- [`LeanPool.DemazureProduct.Reduction.starGreedy`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Reduction.html#LeanPool.DemazureProduct.Reduction.starGreedy) (theorem), declared in [LeanPool/DemazureProduct/Reduction.lean, line 116](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Reduction.lean#L116): “Characterizes the Demazure product as the Bruhat-maximum of ordinary products of smaller factors.”
- [`LeanPool.DemazureProduct.Reduction.reduce`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Reduction.html#LeanPool.DemazureProduct.Reduction.reduce) (theorem), declared in [LeanPool/DemazureProduct/Reduction.lean, line 179](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Reduction.lean#L179): “Reduces inequalities against a Demazure product to ordinary products of Bruhat-smaller factors with fixed shift.”
- [`LeanPool.DemazureProduct.Reduction.lres_stingy`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Reduction.html#LeanPool.DemazureProduct.Reduction.lres_stingy) (theorem), declared in [LeanPool/DemazureProduct/Reduction.lean, line 294](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Reduction.lean#L294): “Gives the stingy characterization of the left residual as a Bruhat-minimum of ordinary products.”
- [`LeanPool.DemazureProduct.ReducedProducts.star_eq_mul_iff_reducedProduct`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/ReducedProducts.html#LeanPool.DemazureProduct.ReducedProducts.star_eq_mul_iff_reducedProduct) (theorem), declared in [LeanPool/DemazureProduct/ReducedProducts.lean, line 249](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/ReducedProducts.lean#L249): “Shows that the Demazure product equals ordinary multiplication exactly for reduced ASP products.”
- [`LeanPool.DemazureProduct.Transpositions.starSigma`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Transpositions.html#LeanPool.DemazureProduct.Transpositions.starSigma) (theorem), declared in [LeanPool/DemazureProduct/Transpositions.lean, line 861](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Transpositions.lean#L861): “Proves the adjacent-transposition formula for multiplying an ASP permutation by a no-consecutive-pair involution.”
- [`LeanPool.DemazureProduct.ASP321a.dprod_eq_iff`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Avoiding321.html#LeanPool.DemazureProduct.ASP321a.dprod_eq_iff) (theorem), declared in [LeanPool/DemazureProduct/Avoiding321.lean, line 1439](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Avoiding321.lean#L1439): “Characterizes Demazure factorizations of 321-avoiding ASP permutations by isolated inversion-set decompositions.”
- [`LeanPool.DemazureProduct.Tableaux.setValuedTableauEquivHeckeFactorization`](https://leanpool.github.io/lean-pool/LeanPool/DemazureProduct/Tableaux.html#LeanPool.DemazureProduct.Tableaux.setValuedTableauEquivHeckeFactorization) (def), declared in [LeanPool/DemazureProduct/Tableaux.lean, line 1158](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct/Tableaux.lean#L1158): “Relates fixed-shift set-valued tableaux to Hecke factorizations of 321-avoiding ASP permutations.”

## Project

- Authors: Nathan Pflueger.
- Source: *An extended Demazure product on integer permutations via min-plus matrix multiplication* by Nathan Pflueger, [arXiv:2206.14227](https://arxiv.org/abs/2206.14227).
- Project repository: [npflueger/demazure](https://github.com/npflueger/demazure).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05E05, 20F55.
- In Lean Pool: [LeanPool/DemazureProduct](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct), from the card [LeanPool/projects/demazure-product.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/demazure-product.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/demazure-product.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/demazure-product.yaml)
- [Lean Pool at 2b205bf9: LeanPool/DemazureProduct](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DemazureProduct)
