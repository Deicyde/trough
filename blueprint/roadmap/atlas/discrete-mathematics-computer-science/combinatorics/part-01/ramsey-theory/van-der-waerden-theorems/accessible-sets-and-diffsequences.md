---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMonochromatic, MetaMathlibExt.IsDAP, MetaMathlibExt.isDAP_iff, MetaMathlibExt.IsRLarge, MetaMathlibExt.isRLarge_iff, MetaMathlibExt.IsLarge, MetaMathlibExt.isLarge_iff, MetaMathlibExt.IsDDiffSequence
statement: formalized
---

# Accessible sets and diffsequences

80 results, 47 proved and 33 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html).

## Monochromatic sequences of positive integers

Let $r$ and $k$ be natural numbers and let
$c$ color the positive integers with the colors $0, 1, \dots, r - 1$. A sequence
$x_0, \dots, x_{k-1}$ of positive integers is monochromatic for $c$ when $c(x_i) = c(x_j)$ for
all $i, j < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.IsMonochromatic`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-monochromatic).

## Arithmetic progressions with gap in $D$

Let $D$ be a set of natural numbers and $k$ a
natural number. A sequence $x_0, \dots, x_{k-1}$ of positive integers is a $k$-term arithmetic
progression with gap in $D$ if there are a positive integer $a$ and an element $d \in D$ such
that $x_i = a + i d$ for every $i < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.IsDAP`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-dap).

## Characterization of arithmetic progressions with gap in $D$

Let $D$ be a set of natural
numbers, $k$ a natural number and $x_0, \dots, x_{k-1}$ positive integers. Then
$x_0, \dots, x_{k-1}$ is a $k$-term arithmetic progression with gap in $D$ if and only if there
are a positive integer $a$ and an element $d \in D$ such that $x_i = a + i d$ for every $i < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.isDAP_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-dap-iff).

## $r$-large sets

Let $r$ be a natural number. A set $D$ of natural numbers is $r$-large when
every element of $D$ is positive, $r \ge 1$, and for every coloring $c$ of the positive integers
with the colors $0, 1, \dots, r - 1$ and every natural number $k \ge 1$ there are positive integers
$x_0, \dots, x_{k-1}$ that are monochromatic for $c$ and form a $D$-AP: there are a positive
integer $a$ and some $d \in D$ with $x_i = a + i d$ for all $i < k$.

Quantifying over every length $k \ge 1$ formalizes "arbitrarily long" monochromatic $D$-APs.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.IsRLarge`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-rlarge).

## Characterization of $r$-large sets

Let $r$ be a natural number and $D$ a set of natural
numbers. Then $D$ is $r$-large if and only if every element of $D$ is positive, $r \ge 1$, and for
every coloring $c$ of the positive integers with the colors $0, 1, \dots, r - 1$ and every natural
number $k \ge 1$ there are positive integers $x_0, \dots, x_{k-1}$ that are monochromatic for $c$
and form a $D$-AP: there are a positive integer $a$ and some $d \in D$ with $x_i = a + i d$ for
all $i < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.isRLarge_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-rlarge-iff).

## Large set

A set $D$ of natural numbers is large when it is $r$-large for every natural
number $r \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.IsLarge`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-large).

## Characterization of large sets

A set $D$ of natural numbers is large if and only if it
is $r$-large for every natural number $r \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-large).

Formalized by `MetaMathlibExt.isLarge_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-large-iff).

## $D$-diffsequences

Let $D$ be a set of natural numbers and $k$ a natural number. A
finite sequence $x_0, \dots, x_{k-1}$ of integers is a $D$-diffsequence when for every $i$ with
$i + 1 < k$ there is $d \in D$ with $x_{i+1} - x_i = d$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (D-diffsequence).

Formalized by `MetaMathlibExt.IsDDiffSequence`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-ddiff-sequence).

## Characterization of $D$-diffsequences

Let $D$ be a set of natural numbers and
$x_0, \dots, x_{k-1}$ integers. Then $x_0, \dots, x_{k-1}$ is a $D$-diffsequence if and only if
for every $i$ with $i + 1 < k$ there is $d \in D$ such that $x_{i+1} - x_i = d$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (D-diffsequence).

Formalized by `MetaMathlibExt.isDDiffSequence_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-ddiff-sequence-iff).

## $r$-accessibility for colorings of the positive integers

Let $r$ be a natural number. A set
$D$ of natural numbers is $r$-accessible when every element of $D$ is positive, $r \ge 1$, and for
every coloring $c$ of the positive integers with the colors $0, 1, \dots, r - 1$ and every natural
number $k \ge 1$ there are positive integers $x_0, \dots, x_{k-1}$ that are monochromatic for $c$
and form a $D$-diffsequence: $x_{i+1} - x_i \in D$, the difference taken in the integers, for every
$i$ with $i + 1 < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-accessible).

Formalized by `MetaMathlibExt.IsRAccessible`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-raccessible).

## Characterization of $r$-accessible sets

Let $r$ be a natural number and $D$ a set of
natural numbers. Then $D$ is $r$-accessible if and only if every element of $D$ is positive,
$r \ge 1$, and for every coloring $c$ of the positive integers with the colors $0, 1, \dots, r - 1$
and every natural number $k \ge 1$ there are positive integers $x_0, \dots, x_{k-1}$ that are
monochromatic for $c$ and form a $D$-diffsequence: $x_{i+1} - x_i \in D$, the difference taken in
the integers, for every $i$ with $i + 1 < k$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-accessible).

