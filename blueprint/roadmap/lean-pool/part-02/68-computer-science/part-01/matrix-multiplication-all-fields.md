---
declaration: theorem
origin: cited
lean: MatrixMultiplicationAllFields.omega_le_nine_quarters_all_fields
statement: formalized
proof: formalized
---

# Matrix multiplication exponent at most 9/4 over every field

> The arithmetic exponent of square matrix multiplication is at most 9/4 over every field. The proof preserves a general tensor-rank and arithmetic-program library, extends Fourier separation to positive characteristic, and descends finite tensor decompositions through algebraic extensions. For every positive epsilon it constructs correct division-free programs of cost at most C n^(9/4 + epsilon), with C uniform in the matrix size.

*Quoted from the card [LeanPool/projects/matrix-multiplication-all-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/matrix-multiplication-all-fields.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MatrixMultiplicationAllFields.omega_le_nine_quarters_all_fields`](https://leanpool.github.io/lean-pool/LeanPool/MatrixMultiplicationAllFields.html#MatrixMultiplicationAllFields.omega_le_nine_quarters_all_fields) (theorem; a main declaration), declared in [LeanPool/MatrixMultiplicationAllFields.lean, line 117](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields.lean#L117): “For every field F, the infimum of admissible arithmetic matrix multiplication exponents is at most 9/4.”
- [`MatrixMultiplicationAllFields.MatrixMultiplication.admissibleExponent_nine_quarters_all_fields`](https://leanpool.github.io/lean-pool/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.html#MatrixMultiplicationAllFields.MatrixMultiplication.admissibleExponent_nine_quarters_all_fields) (theorem), declared in [LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.lean, line 109](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.lean#L109): “Over every field F and for every epsilon > 0, a positive constant C bounds the cost of a correct division-free straight-line program for n by n matrix multiplication by C n^(9/4 + epsilon) for every n >= 1.”
- [`MatrixMultiplicationAllFields.MatrixMultiplication.matrix_multiplication_cost_le_all_fields`](https://leanpool.github.io/lean-pool/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.html#MatrixMultiplicationAllFields.MatrixMultiplication.matrix_multiplication_cost_le_all_fields) (theorem), declared in [LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.lean, line 114](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Main.lean#L114): “The bound is realized by correct arithmetic programs at every positive matrix size, with a constant depending on the field and epsilon but not the size.”
- [`MatrixMultiplicationAllFields.MatrixMultiplication.AllFields.rankAtMost_of_map`](https://leanpool.github.io/lean-pool/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Descent.html#MatrixMultiplicationAllFields.MatrixMultiplication.AllFields.rankAtMost_of_map) (theorem), declared in [LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Descent.lean, line 110](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields/LinearAlgebra/MatrixMultiplication/AllFields/Descent.lean#L110): “A rank-R decomposition over a finite extension E/P of degree m descends to a rank at most m^3 R decomposition over P.”

## Project

- Authors: OpenAI, Jeroen Zuiddam.
- Source: [paper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf).
- Project repository: [jzuiddam/omega-nine-quarters-all-fields](https://github.com/jzuiddam/omega-nine-quarters-all-fields), at commit [615b591c](https://github.com/jzuiddam/omega-nine-quarters-all-fields/tree/615b591cddd8792173c17b58558ef3b9f11a702c).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q17, 15A69, 68Q25.
- In Lean Pool: [LeanPool/MatrixMultiplicationAllFields](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields), from the card [LeanPool/projects/matrix-multiplication-all-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/matrix-multiplication-all-fields.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/matrix-multiplication-all-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/matrix-multiplication-all-fields.yaml)
- [Lean Pool at 701389c0: LeanPool/MatrixMultiplicationAllFields](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MatrixMultiplicationAllFields)
