---
declaration: theorem
origin: cited
lean: JordanPrime.jordan_onto_prime, JordanPrime.twoIdentity_onto_prime, JordanPrime.twoIdentity_into_domain
statement: formalized
proof: formalized
---

# Herstein–Smiley theorems on Jordan homomorphisms of prime rings

> Classifies surjective Jordan homomorphisms onto prime rings without two-torsion as multiplicative or anti-multiplicative. Also proves Smiley's square-and-triple-identity form in every characteristic and the Jacobson–Rickart domain form without surjectivity, with counterexamples separating the original hypotheses and general biadditive and prime-ring lemmas.

*Quoted from the card [LeanPool/projects/herstein-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/herstein-jordan.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`JordanPrime.jordan_onto_prime`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.jordan_onto_prime) (theorem; a main declaration), declared in [LeanPool/HersteinJordan/Statements.lean, line 78](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L78): “A surjective additive Jordan homomorphism of possibly nonunital rings onto a prime ring without two-torsion is multiplicative or anti-multiplicative.”
- [`JordanPrime.twoIdentity_onto_prime`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.twoIdentity_onto_prime) (theorem; a main declaration), declared in [LeanPool/HersteinJordan/Statements.lean, line 152](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L152): “In every characteristic a surjective additive map onto a prime ring that preserves squares and triple products aba is multiplicative or anti-multiplicative.”
- [`JordanPrime.twoIdentity_into_domain`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.twoIdentity_into_domain) (theorem; a main declaration), declared in [LeanPool/HersteinJordan/Statements.lean, line 89](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L89): “An additive map preserving squares and triple products into a ring without zero divisors is multiplicative or anti-multiplicative, without assuming surjectivity or excluding any characteristic.”
- [`JordanPrime.onto_needed`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.onto_needed) (theorem), declared in [LeanPool/HersteinJordan/Statements.lean, line 97](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L97): “An explicit integer-matrix Jordan homomorphism shows that surjectivity cannot be dropped from the first theorem.”
- [`JordanPrime.prime_needed`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.prime_needed) (theorem), declared in [LeanPool/HersteinJordan/Statements.lean, line 116](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L116): “Transposing one factor in a product of integer-matrix rings shows that the prime-target hypothesis cannot be dropped.”
- [`JordanPrime.two_needed`](https://leanpool.github.io/lean-pool/LeanPool/HersteinJordan/Statements.html#JordanPrime.two_needed) (theorem), declared in [LeanPool/HersteinJordan/Statements.lean, line 138](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan/Statements.lean#L138): “Addition from two copies of the field with two elements shows that the two-torsion hypothesis cannot be dropped from the first theorem.”

## Project

- Authors: Stephanie Alexander.
- Source: *Jordan homomorphisms onto prime rings*, [doi:10.1090/S0002-9947-1957-0083484-X](https://doi.org/10.1090/S0002-9947-1957-0083484-X).
- Project repository: [stalex444/herstein-jordan-homomorphisms](https://github.com/stalex444/herstein-jordan-homomorphisms), at commit [34dffa8a](https://github.com/stalex444/herstein-jordan-homomorphisms/tree/34dffa8aace3a1b565b11cbb561db3a58fa203da).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 16W10, 16N60, 17C50.
- In Lean Pool: [LeanPool/HersteinJordan](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan), from the card [LeanPool/projects/herstein-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/herstein-jordan.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/herstein-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/herstein-jordan.yaml)
- [Lean Pool at bb99e52c: LeanPool/HersteinJordan](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HersteinJordan)