Formalized by `MetaMathlibExt.isRAccessible_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-raccessible-iff).

## Accessibility with more colors implies accessibility with fewer

Let $D$ be a set of
natural numbers and let $r, s$ be natural numbers with $1 \le r \le s$. If $D$ is
$s$-accessible, then $D$ is $r$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-accessible).

Formalized by `MetaMathlibExt.IsRAccessible.mono`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#mono).

## Accessible sets

A set $D$ of natural numbers is accessible if it is $r$-accessible for
every natural number $r \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-accessible).

Formalized by `MetaMathlibExt.IsAccessible`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-accessible).

## Accessibility means $r$-accessibility for every $r \ge 1$

A set $D$ of natural numbers
is accessible if and only if it is $r$-accessible for every natural number $r \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (r-accessible).

Formalized by `MetaMathlibExt.isAccessible_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-accessible-iff).

## Lacunary sequence

A sequence $(m_n)_{n \ge 0}$ of natural numbers is lacunary when
$m_n > 0$ for every $n$ and there is a real number $\lambda > 1$ such that
$m_{n+1} \ge \lambda m_n$ for every $n \ge 0$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Context (lacunary sequence).

Formalized by `MetaMathlibExt.IsLacunary`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-lacunary).

## Characterization of lacunary sequences

A sequence $(m_n)_{n \ge 0}$ of natural numbers
is lacunary if and only if $m_n > 0$ for every $n$ and there is a real number $q > 1$ such that
$m_{n+1} \ge q \, m_n$ for every $n \ge 0$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Context (lacunary sequence).

Formalized by `MetaMathlibExt.isLacunary_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-lacunary-iff).

## Lacunary set

A set $D$ of natural numbers is lacunary when $D = \{m_n : n \ge 0\}$ for
some lacunary sequence $(m_n)_{n \ge 0}$ of natural numbers.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Context (lacunary set).

Formalized by `MetaMathlibExt.IsLacunarySet`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-lacunary-set).

## Characterization of lacunary sets

A set $D$ of natural numbers is lacunary if and only
if there is a lacunary sequence $(m_n)_{n \ge 0}$ of natural numbers with
$D = \{m_n : n \ge 0\}$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Context (lacunary set).

Formalized by `MetaMathlibExt.isLacunarySet_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-lacunary-set-iff).

## Minimal system

Let $X$ be a compact metric space and $T$ a homeomorphism of $X$. The
system $(X, T)$ is minimal when there is no closed set $K \subseteq X$ that is nonempty, different
from $X$ and invariant, meaning $T(K) = K$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (topological dynamical system, minimal).

Formalized by `MetaMathlibExt.IsMinimalSystem`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-minimal-system).

## Characterization of minimal systems

Let $X$ be a compact metric space and
$T \colon X \to X$ a homeomorphism. Then $T$ is minimal if and only if there is no closed set
$K \subseteq X$ with $K \ne \emptyset$, $K \ne X$ and $T(K) = K$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (topological dynamical system, minimal).

Formalized by `MetaMathlibExt.isMinimalSystem_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-minimal-system-iff).

## Iterated preimage

For a homeomorphism $T$ of a topological space $X$, an integer $s$ and
a subset $U \subseteq X$, the iterated preimage $T^{-s} U$ is defined as the preimage
$(T^s)^{-1}(U)$ of $U$ under the $s$-th power $T^s$ of $T$ in the group of homeomorphisms of $X$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.iteratePreimage`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#iterate-preimage).

## Iterated preimage as a preimage under a power

For a homeomorphism $T$ of a topological
space $X$, an integer $s$ and a subset $U \subseteq X$, the iterated preimage $T^{-s} U$ is the
preimage $(T^s)^{-1}(U)$ of $U$ under the $s$-th power $T^s$ of $T$ in the group of
homeomorphisms of $X$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.iteratePreimage_eq`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#iterate-preimage-eq).

## Sets of $\ell$-topological recurrence

Let $\ell$ be a natural number. A set $D$ of
natural numbers is a set of $\ell$-topological recurrence when every element of $D$ is positive
and, for every compact metric space $X$, every minimal homeomorphism $T \colon X \to X$ and
every nonempty open set $U \subseteq X$, there is $d \in D$ such that
$\bigcap_{j=0}^{\ell} T^{-jd}(U)$ is nonempty, where $T^{-jd}(U)$ is the preimage of $U$ under
the $jd$-th iterate of $T$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.IsLTopologicalRecurrence`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-ltopological-recurrence).

## Characterization of $\ell$-topological recurrence

Let $\ell$ be a natural number and $D$
a set of natural numbers. Then $D$ is a set of $\ell$-topological recurrence if and only if every
element of $D$ is positive and, for every compact metric space $X$, every minimal homeomorphism
$T \colon X \to X$ and every nonempty open set $U \subseteq X$, there is $d \in D$ such that
$\bigcap_{j=0}^{\ell} T^{-jd}(U)$ is nonempty, where $T^{-jd}(U)$ is the preimage of $U$ under
the $jd$-th iterate of $T$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.isLTopologicalRecurrence_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-ltopological-recurrence-iff).

## Sets of topological recurrence

A set $D$ of natural numbers is a set of topological
recurrence when it is a set of $\ell$-topological recurrence for $\ell = 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.IsTopologicalRecurrence`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-topological-recurrence).

## Topological recurrence is $1$-topological recurrence

A set $D$ of natural numbers is a
set of topological recurrence if and only if it is a set of $\ell$-topological recurrence for
$\ell = 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.isTopologicalRecurrence_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-topological-recurrence-iff).

## Sets of multiple topological recurrence

A set $D$ of natural numbers is a set of multiple
topological recurrence when it is a set of $\ell$-topological recurrence for every natural number
$\ell \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.IsMultipleTopologicalRecurrence`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-multiple-topological-recurrence).

## Characterization of multiple topological recurrence

A set $D$ of natural numbers is a set
of multiple topological recurrence if and only if $D$ is a set of $\ell$-topological recurrence for
every natural number $\ell \ge 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Definition (ℓ-topological recurrence).

