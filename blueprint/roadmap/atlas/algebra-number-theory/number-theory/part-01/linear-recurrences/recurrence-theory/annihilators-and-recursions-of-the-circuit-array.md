---
declaration: section
origin: cited
lean: MetaMathlibExt.AnnihilatesSeq, MetaMathlibExt.annihilatesSeq_zero, MetaMathlibExt.annihilatesSeq_charPoly_of_isSolution, MetaMathlibExt.annihilatesSeq_X_sub_C_pow, MetaMathlibExt.annihilatesSeq_sum_prod_and_mul, MetaMathlibExt.CircuitEdge, MetaMathlibExt.circuitDelta, MetaMathlibExt.circuitY
statement: formalized
---

# Annihilators and recursions of the circuit array

32 results, 22 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html).

## Annihilator of a sequence

Let $K$ be a semiring, $p = \sum_i a_i X^i \in K[X]$ and
$G \colon \mathbb{N} \to K$ a sequence, and let $E$ be the translation operator
$E(G_s) = G_{s+1}$. The operator $p(E)$ annihilates $G$ when $\sum_i a_i G_{s+i} = 0$ for every
$s \ge 0$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Section 3 (definitions of the translation operator and of an annihilator).

Formalized by `MetaMathlibExt.AnnihilatesSeq`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#annihilates-seq).

## Every operator annihilates the zero sequence

For every semiring $K$ and every polynomial
$p \in K[X]$, the operator $p(E)$ annihilates the zero sequence, where $E$ is the translation
operator $E(G_s) = G_{s+1}$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Section 3 (definition of an annihilator).

Formalized by `MetaMathlibExt.annihilatesSeq_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#annihilates-seq-zero).

## The characteristic polynomial annihilates the solutions of its recurrence

Let $K$ be a
field, $d \ge 0$ and $a_0, \dots, a_{d-1} \in K$. If a sequence $G \colon \mathbb{N} \to K$
satisfies $G_{n+d} = \sum_{i=0}^{d-1} a_i G_{n+i}$ for every $n \ge 0$, then the characteristic
polynomial $X^d - \sum_{i=0}^{d-1} a_i X^i$ of this recurrence annihilates $G$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Lemma 3.4.

Stated but not proved: `MetaMathlibExt.annihilatesSeq_charPoly_of_isSolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#annihilates-seq-char-poly-of-is-solution).

## The operator $E - c$ annihilates the powers of $c$

Let $K$ be a field, $c \in K$, and let
$E$ be the translation operator $E(G_s) = G_{s+1}$ on sequences $G \colon \mathbb{N} \to K$. Then
the operator $E - c$, that is, $p(E)$ for the polynomial $p = X - c \in K[X]$, annihilates the
sequence $s \mapsto c^s$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Lemma 3.7, part (i).

Stated but not proved: `MetaMathlibExt.annihilatesSeq_X_sub_C_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#annihilates-seq-x-sub-c-pow).

## The Addition-Multiplication Lemma for annihilators

Let $E$ be the translation operator
$E(G_s) = G_{s+1}$ on sequences. (i) Let $K$ be a field, $I$ a finite index set, and for each
$i \in I$ let $A_i \in K[X]$, $G_i \colon \mathbb{N} \to K$ and $c_i \in K$. If $A_i(E)$
annihilates $G_i$ for every $i \in I$, then $\prod_{i \in I} A_i(E)$ annihilates the sequence
$s \mapsto \sum_{i \in I} c_i G_i(s)$. (ii) Let $p_1, p_2 \in \mathbb{C}[X]$ be nonzero
polynomials and $G_1, G_2 \colon \mathbb{N} \to \mathbb{C}$ sequences such that $p_1(E)$
annihilates $G_1$ and $p_2(E)$ annihilates $G_2$. If $r_{1,1}, \dots, r_{1,m}$ and
$r_{2,1}, \dots, r_{2,n}$ are the complex roots of $p_1$ and $p_2$, listed with multiplicity,
then $\prod_{j=1}^{m} \prod_{j'=1}^{n} (E - r_{1,j} r_{2,j'})$ annihilates the termwise product
$s \mapsto G_1(s) G_2(s)$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Lemma 3.8; part (ii) quoted from Jarden.

Stated but not proved: `MetaMathlibExt.annihilatesSeq_sum_prod_and_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#annihilates-seq-sum-prod-and-mul).

