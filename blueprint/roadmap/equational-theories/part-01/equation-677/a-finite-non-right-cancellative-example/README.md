# A finite non-right-cancellative example

Suppose $G$ is already a 677 magma, and to each pair $x,y \in G$ we assign a binary operation $\diamond_{x,y}: M \times M \to M$ such that one has the functional equation

$$
s = t \diamond_{y,L_y^{-1} x} (s \diamond_{x, (y \diamond x) \diamond y} ((t \diamond_{y,x} s) \diamond_{y \diamond x, y} t))\qquad\text{(1)}
$$

for all $x,y \in G$, then the operation

$$
(x,s) \diamond (y,t) := (x \diamond y, s \diamond_{x,y} t)
$$

is easily seen to be a 677 magma. It is right-injective if $G$ and all of the $\diamond_{y,x}$ are right-injective.

Suppose $M$ is a field that admits a primitive cube root of unity $\omega$ as well as a primitive fifth root of unity $\zeta$ (for instance, $M$ could be a field of size $16$). Then the three operations

$$
s \diamond^0 t := s - \zeta(t-s)
$$

$$
s \diamond^+ t := t
$$

$$
s \diamond^- t := s - \omega(t-s)
$$

can easily be seen to satisfy the identities

$$
s = t \diamond^0 (s \diamond^0 ((t \diamond^0 s) \diamond^0 t))
$$

$$
s = t \diamond^+ (s \diamond^+ ((t \diamond^- s) \diamond^- t))
$$

$$
s = t \diamond^- (s \diamond^- ((t \diamond^+ s) \diamond^+ t))
$$

for all $t,s$.

Now suppose that $G$ is also a field with a primitive fifth root of unity $\beta$ (so that $\beta = \left(\beta^{-2}\right)^2 = \beta^{-4}$ is a square), but $-1$ and $\beta+1$ are non-zero non-squares (for instance, $G$ could be the field of size $31$, with $\beta=2$). If we define $x \diamond y = x - \beta(y-x)$, and then define $\diamond_{x,y}$ to be $\diamond^0$ when $y=x$, $\diamond^+$ when $y-x$ is a non-zero square, and $\diamond^-$ when $y-x$ is a non-zero non-square, one can then check that (1) holds. Since $\diamond^0$ is not right-cancellative, this gives a finite 677 magma that is not right-cancellative.
