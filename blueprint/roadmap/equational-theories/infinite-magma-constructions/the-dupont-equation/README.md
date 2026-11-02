# The Dupont equation

Now we consider the Dupont equation, [E63](https://teorth.github.io/equational_theories/implications/?63) $({x = y \diamond (x \diamond (x \diamond y))})$, which can be treated by a greedy translation invariant construction that is more complicated than the one considered for the Asterix law in [The Asterix equation](../the-asterix-equation/README.md).

If we adopt a translation-invariant model

$$
x \diamond y = x + f(y-x)
$$

on some abelian group $G$, then with $y = x+h$, we have

$$
x \diamond y = x + f(h)
$$

$$
x \diamond (x \diamond y) = x + f^2(h)
$$

$$
y \diamond (x \diamond (x \diamond y)) = y + f(f^2(h)-h)
$$

and so the Dupont law $x = y \diamond (x \diamond (x \diamond y))$ becomes the functional equation

$$
f(f^2(h)-h) = -h.
$$

One way to solve this equation is to have an automorphism $T: G \to G$ that satisfies the identity

$$
T^3 - T = -I,
$$

then one can just take $f(h) = T(h)$. For instance, if $G = \mathbb{Z}^3$, one can take the automorphism $T: \mathbb{Z}^3 \to \mathbb{Z}^3$ defined by

$$
T(x,y,z) := (-z,x+z,y).
$$

We now extend this greedily to $\mathbb{Z}^3 \times \mathbb{Z}$ as follows. Define a *partial solution* $(E_1,E_2,f)$ to be a pair $\mathbb{Z}^3 \subseteq E_1 \subseteq E_2 \subseteq \mathbb{Z}^3 \times \mathbb{Z}$, and a function $f: E_2 \to E_1$ satisfying the following axioms.

- **(a)** The set $E_2 \backslash \mathbb{Z}^3$ is finite.
- **(b)** For $h \in \mathbb{Z}^3$, $f(h) = Th$; in particular, $f$ is a bijection on $\mathbb{Z}^3$.
- **(c)** For $h \in E_1 \backslash \mathbb{Z}^3$, $f(h) \in E_1$. Also, $-h + f^2(h) \in E_1$ and $f(-h + f^2(h)) = -h$. Note that this (and (b)) implies that $-h \in E_1$, thus $E_1$ is symmetric around the origin.
- **(d)** For $h \in E_2 \backslash E_1$, $f(h) \in E_1$.
- **(e)** The elements $-h$, $h - f^2(h)$, and $f^2(h) - h$ for $h \in E_2 \backslash E_1$ are all distinct from each other, and all lie outside of $E_2$. In particular this forces $f^2(h) \neq 0$, hence $f(h) \neq 0$. It also forces $f^2(h) \neq h$, hence $f(h) \neq h$.

Thus for instance one can take $(\mathbb{Z}^3,\mathbb{Z}^3,T)$ as a partial solution. We say that a partial solution $(E'_1, E'_2, f')$ is an *extension* of $(E_1,E_2,f)$ if $E_1 \subseteq E'_1$, $E'_2 \subseteq E_2$, and $f'$ agrees with $f$ on $E_2$.

Informally, $E_1$ represents the portion of $\mathbb{Z}^3 \times \mathbb{Z}$ where we have completely resolved the Dupont equation; the set $E_2 \backslash E_1$ represents the portion for which $f$ (and all forward iterates of $f$) have been defined, but the Dupont equation has not yet been verified; and the elements $-h$, $h - f^2(h)$, and $f^2(h) - h$ for $h \in E_2 \backslash E_1$ are the portion where $f$ is not yet defined, but for which one is ready to “promote” these elements to $E_2$ or $E_1$ by defining $f$ appropriately.

The key lemmas are then

- [Promoting to $E_1$](add-e1.md)
- [Promoting to $E_2$](add-e2.md)
- [Seed solution](finite-check.md)
- [Extension](extension-lemma.md)
- [Greedy completion of Dupont](dupont-iter.md)
- [Non-injective Dupont solution](non-inject.md)