## Edges of an upright triangle

An upright triangle of the grid has three edges: the left
edge $L$, the right edge $R$ and the base $B$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Section 2 (edge labels `L`, `R`, `B`).

Formalized by `MetaMathlibExt.CircuitEdge`, an inductive type declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-edge).

## Delta-wye resistance function

For elements $x$, $y$, $z$ of a field $K$, the delta-wye
resistance function is $\Delta(x, y, z) = \frac{xy}{x + y + z}$.

Division follows the convention $a / 0 = 0$, so $\Delta(x, y, z) = 0$ when $x + y + z = 0$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.1).

Formalized by `MetaMathlibExt.circuitDelta`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-delta).

## The Y-Δ resistance function

For elements $a$, $b$, $c$ of a field $K$, the $Y$-$\Delta$
resistance function is $Y(a, b, c) = (ab + bc + ca)/a$.

When $a = 0$ the value is $0$, by the convention $x/0 = 0$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.1).

Formalized by `MetaMathlibExt.circuitY`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-y).

## Top delta-wye arm

For an upright triangle whose left, right and base edges carry the
values $L$, $R$, $B$ in a field $K$, the top arm is $\Delta(L, R, B) = \frac{LR}{L + R + B}$, where
$\Delta$ is the delta-wye resistance function: the arm of the equivalent star from the centre of
the triangle to its top vertex.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Figure 2 (`Y₁₂ = Δ(L, R, B)`).

Formalized by `MetaMathlibExt.circuitTopArm`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-top-arm).

## Bottom-right delta-wye arm

For an upright triangle whose left, right and base edges carry
the values $L$, $R$, $B$ in a field $K$, the bottom-right arm is
$\Delta(R, B, L) = \frac{RB}{R + B + L}$, where $\Delta$ is the delta-wye resistance function: the
arm of the equivalent star from the centre of the triangle to its bottom-right vertex.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Figure 2 (`Y₄ = Δ(R, B, L)`).

Formalized by `MetaMathlibExt.circuitRightArm`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-right-arm).

## Bottom-left delta-wye arm

For an upright triangle whose left, right and base edges carry
the values $L$, $R$, $B$ in a field $K$, the bottom-left arm is
$\Delta(B, L, R) = \frac{BL}{B + L + R}$, where $\Delta$ is the delta-wye resistance function: the
arm of the equivalent star from the centre of the triangle to its bottom-left vertex.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Figure 2 (`Y₈ = Δ(B, L, R)`).

Formalized by `MetaMathlibExt.circuitLeftArm`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-left-arm).

## Left-perimeter function

Let $K$ be a field, let $\Delta(x, y, z) = xy/(x + y + z)$ be the
delta-wye resistance function, and for an upright triangle $t$ write $L_t$, $R_t$, $B_t \in K$ for
the values on its left, right and base edges. For triangles $t$ and $u$, the left-perimeter
function is $\mathcal{P}(t, u) = \Delta(B_t, L_t, R_t) + \Delta(L_u, R_u, B_u)$, the series
resistance of the bottom-left arm of $t$ and the top arm of $u$.

In the row reduction of a labelling $T$ it is applied to $t = T_{r,1}$ and $u = T_{r+1,1}$, where
$T_{r,d}$ is the triangle in row $r$ and diagonal $d$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.2).

Formalized by `MetaMathlibExt.circuitPerimeter`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-perimeter).

## Left-edge function

Let $K$ be a field, let $\Delta(x, y, z) = xy/(x + y + z)$ and
$Y(a, b, c) = (ab + bc + ca)/a$ be the delta-wye and wye-delta resistance functions, and for an
upright triangle $t$ write $L_t$, $R_t$, $B_t \in K$ for the values on its left, right and base
edges. For triangles $t$, $u$, $v$, the left-edge function is
$\mathcal{L}(t, u, v) = Y(\Delta(R_t, B_t, L_t), \Delta(B_u, L_u, R_u), \Delta(L_v, R_v, B_v))$,
the wye-delta transform of the star formed by the bottom-right arm of $t$, the bottom-left arm of
$u$ and the top arm of $v$, with the arm of $t$ first.

In the row reduction of a labelling $T$ it is applied to $t = T_{r,d-1}$, $u = T_{r,d}$ and
$v = T_{r+1,d}$ for $d \ne 1$, where $T_{r,d}$ is the triangle in row $r$ and diagonal $d$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.5).

