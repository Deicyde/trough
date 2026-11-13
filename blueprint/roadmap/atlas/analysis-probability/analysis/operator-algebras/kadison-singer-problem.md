---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.eval_mixedDetPolynomial, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial_pderiv_sq_eq_zero_of_eq_vecMulVec, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_update_sum, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_update_affine, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_eq_charpoly_sum_of_eq_vecMulVec, MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_fin_one
statement: formalized
proof: formalized
---

# Kadison–Singer problem

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html).

## Mixed determinant polynomial

For square complex matrices $A_1, \dots, A_m$ whose rows and
columns are indexed by a finite set $d$, the mixed determinant polynomial is
$\det(x I + \sum_{i=1}^m z_i A_i)$, viewed as a polynomial with complex coefficients in the
$m + 1$ variables $x, z_1, \dots, z_m$, where $I$ is the identity matrix.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial`, a definition declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-det-polynomial).

## Values of the mixed determinant polynomial

Let $A_1, \dots, A_m$ be square complex
matrices whose rows and columns are indexed by a finite set $d$. For all complex numbers
$x, z_1, \dots, z_m$, the value of the mixed determinant polynomial of $A_1, \dots, A_m$ at the
point $(x, z_1, \dots, z_m)$ is $\det(x I + \sum_{i=1}^m z_i A_i)$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.eval_mixedDetPolynomial`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#eval-mixed-det-polynomial).

## Rank-one coefficients make the mixed determinant polynomial affine

Let
$A_1, \dots, A_m$ be square complex matrices whose rows and columns are indexed by a finite set
$d$, and suppose that $A_i = u v^{\mathsf T}$ for some index $i$ and vectors
$u, v \in \mathbb{C}^d$. Consider the mixed determinant polynomial
$\det(x I + \sum_{j=1}^m z_j A_j)$ in the variables $x, z_1, \dots, z_m$, where $I$ is the
identity matrix. Then its second partial derivative with respect to $z_i$ is zero; equivalently,
it has degree at most one in $z_i$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial_pderiv_sq_eq_zero_of_eq_vecMulVec`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-det-polynomial-pderiv-sq-eq-zero-o).

## Mixed characteristic polynomial

For square complex matrices $A_1, \dots, A_m$ whose rows
and columns are indexed by a finite set $d$, consider the mixed determinant polynomial
$\det(x I + \sum_{i=1}^m z_i A_i)$ in the variables $x, z_1, \dots, z_m$, where $I$ is the
identity matrix. The mixed characteristic polynomial is the polynomial in $x$ with complex
coefficients obtained by applying the operator $\prod_{i=1}^m (1 - \partial_{z_i})$ to it and
then setting $z_1 = \dots = z_m = 0$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial`, a definition declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial).

## The mixed characteristic polynomial is affine in each matrix

Let $A_1, \dots, A_m$ be
square complex matrices whose rows and columns are indexed by a finite set $d$, and fix an index
$i$. Let $(C_a)_{a \in \iota}$ be a family of such matrices indexed by a finite set $\iota$, with
real weights $w_a$, not necessarily nonnegative, such that $\sum_a w_a = 1$. Then the mixed
characteristic polynomial of the family obtained from $A_1, \dots, A_m$ by replacing $A_i$ with
$\sum_a w_a C_a$ equals $\sum_a w_a \mu_a$, where $\mu_a$ is the mixed characteristic polynomial of
the family obtained by replacing $A_i$ with $C_a$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_update_sum`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-update-s).

## The mixed characteristic polynomial along a line

Let $A_1, \dots, A_m$ be square complex
matrices whose rows and columns are indexed by a finite set $d$, fix an index $i$, let $B$ and
$C$ be two such matrices and let $t$ be a real number. Write $\mu_M$ for the mixed
characteristic polynomial of the family obtained from $A_1, \dots, A_m$ by replacing $A_i$ with
$M$. Then $\mu_{(1 - t) B + t C} = (1 - t)\, \mu_B + t\, \mu_C$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_update_affine`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-update-a).

## Mixed characteristic polynomials of outer products

Let $A_1, \dots, A_m$ be square
complex matrices whose rows and columns are indexed by a finite set $d$, and suppose that
$A_i = u_i v_i^{\mathsf T}$ for vectors $u_i, v_i \in \mathbb{C}^d$, for every $i$. Then the
mixed characteristic polynomial of $A_1, \dots, A_m$ equals the characteristic polynomial of the
sum $\sum_{i=1}^m A_i$, that is, the polynomial $\det(x I - \sum_{i=1}^m A_i)$ in the variable
$x$, where $I$ is the identity matrix.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_eq_charpoly_sum_of_eq_vecMulVec`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-eq-charp).

## Mixed characteristic polynomial of a single $1 \times 1$ matrix

For every complex number
$a$, the mixed characteristic polynomial of the family consisting of the single $1 \times 1$
complex matrix $(a)$ is the polynomial $x - a$ in the variable $x$, which is the characteristic
polynomial of $(a)$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_fin_one`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MixedCharPoly.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-fin-one).

