# Definition of the Noperthedron

We define three points $C_1,C_2,C_3\in \mathbb{Q}^3$.

$$
C_1:=
\frac{1}{259375205}
\begin{pmatrix}
{152024884} \\ 0 \\ {210152163}
\end{pmatrix},
\qquad
C_2:= \frac{1}{10^{10}}
\begin{pmatrix}
6632738028 \\ 6106948881 \\ 3980949609
\end{pmatrix},
$$

$$
C_3:=
\frac{1}{10^{10}}
\begin{pmatrix}
8193990033 \\ 5298215096 \\ 1230614493
\end{pmatrix}.
$$

- [c1_c2_c3_norms](lem-c1-c2-c3-norms.md)

The rotation about the $z$ axis by the angle $\alpha$ is

$$
R_z(\alpha):=
\begin{pmatrix}
\cos\alpha & -\sin\alpha &0\\
\sin\alpha & \cos\alpha &0\\
0 & 0 & 1
\end{pmatrix}.
$$

We define a 30-element set $\mathcal{C}_{30}$

$$
\mathcal{C}_{30} := \left\{(-1)^\ell R_z\left(\frac{2\pi k}{15}\right) \colon k=0,\dots,14; \ell=0,1\right\}.
$$

of rotations.

We write $\mathcal{C}_{30} \cdot P = \{c P \,\text{ for } \, c \in \mathcal{C}_{30}\}$ for the orbit of $P$ under the action of $\mathcal{C}_{30}$.

- [noperthedron](def-noperthedron.md)
- [nopert_verts_norm_le_one](lemma-nopert-verts-norm-le-one.md)
- [pointsymmetric](def-pointsymmetric.md)
- [nopert_point_symmetric](lemma-nopert-point-symmetric.md)
- [nopert_interior](lemma-nopert-interior.md)