Formalized by `MetaMathlibExt.circuitLeftEdge`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-left-edge).

## Right-edge function

Let $K$ be a field, let $\Delta(x, y, z) = xy/(x + y + z)$ and
$Y(a, b, c) = (ab + bc + ca)/a$ be the delta-wye and wye-delta resistance functions, and for an
upright triangle $t$ write $L_t$, $R_t$, $B_t \in K$ for the values on its left, right and base
edges. For triangles $t$, $u$, $v$, the right-edge function is
$\mathcal{R}(t, u, v) = Y(\Delta(B_u, L_u, R_u), \Delta(R_t, B_t, L_t), \Delta(L_v, R_v, B_v))$,
the wye-delta transform of the star formed by the bottom-left arm of $u$, the bottom-right arm of
$t$ and the top arm of $v$, with the arm of $u$ first.

In the row reduction of a labelling $T$ it is applied to $t = T_{r,d}$, $u = T_{r,d+1}$ and
$v = T_{r+1,d+1}$ for $d \ne r$, where $T_{r,d}$ is the triangle in row $r$ and diagonal $d$. This
follows Steps 2-5 and Figure 2; the displayed equation (2.4) instead uses $T_{r+1,d}$ in place of
$T_{r+1,d+1}$ and puts the arm of $t$ first, which gives $C_{1,2} = 29/36$ against Table 1's
$13/12$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.4) (corrected as above).

Formalized by `MetaMathlibExt.circuitRightEdge`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-right-edge).

## Base-edge function

Let $K$ be a field. For a triangle with left, right and base
resistances $L$, $R$, $B$ in $K$, its top arm is $\Delta(L, R, B)$, its bottom-right arm is
$\Delta(R, B, L)$ and its bottom-left arm is $\Delta(B, L, R)$, where
$\Delta(x, y, z) = xy/(x + y + z)$. For triangles $t$, $u$, $v$, the base-edge function is
$\mathcal{B}(t, u, v) = Y(a, b, c) = (ab + bc + ca)/a$, where $a$ is the top arm of $t$, $b$ is
the bottom-right arm of $u$ and $c$ is the bottom-left arm of $v$. In a row reduction, for a row
$r$ and a diagonal $d$, the triangles $t$, $u$, $v$ are those in row $r + 2$ and diagonal $d + 1$,
in row $r + 1$ and diagonal $d$, and in row $r + 1$ and diagonal $d + 1$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, equation (2.3).

Formalized by `MetaMathlibExt.circuitBaseEdge`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-base-edge).

## Row reduction of a labelled triangular grid

Let $K$ be a field and let $T$ be a labelling
that assigns a value $T_{r,d,e} \in K$ to the edge $e$ (left $L$, right $R$ or base $B$) of the
upright triangle in row $r$ (from the top) and diagonal $d$ (from the left); write $T_{r,d}$ for
that triangle and $\Delta(x, y, z) = xy/(x + y + z)$ for the delta-wye resistance function. The
reduced labelling $T'$ is given by $T'_{r,1,L} = \mathcal{P}(T_{r,1}, T_{r+1,1})$ and
$T'_{r,d,L} = \mathcal{L}(T_{r,d-1}, T_{r,d}, T_{r+1,d})$ for $d \ne 1$, where $\mathcal{P}$ is the
left-perimeter function and $\mathcal{L}$ the left-edge function; by $T'_{r,r,R}$ equal to the
bottom-right arm $\Delta(R, B, L)$ of $T_{r,r}$ plus the top arm $\Delta(L, R, B)$ of
$T_{r+1,r+1}$, and $T'_{r,d,R} = \mathcal{R}(T_{r,d}, T_{r,d+1}, T_{r+1,d+1})$ for $d \ne r$, where
$\mathcal{R}$ is the right-edge function; and by
$T'_{r,d,B} = \mathcal{B}(T_{r+2,d+1}, T_{r+1,d}, T_{r+1,d+1})$, where $\mathcal{B}$ is the
base-edge function.

Here $r$ and $d$ range over all natural numbers, with $d - 1$ truncated at $0$; only the values
with $1 \le d \le r$ are meaningful.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Section 2 (row reduction, equations (2.2)-(2.5)).

Formalized by `MetaMathlibExt.circuitReduce`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-reduce).

## Reduced circuit grids

