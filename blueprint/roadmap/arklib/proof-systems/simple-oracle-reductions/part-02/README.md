---
navigation: transparent
---

# SendClaim Oracle Reduction to No-interaction Completeness

## Sending a Claim

The SendClaim reduction lets the prover send a claim computed from the input statement, as one oracle message. The verifier does not check the claim; the check is carried by the output relation.

- [SendClaim Oracle Reduction](def-sendclaim-oracle-reduction.md)
- [SendClaim Coordinate-wise Special Soundness](theorem-simple-protocols-12.md)

## Sending a Challenge

- [SendChallenge Oracle Reduction](def-sendchallenge-oracle-reduction.md)

## Claim Reduction

A fundamental building block for constructing complex proof systems is the ability to locally reduce one type of claim to another. The ReduceClaim reduction provides this functionality through mappings between statement and witness types.

- [ReduceClaim Reduction](def-reduceclaim-reduction.md)
- [ReduceClaim Perfect Completeness](theorem-simple-protocols-14.md)
- [ReduceClaim Round-by-Round Knowledge Soundness](theorem-simple-protocols-15.md)
- [ReduceClaim Oracle Reduction](def-reduceclaim-oracle-reduction.md)
- [ReduceClaim Oracle Security](theorem-simple-protocols-16.md)

## Claim Verification

Another essential building block is the ability to verify that a given predicate holds for a statement without requiring additional witness information.

- [CheckClaim Reduction](def-checkclaim-reduction.md)
- [CheckClaim Security](theorem-simple-protocols-17.md)
- [CheckClaim Oracle Reduction](def-checkclaim-oracle-reduction.md)
- [CheckClaim Oracle Security](theorem-simple-protocols-18.md)

## Reductions Without Interaction

- [No-interaction Reduction](def-no-interaction-reduction.md)
- [No-interaction Completeness](theorem-simple-protocols-19.md)
