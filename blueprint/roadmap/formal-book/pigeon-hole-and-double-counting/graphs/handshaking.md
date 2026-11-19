---
declaration: lemma
origin: cited
lean: chapter28.handshaking
statement: formalized
proof: formalized
---

# Handshaking

Let $G$ be a finite simple graph with vertex set $V$ and edge set $E$ and let $d(v)$ denote the degree of a vertex $v$. Then

$$
\sum_{v\in V}d(v) = 2|E|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For the proof consider $S \subseteq V \times E$, where $S$ is the set of pairs $(v, e)$ such that $v \in V$ is an end-vertex of $e \in E$. Counting $S$ in two ways gives on the one hand $\sum_{v \in V} d(v)$, since every vertex contributes $d(v)$ to the count, and on the other hand $2|E|$, since every edge has two ends.

## Lean

Formalized as [`chapter28.handshaking`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.handshaking).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 213](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L213)
