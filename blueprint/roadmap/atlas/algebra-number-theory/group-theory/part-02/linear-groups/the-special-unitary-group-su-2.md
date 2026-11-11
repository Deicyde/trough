---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SU2Longitude.diagRotation, MathlibExt.GroupTheory.SU2Longitude.diagRotation_eq_diagonal, MathlibExt.GroupTheory.SU2Longitude.star_diagRotation, MathlibExt.GroupTheory.SU2Longitude.diagRotation_mem_specialUnitaryGroup, MathlibExt.GroupTheory.SU2Longitude.diagRotation_int_mul_two_pi, MathlibExt.GroupTheory.SU2Longitude.diagRotation_add_int_mul_two_pi, MathlibExt.GroupTheory.SU2Longitude.longitudeSubgroup, MathlibExt.GroupTheory.SU2Longitude.diagRotationToLongitude
statement: formalized
proof: formalized
---

# The special unitary group SU(2)

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html).

## Diagonal rotation

For a real number $\theta$, the diagonal rotation through $\theta$ is
the $2 \times 2$ complex diagonal matrix $\operatorname{diag}(e^{i\theta}, e^{-i\theta})$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation).

## Diagonal rotations as diagonal matrices

For every real number $\theta$, the diagonal
rotation through $\theta$ is the diagonal matrix whose diagonal entries are $e^{i\theta}$ and
$e^{-i\theta}$, in that order.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation_eq_diagonal`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-eq-diagonal).

## Conjugate transpose of a diagonal rotation

For every real number $\theta$, the conjugate
transpose of the diagonal rotation through $\theta$ is the diagonal rotation through $-\theta$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.star_diagRotation`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#star-diag-rotation).

## Diagonal rotations lie in $\mathrm{SU}(2)$

For every real number $\theta$, the
diagonal rotation through $\theta$ is a $2 \times 2$ complex matrix that is unitary and has
determinant $1$, that is, it lies in $\mathrm{SU}(2)$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation_mem_specialUnitaryGroup`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-mem-special-unitary-group).

## Diagonal rotation through a multiple of $2\pi$

For every integer $n$, the diagonal
rotation through $2\pi n$ is the $2 \times 2$ identity matrix.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation_int_mul_two_pi`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-int-mul-two-pi).

## Diagonal rotations are $2\pi$-periodic

For every real number $\theta$ and every integer
$n$, the diagonal rotation through $\theta + 2\pi n$ equals the diagonal rotation through
$\theta$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation_add_int_mul_two_pi`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-add-int-mul-two-pi).

## Longitude subgroup

The longitude subgroup of $\mathrm{SU}(2)$ is the subgroup of those
elements of $\mathrm{SU}(2)$ that are the diagonal rotation through $\theta$ for some real number
$\theta$.

It is the longitude $\mathrm{Long}_i$ at the equator point $i$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeSubgroup`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-subgroup).

## Diagonal rotation as a longitude element

For a real number $\theta$, the diagonal
rotation through $\theta$, regarded as an element of the longitude subgroup of
$\mathrm{SU}(2)$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotationToLongitude`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-to-longitude).

## Longitude elements multiply by adding angles

For real numbers $a$ and $b$, in the
longitude subgroup the product of the diagonal rotations through $a$ and through $b$ is the
diagonal rotation through $a + b$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotationToLongitude_mul`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-to-longitude-mul).

## Equal rotation matrices give equal longitude elements

For real numbers $a$ and $b$, if
the diagonal rotations through $a$ and through $b$ are equal as matrices, then the elements of
the longitude subgroup given by the diagonal rotations through $a$ and through $b$ are
equal.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotationToLongitude_eq_of_diagRotation_eq`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-to-longitude-eq-of-diag-ro).

## The angle homomorphism into the longitude subgroup

The homomorphism from the additive
group $\mathbb{R}$ to the longitude subgroup, written additively, that sends a real number
$\theta$ to the diagonal rotation through $\theta$, regarded as an element of the longitude
subgroup.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotationToLongitudeHom`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-to-longitude-hom).

## Longitude map

