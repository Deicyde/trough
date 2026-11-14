---
declaration: theorem
origin: cited
lean: chapter28.brouwer_fixed_point_2d
statement: formalized
proof: formalized
---

# Brouwer's Fixed Point Theorem (for $n = 2$)

Every continuous function $f : B^2 \to B^2$ of a $2$-dimensional ball to itself has a fixed point (a point $x \in B^2$ with $f(x) = x$).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Sperner's Lemma](sperner.md)

## Proof

Let $\Delta$ be the triangle in $\mathbb{R}^3$ with vertices $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, and $e_3 = (0,0,1)$. It suffices to prove that every continuous map $f : \Delta \to \Delta$ has a fixed point, since $\Delta$ is homeomorphic to $B^2$.

We use $\delta(T)$ to denote the maximal length of an edge in a triangulation $T$. One can easily construct an infinite sequence of triangulations $T_1, T_2, \dots$ of $\Delta$ such that the sequence of maximal diameters $\delta(T_k)$ converges to $0$ (for example by iterated barycentric subdivision).

For each of these triangulations, we define a $3$-coloring of their vertices $v$ by setting $\lambda(v) := \min\{i : f(v)_i < v_i\}$, that is, $\lambda(v)$ is the smallest index $i$ such that the $i$-th coordinate of $f(v) - v$ is negative. If this smallest index $i$ does not exist, then we have found a fixed point and are done: To see this, note that every $v \in \Delta$ lies in the plane $x_1 + x_2 + x_3 = 1$, hence $\sum_i v_i = 1$. So if $f(v) \neq v$, then at least one of the coordinates of $f(v) - v$ must be negative (and at least one must be positive).

Let us check that this coloring satisfies the assumptions of Sperner's lemma. First, the vertex $e_i$ must receive color $i$, since the only possible negative component of $f(e_i) - e_i$ is the $i$-th component. Moreover, if $v$ lies on the edge opposite to $e_i$, then $v_i = 0$, so the $i$-th component of $f(v) - v$ cannot be negative, and hence $v$ does not get the color $i$.

Sperner's lemma now tells us that in each triangulation $T_k$ there is a tricolored triangle $\{v^{k:1}, v^{k:2}, v^{k:3}\}$ with $\lambda(v^{k:i}) = i$. Since the simplex $\Delta$ is compact, some subsequence of $(v^{k:1})_{k \geq 1}$ has a limit point $v$. The distances of $v^{k:2}$ and $v^{k:3}$ from $v^{k:1}$ are at most the mesh length $\delta(T_k) \to 0$, so all three sequences converge to the same point $v$.

But where is $f(v)$? We know that the first coordinate of $f(v^{k:1})$ is smaller than that of $v^{k:1}$ for all $k$. Now since $f$ is continuous, we derive that the first coordinate of $f(v)$ is smaller or equal to that of $v$. The same reasoning works for the second and third coordinates. Thus none of the coordinates of $f(v) - v$ is positive — and we have already seen that this contradicts the assumption $f(v) \neq v$.

## Lean

Formalized as [`chapter28.brouwer_fixed_point_2d`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.brouwer_fixed_point_2d).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 368](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L368)
