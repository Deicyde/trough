---
declaration: lemma
origin: cited
---

# 477 lemma

If $Z$ and $W$ are simple, then $Z(W\cdots(WW))$ is simple.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Assume the contrary. Then we have 2 cases.

**Case 1: $W\cdots(WW)$ matches the pattern $y(x(y\cdots(yy)))$, with $k$ occurrences of $W$ ($k \le n$).** Since $|x(y\cdots(yy))| > n|y|$, but $|\cdots(WW)| \le (n-1)|W|$, this is impossible.

**Case 2: $Z(W\cdots(WW))$ matches the pattern $y(x(y\cdots(yy)))$.** Since $n \ge 3$, we have $Z = y = W$, so $|W\cdots(WW)| = n|W| = n|Z|$, contradicting $|x(y\cdots(yy))| > n|y|$.

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 154](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L154)
