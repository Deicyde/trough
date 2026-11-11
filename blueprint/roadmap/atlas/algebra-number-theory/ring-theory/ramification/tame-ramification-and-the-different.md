---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.MaximalIdealGradedPiece, IsDiscreteValuationRing.residueFieldLinearEquivMaximalIdealGradedPiece, IsDiscreteValuationRing.finrank_maximalIdealGradedPiece, IsDiscreteValuationRing.residueFieldMulMaximalIdealGradedPiece, IsDiscreteValuationRing.residueFieldMulMaximalIdealGradedPiece_residue_mk, IsDiscreteValuationRing.residueFieldLinearEquivMaximalIdealGradedPiece_conj_lmul, IsDiscreteValuationRing.trace_residueFieldMulMaximalIdealGradedPiece, ResidueFieldMaximalIdealPowQuotient
statement: formalized
proof: formalized
---

# Tame ramification and the different

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html).

## Graded pieces of the maximal-ideal filtration

Let $R$ be a discrete valuation ring with
maximal ideal $\mathfrak{m}$. For $i \in \mathbb{N}$, the $i$-th graded piece is the $R$-module
$\mathfrak{m}^i/\mathfrak{m}^{i+1}$, realized as the quotient of the ideal $\mathfrak{m}^i$,
viewed as an $R$-module, by its submodule $\mathfrak{m} \cdot \mathfrak{m}^i$.

Formalized by `IsDiscreteValuationRing.MaximalIdealGradedPiece`, an abbreviation declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#maximal-ideal-graded-piece).

## Graded pieces of a DVR as copies of the residue field

Let $R$ be a discrete valuation
ring with maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$, and let
$\varpi$ be a generator of $\mathfrak{m}$ chosen once and for all. For $i \in \mathbb{N}$, the
map $\kappa \to \mathfrak{m}^i/\mathfrak{m}^{i+1}$ sending the class of $r \in R$ to the class
of $r \varpi^i$ is a $\kappa$-linear isomorphism.

Here $\kappa$ acts on $\mathfrak{m}^i/\mathfrak{m}^{i+1}$ through $R$, which is well defined
because $\mathfrak{m}$ annihilates the graded piece.

Formalized by `IsDiscreteValuationRing.residueFieldLinearEquivMaximalIdealGradedPiece`, a definition declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-linear-equiv-maximal-ideal).

## Graded pieces of a DVR are one-dimensional

Let $R$ be a discrete valuation ring with
maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$. For every
$i \in \mathbb{N}$, the graded piece $\mathfrak{m}^i/\mathfrak{m}^{i+1}$ is a vector space of
dimension one over $\kappa$.

Formalized by `IsDiscreteValuationRing.finrank_maximalIdealGradedPiece`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPiece.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#finrank-maximal-ideal-graded-piece).

## Multiplication by a residue class on a graded piece

Let $R$ be a discrete valuation ring
with maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$. For $a \in \kappa$
and $i \in \mathbb{N}$, this is the $\kappa$-linear endomorphism $x \mapsto a x$ of the graded
piece $\mathfrak{m}^i/\mathfrak{m}^{i+1}$.

Formalized by `IsDiscreteValuationRing.residueFieldMulMaximalIdealGradedPiece`, a definition declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-mul-maximal-ideal-graded-p).

## Multiplication by a residue class on representatives

Let $R$ be a discrete valuation
ring with maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$. For $x \in R$,
$i \in \mathbb{N}$ and $y \in \mathfrak{m}^i$, multiplication by the residue class
$\bar{x} \in \kappa$ on $\mathfrak{m}^i/\mathfrak{m}^{i+1}$ sends the class of $y$ to the class
of $x y$.

Formalized by `IsDiscreteValuationRing.residueFieldMulMaximalIdealGradedPiece_residue_mk`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-mul-maximal-ideal-graded-p-2).

## The residue-field isomorphism intertwines multiplication

