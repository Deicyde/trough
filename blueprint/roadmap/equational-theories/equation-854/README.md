# Equation 854

In this chapter we study magmas that satisfy [E854](https://teorth.github.io/equational_theories/implications/?854), thus

$$
x = x \diamond ((y \diamond z) \diamond (x \diamond z))
$$

for all $x,y,z$. In particular we have

$$
x = x \diamond (x \diamond z)^2;
$$

substituting $z = (x \diamond x)^2$ we have in particular that

$$
x = x \diamond x^2.
$$

We then have

$$
\begin{aligned}
y &= y \diamond ((x \diamond y) \diamond y^2) \\
& = (y \diamond y^2) \diamond ((x \diamond y) \diamond y^2)
\end{aligned}
$$

and thus by another application of 854 we conclude the useful law

$$
(x \diamond y) \diamond y = x \diamond y
$$

(equation 378). We introduce the notation $y \to x$ to denote the relation that $x = z \diamond y$ for some $z$, then from 378 we see that

$$
y \to x \iff x = x \diamond y.
$$

From 854 we have

$$
(y \diamond z) \diamond (x \diamond z) \to x
$$

for all $x,y,z$.

Now let $X$ be an alphabet, and $M_X$ the free magma. We let $\Gamma$ be the theory consisting just of the law 854, then as in [Existence and uniqueness of free magmas](../some-abstract-nonsense/freemag-exist.md) we have the equivalence relation $\sim$ on $M_X$ defined by setting $w \sim w'$ iff $\Gamma \models w \simeq w'$, then $M_X/\sim$ is a free magma for $\Gamma$. We can then also define a directed graph on $M_X$ by declaring $w' \to w$ if $w \sim w'' \diamond w'$ for some $w''$, or equivalently (by applying yx to $M_X/\sim$) that $w \sim w \diamond w'$.

Call a word $w$ *irreducible* if it is not of the form $w = w_1 \diamond w_2$ with $w_2 \to w_1$, and *reducible* otherwise. Clearly if a word $w = w_1 \diamond w_2$ is reducible, then it is equivalent to the shorter word $w_1$. Iterating, we conclude that every word is equivalent to an irreducible word. Such a word is either a generator in $X$, or else a product $w_1 \to w_2$ with $w_2 \not \to w_1$.

We can describe the words equivalent to an irreducible word as follows.

- [Description of equivalence](irred-desc.md)
- [Unique factorization](unique-factorization.md)
- [Description of graph](graph-desc.md)
- [854 does not imply 3316, 3925](854-anti.md)
- [Some further properties of 854 magmas](some-further-properties-of-854-magmas/README.md)
- [Running a greedy algorithm](running-a-greedy-algorithm/README.md)
- [The free 854 magma](the-free-854-magma/README.md)
