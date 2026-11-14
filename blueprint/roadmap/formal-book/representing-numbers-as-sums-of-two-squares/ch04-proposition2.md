---
declaration: proposition
origin: cited
lean: ch04.theorem₂
statement: formalized
---

# Second proof

Every prime of the form $p = 4m + 1$ is a sum of two squares, that is, it can be written as $p = x^2 + y^2$ for some natural numbers $x,y \in \mathbb{N}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We study the set

$$
S := \{(x, y, z) \in \mathbb{Z}^3 : 4xy + z^2 = p, \ x > 0, \ y > 0\}.
$$

This set is finite. Indeed, $x \geq 1$ and $y \geq 1$ implies $y \leq \frac{p}{4}$ and $x \leq \frac{p}{4}$. So there are only finitely many possible values for $x$ and $y$, and given $x$ and $y$, there are at most two values for $z$.

1. The first linear involution is given by

    $$
    f : S \to S, \quad (x, y, z) \mapsto (y, x, -z),
    $$

    that is, “interchange $x$ and $y$, and negate $z$.” This clearly maps $S$ to itself, and it is an *involution*: Applied twice, it yields the identity. Also, $f$ has no fixed points, since $z = 0$ would imply $p = 4xy$, which is impossible. Furthermore, $f$ maps the solutions in

    $$
    T := \{(x, y, z) \in S : z > 0\}
    $$

    to the solutions in $S \setminus T$, which satisfy $z < 0$. Also, $f$ reverses the signs of $x - y$ and of $z$, so it maps the solutions in

    $$
    U := \{(x, y, z) \in S : (x - y) + z > 0\}
    $$

    to the solutions in $S \setminus U$. For this we have to see that there is no solution with $(x - y) + z = 0$, but there is none since this would give $p = 4xy + z^2 = 4xy + (x - y)^2 = (x + y)^2$.

    What do we get from the study of $f$? The main observation is that since $f$ maps the sets $T$ and $U$ to their complements, it also interchanges the elements in $T \setminus U$ with these in $U \setminus T$. That is, there is the same number of solutions in $U$ that are not in $T$ as there are solutions in $T$ that are not in $U$ — *so $T$ and $U$ have the same cardinality*.

2. The second involution that we study is an involution on the set $U$:

    $$
    g : U \to U, \quad (x, y, z) \mapsto (x - y + z, y, 2y - z).
    $$

    First we check that indeed this is a well-defined map: If $(x, y, z) \in U$, then $x - y + z > 0$, $y > 0$ and $4(x - y + z)y + (2y - z)^2 = 4xy + z^2$, so $g(x, y, z) \in S$. By $(x - y + z) - y + (2y - z) = x > 0$ we find that indeed $g(x, y, z) \in U$.

    Also $g$ is an involution: $g(x, y, z) = (x - y + z, y, 2y - z)$ is mapped by $g$ to $((x - y + z) - y + (2y - z), y, 2y - (2y - z)) = (x, y, z)$.

    And finally $g$ has exactly one fixed point:

    $$
    (x, y, z) = g(x, y, z) = (x - y + z, y, 2y - z)
    $$

    implies that $y = z$, but then $p = 4xy + y^2 = (4x + y)y$, which holds only for $y = z = 1$ and $x = \frac{p - 1}{4}$.

    But if $g$ is an involution on $U$ that has exactly one fixed point, then *the cardinality of $U$ is odd.*

3. The third, trivial, involution that we study is the involution on $T$ that interchanges $x$ and $y$:

    $$
    h : T \to T, \quad (x, y, z) \mapsto (y, x, z).
    $$

    This map is clearly well-defined, and an involution. We combine now our knowledge derived from the other two involutions: The cardinality of $T$ is equal to the cardinality of $U$, which is odd. But if $h$ is an involution on a finite set of odd cardinality, then it *has a fixed point*: There is a point $(x, y, z) \in T$ with $x = y$, that is, a solution of

    $$
    p = 4x^2 + z^2 = (2x)^2 + z^2.
    $$

## Lean

Stated as [`ch04.theorem₂`](https://mo271.github.io/FormalBook/docs/find/#doc/ch04.theorem₂); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter04.tex, line 94](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter04.tex#L94)