Let $R$ be a discrete valuation
ring with maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$, let
$i \in \mathbb{N}$, and let $e : \kappa \to \mathfrak{m}^i/\mathfrak{m}^{i+1}$ be the
$\kappa$-linear isomorphism of the residue field with the graded piece. Let $K$ be a field, with
a $K$-algebra structure on $\kappa$ and a $K$-module structure on
$\mathfrak{m}^i/\mathfrak{m}^{i+1}$ such that $(c b) x = c (b x)$ for all $c \in K$,
$b \in \kappa$ and $x \in \mathfrak{m}^i/\mathfrak{m}^{i+1}$. Then for every $a \in \kappa$,
writing $\mu_a : \kappa \to \kappa$ for multiplication by $a$, the $K$-linear map
$e \circ \mu_a \circ e^{-1}$ equals multiplication by $a$ on $\mathfrak{m}^i/\mathfrak{m}^{i+1}$,
viewed as a $K$-linear map.

Formalized by `IsDiscreteValuationRing.residueFieldLinearEquivMaximalIdealGradedPiece_conj_lmul`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-linear-equiv-maximal-ideal-2).

## Trace of multiplication on a graded piece

Let $R$ be a discrete valuation ring with
maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$, let $i \in \mathbb{N}$,
and let $K$ be a field, with a $K$-algebra structure on $\kappa$ and a $K$-module structure on
$\mathfrak{m}^i/\mathfrak{m}^{i+1}$ such that $(c b) x = c (b x)$ for all $c \in K$,
$b \in \kappa$ and $x \in \mathfrak{m}^i/\mathfrak{m}^{i+1}$. Then for every $a \in \kappa$, the
trace of multiplication by $a$ on $\mathfrak{m}^i/\mathfrak{m}^{i+1}$, as a $K$-linear map,
equals the trace $\operatorname{Tr}_{\kappa/K}(a)$.

Each trace is taken to be $0$ when the corresponding space is not finite-dimensional over $K$.

Formalized by `IsDiscreteValuationRing.trace_residueFieldMulMaximalIdealGradedPiece`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealGradedPieceMul.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#trace-residue-field-mul-maximal-ideal-gr).

## Quotient by the extended maximal ideal plus a maximal-ideal power

Let $A$ and $B$ be
discrete valuation rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an
$A$-algebra, and write $\mathfrak m_A B$ for the ideal of $B$ generated by the image of
$\mathfrak m_A$. For a natural number $n$, this is the quotient ring
$B / (\mathfrak m_A B + \mathfrak m_B^n)$.

Formalized by `ResidueFieldMaximalIdealPowQuotient`, an abbreviation declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-maximal-ideal-pow-quotient).

## Collapse of the quotient-defining ideal

Let $A$ and $B$ be discrete valuation rings with
maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an $A$-algebra, and write
$\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$. For every
natural number $n$, if $\mathfrak m_A B \subseteq \mathfrak m_B^n$, then
$\mathfrak m_A B + \mathfrak m_B^n = \mathfrak m_B^n$.

Formalized by `maximalIdealPowQuotientIdeal_eq`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#maximal-ideal-pow-quotient-ideal-eq).

## The quotient-defining ideals decrease

Let $A$ and $B$ be discrete valuation rings with
maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an $A$-algebra, and write
$\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$. For every
natural number $n$, the ideal $\mathfrak m_A B + \mathfrak m_B^{n+1}$ is contained in
$\mathfrak m_A B + \mathfrak m_B^n$.

Formalized by `maximalIdealPowQuotientIdeal_le`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#maximal-ideal-pow-quotient-ideal-le).

## Transition map between maximal-ideal-power quotients

Let $A$ and $B$ be discrete
valuation rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$ and let
$\kappa_A = A/\mathfrak m_A$ be the residue field of $A$. Let $B$ be an $A$-algebra, write
$\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$, and for each $m$
let $Q_m = B/(\mathfrak m_A B + \mathfrak m_B^m)$, a $\kappa_A$-algebra in which the class of
$r \in A$ acts as multiplication by the class of its image in $B$. For a natural number $n$,
this is the $\kappa_A$-algebra homomorphism $Q_{n+1} \to Q_n$ sending the class of each
$b \in B$ to its class in $Q_n$; it is well defined because
$\mathfrak m_A B + \mathfrak m_B^{n+1} \subseteq \mathfrak m_A B + \mathfrak m_B^n$.

