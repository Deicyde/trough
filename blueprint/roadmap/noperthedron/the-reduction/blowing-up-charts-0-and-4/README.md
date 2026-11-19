# Blowing up charts 0 and 4

The aligned poses of the reduced domain are exactly those with $r = 0$ in charts 0 and 4 (where $Q = I$ or $Q = \tau$). Near $r = 0$ the separation margin tends to zero, so these two charts are blown up: $r$ is written as $\rho\, c$ with $c$ on a face of the cube $[-1,1]^3$ and $\rho = \max_i |r_i|$.

The geometric idea of this real, directional *blow-up* is to separate the size of $r$ from its direction, as in polar coordinates. For $r\ne0$, the direction is $c=r/\rho$. At $\rho=0$, all directions represent the same original vector $r=0$, but the blown-up space retains them as distinct boundary points. Thus, for each fixed outer view, the origin in the relative-rotation coordinates is replaced by the surface of a cube recording the possible directions of approach.

For example, on the positive first-coordinate face, write

$$
c=(1,s_0,s_1), \qquad r=(\rho,\rho s_0,\rho s_1),
\qquad -1\le s_0,s_1\le1.
$$

The other five faces cover the other directions. There are still five continuous parameters: $(u,v,s_0,s_1,\rho)$, together with the discrete chart and face labels. Using cube faces makes the direction coordinates range over squares and keeps the substitution polynomial, which suits the box certificates.

- [faces](def-faces.md)
- [exists_face](lem-exists-face.md)