## Finite-support Marcus–Spielman–Srivastava bound

The proposition that the following holds
for every natural number $m$ and every finite index set $D$. Let $s_1, \dots, s_m$ be positive
integers, let $p_{i,a} \ge 0$ be reals and $v_{i,a} \in \mathbb{C}^D$ be vectors for
$1 \le i \le m$ and $1 \le a \le s_i$, and let $\eta \ge 0$ be real. Suppose that
$\sum_a p_{i,a} = 1$ for each $i$, that $\sum_i \sum_a p_{i,a} v_{i,a} v_{i,a}^* = \mathrm{Id}_D$,
and that $\sum_a p_{i,a} \|v_{i,a}\|^2 \le \eta$ for each $i$, where $\|v_{i,a}\|$ is the
Euclidean norm. Then there are choices $a_i \in \{1, \dots, s_i\}$ for $i = 1, \dots, m$ such
that $\left\|\sum_i v_{i,a_i} v_{i,a_i}^*\right\| \le (1 + \sqrt{\eta})^2$, where the norm of a
matrix is the operator norm.

In probabilistic terms, $p_{i,a}$ is the probability that an independent random vector $v_i$
takes the value $v_{i,a}$, and the conclusion is that some choice of values meets the bound.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.FiniteMSSBound`, a definition declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#finite-mssbound-2).

## Partitioning a Parseval frame with the finite MSS bound

Assume the finite-support
Marcus–Spielman–Srivastava bound holds. Let $I$ be a finite index set, let $d$ and $r$ be natural
numbers with $r > 0$, let $\delta \ge 0$ be real, and let $u_i \in \mathbb{C}^d$ for $i \in I$
be vectors with $\sum_{i \in I} u_i u_i^* = \mathrm{Id}_d$ and $\|u_i\|^2 \le \delta$ for every
$i$. Then there is a map $c : I \to \{1, \dots, r\}$ such that for every $j$,
$\left\|\sum_{i \in I,\ c(i) = j} u_i u_i^*\right\| \le (1/\sqrt{r} + \sqrt{\delta})^2$, where
$\|u_i\|$ is the Euclidean norm of $u_i$ and the norm of a matrix is the operator norm.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.exists_frame_partition_of_finiteMSS`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#exists-frame-partition-of-finite-mss).

## Anderson paving from the finite MSS bound

Assume the finite-support
Marcus–Spielman–Srivastava bound holds. Let $n$ and $r$ be natural numbers with $r > 0$, and let
$A$ be a Hermitian complex $n \times n$ matrix with zero diagonal and operator norm
$\|A\| \le 1$. Then there is a coloring $c$ of the indices $\{1, \dots, n\}$ with $r^2$ colors
such that for every color $j$, writing $P_j$ for the diagonal matrix with entry $1$ at the
indices of color $j$ and $0$ elsewhere,
$\|P_j A P_j\| \le 2\left(1/\sqrt{r} + \sqrt{1/2}\right)^2 - 1$, where $\|\cdot\|$ is the
operator norm.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.andersonPaving_of_finiteMSS`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Paving.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#anderson-paving-of-finite-mss).

## Stability of the determinant polynomial

For every finite family $A_1, \dots, A_m$ of
positive semidefinite complex square matrices whose rows and columns are indexed by a finite set
$d$, the polynomial $\det\left(x I + \sum_{i=1}^m z_i A_i\right)$ in the variables
$x, z_1, \dots, z_m$, where $I$ is the identity matrix, is stable.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial_isStable_of_posSemidef`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-det-polynomial-is-stable-of-pos-se).

## Real stability of the determinant polynomial

For every finite family $A_1, \dots, A_m$ of
positive semidefinite complex square matrices whose rows and columns are indexed by a finite set
$d$, the polynomial $\det\left(x I + \sum_{i=1}^m z_i A_i\right)$ in the variables
$x, z_1, \dots, z_m$, where $I$ is the identity matrix, is real stable.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedDetPolynomial_isRealStable_of_posSemidef`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-det-polynomial-is-real-stable-of-p).

## Mixed characteristic polynomials are monic

For every finite family $A_1, \dots, A_m$ of
complex square matrices of a common size, the mixed characteristic polynomial of
$A_1, \dots, A_m$ is monic.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_monic`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-monic).

## Degree of a mixed characteristic polynomial

For every finite family $A_1, \dots, A_m$ of
complex square matrices whose rows and columns are indexed by a finite set $d$, the mixed
characteristic polynomial of $A_1, \dots, A_m$ has degree $|d|$, the number of elements of $d$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_natDegree`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-nat-degr).

## Mixed characteristic polynomials of positive semidefinite matrices are real-rooted

For
every finite family $A_1, \dots, A_m$ of positive semidefinite complex square matrices of a common
size, the mixed characteristic polynomial of $A_1, \dots, A_m$ is real-rooted.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_isRealRooted_of_posSemidef`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/RealStable.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-is-real).