Formalized by `MetaMathlibExt.isMultipleTopologicalRecurrence_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-multiple-topological-recurrence-iff).

## Chromatically intersective sets

A set $D$ of natural numbers is chromatically
intersective if every element of $D$ is positive and, for every natural number $r \ge 1$ and
every coloring of the positive integers with $r$ colors, there are positive integers $a$ and $b$
of the same color whose difference $a - b$, computed in the integers, lies in $D$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 13(iv).

Formalized by `MetaMathlibExt.IsChromaticallyIntersective`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-chromatically-intersective).

## Characterization of chromatically intersective sets

A set $D$ of natural numbers is
chromatically intersective if and only if every element of $D$ is positive and, for every
natural number $r \ge 1$ and every coloring of the positive integers with $r$ colors, there are
positive integers $a$ and $b$ of the same color whose difference $a - b$, computed in the
integers, lies in $D$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 13(iv).

Formalized by `MetaMathlibExt.isChromaticallyIntersective_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-chromatically-intersective-iff).

## Positive Fibonacci set

The positive Fibonacci set is $\{F_n : n \ge 2\}$, where the
Fibonacci numbers are $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. Equivalently, it is the
set $\{1, 2, 3, 5, 8, \dots\}$ of positive Fibonacci numbers, each counted once.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 1.

Formalized by `MetaMathlibExt.positiveFibonacciSet`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#positive-fibonacci-set).

## Membership in the positive Fibonacci set

Write $F_n$ for the $n$-th Fibonacci number,
with $F_0 = 0$ and $F_1 = 1$. A natural number $d$ belongs to the positive Fibonacci set if and
only if $d = F_n$ for some natural number $n \ge 2$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 1.

Formalized by `MetaMathlibExt.mem_positiveFibonacciSet_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#mem-positive-fibonacci-set-iff).

## Even Fibonacci set

Let $F_m$ denote the $m$-th Fibonacci number, with $F_0 = 0$ and
$F_1 = 1$. The even Fibonacci set is $\{F_{3n+3} : n \ge 0\}$; its first terms are
$2, 8, 34, \dots$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 2.

Formalized by `MetaMathlibExt.evenFibonacciSet`, a definition declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#even-fibonacci-set).

## Membership in the even Fibonacci set

Write $F_m$ for the $m$-th Fibonacci number, with
$F_0 = 0$ and $F_1 = 1$. A natural number $d$ belongs to the even Fibonacci set if and only if
$d = F_{3n+3}$ for some natural number $n$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 2.

Formalized by `MetaMathlibExt.mem_evenFibonacciSet_iff`, a theorem declared in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#mem-even-fibonacci-set-iff).

## Growth bound for the degree of accessibility

Let $r \ge 2$, let $d_0 < d_1 < d_2 < \cdots$
be a strictly increasing sequence of natural numbers with $d_0 > 0$, and let
$D = \{d_n : n \ge 0\}$. If there are a real number $\delta > 0$ and an integer $N \ge 1$ such that
$d_{n+1} \ge \left(2 + \frac{1}{r-1} + \delta\right) d_n$ for every $n \ge N - 1$, then $D$ is not
$r$-accessible.

In the paper's terms, the degree of accessibility of $D$ is at most $r - 1$; the enumeration here
starts at index $0$, so $d_n$ is the paper's $d_{n+1}$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 1.

Stated but not proved: `MetaMathlibExt.accessibility_degree_growth_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#accessibility-degree-growth-bound).

## Fast eventual growth rules out 2-accessibility

Let $d_0 < d_1 < d_2 < \cdots$ be a
strictly increasing sequence of natural numbers with $d_0 > 0$, and let
$D = \{d_n : n \in \mathbb{N}\}$. Suppose there are a real number $\delta > 0$ and a natural
number $N \ge 1$ such that $d_{n+1} \ge (3 + \delta) d_n$ for every $n \in \mathbb{N}$ with
$n + 1 \ge N$. Then $D$ is not $2$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Corollary 1.

Stated but not proved: `MetaMathlibExt.not_two_accessible_of_growth` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#not-two-accessible-of-growth).

## 2-large sets contain multiples of every positive integer

Every $2$-large set $D$ of
positive integers contains a multiple of each positive integer $m$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 2.

Stated but not proved: `MetaMathlibExt.two_large_contains_multiples` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#two-large-contains-multiples).

## Finite removal preserves $r$-largeness

Let $r$ be a natural number. If a set
$D \subseteq \mathbb{N}$ is $r$-large and $F \subseteq \mathbb{N}$ is finite, then $D \setminus F$
is $r$-large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 3.

Stated but not proved: `MetaMathlibExt.rLarge_sdiff_finite` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#r-large-sdiff-finite).

## Largeness is partition regular

If $D_1, D_2 \subseteq \mathbb{N}$ and their union
$D = D_1 \cup D_2$ is large, then $D_1$ is large or $D_2$ is large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 4.

Stated but not proved: `MetaMathlibExt.large_union_partition` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#large-union-partition).

## Sets growing by a factor of three are not 2-large

Let $d_0 < d_1 < d_2 < \cdots$ be a
strictly increasing sequence of natural numbers with $d_0 > 0$ and $d_{n+1} \ge 3 d_n$ for every
$n \in \mathbb{N}$, and let $D = \{d_n : n \in \mathbb{N}\}$. Then $D$ is not $2$-large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 5.

Stated but not proved: `MetaMathlibExt.not_two_large_of_triple_growth` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#not-two-large-of-triple-growth).

## Dilates of a finite union of lacunary sets stay away from the integers