Formalized by `factorResidueFieldMaximalIdealPowQuotient`, a definition declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#factor-residue-field-maximal-ideal-pow-q).

## Surjectivity of the transition maps between maximal-ideal-power quotients

Let $A$ and
$B$ be discrete valuation rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$
be an $A$-algebra, write $\mathfrak m_A B$ for the ideal of $B$ generated by the image of
$\mathfrak m_A$, and for each $m$ let $Q_m = B/(\mathfrak m_A B + \mathfrak m_B^m)$. For every
natural number $n$, the transition homomorphism $Q_{n+1} \to Q_n$ that sends the class of each
$b \in B$ to its class in $Q_n$ is surjective.

Formalized by `factorResidueFieldMaximalIdealPowQuotient_surjective`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#factor-residue-field-maximal-ideal-pow-q-2).

## The transition map on residue classes

Let $A$ and $B$ be discrete valuation rings with
maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an $A$-algebra, write
$\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$, and for each $m$
let $Q_m = B/(\mathfrak m_A B + \mathfrak m_B^m)$. For every natural number $n$ and every
$b \in B$, the transition homomorphism $Q_{n+1} \to Q_n$ maps the class of $b$ in $Q_{n+1}$ to
the class of $b$ in $Q_n$.

Formalized by `factorResidueFieldMaximalIdealPowQuotient_mk`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#factor-residue-field-maximal-ideal-pow-q-3).

## Ring isomorphism with the quotient by a power of the maximal ideal

Let $A$ and $B$ be
discrete valuation rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an
$A$-algebra, and write $\mathfrak m_A B$ for the ideal of $B$ generated by the image of
$\mathfrak m_A$. For a natural number $n$ with $\mathfrak m_A B \subseteq \mathfrak m_B^n$, this
is the ring isomorphism $B/(\mathfrak m_A B + \mathfrak m_B^n) \cong B/\mathfrak m_B^n$ sending
the class of each $b \in B$ to the class of $b$; it exists because the two ideals are equal.

Formalized by `residueFieldMaximalIdealPowQuotientEquivPow`, a definition declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-maximal-ideal-pow-quotient-2).

## The power-quotient isomorphism on residue classes

Let $A$ and $B$ be discrete valuation
rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, let $B$ be an $A$-algebra, and
write $\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$. For every
natural number $n$ with $\mathfrak m_A B \subseteq \mathfrak m_B^n$ and every $b \in B$, the ring
isomorphism $B/(\mathfrak m_A B + \mathfrak m_B^n) \cong B/\mathfrak m_B^n$ induced by the
equality of these two ideals sends the class of $b$ to the class of $b$.

Formalized by `residueFieldMaximalIdealPowQuotientEquivPow_mk`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-maximal-ideal-pow-quotient-3).

## Graded pieces as kernels of the transition maps

Let $A$ and $B$ be discrete valuation
rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$ and residue fields
$\kappa_A = A/\mathfrak m_A$ and $\kappa_B = B/\mathfrak m_B$, let $B$ be an $A$-algebra whose
algebra map $A \to B$ is a local homomorphism, so that it induces a field homomorphism
$\kappa_A \to \kappa_B$, and write $\mathfrak m_A B$ for the ideal of $B$ generated by the image
of $\mathfrak m_A$. For each $m$ let $Q_m = B/(\mathfrak m_A B + \mathfrak m_B^m)$, a
$\kappa_A$-algebra in which the class of $r \in A$ acts as multiplication by the class of its
image in $B$. Let $n$ be a natural number with $\mathfrak m_A B \subseteq \mathfrak m_B^{n+1}$,
and suppose the $\kappa_B$-vector space $\mathfrak m_B^n/\mathfrak m_B^{n+1}$ carries a
$\kappa_A$-module structure such that $(\bar a c) \cdot x = a \cdot (c \cdot x)$ for all
$a \in \kappa_A$, $c \in \kappa_B$ and $x \in \mathfrak m_B^n/\mathfrak m_B^{n+1}$, where $\bar a$
is the image of $a$ in $\kappa_B$. This is the $\kappa_A$-linear isomorphism from
$\mathfrak m_B^n/\mathfrak m_B^{n+1}$ onto the kernel of the $\kappa_A$-algebra homomorphism
$Q_{n+1} \to Q_n$ that sends the class of each $b \in B$ to its class in $Q_n$; it sends the
class of each $z \in \mathfrak m_B^n$ to the class of $z$ in $Q_{n+1}$.

