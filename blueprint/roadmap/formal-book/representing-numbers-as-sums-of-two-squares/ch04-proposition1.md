---
declaration: proposition
origin: cited
lean: ch04.theorem₁
statement: formalized
---

# First proof

Every prime of the form $p = 4m + 1$ is a sum of two squares, that is, it can be written as $p = x^2 + y^2$ for some natural numbers $x,y \in \mathbb{N}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Lemma 1](ch04-lemma1.md)

## Proof

Consider the pairs $(x', y')$ of integers with $0 \leq x', y' \leq \sqrt{p}$, that is, $x', y' \in \{0, 1, \dots, \lfloor \sqrt{p} \rfloor\}$. There are $(\lfloor \sqrt{p} \rfloor + 1)^2$ such pairs. Using the estimate $\lfloor x \rfloor + 1 > x$ for $x = \sqrt{p}$, we see that we have more than $p$ such pairs of integers. Thus for any $s \in \mathbb{Z}$, it is impossible that all the values $x' - sy'$ produced by the pairs $(x', y')$ are distinct modulo $p$. That is, for every $s$ there are two distinct pairs

$$
(x', y'), (x'', y'') \in \{0, 1, \dots, \lfloor \sqrt{p} \rfloor\}^2
$$

with $x' - sy' \equiv x'' - sy'' \pmod{p}$. Now we take differences: We have $x' - x'' \equiv s(y' - y'') \pmod{p}$. Thus if we define $x := |x' - x''|$, $y := |y' - y''|$, then we get

$$
(x, y) \in
\{0, 1, \dots, \lfloor \sqrt{p} \rfloor\}^2 \quad \text{with} \quad x \equiv \pm sy \pmod{p}.
$$

Also we know that not both $x$ and $y$ can be zero, because the pairs $(x', y')$ and $(x'', y'')$ are distinct.

Now let $s$ be a solution of $s^2 \equiv -1 \pmod{p}$, which exists by Lemma 1. Then $x^2 \equiv s^2 y^2 = -y^2 \pmod{p}$, and so we have produced

$$
(x, y) \in
\mathbb{Z}^2 \quad \text{with} \quad
0 < x^2 + y^2 < 2p \quad \text{and} \quad x^2 + y^2 \equiv 0 \pmod{p}.
$$

But $p$ is the only number between $0$ and $2p$ that is divisible by $p$. Thus $x^2 + y^2 = p$: done!

## Lean

Stated as [`ch04.theorem₁`](https://mo271.github.io/FormalBook/docs/find/#doc/ch04.theorem₁); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter04.tex, line 54](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter04.tex#L54)