Let $K$ be a field, and for each $m$ let either a boundary value
$\beta_m \in K$ be given or none. The labellings $T^m$, which assign a value $T^m_{r,d,e} \in K$ to
the edge $e$ (left $L$, right $R$ or base $B$) of the upright triangle in row $r$ and diagonal $d$,
are defined by recursion on $m$: $T^0$ is identically $1$, and $T^{m+1}$ is the row reduction of
$T^m$, except that if $\beta_{m+1}$ is given then every left edge with $d = 1$ and every right edge
with $d = r$ takes the value $\beta_{m+1}$.

With no boundary values given this is the numerical reduction of the all-one grid; in
Definitions 2.4 and 2.5 the boundary values are variables.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Section 2 (reductions `T^m`, Definitions 2.4 and 2.5).

Formalized by `MetaMathlibExt.circuitGrid`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-grid).

## Circuit array of a boundary assignment

Let $K$ be a field and let $\beta$ assign to each
natural number $m$ either nothing or a value $\beta(m) \in K$. Let $T^0$ be the all-one triangular
grid and, for $m \ge 1$, let $T^m$ be obtained from $T^{m-1}$ by one row reduction followed, when
$\beta(m)$ is given, by setting every boundary edge (left edges on diagonal $1$, right edges on
diagonal $r$ in row $r$) to $\beta(m)$. For natural numbers $i$ and $j$, the entry $C_{i,j}$ of the
circuit array of $\beta$ is the resistance of the left edge (for even $i$) or the right edge (for
odd $i$) of the triangle of $T^j$ in row $2j - 1$ and diagonal $j - \lfloor (i+1)/2 \rfloor$, with
subtraction truncated at $0$. The entries are meaningful for $j \ge 1$ and $0 \le i \le 2(j - 1)$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.3.

Formalized by `MetaMathlibExt.circuitArrayOf`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-of).

## Circuit array

The circuit array $C_{i,j} \in \mathbb{Q}$ is the circuit array of the
reductions of the all-one triangular grid with no boundary edge replaced: $C_{i,j}$ is the left
edge (for even $i$) or the right edge (for odd $i$) of the triangle in row $2j - 1$ and diagonal
$j - \lfloor (i+1)/2 \rfloor$ of the all-one grid reduced $j$ times, with subtraction truncated
at $0$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.3 and Table 1.

Formalized by `MetaMathlibExt.circuitArray`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array).

## One-variable circuit array

The one-variable circuit array $C^X_{i,j}$, with entries in
the field $\mathbb{Q}(X)$ of rational functions in one variable over $\mathbb{Q}$, is the circuit
array of the reductions of the all-one triangular grid in which, after the first reduction, every
boundary edge is set to $(X - 3)/X$, and no boundary edge is replaced after any later reduction.
Thus $C^X_{i,j}$ is the left edge (for even $i$) or the right edge (for odd $i$) of the triangle
in row $2j - 1$ and diagonal $j - \lfloor (i+1)/2 \rfloor$ of this grid reduced $j$ times, with
subtraction truncated at $0$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.4 and Table 2.

Formalized by `MetaMathlibExt.circuitArrayX`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x).

## Variables of the multivariable circuit array

For a natural number $m$, $X_m$ is the
indeterminate $X_m$ regarded as an element of the field of fractions
$\mathbb{Q}(X_0, X_1, X_2, \dots)$ of the polynomial ring $\mathbb{Q}[X_0, X_1, X_2, \dots]$ in
countably many variables.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.5 (the variables `X_i`).

Formalized by `MetaMathlibExt.circuitVar`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-var).

## Multivariable circuit array

Reduce the all-one triangular grid row by row as in Section 2,
and after the $m$-th reduction, for every $m \ge 1$, set every boundary edge (the left edges on the
first diagonal and the right edges on the last diagonal) to the variable $X_m$ of the field of
rational functions over $\mathbb{Q}$ in $X_0, X_1, \dots$. The multivariable circuit array
$C^M_{i,j}$ (Table 3) is the circuit array read off these grids: for $j \ge 1$ and
$0 \le i \le 2(j-1)$, it is the left edge for even $i$, or the right edge for odd $i$, of the
triangle in row $2j - 1$ and diagonal $j - \lfloor (i+1)/2 \rfloor$ of the $j$-times reduced
grid (other indices give junk values). In particular $C^M_{2(m-1),m} = X_m$ for every $m \ge 1$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.5 and Table 3.