Formalized by `residueFieldLinearEquivMaximalIdealGradedPieceKerFactor`, a definition declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-linear-equiv-maximal-ideal-3).

## The kernel identification on representatives

Let $A$ and $B$ be discrete valuation
rings with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$ and residue fields
$\kappa_A = A/\mathfrak m_A$ and $\kappa_B = B/\mathfrak m_B$, let $B$ be an $A$-algebra whose
algebra map $A \to B$ is a local homomorphism, so that it induces a field homomorphism
$\kappa_A \to \kappa_B$, and write $\mathfrak m_A B$ for the ideal of $B$ generated by the image
of $\mathfrak m_A$. For each $m$ let $Q_m = B/(\mathfrak m_A B + \mathfrak m_B^m)$, a
$\kappa_A$-algebra in which the class of $r \in A$ acts as multiplication by the class of its
image in $B$. Let $n$ be a natural number with $\mathfrak m_A B \subseteq \mathfrak m_B^{n+1}$,
and suppose the $\kappa_B$-vector space $\mathfrak m_B^n/\mathfrak m_B^{n+1}$ carries a
$\kappa_A$-module structure such that $(\bar a c) \cdot x = a \cdot (c \cdot x)$ for all
$a \in \kappa_A$, $c \in \kappa_B$ and $x \in \mathfrak m_B^n/\mathfrak m_B^{n+1}$, where $\bar a$
is the image of $a$ in $\kappa_B$. Let $\pi \colon Q_{n+1} \to Q_n$ be the $\kappa_A$-algebra
homomorphism sending the class of each $b \in B$ to its class in $Q_n$. Then for every
$z \in \mathfrak m_B^n$, the $\kappa_A$-linear isomorphism from
$\mathfrak m_B^n/\mathfrak m_B^{n+1}$ onto $\ker \pi$ sends the class of $z$ to the class of $z$ in
$Q_{n+1}$.

Formalized by `residueFieldLinearEquivMaximalIdealGradedPieceKerFactor_mk`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowFactor.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-field-linear-equiv-maximal-ideal-4).

## One-step trace recurrence for the maximal-ideal-power quotients

Let $A$ and $B$ be
discrete valuation rings with maximal ideals $\mathfrak m_A$, $\mathfrak m_B$ and residue fields
$\kappa_A$, $\kappa_B$, and let $B$ be an $A$-algebra whose structure map is a local
homomorphism. Write $\mathfrak m_A B$ for the ideal of $B$ generated by the image of
$\mathfrak m_A$, and for each $m$ let $Q_m = B / (\mathfrak m_A B + \mathfrak m_B^m)$, a
$\kappa_A$-algebra. Let $n$ be a natural number with
$\mathfrak m_A B \subseteq \mathfrak m_B^{n+1}$, suppose $Q_{n+1}$ is finite-dimensional over
$\kappa_A$, and equip the graded piece $\mathfrak m_B^n / \mathfrak m_B^{n+1}$ with a
$\kappa_A$-module structure compatible with its $\kappa_B$-module structure through
$\kappa_A \to \kappa_B$. Then for every $b \in B$, writing $\bar b$ for the residue of $b$ in
$\kappa_B$, the trace over $\kappa_A$ of multiplication by the class of $b$ on $Q_{n+1}$ equals
$\operatorname{Tr}_{\kappa_B/\kappa_A}(\bar b)$ plus the trace over $\kappa_A$ of multiplication
by the class of $b$ on $Q_n$.

Formalized by `trace_residueFieldMaximalIdealPowQuotient_succ`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#trace-residue-field-maximal-ideal-pow-qu).

## Trace on the maximal-ideal-power quotients