The longitude map is the group homomorphism from the circle group
$\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, to the longitude subgroup of $\mathrm{SU}(2)$
that sends the class of a real number $\theta$ to the diagonal rotation through $\theta$, that is,
to $\cos\theta \cdot I + \sin\theta \cdot \operatorname{diag}(i, -i) =
\operatorname{diag}(e^{i\theta}, e^{-i\theta})$, where $I$ is the $2 \times 2$ identity matrix.
It is well defined because diagonal rotations are $2\pi$-periodic.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMap`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-map).

## The longitude map on the class of an angle

For every real number $\theta$, the longitude
map sends the class of $\theta$ in $\mathbb{R}/2\pi\mathbb{Z}$ to the diagonal rotation through
$\theta$, regarded as an element of the longitude subgroup.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMap_apply_ofAdd_mk`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-map-apply-of-add-mk).

## When two diagonal rotations are equal

For real numbers $a$ and $b$, the diagonal
rotations through $a$ and through $b$ are equal if and only if $a = b + 2\pi n$ for some
integer $n$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.diagRotation_eq_diagRotation_iff`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-rotation-eq-diag-rotation-iff).

## Every point of $\mathbb{R}/2\pi\mathbb{Z}$ comes from a real angle

Every element $x$ of
the circle group $\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, is the class of some real
number $a$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.exists_ofAdd_mk_eq`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#exists-of-add-mk-eq).

## The longitude map is injective

The longitude map from the circle group
$\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, to the longitude subgroup of $\mathrm{SU}(2)$
is injective.

The angle class is recovered from the diagonal rotation via the complex exponential.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMap_injective`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-map-injective).

## The longitude map is surjective

The longitude map from the circle group
$\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, to the longitude subgroup of $\mathrm{SU}(2)$
is surjective: every element of the longitude subgroup is the image of some class.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMap_surjective`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-map-surjective).

## The longitude map is bijective

The longitude map from the circle group
$\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, to the longitude subgroup of $\mathrm{SU}(2)$
is bijective.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMap_bijective`, a theorem declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-map-bijective).

## Isomorphism of the circle group with the longitude subgroup

The group isomorphism from
the circle group $\mathbb{R}/2\pi\mathbb{Z}$, written multiplicatively, onto the longitude
subgroup of $\mathrm{SU}(2)$ given by the longitude map, which sends the class of a real number
$\theta$ to the diagonal rotation through $\theta$.

Formalized by `MathlibExt.GroupTheory.SU2Longitude.longitudeMulEquiv`, a definition declared in [MathlibExt/GroupTheory/SU2Longitude.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Longitude.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#longitude-mul-equiv).

## Matrix form of $\mathrm{SU}(2)$

Let $M$ be a complex $2 \times 2$ matrix in the special
unitary group $\mathrm{SU}(2)$, that is, $M$ is unitary with determinant $1$. Then there are
complex numbers $a, b$ with $|a|^2 + |b|^2 = 1$ such that the first row of $M$ is $(a, b)$ and the
second row of $M$ is $(-\bar b, \bar a)$.

Formalized by `Matrix.exists_eq_of_mem_specialUnitaryGroup_fin_two`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#exists-eq-of-mem-special-unitary-group-f).

## The trace of an $\mathrm{SU}(2)$ matrix is real

For every complex $2 \times 2$ matrix
$M$ in the special unitary group $\mathrm{SU}(2)$, the imaginary part of the trace of $M$ is $0$.

Formalized by `Matrix.trace_im_eq_zero_of_mem_specialUnitaryGroup_fin_two`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#trace-im-eq-zero-of-mem-special-unitary).

## The trace of an $\mathrm{SU}(2)$ matrix has absolute value at most two

For every complex
$2 \times 2$ matrix $M$ in the special unitary group $\mathrm{SU}(2)$, the trace of $M$ satisfies
$|\operatorname{tr} M| \le 2$.

Formalized by `Matrix.norm_trace_le_two_of_mem_specialUnitaryGroup_fin_two`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#norm-trace-le-two-of-mem-special-unitary).

## The center of $\mathrm{SU}(2)$

An element $M$ of the special unitary group
$\mathrm{SU}(2)$ of complex $2 \times 2$ matrices lies in the center of $\mathrm{SU}(2)$ if and
only if $M$ is the identity matrix $I$ or $M = -I$.

Formalized by `Matrix.mem_center_specialUnitaryGroup_fin_two_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#mem-center-special-unitary-group-fin-two).

## Characterization of $\mathrm{SU}(2)$