Formalized by `MetaMathlibExt.circuitArrayM`, a definition declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-m).

## First entries of the circuit array

The circuit array satisfies $C_{0,1} = 2/3$,
$C_{0,2} = 26/27$, $C_{1,2} = 13/12$ and $C_{2,2} = 1/2$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Table 1.

Formalized by `MetaMathlibExt.circuitArray_small`, a theorem declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-small).

## First entry of the one-variable circuit array

The one-variable circuit array $C^X$, with
entries in the field $\mathbb{Q}(X)$ of rational functions over $\mathbb{Q}$, satisfies
$C^X_{0,1} = (X - 3)/X$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.4 and Proposition 4.1 (iv).

Formalized by `MetaMathlibExt.circuitArrayX_zero_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x-zero-one).

## First entries of the left diagonal of the multivariable circuit array

The multivariable
circuit array $C^M$, with values in the field of rational functions over $\mathbb{Q}$ in the
variables $X_0, X_1, \dots$, satisfies $C^M_{0,1} = X_1$ and $C^M_{2,2} = X_2$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Definition 2.5.

Formalized by `MetaMathlibExt.circuitArrayM_diagonal`, a theorem declared in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-m-diagonal).

## Column recursion for the one-variable circuit array

Extend the one-variable circuit array
$C^X$, with entries in the field $\mathbb{Q}(X)$ of rational functions over $\mathbb{Q}$, to integer
row indices by $C_{i,j} = C^X_{i,j}$ for $i \ge 0$ and $C_{i,j} = 1$ for $i < 0$. For an integer
$i$ and a natural number $j$, let $\tau_{i,j}$ be the triangle with left edge $C_{i,j}$ and right
and base edges $C_{i-1,j}$. Let $\mathcal{P}$, $\mathcal{L}$ and $\mathcal{R}$ be the
left-perimeter, left-edge and right-edge functions of the reduction. Then:
(i) $C_{2(c-1),c} = \mathcal{P}(\tau_{2(c-2),c-1}, \tau_{2(c-2),c-1})$ for every natural number
$c \ge 2$;
(ii) $C_{2(c-1),j} = \mathcal{L}(\tau_{2(c-1),j-1}, \tau_{2c-4,j-1}, \tau_{2c-4,j-1})$ for all
natural numbers $c$, $j$ with $2 \le c < j$;
(iii) $C_{2c-3,j} = \mathcal{R}(\tau_{2c-4,j-1}, \tau_{2c-6,j-1}, \tau_{2c-6,j-1})$ for all
natural numbers $c$, $j$ with $2 \le c \le j$;
(iv) $C^X_{0,1} = (X - 3)/X$.

Here $\mathcal{R}$ is the right-edge function of the reduction algorithm, not the misprinted
display (2.4), and the printed $C_{2(c-1-4),j-1}$ in (iii) is read as $C_{2(c-1)-4,j-1}$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Proposition 4.1.

Stated but not proved: `MetaMathlibExt.circuitArrayX_inductive` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x-inductive).

## Row zero of the one-variable circuit array

For every natural number $s \ge 1$, the
one-variable circuit array $C^X$, with entries in the field $\mathbb{Q}(X)$ of rational functions
over $\mathbb{Q}$, satisfies $C^X_{0,s} = (3 \cdot 9^{s-2} X - 1)/(3 \cdot 9^{s-2} X)$, with an
integer exponent (so $9^{s-2} = 1/9$ when $s = 1$), and the circuit array $C$ satisfies
$C_{0,s} = (9^s/3 - 1)/(9^s/3)$ in $\mathbb{Q}$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.4 with (2.6).

Stated but not proved: `MetaMathlibExt.circuitArrayX_row_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x-row-zero).

## Row one of the one-variable circuit array

For every natural number $s \ge 2$, the
one-variable circuit array $C^X$, with entries in the field $\mathbb{Q}(X)$ of rational functions
over $\mathbb{Q}$, satisfies $C^X_{1,s} = (3 \cdot 9^{s-2} X - 1)/(3 \cdot 9^{s-2} X - 3)$.

The printed denominator $3 \cdot 9^{s-2} X$ is the row-zero formula; Table 2 has
$(3X - 1)/(3X - 3)$ at $s = 2$, which is $13/12$ at $X = 9$, not $26/27$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.5, denominator corrected from Table 2.

