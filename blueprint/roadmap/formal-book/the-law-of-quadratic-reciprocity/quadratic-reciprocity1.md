---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.quadratic_reciprocity_1
statement: formalized
---

# Quadratic reciprocity I

Let $p$ and $q$ be different odd primes. Then

$$
(\frac{q}{p})(\frac{p}{q}) = (-1)^{\frac{p-1}{2} \frac{q-1}{2}}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The key to our first proof is a counting formula given by Lemma of Gauss. Let $p$ and $q$ be odd primes, and consider $(\frac{q}{p})$. Suppose $iq$ is a multiple of $q$ that reduces to negative residue $r_i < 0$ in the Lemma of Gauss. This means that there is a unique integer $j$ such that $-\frac{p}{2} < iq-jp < 0$. Note that $0 < j < \frac{q}{2}$ since $0 < i < \frac{p}{2}$. In other words, $(\frac{q}{p}) = (-1)^s$, where $s$ is the number of lattice points $(x, y)$, that is, pairs of integers $x$, $y$ satisfying

$$
0 < py - qx < \frac{p}{2}, \quad 0 < x < \frac{p}{2}, \quad 0 < y < \frac{q}{2}.\qquad\text{(2)}
$$

Similarly, $(\frac{p}{q}) = (-1)^t$ where $t$ is the number of lattice points $(x, y)$ with

$$
0 < qx - py < \frac{q}{2}, \quad 0 < x < \frac{p}{2}, \quad 0 < y < \frac{q}{2}.\qquad\text{(3)}
$$

Now look at the rectangle with side lengths $\frac{p}{2}$, $\frac{q}{2}$, and draw the two lines parallel to the diagonal $py = qx$, $y = \frac{q}{p}x + \frac{1}{2}$ or $py - qx = \frac{p}{2}$, respectively, $y = \frac{q}{p} \left(x - \frac{1}{2}\right)$ or $qx - py = \frac{q}{2}$.

The proof is now quickly completed by the following three observations:

1. There are no lattice points on the diagonal and the two parallels. This is so because $py = qx$ would imply $p \mid x$, which cannot be. For the parallels observe that $py - qx$ is an integer while $\frac{p}{2}$ and $\frac{q}{2}$ are not.
2. The lattice points observing (2) are precisely the points in the upper strip $0 < py - qx < \frac{p}{2}$, and those of (3) the points in the lower strip $0 < qx - py < \frac{q}{2}$. Hence the number of lattice points in the two strips is $s + t$.
3. The outer regions $R : py - qx > \frac{p}{2}$ and $S: qx - py > \frac{q}{2}$ contain the *same* number of points. To see this consider the map $\varphi: R \to S$ which maps $(x, y)$ to $\left(\frac{p+1}{2} - x, \frac{q+1}{2} - y\right)$ and check that $\varphi$ is an involution.

Since the total number of lattice points in the rectangle is $\frac{p-1}{2} \cdot \frac{q-1}{2}$, we infer that $s + t$ and $\frac{p-1}{2} \cdot \frac{q-1}{2}$ have the same parity, and so

$$
(\frac{q}{p}) (\frac{p}{q}) = (-1)^{s+t} = (-1)^{\frac{p-1}{2} \frac{q-1}{2}}. \qedhere
$$

## Lean

Stated as [`book.quadratic_reciprocity.quadratic_reciprocity_1`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.quadratic_reciprocity_1); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 87](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L87)
