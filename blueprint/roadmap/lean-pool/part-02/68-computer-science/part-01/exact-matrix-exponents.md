---
declaration: theorem
origin: cited
lean: MatrixMultiplicationAllFields.SpectralBooks.square_exponent, MatrixMultiplicationAllFields.SpectralBooks.dual_exponent, MatrixMultiplicationAllFields.SpectralBooks.rectangular_exponent
statement: formalized
proof: formalized
---

# Exact square, dual and rectangular matrix multiplication exponents

> Determines the arithmetic exponent of square matrix multiplication as 9/4 over every field and the dual exponent as 1/2. It also gives a symmetric formula for the rectangular exponent, using formal polynomial identities in division-free arithmetic programs. The pinned Lean source states all three exact results. The accompanying preprint gives the square equality for circuits allowing division and states bounds for the dual exponent and rectangular rank.

*Quoted from the card [LeanPool/projects/exact-matrix-exponents.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/exact-matrix-exponents.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MatrixMultiplicationAllFields.SpectralBooks.square_exponent`](https://leanpool.github.io/lean-pool/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.html#MatrixMultiplicationAllFields.SpectralBooks.square_exponent) (theorem; a main declaration), declared in [LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean, line 27](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean#L27): “Over every field, the exponent of division-free square matrix multiplication in the formal polynomial model is 9/4.”
- [`MatrixMultiplicationAllFields.SpectralBooks.dual_exponent`](https://leanpool.github.io/lean-pool/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.html#MatrixMultiplicationAllFields.SpectralBooks.dual_exponent) (theorem; a main declaration), declared in [LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean, line 31](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean#L31): “The dual exponent for multiplying rectangular matrices is 1/2 over every field.”
- [`MatrixMultiplicationAllFields.SpectralBooks.rectangular_exponent`](https://leanpool.github.io/lean-pool/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.html#MatrixMultiplicationAllFields.SpectralBooks.rectangular_exponent) (theorem; a main declaration), declared in [LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean, line 66](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ExactMatrixExponents/LinearAlgebra/SpectralBooks/ExactExponent.lean#L66): “Over every field, the exact rectangular exponent is a symmetric function of the three nonnegative parts of its dimension weights.”

## Project

- Authors: OpenAI.
- Source: [https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ExactExponent.lean), [paper](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf).
- Project repository: [openai/math](https://github.com/openai/math), at commit [3344da59](https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q17, 15A69, 68Q25.
- In Lean Pool: [LeanPool/ExactMatrixExponents](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ExactMatrixExponents), from the card [LeanPool/projects/exact-matrix-exponents.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/exact-matrix-exponents.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/exact-matrix-exponents.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/exact-matrix-exponents.yaml)
- [Lean Pool at bb99e52c: LeanPool/ExactMatrixExponents](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ExactMatrixExponents)