Stated but not proved: `MetaMathlibExt.circuitArrayX_row_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x-row-one).

## Row two of the one-variable circuit array

For every natural number $s \ge 2$, the
one-variable circuit array $C^X$, with entries in the field $\mathbb{Q}(X)$ of rational functions
over $\mathbb{Q}$, satisfies
$C^X_{2,s} = (c_{2,0}(s) - c_{2,1}(s) X + c_{2,2}(s) X^2)/(9^{s-2} X - 1)^2$, where
$c_{2,0}(s) = 27 \cdot 9^{s-3} - 1$, $c_{2,1}(s) = 24(2s - 3) \cdot 9^{s-3}$ and
$c_{2,2}(s) = 81 \cdot 81^{s-3} - 3 \cdot 9^{s-3}$, with integer exponents (so $9^{s-3} = 1/9$
and $81^{s-3} = 1/81$ when $s = 2$).

The printed $c_{2,2}(X^2)$ is read as $c_{2,2}(s) X^2$, as in Remark 4.7.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.6.

Stated but not proved: `MetaMathlibExt.circuitArrayX_row_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-x-row-two).

## Row 0 of the multivariable circuit array

Let $C^M$ be the multivariable circuit array, with
values in the field of rational functions over $\mathbb{Q}$ in the variables $X_0, X_1, \dots$.
For every integer $s \ge 1$, $C^M_{0,s} = (9^{s-1} - 1 + X_1)/9^{s-1}$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.8.

Stated but not proved: `MetaMathlibExt.circuitArrayM_row_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-m-row-zero).

## Row 1 of the multivariable circuit array

Let $C^M$ be the multivariable circuit array, with
values in the field of rational functions over $\mathbb{Q}$ in the variables $X_0, X_1, \dots$.
For every integer $s \ge 2$,
$C^M_{1,s} = (9^{s-1} - 1 + X_1)/\bigl(3(X_1 + 3 \cdot 9^{s-2} - 1)\bigr)$.

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.10.

Stated but not proved: `MetaMathlibExt.circuitArrayM_row_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-m-row-one).

## Row 2 of the multivariable circuit array

Let $C^M$ be the multivariable circuit array, with
values in the field of rational functions over $\mathbb{Q}$ in the variables $X_0, X_1, \dots$.
For every integer $s \ge 2$,

$$C^M_{2,s} = \frac{\sum_{i,j} c_{i,j}(s) X_1^i X_2^j}{(3 \cdot 9^{s-2} - 1 + X_1)^2},$$

where the sum runs over the six coefficients $c_{2,1}(s) = 9^{s-2}$, $c_{2,0}(s) = 9^{s-2} - 1$,
$c_{1,1}(s) = 4 \cdot 9^{s-2}$, $c_{1,0}(s) = 2 + (16(s-2) - 2) \cdot 9^{s-2}$,
$c_{0,1}(s) = 4 \cdot 9^{s-2}$ and
$c_{0,0}(s) = -1 + 9 \cdot 81^{s-2} - (8 + 16(s-2)) \cdot 9^{s-2}$.
Moreover, writing $E$ for the translation operator on rational sequences, the shifted coefficient
sequences $s \mapsto c_{i,j}(s+2)$, $s \ge 0$, are annihilated as in Table 4: $c_{0,0}$ by
$(E-81)(E-9)^2(E-1)$, $c_{0,1}$ by $(E-1)(E-9)$, $c_{1,0}$ by $(E-9)^2(E-1)$, $c_{1,1}$ by
$E-9$, $c_{2,0}$ by $(E-1)(E-9)$ and $c_{2,1}$ by $E-9$.

The paper's base case is $s = 3$; the identity also holds at $s = 2$. The recursions column of
Table 4 is omitted (its $X_1^0 X_2^1$ entry $G_s = 10G_{s-1} - G_{s-2}$ is misprinted for
$-9G_{s-2}$).

## Sources

- Emily J. Evans and Russell Jay Hendel, *Recursions and Characteristic Polynomials of the Rows of the Circuit Array*, Fibonacci Quarterly 62 (2024), Article 62-4/hendel08232024rev2, Corollary 4.12 and Table 4.

Stated but not proved: `MetaMathlibExt.circuitArrayM_row_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/CircuitArrayRecursionsWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html#circuit-array-m-row-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Annihilators and recursions of the circuit array](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/annihilators-and-recursions-of-the-circuit-array)