Let $\ell \ge 1$
and let $S_0, \dots, S_{\ell-1} \subseteq \mathbb{N}$ be lacunary sets with union
$S = \bigcup_i S_i$. Then there are real numbers $\alpha$ and $\varepsilon > 0$ such that the
infimum over $s \in S$ of the distance $|\alpha s - \operatorname{round}(\alpha s)|$ from
$\alpha s$ to its nearest integer $\operatorname{round}(\alpha s)$ equals $\varepsilon$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 6.

Stated but not proved: `MetaMathlibExt.lacunary_union_avoids_integers` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#lacunary-union-avoids-integers).

## Two-colorings avoiding long $D$-progressions

Let $D$ be a set of positive integers,
let $\alpha$ be a real number and let $\varepsilon > 0$ be such that
$\lVert \alpha d \rVert \ge \varepsilon$ for every $d \in D$, where $\lVert t \rVert$ denotes the
distance from $t$ to the nearest integer. Then there is a $2$-coloring of the positive integers
with no monochromatic $D$-arithmetic progression of length $\lceil 1/(2\varepsilon) \rceil + 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 7.

Stated but not proved: `MetaMathlibExt.two_coloring_avoids_long_DAP` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#two-coloring-avoids-long-dap).

## Finite unions of lacunary sets are not 2-large

For every $n \ge 1$ and all lacunary sets
$D_1, \dots, D_n$, the union $D_1 \cup \dots \cup D_n$ is not 2-large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 8.

Stated but not proved: `MetaMathlibExt.finite_union_lacunary_not_two_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#finite-union-lacunary-not-two-large).

## Positive values of a polynomial vanishing at zero form a large set

Let $p$ be a
polynomial with integer coefficients, positive leading coefficient and $p(0) = 0$. Then the set
of positive integers $d$ such that $p(n) = d$ for some positive integer $n$ is large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 9.

Stated but not proved: `MetaMathlibExt.polynomial_range_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#polynomial-range-large).

## A coloring criterion for accessibility of a shifted set

Let $r \ge 2$ and $c$ be natural
numbers, let $D$ be a set of positive integers, and write $D + c = \{d + c : d \in D\}$. Suppose
that for every coloring of $D$ with $r - 1$ colors and every $k \ge 1$ there are
$x_0, \dots, x_{k-1} \in D$, all of the same color, that form a $(D + c)$-diffsequence, that is,
$x_{i+1} - x_i \in D + c$ for every $i < k - 1$. Then $D + c$ is $r$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 10.

Stated but not proved: `MetaMathlibExt.accessible_of_colored_subset_diffsequences` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#accessible-of-colored-subset-diffsequenc).

## Sets containing their own long diffsequences are 2-accessible

Let $D$ be a set of
positive integers. If for every $k \ge 1$ there are positive integers $x_1, \dots, x_k$, all in
$D$, that form a $D$-diffsequence, then $D$ is $2$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Corollary 2.

Stated but not proved: `MetaMathlibExt.two_accessible_of_internal_diffsequences` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#two-accessible-of-internal-diffsequences).

## Integral quotients of an accessible set

Let $d \ge 1$ and $r$ be natural numbers and let
$A$ be a set of natural numbers. If $A$ is $rd$-accessible, then the set $\{n \ge 1 : nd \in A\}$,
that is, the positive integers of the form $a/d$ with $a \in A$, is $r$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 11(i).

Stated but not proved: `MetaMathlibExt.accessible_integral_quotients` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#accessible-integral-quotients).

## Multiples of $d$ in an accessible set

Let $d \ge 1$ and $r$ be natural numbers and let $A$
be a set of natural numbers. If $A$ is $rd$-accessible, then the set $\{a \in A : d \mid a\}$ of
members of $A$ divisible by $d$ is $r$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 11(ii).

Stated but not proved: `MetaMathlibExt.accessible_divisible_subset` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#accessible-divisible-subset).

## Colorings avoiding long diffsequences under fractional-part bounds

Let $r \ge 1$, let
$d_0 < d_1 < \cdots$ be a strictly increasing sequence of natural numbers with $d_0 > 0$, and let
$D = \{d_n : n \ge 0\}$. Suppose there are real numbers $\alpha$ and $\varepsilon > 0$ such that
for every $n$ the fractional part of $\alpha d_n$ lies in the closed interval
$[\varepsilon, (r-1)/r]$. Then there is a coloring of the positive integers with $r$ colors that
has no monochromatic $D$-diffsequence of positive integers of length
$\lceil 1/(r\varepsilon) \rceil + 1$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 12.

Stated but not proved: `MetaMathlibExt.coloring_avoids_diffsequence_of_fractional_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#coloring-avoids-diffsequence-of-fraction).

## A 2-coloring with no monochromatic 6-term progression with positive Fibonacci gap

There
is a coloring of the positive integers with two colors such that no 6-term arithmetic progression
$a, a + d, \dots, a + 5d$ of positive integers whose gap $d$ is a positive Fibonacci number is
monochromatic.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 1 (coloring claim).

Stated but not proved: `MetaMathlibExt.fibonacci_two_coloring_avoids_six_term_AP` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-two-coloring-avoids-six-term-a).

## The positive Fibonacci set is not 2-large

Let $F_n$ denote the $n$-th Fibonacci number,
with $F_0 = 0$ and $F_1 = 1$. The positive Fibonacci set
$\{F_n : n \ge 2\} = \{1, 2, 3, 5, 8, \dots\}$ is not $2$-large.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 1 (consequence).

Stated but not proved: `MetaMathlibExt.fibonacci_not_two_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-not-two-large).

## A 2-coloring with no monochromatic 4-term even-Fibonacci diffsequence

Let $F_m$ denote
the $m$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$, and let
$E = \{F_{3n+3} : n \ge 0\} = \{2, 8, 34, \dots\}$ be the even Fibonacci set. There is a coloring
of the positive integers with $2$ colors under which no four positive integers
$x_0, x_1, x_2, x_3$ of the same color satisfy $x_{i+1} - x_i \in E$ for $i = 0, 1, 2$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 2 (coloring claim).

