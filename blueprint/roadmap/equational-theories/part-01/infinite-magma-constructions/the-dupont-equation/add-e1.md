---
declaration: lemma
origin: cited
---

# Promoting to $E_1$

If $(E_1,E_2,f)$ is a partial solution and $h \in E_2 \backslash E_1$, then there exists an extension $(E'_1,E'_2,f')$ of $(E_1,E_2,f)$ such that $h \in E'_1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This will be a greedy construction, but we have to introduce a rather large number of additional elements to ensure that certain non-degeneracy conditions are maintained (in particular, the new elements $h'$ introduced have to be such that $f^2(h') - h'$ avoids $E_2$ and hence $\mathbb{Z}^3$, which requires a certain amount of complexity in the construction).

Let $\tilde E_2$ denote the set $E_2$ together with all the elements of the form $-h'$, $h' - f^2(h')$, and $f^2(h') - h'$ for $h' \in E_2 \backslash E_1$; this is $\mathbb{Z}^3$ with a finite number of additional elements.

Let $a$ be an element of $\mathbb{Z}^3$ such that the quantities

$$
\pm Ta, \pm(Ta + a)
$$

are distinct from each other and from

$$
0, \pm h, \pm (h - f(h)), \pm (f^2(h)-h);
$$

this is possible since $T, T+1$ are invertible.

Next, we pick an $x \in \mathbb{Z}^3 \times \mathbb{Z}$ such that the quantities

$$
\pm x, \pm x + Ta, \pm x - Ta, \pm 2 x + Ta, \pm x + Ta + a, \pm (h + x), \pm (h - f(h) + x), \pm (f^2(h)-h + x + Ta)
$$

are all distinct from each other and from $\tilde E_2$; indeed, from the choice of $a$ (and the non-zero nature of $h$, $f(h)$, $h-f(h)$, and $f^2(h)-h$) there are only finitely many $x$ for which a collision can occur between any pair of these expressions.

We now promote $\pm h, \pm x, \pm x + Ta, \pm x - Ta$ to $E_1$, and also promote $h+x$, $h - f^2(h)$, $\pm 2x + Ta$, $\pm x + Ta + a$ to $E_2$. That is to say, we define

$$
E'_1 := E_1 \cup \{\pm h, \pm x, \pm x + Ta, \pm x - Ta\}
$$

and

$$
E'_2 := E_2 \cup \{ -h, \pm x, \pm x + Ta, \pm x - Ta, h + x, h - f^2(h), \pm 2x + Ta \}.
$$

We then define an extension $f'$ of $f$ to $E'_2$ by setting

$$
\begin{aligned}
f'(\pm x) &:= a \\
f'(\pm x + Ta) &:= \pm x \\
f'(\pm x - Ta) &:= \mp x + Ta \\
f'(\pm x + Ta + a) &:= \pm x - Ta \\
f'(\pm 2x + Ta) &:= \pm x + Ta \\
f'(\pm x + Ta + a) &:= \pm x - Ta \\
f'(-h) &:= x + Ta \\
f'(h+x) &:= h \\
f'(h - f^2(h)) &:= -h.
\end{aligned}
$$

It is easy to see that $(E'_1,E'_2,f')$ satisfies properties (a), (b), (d). By construction, we have

$$
f'( (f')^2(h') - h') = -h'
$$

for

$$
h' = \pm h, \pm x, \pm x+Ta, \pm x-Ta
$$

giving property (c). By construction, the quantities

$$
-h', h' - f^2(h'), f^2(h') - h'
$$

are distinct from each other and lie outside of $\tilde E_2 \cup E'_2$ for

$$
h' = h+x, h - f^2(h), \pm 2x + Ta, \pm x + Ta + a
$$

while these quantities are distinct from each other and lie in $\tilde E_2 \backslash E'_2$ for $h' \in E_2 \backslash E'_1$ (note that this forces $h' \neq \pm h$). This gives property (e).

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 704](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L704)
