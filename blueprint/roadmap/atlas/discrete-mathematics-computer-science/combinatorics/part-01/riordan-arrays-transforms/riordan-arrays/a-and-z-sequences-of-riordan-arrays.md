---
declaration: section
origin: cited
lean: MetaMathlibExt.riordan_iff_AZ_sequences, MetaMathlibExt.riordan_array_inverse_via_a_and_z_sequences_general, MetaMathlibExt.riordan_array_inverse_via_a_and_z_sequences
statement: formalized
proof: formalized
---

# A- and Z-sequences of Riordan arrays

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays/index.html).

## A- and Z-sequence characterization of integer Riordan arrays

Let $(d_{n,k})_{n,k \ge 0}$ be
an integer matrix that is lower triangular, that is, $d_{n,k} = 0$ whenever $n < k$. Then the
following are equivalent: (i) there are power series $g, f \in \mathbb{Z}[[x]]$ with $g(0) = 1$,
$f(0) = 0$ and $[x^1]\, f \ne 0$ such that $d_{n,k} = [x^n]\, g f^k$ for all $n, k \ge 0$;
(ii) $d_{0,0} = 1$ and there are rational sequences $(A_j)_{j \ge 0}$ and $(Z_j)_{j \ge 0}$ with
$A_0 \ne 0$ such that, for all $n, k \ge 0$,

$$d_{n+1,k+1} = \sum_{j=0}^{n} A_j\, d_{n,k+j} \quad\text{and}\quad
d_{n+1,0} = \sum_{j=0}^{n} Z_j\, d_{n,j}.$$

The sequences are rational because $A_0 = [x^1]\, f$ need not be a unit in $\mathbb{Z}$.

Correction to the cited source: Barry's Proposition displays the hypothesis $Z_0 \ne 0$, but the
identity Riordan array has $Z_0 = 0$, so that condition cannot hold in general. This statement
therefore drops $Z_0 \ne 0$ — a deliberate correction to the source, not just a normalization —
and instead imposes the Riordan normalization $d_{0,0} = 1$.

Proof: The forward implication uses coefficientwise triangular expansions in powers of $f$; the
converse reconstructs $g$ and $f$ from columns zero and one and proves rowwise uniqueness. This is
the route of Barry's Proposition Char following He and Sprugnoli's Theorems 2.1 and 2.2.

## Sources

- P. Barry, *A Note on a Family of Generalized Pascal Matrices Defined by Riordan Arrays*, Journal of Integer Sequences 16 (2013), Article 13.5.4, Proposition Char, lines 173-180, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Barry2/barry231.tex>, after Theorems 2.1 and 2.2 of He.

Formalized by `MetaMathlibExt.riordan_iff_AZ_sequences`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RiordanAZSequences.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RiordanAZSequences.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays/index.html#riordan-iff-az-sequences).

## Inverse of a Riordan array from its A- and Z-sequences (one-sided form)

Let $K$ be a
field, let $g, f, A, Z, \bar f$ be formal power series over $K$, and let $d_{00} \in K$ with
$d_{00} \ne 0$. Suppose that $g(0) = d_{00}$, $f(0) = 0$, $A(0) \ne 0$, $\bar f(0) = 0$,
$f(\bar f(x)) = x$, $f(x) = x\, A(f(x))$ and $g(x) = d_{00} \bigl(1 - x\, Z(f(x))\bigr)^{-1}$.
Then

$$\left(\frac{1}{g(\bar f(x))},\ \bar f(x)\right) =
\left(\frac{A(x) - x\, Z(x)}{d_{00}\, A(x)},\ \frac{x}{A(x)}\right).$$

Here $A$ and $Z$ are the generating functions of the A- and Z-sequences of the Riordan array
$(g, f)$, and the pair on the left is its inverse. Only $f(\bar f(x)) = x$ is assumed, not also
$\bar f(f(x)) = x$.

Formalized by `MetaMathlibExt.riordan_array_inverse_via_a_and_z_sequences_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RiordanArrayInverse.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RiordanArrayInverse.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays/index.html#riordan-array-inverse-via-a-and-z-sequen).

## Inverse of a Riordan array from its A- and Z-sequences

Let $K$ be a field, let
$g, f, A, Z, \bar f$ be formal power series over $K$, and let $d_{00} \in K$ with $d_{00} \ne 0$.
Suppose that $g(0) = d_{00}$, $f(0) = 0$, $A(0) \ne 0$ and $\bar f(0) = 0$; that
$f(\bar f(x)) = x$ and $\bar f(f(x)) = x$, so that $\bar f$ is the compositional inverse of $f$;
that $f(x) = x\, A(f(x))$, so that $A$ is the generating function of the A-sequence; and that
$g(x) = d_{00} \bigl(1 - x\, Z(f(x))\bigr)^{-1}$, so that $Z$ is the generating function of the
Z-sequence. Then

$$\left(\frac{1}{g(\bar f(x))},\ \bar f(x)\right) =
\left(\frac{A(x) - x\, Z(x)}{d_{00}\, A(x)},\ \frac{x}{A(x)}\right).$$

The pair on the left is the inverse of the Riordan array $(g, f)$. The hypothesis
$\bar f(f(x)) = x$ is not needed for the conclusion; it is kept to match the source.

## Sources

- Paul Barry and Aoife Hennessy, "Meixner-Type Results for Riordan Arrays and Associated Integer Sequences," Journal of Integer Sequences 13 (2010), Article 10.9.4, Lemma, lines 280-283, <https://cs.uwaterloo.ca/journals/JIS/VOL13/Barry5/barry96s.tex>. The paper attributes this formula to Luzon.

Formalized by `MetaMathlibExt.riordan_array_inverse_via_a_and_z_sequences`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RiordanArrayInverse.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RiordanArrayInverse.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays/index.html#riordan-array-inverse-via-a-and-z-sequen-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A- and Z-sequences of Riordan arrays](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/a-and-z-sequences-of-riordan-arrays)
