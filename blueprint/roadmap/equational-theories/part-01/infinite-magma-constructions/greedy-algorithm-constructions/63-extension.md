---
declaration: lemma
origin: cited
---

# 63 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $a = b$, set $a \diamond' a = a$. This clearly does not destroy Laws 3 or 4, and because of Law 4, Law 2 will also be retained. Finally, using Law 4, we can check that this addition does not break Law 1.

Now suppose $a \neq b$. Let $d_1,d_2,..., d_n$ be all the elements with $b = a \diamond d_i$, and note from Law 3 and $a \neq b$ that we have the crucial inequality $d_i \neq a$ for all $i$. If $d_i \diamond a$ is defined, let $e_i = d_i \diamond a.$ From Law 4 and $d_i \neq a$, we have $e_i \neq d_i$. From Law 2 and $a \diamond d_i = a \diamond d_j$, we further have $e_i \neq e_j$ and $e_i \neq d_j$ for $i \neq j$.

For the algorithm, we set $a \diamond' b = c$ for some new $c$, $d_i \diamond' c = a$, and $c \diamond' e_i = d_i$ (This is well defined as we have just argued $e_i \neq e_j$ for $i \neq j$).

This creates a new partial function. Law 2 is verified as follows: The case $x=c$ cannot occur because $c \diamond' e_i \neq c \diamond' e_j$ for $i \neq j$. If $y=c$, then $x = d_i$ for some $i$, but then $y \diamond' x = c \diamond' d_i$ is undefined as $d_i \neq e_j$, so this case is vacuous. If $z=c$ and $x,y \neq c$, then similarly $z \diamond' x$ is undefined, and $y \diamond' x$ is not equal to $c = z$, so we are ok in this case also.

Law 3 is clearly unaffected, and it is also straightforward to check that Law 4 is also not invalidated (here it is essential that $d_i \neq a$).

Now we verify Law 1.

- Case 1: $x=c$. Then for $x \diamond' y$ to be defined we must have $y=e_i$ for some $i$, but then $x \diamond' (x \diamond' y) = c \diamond' d_i$ is undefined as $d_i \neq e_j$ for all $j$.
- Case 2: $y=c$. Then for $x \diamond' y$ to be defined we must have $x = d_i$ for some $i$. Then $d_i \diamond' (d_i \diamond' c)$ is either undefined or is equal to $e_i$, in which case Law 1 holds as $c \diamond' e_i = d_i$.
- Case 3: $x \diamond' y = c$. Then $x=a$ and $y=b$. Since $d_i \neq a$ for all $i$, $x \diamond (x \diamond y)$ is undefined.
- Case 4: $x \diamond' (x \diamond' y) = c$. Then $x = a$ and $y = d_i$ for some $i$, and Law 1 holds as $d_i \diamond' c = a$.
- Case 5: None of $x, y, x \diamond' y, x \diamond' (x \diamond' y)$ are equal to $c$. Then this case is covered by the previous seed.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 496](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L496)
