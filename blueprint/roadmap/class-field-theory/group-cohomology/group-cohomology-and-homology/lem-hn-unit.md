---
declaration: lemma
origin: cited
lean: Rep.instTrivialCohomologyOfSubsingleton
statement: formalized
proof: formalized
---

# Hn unit

If $G$ is the trivial group then for all $n>0$, $H^n(G,M)\cong 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Each of the modules $C^n(G,M)$ may be identified with $M$, and the coboundary maps reduce to alternating sums of the form $d^n(m) = \sum_{i=0}^{n+1} (-1)^i m$. Hence $d^n$ is the identity map for odd $n$, and is the zero map for even $m$. It follows that the image of $d^n$ is equal to the kernel of $d^{n+1}$.

## Lean

Formalized as [`Rep.instTrivialCohomologyOfSubsingleton`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.instTrivialCohomologyOfSubsingleton).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 119](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L119)
