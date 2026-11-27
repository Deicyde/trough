---
declaration: theorem
origin: cited
lean: WordRepTensor.not_wordRepresentable_mycielskian_tensor_wheel, WordRepTensor.not_wordRepresentable_extended_tensor_wheel, WordRepTensor.not_wordRepresentable_mycielskian_tensor_extended, WordRepTensor.not_wordRepresentable_extended_tensor_extended
statement: formalized
proof: formalized
---

# Non-word-representability of tensor products of Mycielski graphs

> Answers three questions of Alshammari about word-representability of tensor products of graphs built from odd cycles. Induced embeddings settle the products with odd wheels, and a seven-vertex orientation certificate rules out word representations of the mixed and extended Mycielski products.

*Quoted from the card [LeanPool/projects/word-rep-tensor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/word-rep-tensor.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`WordRepTensor.not_wordRepresentable_mycielskian_tensor_wheel`](https://leanpool.github.io/lean-pool/LeanPool/WordRepTensor/WheelProducts.html#WordRepTensor.not_wordRepresentable_mycielskian_tensor_wheel) (theorem; a main declaration), declared in [LeanPool/WordRepTensor/WheelProducts.lean, line 27](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor/WheelProducts.lean#L27): “For n ≥ 1 and m ≥ 2, the tensor product of the Mycielskian of C(2n+1) with the wheel on a rim C(2m+1) is not word-representable.”
- [`WordRepTensor.not_wordRepresentable_extended_tensor_wheel`](https://leanpool.github.io/lean-pool/LeanPool/WordRepTensor/WheelProducts.html#WordRepTensor.not_wordRepresentable_extended_tensor_wheel) (theorem; a main declaration), declared in [LeanPool/WordRepTensor/WheelProducts.lean, line 39](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor/WheelProducts.lean#L39): “The same non-word-representability holds when the first factor is the extended Mycielskian of C(2n+1).”
- [`WordRepTensor.not_wordRepresentable_mycielskian_tensor_extended`](https://leanpool.github.io/lean-pool/LeanPool/WordRepTensor/MycielskiProducts.html#WordRepTensor.not_wordRepresentable_mycielskian_tensor_extended) (theorem; a main declaration), declared in [LeanPool/WordRepTensor/MycielskiProducts.lean, line 19](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor/MycielskiProducts.lean#L19): “For 1 ≤ n < m, the product of the Mycielskian of C(2n+1) and the extended Mycielskian of C(2m+1) is not word-representable.”
- [`WordRepTensor.not_wordRepresentable_extended_tensor_extended`](https://leanpool.github.io/lean-pool/LeanPool/WordRepTensor/MycielskiProducts.html#WordRepTensor.not_wordRepresentable_extended_tensor_extended) (theorem; a main declaration), declared in [LeanPool/WordRepTensor/MycielskiProducts.lean, line 36](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor/MycielskiProducts.lean#L36): “For 1 ≤ n < m, the product of the extended Mycielskians of C(2n+1) and C(2m+1) is not word-representable.”

## Project

- Authors: Horace Dong.
- Source: *Tensor products of Mycielskians of odd cycles with odd wheels and with extended Mycielskians of odd cycles are not word-representable*, [https://github.com/Horace-Maxwell/ai4math-results/blob/65dd8899dfe1abf289282f141222057d5593ca02/papers/wordrep-tensor/note.pdf](https://github.com/Horace-Maxwell/ai4math-results/blob/65dd8899dfe1abf289282f141222057d5593ca02/papers/wordrep-tensor/note.pdf).
- Project repository: [Horace-Maxwell/ai4math-results](https://github.com/Horace-Maxwell/ai4math-results), at commit [65dd8899](https://github.com/Horace-Maxwell/ai4math-results/tree/65dd8899dfe1abf289282f141222057d5593ca02).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C76, 05C62.
- In Lean Pool: [LeanPool/WordRepTensor](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor), from the card [LeanPool/projects/word-rep-tensor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/word-rep-tensor.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/word-rep-tensor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/word-rep-tensor.yaml)
- [Lean Pool at bb99e52c: LeanPool/WordRepTensor](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WordRepTensor)
