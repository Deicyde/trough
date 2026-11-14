---
declaration: theorem
origin: cited
lean: chapter30.sperner
statement: formalized
proof: formalized
---

# Sperner's theorem

The size of a largest antichain of an $n$-set is $\binom{n}{\lfloor n/2\rfloor}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We follow Lubell's elegant proof via the LYM inequality. Consider all $n!$ permutations $\sigma$ of $\{1,\dots,n\}$, each generating a maximal chain $\{\sigma(1)\} \subset \{\sigma(1),\sigma(2)\} \subset \cdots \subset \{1,\dots,n\}$. A $k$-element set $A$ appears in exactly $k!(n-k)!$ of these chains. Since an antichain $\mathcal{F}$ meets each chain in at most one set, summing over $\mathcal{F}$ gives

$$
\sum_{A \in \mathcal{F}} k_A!(n-k_A)! \le n!,
$$

i.e. $\sum_{A \in \mathcal{F}} \frac{1}{\binom{n}{|A|}} \le 1$ (the *LYM inequality*). Since each summand is at least $1/\binom{n}{\lfloor n/2\rfloor}$, we conclude $|\mathcal{F}| \le \binom{n}{\lfloor n/2\rfloor}$.

## Lean

Formalized as [`chapter30.sperner`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter30.sperner).

## Sources

- [Formal Book blueprint: chapter/chapter30.tex, line 4](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter30.tex#L4)
