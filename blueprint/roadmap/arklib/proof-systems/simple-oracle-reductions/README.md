# Simple Oracle Reductions

We start by introducing a number of simple oracle reductions that serve as fundamental building blocks for more complex proof systems. These components can be composed together to construct larger protocols.

## Trivial Reduction

The simplest possible oracle reduction is one that performs no computation at all. Both the prover and verifier simply pass their inputs through unchanged. While seemingly trivial, this reduction serves as an important identity element for composition and provides a base case for lifting and lens operations.

## [DoNothing Reduction to Generator Batching Security](part-01/README.md)

- [DoNothing Reduction](part-01/def-donothing-reduction.md)
- [DoNothing Perfect Completeness](part-01/theorem-simple-protocols-1.md)
- [DoNothing Round-by-Round Knowledge Soundness](part-01/theorem-simple-protocols-2.md)
- [SendWitness Reduction](part-01/def-sendwitness-reduction.md)
- [SendWitness Security](part-01/theorem-simple-protocols-3.md)
- [SendSingleWitness Oracle Reduction](part-01/def-sendsinglewitness-oracle-reduction.md)
- [SendSingleWitness Security](part-01/theorem-simple-protocols-4.md)
- [Single-message adapter](part-01/def-sendsinglewitness-adapter.md)
- [Single-message adapter security](part-01/theorem-simple-protocols-5.md)
- [RandomQuery Oracle Reduction](part-01/def-randomquery-oracle-reduction.md)
- [RandomQuery Perfect Completeness](part-01/theorem-simple-protocols-6.md)
- [RandomQuery Knowledge Soundness](part-01/theorem-simple-protocols-7.md)
- [Oracle Distance](part-01/def-oracle-distance.md)
- [RandomQuery Knowledge Soundness from Distance](part-01/theorem-simple-protocols-8.md)
- [RandomEvaluation Oracle Reduction](part-01/def-random-evaluation.md)
- [RandomEvaluation Soundness](part-01/theorem-simple-protocols-9.md)
- [Quotient Zero Test](part-01/def-quotient-zero-test.md)
- [Quotient Zero Test Security](part-01/theorem-simple-protocols-10.md)
- [Generator Batching](part-01/def-generator-batch.md)
- [Generator Batching Security](part-01/theorem-simple-protocols-11.md)

## [SendClaim Oracle Reduction to No-interaction Completeness](part-02/README.md)

- [SendClaim Oracle Reduction](part-02/def-sendclaim-oracle-reduction.md)
- [SendClaim Coordinate-wise Special Soundness](part-02/theorem-simple-protocols-12.md)
- [SendChallenge Oracle Reduction](part-02/def-sendchallenge-oracle-reduction.md)
- [ReduceClaim Reduction](part-02/def-reduceclaim-reduction.md)
- [ReduceClaim Perfect Completeness](part-02/theorem-simple-protocols-14.md)
- [ReduceClaim Round-by-Round Knowledge Soundness](part-02/theorem-simple-protocols-15.md)
- [ReduceClaim Oracle Reduction](part-02/def-reduceclaim-oracle-reduction.md)
- [ReduceClaim Oracle Security](part-02/theorem-simple-protocols-16.md)
- [CheckClaim Reduction](part-02/def-checkclaim-reduction.md)
- [CheckClaim Security](part-02/theorem-simple-protocols-17.md)
- [CheckClaim Oracle Reduction](part-02/def-checkclaim-oracle-reduction.md)
- [CheckClaim Oracle Security](part-02/theorem-simple-protocols-18.md)
- [No-interaction Reduction](part-02/def-no-interaction-reduction.md)
- [No-interaction Completeness](part-02/theorem-simple-protocols-19.md)