Let $A$ and $B$ be discrete valuation rings
with maximal ideals $\mathfrak m_A$, $\mathfrak m_B$ and residue fields $\kappa_A$, $\kappa_B$,
and let $B$ be an $A$-algebra whose structure map is a local homomorphism. Write
$\mathfrak m_A B$ for the ideal of $B$ generated by the image of $\mathfrak m_A$. Let $n$ be a
natural number with $\mathfrak m_A B \subseteq \mathfrak m_B^n$, and suppose the $\kappa_A$-algebra
$Q_n = B / (\mathfrak m_A B + \mathfrak m_B^n)$ is finite-dimensional over $\kappa_A$. Then for
every $b \in B$, writing $\bar b$ for the residue of $b$ in $\kappa_B$, the trace over
$\kappa_A$ of multiplication by the class of $b$ on $Q_n$ equals
$n \cdot \operatorname{Tr}_{\kappa_B/\kappa_A}(\bar b)$.

Formalized by `trace_residueFieldMaximalIdealPowQuotient`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#trace-residue-field-maximal-ideal-pow-qu-2).

## Residue of the integral trace

Let $A$ and $B$ be discrete valuation rings with maximal
ideals $\mathfrak m_A$, $\mathfrak m_B$ and residue fields $\kappa_A$, $\kappa_B$, and let $B$
be an $A$-algebra that is finitely generated and torsion-free as an $A$-module. Let $e$ be a
natural number such that the ideal $\mathfrak m_A B$ generated by the image of $\mathfrak m_A$
equals $\mathfrak m_B^e$. Then for every $b \in B$, writing $\bar b$ for the residue of $b$ in
$\kappa_B$, the residue in $\kappa_A$ of the integral trace $\operatorname{Tr}_{B/A}(b)$ (the
trace of the extension of fraction fields, restricted to $B$) equals
$e \cdot \operatorname{Tr}_{\kappa_B/\kappa_A}(\bar b)$.

This determines the integral trace only modulo $\mathfrak m_A$.

Formalized by `residue_intTrace_eq_nsmul_trace_residue_of_map_maximalIdeal_eq_pow`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#residue-int-trace-eq-nsmul-trace-residue).

## Tame extensions have surjective integral trace

Let $A$ and $B$ be discrete valuation
rings with maximal ideals $\mathfrak m_A$, $\mathfrak m_B$ and residue fields $\kappa_A$,
$\kappa_B$, and let $B$ be an $A$-algebra that is finitely generated and torsion-free as an
$A$-module, with $\kappa_B / \kappa_A$ separable. Let $e$ be a natural number that is a unit
in $B$ and such that the ideal $\mathfrak m_A B$ generated by the image of $\mathfrak m_A$
equals $\mathfrak m_B^e$. Then the integral trace $\operatorname{Tr}_{B/A} \colon B \to A$
(the trace of the extension of fraction fields, restricted to $B$) is surjective.

Since $A \to B$ is local, $e$ is a unit in $B$ if and only if it is a unit in $A$.

Formalized by `intTrace_surjective_of_isUnit_natCast_of_map_maximalIdeal_eq_pow`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/MaximalIdealPowQuotientTrace.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#int-trace-surjective-of-is-unit-nat-cast).

## Different ideal of a tamely ramified extension of DVRs

Let $A$ and $B$ be discrete
valuation rings with maximal ideals $\mathfrak{m}_A$ and $\mathfrak{m}_B$, and let $B$ be an
$A$-algebra that is finite and torsion-free as an $A$-module, such that the extension of
fraction fields and the extension of residue fields are both separable. Let $e$ be a natural
number whose image in $B$ is a unit, and suppose that the ideal of $B$ generated by the image of
$\mathfrak{m}_A$ equals $\mathfrak{m}_B^e$. Then the different ideal of $B$ over $A$ equals
$\mathfrak{m}_B^{e-1}$.

Without the tameness hypothesis that $e$ is a unit in $B$, this equality fails in general.

Formalized by `differentIdeal_eq_maximalIdeal_pow_sub_one_of_isUnit_natCast`, a theorem declared in [MathlibExt/RingTheory/DiscreteValuationRing/TameDifferent.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DiscreteValuationRing/TameDifferent.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html#different-ideal-eq-maximal-ideal-pow-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tame ramification and the different](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/tame-ramification-and-the-different/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/tame-ramification-and-the-different)
