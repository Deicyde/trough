---
declaration: theorem
origin: cited
lean: Ratpoints.mem_bruteForce_iff, Ratpoints.Fast.isPoint_and_inRegion_of_mem_fastPoints, Ratpoints.Fast.mem_fastPoints_iff, Ratpoints.Fast.nodup_fastPoints
statement: formalized
proof: formalized
---

# Verified bounded-height rational-point search on hyperelliptic curves

> Certifies a pure Lean brute-force reference and modular sieve for normalized integral triples (x, y, z) satisfying a hyperelliptic binary-form equation. Height is max(|x|, z), where x and z are the coprime numerator and denominator. Both searches include eligible points at infinity (z = 0). For finite points the fast search enforces the lower denominator bound and applies the upper bound only when it is positive. The fast search enumerates exactly these points without duplicates, using Tau Ceti's Sturm root count for pruning.

*Quoted from the card [LeanPool/projects/ratpoints.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/ratpoints.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Ratpoints.mem_bruteForce_iff`](https://leanpool.github.io/lean-pool/LeanPool/Ratpoints/Proof/BruteForce.html#Ratpoints.mem_bruteForce_iff) (theorem; a main declaration), declared in [LeanPool/Ratpoints/Proof/BruteForce.lean, line 181](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints/Proof/BruteForce.lean#L181): “Membership in the brute-force output is equivalent to being a normalized integral solution (x, y, z) with max(|x|, z) at most the height bound.”
- [`Ratpoints.Fast.isPoint_and_inRegion_of_mem_fastPoints`](https://leanpool.github.io/lean-pool/LeanPool/Ratpoints/Proof/FastSieve.html#Ratpoints.Fast.isPoint_and_inRegion_of_mem_fastPoints) (theorem; a main declaration), declared in [LeanPool/Ratpoints/Proof/FastSieve.lean, line 1279](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints/Proof/FastSieve.lean#L1279): “Every fast-search output is a normalized solution within the height bound. Its denominator is zero or meets the lower bound and any positive upper denominator bound.”
- [`Ratpoints.Fast.mem_fastPoints_iff`](https://leanpool.github.io/lean-pool/LeanPool/Ratpoints/Proof/FastSieve.html#Ratpoints.Fast.mem_fastPoints_iff) (theorem; a main declaration), declared in [LeanPool/Ratpoints/Proof/FastSieve.lean, line 1315](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints/Proof/FastSieve.lean#L1315): “For any tuning parameters, the fast search finds exactly the normalized solutions with max(|x|, z) within the height bound and with z zero or meeting the lower bound and any positive upper bound.”
- [`Ratpoints.Fast.nodup_fastPoints`](https://leanpool.github.io/lean-pool/LeanPool/Ratpoints/Proof/FastSieve.html#Ratpoints.Fast.nodup_fastPoints) (theorem; a main declaration), declared in [LeanPool/Ratpoints/Proof/FastSieve.lean, line 1323](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints/Proof/FastSieve.lean#L1323): “The fast search never returns a point twice.”

## Project

- Authors: Michael Stoll.
- Source: *RatpointsLean, verified bounded-height search*.
- Project repository: [MichaelStollBayreuth/RatpointsLean](https://github.com/MichaelStollBayreuth/RatpointsLean), at commit [aa11615d](https://github.com/MichaelStollBayreuth/RatpointsLean/tree/aa11615d33f7b09c063447c1bffd00849db9acba).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11G30, 11Y50, 68V20.
- In Lean Pool: [LeanPool/Ratpoints](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints), from the card [LeanPool/projects/ratpoints.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/ratpoints.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/ratpoints.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/ratpoints.yaml)
- [Lean Pool at bb99e52c: LeanPool/Ratpoints](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Ratpoints)
