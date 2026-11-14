---
declaration: theorem
origin: cited
lean: infinity_of_primes₅
statement: formalized
---

# Fifth Proof

The set of primes $\mathbb{P}$ is infinite.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Consider the following curious topology on the set $\mathbb{Z}$ of integers. For $a, b \in \mathbb{Z}, b > 0$, we set

$$
N_{a,b} = \{a + nb : n \in \mathbb{Z}\}.
$$

Each set $N_{a,b}$ is a two-way infinite arithmetic progression. Now call a set $O \subseteq \mathbb{Z}$ open if either $O$ is empty, or if to every $a \in O$ there exists some $b > 0$ with $N_{a,b} \subseteq O$. Clearly, the union of open sets is open again. If $O_1, O_2$ are open, and $a \in O_1 \cap O_2$ with $N_{a,b_1} \subseteq O_1$ and $N_{a,b_2} \subseteq O_2$, then $a \in N_{a, b_1 b_2} \subseteq O_1 \cap O_2$. So we conclude that any finite intersection of open sets is again open. Therefore, this family of open sets induces a bona fide topology on $\mathbb{Z}$.

Let us note two facts:

- (A) Any nonempty open set is infinite.
- (B) Any set $N_{a,b}$ is closed as well.

Indeed, the first fact follows from the definition. For the second, we observe

$$
N_{a,b} = \mathbb{Z} \setminus \bigcup_{i=1}^{b-1} N_{a+i,b},
$$

which proves that $N_{a,b}$ is the complement of an open set and hence closed.

So far, the primes have not yet entered the picture — but here they come. Since any number $n \neq 1, -1$ has a prime divisor $p$, and hence is contained in $N_{0,p}$, we conclude

$$
\mathbb{Z} \setminus \{1, -1\} = \bigcup_{p \in \mathbb{P}} N_{0,p}.
$$

Now if $\mathbb{P}$ were finite, then $\bigcup_{p \in \mathbb{P}} N_{0,p}$ would be a finite union of closed sets (by (B)), and hence closed. Consequently, $\{1, -1\}$ would be an open set, in violation of (A).

## Lean

Stated as [`infinity_of_primes₅`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₅); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 108](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L108)