## Marcus--Spielman--Srivastava barrier bound

Let $d$ be a nonempty finite index set, let
$A_1, \dots, A_m$ be positive semidefinite complex $d \times d$ matrices with $\sum_i A_i = I$,
and let $\eta \ge 0$ be a real number such that $\operatorname{Re} \operatorname{tr} A_i \le \eta$
for every $i$. Then the largest real part of a root of the mixed characteristic polynomial of
$A_1, \dots, A_m$ is at most $(1 + \sqrt{\eta})^2$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.mixedCharacteristicPolynomial_maxRealRoot_le`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Barrier.lean, line 1958](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/Barrier.lean#L1958). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#mixed-characteristic-polynomial-max-real).

## An outcome bounded by the mixed characteristic polynomial

Let $d$ be a nonempty finite
index set. For $i = 1, \dots, m$ let $s_i \ge 1$, let $v_{i,1}, \dots, v_{i,s_i} \in \mathbb{C}^d$,
let $p_{i,1}, \dots, p_{i,s_i} \ge 0$ be reals with $\sum_a p_{i,a} = 1$, and put
$A_i = \sum_a p_{i,a} v_{i,a} v_{i,a}^*$. Then there is a choice of indices
$\omega_i \in \{1, \dots, s_i\}$, one for each $i$, such that the largest real part of a root of
the characteristic polynomial of $\sum_i v_{i,\omega_i} v_{i,\omega_i}^*$ is at most the largest
real part of a root of the mixed characteristic polynomial of $A_1, \dots, A_m$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.exists_outcome_maxRealRoot_le_mixedCharacteristicPolynomial`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MSS.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MSS.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#exists-outcome-max-real-root-le-mixed-ch).

## Marcus--Spielman--Srivastava bound, finite-support form

Let $d$ be a finite index set
and, for $i = 1, \dots, m$, let $s_i \ge 1$, let $v_{i,1}, \dots, v_{i,s_i} \in \mathbb{C}^d$, and
let $p_{i,1}, \dots, p_{i,s_i} \ge 0$ be reals with $\sum_a p_{i,a} = 1$. Let $\eta \ge 0$ be a real
number, and suppose that $\sum_i \sum_a p_{i,a} v_{i,a} v_{i,a}^* = I$ and
$\sum_a p_{i,a} \|v_{i,a}\|^2 \le \eta$ for every $i$, where $\|\cdot\|$ is the Euclidean norm.
Then there is a choice of indices $\omega_i \in \{1, \dots, s_i\}$, one for each $i$, such that
the operator norm of $\sum_i v_{i,\omega_i} v_{i,\omega_i}^*$ with respect to the Euclidean norm
on $\mathbb{C}^d$ is at most $(1 + \sqrt{\eta})^2$.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSinger.finiteMSSBound`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MSS.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger/MSS.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#finite-mssbound).

## Paving projection

Given a colouring $c$ of the indices $\{0, \dots, n-1\}$ with the
colours $\{0, \dots, r-1\}$ and a colour $j$, the paving projection of $c$ onto colour $j$ is the
diagonal complex $n \times n$ matrix whose $i$-th diagonal entry is $1$ if $c(i) = j$ and $0$
otherwise.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSingerWanted.pavingProj`, a definition declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#paving-proj).

## Anderson paving theorem

For every real $\varepsilon > 0$ there is a positive integer $r$ such
that for every $n \in \mathbb{N}$ and every Hermitian complex $n \times n$ matrix $A$ with zero
diagonal and $\|A\| \le 1$, where $\|\cdot\|$ is the operator norm for the Euclidean norm on
$\mathbb{C}^n$, there is a colouring $c$ of the indices $\{0, \dots, n-1\}$ with the $r$ colours
$\{0, \dots, r-1\}$ such that $\|P_j A P_j\| \le \varepsilon$ for every colour $j$, where $P_j$ is
the paving projection of $c$ onto colour $j$.

Proof: We formalize the Marcus--Spielman--Srivastava mixed-characteristic-polynomial bound via
real stability, interlacing families, and the barrier argument, then use Timotin's projection
dilation reduction to derive Anderson paving.

## Sources

- Anderson paving formulation equivalent to Kadison–Singer conjecture; proved by Marcus–Spielman–Srivastava, Ann. of Math. 182 (2015), 327–350; original Kadison–Singer, Amer. J. Math. 81 (1959) and Anderson, Trans. Amer. Math. Soc. 249 (1979); Lean is finite-dimensional Hermitian zero-diagonal paving with r(ε) independent of n.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KadisonSingerWanted.kadison_singer_paving`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KadisonSinger.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/CStarAlgebra/KadisonSinger.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html#kadison-singer-paving).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kadison–Singer problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kadison-singer-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-algebras/kadison-singer-problem)
