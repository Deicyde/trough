---
declaration: theorem
origin: cited
lean: chapter28.claim2_divisible
statement: formalized
proof: formalized
---

# Claim

Suppose again $A \subset \{1, 2, \dots, 2n\}$ with $|A| = n+1$. Then there are always two numbers in $A$ such that one divides the other.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Pigeon-hole principle](../pigeon-hole-principle.md)

## Proof

Write every number $a \in A$ in the form $a = 2^k m$, where $m$ is an odd number between $1$ and $2n - 1$. Since there are $n + 1$ numbers in $A$, but only $n$ different odd parts, there must be two numbers in $A$ with the same odd part. Hence one is a multiple of the other.

## Lean

Formalized as [`chapter28.claim2_divisible`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.claim2_divisible).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 52](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L52)
