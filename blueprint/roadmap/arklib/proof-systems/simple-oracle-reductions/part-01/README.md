---
navigation: transparent
---

# DoNothing Reduction to Generator Batching Security

- [DoNothing Reduction](def-donothing-reduction.md)
- [DoNothing Perfect Completeness](theorem-simple-protocols-1.md)
- [DoNothing Round-by-Round Knowledge Soundness](theorem-simple-protocols-2.md)

The oracle version of DoNothing handles oracle statements by passing them through unchanged as well. The prover receives both non-oracle and oracle statements as input, and outputs them in the same form to the verifier.

## Sending the Witness

A fundamental building block in many proof systems is the ability for the prover to transmit witness information to the verifier. The SendWitness reduction provides this functionality in both direct and oracle settings.

- [SendWitness Reduction](def-sendwitness-reduction.md)
- [SendWitness Security](theorem-simple-protocols-3.md)
- [SendSingleWitness Oracle Reduction](def-sendsinglewitness-oracle-reduction.md)
- [SendSingleWitness Security](theorem-simple-protocols-4.md)

SendSingleWitness is the identity instance of a more general one-message stage. Spartan's witness attachment instantiates the same stage.

- [Single-message adapter](def-sendsinglewitness-adapter.md)
- [Single-message adapter security](theorem-simple-protocols-5.md)

## Random Query Testing

One of the most fundamental oracle reductions tests whether two values computed from the statement and the oracle statements are equal, by comparing them at a single random query.

- [RandomQuery Oracle Reduction](def-randomquery-oracle-reduction.md)
- [RandomQuery Perfect Completeness](theorem-simple-protocols-6.md)
- [RandomQuery Knowledge Soundness](theorem-simple-protocols-7.md)

The agreement bound only needs to hold for the pairs $f(x, \mathsf{o}), g(x, \mathsf{o})$ that actually occur. When it holds for all pairs, it is a property of the oracle interface:

- [Oracle Distance](def-oracle-distance.md)
- [RandomQuery Knowledge Soundness from Distance](theorem-simple-protocols-8.md)

### Random Evaluation of a Polynomial

Polynomial identity testing is the instance of RandomQuery in which $M$ is the type of multivariate polynomials in $m$ variables over a field $\mathbb{F}$, a query is a point of $\mathbb{F}^m$ answered by evaluation, and $g = 0$. To test $P = Q$, take $f = P - Q$.

- [RandomEvaluation Oracle Reduction](def-random-evaluation.md)
- [RandomEvaluation Soundness](theorem-simple-protocols-9.md)

## Vanishing on a Finite Domain

Fix a field $\mathbb{F}$, a finite domain $H \subseteq \mathbb{F}$ with vanishing polynomial $Z_H(X) = \prod_{h \in H} (X - h)$, and a degree bound $d$ with $|H| \leq d$. The claims in this subsection are that polynomial oracles of degree at most $d$ vanish on $H$.

- [Quotient Zero Test](def-quotient-zero-test.md)
- [Quotient Zero Test Security](theorem-simple-protocols-10.md)

Several vanishing claims can be batched into one before running the zero test. A generator $G : S \to \mathbb{F}^k$ is $\varepsilon$-zero-evading if, for every nonzero $v \in \mathbb{F}^k$, a uniformly random seed $s \in S$ satisfies $\langle G(s), v \rangle = 0$ with probability at most $\varepsilon$.

- [Generator Batching](def-generator-batch.md)
- [Generator Batching Security](theorem-simple-protocols-11.md)
