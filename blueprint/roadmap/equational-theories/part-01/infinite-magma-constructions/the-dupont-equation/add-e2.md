---
declaration: lemma
origin: cited
---

# Promoting to $E_2$

If $(E_1,E_2,f)$ is a partial solution and $h \in (\mathbb{Z}^3 \times \mathbb{Z}) \backslash E_2$, then there exists an extension $(E'_1,E'_2,f')$ of $(E_1,E_2,f)$ such that $h \in E'_2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $\tilde E_2$ denote the set $E_2$ together with all elements of the form

$$
-h', h' - f^2(h'), f^2(h') - h'\qquad\text{(2)}
$$

for some $h' \in E_2 \backslash E_1$; this is $\mathbb{Z}^3$ with a finite number of elements attached, and is symmetric around the origin.

First suppose that $h$ lies outside of $\tilde E_2$. Then we can find $a \in \mathbb{Z}^3$ such that the quantities

$$
-h, \pm (h - Ta)
$$

are distinct from each other, and lie outside of $\tilde E_2$. We now promote $h$ to $E_2$, thus setting

$$
E'_1 := E_1
$$

and

$$
E'_2 := E_2 \cup \{h\}
$$

and define an extension $f'$ of $f$ to $E'_2$ by setting

$$
f'(h) := a.
$$

It is then a routine matter to check that $(E'_1,E'_2,f')$ is an extension of $(E_1,E_2,f)$.

Now suppose that $h$ lies in $\tilde E_2$. Then $h$ is of one of the forms (2) for some $h' \in E_2 \backslash E_1$. Suppose it is of the form $-h'$ or $f^2(h') - h'$. We invoke [Promoting to $E_1$](add-e1.md) to promote $h'$ to $E_1$ by using a suitable extension $(E'_1,E'_2,f')$; and now $h$ will lie in $E'_2$, giving the claim. If instead $h$ is of the form $h'-f^2(h')$, then this procedure might not place $h$ in $E'_2$; but if it does not, it will be of the form $-h''$ for $h'' = f^2(h')-h' \in E'_2 \backslash E'_1$. Applying [Promoting to $E_1$](add-e1.md) one more time to now promote $h''$ to $E_1$, we will obtain a larger extension $(E''_1,E''_2,f'')$ with $h \in E''_2$, giving the claim.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 749](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L749)