Stated but not proved: `MetaMathlibExt.even_fibonacci_two_coloring_avoids_four_term_diffsequence` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#even-fibonacci-two-coloring-avoids-four).

## The even Fibonacci set is not 2-accessible

Let $F_m$ denote the $m$-th Fibonacci number,
with $F_0 = 0$ and $F_1 = 1$. The even Fibonacci set
$\{F_{3n+3} : n \ge 0\} = \{2, 8, 34, \dots\}$ is not $2$-accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Proposition 2 (consequence).

Stated but not proved: `MetaMathlibExt.even_fibonacci_not_two_accessible` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#even-fibonacci-not-two-accessible).

## Furstenberg–Weiss correspondence for translation-invariant families

Let $\mathcal{A}$ be
a collection of finite sets of integers that is closed under translation, that is,
$A + t \in \mathcal{A}$ for all $A \in \mathcal{A}$ and $t \in \mathbb{Z}$, and let $r \ge 1$.
For a homeomorphism $T$ and an integer $a$, write $T^{-a}(U)$ for the preimage of $U$ under the
$a$-th power of $T$. Then the following three conditions are equivalent: (a) for every coloring
of $\mathbb{Z}$ with $r$ colors there are a color $i$ and a set $A \in \mathcal{A}$ all of whose
elements have color $i$; (b) for every nonempty compact metric space $X$, every homeomorphism
$T$ of $X$ and every cover of $X$ by $r$ open sets $U_1, \dots, U_r$, there are $i$ and
$A \in \mathcal{A}$ such that $\bigcap_{a \in A} T^{-a}(U_i)$ is nonempty; (c) the same holds
for every nonempty compact metric space $X$, every minimal homeomorphism $T$ of $X$ and every
cover of $X$ by $r$ clopen sets $U_1, \dots, U_r$.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Lemma 1.

Stated but not proved: `MetaMathlibExt.furstenberg_weiss_correspondence` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#furstenberg-weiss-correspondence).

## Topological recurrence, accessibility and chromatic intersectivity

Let $D$ be a set
of positive integers. Say that $D$ has *diffsequence recurrence* if for every compact metric
space $X$, every minimal homeomorphism $T$ of $X$, every nonempty open set $U \subseteq X$ and
every $k \ge 1$ there are integers $s_1, \dots, s_k$ forming a $D$-diffsequence such that
$U \cap T^{-s_1}U \cap \dots \cap T^{-s_k}U$ is nonempty, where $T^{-s}U$ is the preimage of $U$
under the integer power $T^s$. Then the following are equivalent: $D$ is a set of topological
recurrence; $D$ has diffsequence recurrence; $D$ is accessible; $D$ is chromatically
intersective.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 13.

Stated but not proved: `MetaMathlibExt.recurrence_accessibility_equivalences` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#recurrence-accessibility-equivalences).

## One part of a union inherits $k$-topological recurrence

Let $k$ be a natural number
and let $D_1, D_2 \subseteq \mathbb{N}$. If $D_1 \cup D_2$ is a set of $k$-topological recurrence,
then $D_1$ or $D_2$ is a set of $k$-topological recurrence.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Theorem 14.

Stated but not proved: `MetaMathlibExt.topological_recurrence_union_partition` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#topological-recurrence-union-partition).

## One part of an accessible union is accessible

Let $D$, $D_1$ and $D_2$ be sets of
natural numbers with $D = D_1 \cup D_2$. If $D$ is accessible, then $D_1$ is accessible or $D_2$
is accessible.

## Sources

- Oscar Quester, *On Some Properties of Accessible Sets*, INTEGERS 25 (2025), Article A64, Corollary 3.

