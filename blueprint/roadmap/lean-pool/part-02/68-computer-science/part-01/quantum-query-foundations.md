---
declaration: theorem
origin: cited
lean: QuantumQueryComplexity.boundedErrorQQuery_characterized_by_advPM
statement: formalized
proof: formalized
---

# Adversary bounds and the polynomial method for quantum queries

> Develops finite quantum query algorithms, real adversary primal and dual programs, strong duality, exact Boolean block composition, explicit constant-factor bounded-error query characterizations, and degree bounds for output-probability polynomials. Query models include idle and blank sectors; bounds count queries, not gate complexity or running time. Uniform algorithm extraction assumes a supplied dual certificate.

*Quoted from the card [LeanPool/projects/quantum-query-foundations.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quantum-query-foundations.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`QuantumQueryComplexity.advDual_eq_advPM`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/Adversary.html#QuantumQueryComplexity.advDual_eq_advPM) (theorem), declared in [LeanPool/QuantumQuery/Adversary.lean, line 6567](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/Adversary.lean#L6567): “For every total Boolean function on a finite Boolean input cube, the all-pairs real adversary dual infimum equals the real symmetric primal supremum.”
- [`QuantumQueryComplexity.advPM_composeFun_eq`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/Adversary.html#QuantumQueryComplexity.advPM_composeFun_eq) (theorem), declared in [LeanPool/QuantumQuery/Adversary.lean, line 6587](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/Adversary.lean#L6587): “The negative-weight adversary value of total Boolean functions composed on disjoint blocks equals the product of their adversary values, including constant functions and empty index types.”
- [`QuantumQueryComplexity.boundedErrorQQuery_characterized_by_advPM`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/QueryBounds.html#QuantumQueryComplexity.boundedErrorQQuery_characterized_by_advPM) (theorem; a main declaration), declared in [LeanPool/QuantumQuery/QueryBounds.lean, line 1806](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/QueryBounds.lean#L1806): “For a total Boolean function at error one third, quantum value-query complexity lies between ADV±/36 and 2^14 ADV±. The value oracle swaps a blank answer with the queried letter and includes an idle query index.”
- [`QuantumQueryComplexity.xorQQuery_characterized_by_advPM`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/QueryBounds.html#QuantumQueryComplexity.xorQQuery_characterized_by_advPM) (theorem), declared in [LeanPool/QuantumQuery/QueryBounds.lean, line 1818](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/QueryBounds.lean#L1818): “For the Boolean XOR oracle with idle and blank sectors, query complexity at error one third lies between ADV±/72 and 2^15 ADV±.”
- [`QuantumQueryComplexity.qQueryOn_third_le_of_hasDualOn_uniform`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/StateConversion.html#QuantumQueryComplexity.qQueryOn_third_le_of_hasDualOn_uniform) (theorem), declared in [LeanPool/QuantumQuery/StateConversion.lean, line 5494](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/StateConversion.lean#L5494): “A supplied all-pairs real dual certificate of nonnegative cost c gives a finite quantum algorithm using at most 8192(1+c) value queries at error one third, for any finite promise domain and nonempty decidable output type.”
- [`QuantumQueryComplexity.QAlg.exists_probability_polynomial`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/Polynomial.html#QuantumQueryComplexity.QAlg.exists_probability_polynomial) (theorem), declared in [LeanPool/QuantumQuery/Polynomial.lean, line 388](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/Polynomial.lean#L388): “Each output probability of a q-query value-oracle algorithm on Boolean inputs agrees on the Boolean cube with a real polynomial of total degree at most 2q.”
- [`QuantumQueryComplexity.exists_xor_probability_polynomial`](https://leanpool.github.io/lean-pool/LeanPool/QuantumQuery/Polynomial.html#QuantumQueryComplexity.exists_xor_probability_polynomial) (theorem), declared in [LeanPool/QuantumQuery/Polynomial.lean, line 516](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery/Polynomial.lean#L516): “Each output probability of a q-query Boolean XOR algorithm agrees on the Boolean cube with a real polynomial of total degree at most 2q.”

## Project

- Authors: Troy Lee.
- Source: [arXiv:1011.3020v2](https://arxiv.org/abs/1011.3020v2), [https://github.com/troyjlee/quantum-query-complexity/tree/517ba85eb211232771429804d8583e3f52b9d541](https://github.com/troyjlee/quantum-query-complexity/tree/517ba85eb211232771429804d8583e3f52b9d541).
- Project repository: [troyjlee/quantum-query-complexity](https://github.com/troyjlee/quantum-query-complexity), at commit [517ba85e](https://github.com/troyjlee/quantum-query-complexity/tree/517ba85eb211232771429804d8583e3f52b9d541).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q12, 81P68.
- In Lean Pool: [LeanPool/QuantumQuery](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery), from the card [LeanPool/projects/quantum-query-foundations.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quantum-query-foundations.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/quantum-query-foundations.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quantum-query-foundations.yaml)
- [Lean Pool at 2b205bf9: LeanPool/QuantumQuery](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuantumQuery)