A complex $2 \times 2$ matrix $M$ lies in the
special unitary group $\mathrm{SU}(2)$, that is, $M$ is unitary with determinant $1$, if and
only if there are complex numbers $\alpha, \beta$ with $|\alpha|^2 + |\beta|^2 = 1$ such that
the first row of $M$ is $(\alpha, \beta)$ and the second row is $(-\bar\beta, \bar\alpha)$.

Formalized by `Matrix.mem_specialUnitaryGroup_fin_two_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SpecialUnitaryFinTwo.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#mem-special-unitary-group-fin-two-iff).

## The matrix $\operatorname{diag}(i, -i)$ is special unitary

The complex diagonal matrix
$\operatorname{diag}(i, -i)$, where $i$ is the imaginary unit, lies in the special unitary group
$\mathrm{SU}(2)$ of complex $2 \times 2$ matrices.

Formalized by `SU2.diag_I_mem`, a theorem declared in [MathlibExt/GroupTheory/SU2Basic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Basic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#diag-i-mem).

## The matrix with rows $(0, 1)$ and $(-1, 0)$ is special unitary

The complex $2 \times 2$
matrix with rows $(0, 1)$ and $(-1, 0)$ lies in the special unitary group $\mathrm{SU}(2)$ of
complex $2 \times 2$ matrices.

Formalized by `SU2.antidiag_mem`, a theorem declared in [MathlibExt/GroupTheory/SU2Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#antidiag-mem).

## The center of $\mathrm{SU}(2)$ is proper

The center of the special unitary group
$\mathrm{SU}(2)$ of complex $2 \times 2$ matrices is not all of $\mathrm{SU}(2)$.

The matrix $\operatorname{diag}(i, -i)$, where $i$ is the imaginary unit, lies in
$\mathrm{SU}(2)$ but is not central.

Formalized by `SU2.su2_center_ne_top`, a theorem declared in [MathlibExt/GroupTheory/SU2Basic.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Basic.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#su2-center-ne-top).

## Diagonalization in $\mathrm{SU}(2)$ up to conjugacy

Every element of $\mathrm{SU}(2)$ is
conjugate in $\mathrm{SU}(2)$ to an element of $\mathrm{SU}(2)$ that is the diagonal matrix
$\operatorname{diag}(z, \bar z)$ for some complex number $z$ with $z \bar z = 1$.

Formalized by `SU2.su2_conj_to_diag`, a theorem declared in [MathlibExt/GroupTheory/SU2Conjugacy.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Conjugacy.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#su2-conj-to-diag).

## Trace is invariant under conjugation in $\mathrm{SU}(2)$

For all $P$ and $A$ in
$\mathrm{SU}(2)$, the trace of $P A P^{-1}$ equals the trace of $A$.

Formalized by `SU2.su2_trace_conj_inv`, a theorem declared in [MathlibExt/GroupTheory/SU2Conjugacy.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Conjugacy.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#su2-trace-conj-inv).

## Diagonal elements of $\mathrm{SU}(2)$ with equal trace are conjugate

Let $z_1, z_2$ be
complex numbers with $z_1 \bar z_1 = 1$ and $z_2 \bar z_2 = 1$, and let $D_1, D_2$ be elements of
$\mathrm{SU}(2)$ equal to the diagonal matrices $\operatorname{diag}(z_1, \bar z_1)$ and
$\operatorname{diag}(z_2, \bar z_2)$. If $D_1$ and $D_2$ have the same trace, then they are
conjugate in $\mathrm{SU}(2)$.

In the proof, either $z_1 = z_2$, or $z_1 = \bar z_2$ and conjugation by the anti-diagonal matrix
with rows $(0, 1)$ and $(-1, 0)$ swaps the diagonal entries.

Formalized by `SU2.su2_diag_conj_of_trace`, a theorem declared in [MathlibExt/GroupTheory/SU2Conjugacy.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Conjugacy.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#su2-diag-conj-of-trace).

## Conjugacy in `SU₂` is determined by the trace

Two elements of `SU₂`
with the same trace are conjugate in `SU₂`.

Formalized by `SU2.su2_conj_of_trace_eq`, a theorem declared in [MathlibExt/GroupTheory/SU2Conjugacy.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SU2Conjugacy.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html#su2-conj-of-trace-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The special unitary group SU(2)](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/linear-groups/the-special-unitary-group-su-2)
