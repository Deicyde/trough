---
declaration: theorem
origin: cited
lean: chapter30.hall_marriage
statement: formalized
proof: formalized
---

# Hall's marriage theorem

Let $A_1, \dots A_n$ be a collection of subsets of a finite set $X$. Then there exists a system of distinct representatives if and only if the union of any $m$ sets $A_i$ contains at least $m$ elements, for $1 \le m \le n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Necessity is clear: the $m$ distinct representatives of any $m$ sets must lie in their union.

For sufficiency, we use induction on $n$. **Case 1:** If Hall's condition holds strictly ($|\bigcup_{i \in S} A_i| \ge |S| + 1$ for every proper nonempty $S \subsetneq \{1,\dots,n\}$), pick any $a_1 \in A_1$ as representative, remove $a_1$ from all sets, and verify that Hall's condition still holds for $A_2 \setminus \{a_1\}, \dots, A_n \setminus \{a_1\}$.

**Case 2:** If some proper nonempty subset $S$ is “tight” ($|\bigcup_{i \in S} A_i| = |S|$), first find an SDR for the subfamily $(A_i)_{i \in S}$ by induction. Then show that the remaining sets $(A_j)_{j \notin S}$, with the chosen representatives removed, still satisfy Hall's condition (using tightness of $S$), and apply induction again.

## Lean

Formalized as [`chapter30.hall_marriage`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter30.hall_marriage).

## Sources

- [Formal Book blueprint: chapter/chapter30.tex, line 59](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter30.tex#L59)
