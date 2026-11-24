---
declaration: lemma
origin: cited
lean: big_shifts
statement: formalized
proof: formalized
---

# lots_of_diagonals

Let $A\subseteq G$ and $k\geq 1$ and $L\subseteq A^k$. Then there exists some ${\vec{a}}\in L$ such that

$$
\#\{ t\in G : {\vec{a}}+(t,\ldots,t)\in L\}\geq \frac{\lvert L\rvert}{\lvert A+S\rvert^k}\lvert S\rvert.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`big_shifts`](https://yaeldillies.github.io/apap/docs/find/#doc/big_shifts).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 112](https://github.com/YaelDillies/apap/blob/b401f6e22417e6dbe6f87d6620571ea6c513aed3/blueprint/src/chapter/ap.tex#L112)