Stated but not proved: `MetaMathlibExt.accessible_union_partition` is written with `theorem_wanted` in [WantedExt/Combinatorics/AccessibleSetsWanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AccessibleSetsWanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#accessible-union-partition).

## Monochromatic finite sequences

Given a colouring $c : \mathbb{N} \to \{0, \dots, r - 1\}$
of the natural numbers with $r$ colours, a finite sequence $x_0, \dots, x_{k-1}$ of natural
numbers is monochromatic when all its terms have the same colour: $c(x_i) = c(x_j)$ for all
$i, j < k$.

## Sources

- `OPG-1797` (Open Problem Garden, node 1797, http://www.openproblemgarden.org/op/2_accessibility_of_primes): formalizes "monochromatic sequence" from the definition of `r`-accessible.

Formalized by `MathlibExt.Combinatorics.PrimeTwoAccessibilityWanted.IsMonochromatic`, a definition declared in [WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-monochromatic-2).

## Finite $S$-diffsequences

For a set $S$ of natural numbers, a finite sequence
$x_0, \dots, x_{k-1}$ of natural numbers is an $S$-diffsequence when each term is the previous
one plus an element of $S$: for every $i$ with $i + 1 < k$ there is $d \in S$ with
$x_{i+1} = x_i + d$.

## Sources

- `OPG-1797` (Open Problem Garden, node 1797, http://www.openproblemgarden.org/op/2_accessibility_of_primes): formalizes "`S`-diffsequence", i.e. `x_{i+1} - x_i ∈ S`, stated additively as `x (i+1) = x i + d` with `d ∈ S`.

Formalized by `MathlibExt.Combinatorics.PrimeTwoAccessibilityWanted.IsSDiffSequence`, a definition declared in [WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-sdiff-sequence).

## $r$-accessible sets of natural numbers

A set $S \subseteq \mathbb{N}$ is $r$-accessible
when for every colouring $c : \mathbb{N} \to \{0, \dots, r - 1\}$ with $r$ colours and every
length $k \ne 1$ there is a sequence $x_0, \dots, x_{k-1}$ of natural numbers that is
monochromatic for $c$ and is an $S$-diffsequence: for each $i$ with $i + 1 < k$ there is
$d \in S$ with $x_{i+1} = x_i + d$.

## Sources

- `OPG-1797` (Open Problem Garden, node 1797, http://www.openproblemgarden.org/op/2_accessibility_of_primes): `S` is `r`-accessible if for every `r`-coloring of `ℕ` and every `k ∈ ℕ \ {1}` there is a monochromatic `S`-diffsequence of length `k`.

Formalized by `MathlibExt.Combinatorics.PrimeTwoAccessibilityWanted.IsRAccessible`, a definition declared in [WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#is-raccessible-2).

## 2-accessibility of the primes

The statement that the set of prime numbers is
$2$-accessible: for every colouring $c : \mathbb{N} \to \{0, 1\}$ of the natural numbers with two
colours and every length $k \ne 1$ there is a sequence $x_0, \dots, x_{k-1}$ of natural numbers,
all of the same colour, such that each difference $x_{i+1} - x_i$ is a prime number. Open Problem
Garden question OPG-1797 asks whether this holds.

## Sources

- `OPG-1797` (Open Problem Garden, node 1797, http://www.openproblemgarden.org/op/2_accessibility_of_primes): "Is the set of prime numbers 2-accessible?"

Formalized by `MathlibExt.Combinatorics.PrimeTwoAccessibilityWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#conjecture).

## The primes are 2-accessible

The set of prime numbers is $2$-accessible: for every colouring
$c : \mathbb{N} \to \{0, 1\}$ of the natural numbers with two colours and every length $k \ne 1$
there is a sequence $x_0, \dots, x_{k-1}$ of natural numbers, all of the same colour, such that
each difference $x_{i+1} - x_i$ is a prime number.

Quester proves this as a special case of Theorem 1 of the paper, using the
Frantzikinakis–Host–Kra recurrence theorem along shifted primes.

## Sources

- Oscar Quester, The Primes are 2-Accessible, arXiv preprint (2026), arXiv:2606.00410, https://arxiv.org/abs/2606.00410; Nikos Frantzikinakis, Bernard Host, Bryna Kra, The polynomial multidimensional Szemeredi theorem along shifted primes, Israel J. Math. 194 (2013), 331-348, arXiv:1009.1484, https://arxiv.org/abs/1009.1484.

Stated but not proved: `MathlibExt.Combinatorics.PrimeTwoAccessibilityWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PrimeTwoAccessibilityWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#conjecture-holds).

## Halves of even Fibonacci numbers

Let $F_m$ be the $m$-th Fibonacci number, with $F_0 = 0$
and $F_1 = 1$. The set of halves of the positive even Fibonacci numbers is
$G = \{F_{3n}/2 : n \ge 1\} = \{1, 4, 17, 72, \dots\}$; its elements are written
$g_n = F_{3n}/2$ for $n \ge 1$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Section 2 (notation `G`, `g_n`).

Formalized by `MetaMathlibExt.halfEvenFibonacciSet`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#half-even-fibonacci-set).

## $4$ is half of an even Fibonacci number

Let $F_m$ be the $m$-th Fibonacci number, with
$F_0 = 0$ and $F_1 = 1$. The number $4$ belongs to the set
$G = \{F_{3n}/2 : n \ge 1\} = \{1, 4, 17, 72, \dots\}$ of halves of the positive even Fibonacci
numbers; indeed $4 = F_6/2$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Section 2 (notation `G`, `g_n`).

Formalized by `MetaMathlibExt.four_mem_halfEvenFibonacciSet`, a theorem declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#four-mem-half-even-fibonacci-set).

## The Thue–Morse morphism $\mu$

The morphism $\mu$ on binary words sends the letter $0$ to
the word $10$ and the letter $1$ to the word $01$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Definition 1.

Formalized by `MetaMathlibExt.thueMorseMorphism`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#thue-morse-morphism).

## The morphism $\nu$

The morphism $\nu$ is given on the letters $0$ and $1$ by
$\nu(0) = 1$ and $\nu(1) = 00$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Definition 1.

Formalized by `MetaMathlibExt.fibonacciNuMorphism`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-nu-morphism).

## Wesley's word $S$

Let $\mu$ be the morphism of binary words with $0 \mapsto 10$ and
$1 \mapsto 01$, and let $f_0 = 0$, $f_1 = 01$, $f_2 = 010$, $\dots$ be the finite Fibonacci words.
The word $S$ is the infinite binary word, indexed from $0$, whose letter at index $n$ is the
letter at index $n$ of $\mu(f_{n+2})$.

Since each $f_k$ is a prefix of $f_{k+1}$, $S = \mu(F_\infty) = 1001101001\dots$, where
$F_\infty = 010010100\dots$ is the infinite Fibonacci word.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Definition 1.

Formalized by `MetaMathlibExt.wesleyWordS`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#wesley-word-s).

## Wesley's word $T$

Let $\nu$ be the morphism of binary words with $0 \mapsto 1$ and
$1 \mapsto 00$, and let $f_0 = 0$, $f_1 = 01$, $f_2 = 010$, $\dots$ be the finite Fibonacci words.
The word $T$ is the infinite binary word, indexed from $0$, whose letter at index $n$ is the
letter at index $n$ of $\nu(f_{n+2})$.

Since each $f_k$ is a prefix of $f_{k+1}$, $T = \nu(F_\infty) = 1001100100\dots$, where
$F_\infty = 010010100\dots$ is the infinite Fibonacci word.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Definition 1.

Formalized by `MetaMathlibExt.wesleyWordT`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#wesley-word-t).

## The first ten letters of Wesley's words $S$ and $T$

Indexing letters from $0$, the
letters of $S$ at indices $0, 1, \dots, 9$ are $1, 0, 0, 1, 1, 0, 1, 0, 0, 1$ and the letters of
$T$ at indices $0, 1, \dots, 9$ are $1, 0, 0, 1, 1, 0, 0, 1, 0, 0$; that is, $S$ begins with
$1001101001$ and $T$ begins with $1001100100$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Definition 1.

Formalized by `MetaMathlibExt.wesleyWords_first_ten`, a theorem declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#wesley-words-first-ten).

## Wesley's constants $c_{n,\varepsilon}$

For a natural number $n$ and an integer
$\varepsilon$, the real number $c_{n,\varepsilon}$ is defined by the residue of $n$ modulo $4$:
if $n \equiv 0 \pmod 4$, then $c_{n,\varepsilon} = (4 + (2\sqrt5 - 5)\varepsilon)/10$;
if $n \equiv 1 \pmod 4$, then $c_{n,\varepsilon} = (11 - 4\sqrt5)/5$ when $\varepsilon = -4$ and
$c_{n,\varepsilon} = (4 + (4\sqrt5 - 5)\varepsilon)/20$ otherwise;
if $n \equiv 2 \pmod 4$, then $c_{n,\varepsilon} = (6 + (2\sqrt5 - 5)\varepsilon)/10$;
if $n \equiv 3 \pmod 4$, then $c_{n,\varepsilon} = (9 - 4\sqrt5)/5$ when $\varepsilon = -4$ and
$c_{n,\varepsilon} = (8 + (2\sqrt5 - 5)\varepsilon)/10$ otherwise.

Lemma 5 uses these constants only for $\varepsilon \in \{-4, 0, 4\}$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 5 (definition of `c_{n,ε}`).

Formalized by `MetaMathlibExt.wesleyFractionalConstant`, a definition declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#wesley-fractional-constant).

## Wesley's constant $c_{n,0}$ for $n \equiv 0 \pmod 4$

For every natural number $n$ with
$n \equiv 0 \pmod 4$, Wesley's constant satisfies $c_{n,0} = 2/5$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 5 (definition of `c_{n,ε}`).

Formalized by `MetaMathlibExt.wesleyFractionalConstant_zero_of_mod_four_eq_zero`, a theorem declared in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#wesley-fractional-constant-zero-of-mod-f).

## The Fibonacci numbers have degree of accessibility at most $3$

The positive Fibonacci set
$\{1, 2, 3, 5, 8, \dots\}$ is not $r$-accessible for any natural number $r \ge 4$. Moreover, some
coloring of the positive integers with four colors admits no monochromatic $4$-term
diffsequence with differences in the positive Fibonacci set: there are no positive integers
$x_0, x_1, x_2, x_3$ of one color such that $x_{i+1} - x_i$ is a positive Fibonacci number for
$i = 0, 1, 2$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Theorem 1.

Stated but not proved: `MetaMathlibExt.fibonacciSet_degreeOfAccessibility_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-set-degree-of-accessibility-le).

## Arithmetic progressions with Fibonacci gaps are not $2$-regular

There is a coloring of the
positive integers with two colors that admits no monochromatic $5$-term arithmetic progression
with gap in the positive Fibonacci set $\{1, 2, 3, 5, 8, \dots\}$, that is, no positive integers
$x_0, \dots, x_4$ of one color with $x_i = a + i d$ for all $i < 5$, for a positive integer $a$ and
a positive Fibonacci number $d$. Moreover, the positive Fibonacci set is $1$-large, and it is not
$r$-large for any natural number $r \ge 2$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Theorem 2.

Stated but not proved: `MetaMathlibExt.fibonacci_gap_progressions_not_two_regular` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-gap-progressions-not-two-regul).

## Fibonacci numbers divided by the golden ratio

Let $F_n$ be the $n$-th Fibonacci number,
with $F_0 = 0$ and $F_1 = 1$, and let $\varphi = (1 + \sqrt{5})/2$ be the golden ratio. For every
natural number $n \ge 2$,

$$\frac{F_n}{\varphi} - F_{n-1} = (-1)^{n+1} \varphi^{-n}.$$

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Corollary 1.

Stated but not proved: `MetaMathlibExt.fib_div_goldenRatio_sub_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fib-div-golden-ratio-sub-fib).

## Beatty-sequence descriptions of the words $F_\infty$, $S$ and $T$

Let
$\varphi = (1 + \sqrt{5})/2$ be the golden ratio and $F_\infty = 010010100\cdots$ the infinite
Fibonacci word. Let $S = \mu(F_\infty)$ be its image under the morphism $\mu$ with $\mu(0) = 10$
and $\mu(1) = 01$, and $T = \nu(F_\infty)$ its image under the morphism $\nu$ with $\nu(0) = 1$
and $\nu(1) = 00$. For a word $W$ and an integer $n \ge 1$, write $W(n)$ for the $n$-th letter of
$W$, counting from $1$. Then:
(i) for every integer $n \ge 1$, $F_\infty(n) = 0$ if and only if $n = \lfloor m\varphi \rfloor$
for some integer $m$;
(ii) for every integer $n$, positive or not, if $n \ne \lfloor m\varphi \rfloor$ for every
integer $m$, then $n + 1 = \lfloor m'\varphi \rfloor$ and $n - 1 = \lfloor m''\varphi \rfloor$ for
some integers $m'$ and $m''$;
(iii) for every integer $n \ge 1$, $S(n) = 0$ if and only if either $n$ is even and
$n/2 = \lfloor m\varphi \rfloor$ for some integer $m$, or $n$ is odd and
$(n+1)/2 \ne \lfloor m\varphi \rfloor$ for every integer $m$;
(iv) for every integer $n \ge 1$, $T(n) = 1$ if and only if $n = 2\lfloor m\varphi \rfloor - m$
for some integer $m$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 2.

Stated but not proved: `MetaMathlibExt.fibonacciWord_beatty_properties` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fibonacci-word-beatty-properties).

## Halved even Fibonacci numbers and $4$-accessibility of the Fibonacci numbers

Write $f_n$
for the $n$-th Fibonacci number ($f_0 = 0$, $f_1 = 1$). Let $F = \{1, 2, 3, 5, 8, \dots\}$ be the
set of positive Fibonacci numbers and $G = \{f_{3n}/2 : n \ge 1\} = \{1, 4, 17, 72, \dots\}$ the set
of halves of the even Fibonacci numbers. If $G$ is not $2$-accessible, then $F$ is not
$4$-accessible.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 3.

Stated but not proved: `MetaMathlibExt.not_accessible_four_of_halfEvenFibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#not-accessible-four-of-half-even-fibonac).

## Differences of fractional parts of multiples of the golden ratio

Let $F_m$ be the $m$-th
Fibonacci number, with $F_0 = 0$ and $F_1 = 1$, let $\varphi = (1 + \sqrt{5})/2$ be the golden
ratio, and write $\{y\} = y - \lfloor y \rfloor$ for the fractional part. Let $i \ge 1$ be a
natural number, put $g_i = F_{3i}/2$ (an integer, since $F_{3i}$ is even), and let
$x_1, x_2, m_1, m_2$ be integers. Then:
(i) if $g_i$ is even, $2(x_2 - x_1) = g_i$, $x_1 = \lfloor m_1\varphi \rfloor$ and
$x_2 = \lfloor m_2\varphi \rfloor$, then
$\{m_2\varphi\} - \{m_1\varphi\} \le (\varphi^{-3i+1} - \varphi)/4 < -0.38$;
(ii) if $g_i$ is odd, $2(x_2 - x_1) = g_i + 1$, $x_1 = \lfloor m_1\varphi \rfloor$ and
$x_2 + 1 = \lfloor m_2\varphi \rfloor$, then
$\{m_2\varphi\} - \{m_1\varphi\} < (3\varphi - 6)/4 < -0.28$;
(iii) if $g_i$ is odd, $i > 1$, $2(x_2 - x_1) = g_i - 1$, $x_1 + 1 = \lfloor m_1\varphi \rfloor$
and $x_2 = \lfloor m_2\varphi \rfloor$, then
$\{m_2\varphi\} - \{m_1\varphi\} < (-5\varphi + 6)/4 < -0.52$.

The paper states (i) with a strict inequality, but equality occurs: $i = 2$, $m_1 = 1$, $m_2 = 2$,
$x_1 = 1$, $x_2 = 3$ give $\{2\varphi\} - \{\varphi\} = (\varphi^{-5} - \varphi)/4$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 4.

Stated but not proved: `MetaMathlibExt.fract_goldenRatio_differences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fract-golden-ratio-differences).

## Fractional parts of shifted Fibonacci numbers divided by $\sqrt{5}$

Let $F_n$ be the
$n$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$, let $\varphi = (1 + \sqrt{5})/2$ be the
golden ratio, so that $2\varphi - 1 = \sqrt{5}$, and write $\{y\} = y - \lfloor y \rfloor$ for the
fractional part. Let $n \ge 13$ be a natural number and $\varepsilon \in \{-4, 0, 4\}$, let
$c_{n,\varepsilon}$ be Wesley's constant, which depends on $n \bmod 4$ and $\varepsilon$, and put
$y = (F_n + \varepsilon)/(2\varphi - 1)$. Then
(i) $\{y\} = -2(-\varphi)^{-n}/5 + c_{n,\varepsilon}$, and
(ii) $\lfloor y \rfloor$ is even if and only if $\varepsilon = 0$ and
$n \equiv 0, 1, 2, 3, 5, 10 \pmod{12}$, or $\varepsilon = 4$ and
$n \equiv 0, 2, 3, 9, 10 \pmod{12}$, or $\varepsilon = -4$ and
$n \equiv 0, 1, 2, 5, 7, 10, 11 \pmod{12}$.

The paper prints $+2(-\varphi)^{-n}/5$ in (i). The sign $-$ is the one its proof derives
(Equation (1)); the printed sign fails for every $n \ge 13$, since this term is nonzero.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 5.

Stated but not proved: `MetaMathlibExt.fract_fib_add_div_sqrt_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#fract-fib-add-div-sqrt-five).

## The Lucas numbers are not $4$-accessible

Let $L = \{2, 1, 3, 4, 7, \dots\}$ be the set of
Lucas numbers $L_0 = 2$, $L_1 = 1$, $L_{n+2} = L_{n+1} + L_n$. There is a coloring of the positive
integers with the colors $0, 1, 2, 3$ for which no sequence $x_0, x_1, x_2$ of positive integers is
both monochromatic and an $L$-diffsequence; and $L$ is not $r$-accessible for any $r \ge 4$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Lemma 6.

Stated but not proved: `MetaMathlibExt.lucasSet_not_four_accessible` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#lucas-set-not-four-accessible).

## The even Fibonacci numbers have degree of accessibility $1$

The even Fibonacci set
$\{2, 8, 34, \dots\}$ is $1$-accessible, and it is not $r$-accessible for any natural number
$r \ge 2$.

## Sources

- William J. Wesley, *Improved Ramsey-Type Theorems for Fibonacci Numbers and Other Sequences*, INTEGERS 25 (2025), Article A29, Corollary 2.

Stated but not proved: `MetaMathlibExt.evenFibonacciSet_degreeOfAccessibility_eq_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/FibonacciDiffsequenceRamseyWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html#even-fibonacci-set-degree-of-accessibili).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Accessible sets and diffsequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/accessible-sets-and-diffsequences)
