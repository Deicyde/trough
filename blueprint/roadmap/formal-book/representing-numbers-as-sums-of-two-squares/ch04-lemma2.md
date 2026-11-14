---
declaration: lemma
origin: cited
lean: ch04.lemma₂
statement: formalized
proof: formalized
---

# Lemma 2

No number $n = 4m + 3$ is a sum of two squares.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The square of any even number is $(2k)^2 = 4k^2 \equiv 0 \pmod{4}$, while squares of odd numbers yield $(2k + 1)^2 = 4(k^2 + k) + 1 \equiv 1 \pmod{4}$. Thus any sum of two squares is congruent to $0$, $1$ or $2 \pmod{4}$.

## Lean

Formalized as [`ch04.lemma₂`](https://mo271.github.io/FormalBook/docs/find/#doc/ch04.lemma₂).

## Sources

- [Formal Book blueprint: chapter/chapter04.tex, line 41](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter04.tex#L41)
