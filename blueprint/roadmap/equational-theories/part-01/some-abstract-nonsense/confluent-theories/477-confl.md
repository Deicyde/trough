---
declaration: theorem
origin: cited
---

# 477 confluent

[E477](https://teorth.github.io/equational_theories/implications/?477) $({x = y \diamond (x \diamond (y \diamond (y \diamond y)))})$ is confluent.

## Depends on

- [Confluent theory](confluent-theory.md)
- [Equation 477](../../selected-laws/part-02/eq477.md)

## Proof depends on

- [477 lemma](477-lemma.md)

## Proof

See the notes [here](https://www.overleaf.com/project/66f847bb14d0d8f0b77f74e1). A sketch of proof is as follows. We induct on the length of the term. As before we consider terms of the form $XY$. Also, in both sequences if a simplification is applied to the whole term, then we can assume the sequence is simply final.

By [477 lemma](477-lemma.md), if any of the two sequences is final, then right before the last step, the two factors of the outermost product are both simple. This is also true for the result of the non-final sequence. By the induction hypothesis, they can be identified correspondingly, so the two sequences are either both final or both non-final, and in the first case, the same simplification is applied to give the same result.

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 136](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L136)
